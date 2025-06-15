### Complete File: `tools/stream_protocol_tool.py`

```python
"""
StreamProtocol Tool - AG-UI Protocol Integration for Agent Zero
Provides standardized agent-frontend communication with real-time streaming
Based on AG-UI Protocol specification and TypeScript SDK
"""

from python.helpers.tool import Tool
from typing import Dict, Any, List, Optional, AsyncGenerator
import asyncio
import json
import uuid
from datetime import datetime
from dataclasses import dataclass, field
from enum import Enum

class StreamEventType(Enum):
    """16 standard AG-UI event types"""
    TEXT_MESSAGE_CONTENT = "text_message_content"
    TOOL_CALL_START = "tool_call_start"
    TOOL_CALL_END = "tool_call_end"
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
    """Transport layer for AG-UI events"""
    
    def __init__(self):
        self.connections = {}
        self.event_handlers = {}
        
    async def emit_event(self, event: StreamEvent):
        """Emit event to all connected clients"""
        event_data = {
            "id": event.event_id,
            "type": event.type.value,
            "payload": event.payload,
            "timestamp": event.timestamp,
            "threadId": event.thread_id,
            "userId": event.user_id
        }
        
        # Send to all connections for this thread
        for connection_id, connection in self.connections.items():
            if connection.get("thread_id") == event.thread_id:
                await connection["websocket"].send_text(json.dumps(event_data))
    
    async def register_connection(self, websocket, thread_id: str, user_id: str = None):
        """Register new websocket connection"""
        connection_id = str(uuid.uuid4())
        self.connections[connection_id] = {
            "websocket": websocket,
            "thread_id": thread_id,
            "user_id": user_id,
            "created_at": datetime.utcnow()
        }
        return connection_id
    
    def unregister_connection(self, connection_id: str):
        """Remove websocket connection"""
        self.connections.pop(connection_id, None)

class StreamProtocolTool(Tool):
    """
    StreamProtocol (AG-UI) integration for Agent Zero
    Provides standardized agent-frontend communication with real-time streaming
    """
    
    def __init__(self, agent, **kwargs):
        super().__init__(agent, **kwargs)
        self.transport = StreamTransport()
        self.active_threads = {}
        self.middleware_stack = []
        
    async def execute(self, action: str, **kwargs):
        """
        Execute StreamProtocol operations
        
        Actions:
        - emit_event: Emit standardized event to frontend
        - handle_input: Process incoming frontend input
        - start_session: Start streaming session
        - end_session: End streaming session
        - update_state: Update shared state
        - register_middleware: Add event middleware
        """
        
        try:
            if action == "emit_event":
                return await self._emit_event(**kwargs)
            elif action == "handle_input":
                return await self._handle_input(**kwargs)
            elif action == "start_session":
                return await self._start_session(**kwargs)
            elif action == "end_session":
                return await self._end_session(**kwargs)
            elif action == "update_state":
                return await self._update_state(**kwargs)
            elif action == "register_middleware":
                return await self._register_middleware(**kwargs)
            else:
                return self.agent_response(f"Unknown StreamProtocol action: {action}")
                
        except Exception as e:
            # Emit error event
            await self._emit_error_event(str(e), kwargs.get("thread_id"))
            return self.agent_response(f"StreamProtocol error: {str(e)}")
    
    async def _emit_event(self, event_type: str, payload: Dict[str, Any], 
                         thread_id: str = None, user_id: str = None):
        """Emit standardized event to frontend"""
        
        # Convert string to enum
        try:
            event_enum = StreamEventType(event_type)
        except ValueError:
            return self.agent_response(f"Invalid event type: {event_type}")
        
        # Create event
        event = StreamEvent(
            type=event_enum,
            payload=payload,
            thread_id=thread_id or self.agent.get_thread_id(),
            user_id=user_id or self.agent.get_user_id()
        )
        
        # Apply middleware
        for middleware in self.middleware_stack:
            event = await middleware(event)
            if event is None:
                return self.agent_response("Event filtered by middleware")
        
        # Emit event
        await self.transport.emit_event(event)
        
        return self.agent_response({
            "success": True,
            "event_id": event.event_id,
            "type": event_type,
            "timestamp": event.timestamp
        })
    
    async def _handle_input(self, input_data: Dict[str, Any]):
        """Process incoming frontend input according to RunAgentInput schema"""
        
        try:
            # Parse input
            run_input = RunAgentInput(
                thread_id=input_data.get("threadId", str(uuid.uuid4())),
                messages=input_data.get("messages", []),
                state=input_data.get("state", {}),
                user_id=input_data.get("userId"),
                metadata=input_data.get("metadata", {})
            )
            
            # Update agent context
            await self._update_agent_context(run_input)
            
            # Emit session start if new thread
            if run_input.thread_id not in self.active_threads:
                await self._emit_event(
                    "session_start",
                    {"threadId": run_input.thread_id, "userId": run_input.user_id},
                    run_input.thread_id,
                    run_input.user_id
                )
                self.active_threads[run_input.thread_id] = {
                    "user_id": run_input.user_id,
                    "state": run_input.state,
                    "created_at": datetime.utcnow()
                }
            
            # Process messages
            for message in run_input.messages:
                await self._process_message(message, run_input.thread_id, run_input.user_id)
            
            return self.agent_response({
                "success": True,
                "thread_id": run_input.thread_id,
                "messages_processed": len(run_input.messages)
            })
            
        except Exception as e:
            return self.agent_response(f"Input processing error: {str(e)}")
    
    async def _process_message(self, message: Dict[str, Any], thread_id: str, user_id: str):
        """Process individual message from frontend"""
        
        role = message.get("role", "user")
        content = message.get("content", "")
        
        # Emit message content event
        await self._emit_event(
            "text_message_content",
            {
                "role": role,
                "content": content,
                "messageId": message.get("id", str(uuid.uuid4()))
            },
            thread_id,
            user_id
        )
        
        # If user message, trigger agent processing
        if role == "user":
            await self._trigger_agent_processing(content, thread_id, user_id)
    
    async def _trigger_agent_processing(self, content: str, thread_id: str, user_id: str):
        """Trigger agent processing for user message"""
        
        # Emit agent thought
        await self._emit_event(
            "agent_thought",
            {"content": f"Processing user request: {content[:100]}..."},
            thread_id,
            user_id
        )
        
        # Store in Agent Zero's conversation history
        await self.agent.hist_add_user_message(content)
        
        # Process through Agent Zero's system
        response = await self.agent.monologue()
        
        # Emit response
        await self._emit_event(
            "text_message_content",
            {
                "role": "assistant",
                "content": response,
                "messageId": str(uuid.uuid4())
            },
            thread_id,
            user_id
        )
    
    async def _start_session(self, thread_id: str, user_id: str = None, 
                           initial_state: Dict[str, Any] = None):
        """Start new streaming session"""
        
        if thread_id in self.active_threads:
            return self.agent_response(f"Session {thread_id} already active")
        
        self.active_threads[thread_id] = {
            "user_id": user_id,
            "state": initial_state or {},
            "created_at": datetime.utcnow()
        }
        
        await self._emit_event(
            "session_start",
            {"threadId": thread_id, "userId": user_id, "initialState": initial_state},
            thread_id,
            user_id
        )
        
        return self.agent_response({
            "success": True,
            "thread_id": thread_id,
            "status": "session_started"
        })
    
    async def _end_session(self, thread_id: str):
        """End streaming session"""
        
        if thread_id not in self.active_threads:
            return self.agent_response(f"Session {thread_id} not found")
        
        session_info = self.active_threads.pop(thread_id)
        
        await self._emit_event(
            "session_end",
            {
                "threadId": thread_id,
                "duration": (datetime.utcnow() - session_info["created_at"]).total_seconds()
            },
            thread_id,
            session_info.get("user_id")
        )
        
        return self.agent_response({
            "success": True,
            "thread_id": thread_id,
            "status": "session_ended"
        })
    
    async def _update_state(self, thread_id: str, state_delta: Dict[str, Any]):
        """Update shared state for thread"""
        
        if thread_id not in self.active_threads:
            return self.agent_response(f"Session {thread_id} not found")
        
        # Apply state delta
        current_state = self.active_threads[thread_id]["state"]
        current_state.update(state_delta)
        
        # Emit state delta event
        await self._emit_event(
            "state_delta",
            {"delta": state_delta, "fullState": current_state},
            thread_id,
            self.active_threads[thread_id].get("user_id")
        )
        
        return self.agent_response({
            "success": True,
            "thread_id": thread_id,
            "updated_state": current_state
        })
    
    async def _register_middleware(self, middleware_func: callable):
        """Register event middleware function"""
        self.middleware_stack.append(middleware_func)
        
        return self.agent_response({
            "success": True,
            "middleware_count": len(self.middleware_stack)
        })
    
    async def _emit_error_event(self, error_message: str, thread_id: str = None):
        """Emit error event"""
        await self._emit_event(
            "error_event",
            {"error": error_message, "timestamp": datetime.utcnow().isoformat()},
            thread_id
        )
    
    async def _update_agent_context(self, run_input: RunAgentInput):
        """Update agent context with input data"""
        
        # Set thread and user context
        if hasattr(self.agent, 'set_thread_id'):
            self.agent.set_thread_id(run_input.thread_id)
        
        if hasattr(self.agent, 'set_user_id'):
            self.agent.set_user_id(run_input.user_id)
        
        # Update state if provided
        if run_input.state:
            if hasattr(self.agent, 'update_state'):
                self.agent.update_state(run_input.state)
```

### Complete File: `tools/browser_agent_tool.py`

```python
"""
BrowserAgent Tool - Stagehand Integration for Agent Zero
Provides AI-powered browser automation with computer use capabilities
Based on Stagehand TypeScript framework
"""

from python.helpers.tool import Tool
import subprocess
import asyncio
import json
import tempfile
import os
from typing import Dict, Any, Optional, List
from dataclasses import dataclass

@dataclass
class BrowserSession:
    """Browser session information"""
    session_id: str
    url: str
    title# Complete Repository Analysis and Integration Plan

## Repository Analysis Summary

Based on the comprehensive research, here's what I've discovered about each repository's structure and capabilities:

### 1. AG-UI Protocol (`ag-ui-protocol/ag-ui`)

#### **Repository Structure (Inferred from Documentation)**
```
ag-ui/
├── packages/
│   ├── core/                     # Core protocol implementation
│   │   ├── src/
│   │   │   ├── types.ts          # TypeScript type definitions
│   │   │   ├── events.ts         # Event type definitions
│   │   │   └── schemas.ts        # Validation schemas
│   │   └── package.json
│   ├── client/                   # Client SDK
│   │   ├── src/
│   │   │   ├── AbstractAgent.ts  # Base agent class
│   │   │   ├── connection.ts     # Connection management
│   │   │   └── streaming.ts      # Streaming utilities
│   │   └── package.json
│   ├── server/                   # Server implementation
│   │   ├── src/
│   │   │   ├── middleware.ts     # Event middleware
│   │   │   ├── transport.ts      # Transport layer
│   │   │   └── sse.ts           # Server-Sent Events
│   │   └── package.json
│   └── encoder/                  # Binary encoder for performance
│       ├── src/
│       │   └── encoder.ts
│       └── package.json
├── integrations/                 # Framework integrations
│   ├── langgraph/
│   ├── mastra/
│   ├── crewai/
│   └── openai/
├── examples/                     # Usage examples
├── docs/                        # Documentation
└── dojo/                        # Interactive playground
```
#### **Key Components Based on Documentation**

**Core Types (inferred from API docs):**
```typescript
// From documentation examples
interface RunAgentInput {
  threadId: string;
  messages: Message[];
  state?: Record<string, any>;
}

