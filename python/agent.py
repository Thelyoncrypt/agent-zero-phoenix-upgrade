# agent.py - Agent Zero core agent and context classes with StreamProtocol enhancements
import asyncio
import json
import uuid
from typing import Optional, Dict, Any, List
from dataclasses import dataclass
from datetime import datetime

# Import StreamProtocol components for event emission
try:
    from python.tools.stream_protocol_tool import StreamProtocolTool, StreamEventType
    STREAM_PROTOCOL_AVAILABLE = True
except ImportError:
    STREAM_PROTOCOL_AVAILABLE = False
    StreamProtocolTool = None
    StreamEventType = None

# Placeholder imports - these would come from actual Agent Zero codebase
class LogEntry:
    def __init__(self, log_id: str, log_type: str, heading: str, content: str):
        self.id = log_id
        self.type = log_type
        self.heading = heading
        self.content = content
    
    def update(self, content: str):
        self.content = content
        print(f"Log entry {self.id} updated: {content[:100]}...")

class Log:
    def __init__(self, context_id: str):
        self.context_id = context_id
        self.entries = {}
        print(f"Log initialized for context {context_id}")
    
    def set_progress(self, message: str):
        print(f"Progress: {message}")
    
    def log(self, type: str, heading: str, content: str) -> LogEntry:
        log_id = str(uuid.uuid4())
        entry = LogEntry(log_id, type, heading, content)
        self.entries[log_id] = entry
        print(f"Log entry created: {heading} - {content[:100]}...")
        return entry

class History:
    def __init__(self, context):
        self.context = context
        self.messages = []
        print(f"History initialized for context {context.id}")
    
    def add_message(self, role: str, message):
        self.messages.append((role, message))
        print(f"History: Added {role} message: {getattr(message, 'message', str(message))[:100]}...")

@dataclass
class AgentConfig:
    model: str = "gpt-4"
    temperature: float = 0.7
    max_tokens: int = 2000

@dataclass
class UserMessage:
    message: str
    attachments: List[Dict[str, Any]] = None
    timestamp: str = None
    
    def __post_init__(self):
        if self.attachments is None:
            self.attachments = []
        if self.timestamp is None:
            self.timestamp = datetime.utcnow().isoformat()

@dataclass
class AIMessage:
    message: str
    timestamp: str = None
    
    def __post_init__(self):
        if self.timestamp is None:
            self.timestamp = datetime.utcnow().isoformat()

# Mock settings module
class settings:
    @staticmethod
    def get_agent_config():
        return AgentConfig()

