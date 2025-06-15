# agent.py - Agent Zero core agent and context classes with StreamProtocol enhancements
import asyncio
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

        # StreamTransport will be managed globally
        self.stream_transport: Optional[Any] = None

        AgentContext._instances[self.id] = self
        print(f"AgentContext created: id={self.id}, name='{self.name}', thread_id='{self.thread_id}', user_id='{self.user_id}'")

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

    def update_agent_state(self, state_delta: Dict[str, Any]):
        """
        Updates the agent's persistent state associated with the AG-UI protocol.
        This state is managed per thread_id.
        """
        self.context.agent_state.update(state_delta)
        # TODO: Persist this state if necessary (e.g., if it needs to survive server restarts)
        # For now, it's in-memory per context.
        print(f"Agent {self.agent_name} (ctx: {self.context.id}, thread: {self.get_thread_id()}) updated state with delta: {state_delta}")
        print(f"Agent {self.agent_name} new state: {self.context.agent_state}")

    async def process_streamed_message(self, content: str, role: str = "user", attachments: Optional[List[Dict[str, Any]]] = None):
        """
        Processes a message received via the StreamProtocol, adds it to history,
        and triggers the agent's monologue if it's a user message.
        Enhanced with StreamProtocol event emission.
        """
        print(f"Agent {self.agent_name} (ctx: {self.context.id}, thread: {self.get_thread_id()}) processing streamed message: Role='{role}', Content='{content[:100]}...'")
        
        # Emit event that user message was received by the agent logic
        await self._emit_stream_event(
            StreamEventType.CONTEXT_UPDATE if STREAM_PROTOCOL_AVAILABLE else "context_update",
            {"role": role, "content": content, "status": "processing_started"}
        )

        if role.lower() == "user":
            user_message = UserMessage(message=content, attachments=attachments or [])
            self.hist_add_user_message(user_message)
            
            # Trigger monologue which will emit its own events
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

    async def monologue(self) -> Optional[str]:
        """
        Agent's main reasoning loop with StreamProtocol event emission.
        This handles the agent's thought process and tool usage with full event streaming.
        """
        print(f"Agent {self.agent_name} entering monologue...")
        self.iteration_no = 0
        
        # Emit an initial thought
        await self._emit_stream_event(
            StreamEventType.AGENT_THOUGHT if STREAM_PROTOCOL_AVAILABLE else "agent_thought",
            {"content": "Starting to process the request."}
        )

        max_iterations = 10  # Prevent infinite loops
        while self.iteration_no < max_iterations:
            self.iteration_no += 1
            
            # Emit a general "thinking" thought before LLM call in each iteration
            await self._emit_stream_event(
                StreamEventType.AGENT_THOUGHT if STREAM_PROTOCOL_AVAILABLE else "agent_thought",
                {"content": f"Iteration {self.iteration_no}: Preparing to analyze the request."}
            )

            # Simulate getting response from LLM
            response_json = await self._get_response(f"Processing user request (iteration {self.iteration_no})")
            
            if not response_json:
                await self._emit_stream_event(
                    StreamEventType.ERROR_EVENT if STREAM_PROTOCOL_AVAILABLE else "error_event",
                    {"error": "LLM did not return a valid response."}
                )
                break
            
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
                        "error": tool_response.get("error") if tool_response else None
                    }
                )

                if tool_response and tool_response.get("break_loop"):
                    # If it's the 'response' tool (or any tool that breaks loop and provides final answer)
                    if tool_name == "response" and tool_response.get("message"):
                        self.last_tool_was_response_tool = True
                        await self._emit_stream_event(
                            StreamEventType.TEXT_MESSAGE_CONTENT if STREAM_PROTOCOL_AVAILABLE else "text_message_content",
                            {"role": "assistant", "content": tool_response["message"]}
                        )
                        await self._emit_stream_event(
                            StreamEventType.PROGRESS_UPDATE if STREAM_PROTOCOL_AVAILABLE else "progress_update",
                            {"status": "completed", "reason": "Final response provided by agent."}
                        )
                        return tool_response["message"]
            else:
                # No tool needed, provide direct response
                response_text = response_json.get("response", "I understand your request and I'm working on it.")
                
                # Emit final response
                await self._emit_stream_event(
                    StreamEventType.TEXT_MESSAGE_CONTENT if STREAM_PROTOCOL_AVAILABLE else "text_message_content",
                    {"role": "assistant", "content": response_text}
                )
                
                response = AIMessage(message=response_text)
                self.hist_add_ai_message(response)
                return response_text

        # If monologue loop finishes without completion
        await self._emit_stream_event(
            StreamEventType.STATE_DELTA if STREAM_PROTOCOL_AVAILABLE else "state_delta",
            {"status": "idle", "message": "Agent has completed processing or reached iteration limit."}
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
                # Execute the actual tool
                result = await tool_instance.execute(**tool_args)
                
                # Convert tool response to expected format
                if hasattr(result, 'success') and hasattr(result, 'message'):
                    return {
                        "message": result.message,
                        "break_loop": getattr(result, 'break_loop', False),
                        "data": getattr(result, 'data', None),
                        "error": getattr(result, 'error', None) if not result.success else None
                    }
                else:
                    # Fallback for tools that don't return proper Response objects
                    return {
                        "message": str(result),
                        "break_loop": False
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