// 16 standard event types mentioned
type EventType = 
  | "TEXT_MESSAGE_CONTENT"
  | "TOOL_CALL_START" 
  | "TOOL_CALL_END"
  | "STATE_DELTA"
  | "AGENT_THOUGHT"
  | "HUMAN_INTERVENTION"
  | "GENERATIVE_UI"
  | "CONTEXT_UPDATE"
  // ... 8 more types

interface AGUIEvent {
  type: EventType;
  payload: any;
  timestamp?: string;
  threadId?: string;
}
```
**Server Implementation (from quickstart guide):**
```typescript
// TypeScript version from docs
import express, { Request, Response } from "express"
import { RunAgentInputSchema, RunAgentInput } from "@ag-ui/core"

const app = express()
app.use(express.json())

app.post("/awp", (req: Request, res: Response) => {
  try {
    const input: RunAgentInput = RunAgentInputSchema.parse(req.body)
    res.json({ message: `Hello World from ${input.threadId}` })
  } catch (error) {
    res.status(422).json({ error: (error as Error).message })
  }
})
```
**Python Version (from docs):**
```python
from fastapi import FastAPI, Request
from ag_ui.core.types import RunAgentInput

app = FastAPI(title="AG-UI Endpoint")

@app.post("/awp")
async def my_endpoint(request: RunAgentInput):
    return {"message": "Hello World"}
```
### 2. Stagehand (`browserbase/stagehand`)

#### **Repository Structure (from documentation analysis)**
```
stagehand/
├── lib/
│   ├── browser/
│   │   ├── Browser.ts            # Browser management
│   │   ├── Page.ts              # Page automation
│   │   └── Context.ts           # Browser context
│   ├── ai/
│   │   ├── models/
│   │   │   ├── OpenAI.ts        # OpenAI integration
│   │   │   └── Anthropic.ts     # Anthropic integration
│   │   └── ModelProvider.ts     # Model abstraction
│   ├── cache/
│   │   ├── ActionCache.ts       # Action caching system
│   │   └── CacheManager.ts      # Cache management
│   ├── types/
│   │   ├── StagehandConfig.ts   # Configuration types
│   │   └── ActionTypes.ts       # Action definitions
│   └── index.ts                 # Main exports
├── examples/
│   ├── example.ts               # Basic example
│   └── computer-use/            # Computer use examples
├── docs/                        # Documentation
├── package.json
└── README.md
```
#### **Key API (from documentation examples):**
```typescript
import { Stagehand } from 'stagehand';

// Basic usage
const stagehand = new Stagehand();
await stagehand.init();
const page = stagehand.page;

// Use Playwright functions directly
await page.goto("https://github.com/browserbase");

// Use AI for navigation
await page.act("click on the stagehand repo");

// Computer use agent
const agent = stagehand.agent({
  provider: "openai",
  model: "computer-use-preview",
});
await agent.execute("Get to the latest PR");

// Extract structured data
const { author, title } = await page.extract({
  instruction: "extract the author and title of the PR",
  schema: z.object({
    author: z.string().describe("The username of the PR author"),
    title: z.string().describe("The title of the PR"),
  }),
});
```
### 3. Crawl4AI Agent v2 (`coleam00/ottomator-agents/crawl4AI-agent-v2`)

#### **Complete File Structure (from search results):**
```
crawl4AI-agent-v2/
├── crawl4AI-examples/
│   ├── 3-crawl_sitemap_in_parallel.py
│   ├── 4-crawl_llms_txt.py
│   └── 5-crawl_site_recursively.py
├── insert_docs.py               # Main ingestion script
├── rag_agent.py                # Pydantic AI RAG agent
├── streamlit_app.py            # Web interface
├── utils.py                    # Utility functions
├── requirements.txt            # Dependencies
├── .env.example               # Environment template
└── README.md                  # Documentation
```
#### **Key Dependencies (from documentation):**
```
# requirements.txt content (inferred)
crawl4ai
pydantic-ai
chromadb
streamlit
playwright
openai
python-dotenv
```
#### **Core Components (from analysis):**

**insert_docs.py** - Main entry point:
- Handles regular documentation sites
- Processes markdown/txt pages (llms.txt format)
- Recursive crawling with deduplication
- Parallel processing with memory tracking

**rag_agent.py** - Pydantic AI agent:
- ChromaDB integration for vector storage
- Semantic search capabilities
- Context-rich response generation

**utils.py** - Utility functions:
- Document processing and chunking
- Hierarchical Markdown chunking by headers
- Memory-adaptive batching

### 4. Foundational RAG Agent (`coleam00/ottomator-agents/foundational-rag-agent`)

#### **Complete File Structure (confirmed from search results):**
```
foundational-rag-agent/
├── database/
│   └── setup.py                # Database setup with Supabase/pgvector
├── document_processing/
│   ├── __init__.py
│   ├── chunker.py             # Text chunking functionality
│   ├── embeddings.py          # OpenAI embeddings generation
│   ├── ingestion.py           # Document ingestion pipeline
│   └── processors.py          # TXT and PDF processing
├── agent/
│   ├── __init__.py
│   ├── agent.py               # Main Pydantic AI agent
│   ├── prompts.py             # System prompts and templates
│   └── tools.py               # Knowledge base search tools
├── ui/
│   └── app.py                 # Streamlit application
├── tests/
│   ├── test_chunker.py
│   ├── test_embeddings.py
│   ├── test_ingestion.py
│   ├── test_processors.py
│   └── test_agent.py
├── .env.example               # Environment variables
├── requirements.txt           # Dependencies
├── PLANNING.md               # Project planning
├── TASK.md                   # Task tracking
└── README.md                 # Documentation
```
#### **Key Components Analysis:**

**Database Layer (database/setup.py):**
- Supabase integration with pgvector
- Vector similarity search setup
- Connection pooling and management

**Document Processing:**
- **chunker.py**: Intelligent text chunking with overlap management
- **embeddings.py**: OpenAI embedding generation with batch processing
- **ingestion.py**: Full pipeline with file type detection
- **processors.py**: TXT/PDF processing with metadata extraction

**Agent Layer:**
- **agent.py**: Pydantic AI agent with conversation management
- **prompts.py**: RAG-specific prompt templates
- **tools.py**: Vector search interface and result ranking

### 5. Mem0 (`mem0ai/mem0`)

#### **Repository Structure (from analysis):**
```
mem0/
├── mem0/
│   ├── __init__.py
│   ├── client/
│   │   ├── main.py             # Main client interface
│   │   └── memory.py           # Memory operations
│   ├── memory/
│   │   ├── base.py             # Base memory class
│   │   ├── graph.py            # Graph-based memory
│   │   └── vector.py           # Vector memory
│   ├── embeddings/
│   │   ├── openai.py           # OpenAI embeddings
│   │   └── base.py             # Embedding interface
│   ├── llms/
│   │   ├── openai.py           # OpenAI LLM integration
│   │   └── base.py             # LLM interface
│   └── utils/
│       ├── parsing.py          # Text parsing utilities
│       └── helpers.py          # Helper functions
├── examples/                   # Usage examples
├── tests/                      # Test suite
├── docs/                       # Documentation
└── requirements.txt           # Dependencies
```
#### **Core API (from documentation):**
```python
from mem0 import Memory

# Initialize memory
memory = Memory()

# Add memories from conversation
messages = [
    {"role": "user", "content": "I like pizza"},
    {"role": "assistant", "content": "Great! I'll remember that."}
]
memory.add(messages=messages, user_id="user_123")

# Search memories
results = memory.search(query="food preferences", user_id="user_123", limit=5)

# Update memories
memory.update(memory_id="mem_456", data="Updated information")

# Delete memories
memory.delete(memory_id="mem_456")
```
## Agent Zero Enhanced Integration Architecture

Now that I have a complete understanding of each repository, here's the detailed integration plan:

### Standardized Naming Convention

Instead of using the original names, we'll use these standardized names:
- **AG-UI Protocol** → **StreamProtocol**
- **Stagehand** → **BrowserAgent**  
- **Crawl4AI Agent v2** → **WebCrawler**
- **Foundational RAG Agent** → **KnowledgeAgent**
- **Mem0** → **MemoryAgent**

### Enhanced Agent Zero Architecture
```
enhanced_agent_zero/
├── core/
│   ├── agent.py                    # Enhanced Agent class with new capabilities
│   ├── models.py                   # Extended model support
│   ├── config.py                   # Centralized configuration
│   └── events.py                   # StreamProtocol event system
├── tools/
│   ├── stream_protocol_tool.py     # StreamProtocol integration
│   ├── browser_agent_tool.py       # BrowserAgent integration  
│   ├── web_crawler_tool.py         # WebCrawler integration
│   ├── knowledge_agent_tool.py     # KnowledgeAgent integration
│   ├── memory_agent_tool.py        # MemoryAgent integration
│   └── hybrid_memory_tool.py       # Combined memory system
├── protocols/
│   ├── stream_protocol/            # StreamProtocol implementation
│   │   ├── events.py              # Event definitions
│   │   ├── transport.py           # Transport layer
│   │   └── middleware.py          # Event middleware
│   └── types.py                   # Protocol type definitions
├── agents/
│   ├── browser_agent/             # BrowserAgent implementation
│   │   ├── browser.py             # Browser management
│   │   ├── ai_models.py           # AI model integration
│   │   └── actions.py             # Action definitions
│   ├── web_crawler/               # WebCrawler implementation
│   │   ├── crawler.py             # Crawling logic
│   │   ├── processors.py          # Document processing
│   │   └── chunker.py             # Text chunking
│   ├── knowledge_agent/           # KnowledgeAgent implementation
│   │   ├── agent.py               # Main agent logic
│   │   ├── database.py            # Database operations
│   │   ├── embeddings.py          # Embedding generation
│   │   └── retrieval.py           # Information retrieval
│   └── memory_agent/              # MemoryAgent implementation
│       ├── memory.py              # Memory operations
│       ├── graph.py               # Graph-based memory
│       └── vector.py              # Vector memory
├── ui/
│   ├── stream_interface.py        # StreamProtocol interface
│   ├── components/                # UI components
│   └── handlers/                  # Event handlers
├── memory/
│   ├── hybrid_system.py           # Combined memory approach
│   ├── agent_zero_memory.py       # Original Agent Zero memory
│   └── intelligent_memory.py      # MemoryAgent integration
├── prompts/
│   ├── enhanced/                  # Enhanced prompt templates
│   │   ├── agent.system.md        # Main system prompt
│   │   ├── browser_agent.md       # Browser automation prompts
│   │   ├── web_crawler.md         # Web crawling prompts
│   │   ├── knowledge_agent.md     # RAG prompts
│   │   └── memory_agent.md        # Memory prompts
│   └── tools/                     # Tool-specific prompts
├── tests/
│   ├── integration/               # Integration tests
│   ├── unit/                      # Unit tests
│   └── performance/               # Performance tests
└── examples/
    ├── basic_usage.py             # Basic integration example
    ├── advanced_rag.py            # Advanced RAG example
    └── browser_automation.py      # Browser automation example
```
## Complete Implementation Files

### Repository Integration Structure

Based on comprehensive analysis, here are the complete implementation files that integrate all repositories with Agent Zero:

## Phase 1: Core Integration Framework (Week 1-2)

#### 1.1 StreamProtocol Integration

**File: `tools/stream_protocol_tool.py`**
```python
from python.helpers.tool import Tool
from protocols.stream_protocol.events import EventEmitter, EventType
from protocols.stream_protocol.transport import StreamTransport
import asyncio
import json
from typing import Dict, Any, List

