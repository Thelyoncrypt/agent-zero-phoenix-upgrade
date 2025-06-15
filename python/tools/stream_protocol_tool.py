"""
StreamProtocol Tool - AG-UI Protocol Integration for Agent Zero
Provides standardized agent-frontend communication with real-time streaming
Based on AG-UI Protocol specification and TypeScript SDK
"""

from python.helpers.tool import Tool  # Existing Agent Zero helper
from typing import Dict, Any, List, Optional
import asyncio
import asyncio
import json
import uuid
from datetime import datetime
from dataclasses import dataclass, field
from enum import Enum

class StreamEventType(Enum):
    """20 standard AG-UI event types including audio streaming"""
    TEXT_MESSAGE_CONTENT = "text_message_content"
    TOOL_CALL_START = "tool_call_start"
    TOOL_CALL_END = "tool_call_end"
    TOOL_RESULT = "tool_result"
    STATE_DELTA = "state_delta"
    AGENT_THOUGHT = "agent_thought"
    HUMAN_INTERVENTION = "human_intervention"
    GENERATIVE_UI = "generative_ui"
    CONTEXT_UPDATE = "context_update"
    PROGRESS_UPDATE = "progress_update"
    ERROR_EVENT = "error_event"
    SESSION_START = "session_start"
    SESSION_END = "session_end"
    MEMORY_UPDATE = "memory_update"
    KNOWLEDGE_RESULT = "knowledge_result"
    BROWSER_ACTION = "browser_action"
    CRAWL_PROGRESS = "crawl_progress"
    # Audio streaming events for TTS
    AUDIO_CHUNK = "audio_chunk"
    TTS_STREAM_START = "tts_stream_start"
    TTS_STREAM_END = "tts_stream_end"

@dataclass
class RunAgentInput:
    """AG-UI RunAgentInput schema"""
    thread_id: str
    messages: List[Dict[str, Any]]
    state: Optional[Dict[str, Any]] = None
    user_id: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None

@dataclass 
class StreamEvent:
    """AG-UI compatible event structure"""
    type: StreamEventType
    payload: Dict[str, Any]
    timestamp: str = field(default_factory=lambda: datetime.utcnow().isoformat())
    thread_id: Optional[str] = None
    user_id: Optional[str] = None
    event_id: str = field(default_factory=lambda: str(uuid.uuid4()))

class StreamTransport:
    """
    Transport layer for AG-UI events. Manages active WebSocket connections.
    An instance of this class should be globally available in the application.
    """
    def __init__(self):
        self.connections: Dict[str, Dict[str, Any]] = {}  # connection_id -> {"websocket": ws, "thread_id": str, "user_id": str}
        self.lock = asyncio.Lock()  # To protect access to self.connections
        print("StreamTransport: Instance created.")
        
    async def emit_event(self, event: StreamEvent):
        """Emit event to all connected clients relevant to the event's thread_id."""
        event_data_str = json.dumps({
            "id": event.event_id,
            "type": event.type.value,
            "payload": event.payload,
            "timestamp": event.timestamp,
            "threadId": event.thread_id,
            "userId": event.user_id
        })
        
        connections_to_send = []
        async with self.lock:
            for conn_id, conn_info in self.connections.items():
                if conn_info.get("thread_id") == event.thread_id:
                    connections_to_send.append(conn_info["websocket"])
        
        if not connections_to_send:
            print(f"StreamTransport: No active connections for thread_id {event.thread_id} to emit event {event.type.value}")
            return

        for ws in connections_to_send:
            try:
                if not hasattr(ws, 'closed') or not ws.closed:
                    await ws.send(event_data_str)  # Use send() for flask-sock
                else:
                    print(f"StreamTransport: WebSocket for thread {event.thread_id} was closed. Cannot send event.")
                    # Consider removing closed WebSockets from self.connections here or during unregister.
            except Exception as e:
                print(f"StreamTransport: Error sending event to WebSocket for thread {event.thread_id}: {e}")
                # Consider removing this WebSocket or handling disconnection.
    
    async def register_connection(self, websocket, thread_id: str, user_id: Optional[str] = None) -> str:
        """Register new websocket connection."""
        connection_id = str(uuid.uuid4())
        async with self.lock:
            self.connections[connection_id] = {
                "websocket": websocket,
                "thread_id": thread_id,
                "user_id": user_id,
                "created_at": datetime.utcnow()
            }
        print(f"StreamTransport: Registered WS connection {connection_id} for thread {thread_id}")
        return connection_id
    
    async def unregister_connection(self, connection_id: str):
        """Remove websocket connection."""
        async with self.lock:
            if connection_id in self.connections:
                del self.connections[connection_id]
                print(f"StreamTransport: Unregistered WS connection {connection_id}")