class AgentContext:
    """Enhanced AgentContext with StreamProtocol support"""
    _instances: Dict[str, 'AgentContext'] = {}

    def __init__(self, id: Optional[str] = None, name: Optional[str] = None, 
                 thread_id: Optional[str] = None, user_id: Optional[str] = None):
        self.id: str = id or str(uuid.uuid4())
        self.name: str = name or "New Chat"
        self.config: AgentConfig = settings.get_agent_config()
        self.log: Log = Log(self.id)
        self.history: History = History(self)
        self.agent0: Optional['Agent'] = None
        self.streaming_agent: Optional['Agent'] = None
        self.custom_data: Dict[str, Any] = {} 
        self.halt_event: asyncio.Event = asyncio.Event()
        self.intervention_needed: bool = False
        self.intervention_message: Optional[UserMessage] = None
        self.paused: bool = False
        self.current_tool_log_id: Optional[str] = None

        # New attributes for StreamProtocol
        self.thread_id: Optional[str] = thread_id or self.id
        self.user_id: Optional[str] = user_id
        self.agent_state: Dict[str, Any] = {}

        # Human intervention support
        self.intervention_prompt: Optional[str] = None

        # StreamTransport will be managed globally
        self.stream_transport: Optional[Any] = None

        AgentContext._instances[self.id] = self
        print(f"AgentContext created: id={self.id}, name='{self.name}', thread_id='{self.thread_id}', user_id='{self.user_id}'")

    def update_internal_agent_state(self, state_delta: Dict[str, Any], source: str = "agent_logic") -> bool:
        """
        Updates the agent_state and returns True if changed, False otherwise.
        Does NOT emit STATE_DELTA itself; that's the agent's job.
        """
        changed = False
        for key, value in state_delta.items():
            if key not in self.agent_state or self.agent_state[key] != value:
                self.agent_state[key] = value
                changed = True
        if changed:
            print(f"AgentContext {self.id} (Thread: {self.thread_id}): Internal state updated by {source}. New state snapshot: {self.agent_state}")
        return changed

    def get_agent_state(self) -> Dict[str, Any]:
        """Returns a copy of the current agent state."""
        return self.agent_state.copy()

    def request_intervention(self, prompt_for_human: str):
        """Sets flags indicating intervention is needed."""
        print(f"AgentContext {self.id}: Intervention requested with prompt: '{prompt_for_human}'")
        self.intervention_needed = True
        self.intervention_prompt = prompt_for_human
        self.halt_event.clear()  # Ensure halt_event is not set, so agent will pause

    def resolve_intervention(self):
        """Clears intervention flags and allows agent to proceed."""
        print(f"AgentContext {self.id}: Intervention resolved.")
        self.intervention_needed = False
        self.intervention_prompt = None
        self.halt_event.set()  # Signal the agent to continue

    @classmethod
    def get(cls, id: Optional[str] = None, name: Optional[str] = None,
            thread_id: Optional[str] = None, user_id: Optional[str] = None) -> 'AgentContext':
        if id and id in cls._instances:
            ctx = cls._instances[id]
            # Update thread_id and user_id if provided and different
            if thread_id and ctx.thread_id != thread_id:
                ctx.thread_id = thread_id
                print(f"AgentContext {id} updated thread_id to {thread_id}")
            if user_id and ctx.user_id != user_id:
                ctx.user_id = user_id
                print(f"AgentContext {id} updated user_id to {user_id}")
            return ctx
        
        new_id = id or str(uuid.uuid4())
        # Pass through thread_id and user_id to constructor
        return cls(id=new_id, name=name, thread_id=thread_id or new_id, user_id=user_id)

    def reset(self):
        """Reset the context state"""
        self.history = History(self)
        self.custom_data = {}
        self.halt_event.clear()
        self.intervention_needed = False
        self.intervention_message = None
        self.paused = False
        self.current_tool_log_id = None
        self.agent_state = {}
        print(f"AgentContext {self.id} reset")

    @classmethod
    def remove(cls, id: str):
        """Remove a context instance"""
        if id in cls._instances:
            del cls._instances[id]
            print(f"AgentContext {id} removed")
    
    def set_custom_data(self, key: str, value: Any):
        """Set custom data for the context"""
        self.custom_data[key] = value
        print(f"AgentContext {self.id} set custom_data['{key}']")
    
    def get_custom_data(self, key: str, default: Any = None) -> Any:
        """Get custom data from the context"""
        return self.custom_data.get(key, default)