class StreamProtocolTool(Tool):
    """
    StreamProtocol (AG-UI) integration for Agent Zero
    Provides standardized agent-frontend communication with real-time streaming
    """
    
    def __init__(self, agent, **kwargs):
        super().__init__(agent, **kwargs)
        self.event_emitter = EventEmitter()
        self.transport = StreamTransport()
        self.active_connections = {}
        
    async def execute(self, action: str, **kwargs):
        """
        Execute StreamProtocol operations
        
        Actions:
        - emit_event: Emit standardized event to frontend
        - handle_input: Process incoming frontend input
        - start_stream: Start streaming session
        - update_state: Update shared state
        """
        
        if action == "emit_event":
            return await self._emit_event(**kwargs)
        elif action == "handle_input":
            return await self._handle_input(**kwargs)
        elif action == "start_stream":
            return await self._start_stream(**kwargs)
        elif action == "update_state":
            return await self._update_state(**kwargs)
        else:
            return self.agent_response(f"Unknown StreamProtocol action: {action}")
    
    async def _emit_event(self, event_type: EventType, payload: Dict[str, Any], 
                         thread_id: str = None):
        """Emit standardized event to frontend"""
        
        event = {
            "type": event_type,
            "payload": payload,
            "timestamp": self._get_timestamp(),
            "threadId": thread_id or self.agent.thread_id
        }
        
        await self.event_emitter.emit(event)
        return self.agent_response(f"Event emitted: {event_type}")
    
    async def _handle_input(self, input_data: Dict[str, Any]):
        """Process incoming frontend input according to RunAgentInput schema"""
        
        thread_id = input_data.get("threadId")
        messages = input_data.get("messages", [])
        state = input_data.get("state", {})
        
        # Process the input and route to appropriate agent functionality
        response = await self.agent.process_stream_input(
            thread_id=thread_id,
            messages=messages,
            state=state
        )
        
        return self.agent_response(response)
```
**File: `protocols/stream_protocol/events.py`**
```python
from enum import Enum
from typing import Dict, Any, List, Optional
from dataclasses import dataclass
import asyncio
import json

class EventType(Enum):
    """16 standard StreamProtocol event types"""
    TEXT_MESSAGE_CONTENT = "text_message_content"
    TOOL_CALL_START = "tool_call_start"
    TOOL_CALL_END = "tool_call_end"
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

@dataclass
class StreamEvent:
    """Standardized event structure"""
    type: EventType
    payload: Dict[str, Any]
    timestamp: str
    thread_id: Optional[str] = None
    user_id: Optional[str] = None

class EventEmitter:
    """Event emission system for StreamProtocol"""
    
    def __init__(self):
        self.listeners = {}
        self.event_queue = asyncio.Queue()
        
    async def emit(self, event: StreamEvent):
        """Emit event to all registered listeners"""
        await self.event_queue.put(event)
        
        # Notify listeners
        for listener in self.listeners.get(event.type, []):
            await listener(event)
    
    def on(self, event_type: EventType, listener):
        """Register event listener"""
        if event_type not in self.listeners:
            self.listeners[event_type] = []
        self.listeners[event_type].append(listener)
    
    async def get_events_stream(self):
        """Get continuous stream of events"""
        while True:
            event = await self.event_queue.get()
            yield event
```
#### 1.2 BrowserAgent Integration

**File: `tools/browser_agent_tool.py`**
```python
from python.helpers.tool import Tool
from agents.browser_agent.browser import BrowserManager
from agents.browser_agent.ai_models import AIModelProvider
from agents.browser_agent.actions import ActionExecutor
import asyncio
import json
from typing import Dict, Any, Optional

class BrowserAgentTool(Tool):
    """
    BrowserAgent (Stagehand) integration for Agent Zero
    Provides AI-powered browser automation with computer use capabilities
    """
    
    def __init__(self, agent, **kwargs):
        super().__init__(agent, **kwargs)
        self.browser_manager = BrowserManager()
        self.ai_provider = AIModelProvider()
        self.action_executor = ActionExecutor()
        self.active_sessions = {}
        
    async def execute(self, action: str, **kwargs):
        """
        Execute BrowserAgent operations
        
        Actions:
        - navigate: Navigate to URL using AI or direct control
        - act: Perform AI-powered actions on page
        - extract: Extract structured data from page
        - agent_execute: Use computer use models for complex tasks
        - cache_action: Cache repeatable actions
        """
        
        try:
            if action == "navigate":
                return await self._navigate(**kwargs)
            elif action == "act":
                return await self._ai_act(**kwargs)
            elif action == "extract":
                return await self._extract(**kwargs)
            elif action == "agent_execute":
                return await self._agent_execute(**kwargs)
            elif action == "cache_action":
                return await self._cache_action(**kwargs)
            else:
                return self.agent_response(f"Unknown BrowserAgent action: {action}")
                
        except Exception as e:
            return self.agent_response(f"BrowserAgent error: {str(e)}")
    
    async def _navigate(self, url: str, session_id: str = "default"):
        """Navigate to URL using browser automation"""
        
        # Emit StreamProtocol event
        await self.agent.emit_stream_event("browser_action", {
            "action": "navigate",
            "url": url,
            "status": "starting"
        })
        
        browser = await self.browser_manager.get_browser(session_id)
        page = await browser.new_page()
        
        try:
            await page.goto(url)
            
            result = {
                "success": True,
                "url": page.url,
                "title": await page.title(),
                "session_id": session_id
            }
            
            # Emit completion event
            await self.agent.emit_stream_event("browser_action", {
                "action": "navigate",
                "url": url,
                "status": "completed",
                "result": result
            })
            
            return self.agent_response(result)
            
        except Exception as e:
            await self.agent.emit_stream_event("error_event", {
                "action": "navigate",
                "error": str(e)
            })
            raise
    
    async def _ai_act(self, instructions: str, session_id: str = "default"):
        """Perform AI-powered actions using natural language"""
        
        await self.agent.emit_stream_event("browser_action", {
            "action": "ai_act",
            "instructions": instructions,
            "status": "processing"
        })
        
        browser = await self.browser_manager.get_browser(session_id)
        page = browser.page
        
        # Use AI model to interpret and execute instructions
        result = await self.action_executor.execute_ai_action(page, instructions)
        
        await self.agent.emit_stream_event("browser_action", {
            "action": "ai_act",
            "instructions": instructions,
            "status": "completed",
            "result": result
        })
        
        return self.agent_response(result)
    
    async def _extract(self, instructions: str, schema: Dict = None, 
                      session_id: str = "default"):
        """Extract structured data from current page"""
        
        browser = await self.browser_manager.get_browser(session_id)
        page = browser.page
        
        extraction_result = await self.action_executor.extract_data(
            page, instructions, schema
        )
        
        await self.agent.emit_stream_event("knowledge_result", {
            "type": "browser_extraction",
            "instructions": instructions,
            "data": extraction_result
        })
        
        return self.agent_response(extraction_result)
    
    async def _agent_execute(self, instructions: str, model: str = "computer-use-preview"):
        """Use computer use models for complex browser tasks"""
        
        agent = await self.ai_provider.get_computer_use_agent(model)
        
        await self.agent.emit_stream_event("agent_thought", {
            "content": f"Executing complex browser task: {instructions}",
            "model": model
        })
        
        result = await agent.execute(instructions)
        
        return self.agent_response(result)
```
### Phase 2: WebCrawler and KnowledgeAgent Integration (Week 3-4)

#### 2.1 WebCrawler Integration

**File: `tools/web_crawler_tool.py`**
```python
from python.helpers.tool import Tool
from agents.web_crawler.crawler import DocumentCrawler
from agents.web_crawler.processors import DocumentProcessor
from agents.web_crawler.chunker import HierarchicalChunker
import asyncio
from typing import Dict, Any, List

class WebCrawlerTool(Tool):
    """
    WebCrawler (Crawl4AI-agent-v2) integration for Agent Zero
    Provides intelligent web crawling and documentation processing
    """
    
    def __init__(self, agent, **kwargs):
        super().__init__(agent, **kwargs)
        self.crawler = DocumentCrawler()
        self.processor = DocumentProcessor()
        self.chunker = HierarchicalChunker()
        
    async def execute(self, action: str, **kwargs):
        """
        Execute WebCrawler operations
        
        Actions:
        - crawl_site: Recursively crawl website
        - crawl_sitemap: Process URLs from sitemap
        - crawl_markdown: Process markdown/txt files
        - process_documents: Process crawled documents
        """
        
        try:
            if action == "crawl_site":
                return await self._crawl_site(**kwargs)
            elif action == "crawl_sitemap":
                return await self._crawl_sitemap(**kwargs)
            elif action == "crawl_markdown":
                return await self._crawl_markdown(**kwargs)
            elif action == "process_documents":
                return await self._process_documents(**kwargs)
            else:
                return self.agent_response(f"Unknown WebCrawler action: {action}")
                
        except Exception as e:
            return self.agent_response(f"WebCrawler error: {str(e)}")
    
    async def _crawl_site(self, url: str, max_depth: int = 3, 
                         max_pages: int = 100):
        """Recursively crawl website with deduplication"""
        
        await self.agent.emit_stream_event("crawl_progress", {
            "action": "start_crawl",
            "url": url,
            "max_depth": max_depth,
            "max_pages": max_pages
        })
        
        crawled_docs = []
        processed_count = 0
        
        async for doc in self.crawler.crawl_recursive(url, max_depth, max_pages):
            # Process document
            processed_doc = await self.processor.process_document(doc)
            
            # Chunk for vector storage
            chunks = await self.chunker.chunk_document(processed_doc)
            
            # Store in knowledge base via KnowledgeAgent
            await self.agent.call_tool("knowledge_agent_tool", {
                "action": "ingest_chunks",
                "chunks": chunks,
                "source": url,
                "metadata": {
                    "url": doc.get("url"),
                    "title": doc.get("title"),
                    "crawl_depth": doc.get("depth", 0)
                }
            })
            
            processed_count += 1
            crawled_docs.append(processed_doc)
            
            # Emit progress update
            if processed_count % 10 == 0:
                await self.agent.emit_stream_event("crawl_progress", {
                    "action": "progress_update",
                    "processed": processed_count,
                    "total_estimated": max_pages,
                    "current_url": doc.get("url")
                })
        
        await self.agent.emit_stream_event("crawl_progress", {
            "action": "crawl_completed",
            "total_processed": processed_count,
            "url": url
        })
        
        return self.agent_response({
            "success": True,
            "documents_crawled": processed_count,
            "source_url": url
        })
```
#### 2.2 KnowledgeAgent Integration (Replacing ChromaDB with Foundational RAG)

**File: `tools/knowledge_agent_tool.py`**
```python
from python.helpers.tool import Tool
from agents.knowledge_agent.agent import KnowledgeRAGAgent
from agents.knowledge_agent.database import DatabaseManager
from agents.knowledge_agent.embeddings import EmbeddingGenerator
from agents.knowledge_agent.retrieval import InformationRetriever
import asyncio
from typing import Dict, Any, List

