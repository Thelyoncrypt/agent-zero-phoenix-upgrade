# python/tools/memory_agent_tool.py
from python.helpers.tool import Tool, Response as ToolResponse
from typing import Dict, Any, List, Optional
import json
from pathlib import Path

# Import StreamProtocol components if available
try:
    from python.tools.stream_protocol_tool import StreamEventType
    STREAM_PROTOCOL_AVAILABLE = True
except ImportError:
    STREAM_PROTOCOL_AVAILABLE = False
    StreamEventType = None

# Import memory agent components
from python.agents.memory_agent.memory import Mem0MemorySystem # Import the real wrapper
import json # For formatting results if needed

class MemoryAgentTool(Tool):
    """
    MemoryAgent (Mem0 inspired) integration for Agent Zero.
    Provides intelligent, self-improving memory capabilities.
    """
    
    def __init__(self, agent, **kwargs):
        super().__init__(
            agent=agent,
            name="memory_agent_tool",
            description="Manages an intelligent memory system, allowing adding, searching, updating, and deleting memories.",
            args_schema={
                "type": "object",
                "properties": {
                    "action": {
                        "type": "string",
                        "enum": ["add", "search", "update", "delete", "get_all", "add_triplets", "search_graph", "summarize_memory", "track_conversation"],
                        "description": "Type of memory operation to perform"
                    },
                    "user_id": {
                        "type": "string",
                        "description": "Identifier for the user whose memory is being accessed (optional)"
                    },
                    "messages": {
                        "type": "array",
                        "items": {"type": "object"},
                        "description": "List of messages to extract memories from (for add action)"
                    },
                    "data": {
                        "description": "Generic data to store as a memory (for add action)"
                    },
                    "memory_id": {
                        "type": "string",
                        "description": "Specific ID for memory operations"
                    },
                    "query": {
                        "type": "string",
                        "description": "Search query (for search action)"
                    },
                    "limit": {
                        "type": "integer",
                        "description": "Maximum number of results to return (default: 5)"
                    },
                    "triplets": {
                        "type": "array",
                        "items": {"type": "object"},
                        "description": "List of KG triplets for add_triplets action. Each dict: {\"head\": str, \"relation\": str, \"tail\": str, \"properties\": Optional[dict]}"
                    },
                    "entity": {
                        "type": "string",
                        "description": "Entity to search for in graph (for search_graph action)"
                    },
                    "relation": {
                        "type": "string",
                        "description": "Relation type to filter by in graph search (for search_graph action)"
                    },
                    "target": {
                        "type": "string",
                        "description": "Target entity for graph search (for search_graph action)"
                    },
                    "query_for_context": {
                        "type": "string",
                        "description": "Query to find relevant memories to summarize collectively (for summarize_memory action)"
                    },
                    "summary_instruction": {
                        "type": "string",
                        "description": "Specific instruction for how to summarize (e.g., 'Summarize as bullet points', 'Extract key dates'). Defaults to 'Provide a concise summary.' (for summarize_memory action)"
                    },
                    "conversation_messages": {
                        "type": "array",
                        "items": {"type": "object"},
                        "description": "List of conversation messages for track_conversation action. Each dict: {\"role\": str, \"content\": str, \"timestamp\": Optional[str]}"
                    },
                    "conversation_id": {
                        "type": "string",
                        "description": "Unique identifier for the conversation (for track_conversation action)"
                    },
                    "conversation_metadata": {
                        "type": "object",
                        "description": "Additional metadata for the conversation (for track_conversation action)"
                    }
                },
                "required": ["action"]
            },
            **kwargs
        )
        # Initialize the real Mem0MemorySystem
        agent_id_for_mem0 = self.agent.get_user_id() or self.agent.get_thread_id() or "agent0_default_user"

        # Get persistence directory from agent config or use a default
        # Agent Zero stores memory in "memory/{ctxid}/..."
        # We can adopt a similar structure for mem0 data.
        default_persistence_base_dir = Path(self.agent.context.get_custom_data("base_dir", ".")) / "memory" / "mem0_data"
        mem0_config = getattr(self.agent, 'config', {}).get("mem0_config", {})
        persistence_dir_for_agent = mem0_config.get("persistence_dir_base", str(default_persistence_base_dir))

        # mem0 config can be passed here if needed. For now, rely on defaults.
        # Example: config = {"llm": {"provider": "openai", "config": {"model": "gpt-4o-mini"}}}
        self.memory_system = Mem0MemorySystem(
            agent_id=agent_id_for_mem0,
            config=mem0_config.get("client_config"), # Pass specific client config to mem0
            persistence_dir=persistence_dir_for_agent # Pass full path including agent_id subdir
        )

        print(f"MemoryAgentTool initialized for agent {agent.agent_name} (context: {agent.context.id}) "
              f"with Mem0MemorySystem (agent_id_scope: {self.memory_system.agent_id}), "
              f"persistence at: {self.memory_system.persistence_dir}")

    async def _emit_memory_event(self, action_name: str, status: str, details: Optional[Dict[str, Any]] = None):
        payload = {"source_tool": "memory_agent", "action": action_name, "status": status}
        if details: payload.update(details)
        if hasattr(self.agent, '_emit_stream_event'):
             await self.agent._emit_stream_event(StreamEventType.MEMORY_UPDATE, payload)
        else:
            print(f"MemoryAgentTool: Agent does not have _emit_stream_event. Cannot emit MEMORY_UPDATE.")

    async def execute(self, **kwargs) -> ToolResponse:
        """
        Execute MemoryAgent operations.
        
        Args:
            action (str): Memory operation (e.g., "add", "search", "update", "delete", "get_all").
            **kwargs: Arguments for the action.
        """
        action = kwargs.get("action")
        if not action:
            return ToolResponse(
                success=False,
                error="Missing required 'action' parameter",
                message="Error: 'action' is required for MemoryAgent operations."
            )
            
        user_id_arg = kwargs.get("user_id") # User ID passed in tool args
        # If no user_id in args, use the memory_system's configured agent_id (which might be from agent context)
        # This is important because Mem0 operations are typically user-scoped.
        # The self.memory_system was initialized with an agent_id.

        try:
            if action == "add":
                messages = kwargs.get("messages")
                data_to_add = kwargs.get("data")
                memory_id_arg = kwargs.get("memory_id")
                metadata_arg = kwargs.get("metadata")

                if messages and isinstance(messages, list):
                    # IntelligentMemory.add_messages internally uses user_id/agent_id for scoping
                    return await self._add_from_messages(messages, user_id_arg) # Pass user_id_arg for clarity
                elif data_to_add is not None: # Check for not None, as data could be False, 0, etc.
                    return await self._add_generic_memory(data_to_add, memory_id_arg, user_id_arg, metadata_arg)
                else:
                    return ToolResponse(success=False, message="Error: 'messages' or 'data' required for 'add'.", error="Missing required parameters")

            elif action == "search":
                query = kwargs.get("query")
                limit = kwargs.get("limit", 5)
                if not query:
                    return ToolResponse(success=False, message="Error: 'query' is required for search.", error="Missing query parameter")
                return await self._search_memory(query, user_id_arg, limit)
            
            elif action == "update":
                memory_id = kwargs.get("memory_id")
                new_data = kwargs.get("data")
                new_metadata = kwargs.get("metadata")
                if not memory_id or new_data is None:
                    return ToolResponse(success=False, message="Error: 'memory_id' and 'data' are required for update.", error="Missing required parameters")
                return await self._update_memory(memory_id, new_data, user_id_arg, new_metadata)

            elif action == "delete":
                memory_id = kwargs.get("memory_id")
                if not memory_id:
                    return ToolResponse(success=False, message="Error: 'memory_id' is required for delete.", error="Missing memory_id parameter")
                return await self._delete_memory(memory_id, user_id_arg)

            elif action == "get_all":
                return await self._get_all_memories(user_id_arg)

            # New Graph Actions
            elif action == "add_triplets":
                triplets = kwargs.get("triplets") # List of {"head": "...", "relation": "...", "tail": "..."}
                if not triplets or not isinstance(triplets, list):
                    return ToolResponse(success=False, message="Error: 'triplets' (list of dicts) is required for add_triplets.", error="Missing triplets parameter")
                return await self._add_triplets(triplets, user_id_arg)

            elif action == "search_graph":
                query_entity = kwargs.get("entity")
                relation_type = kwargs.get("relation")
                target_entity = kwargs.get("target") # Name consistent with search_knowledge_graph
                limit = kwargs.get("limit", 10)
                if not query_entity and not relation_type and not target_entity:
                    return ToolResponse(success=False, message="Error: At least one of 'entity', 'relation', or 'target' must be provided for search_graph.", error="Missing search parameters")
                return await self._search_graph(query_entity, relation_type, target_entity, user_id_arg, limit)

            # New Action for Summarization
            elif action == "summarize_memory":
                memory_id_arg = kwargs.get("memory_id")
                query_for_context_arg = kwargs.get("query_for_context")
                summary_instruction_arg = kwargs.get("summary_instruction", "Provide a concise summary.") # New optional param
                if not memory_id_arg and not query_for_context_arg:
                    return ToolResponse(success=False, message="Error: 'memory_id' or 'query_for_context' is required for summarize_memory.", error="Missing summarization parameters")
                return await self._summarize_memory(memory_id_arg, query_for_context_arg, user_id_arg, summary_instruction_arg)

            # New Action for Conversation Tracking
            elif action == "track_conversation":
                conversation_messages = kwargs.get("conversation_messages")
                conversation_id = kwargs.get("conversation_id")
                conversation_metadata = kwargs.get("conversation_metadata", {})
                if not conversation_messages or not isinstance(conversation_messages, list):
                    return ToolResponse(success=False, message="Error: 'conversation_messages' (list of dicts) is required for track_conversation.", error="Missing conversation messages")
                if not conversation_id:
                    return ToolResponse(success=False, message="Error: 'conversation_id' is required for track_conversation.", error="Missing conversation ID")
                return await self._track_conversation(conversation_messages, conversation_id, conversation_metadata, user_id_arg)

            else:
                return ToolResponse(success=False, message=f"Unknown MemoryAgent action: {action}", error=f"Unknown action: {action}")

        except Exception as e:
            import traceback
            error_message = f"MemoryAgentTool error during action '{action}': {str(e)}"
            print(f"{error_message}\n{traceback.format_exc()}")
            await self._emit_memory_event(action, "error", {"error": str(e), "user_id": user_id_arg})
            return ToolResponse(success=False, message=error_message, error=str(e))

    async def _add_from_messages(self, messages: List[Dict[str, Any]], user_id: Optional[str]) -> ToolResponse:
        await self._emit_memory_event("add_messages", "starting", {"count": len(messages), "user_id": user_id})
        stored_ids = await self.memory_system.add_messages(messages, user_id_override=user_id)
        result_details = {"stored_ids": stored_ids, "user_id": user_id, "processed_messages": len(messages)}
        await self._emit_memory_event("add_messages", "completed", result_details)
        return ToolResponse(success=True, message=f"Added {len(stored_ids)} memories from messages.", data=result_details)

    async def _add_generic_memory(self, data: Any, memory_id: Optional[str], user_id: Optional[str], metadata: Optional[Dict] = None) -> ToolResponse:
        await self._emit_memory_event("add_generic", "starting", {"has_id": bool(memory_id), "user_id": user_id})
        stored_id = await self.memory_system.add_generic_memory(data, memory_id=memory_id, user_id_override=user_id, metadata=metadata)
        result_details = {"stored_id": stored_id, "user_id": user_id}
        await self._emit_memory_event("add_generic", "completed", result_details)
        return ToolResponse(success=True, message=f"Memory added with ID: {stored_id}", data=result_details)

    async def _search_memory(self, query: str, user_id: Optional[str], limit: int) -> ToolResponse:
        await self._emit_memory_event("search", "processing", {"query": query, "limit": limit, "user_id": user_id})
        results = await self.memory_system.search(query, user_id_override=user_id, limit=limit)
        await self._emit_memory_event("search", "completed", {"query": query, "results_count": len(results), "user_id": user_id})
        return ToolResponse(success=True, message=json.dumps(results), data={"results": results})

    async def _update_memory(self, memory_id: str, new_data: Any, user_id: Optional[str], new_metadata: Optional[Dict] = None) -> ToolResponse:
        await self._emit_memory_event("update", "processing", {"memory_id": memory_id, "user_id": user_id})
        success = await self.memory_system.update(memory_id, new_data, user_id_override=user_id, new_metadata=new_metadata)
        status = "completed" if success else "failed"
        await self._emit_memory_event("update", status, {"memory_id": memory_id, "success": success, "user_id": user_id})
        return ToolResponse(success=success, message=f"Memory update {status}.", data={"success": success})

    async def _delete_memory(self, memory_id: str, user_id: Optional[str]) -> ToolResponse:
        await self._emit_memory_event("delete", "processing", {"memory_id": memory_id, "user_id": user_id})
        success = await self.memory_system.delete(memory_id, user_id_override=user_id)
        status = "completed" if success else "failed"
        await self._emit_memory_event("delete", status, {"memory_id": memory_id, "success": success, "user_id": user_id})
        return ToolResponse(success=success, message=f"Memory deletion {status}.", data={"success": success})

    async def _get_all_memories(self, user_id: Optional[str]) -> ToolResponse:
        await self._emit_memory_event("get_all", "processing", {"user_id": user_id})
        all_memories = await self.memory_system.get_all(user_id_override=user_id)
        await self._emit_memory_event("get_all", "completed", {"count": len(all_memories), "user_id": user_id})
        return ToolResponse(success=True, message=json.dumps(all_memories), data={"memories": all_memories})

    # New private helper methods for graph operations
    async def _add_triplets(self, triplets: List[Dict[str, Any]], user_id_for_op: Optional[str]) -> ToolResponse:
        await self._emit_memory_event("add_triplets", "starting", {"triplet_count": len(triplets), "user_id": user_id_for_op})
        result = await self.memory_system.add_knowledge_graph_triplets(triplets, user_id_override=user_id_for_op)
        status = "completed" if result.get("status") == "success" else "failed"
        await self._emit_memory_event("add_triplets", status, {**result, "user_id": user_id_for_op})
        return ToolResponse(success=(status=="completed"), message=f"Add triplets {status}. Added: {result.get('triplets_added', 0)}", data=result)

    async def _search_graph(self, query_entity: Optional[str], relation_type: Optional[str],
                            target_entity: Optional[str], user_id_for_op: Optional[str], limit: int) -> ToolResponse:
        query_details = {"entity": query_entity, "relation": relation_type, "target": target_entity, "limit": limit, "user_id": user_id_for_op}
        await self._emit_memory_event("search_graph", "processing", query_details)
        results = await self.memory_system.search_knowledge_graph(
            query_entity, relation_type, target_entity, user_id_override=user_id_for_op, limit=limit
        )
        await self._emit_memory_event("search_graph", "completed", {"query": query_details, "results_count": len(results)})
        return ToolResponse(success=True, message=json.dumps(results), data={"results": results})

    # New private helper method for summarization
    async def _summarize_memory(self, memory_id: Optional[str], query_for_context: Optional[str],
                               user_id_for_op: Optional[str], summary_instruction: str) -> ToolResponse:
        details_for_event = {"user_id": user_id_for_op, "instruction": summary_instruction}
        if memory_id: details_for_event["memory_id"] = memory_id
        if query_for_context: details_for_event["query_for_context"] = query_for_context

        await self._emit_memory_event("summarize_memory", "processing", details_for_event)

        summary = await self.memory_system.summarize_memory_content(
            memory_id=memory_id,
            query_for_context=query_for_context,
            user_id_override=user_id_for_op,
            summary_instruction=summary_instruction
        )

        # Check if summary was successful
        if summary and "Could not generate summary" not in summary and "not found" not in summary and "service not available" not in summary and "not configured" not in summary:
            status = "completed"
            response_message = "Memory summarized successfully."
        else:
            status = "failed"
            response_message = summary or "Failed to generate summary."

        await self._emit_memory_event("summarize_memory", status, {**details_for_event, "summary_present": bool(summary and status=='completed')})
        return ToolResponse(success=(status=="completed"), message=response_message, data={"summary": summary} if status == "completed" else None, error=(status=="failed"))

    # New private helper method for conversation tracking
    async def _track_conversation(self, conversation_messages: List[Dict[str, Any]],
                                 conversation_id: str, conversation_metadata: Dict[str, Any],
                                 user_id_for_op: Optional[str]) -> ToolResponse:
        """
        Tracks conversation history by storing messages and extracting insights.
        """
        details_for_event = {
            "user_id": user_id_for_op,
            "conversation_id": conversation_id,
            "message_count": len(conversation_messages)
        }

        await self._emit_memory_event("track_conversation", "processing", details_for_event)

        try:
            # Process conversation messages and extract insights
            processed_memories = []

            # 1. Store individual messages as memories
            for i, message in enumerate(conversation_messages):
                if not isinstance(message, dict) or not message.get("content"):
                    continue

                role = message.get("role", "unknown")
                content = message.get("content", "")
                timestamp = message.get("timestamp", "")

                # Create a structured memory entry for each message
                message_memory = {
                    "conversation_id": conversation_id,
                    "message_index": i,
                    "role": role,
                    "content": content,
                    "timestamp": timestamp,
                    **conversation_metadata
                }

                # Add the message as a memory
                memory_text = f"[Conversation {conversation_id}] {role}: {content}"
                add_result = await self.memory_system.add_messages(
                    [{"role": "user", "content": memory_text}],
                    user_id_override=user_id_for_op
                )

                if add_result:
                    processed_memories.extend(add_result)

            # 2. Extract conversation insights and patterns
            conversation_summary = await self._extract_conversation_insights(
                conversation_messages, conversation_id, user_id_for_op
            )

            # 3. Store conversation-level insights
            if conversation_summary:
                insights_text = f"[Conversation {conversation_id} Summary] {conversation_summary}"
                summary_result = await self.memory_system.add_messages(
                    [{"role": "assistant", "content": insights_text}],
                    user_id_override=user_id_for_op
                )
                if summary_result:
                    processed_memories.extend(summary_result)

            # 4. Create knowledge graph triplets from conversation
            triplets = await self._extract_conversation_triplets(
                conversation_messages, conversation_id, user_id_for_op
            )

            triplets_added = 0
            if triplets:
                triplet_result = await self.memory_system.add_knowledge_graph_triplets(
                    triplets, user_id_override=user_id_for_op
                )
                triplets_added = triplet_result.get("triplets_added", 0)

            result_data = {
                "conversation_id": conversation_id,
                "messages_processed": len([m for m in conversation_messages if m.get("content")]),
                "memories_created": len(processed_memories),
                "triplets_added": triplets_added,
                "conversation_summary": conversation_summary,
                "memory_ids": processed_memories
            }

            await self._emit_memory_event("track_conversation", "completed", {**details_for_event, **result_data})
            return ToolResponse(
                success=True,
                message=f"Conversation tracking completed. Processed {result_data['messages_processed']} messages, created {result_data['memories_created']} memories, added {result_data['triplets_added']} knowledge triplets.",
                data=result_data
            )

        except Exception as e:
            error_msg = f"Error tracking conversation: {str(e)}"
            await self._emit_memory_event("track_conversation", "failed", {**details_for_event, "error": error_msg})
            return ToolResponse(success=False, message=error_msg, error=error_msg)

    async def _extract_conversation_insights(self, messages: List[Dict[str, Any]],
                                           conversation_id: str, user_id: Optional[str]) -> Optional[str]:
        """
        Extracts high-level insights from a conversation using pattern analysis.
        """
        try:
            # Simple pattern-based insight extraction
            user_messages = [m for m in messages if m.get("role") == "user" and m.get("content")]
            assistant_messages = [m for m in messages if m.get("role") == "assistant" and m.get("content")]

            if not user_messages and not assistant_messages:
                return None

            # Extract topics and themes
            topics = set()
            for msg in user_messages + assistant_messages:
                content = msg.get("content", "").lower()
                # Simple keyword extraction (could be enhanced with NLP)
                words = content.split()
                # Look for potential topics (nouns, important words)
                for word in words:
                    if len(word) > 4 and word.isalpha():  # Simple heuristic
                        topics.add(word)

            # Create summary
            summary_parts = []
            summary_parts.append(f"Conversation with {len(user_messages)} user messages and {len(assistant_messages)} assistant responses")

            if topics:
                top_topics = list(topics)[:5]  # Top 5 topics
                summary_parts.append(f"Key topics discussed: {', '.join(top_topics)}")

            # Analyze conversation flow
            if len(messages) > 1:
                summary_parts.append(f"Conversation flow: {len(messages)} total exchanges")

            return ". ".join(summary_parts)

        except Exception as e:
            print(f"MemoryAgentTool: Error extracting conversation insights: {e}")
            return f"Conversation {conversation_id} with {len(messages)} messages (insight extraction failed)"

    async def _extract_conversation_triplets(self, messages: List[Dict[str, Any]],
                                           conversation_id: str, user_id: Optional[str]) -> List[Dict[str, Any]]:
        """
        Extracts knowledge graph triplets from conversation content.
        """
        try:
            triplets = []

            # Add conversation-level triplets
            triplets.append({
                "head": f"Conversation_{conversation_id}",
                "relation": "has_participant",
                "tail": user_id or "unknown_user",
                "properties": {"conversation_id": conversation_id, "type": "conversation_tracking"}
            })

            # Extract entity relationships from messages
            for i, message in enumerate(messages):
                if not isinstance(message, dict) or not message.get("content"):
                    continue

                role = message.get("role", "unknown")
                content = message.get("content", "")

                # Simple entity extraction (could be enhanced with NER)
                # Look for patterns like "I like X", "X is Y", etc.
                content_lower = content.lower()

                # Pattern: "I like/love/prefer X"
                import re
                like_patterns = re.findall(r'i (like|love|prefer|enjoy) ([a-zA-Z\s]+?)(?:[.!?]|$)', content_lower)
                for pattern, entity in like_patterns:
                    entity = entity.strip()
                    if entity and len(entity) < 50:  # Reasonable entity length
                        triplets.append({
                            "head": user_id or "user",
                            "relation": pattern,
                            "tail": entity,
                            "properties": {
                                "conversation_id": conversation_id,
                                "message_index": i,
                                "confidence": 0.7
                            }
                        })

                # Pattern: "X is Y"
                is_patterns = re.findall(r'([a-zA-Z\s]+?) is ([a-zA-Z\s]+?)(?:[.!?]|$)', content_lower)
                for entity1, entity2 in is_patterns:
                    entity1, entity2 = entity1.strip(), entity2.strip()
                    if entity1 and entity2 and len(entity1) < 30 and len(entity2) < 30:
                        triplets.append({
                            "head": entity1,
                            "relation": "is",
                            "tail": entity2,
                            "properties": {
                                "conversation_id": conversation_id,
                                "message_index": i,
                                "confidence": 0.6
                            }
                        })

                # Add message-level triplets
                triplets.append({
                    "head": f"Conversation_{conversation_id}",
                    "relation": "contains_message",
                    "tail": f"Message_{conversation_id}_{i}",
                    "properties": {
                        "role": role,
                        "message_index": i,
                        "content_length": len(content)
                    }
                })

            return triplets

        except Exception as e:
            print(f"MemoryAgentTool: Error extracting conversation triplets: {e}")
            return []