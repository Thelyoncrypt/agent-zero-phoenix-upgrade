# python/tools/hybrid_memory_tool.py
from python.helpers.tool import Tool, Response as ToolResponse
from typing import Dict, Any, List, Optional
import json

# Import StreamProtocol components if available
try:
    from python.tools.stream_protocol_tool import StreamEventType
    STREAM_PROTOCOL_AVAILABLE = True
except ImportError:
    STREAM_PROTOCOL_AVAILABLE = False
    StreamEventType = None

class HybridMemoryTool(Tool):
    """
    Hybrid Memory Tool for Agent Zero.
    Combines Agent Zero's existing structured memory with MemoryAgent (Mem0) capabilities.
    Provides a unified interface for storing and retrieving context.
    """
    
    def __init__(self, agent, **kwargs):
        super().__init__(
            agent=agent,
            name="hybrid_memory_tool",
            description="Manages a hybrid memory system, storing and retrieving information using both structured and intelligent memory approaches.",
            args_schema={
                "type": "object",
                "properties": {
                    "action": {
                        "type": "string",
                        "enum": ["store_interaction", "retrieve_context"],
                        "description": "Type of hybrid memory operation to perform"
                    },
                    "user_id": {
                        "type": "string",
                        "description": "Identifier for the user context (optional)"
                    },
                    "interaction_data": {
                        "type": "object",
                        "description": "Data about the interaction to store (for store_interaction action)"
                    },
                    "query": {
                        "type": "string",
                        "description": "Query to retrieve relevant context (for retrieve_context action)"
                    },
                    "limit": {
                        "type": "integer",
                        "description": "Maximum results from each memory source (default: 5)"
                    }
                },
                "required": ["action"]
            },
            **kwargs
        )
        # Use agent's user/thread ID for memory scoping
        self.agent_id_for_memory = self.agent.get_user_id() or self.agent.get_thread_id() or "default_hybrid_user"
        print(f"HybridMemoryTool initialized for agent {agent.agent_name} (context: {agent.context.id}) with memory_id: {self.agent_id_for_memory}")

    async def _emit_hybrid_memory_event(self, action_name: str, status: str, details: Optional[Dict[str, Any]] = None):
        """Helper to emit events related to hybrid memory operations."""
        if not STREAM_PROTOCOL_AVAILABLE:
            print(f"HybridMemoryTool: StreamProtocol not available, logging event: {action_name} - {status}")
            return
            
        # Use MEMORY_UPDATE event type for hybrid memory operations
        payload = {"source_system": "hybrid_memory", "action": action_name, "status": status}
        if details:
            payload.update(details)
        
        if hasattr(self.agent, '_emit_stream_event'):
            await self.agent._emit_stream_event(StreamEventType.MEMORY_UPDATE, payload)
        else:
            print(f"HybridMemoryTool: Agent does not have _emit_stream_event method. Cannot emit MEMORY_UPDATE.")

    async def execute(self, **kwargs) -> ToolResponse:
        """
        Execute HybridMemory operations.
        
        Args:
            action (str): "store_interaction" or "retrieve_context".
            **kwargs: Arguments for the action.
        """
        action = kwargs.get("action")
        if not action:
            return ToolResponse(
                success=False,
                error="Missing required 'action' parameter",
                message="Error: 'action' is required for HybridMemory operations."
            )
            
        user_id = kwargs.get("user_id", self.agent_id_for_memory)

        try:
            if action == "store_interaction":
                # interaction_data: Dict, e.g., {"type": "user_message", "content": "...", "timestamp": "...", "messages": [...]}
                interaction_data = kwargs.get("interaction_data")
                if not interaction_data or not isinstance(interaction_data, dict):
                    return ToolResponse(
                        success=False,
                        error="Missing or invalid 'interaction_data'",
                        message="Error: 'interaction_data' (dict) is required for store_interaction."
                    )
                return await self._store_interaction(interaction_data, user_id)
            
            elif action == "retrieve_context":
                query = kwargs.get("query")
                limit = kwargs.get("limit", 5) # Results from each source
                if not query:
                    return ToolResponse(
                        success=False,
                        error="Missing 'query' parameter",
                        message="Error: 'query' is required for retrieve_context."
                    )
                return await self._retrieve_context(query, user_id, limit)
            
            else:
                return ToolResponse(
                    success=False,
                    error=f"Unknown action: {action}",
                    message=f"Unknown HybridMemoryTool action: {action}"
                )

        except Exception as e:
            import traceback
            error_message = f"HybridMemoryTool error during action '{action}': {str(e)}"
            print(f"{error_message}\\n{traceback.format_exc()}")
            await self._emit_hybrid_memory_event(action, "error", {"error": str(e), "user_id": user_id})
            return ToolResponse(
                success=False,
                error=str(e),
                message=error_message
            )

    async def _store_interaction(self, interaction_data: Dict[str, Any], user_id: Optional[str]) -> ToolResponse:
        """
        Stores an interaction in both structured (Agent Zero native) and intelligent (Mem0-like) memory.
        interaction_data should be a dictionary, potentially including 'messages' for Mem0,
        and 'text' or 'content' for Agent Zero's memory_save.
        """
        await self._emit_hybrid_memory_event("store_interaction", "starting", {"user_id": user_id})
        
        results = {"structured_memory_status": "not_attempted", "intelligent_memory_status": "not_attempted"}

        # 1. Store in Agent Zero's structured memory (e.g., using memory_save tool)
        try:
            # Adapt interaction_data for memory_save tool's expected format
            text_to_save = interaction_data.get("content", json.dumps(interaction_data)) # Fallback to full JSON
            metadata_for_az = interaction_data.get("metadata", {})
            metadata_for_az["source_interaction_type"] = interaction_data.get("type", "generic")
            metadata_for_az["user_id"] = user_id # Ensure user_id is part of metadata for AZ memory if it supports it

            # Call existing memory_save tool
            # Note: self.agent.call_tool needs to be robust or this needs direct access to memory logic
            response_az = await self.agent._call_tool(
                "memory_save", 
                {"text": text_to_save, "area": "hybrid_interaction", **metadata_for_az}
            )
            if response_az and not response_az.get("error", False): # Check for error in response dict
                results["structured_memory_status"] = f"success: {response_az.get('message', 'Stored successfully')}"
            else:
                results["structured_memory_status"] = f"failed: {response_az.get('message', 'Unknown error') if response_az else 'No response'}"
        except Exception as e:
            results["structured_memory_status"] = f"error: {str(e)}"
            print(f"HybridMemoryTool: Error storing in Agent Zero structured memory: {e}")

        # 2. Store in MemoryAgent's intelligent memory (using memory_agent_tool)
        try:
            # Adapt interaction_data for memory_agent_tool's "add" action
            mem0_payload = {"action": "add", "user_id": user_id}
            if "messages" in interaction_data: # Mem0 prefers message lists
                mem0_payload["messages"] = interaction_data["messages"]
            else: # Fallback to generic data
                mem0_payload["data"] = interaction_data 
            
            response_mem0 = await self.agent._call_tool("memory_agent_tool", mem0_payload)
            if response_mem0 and not response_mem0.get("error", False):
                results["intelligent_memory_status"] = f"success: {response_mem0.get('message', 'Stored successfully')}"
            else:
                results["intelligent_memory_status"] = f"failed: {response_mem0.get('message', 'Unknown error') if response_mem0 else 'No response'}"
        except Exception as e:
            results["intelligent_memory_status"] = f"error: {str(e)}"
            print(f"HybridMemoryTool: Error storing in MemoryAgent intelligent memory: {e}")

        await self._emit_hybrid_memory_event("store_interaction", "completed", {"results": results, "user_id": user_id})
        return ToolResponse(
            success=True,
            data=results,
            message="Interaction processed by hybrid memory."
        )

    async def _retrieve_context(self, query: str, user_id: Optional[str], limit: int) -> ToolResponse:
        """
        Retrieves and combines context from both memory systems.
        Placeholder: currently just queries both and returns a combined list.
        """
        await self._emit_hybrid_memory_event("retrieve_context", "processing", {"query": query, "user_id": user_id})
        
        combined_results = {
            "query": query,
            "structured_results": [],
            "intelligent_results": [],
            "ranked_combined_context": "Placeholder: Combined context would appear here." # Placeholder for actual ranked text
        }

        # 1. Retrieve from Agent Zero's structured memory (e.g., using memory_load tool)
        try:
            # Note: Agent Zero's memory_load tool might have different args (e.g., threshold, filter)
            az_mem_response = await self.agent._call_tool(
                "memory_load",
                {"query": query, "limit": limit} # Add other relevant AZ memory_load args if needed
            )
            if az_mem_response and not az_mem_response.get("error", False) and az_mem_response.get("message"):
                # Assuming message is a JSON string of results or a list of dicts
                try:
                    az_results = json.loads(az_mem_response["message"]) if isinstance(az_mem_response["message"], str) else az_mem_response["message"]
                    combined_results["structured_results"] = az_results if isinstance(az_results, list) else [az_results]
                except json.JSONDecodeError:
                    combined_results["structured_results"] = [{"error": "Failed to parse AZ memory response", "raw": az_mem_response["message"]}]
            elif az_mem_response and az_mem_response.get("error"):
                combined_results["structured_results"] = [{"error": az_mem_response.get("message", "Unknown error")}]

        except Exception as e:
            print(f"HybridMemoryTool: Error retrieving from Agent Zero structured memory: {e}")
            combined_results["structured_results"] = [{"error": str(e)}]

        # 2. Retrieve from MemoryAgent's intelligent memory (using memory_agent_tool)
        try:
            mem0_response = await self.agent._call_tool(
                "memory_agent_tool",
                {"action": "search", "query": query, "user_id": user_id, "limit": limit}
            )
            if mem0_response and not mem0_response.get("error", False) and mem0_response.get("data"): # Assuming data field holds the results
                combined_results["intelligent_results"] = mem0_response["data"].get("results", [])
            elif mem0_response and mem0_response.get("error"):
                combined_results["intelligent_results"] = [{"error": mem0_response.get("message", "Unknown error")}]

        except Exception as e:
            print(f"HybridMemoryTool: Error retrieving from MemoryAgent intelligent memory: {e}")
            combined_results["intelligent_results"] = [{"error": str(e)}]
        
        # Placeholder for actual combination and ranking logic
        # For now, just concatenating content for the ranked_combined_context
        ranked_text_parts = []
        for res_list_key in ["structured_results", "intelligent_results"]:
            for item in combined_results.get(res_list_key, []):
                if isinstance(item, dict) and "content" in item:
                    ranked_text_parts.append(str(item["content"])) # Mem0 search result might be dict
                elif isinstance(item, dict) and "text" in item: # Agent Zero memory_load might have 'text'
                    ranked_text_parts.append(str(item["text"]))
                elif isinstance(item, dict) and "data" in item: # MemoryAgent results might have 'data' field
                    ranked_text_parts.append(str(item["data"]))
                elif isinstance(item, str): # If memory_load just returns string
                    ranked_text_parts.append(item)

        if ranked_text_parts:
            combined_results["ranked_combined_context"] = "\\n".join(ranked_text_parts)[:2000] # Truncate for now
        else:
            combined_results["ranked_combined_context"] = "No relevant information found in either memory system."

        await self._emit_hybrid_memory_event("retrieve_context", "completed", {"query": query, "retrieved_count": len(combined_results["structured_results"]) + len(combined_results["intelligent_results"]), "user_id": user_id})
        return ToolResponse(
            success=True,
            data=combined_results,
            message="Context retrieved from hybrid memory."
        )