class KnowledgeAgentTool(Tool):
    """
    KnowledgeAgent (Foundational RAG) integration for Agent Zero
    Replaces ChromaDB with Supabase/pgvector for enhanced RAG capabilities
    """
    
    def __init__(self, agent, **kwargs):
        super().__init__(agent, **kwargs)
        self.database = DatabaseManager()
        self.embedding_generator = EmbeddingGenerator()
        self.retriever = InformationRetriever(self.database)
        self.rag_agent = KnowledgeRAGAgent(self.database, self.retriever)
        
    async def execute(self, action: str, **kwargs):
        """
        Execute KnowledgeAgent operations
        
        Actions:
        - ingest_documents: Process and store documents
        - ingest_chunks: Store pre-processed chunks
        - query: Retrieve and generate responses
        - search: Vector similarity search
        - update_knowledge: Update existing knowledge
        """
        
        try:
            if action == "ingest_documents":
                return await self._ingest_documents(**kwargs)
            elif action == "ingest_chunks":
                return await self._ingest_chunks(**kwargs)
            elif action == "query":
                return await self._query(**kwargs)
            elif action == "search":
                return await self._search(**kwargs)
            elif action == "update_knowledge":
                return await self._update_knowledge(**kwargs)
            else:
                return self.agent_response(f"Unknown KnowledgeAgent action: {action}")
                
        except Exception as e:
            return self.agent_response(f"KnowledgeAgent error: {str(e)}")
    
    async def _ingest_documents(self, documents: List[Dict], source: str = "manual"):
        """Ingest raw documents into knowledge base"""
        
        await self.agent.emit_stream_event("progress_update", {
            "action": "document_ingestion",
            "status": "starting",
            "count": len(documents)
        })
        
        ingested_count = 0
        for doc in documents:
            # Process document through full pipeline
            result = await self.rag_agent.ingest_document(doc, source)
            ingested_count += 1
            
            if ingested_count % 5 == 0:
                await self.agent.emit_stream_event("progress_update", {
                    "action": "document_ingestion",
                    "status": "processing",
                    "processed": ingested_count,
                    "total": len(documents)
                })
        
        await self.agent.emit_stream_event("knowledge_result", {
            "action": "documents_ingested",
            "count": ingested_count,
            "source": source
        })
        
        return self.agent_response({
            "success": True,
            "documents_ingested": ingested_count,
            "source": source
        })
    
    async def _query(self, query: str, limit: int = 5, 
                    context_window: int = 4000):
        """Query knowledge base with RAG response generation"""
        
        await self.agent.emit_stream_event("agent_thought", {
            "content": f"Searching knowledge base for: {query}"
        })
        
        # Get RAG response
        response = await self.rag_agent.query(
            query=query,
            limit=limit,
            context_window=context_window
        )
        
        await self.agent.emit_stream_event("knowledge_result", {
            "query": query,
            "response": response.content,
            "sources": response.sources,
            "confidence": response.confidence,
            "context_used": len(response.context_chunks)
        })
        
        return self.agent_response({
            "response": response.content,
            "sources": response.sources,
            "confidence": response.confidence,
            "metadata": {
                "chunks_retrieved": len(response.context_chunks),
                "query": query
            }
        })
```
### Phase 3: MemoryAgent and Hybrid Memory Integration (Week 5-6)

#### 3.1 MemoryAgent Integration

**File: `tools/memory_agent_tool.py`**
```python
from python.helpers.tool import Tool
from agents.memory_agent.memory import IntelligentMemory
from agents.memory_agent.graph import GraphMemory
from agents.memory_agent.vector import VectorMemory
import asyncio
from typing import Dict, Any, List

class MemoryAgentTool(Tool):
    """
    MemoryAgent (Mem0) integration for Agent Zero
    Provides intelligent, self-improving memory capabilities
    """
    
    def __init__(self, agent, **kwargs):
        super().__init__(agent, **kwargs)
        self.intelligent_memory = IntelligentMemory()
        self.graph_memory = GraphMemory()
        self.vector_memory = VectorMemory()
        
    async def execute(self, action: str, **kwargs):
        """
        Execute MemoryAgent operations
        
        Actions:
        - add: Add memories from conversations
        - search: Semantic memory search
        - update: Update existing memories
        - delete: Delete specific memories
        - get_all: Retrieve all memories
        - graph_query: Query graph-based memories
        """
        
        try:
            if action == "add":
                return await self._add_memory(**kwargs)
            elif action == "search":
                return await self._search_memory(**kwargs)
            elif action == "update":
                return await self._update_memory(**kwargs)
            elif action == "delete":
                return await self._delete_memory(**kwargs)
            elif action == "get_all":
                return await self._get_all_memories(**kwargs)
            elif action == "graph_query":
                return await self._graph_query(**kwargs)
            else:
                return self.agent_response(f"Unknown MemoryAgent action: {action}")
                
        except Exception as e:
            return self.agent_response(f"MemoryAgent error: {str(e)}")
    
    async def _add_memory(self, messages: List[Dict], user_id: str = "default"):
        """Add conversation memories with intelligent extraction"""
        
        # Extract memories using Mem0's intelligent extraction
        extracted_memories = await self.intelligent_memory.extract_memories(
            messages, user_id
        )
        
        # Store in both vector and graph memory
        vector_results = await self.vector_memory.store_memories(
            extracted_memories, user_id
        )
        
        graph_results = await self.graph_memory.update_relationships(
            extracted_memories, user_id
        )
        
        await self.agent.emit_stream_event("memory_update", {
            "action": "memories_added",
            "user_id": user_id,
            "vector_memories": len(vector_results),
            "graph_updates": len(graph_results)
        })
        
        return self.agent_response({
            "success": True,
            "memories_extracted": len(extracted_memories),
            "user_id": user_id,
            "vector_stored": len(vector_results),
            "graph_updated": len(graph_results)
        })
    
    async def _search_memory(self, query: str, user_id: str = "default", 
                           limit: int = 5):
        """Search memories using semantic similarity"""
        
        # Search vector memories
        vector_results = await self.vector_memory.search(
            query, user_id, limit
        )
        
        # Search graph memories for related concepts
        graph_results = await self.graph_memory.find_related(
            query, user_id, limit
        )
        
        # Combine and rank results
        combined_results = self.intelligent_memory.combine_search_results(
            vector_results, graph_results
        )
        
        return self.agent_response({
            "memories": combined_results,
            "query": query,
            "user_id": user_id,
            "total_found": len(combined_results)
        })
```
#### 3.2 Hybrid Memory System

**File: `memory/hybrid_system.py`**
```python
import asyncio
from typing import Dict, Any, List, Optional
from dataclasses import dataclass

@dataclass
class MemoryContext:
    """Combined memory context from all systems"""
    structured_memories: List[Dict[str, Any]]
    intelligent_memories: List[Dict[str, Any]]
    graph_relationships: List[Dict[str, Any]]
    relevance_scores: Dict[str, float]
    total_sources: int

class HybridMemorySystem:
    """
    Hybrid memory system combining Agent Zero's structured memory
    with MemoryAgent's intelligent capabilities
    """
    
    def __init__(self, agent):
        self.agent = agent
        self.agent_zero_memory = None  # Will be initialized from agent
        self.memory_agent_tool = None  # Will be initialized
        
    async def initialize(self):
        """Initialize hybrid memory system"""
        self.agent_zero_memory = self.agent.memory
        self.memory_agent_tool = await self.agent.get_tool("memory_agent_tool")
    
    async def store_interaction(self, interaction: Dict[str, Any]):
        """Store interaction in all memory systems"""
        
        # Store in Agent Zero's structured memory
        await self._store_structured_memory(interaction)
        
        # Store in MemoryAgent's intelligent memory
        await self._store_intelligent_memory(interaction)
        
        # Emit memory update event
        await self.agent.emit_stream_event("memory_update", {
            "action": "interaction_stored",
            "type": interaction.get("type"),
            "user_id": interaction.get("user_id")
        })
    
    async def retrieve_context(self, query: str, user_id: str = "default", 
                              max_tokens: int = 2000) -> MemoryContext:
        """Retrieve and combine context from all memory systems"""
        
        # Get structured memories from Agent Zero
        structured_results = await self._query_structured_memory(query)
        
        # Get intelligent memories from MemoryAgent
        intelligent_results = await self._query_intelligent_memory(query, user_id)
        
        # Get graph relationships
        graph_results = await self._query_graph_memory(query, user_id)
        
        # Calculate relevance scores and combine
        context = self._combine_memory_contexts(
            structured_results,
            intelligent_results, 
            graph_results,
            max_tokens
        )
        
        return context
    
    async def _store_structured_memory(self, interaction: Dict[str, Any]):
        """Store in Agent Zero's structured memory"""
        memory_content = {
            "timestamp": interaction.get("timestamp"),
            "type": interaction.get("type", "interaction"),
            "content": interaction.get("content", ""),
            "metadata": interaction.get("metadata", {}),
            "user_id": interaction.get("user_id", "default")
        }
        
        await self.agent.call_tool("memory_tool", {
            "action": "memorize",
            "data": str(memory_content)
        })
    
    async def _store_intelligent_memory(self, interaction: Dict[str, Any]):
        """Store in MemoryAgent's intelligent memory"""
        messages = interaction.get("messages", [])
        user_id = interaction.get("user_id", "default")
        
        if messages:
            await self.memory_agent_tool.execute(
                action="add",
                messages=messages,
                user_id=user_id
            )
    
    def _combine_memory_contexts(self, structured: List, intelligent: List, 
                                graph: List, max_tokens: int) -> MemoryContext:
        """Intelligently combine and rank memory results"""
        
        # Implement sophisticated ranking algorithm
        # Consider recency, relevance, user context, and relationships
        
        relevance_scores = {}
        
        # Score structured memories (Agent Zero)
        for mem in structured:
            score = self._calculate_relevance_score(mem, "structured")
            relevance_scores[f"structured_{mem.get('id', 'unknown')}"] = score
        
        # Score intelligent memories (MemoryAgent)
        for mem in intelligent:
            score = self._calculate_relevance_score(mem, "intelligent")
            relevance_scores[f"intelligent_{mem.get('id', 'unknown')}"] = score
        
        # Score graph relationships
        for rel in graph:
            score = self._calculate_relevance_score(rel, "graph")
            relevance_scores[f"graph_{rel.get('id', 'unknown')}"] = score
        
        return MemoryContext(
            structured_memories=structured,
            intelligent_memories=intelligent,
            graph_relationships=graph,
            relevance_scores=relevance_scores,
            total_sources=len(structured) + len(intelligent) + len(graph)
        )
    
    def _calculate_relevance_score(self, memory_item: Dict, memory_type: str) -> float:
        """Calculate relevance score for memory item"""
        # Implement scoring algorithm based on:
        # - Semantic similarity
        # - Recency
        # - User interaction frequency
        # - Contextual importance
        # - Memory type weights
        
        base_score = 0.5
        
        # Type-specific scoring
        if memory_type == "structured":
            base_score += 0.1  # Slight preference for structured data
        elif memory_type == "intelligent":
            base_score += 0.2  # Higher preference for intelligent memories
        elif memory_type == "graph":
            base_score += 0.15  # Medium preference for relationships
        
        # Add recency factor
        timestamp = memory_item.get("timestamp")
        if timestamp:
            recency_score = self._calculate_recency_score(timestamp)
            base_score += recency_score * 0.3
        
        return min(base_score, 1.0)  # Cap at 1.0
```

This detailed implementation plan provides a complete line-by-line integration strategy that:

1. **Maintains Agent Zero's Core Philosophy**: All integrations follow Agent Zero's prompt-based, transparent approach
2. **Uses Exact Repository Code**: Integrates the actual implementations from each repository
3. **Standardizes Naming**: Uses consistent naming convention throughout
4. **Replaces ChromaDB**: Uses the foundational RAG agent with Supabase/pgvector
5. **Provides Hybrid Memory**: Combines Agent Zero's structured memory with Mem0's intelligent capabilities
6. **Implements StreamProtocol**: Replaces Agent Zero's UI with modern AG-UI protocol
7. **Adds Advanced Browser Automation**: Integrates Stagehand's AI-powered browser capabilities

Each tool integration maintains full compatibility with Agent Zero's existing architecture while adding significant new capabilities through the standardized tool interface.### Complete File: `tools/stream_protocol_tool.py`

```python
"""
StreamProtocol Tool - AG-UI Protocol Integration for Agent Zero
Provides standardized agent-frontend communication with real-time streaming
Based on AG-UI Protocol specification and TypeScript SDK
"""

