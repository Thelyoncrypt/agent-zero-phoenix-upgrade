# python/tools/memory_agent_tool.py
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

# Import memory agent components
from python.agents.memory_agent.memory import IntelligentMemory

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
                        "enum": ["add", "search", "update", "delete", "get_all"],
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
                    }
                },
                "required": ["action"]
            },
            **kwargs
        )
        # Each agent/context gets its own memory instance for now.
        # In a multi-user/multi-agent setup, agent_id would be crucial.
        agent_id_for_memory = self.agent.get_user_id() or self.agent.get_thread_id() or "default_agent_zero_user"
        self.memory_system = IntelligentMemory(agent_id=agent_id_for_memory)
        print(f"MemoryAgentTool initialized for agent {agent.agent_name} (context: {agent.context.id}) with memory agent_id: {agent_id_for_memory}")

    async def _emit_memory_event(self, action_name: str, status: str, details: Optional[Dict[str, Any]] = None):
        """Helper to emit MEMORY_UPDATE events."""
        if not STREAM_PROTOCOL_AVAILABLE:
            print(f"MemoryAgentTool: StreamProtocol not available, logging event: {action_name} - {status}")
            return
            
        payload = {"action": action_name, "status": status}
        if details:
            payload.update(details)
        
        if hasattr(self.agent, '_emit_stream_event'):
            await self.agent._emit_stream_event(StreamEventType.MEMORY_UPDATE, payload)
        else:
            print(f"MemoryAgentTool: Agent does not have _emit_stream_event method. Cannot emit MEMORY_UPDATE.")

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
            
        user_id = kwargs.get("user_id", self.agent.get_user_id()) # Mem0 operations are often user-scoped

        try:
            if action == "add":
                # Mem0's `add` can take various forms of data. Here we simplify.
                # If 'messages' kwarg is present, use specific message processing.
                messages = kwargs.get("messages") # List of {"role": "user/assistant", "content": "..."}
                data_to_add = kwargs.get("data") # Generic data
                memory_id = kwargs.get("memory_id") # Optional ID for the new memory

                if messages and isinstance(messages, list):
                    return await self._add_from_messages(messages, user_id)
                elif data_to_add is not None:
                    return await self._add_generic_memory(data_to_add, memory_id, user_id)
                else:
                    return ToolResponse(
                        success=False,
                        error="Missing required data",
                        message="Error: 'messages' (list of dicts) or 'data' (generic) required for 'add' action."
                    )

            elif action == "search":
                query = kwargs.get("query")
                limit = kwargs.get("limit", 5)
                if not query:
                    return ToolResponse(
                        success=False,
                        error="Missing 'query' parameter",
                        message="Error: 'query' is required for search action."
                    )
                return await self._search_memory(query, user_id, limit)
            
            elif action == "update":
                memory_id = kwargs.get("memory_id")
                new_data = kwargs.get("data")
                if not memory_id or new_data is None:
                    return ToolResponse(
                        success=False,
                        error="Missing required parameters",
                        message="Error: 'memory_id' and 'data' are required for update action."
                    )
                return await self._update_memory(memory_id, new_data, user_id)
                
            elif action == "delete":
                memory_id = kwargs.get("memory_id")
                if not memory_id:
                    return ToolResponse(
                        success=False,
                        error="Missing 'memory_id' parameter",
                        message="Error: 'memory_id' is required for delete action."
                    )
                return await self._delete_memory(memory_id, user_id)

            elif action == "get_all": # For debugging or specific use cases
                return await self._get_all_memories(user_id)
            else:
                return ToolResponse(
                    success=False,
                    error=f"Unknown action: {action}",
                    message=f"Unknown MemoryAgent action: {action}"
                )
                
        except Exception as e:
            import traceback
            error_message = f"MemoryAgentTool error during action '{action}': {str(e)}"
            print(f"{error_message}\\n{traceback.format_exc()}")
            await self._emit_memory_event(action, "error", {"error": str(e), "user_id": user_id})
            return ToolResponse(
                success=False,
                error=str(e),
                message=error_message
            )

    async def _add_from_messages(self, messages: List[Dict[str, Any]], user_id: Optional[str]) -> ToolResponse:
        await self._emit_memory_event("add_messages", "starting", {"count": len(messages), "user_id": user_id})
        # In real Mem0, this call is more complex, involving LLMs for extraction.
        # Here, our mock IntelligentMemory.add_messages does a simplified version.
        stored_ids = await self.memory_system.add_messages(messages, user_id=user_id)
        result_details = {"stored_ids": stored_ids, "user_id": user_id, "processed_messages": len(messages)}
        await self._emit_memory_event("add_messages", "completed", result_details)
        return ToolResponse(
            success=True,
            data=result_details,
            message=f"Added {len(stored_ids)} memories from messages."
        )

    async def _add_generic_memory(self, data: Any, memory_id: Optional[str], user_id: Optional[str]) -> ToolResponse:
        await self._emit_memory_event("add_generic", "starting", {"has_id": bool(memory_id), "user_id": user_id})
        stored_id = await self.memory_system.add(data, memory_id=memory_id) # user_id scoping is part of memory_system
        result_details = {"stored_id": stored_id, "user_id": user_id}
        await self._emit_memory_event("add_generic", "completed", result_details)
        return ToolResponse(
            success=True,
            data=result_details,
            message=f"Memory added with ID: {stored_id}"
        )

    async def _search_memory(self, query: str, user_id: Optional[str], limit: int) -> ToolResponse:
        await self._emit_memory_event("search", "processing", {"query": query, "limit": limit, "user_id": user_id})
        results = await self.memory_system.search(query, user_id=user_id, limit=limit)
        await self._emit_memory_event("search", "completed", {"query": query, "results_count": len(results), "user_id": user_id})
        return ToolResponse(
            success=True,
            data={"results": results},
            message=json.dumps(results)
        )

    async def _update_memory(self, memory_id: str, new_data: Any, user_id: Optional[str]) -> ToolResponse:
        await self._emit_memory_event("update", "processing", {"memory_id": memory_id, "user_id": user_id})
        success = await self.memory_system.update(memory_id, new_data) # user_id scoping in memory_system
        status = "completed" if success else "failed"
        await self._emit_memory_event("update", status, {"memory_id": memory_id, "success": success, "user_id": user_id})
        return ToolResponse(
            success=success,
            data={"success": success},
            message=f"Memory update {status}."
        )

    async def _delete_memory(self, memory_id: str, user_id: Optional[str]) -> ToolResponse:
        await self._emit_memory_event("delete", "processing", {"memory_id": memory_id, "user_id": user_id})
        success = await self.memory_system.delete(memory_id) # user_id scoping in memory_system
        status = "completed" if success else "failed"
        await self._emit_memory_event("delete", status, {"memory_id": memory_id, "success": success, "user_id": user_id})
        return ToolResponse(
            success=success,
            data={"success": success},
            message=f"Memory deletion {status}."
        )

    async def _get_all_memories(self, user_id: Optional[str]) -> ToolResponse:
        await self._emit_memory_event("get_all", "processing", {"user_id": user_id})
        all_memories = await self.memory_system.get_all(user_id=user_id)
        await self._emit_memory_event("get_all", "completed", {"count": len(all_memories), "user_id": user_id})
        return ToolResponse(
            success=True,
            data={"memories": all_memories},
            message=json.dumps(all_memories)
        )