class Agent:
    """Enhanced Agent class with StreamProtocol support"""
    
    def __init__(self, agent_id: str, agent_name: str, context: AgentContext, **kwargs):
        self.agent_id = agent_id
        self.agent_name = agent_name
        self.context = context
        self.tools = []
        self.knowledge = None
        self.iteration_no = 0
        self.last_tool_was_response_tool = False
        self._stream_protocol_tool_instance = None
        
        # Auto-register available tools
        self._register_default_tools()
        
        print(f"Agent initialized: {agent_name} (id: {agent_id}, context: {context.id})")

    def get_thread_id(self) -> Optional[str]:
        """Returns the current thread ID from the context."""
        return self.context.thread_id

    def set_thread_id(self, thread_id: str):
        """Sets the thread ID in the context."""
        self.context.thread_id = thread_id
        print(f"Agent {self.agent_name} (ctx: {self.context.id}) set thread_id to: {thread_id}")

    def get_user_id(self) -> Optional[str]:
        """Returns the current user ID from the context."""
        return self.context.user_id

    def set_user_id(self, user_id: Optional[str]):
        """Sets the user ID in the context."""
        self.context.user_id = user_id
        print(f"Agent {self.agent_name} (ctx: {self.context.id}) set user_id to: {user_id}")

    async def update_and_broadcast_agent_state(self, state_delta: Dict[str, Any], source_of_change: str = "agent_internal"):
        """
        Updates the agent's state and emits a STATE_DELTA event if changes occurred.
        """
        if self.context.update_internal_agent_state(state_delta, source=source_of_change):
            await self._emit_stream_event(
                StreamEventType.STATE_DELTA if STREAM_PROTOCOL_AVAILABLE else "state_delta",
                {
                    "delta": state_delta,  # The changes that were applied
                    "full_state": self.context.get_agent_state()  # The new complete state
                }
            )

    async def set_agent_state_from_external(self, new_full_state: Dict[str, Any], source: str = "external_tool"):
        """
        Sets the agent's state to a new full state, usually from an external source like client input.
        This replaces the entire agent_state with new_full_state.
        Emits a STATE_DELTA event.
        """
        # Calculate delta for the event
        current_state = self.context.get_agent_state()
        delta = {}
        all_keys = set(current_state.keys()) | set(new_full_state.keys())
        changed = False
        for k in all_keys:
            old_v = current_state.get(k)
            new_v = new_full_state.get(k)
            if old_v != new_v:
                delta[k] = new_v  # new_v could be None if key is removed
                changed = True

        if changed:
            self.context.agent_state = new_full_state.copy()  # Replace entirely
            print(f"Agent {self.agent_name} (Thread: {self.get_thread_id()}): State fully replaced by {source}. New state: {self.context.agent_state}")
            await self._emit_stream_event(
                StreamEventType.STATE_DELTA if STREAM_PROTOCOL_AVAILABLE else "state_delta",
                {
                    "delta": delta,  # What actually changed to reach the new state
                    "full_state": self.context.get_agent_state()
                }
            )
        else:
            print(f"Agent {self.agent_name}: No change in state from external update. New state is same as current.")

    def update_agent_state(self, state_delta: Dict[str, Any]):
        """
        Legacy method - Updates the agent's persistent state associated with the AG-UI protocol.
        This state is managed per thread_id. Use update_and_broadcast_agent_state for new code.
        """
        self.context.agent_state.update(state_delta)
        print(f"Agent {self.agent_name} (ctx: {self.context.id}, thread: {self.get_thread_id()}) updated state with delta: {state_delta}")
        print(f"Agent {self.agent_name} new state: {self.context.agent_state}")

    async def process_streamed_message(self, content: str, role: str = "user",
                                       attachments: Optional[List[Dict[str, Any]]] = None,
                                       incoming_state: Optional[Dict[str, Any]] = None,
                                       ui_response_data: Optional[Dict[str, Any]] = None):
        """
        Processes a message. If ui_response_data is present, it's data from a generative UI component.
        Enhanced with StreamProtocol event emission and state management.
        """
        print(f"Agent {self.agent_name}: process_streamed_message. Role='{role}', Content='{content[:50]}...'")

        if incoming_state:
            print(f"Agent {self.agent_name}: Received incoming state with message: {incoming_state}")
            await self.update_and_broadcast_agent_state(incoming_state, source_of_change="client_stream_input")

        # Handle UI response data if present
        if ui_response_data:
            ui_request_id = ui_response_data.get("ui_request_id")
            form_data = ui_response_data.get("data")
            print(f"Agent {self.agent_name}: Received UI response for request_id '{ui_request_id}': {form_data}")
            await self._emit_stream_event(
                StreamEventType.GENERATIVE_UI if STREAM_PROTOCOL_AVAILABLE else "generative_ui",
                {"request_id": ui_request_id, "data_received": form_data, "status": "response_received"}
            )
            # Store this UI response data in context or history for the agent to use
            self.hist_add_ui_response(ui_request_id, form_data)
            await self._emit_stream_event(
                StreamEventType.CONTEXT_UPDATE if STREAM_PROTOCOL_AVAILABLE else "context_update",
                {"type": "ui_response_added", "ui_request_id": ui_request_id}
            )

            if self.context.intervention_needed and self.context.intervention_prompt and ui_request_id in self.context.intervention_prompt:
                print(f"Agent {self.agent_name}: UI response received, resolving intervention for {ui_request_id}.")
                self.context.resolve_intervention()

        # Emit event that user message was received by the agent logic
        await self._emit_stream_event(
            StreamEventType.CONTEXT_UPDATE if STREAM_PROTOCOL_AVAILABLE else "context_update",
            {"role": role, "content": content, "status": "processing_started"}
        )

        # Update state with message info
        await self.update_and_broadcast_agent_state(
            {"last_user_message_received": content[:100]},
            source_of_change="user_message_ingestion"
        )

        # If it was a regular user message (not ui_response_data)
        if not ui_response_data and role.lower() == "user":
            # If the agent was waiting for intervention, this new user message resolves it.
            if self.context.intervention_needed:
                print(f"Agent {self.agent_name}: Received user message, resolving intervention.")
                self.context.resolve_intervention()
                # The halt_event is set, _check_and_handle_intervention will now pass.

            user_message = UserMessage(message=content, attachments=attachments or [])
            self.hist_add_user_message(user_message)
            await self._emit_stream_event(
                StreamEventType.CONTEXT_UPDATE if STREAM_PROTOCOL_AVAILABLE else "context_update",
                {"type": "user_message_added", "content_preview": content[:50]}
            )

        # Trigger monologue if it's a user message or if a UI response should trigger further processing
        if role.lower() == "user" or ui_response_data:
            final_agent_response_text = await self.monologue()

            # If monologue doesn't end with 'response' tool, emit the response here
            if final_agent_response_text and not self.last_tool_was_response_tool:
                await self._emit_stream_event(
                    StreamEventType.TEXT_MESSAGE_CONTENT if STREAM_PROTOCOL_AVAILABLE else "text_message_content",
                    {"role": "assistant", "content": final_agent_response_text}
                )

            # Reset the flag for next interaction
            self.last_tool_was_response_tool = False
            return final_agent_response_text
        else:
            print(f"Agent {self.agent_name} received non-user streamed message (role: {role}), not triggering monologue.")
            return None

    def hist_add_user_message(self, message: UserMessage):
        """Add user message to history"""
        self.context.history.add_message("user", message)
        print(f"Agent {self.agent_name} added user message to history: {message.message[:100]}...")

    def hist_add_ai_message(self, message: AIMessage):
        """Add AI message to history"""
        self.context.history.add_message("assistant", message)
        print(f"Agent {self.agent_name} added AI message to history: {message.message[:100]}...")

    def hist_add_tool_result(self, tool_name: str, result_text: str):
        """Add tool result to history"""
        tool_message = AIMessage(message=f"Tool '{tool_name}' result: {result_text}")
        self.context.history.add_message("assistant", tool_message)
        print(f"Agent {self.agent_name} added tool result to history: {tool_name} -> {result_text[:100]}...")

    def hist_add_ui_response(self, ui_request_id: str, form_data: Dict[str, Any]):
        """Add UI response to history"""
        ui_message = AIMessage(message=f"Data received from UI component (ID: {ui_request_id}): {json.dumps(form_data)}")
        self.context.history.add_message("system", ui_message)
        print(f"Agent {self.agent_name} added UI response to history: {ui_request_id} -> {str(form_data)[:100]}...")

    async def _get_stream_protocol_tool(self) -> Optional['StreamProtocolTool']:
        """Helper to get or create an instance of StreamProtocolTool."""
        if not STREAM_PROTOCOL_AVAILABLE:
            return None
            
        if not self._stream_protocol_tool_instance:
            try:
                self._stream_protocol_tool_instance = StreamProtocolTool(self)
            except Exception as e:
                print(f"Agent {self.agent_name}: Failed to initialize StreamProtocolTool: {e}")
                return None
        return self._stream_protocol_tool_instance

    async def _emit_stream_event(self, event_type, payload: Dict[str, Any]):
        """Convenience method for emitting stream events."""
        if not STREAM_PROTOCOL_AVAILABLE:
            print(f"Agent {self.agent_name}: StreamProtocol not available, skipping event {event_type}")
            return

        try:
            tool = await self._get_stream_protocol_tool()
            if tool:
                await tool.execute(
                    action="emit_event",
                    event_type=event_type.value if hasattr(event_type, 'value') else str(event_type),
                    payload=payload,
                    thread_id=self.get_thread_id(),
                    user_id=self.get_user_id()
                )
        except Exception as e:
            print(f"Agent {self.agent_name}: Error emitting stream event {event_type}: {e}")

    async def _emit_progress_update(self, message: str, percentage: Optional[float] = None,
                                   current_step: Optional[int] = None, total_steps: Optional[int] = None):
        """Helper method for emitting progress updates with optional progress indicators."""
        payload = {"message": message}
        if percentage is not None:
            payload["percentage"] = percentage
        if current_step is not None:
            payload["current_step"] = current_step
        if total_steps is not None:
            payload["total_steps"] = total_steps
        await self._emit_stream_event(
            StreamEventType.PROGRESS_UPDATE if STREAM_PROTOCOL_AVAILABLE else "progress_update",
            payload
        )

    async def _check_and_handle_intervention(self):
        """Checks if intervention is needed and waits if so."""
        if self.context.intervention_needed:
            # The HUMAN_INTERVENTION event should have been emitted when intervention_needed was set.
            # Here, we just log and wait.
            prompt = self.context.intervention_prompt or "Waiting for human input..."
            print(f"Agent {self.agent_name}: Pausing for human intervention. Prompt: '{prompt}'")
            await self._emit_progress_update(f"Waiting for human: {prompt}")

            # Wait for the halt_event to be set (by a new message or explicit resume)
            await self.context.halt_event.wait()

            # Once resumed:
            print(f"Agent {self.agent_name}: Resuming after intervention.")
            self.context.intervention_needed = False  # Clear the flag as it's being handled
            self.context.intervention_prompt = None
            await self._emit_stream_event(
                StreamEventType.HUMAN_INTERVENTION if STREAM_PROTOCOL_AVAILABLE else "human_intervention",
                {"status": "resolved"}
            )
            await self._emit_progress_update("Resuming operation...")

    async def _handle_intervention_request(self, prompt_for_human: str):
        """Handles the agent pausing for human intervention."""
        print(f"Agent {self.agent_name}: Requesting human intervention: {prompt_for_human}")
        self.context.request_intervention(prompt_for_human)

        await self._emit_stream_event(
            StreamEventType.HUMAN_INTERVENTION if STREAM_PROTOCOL_AVAILABLE else "human_intervention",
            {"prompt": prompt_for_human, "status": "required"}
        )

    async def _request_generative_ui(self, component_name: str, component_props: Dict[str, Any],
                                     request_id: Optional[str] = None) -> str:
        """
        Emits a GENERATIVE_UI event to request the frontend to render a component.
        Returns a request_id that the frontend should use when sending back data from this UI.
        """
        ui_request_id = request_id or f"ui_req_{str(uuid.uuid4())}"
        payload = {
            "request_id": ui_request_id,
            "component_name": component_name,  # e.g., "user_feedback_form", "data_table_viewer"
            "properties": component_props,     # Data to initialize the component
            "status": "request_render"
        }
        await self._emit_stream_event(
            StreamEventType.GENERATIVE_UI if STREAM_PROTOCOL_AVAILABLE else "generative_ui",
            payload
        )
        print(f"Agent {self.agent_name}: Requested generative UI '{component_name}' with ID '{ui_request_id}'.")
        return ui_request_id

    async def monologue(self) -> Optional[str]:
        """
        Agent's main reasoning loop with comprehensive StreamProtocol event emission.
        This handles the agent's thought process and tool usage with full event streaming.
        """
        print(f"Agent {self.agent_name} entering monologue...")
        self.iteration_no = 0

        # Emit initial progress and thought
        await self._emit_progress_update("Agent monologue started: Thinking...", percentage=5.0)
        await self._emit_stream_event(
            StreamEventType.AGENT_THOUGHT if STREAM_PROTOCOL_AVAILABLE else "agent_thought",
            {"content": "Starting to process the request."}
        )

        # Update state to indicate processing
        await self.update_and_broadcast_agent_state(
            {"status": "processing_monologue", "current_iteration": self.iteration_no}
        )

        max_iterations = 10  # Prevent infinite loops
        while self.iteration_no < max_iterations:
            self.iteration_no += 1

            # Check for intervention at start of each iteration
            await self._check_and_handle_intervention()

            # Emit iteration progress and thought
            current_thought = f"Iteration {self.iteration_no}: Analyzing current state and planning next action."
            await self._emit_stream_event(
                StreamEventType.AGENT_THOUGHT if STREAM_PROTOCOL_AVAILABLE else "agent_thought",
                {"content": current_thought}
            )
            await self._emit_progress_update(
                current_thought,
                percentage=(self.iteration_no / max_iterations) * 90.0
            )

            # Pre-LLM thought
            pre_llm_thought = "Preparing to query LLM for next action."
            await self._emit_stream_event(
                StreamEventType.AGENT_THOUGHT if STREAM_PROTOCOL_AVAILABLE else "agent_thought",
                {"content": pre_llm_thought}
            )

            # Get response from LLM
            response_json = await self._get_response(f"Processing user request (iteration {self.iteration_no})")

            if not response_json:
                err_msg = "LLM call failed. Human, please advise or provide new instructions."
                self.context.request_intervention(err_msg)
                await self._emit_stream_event(
                    StreamEventType.HUMAN_INTERVENTION if STREAM_PROTOCOL_AVAILABLE else "human_intervention",
                    {"prompt": err_msg, "status": "required", "details": {"reason": "LLM_FAILURE"}}
                )
                await self._check_and_handle_intervention()  # This will now pause
                # After resuming, the loop will continue, likely with new user input in history.
                continue  # Restart loop iteration to process potential new input

            # Post-LLM thought
            await self._emit_stream_event(
                StreamEventType.AGENT_THOUGHT if STREAM_PROTOCOL_AVAILABLE else "agent_thought",
                {"content": "LLM response received, parsing for action."}
            )
            
            # Extract thoughts from response_json and emit them
            agent_thoughts = response_json.get("thoughts", [])
            if isinstance(agent_thoughts, list) and agent_thoughts:
                for thought in agent_thoughts:
                    await self._emit_stream_event(
                        StreamEventType.AGENT_THOUGHT if STREAM_PROTOCOL_AVAILABLE else "agent_thought",
                        {"content": thought}
                    )
            elif isinstance(agent_thoughts, str) and agent_thoughts:
                await self._emit_stream_event(
                    StreamEventType.AGENT_THOUGHT if STREAM_PROTOCOL_AVAILABLE else "agent_thought",
                    {"content": agent_thoughts}
                )

            # Extract tool information from response
            tool_name, tool_args, tool_message = self._extract_tool_from_response(response_json)
            
            if tool_name:
                # Emit thought about tool execution
                await self._emit_stream_event(
                    StreamEventType.AGENT_THOUGHT if STREAM_PROTOCOL_AVAILABLE else "agent_thought",
                    {"content": f"Executing {tool_name} tool with parameters: {str(tool_args)[:100]}{'...' if len(str(tool_args)) > 100 else ''}"}
                )

                # Emit TOOL_CALL_START before execution
                await self._emit_stream_event(
                    StreamEventType.TOOL_CALL_START if STREAM_PROTOCOL_AVAILABLE else "tool_call_start",
                    {"tool_name": tool_name, "tool_args": tool_args}
                )
                
                # Simulate tool execution
                tool_response = await self._call_tool(tool_name, tool_args, tool_message)
                
                # Emit TOOL_CALL_END after execution
                await self._emit_stream_event(
                    StreamEventType.TOOL_CALL_END if STREAM_PROTOCOL_AVAILABLE else "tool_call_end",
                    {
                        "tool_name": tool_name,
                        "tool_args": tool_args,
                        "result": tool_response.get("message") if tool_response else None,
                        "error": tool_response.get("error") if tool_response else None,
                        "success": bool(tool_response and not tool_response.get("error"))
                    }
                )

                # Handle tool errors
                if tool_response and tool_response.get("error") and tool_name != "response":
                    # Example: Tool failed, ask human for help
                    err_msg = f"Tool '{tool_name}' failed with: {tool_response.get('message')}. What should I do next?"
                    self.context.request_intervention(err_msg)
                    await self._emit_stream_event(
                        StreamEventType.HUMAN_INTERVENTION if STREAM_PROTOCOL_AVAILABLE else "human_intervention",
                        {"prompt": err_msg, "status": "required", "details": {"reason": "TOOL_FAILURE", "tool_name": tool_name}}
                    )
                    await self._check_and_handle_intervention()
                    continue

                if tool_response and tool_response.get("break_loop"):
                    final_message = tool_response.get("message")
                    if tool_name == "response" and final_message:
                        self.last_tool_was_response_tool = True
                        await self._emit_stream_event(
                            StreamEventType.TEXT_MESSAGE_CONTENT if STREAM_PROTOCOL_AVAILABLE else "text_message_content",
                            {"role": "assistant", "content": final_message}
                        )
                        await self._emit_stream_event(
                            StreamEventType.SESSION_END if STREAM_PROTOCOL_AVAILABLE else "session_end",
                            {"reason": "Agent provided final response.", "thread_id": self.get_thread_id()}
                        )
                        await self._emit_progress_update("Task completed.", percentage=100.0)
                        return final_message

                # Add tool result to context and emit TOOL_RESULT event
                if tool_response:
                    tool_result_text = tool_response.get("message") if tool_response.get("message") else "Tool executed."

                    # Emit thought about processing tool result
                    await self._emit_stream_event(
                        StreamEventType.AGENT_THOUGHT if STREAM_PROTOCOL_AVAILABLE else "agent_thought",
                        {"content": f"Processing result from {tool_name}: {tool_result_text[:100]}{'...' if len(tool_result_text) > 100 else ''}"}
                    )

                    self.hist_add_tool_result(tool_name, tool_result_text)

                    # Emit TOOL_RESULT event with comprehensive result information
                    await self._emit_stream_event(
                        StreamEventType.TOOL_RESULT if STREAM_PROTOCOL_AVAILABLE else "tool_result",
                        {
                            "tool_name": tool_name,
                            "success": tool_response.get("success", True),
                            "message": tool_result_text,
                            "data": tool_response.get("data"),
                            "error": tool_response.get("error"),
                            "execution_time": tool_response.get("execution_time"),
                            "agent_id": self.agent_id,
                            "iteration": self.iteration_no
                        }
                    )

                    await self._emit_stream_event(
                        StreamEventType.CONTEXT_UPDATE if STREAM_PROTOCOL_AVAILABLE else "context_update",
                        {"type": "tool_result_added", "tool_name": tool_name}
                    )

                # Example: After a tool call, the agent decides it needs user input via a form
                if tool_name == "some_data_analysis_tool" and tool_response and tool_response.get("data"):
                    analysis_summary = tool_response.get("data", {}).get("summary")
                    if tool_response.get("data", {}).get("needs_clarification_via_form"):
                        form_fields = [
                            {"name": "param1", "label": "Parameter 1", "type": "text", "default": "valueA"},
                            {"name": "param2", "label": "Confirm Option", "type": "boolean", "default": True}
                        ]
                        ui_prompt = f"Analysis complete: {analysis_summary}. Please provide clarification using the form below for next steps."

                        # Emit the event to render a form
                        ui_request_id = await self._request_generative_ui(
                            component_name="clarification_form",
                            component_props={"title": "Clarification Needed", "fields": form_fields, "submit_button_text": "Submit Clarification"}
                        )

                        # Agent now needs to pause and wait for the UI interaction result.
                        intervention_prompt = f"{ui_prompt} (Awaiting form submission with ID: {ui_request_id})"
                        self.context.request_intervention(intervention_prompt)
                        await self._emit_stream_event(
                            StreamEventType.HUMAN_INTERVENTION if STREAM_PROTOCOL_AVAILABLE else "human_intervention",
                            {"prompt": intervention_prompt, "status": "required", "ui_request_id": ui_request_id}
                        )
                        await self._check_and_handle_intervention()  # This will pause
                        continue  # Restart loop to process form data
            else:
                # No tool identified, could be a direct textual response from LLM
                no_tool_message = response_json.get("response", response_json.get("answer", response_json.get("text")))
                if no_tool_message and isinstance(no_tool_message, str):
                    await self._emit_stream_event(
                        StreamEventType.TEXT_MESSAGE_CONTENT if STREAM_PROTOCOL_AVAILABLE else "text_message_content",
                        {"role": "assistant", "content": no_tool_message}
                    )
                    await self._emit_stream_event(
                        StreamEventType.SESSION_END if STREAM_PROTOCOL_AVAILABLE else "session_end",
                        {"reason": "Agent provided direct LLM response."}
                    )
                    await self._emit_progress_update("Task completed with direct response.", percentage=100.0)

                    response = AIMessage(message=no_tool_message)
                    self.hist_add_ai_message(response)
                    return no_tool_message
                else:
                    # LLM didn't call a tool and didn't provide a direct response text
                    await self._emit_stream_event(
                        StreamEventType.ERROR_EVENT if STREAM_PROTOCOL_AVAILABLE else "error_event",
                        {"error": "LLM did not call a tool nor provide a direct textual response."}
                    )
                    break

        # Monologue ended (max_iterations or other break condition)
        await self._emit_progress_update("Agent monologue finished.", percentage=100.0)
        await self.update_and_broadcast_agent_state(
            {"status": "idle", "reason": "Monologue ended by max_iterations or other condition."},
            source_of_change="monologue_completion"
        )
        return "I've processed your request to the best of my ability."

    async def _get_response(self, prompt: str) -> Dict[str, Any]:
        """Get response from LLM - enhanced placeholder with structured response"""
        print(f"Agent {self.agent_name} getting LLM response for prompt: {prompt[:100]}...")
        
        # Simulate a structured LLM response with thoughts and potential tool calls
        if "iteration 1" in prompt.lower():
            if "website" in prompt.lower() or "navigate" in prompt.lower() or "browser" in prompt.lower():
                return {
                    "thoughts": ["The user wants me to interact with a website.", "I should use the browser agent tool."],
                    "tool_name": "browser_agent",
                    "tool_args": {"action": "navigate", "url": "https://example.com"},
                    "response": "I'll help you navigate to that website."
                }
            else:
                return {
                    "thoughts": ["I need to understand what the user is asking for.", "Let me analyze their request carefully."],
                    "tool_name": "analyze",
                    "tool_args": {"query": prompt},
                    "response": "I'm analyzing your request."
                }
        elif "iteration" in prompt.lower():
            return {
                "thoughts": ["Based on my analysis, I can now provide a helpful response."],
                "tool_name": "response", 
                "tool_args": {"text": "I've processed your request and here's my response."},
                "response": "I've processed your request and here's my response."
            }
        else:
            return {
                "thoughts": ["Processing the user's message."],
                "response": "I understand and I'm here to help."
            }

    def _extract_tool_from_response(self, response_json: Dict[str, Any]) -> tuple:
        """Extract tool information from LLM response"""
        tool_name = response_json.get("tool_name")
        tool_args = response_json.get("tool_args", {})
        tool_message = response_json.get("response", "")
        return tool_name, tool_args, tool_message
    
    async def _call_tool(self, tool_name: str, tool_args: Dict[str, Any], tool_message: str) -> Dict[str, Any]:
        """Execute a tool call - enhanced with real tool execution"""
        print(f"Agent {self.agent_name} calling tool '{tool_name}' with args: {tool_args}")
        
        # Find the tool in registered tools
        tool_instance = None
        for tool in self.tools:
            if hasattr(tool, 'name') and tool.name == tool_name:
                tool_instance = tool
                break
        
        if tool_instance:
            try:
                # Capture execution timing
                import time
                start_time = time.time()

                # Execute the actual tool
                result = await tool_instance.execute(**tool_args)

                # Calculate execution time
                execution_time = time.time() - start_time

                # Convert tool response to expected format
                if hasattr(result, 'success') and hasattr(result, 'message'):
                    return {
                        "message": result.message,
                        "success": result.success,
                        "break_loop": getattr(result, 'break_loop', False),
                        "data": getattr(result, 'data', None),
                        "error": getattr(result, 'error', None) if not result.success else None,
                        "execution_time": execution_time
                    }
                else:
                    # Fallback for tools that don't return proper Response objects
                    return {
                        "message": str(result),
                        "success": True,
                        "break_loop": False,
                        "execution_time": execution_time
                    }
            except Exception as e:
                print(f"Agent {self.agent_name}: Error executing tool {tool_name}: {e}")
                return {
                    "message": f"Error executing tool {tool_name}: {str(e)}",
                    "break_loop": False,
                    "error": str(e)
                }
        else:
            # Fallback to simulated responses for unknown tools
            if tool_name == "response":
                return {
                    "message": tool_args.get("text", "Default response"),
                    "break_loop": True
                }
            elif tool_name == "analyze":
                return {
                    "message": f"Analysis complete for: {tool_args.get('query', 'unknown')}",
                    "break_loop": False
                }
            else:
                return {
                    "message": f"Tool {tool_name} not found - simulated execution",
                    "break_loop": False
                }

    def _register_default_tools(self):
        """Register default tools available to the agent"""
        try:
            # Register BrowserAgent tool
            from python.tools.browser_agent_tool import BrowserAgentTool
            browser_tool = BrowserAgentTool(self)
            self.add_tool(browser_tool)
        except ImportError as e:
            print(f"Agent {self.agent_name}: BrowserAgent tool not available: {e}")
        
        try:
            # Register WebCrawler tool
            from python.tools.web_crawler_tool import WebCrawlerTool
            web_crawler_tool = WebCrawlerTool(self)
            self.add_tool(web_crawler_tool)
        except ImportError as e:
            print(f"Agent {self.agent_name}: WebCrawler tool not available: {e}")
        
        try:
            # Register KnowledgeAgent tool
            from python.tools.knowledge_agent_tool import KnowledgeAgentTool
            knowledge_agent_tool = KnowledgeAgentTool(self)
            self.add_tool(knowledge_agent_tool)
        except ImportError as e:
            print(f"Agent {self.agent_name}: KnowledgeAgent tool not available: {e}")
        
        try:
            # Register MemoryAgent tool
            from python.tools.memory_agent_tool import MemoryAgentTool
            memory_agent_tool = MemoryAgentTool(self)
            self.add_tool(memory_agent_tool)
        except ImportError as e:
            print(f"Agent {self.agent_name}: MemoryAgent tool not available: {e}")
        
        try:
            # Register HybridMemory tool
            from python.tools.hybrid_memory_tool import HybridMemoryTool
            hybrid_memory_tool = HybridMemoryTool(self)
            self.add_tool(hybrid_memory_tool)
        except ImportError as e:
            print(f"Agent {self.agent_name}: HybridMemory tool not available: {e}")
        
        try:
            # Register ChatterboxTTS tool
            from python.tools.chatterbox_tts_tool import ChatterboxTTSTool
            chatterbox_tts_tool = ChatterboxTTSTool(self)
            self.add_tool(chatterbox_tts_tool)
        except ImportError as e:
            print(f"Agent {self.agent_name}: ChatterboxTTS tool not available: {e}")
        
        try:
            # Register Response tool
            from python.tools.response import ResponseTool
            response_tool = ResponseTool(self)
            self.add_tool(response_tool)
        except ImportError as e:
            print(f"Agent {self.agent_name}: Response tool not available: {e}")
    
    def add_tool(self, tool):
        """Add a tool to the agent"""
        self.tools.append(tool)
        print(f"Agent {self.agent_name} added tool: {tool.name if hasattr(tool, 'name') else tool}")
    
    async def _extract_and_call_tool(self, response: str) -> Optional[Dict[str, Any]]:
        """Extract and execute tool calls - placeholder for compatibility"""
        print(f"Agent {self.agent_name} checking for tool calls in response...")
        return None