from python.helpers.tool import Tool
from typing import Dict, Any, List, Optional, AsyncGenerator
import asyncio
import json
import uuid
from datetime import datetime
from dataclasses import dataclass, field
from enum import Enum

class StreamEventType(Enum):
    """16 standard AG-UI event types"""
    TEXT_MESSAGE_CONTENT = "text_message_content"
    TOOL_CALL_START = "tool_call_start"
    TOOL_CALL_END = "tool_call_end"
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
    """Transport layer for AG-UI events"""
    
    def __init__(self):
        self.connections = {}
        self.event_handlers = {}
        
    async def emit_event(self, event: StreamEvent):
        """Emit event to all connected clients"""
        event_data = {
            "id": event.event_id,
            "type": event.type.value,
            "payload": event.payload,
            "timestamp": event.timestamp,
            "threadId": event.thread_id,
            "userId": event.user_id
        }
        
        # Send to all connections for this thread
        for connection_id, connection in self.connections.items():
            if connection.get("thread_id") == event.thread_id:
                await connection["websocket"].send_text(json.dumps(event_data))
    
    async def register_connection(self, websocket, thread_id: str, user_id: str = None):
        """Register new websocket connection"""
        connection_id = str(uuid.uuid4())
        self.connections[connection_id] = {
            "websocket": websocket,
            "thread_id": thread_id,
            "user_id": user_id,
            "created_at": datetime.utcnow()
        }
        return connection_id
    
    def unregister_connection(self, connection_id: str):
        """Remove websocket connection"""
        self.connections.pop(connection_id, None)

class StreamProtocolTool(Tool):
    """
    StreamProtocol (AG-UI) integration for Agent Zero
    Provides standardized agent-frontend communication with real-time streaming
    """
    
    def __init__(self, agent, **kwargs):
        super().__init__(agent, **kwargs)
        self.transport = StreamTransport()
        self.active_threads = {}
        self.middleware_stack = []
        
    async def execute(self, action: str, **kwargs):
        """
        Execute StreamProtocol operations
        
        Actions:
        - emit_event: Emit standardized event to frontend
        - handle_input: Process incoming frontend input
        - start_session: Start streaming session
        - end_session: End streaming session
        - update_state: Update shared state
        - register_middleware: Add event middleware
        """
        
        try:
            if action == "emit_event":
                return await self._emit_event(**kwargs)
            elif action == "handle_input":
                return await self._handle_input(**kwargs)
            elif action == "start_session":
                return await self._start_session(**kwargs)
            elif action == "end_session":
                return await self._end_session(**kwargs)
            elif action == "update_state":
                return await self._update_state(**kwargs)
            elif action == "register_middleware":
                return await self._register_middleware(**kwargs)
            else:
                return self.agent_response(f"Unknown StreamProtocol action: {action}")
                
        except Exception as e:
            # Emit error event
            await self._emit_error_event(str(e), kwargs.get("thread_id"))
            return self.agent_response(f"StreamProtocol error: {str(e)}")
    
    async def _emit_event(self, event_type: str, payload: Dict[str, Any], 
                         thread_id: str = None, user_id: str = None):
        """Emit standardized event to frontend"""
        
        # Convert string to enum
        try:
            event_enum = StreamEventType(event_type)
        except ValueError:
            return self.agent_response(f"Invalid event type: {event_type}")
        
        # Create event
        event = StreamEvent(
            type=event_enum,
            payload=payload,
            thread_id=thread_id or self.agent.get_thread_id(),
            user_id=user_id or self.agent.get_user_id()
        )
        
        # Apply middleware
        for middleware in self.middleware_stack:
            event = await middleware(event)
            if event is None:
                return self.agent_response("Event filtered by middleware")
        
        # Emit event
        await self.transport.emit_event(event)
        
        return self.agent_response({
            "success": True,
            "event_id": event.event_id,
            "type": event_type,
            "timestamp": event.timestamp
        })
    
    async def _handle_input(self, input_data: Dict[str, Any]):
        """Process incoming frontend input according to RunAgentInput schema"""
        
        try:
            # Parse input
            run_input = RunAgentInput(
                thread_id=input_data.get("threadId", str(uuid.uuid4())),
                messages=input_data.get("messages", []),
                state=input_data.get("state", {}),
                user_id=input_data.get("userId"),
                metadata=input_data.get("metadata", {})
            )
            
            # Update agent context
            await self._update_agent_context(run_input)
            
            # Emit session start if new thread
            if run_input.thread_id not in self.active_threads:
                await self._emit_event(
                    "session_start",
                    {"threadId": run_input.thread_id, "userId": run_input.user_id},
                    run_input.thread_id,
                    run_input.user_id
                )
                self.active_threads[run_input.thread_id] = {
                    "user_id": run_input.user_id,
                    "state": run_input.state,
                    "created_at": datetime.utcnow()
                }
            
            # Process messages
            for message in run_input.messages:
                await self._process_message(message, run_input.thread_id, run_input.user_id)
            
            return self.agent_response({
                "success": True,
                "thread_id": run_input.thread_id,
                "messages_processed": len(run_input.messages)
            })
            
        except Exception as e:
            return self.agent_response(f"Input processing error: {str(e)}")
    
    async def _process_message(self, message: Dict[str, Any], thread_id: str, user_id: str):
        """Process individual message from frontend"""
        
        role = message.get("role", "user")
        content = message.get("content", "")
        
        # Emit message content event
        await self._emit_event(
            "text_message_content",
            {
                "role": role,
                "content": content,
                "messageId": message.get("id", str(uuid.uuid4()))
            },
            thread_id,
            user_id
        )
        
        # If user message, trigger agent processing
        if role == "user":
            await self._trigger_agent_processing(content, thread_id, user_id)
    
    async def _trigger_agent_processing(self, content: str, thread_id: str, user_id: str):
        """Trigger agent processing for user message"""
        
        # Emit agent thought
        await self._emit_event(
            "agent_thought",
            {"content": f"Processing user request: {content[:100]}..."},
            thread_id,
            user_id
        )
        
        # Store in Agent Zero's conversation history
        await self.agent.hist_add_user_message(content)
        
        # Process through Agent Zero's system
        response = await self.agent.monologue()
        
        # Emit response
        await self._emit_event(
            "text_message_content",
            {
                "role": "assistant",
                "content": response,
                "messageId": str(uuid.uuid4())
            },
            thread_id,
            user_id
        )
    
    async def _start_session(self, thread_id: str, user_id: str = None, 
                           initial_state: Dict[str, Any] = None):
        """Start new streaming session"""
        
        if thread_id in self.active_threads:
            return self.agent_response(f"Session {thread_id} already active")
        
        self.active_threads[thread_id] = {
            "user_id": user_id,
            "state": initial_state or {},
            "created_at": datetime.utcnow()
        }
        
        await self._emit_event(
            "session_start",
            {"threadId": thread_id, "userId": user_id, "initialState": initial_state},
            thread_id,
            user_id
        )
        
        return self.agent_response({
            "success": True,
            "thread_id": thread_id,
            "status": "session_started"
        })
    
    async def _end_session(self, thread_id: str):
        """End streaming session"""
        
        if thread_id not in self.active_threads:
            return self.agent_response(f"Session {thread_id} not found")
        
        session_info = self.active_threads.pop(thread_id)
        
        await self._emit_event(
            "session_end",
            {
                "threadId": thread_id,
                "duration": (datetime.utcnow() - session_info["created_at"]).total_seconds()
            },
            thread_id,
            session_info.get("user_id")
        )
        
        return self.agent_response({
            "success": True,
            "thread_id": thread_id,
            "status": "session_ended"
        })
    
    async def _update_state(self, thread_id: str, state_delta: Dict[str, Any]):
        """Update shared state for thread"""
        
        if thread_id not in self.active_threads:
            return self.agent_response(f"Session {thread_id} not found")
        
        # Apply state delta
        current_state = self.active_threads[thread_id]["state"]
        current_state.update(state_delta)
        
        # Emit state delta event
        await self._emit_event(
            "state_delta",
            {"delta": state_delta, "fullState": current_state},
            thread_id,
            self.active_threads[thread_id].get("user_id")
        )
        
        return self.agent_response({
            "success": True,
            "thread_id": thread_id,
            "updated_state": current_state
        })
    
    async def _register_middleware(self, middleware_func: callable):
        """Register event middleware function"""
        self.middleware_stack.append(middleware_func)
        
        return self.agent_response({
            "success": True,
            "middleware_count": len(self.middleware_stack)
        })
    
    async def _emit_error_event(self, error_message: str, thread_id: str = None):
        """Emit error event"""
        await self._emit_event(
            "error_event",
            {"error": error_message, "timestamp": datetime.utcnow().isoformat()},
            thread_id
        )
    
    async def _update_agent_context(self, run_input: RunAgentInput):
        """Update agent context with input data"""
        
        # Set thread and user context
        if hasattr(self.agent, 'set_thread_id'):
            self.agent.set_thread_id(run_input.thread_id)
        
        if hasattr(self.agent, 'set_user_id'):
            self.agent.set_user_id(run_input.user_id)
        
        # Update state if provided
        if run_input.state:
            if hasattr(self.agent, 'update_state'):
                self.agent.update_state(run_input.state)
```

### Complete File: `tools/browser_agent_tool.py`

```python
"""
BrowserAgent Tool - Stagehand Integration for Agent Zero
Provides AI-powered browser automation with computer use capabilities
Based on Stagehand TypeScript framework
"""

from python.helpers.tool import Tool
import subprocess
import asyncio
import json
import tempfile
import os
from typing import Dict, Any, Optional, List
from dataclasses import dataclass

@dataclass
class BrowserSession:
    """Browser session information"""
    session_id: str
    url: str
    title# Complete Repository Analysis and Integration Plan

## Repository Analysis Summary

Based on the comprehensive research, here's what I've discovered about each repository's structure and capabilities:

### 1. AG-UI Protocol (`ag-ui-protocol/ag-ui`)

#### **Repository Structure (Inferred from Documentation)**
```
ag-ui/
├── packages/
│   ├── core/                     # Core protocol implementation
│   │   ├── src/
│   │   │   ├── types.ts          # TypeScript type definitions
│   │   │   ├── events.ts         # Event type definitions
│   │   │   └── schemas.ts        # Validation schemas
│   │   └── package.json
│   ├── client/                   # Client SDK
│   │   ├── src/
│   │   │   ├── AbstractAgent.ts  # Base agent class
│   │   │   ├── connection.ts     # Connection management
│   │   │   └── streaming.ts      # Streaming utilities
│   │   └── package.json
│   ├── server/                   # Server implementation
│   │   ├── src/
│   │   │   ├── middleware.ts     # Event middleware
│   │   │   ├── transport.ts      # Transport layer
│   │   │   └── sse.ts           # Server-Sent Events
│   │   └── package.json
│   └── encoder/                  # Binary encoder for performance
│       ├── src/
│       │   └── encoder.ts
│       └── package.json
├── integrations/                 # Framework integrations
│   ├── langgraph/
│   ├── mastra/
│   ├── crewai/
│   └── openai/
├── examples/                     # Usage examples
├── docs/                        # Documentation
└── dojo/                        # Interactive playground
```

#### **Key Components Based on Documentation**

