# agent.py - Agent Zero core agent and context classes with StreamProtocol enhancements
import asyncio
import uuid
from typing import Optional, Dict, Any, List
from dataclasses import dataclass
from datetime import datetime

# Placeholder imports - these would come from actual Agent Zero codebase
class Log:
    def __init__(self, context_id: str):
        self.context_id = context_id
        print(f"Log initialized for context {context_id}")

class History:
    def __init__(self, context):
        self.context = context
        self.messages = []
        print(f"History initialized for context {context.id}")

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
        self.log: Log = Log(self.id)
        self.config: AgentConfig = settings.get_agent_config()
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
        """
        print(f"Agent {self.agent_name} (ctx: {self.context.id}, thread: {self.get_thread_id()}) processing streamed message: Role='{role}', Content='{content[:100]}...'")
        if role.lower() == "user":
            user_message = UserMessage(message=content, attachments=attachments or [])
            self.hist_add_user_message(user_message)
            
            # Trigger monologue for the agent to respond
            # The monologue will eventually use StreamProtocolTool to emit its thoughts/responses
            return await self.monologue()
        else:
            # Handle other roles if necessary (e.g., system messages via stream)
            # For now, we primarily expect 'user' role to trigger agent action.
            print(f"Agent {self.agent_name} received non-user streamed message (role: {role}), not triggering monologue.")
            return None

    def hist_add_user_message(self, message: UserMessage):
        """Add user message to history"""
        self.context.history.messages.append(("user", message))
        print(f"Agent {self.agent_name} added user message to history: {message.message[:100]}...")

    def hist_add_ai_message(self, message: AIMessage):
        """Add AI message to history"""
        self.context.history.messages.append(("assistant", message))
        print(f"Agent {self.agent_name} added AI message to history: {message.message[:100]}...")

    async def monologue(self):
        """
        Agent's main reasoning loop - placeholder for actual implementation.
        This would normally handle the agent's thought process and tool usage.
        """
        print(f"Agent {self.agent_name} entering monologue...")
        # Placeholder implementation
        # In real Agent Zero, this would:
        # 1. Get response from LLM
        # 2. Extract and execute tool calls
        # 3. Emit events via StreamProtocolTool
        # 4. Continue until task complete
        
        # For now, just echo back
        response = AIMessage(message="I received your message and I'm processing it.")
        self.hist_add_ai_message(response)
        return response

    async def _get_response(self, prompt: str) -> str:
        """Get response from LLM - placeholder"""
        print(f"Agent {self.agent_name} getting LLM response for prompt: {prompt[:100]}...")
        return "This is a placeholder LLM response."

    async def _extract_and_call_tool(self, response: str) -> Optional[Dict[str, Any]]:
        """Extract and execute tool calls - placeholder"""
        print(f"Agent {self.agent_name} checking for tool calls in response...")
        return None

    def add_tool(self, tool):
        """Add a tool to the agent"""
        self.tools.append(tool)
        print(f"Agent {self.agent_name} added tool: {tool.name if hasattr(tool, 'name') else tool}")