class StreamProtocolTool(Tool):
    """
    StreamProtocol (AG-UI) integration for Agent Zero
    Provides standardized agent-frontend communication with real-time streaming
    """
    
    def __init__(self, agent, **kwargs):
        super().__init__(agent, name="stream_protocol_tool", description="Manages AG-UI streaming communication.", args_schema=None, **kwargs)
        
        # Attempt to get the transport from agent context (set by run_ui.py)
        self.transport = self.agent.context.get_custom_data('stream_transport_instance')
        if not self.transport:
            # Fallback or error if not found - this indicates an initialization issue in run_ui.py
            print("StreamProtocolTool: CRITICAL - StreamTransport instance not found in agent context.")
            # As a last resort, could use a global singleton, but injection is cleaner.
            # For now, we'll assume it will be there. If not, emit_event will fail.
            # A more robust solution would be to pass it during agent/tool initialization.
            raise RuntimeError("StreamTransport not properly initialized and passed to StreamProtocolTool.")

        self.active_threads: Dict[str, Dict[str, Any]] = {} 
        self.middleware_stack: List[callable] = []
        print(f"StreamProtocolTool initialized for agent {agent.agent_name}, using injected StreamTransport.")
        
    async def execute(self, action: str, **kwargs):
        """
        Execute StreamProtocol operations
        
        Args:
            action (str): The specific action to perform (e.g., "emit_event", "handle_input").
            **kwargs: Arguments specific to the action.
        """
        
        # Ensure thread_id is available from agent context if not provided
        thread_id = kwargs.get("thread_id")
        if not thread_id:
             thread_id = self.agent.get_thread_id()


        try:
            if action == "emit_event":
                # Required kwargs: event_type (str), payload (Dict)
                # Optional kwargs: thread_id (str), user_id (str)
                if "event_type" not in kwargs or "payload" not in kwargs:
                    return self.agent_response("Missing 'event_type' or 'payload' for emit_event action.", error=True)
                return await self._emit_event(**kwargs)
            elif action == "handle_input":
                # Required kwargs: input_data (Dict)
                if "input_data" not in kwargs:
                    return self.agent_response("Missing 'input_data' for handle_input action.", error=True)
                return await self._handle_input(**kwargs)
            elif action == "start_session":
                # Required kwargs: thread_id (str)
                # Optional kwargs: user_id (str), initial_state (Dict)
                if "thread_id" not in kwargs:
                    return self.agent_response("Missing 'thread_id' for start_session action.", error=True)
                return await self._start_session(**kwargs)
            elif action == "end_session":
                # Required kwargs: thread_id (str)
                if "thread_id" not in kwargs:
                    return self.agent_response("Missing 'thread_id' for end_session action.", error=True)
                return await self._end_session(**kwargs)
            elif action == "update_state":
                # Required kwargs: thread_id (str), state_delta (Dict)
                if "thread_id" not in kwargs or "state_delta" not in kwargs:
                    return self.agent_response("Missing 'thread_id' or 'state_delta' for update_state action.", error=True)
                return await self._update_state(**kwargs)
            elif action == "resume_agent_with_message":
                # Explicit client action to send message and resume
                message_content = kwargs.get("message_content")
                attachments = kwargs.get("attachments")
                client_state = kwargs.get("state")  # Optional state from client
                if message_content is None:
                    return self.agent_response("Missing 'message_content'.", error=True)

                # This will call agent.process_streamed_message, which handles intervention resolution
                await self.agent.process_streamed_message(
                    content=message_content,
                    role="user",  # Assuming resume implies user input
                    attachments=attachments,
                    incoming_state=client_state
                )
                return self.agent_response({"status": "agent_resumed_and_processing_message"})
            elif action == "force_resume_agent":
                # Client wants to unpause without new message content
                if self.agent.context.intervention_needed:
                    print(f"StreamProtocolTool: Forcing agent resume for context {self.agent.context.id}")
                    self.agent.context.resolve_intervention()
                    await self._emit_event_internal(
                        StreamEventType.HUMAN_INTERVENTION,
                        {"status": "resolved_by_client_force_resume", "prompt_resolved": self.agent.context.intervention_prompt},
                        self.agent.get_thread_id(), self.agent.get_user_id()
                    )
                    return self.agent_response({"status": "agent_resume_forced", "message": "Agent will continue on its next processing cycle."})
                else:
                    return self.agent_response({"status": "agent_not_paused_for_intervention"})
            elif action == "register_middleware":
                # Required kwargs: middleware_func (callable)
                if "middleware_func" not in kwargs:
                    return self.agent_response("Missing 'middleware_func' for register_middleware action.", error=True)
                return await self._register_middleware(**kwargs)
            else:
                return self.agent_response(f"Unknown StreamProtocol action: {action}", error=True)
                
        except Exception as e:
            await self._emit_error_event(str(e), thread_id)
            return self.agent_response(f"StreamProtocol error: {str(e)}", error=True)

    async def _emit_event(self, event_type: str, payload: Dict[str, Any], 
                         thread_id: Optional[str] = None, user_id: Optional[str] = None):
        """Emit standardized event to frontend"""
        try:
            event_enum = StreamEventType(event_type)
        except ValueError:
            return self.agent_response(f"Invalid event type: {event_type}", error=True)
        
        # Prioritize explicitly passed IDs, then fallback to agent's context
        effective_thread_id = thread_id if thread_id is not None else self.agent.get_thread_id()
        effective_user_id = user_id if user_id is not None else self.agent.get_user_id()

        if not effective_thread_id:
            print(f"StreamProtocolTool: Warning - Emitting event '{event_type}' without a thread_id.")
            # Potentially default to agent's context ID if no thread_id is available
            # effective_thread_id = self.agent.context.id

        event = StreamEvent(
            type=event_enum,
            payload=payload,
            thread_id=effective_thread_id,
            user_id=effective_user_id
        )
        
        for middleware in self.middleware_stack:
            event = await middleware(event)
            if event is None:
                return self.agent_response("Event filtered by middleware")
        
        await self.transport.emit_event(event)  # Uses the global transport
        
        return self.agent_response({
            "success": True,
            "event_id": event.event_id,
            "type": event_type,
            "timestamp": event.timestamp
        })
    
    async def _handle_input(self, input_data: Dict[str, Any]):
        """Process incoming frontend input according to RunAgentInput schema"""
        try:
            run_input = RunAgentInput(
                thread_id=input_data.get("threadId", str(uuid.uuid4())),
                messages=input_data.get("messages", []),
                state=input_data.get("state", {}),  # This is the state from the client
                user_id=input_data.get("userId"),
                metadata=input_data.get("metadata", {})
            )

            # Check for UI response data
            ui_response_payload = input_data.get("uiResponse")  # Custom field for UI responses
            
            # Update agent's context with thread_id and user_id from the input
            self.agent.set_thread_id(run_input.thread_id)
            if run_input.user_id:  # user_id is optional
                self.agent.set_user_id(run_input.user_id)

            if ui_response_payload and isinstance(ui_response_payload, dict):
                print(f"StreamProtocolTool: Detected uiResponse in input_data: {ui_response_payload}")
                # Process this as a UI response, content might be empty if data is purely structured
                await self.agent.process_streamed_message(
                    content=json.dumps(ui_response_payload.get("data", {})),  # Represent data as string for content
                    role="ui_response",  # Custom role to distinguish
                    attachments=None,
                    incoming_state=run_input.state,  # Client might send state with UI response
                    ui_response_data=ui_response_payload  # Pass the structured UI response
                )
                # If there were also regular messages in this RunAgentInput, process them too
                # For now, let's assume they are mutually exclusive or uiResponse takes precedence for this input.

            elif run_input.messages:  # Process regular messages
                for i, message_data in enumerate(run_input.messages):
                    state_to_pass = run_input.state if i == 0 and not ui_response_payload else None
                    await self.agent.process_streamed_message(
                        content=message_data.get("content", ""),
                        role=message_data.get("role", "user").lower(),
                        attachments=message_data.get("attachments"),
                        incoming_state=state_to_pass,
                        ui_response_data=None  # Not a UI response if in messages list like this
                    )
            elif run_input.state and not ui_response_payload:  # Only state update, no messages
                await self.agent.set_agent_state_from_external(run_input.state, source="client_state_push_no_message")

            if run_input.thread_id not in self.active_threads:
                # This tool's tracking of active_threads is for *its own* session concept, distinct from agent's state.
                await self._emit_event_internal(
                    StreamEventType.SESSION_START,
                    {"threadId": run_input.thread_id, "userId": run_input.user_id, "initialState": self.agent.context.get_agent_state()},
                    run_input.thread_id, run_input.user_id
                )
                self.active_threads[run_input.thread_id] = {
                    "user_id": run_input.user_id,
                    "state_from_tool_perspective": self.agent.context.get_agent_state(),
                    "created_at": datetime.utcnow()
                }
            
            return self.agent_response({
                "success": True,
                "thread_id": run_input.thread_id,
                "messages_processed": len(run_input.messages),
                "ui_response_processed": bool(ui_response_payload),
                "state_applied": bool(run_input.state)
            })
            
        except Exception as e:
            import traceback
            print(f"StreamProtocolTool._handle_input error: {e}\n{traceback.format_exc()}")
            return self.agent_response(f"Input processing error: {str(e)}", error=True)

    async def _process_message(self, message_data: Dict[str, Any], thread_id: str, user_id: Optional[str]):
        """Process individual message from frontend and trigger agent if user message."""
        role = message_data.get("role", "user").lower()
        content = message_data.get("content", "")
        attachments = message_data.get("attachments")  # AG-UI might support attachments

        # Emit received message (e.g., for UI to confirm receipt or for logging)
        # This is distinct from the agent's final response.
        await self._emit_event_internal(
            StreamEventType.TEXT_MESSAGE_CONTENT,  # Or a more specific "USER_INPUT_RECEIVED"
            {
                "role": role,
                "content": content,  # Echoing back received content
                "messageId": message_data.get("id", str(uuid.uuid4())),
                "status": "received" 
            },
            thread_id, user_id
        )
        
        if role == "user":
            # This is now handled directly in _handle_input
            print(f"StreamProtocolTool: User message processed via _handle_input")
        else:
            print(f"StreamProtocolTool: Received non-user message (role: {role}). Not triggering full agent processing.")


    async def _emit_event_internal(self, event_type: StreamEventType, payload: Dict[str, Any], 
                             thread_id: Optional[str], user_id: Optional[str]):
        """Internal helper to create and emit event, using the tool's transport."""
        event = StreamEvent(
            type=event_type,
            payload=payload,
            thread_id=thread_id,
            user_id=user_id
        )
        await self.transport.emit_event(event)  # Uses the global transport

    # Placeholder for methods that will depend on agent modifications
    async def _update_agent_context(self, run_input: RunAgentInput):
        print(f"StreamProtocolTool: Placeholder for _update_agent_context with {run_input}")
        pass

    async def _trigger_agent_processing(self, content: str, thread_id: str, user_id: Optional[str]):
        print(f"StreamProtocolTool: Placeholder for _trigger_agent_processing with content '{content}'")
        # This will eventually call self.agent.hist_add_user_message and self.agent.monologue
        # and then emit events with the agent's thoughts and responses.
        pass

    async def _start_session(self, thread_id: str, user_id: Optional[str] = None, 
                           initial_state: Optional[Dict[str, Any]] = None):
        if thread_id in self.active_threads:
            return self.agent_response(f"Tool: Session {thread_id} already active for this tool instance.", error=True)
        
        self.active_threads[thread_id] = {
            "user_id": user_id,
            "state_from_tool_perspective": initial_state or {},
            "created_at": datetime.utcnow()
        }
        # Also ensure agent context is updated if this is a new session initiation point
        self.agent.set_thread_id(thread_id)
        if user_id: self.agent.set_user_id(user_id)
        if initial_state: self.agent.update_agent_state(initial_state)

        await self._emit_event_internal(
            StreamEventType.SESSION_START,
            {"threadId": thread_id, "userId": user_id, "initialState": initial_state},
            thread_id, user_id
        )
        return self.agent_response({
            "success": True, "thread_id": thread_id, "status": "session_started"
        })

    async def _end_session(self, thread_id: str):
        if thread_id not in self.active_threads:
            return self.agent_response(f"Session {thread_id} not found", error=True)
        session_info = self.active_threads.pop(thread_id)
        await self._emit_event_internal(
            StreamEventType.SESSION_END,
            {"threadId": thread_id, "duration": (datetime.utcnow() - session_info["created_at"]).total_seconds()},
            thread_id, session_info.get("user_id")
        )
        return self.agent_response({
            "success": True, "thread_id": thread_id, "status": "session_ended"
        })

    async def _update_state(self, thread_id: str, state_delta: Dict[str, Any]):
        """
        This action is if the AGENT wants to explicitly update its own state and broadcast.
        Client-pushed state updates are handled via _handle_input.
        """
        if thread_id not in self.active_threads:  # Tool's session tracking
            print(f"StreamProtocolTool: Warning - _update_state called for untracked thread {thread_id}. Will proceed with agent state update.")
            # Ensure agent context is aligned, this might create/get agent context
            self.agent.set_thread_id(thread_id)
            # It's possible user_id is not known here if session wasn't started via tool.

        # The agent updates its own state and broadcasts
        await self.agent.update_and_broadcast_agent_state(state_delta, source_of_change="tool_direct_update_state")

        # Update this tool's local cache of the state if needed (though agent_state is the source of truth)
        if thread_id in self.active_threads:
             self.active_threads[thread_id]["state_from_tool_perspective"].update(state_delta)

        return self.agent_response({
            "success": True, "thread_id": thread_id, "updated_agent_state_snapshot": self.agent.context.get_agent_state()
        })

    async def _register_middleware(self, middleware_func: callable):
        self.middleware_stack.append(middleware_func)
        return self.agent_response({
            "success": True, "middleware_count": len(self.middleware_stack)
        })

    async def _emit_error_event(self, error_message: str, thread_id: str = None):
        # Ensure thread_id is available, similar to _emit_event
        current_thread_id = thread_id
        if not current_thread_id:
             current_thread_id = self.agent.get_thread_id()

        await self._emit_event_internal(
            StreamEventType.ERROR_EVENT,
            {"error": error_message, "timestamp": datetime.utcnow().isoformat()},
            current_thread_id,
            None
        )
        
    def agent_response(self, message_content: Any, error: bool = False) -> Dict[str, Any]:
        """Helper to format tool responses consistently."""
        if error:
            return {"error": str(message_content)}
        return {"result": message_content}