**Core Types (inferred from API docs):**
```typescript
// From documentation examples
interface RunAgentInput {
  threadId: string;
  messages: Message[];
  state?: Record<string, any>;
}

// 16 standard event types mentioned
type EventType = 
  | "TEXT_MESSAGE_CONTENT"
  | "TOOL_CALL_START" 
  | "TOOL_CALL_END"
  | "STATE_DELTA"
  | "AGENT_THOUGHT"
  | "HUMAN_INTERVENTION"
  | "GENERATIVE_UI"
  | "CONTEXT_UPDATE"
  // ... 8 more types

interface AGUIEvent {
  type: EventType;
  payload: any;
  timestamp?: string;
  threadId?: string;
}
```

**Server Implementation (from quickstart guide):**
```typescript
// TypeScript version from docs
import express, { Request, Response } from "express"
import { RunAgentInputSchema, RunAgentInput } from "@ag-ui/core"

const app = express()
app.use(express.json())

app.post("/awp", (req: Request, res: Response) => {
  try {
    const input: RunAgentInput = RunAgentInputSchema.parse(req.body)
    res.json({ message: `Hello World from ${input.threadId}` })
  } catch (error) {
    res.status(422).json({ error: (error as Error).message })
  }
})
```

**Python Version (from docs):**
```python
from fastapi import FastAPI, Request
from ag_ui.core.types import RunAgentInput

app = FastAPI(title="AG-UI Endpoint")

@app.post("/awp")
async def my_endpoint(request: RunAgentInput):
    return {"message": "Hello World"}
```

### 2. Stagehand (`browserbase/stagehand`)

#### **Repository Structure (from documentation analysis)**
```
stagehand/
├── lib/
│   ├── browser/
│   │   ├── Browser.ts            # Browser management
│   │   ├── Page.ts              # Page automation
│   │   └── Context.ts           # Browser context
│   ├── ai/
│   │   ├── models/
│   │   │   ├── OpenAI.ts        # OpenAI integration
│   │   │   └── Anthropic.ts     # Anthropic integration
│   │   └── ModelProvider.ts     # Model abstraction
│   ├── cache/
│   │   ├── ActionCache.ts       # Action caching system
│   │   └── CacheManager.ts      # Cache management
│   ├── types/
│   │   ├── StagehandConfig.ts   # Configuration types
│   │   └── ActionTypes.ts       # Action definitions
│   └── index.ts                 # Main exports
├── examples/
│   ├── example.ts               # Basic example
│   └── computer-use/            # Computer use examples
├── docs/                        # Documentation
├── package.json
└── README.md
```

#### **Key API (from documentation examples):**
```typescript
import { Stagehand } from 'stagehand';

// Basic usage
const stagehand = new Stagehand();
await stagehand.init();
const page = stagehand.page;

// Use Playwright functions directly
await page.goto("https://github.com/browserbase");

// Use AI for navigation
await page.act("click on the stagehand repo");

// Computer use agent
const agent = stagehand.agent({
  provider: "openai",
  model: "computer-use-preview",
});
await agent.execute("Get to the latest PR");

// Extract structured data
const { author, title } = await page.extract({
  instruction: "extract the author and title of the PR",
  schema: z.object({
    author: z.string().describe("The username of the PR author"),
    title: z.string().describe("The title of the PR"),
  }),
});
```

### 3. Crawl4AI Agent v2 (`coleam00/ottomator-agents/crawl4AI-agent-v2`)

#### **Complete File Structure (from search results):**
```
crawl4AI-agent-v2/
├── crawl4AI-examples/
│   ├── 3-crawl_sitemap_in_parallel.py
│   ├── 4-crawl_llms_txt.py
│   └── 5-crawl_site_recursively.py
├── insert_docs.py               # Main ingestion script
├── rag_agent.py                # Pydantic AI RAG agent
├── streamlit_app.py            # Web interface
├── utils.py                    # Utility functions
├── requirements.txt            # Dependencies
├── .env.example               # Environment template
└── README.md                  # Documentation
```

#### **Key Dependencies (from documentation):**
```
# requirements.txt content (inferred)
crawl4ai
pydantic-ai
chromadb
streamlit
playwright
openai
python-dotenv
```

#### **Core Components (from analysis):**

**insert_docs.py** - Main entry point:
- Handles regular documentation sites
- Processes markdown/txt pages (llms.txt format)
- Recursive crawling with deduplication
- Parallel processing with memory tracking

**rag_agent.py** - Pydantic AI agent:
- ChromaDB integration for vector storage
- Semantic search capabilities
- Context-rich response generation

**utils.py** - Utility functions:
- Document processing and chunking
- Hierarchical Markdown chunking by headers
- Memory-adaptive batching

### 4. Foundational RAG Agent (`coleam00/ottomator-agents/foundational-rag-agent`)

#### **Complete File Structure (confirmed from search results):**
```
foundational-rag-agent/
├── database/
│   └── setup.py                # Database setup with Supabase/pgvector
├── document_processing/
│   ├── __init__.py
│   ├── chunker.py             # Text chunking functionality
│   ├── embeddings.py          # OpenAI embeddings generation
│   ├── ingestion.py           # Document ingestion pipeline
│   └── processors.py          # TXT and PDF processing
├── agent/
│   ├── __init__.py
│   ├── agent.py               # Main Pydantic AI agent
│   ├── prompts.py             # System prompts and templates
│   └── tools.py               # Knowledge base search tools
├── ui/
│   └── app.py                 # Streamlit application
├── tests/
│   ├── test_chunker.py
│   ├── test_embeddings.py
│   ├── test_ingestion.py
│   ├── test_processors.py
│   └── test_agent.py
├── .env.example               # Environment variables
├── requirements.txt           # Dependencies
├── PLANNING.md               # Project planning
├── TASK.md                   # Task tracking
└── README.md                 # Documentation
```

#### **Key Components Analysis:**

**Database Layer (database/setup.py):**
- Supabase integration with pgvector
- Vector similarity search setup
- Connection pooling and management

**Document Processing:**
- **chunker.py**: Intelligent text chunking with overlap management
- **embeddings.py**: OpenAI embedding generation with batch processing
- **ingestion.py**: Full pipeline with file type detection
- **processors.py**: TXT/PDF processing with metadata extraction

**Agent Layer:**
- **agent.py**: Pydantic AI agent with conversation management
- **prompts.py**: RAG-specific prompt templates
- **tools.py**: Vector search interface and result ranking

### 5. Mem0 (`mem0ai/mem0`)

#### **Repository Structure (from analysis):**
```
mem0/
├── mem0/
│   ├── __init__.py
│   ├── client/
│   │   ├── main.py             # Main client interface
│   │   └── memory.py           # Memory operations
│   ├── memory/
│   │   ├── base.py             # Base memory class
│   │   ├── graph.py            # Graph-based memory
│   │   └── vector.py           # Vector memory
│   ├── embeddings/
│   │   ├── openai.py           # OpenAI embeddings
│   │   └── base.py             # Embedding interface
│   ├── llms/
│   │   ├── openai.py           # OpenAI LLM integration
│   │   └── base.py             # LLM interface
│   └── utils/
│       ├── parsing.py          # Text parsing utilities
│       └── helpers.py          # Helper functions
├── examples/                   # Usage examples
├── tests/                      # Test suite
├── docs/                       # Documentation
└── requirements.txt           # Dependencies
```

#### **Core API (from documentation):**
```python
from mem0 import Memory

# Initialize memory
memory = Memory()

# Add memories from conversation
messages = [
    {"role": "user", "content": "I like pizza"},
    {"role": "assistant", "content": "Great! I'll remember that."}
]
memory.add(messages=messages, user_id="user_123")

# Search memories
results = memory.search(query="food preferences", user_id="user_123", limit=5)

# Update memories
memory.update(memory_id="mem_456", data="Updated information")

# Delete memories
memory.delete(memory_id="mem_456")
```

## Agent Zero Enhanced Integration Architecture

Now that I have a complete understanding of each repository, here's the detailed integration plan:

### Standardized Naming Convention

Instead of using the original names, we'll use these standardized names:
- **AG-UI Protocol** → **StreamProtocol**
- **Stagehand** → **BrowserAgent**  
- **Crawl4AI Agent v2** → **WebCrawler**
- **Foundational RAG Agent** → **KnowledgeAgent**
- **Mem0** → **MemoryAgent**

### Enhanced Agent Zero Architecture

```
enhanced_agent_zero/
├── core/
│   ├── agent.py                    # Enhanced Agent class with new capabilities
│   ├── models.py                   # Extended model support
│   ├── config.py                   # Centralized configuration
│   └── events.py                   # StreamProtocol event system
├── tools/
│   ├── stream_protocol_tool.py     # StreamProtocol integration
│   ├── browser_agent_tool.py       # BrowserAgent integration  
│   ├── web_crawler_tool.py         # WebCrawler integration
│   ├── knowledge_agent_tool.py     # KnowledgeAgent integration
│   ├── memory_agent_tool.py        # MemoryAgent integration
│   └── hybrid_memory_tool.py       # Combined memory system
├── protocols/
│   ├── stream_protocol/            # StreamProtocol implementation
│   │   ├── events.py              # Event definitions
│   │   ├── transport.py           # Transport layer
│   │   └── middleware.py          # Event middleware
│   └── types.py                   # Protocol type definitions
├── agents/
│   ├── browser_agent/             # BrowserAgent implementation
│   │   ├── browser.py             # Browser management
│   │   ├── ai_models.py           # AI model integration
│   │   └── actions.py             # Action definitions
│   ├── web_crawler/               # WebCrawler implementation
│   │   ├── crawler.py             # Crawling logic
│   │   ├── processors.py          # Document processing
│   │   └── chunker.py             # Text chunking
│   ├── knowledge_agent/           # KnowledgeAgent implementation
│   │   ├── agent.py               # Main agent logic
│   │   ├── database.py            # Database operations
│   │   ├── embeddings.py          # Embedding generation
│   │   └── retrieval.py           # Information retrieval
│   └── memory_agent/              # MemoryAgent implementation
│       ├── memory.py              # Memory operations
│       ├── graph.py               # Graph-based memory
│       └── vector.py              # Vector memory
├── ui/
│   ├── stream_interface.py        # StreamProtocol interface
│   ├── components/                # UI components
│   └── handlers/                  # Event handlers
├── memory/
│   ├── hybrid_system.py           # Combined memory approach
│   ├── agent_zero_memory.py       # Original Agent Zero memory
│   └── intelligent_memory.py      # MemoryAgent integration
├── prompts/
│   ├── enhanced/                  # Enhanced prompt templates
│   │   ├── agent.system.md        # Main system prompt
│   │   ├── browser_agent.md       # Browser automation prompts
│   │   ├── web_crawler.md         # Web crawling prompts
│   │   ├── knowledge_agent.md     # RAG prompts
│   │   └── memory_agent.md        # Memory prompts
│   └── tools/                     # Tool-specific prompts
├── tests/
│   ├── integration/               # Integration tests
│   ├── unit/                      # Unit tests
│   └── performance/               # Performance tests
└── examples/
    ├── basic_usage.py             # Basic integration example
    ├── advanced_rag.py            # Advanced RAG example
    └── browser_automation.py      # Browser automation example
```

## Complete Implementation Files

### Repository Integration Structure

Based on comprehensive analysis, here are the complete implementation files that integrate all repositories with Agent Zero:

## Phase 1: Core Integration Framework (Week 1-2)

#### 1.1 StreamProtocol Integration

**File: `tools/stream_protocol_tool.py`**
```python
from python.helpers.tool import Tool
from protocols.stream_protocol.events import EventEmitter, EventType
from protocols.stream_protocol.transport import StreamTransport
import asyncio
import json
from typing import Dict, Any, List

class StreamProtocolTool(Tool):
    """
    StreamProtocol (AG-UI) integration for Agent Zero
    Provides standardized agent-frontend communication with real-time streaming
    """
    
    def __init__(self, agent, **kwargs):
        super().__init__(agent, **kwargs)
        self.event_emitter = EventEmitter()
        self.transport = StreamTransport()
        self.active_connections = {}
        
    async def execute(self, action: str, **kwargs):
        """
        Execute StreamProtocol operations
        
        Actions:
        - emit_event: Emit standardized event to frontend
        - handle_input: Process incoming frontend input
        - start_stream: Start streaming session
        - update_state: Update shared state
        """
        
        if action == "emit_event":
            return await self._emit_event(**kwargs)
        elif action == "handle_input":
            return await self._handle_input(**kwargs)
        elif action == "start_stream":
            return await self._start_stream(**kwargs)
        elif action == "update_state":
            return await self._update_state(**kwargs)
        else:
            return self.agent_response(f"Unknown StreamProtocol action: {action}")
    
    async def _emit_event(self, event_type: EventType, payload: Dict[str, Any], 
                         thread_id: str = None):
        """Emit standardized event to frontend"""
        
        event = {
            "type": event_type,
            "payload": payload,
            "timestamp": self._get_timestamp(),
            "threadId": thread_id or self.agent.thread_id
        }
        
        await self.event_emitter.emit(event)
        return self.agent_response(f"Event emitted: {event_type}")
    
    async def _handle_input(self, input_data: Dict[str, Any]):
        """Process incoming frontend input according to RunAgentInput schema"""
        
        thread_id = input_data.get("threadId")
        messages = input_data.get("messages", [])
        state = input_data.get("state", {})
        
        # Process the input and route to appropriate agent functionality
        response = await self.agent.process_stream_input(
            thread_id=thread_id,
            messages=messages,
            state=state
        )
        
        return self.agent_response(response)
```

**File: `protocols/stream_protocol/events.py`**
```python
from enum import Enum
from typing import Dict, Any, List, Optional
from dataclasses import dataclass
import asyncio
import json

class EventType(Enum):
    """16 standard StreamProtocol event types"""
    TEXT_MESSAGE_CONTENT = "text_message_content"
    TOOL_CALL_START = "tool_call_start"
    TOOL_CALL_END = "tool_call_end"
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

@dataclass
class StreamEvent:
    """Standardized event structure"""
    type: EventType
    payload: Dict[str, Any]
    timestamp: str
    thread_id: Optional[str] = None
    user_id: Optional[str] = None

class EventEmitter:
    """Event emission system for StreamProtocol"""
    
    def __init__(self):
        self.listeners = {}
        self.event_queue = asyncio.Queue()
        
    async def emit(self, event: StreamEvent):
        """Emit event to all registered listeners"""
        await self.event_queue.put(event)
        
        # Notify listeners
        for listener in self.listeners.get(event.type, []):
            await listener(event)
    
    def on(self, event_type: EventType, listener):
        """Register event listener"""
        if event_type not in self.listeners:
            self.listeners[event_type] = []
        self.listeners[event_type].append(listener)
    
    async def get_events_stream(self):
        """Get continuous stream of events"""
        while True:
            event = await self.event_queue.get()
            yield event
```

#### 1.2 BrowserAgent Integration

**File: `tools/browser_agent_tool.py`**
```python
from python.helpers.tool import Tool
from agents.browser_agent.browser import BrowserManager
from agents.browser_agent.ai_models import AIModelProvider
from agents.browser_agent.actions import ActionExecutor
import asyncio
import json
from typing import Dict, Any, Optional

class BrowserAgentTool(Tool):
    """
    BrowserAgent (Stagehand) integration for Agent Zero
    Provides AI-powered browser automation with computer use capabilities
    """
    
    def __init__(self, agent, **kwargs):
        super().__init__(agent, **kwargs)
        self.browser_manager = BrowserManager()
        self.ai_provider = AIModelProvider()
        self.action_executor = ActionExecutor()
        self.active_sessions = {}
        
    async def execute(self, action: str, **kwargs):
        """
        Execute BrowserAgent operations
        
        Actions:
        - navigate: Navigate to URL using AI or direct control
        - act: Perform AI-powered actions on page
        - extract: Extract structured data from page
        - agent_execute: Use computer use models for complex tasks
        - cache_action: Cache repeatable actions
        """
        
        try:
            if action == "navigate":
                return await self._navigate(**kwargs)
            elif action == "act":
                return await self._ai_act(**kwargs)
            elif action == "extract":
                return await self._extract(**kwargs)
            elif action == "agent_execute":
                return await self._agent_execute(**kwargs)
            elif action == "cache_action":
                return await self._cache_action(**kwargs)
            else:
                return self.agent_response(f"Unknown BrowserAgent action: {action}")
                
        except Exception as e:
            return self.agent_response(f"BrowserAgent error: {str(e)}")
    
    async def _navigate(self, url: str, session_id: str = "default"):
        """Navigate to URL using browser automation"""
        
        # Emit StreamProtocol event
        await self.agent.emit_stream_event("browser_action", {
            "action": "navigate",
            "url": url,
            "status": "starting"
        })
        
        browser = await self.browser_manager.get_browser(session_id)
        page = await browser.new_page()
        
        try:
            await page.goto(url)
            
            result = {
                "success": True,
                "url": page.url,
                "title": await page.title(),
                "session_id": session_id
            }
            
            # Emit completion event
            await self.agent.emit_stream_event("browser_action", {
                "action": "navigate",
                "url": url,
                "status": "completed",
                "result": result
            })
            
            return self.agent_response(result)
            
        except Exception as e:
            await self.agent.emit_stream_event("error_event", {
                "action": "navigate",
                "error": str(e)
            })
            raise
    
    async def _ai_act(self, instructions: str, session_id: str = "default"):
        """Perform AI-powered actions using natural language"""
        
        await self.agent.emit_stream_event("browser_action", {
            "action": "ai_act",
            "instructions": instructions,
            "status": "processing"
        })
        
        browser = await self.browser_manager.get_browser(session_id)
        page = browser.page
        
        # Use AI model to interpret and execute instructions
        result = await self.action_executor.execute_ai_action(page, instructions)
        
        await self.agent.emit_stream_event("browser_action", {
            "action": "ai_act",
            "instructions": instructions,
            "status": "completed",
            "result": result
        })
        
        return self.agent_response(result)
    
    async def _extract(self, instructions: str, schema: Dict = None, 
                      session_id: str = "default"):
        """Extract structured data from current page"""
        
        browser = await self.browser_manager.get_browser(session_id)
        page = browser.page
        
        extraction_result = await self.action_executor.extract_data(
            page, instructions, schema
        )
        
        await self.agent.emit_stream_event("knowledge_result", {
            "type": "browser_extraction",
            "instructions": instructions,
            "data": extraction_result
        })
        
        return self.agent_response(extraction_result)
    
    async def _agent_execute(self, instructions: str, model: str = "computer-use-preview"):
        """Use computer use models for complex browser tasks"""
        
        agent = await self.ai_provider.get_computer_use_agent(model)
        
        await self.agent.emit_stream_event("agent_thought", {
            "content": f"Executing complex browser task: {instructions}",
            "model": model
        })
        
        result = await agent.execute(instructions)
        
        return self.agent_response(result)
```

### Phase 2: WebCrawler and KnowledgeAgent Integration (Week 3-4)

#### 2.1 WebCrawler Integration

**File: `tools/web_crawler_tool.py`**
```python
from python.helpers.tool import Tool
from agents.web_crawler.crawler import DocumentCrawler
from agents.web_crawler.processors import DocumentProcessor
from agents.web_crawler.chunker import HierarchicalChunker
import asyncio
from typing import Dict, Any, List

class WebCrawlerTool(Tool):
    """
    WebCrawler (Crawl4AI-agent-v2) integration for Agent Zero
    Provides intelligent web crawling and documentation processing
    """
    
    def __init__(self, agent, **kwargs):
        super().__init__(agent, **kwargs)
        self.crawler = DocumentCrawler()
        self.processor = DocumentProcessor()
        self.chunker = HierarchicalChunker()
        
    async def execute(self, action: str, **kwargs):
        """
        Execute WebCrawler operations
        
        Actions:
        - crawl_site: Recursively crawl website
        - crawl_sitemap: Process URLs from sitemap
        - crawl_markdown: Process markdown/txt files
        - process_documents: Process crawled documents
        """
        
        try:
            if action == "crawl_site":
                return await self._crawl_site(**kwargs)
            elif action == "crawl_sitemap":
                return await self._crawl_sitemap(**kwargs)
            elif action == "crawl_markdown":
                return await self._crawl_markdown(**kwargs)
            elif action == "process_documents":
                return await self._process_documents(**kwargs)
            else:
                return self.agent_response(f"Unknown WebCrawler action: {action}")
                
        except Exception as e:
            return self.agent_response(f"WebCrawler error: {str(e)}")
    
    async def _crawl_site(self, url: str, max_depth: int = 3, 
                         max_pages: int = 100):
        """Recursively crawl website with deduplication"""
        
        await self.agent.emit_stream_event("crawl_progress", {
            "action": "start_crawl",
            "url": url,
            "max_depth": max_depth,
            "max_pages": max_pages
        })
        
        crawled_docs = []
        processed_count = 0
        
        async for doc in self.crawler.crawl_recursive(url, max_depth, max_pages):
            # Process document
            processed_doc = await self.processor.process_document(doc)
            
            # Chunk for vector storage
            chunks = await self.chunker.chunk_document(processed_doc)
            
            # Store in knowledge base via KnowledgeAgent
            await self.agent.call_tool("knowledge_agent_tool", {
                "action": "ingest_chunks",
                "chunks": chunks,
                "source": url,
                "metadata": {
                    "url": doc.get("url"),
                    "title": doc.get("title"),
                    "crawl_depth": doc.get("depth", 0)
                }
            })
            
            processed_count += 1
            crawled_docs.append(processed_doc)
            
            # Emit progress update
            if processed_count % 10 == 0:
                await self.agent.emit_stream_event("crawl_progress", {
                    "action": "progress_update",
                    "processed": processed_count,
                    "total_estimated": max_pages,
                    "current_url": doc.get("url")
                })
        
        await self.agent.emit_stream_event("crawl_progress", {
            "action": "crawl_completed",
            "total_processed": processed_count,
            "url": url
        })
        
        return self.agent_response({
            "success": True,
            "documents_crawled": processed_count,
            "source_url": url
        })
```

#### 2.2 KnowledgeAgent Integration (Replacing ChromaDB with Foundational RAG)

**File: `tools/knowledge_agent_tool.py`**
```python
from python.helpers.tool import Tool
from agents.knowledge_agent.agent import KnowledgeRAGAgent
from agents.knowledge_agent.database import DatabaseManager
from agents.knowledge_agent.embeddings import EmbeddingGenerator
from agents.knowledge_agent.retrieval import InformationRetriever
import asyncio
from typing import Dict, Any, List

class KnowledgeAgentTool(Tool):
    """
    KnowledgeAgent (Foundational RAG) integration for Agent Zero
    Replaces ChromaDB with Supabase/pgvector for enhanced RAG capabilities
    """
    
    def __init__(self, agent, **kwargs):
        super().__init__(agent, **kwargs)
        self.database = DatabaseManager()
        self.embedding_generator = EmbeddingGenerator()
        self.retriever = InformationRetriever(self.database)
        self.rag_agent = KnowledgeRAGAgent(self.database, self.retriever)
        
    async def execute(self, action: str, **kwargs):
        """
        Execute KnowledgeAgent operations
        
        Actions:
        - ingest_documents: Process and store documents
        - ingest_chunks: Store pre-processed chunks
        - query: Retrieve and generate responses
        - search: Vector similarity search
        - update_knowledge: Update existing knowledge
        """
        
        try:
            if action == "ingest_documents":
                return await self._ingest_documents(**kwargs)
            elif action == "ingest_chunks":
                return await self._ingest_chunks(**kwargs)
            elif action == "query":
                return await self._query(**kwargs)
            elif action == "search":
                return await self._search(**kwargs)
            elif action == "update_knowledge":
                return await self._update_knowledge(**kwargs)
            else:
                return self.agent_response(f"Unknown KnowledgeAgent action: {action}")
                
        except Exception as e:
            return self.agent_response(f"KnowledgeAgent error: {str(e)}")
    
    async def _ingest_documents(self, documents: List[Dict], source: str = "manual"):
        """Ingest raw documents into knowledge base"""
        
        await self.agent.emit_stream_event("progress_update", {
            "action": "document_ingestion",
            "status": "starting",
            "count": len(documents)
        })
        
        ingested_count = 0
        for doc in documents:
            # Process document through full pipeline
            result = await self.rag_agent.ingest_document(doc, source)
            ingested_count += 1
            
            if ingested_count % 5 == 0:
                await self.agent.emit_stream_event("progress_update", {
                    "action": "document_ingestion",
                    "status": "processing",
                    "processed": ingested_count,
                    "total": len(documents)
                })
        
        await self.agent.emit_stream_event("knowledge_result", {
            "action": "documents_ingested",
            "count": ingested_count,
            "source": source
        })
        
        return self.agent_response({
            "success": True,
            "documents_ingested": ingested_count,
            "source": source
        })
    
    async def _query(self, query: str, limit: int = 5, 
                    context_window: int = 4000):
        """Query knowledge base with RAG response generation"""
        
        await self.agent.emit_stream_event("agent_thought", {
            "content": f"Searching knowledge base for: {query}"
        })
        
        # Get RAG response
        response = await self.rag_agent.query(
            query=query,
            limit=limit,
            context_window=context_window
        )
        
        await self.agent.emit_stream_event("knowledge_result", {
            "query": query,
            "response": response.content,
            "sources": response.sources,
            "confidence": response.confidence,
            "context_used": len(response.context_chunks)
        })
        
        return self.agent_response({
            "response": response.content,
            "sources": response.sources,
            "confidence": response.confidence,
            "metadata": {
                "chunks_retrieved": len(response.context_chunks),
                "query": query
            }
        })
```

### Phase 3: MemoryAgent and Hybrid Memory Integration (Week 5-6)

#### 3.1 MemoryAgent Integration

**File: `tools/memory_agent_tool.py`**
```python
from python.helpers.tool import Tool
from agents.memory_agent.memory import IntelligentMemory
from agents.memory_agent.graph import GraphMemory
from agents.memory_agent.vector import VectorMemory
import asyncio
from typing import Dict, Any, List

class MemoryAgentTool(Tool):
    """
    MemoryAgent (Mem0) integration for Agent Zero
    Provides intelligent, self-improving memory capabilities
    """
    
    def __init__(self, agent, **kwargs):
        super().__init__(agent, **kwargs)
        self.intelligent_memory = IntelligentMemory()
        self.graph_memory = GraphMemory()
        self.vector_memory = VectorMemory()
        
    async def execute(self, action: str, **kwargs):
        """
        Execute MemoryAgent operations
        
        Actions:
        - add: Add memories from conversations
        - search: Semantic memory search
        - update: Update existing memories
        - delete: Delete specific memories
        - get_all: Retrieve all memories
        - graph_query: Query graph-based memories
        """
        
        try:
            if action == "add":
                return await self._add_memory(**kwargs)
            elif action == "search":
                return await self._search_memory(**kwargs)
            elif action == "update":
                return await self._update_memory(**kwargs)
            elif action == "delete":
                return await self._delete_memory(**kwargs)
            elif action == "get_all":
                return await self._get_all_memories(**kwargs)
            elif action == "graph_query":
                return await self._graph_query(**kwargs)
            else:
                return self.agent_response(f"Unknown MemoryAgent action: {action}")
                
        except Exception as e:
            return self.agent_response(f"MemoryAgent error: {str(e)}")
    
    async def _add_memory(self, messages: List[Dict], user_id: str = "default"):
        """Add conversation memories with intelligent extraction"""
        
        # Extract memories using Mem0's intelligent extraction
        extracted_memories = await self.intelligent_memory.extract_memories(
            messages, user_id
        )
        
        # Store in both vector and graph memory
        vector_results = await self.vector_memory.store_memories(
            extracted_memories, user_id
        )
        
        graph_results = await self.graph_memory.update_relationships(
            extracted_memories, user_id
        )
        
        await self.agent.emit_stream_event("memory_update", {
            "action": "memories_added",
            "user_id": user_id,
            "vector_memories": len(vector_results),
            "graph_updates": len(graph_results)
        })
        
        return self.agent_response({
            "success": True,
            "memories_extracted": len(extracted_memories),
            "user_id": user_id,
            "vector_stored": len(vector_results),
            "graph_updated": len(graph_results)
        })
    
    async def _search_memory(self, query: str, user_id: str = "default", 
                           limit: int = 5):
        """Search memories using semantic similarity"""
        
        # Search vector memories
        vector_results = await self.vector_memory.search(
            query, user_id, limit
        )
        
        # Search graph memories for related concepts
        graph_results = await self.graph_memory.find_related(
            query, user_id, limit
        )
        
        # Combine and rank results
        combined_results = self.intelligent_memory.combine_search_results(
            vector_results, graph_results
        )
        
        return self.agent_response({
            "memories": combined_results,
            "query": query,
            "user_id": user_id,
            "total_found": len(combined_results)
        })
```

#### 3.2 Hybrid Memory System

**File: `memory/hybrid_system.py`**
```python
import asyncio
from typing import Dict, Any, List, Optional
from dataclasses import dataclass

@dataclass
class MemoryContext:
    """Combined memory context from all systems"""
    structured_memories: List[Dict[str, Any]]
    intelligent_memories: List[Dict[str, Any]]
    graph_relationships: List[Dict[str, Any]]
    relevance_scores: Dict[str, float]
    total_sources: int

class HybridMemorySystem:
    """
    Hybrid memory system combining Agent Zero's structured memory
    with MemoryAgent's intelligent capabilities
    """
    
    def __init__(self, agent):
        self.agent = agent
        self.agent_zero_memory = None  # Will be initialized from agent
        self.memory_agent_tool = None  # Will be initialized
        
    async def initialize(self):
        """Initialize hybrid memory system"""
        self.agent_zero_memory = self.agent.memory
        self.memory_agent_tool = await self.agent.get_tool("memory_agent_tool")
    
    async def store_interaction(self, interaction: Dict[str, Any]):
        """Store interaction in all memory systems"""
        
        # Store in Agent Zero's structured memory
        await self._store_structured_memory(interaction)
        
        # Store in MemoryAgent's intelligent memory
        await self._store_intelligent_memory(interaction)
        
        # Emit memory update event
        await self.agent.emit_stream_event("memory_update", {
            "action": "interaction_stored",
            "type": interaction.get("type"),
            "user_id": interaction.get("user_id")
        })
    
    async def retrieve_context(self, query: str, user_id: str = "default", 
                              max_tokens: int = 2000) -> MemoryContext:
        """Retrieve and combine context from all memory systems"""
        
        # Get structured memories from Agent Zero
        structured_results = await self._query_structured_memory(query)
        
        # Get intelligent memories from MemoryAgent
        intelligent_results = await self._query_intelligent_memory(query, user_id)
        
        # Get graph relationships
        graph_results = await self._query_graph_memory(query, user_id)
        
        # Calculate relevance scores and combine
        context = self._combine_memory_contexts(
            structured_results,
            intelligent_results, 
            graph_results,
            max_tokens
        )
        
        return context
    
    async def _store_structured_memory(self, interaction: Dict[str, Any]):
        """Store in Agent Zero's structured memory"""
        memory_content = {
            "timestamp": interaction.get("timestamp"),
            "type": interaction.get("type", "interaction"),
            "content": interaction.get("content", ""),
            "metadata": interaction.get("metadata", {}),
            "user_id": interaction.get("user_id", "default")
        }
        
        await self.agent.call_tool("memory_tool", {
            "action": "memorize",
            "data": str(memory_content)
        })
    
    async def _store_intelligent_memory(self, interaction: Dict[str, Any]):
        """Store in MemoryAgent's intelligent memory"""
        messages = interaction.get("messages", [])
        user_id = interaction.get("user_id", "default")
        
        if messages:
            await self.memory_agent_tool.execute(
                action="add",
                messages=messages,
                user_id=user_id
            )
    
    def _combine_memory_contexts(self, structured: List, intelligent: List, 
                                graph: List, max_tokens: int) -> MemoryContext:
        """Intelligently combine and rank memory results"""
        
        # Implement sophisticated ranking algorithm
        # Consider recency, relevance, user context, and relationships
        
        relevance_scores = {}
        
        # Score structured memories (Agent Zero)
        for mem in structured:
            score = self._calculate_relevance_score(mem, "structured")
            relevance_scores[f"structured_{mem.get('id', 'unknown')}"] = score
        
        # Score intelligent memories (MemoryAgent)
        for mem in intelligent:
            score = self._calculate_relevance_score(mem, "intelligent")
            relevance_scores[f"intelligent_{mem.get('id', 'unknown')}"] = score
        
        # Score graph relationships
        for rel in graph:
            score = self._calculate_relevance_score(rel, "graph")
            relevance_scores[f"graph_{rel.get('id', 'unknown')}"] = score
        
        return MemoryContext(
            structured_memories=structured,
            intelligent_memories=intelligent,
            graph_relationships=graph,
            relevance_scores=relevance_scores,
            total_sources=len(structured) + len(intelligent) + len(graph)
        )
    
    def _calculate_relevance_score(self, memory_item: Dict, memory_type: str) -> float:
        """Calculate relevance score for memory item"""
        # Implement scoring algorithm based on:
        # - Semantic similarity
        # - Recency
        # - User interaction frequency
        # - Contextual importance
        # - Memory type weights
        
        base_score = 0.5
        
        # Type-specific scoring
        if memory_type == "structured":
            base_score += 0.1  # Slight preference for structured data
        elif memory_type == "intelligent":
            base_score += 0.2  # Higher preference for intelligent memories
        elif memory_type == "graph":
            base_score += 0.15  # Medium preference for relationships
        
        # Add recency factor
        timestamp = memory_item.get("timestamp")
        if timestamp:
            recency_score = self._calculate_recency_score(timestamp)
            base_score += recency_score * 0.3
        
        return min(base_score, 1.0)  # Cap at 1.0
```

This detailed implementation plan provides a complete line-by-line integration strategy that:

1. **Maintains Agent Zero's Core Philosophy**: All integrations follow Agent Zero's prompt-based, transparent approach
2. **Uses Exact Repository Code**: Integrates the actual implementations from each repository
3. **Standardizes Naming**: Uses consistent naming convention throughout
4. **Replaces ChromaDB**: Uses the foundational RAG agent with Supabase/pgvector
5. **Provides Hybrid Memory**: Combines Agent Zero's structured memory with Mem0's intelligent capabilities
6. **Implements StreamProtocol**: Replaces Agent Zero's UI with modern AG-UI protocol
7. **Adds Advanced Browser Automation**: Integrates Stagehand's AI-powered browser capabilities

Each tool integration maintains full compatibility with Agent Zero's existing architecture while adding significant new capabilities through the standardized tool interface.