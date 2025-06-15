Of course. A task of this magnitude requires meticulous detail to ensure the AI coding agent can execute it successfully. This document provides a granular, step-by-step guide with explicit file paths, code snippets, and architectural reasoning for each change.

***

## **Project Task: Agent Zero "Phoenix" Upgrade - Detailed Implementation Plan**

### **1. Executive Summary & Objective**

**Project Codename:** Phoenix

**Objective:** To perform a comprehensive architectural upgrade of the Agent Zero platform. This involves replacing core components with modern, specialized systems for communication, browser automation, knowledge management, and memory. The final step is to replace the existing Text-to-Speech (TTS) system with a high-performance, streaming conversational AI voice engine.

**Target State:** Agent Zero will evolve from a monolithic agent into a modular, extensible platform capable of real-time interaction, advanced web intelligence, and sophisticated, self-improving memory and reasoning.

### **2. High-Level Architectural Vision**

The "Phoenix" upgrade introduces a clear separation of concerns. The core `agent.py` will become an orchestrator, delegating complex tasks to specialized "sub-agents" exposed as tools.

**New Directory Structure:**

```
agent-zero/
├── agents/                  <-- NEW: Houses backends for specialized agents
│   ├── browser_agent/
│   ├── knowledge_agent/
│   ├── memory_agent/
│   └── web_crawler/
├── protocols/               <-- NEW: Implements the real-time communication layer
│   └── stream_protocol/
├── tools/                   <-- MODIFIED: New tools will be added here
│   ├── stream_protocol_tool.py
│   ├── browser_agent_tool.py
│   ├── web_crawler_tool.py
│   ├── knowledge_agent_tool.py
│   └── memory_agent_tool.py
├── memory/                  <-- MODIFIED: Will contain the new hybrid memory system
│   └── hybrid_system.py
├── python/helpers/          <-- MODIFIED: New TTS helper will be added
│   └── tts_chatterbox.py
└── webui/                   <-- MODIFIED: Frontend logic updated for streaming
    └── js/
```

---

## **Phase 1: Real-Time Communication & Advanced Browser Control**

### **Task 1.1: Implement StreamProtocol Core (AG-UI)**

*   **Objective:** To replace the inefficient HTTP polling mechanism with a persistent, real-time streaming protocol. This is the foundational step for all subsequent UI and TTS enhancements.
*   **Affected Files:**
    *   **CREATE:** `tools/stream_protocol_tool.py`
    *   **CREATE:** `protocols/stream_protocol/events.py`
    *   **CREATE:** `protocols/stream_protocol/transport.py`
    *   **MODIFY:** `run_ui.py`
    *   **DELETE:** `python/api/poll.py`
*   **Step-by-Step Instructions:**
    1.  **Create the Tool Interface:** Create the file `tools/stream_protocol_tool.py` with the exact contents from the "Agent Zero Upgrade.md" document. This tool will be the agent's primary way to send standardized messages to the frontend.
    2.  **Implement the Protocol Backend:**
        *   Create the directory `protocols/stream_protocol`.
        *   Inside, create `events.py`. Populate it with the `StreamEventType` Enum and `StreamEvent` dataclass from the upgrade document. This defines the "language" of our new communication protocol.
        *   Create `transport.py` in the same directory. Implement the `StreamTransport` class to manage WebSocket/SSE connections. This class will be responsible for holding open connections and pushing events to the correct clients.
    3.  **Refactor the Main Server:**
        *   Open `run_ui.py`.
        *   Import `StreamTransport` and instantiate it.
        *   Remove the existing `/poll` route and its associated function.
        *   Add a new route, e.g., `@app.websocket("/stream")`, that will handle incoming WebSocket connections. When a client connects, it should be registered with the `StreamTransport` instance.
    4.  **Deprecate Polling API:** Delete the file `python/api/poll.py`. Its functionality is now obsolete.
*   **Verification:** After this task, the server will run without errors, and you should be able to connect to the `/stream` endpoint using a WebSocket client. The old `/poll` endpoint should return a 404 error.

### **Task 1.2: Frontend Integration with StreamProtocol**

*   **Objective:** To update the web UI to use the new real-time streaming connection, eliminating polling and enabling a more responsive user experience.
*   **Affected Files:**
    *   **MODIFY:** `webui/js/messages.js`
    *   **MODIFY:** `webui/js/api.js`
*   **Step-by-Step Instructions:**
    1.  **Establish Persistent Connection:** In `webui/js/messages.js` (or a suitable main JS file), modify the initialization logic. Instead of repeated `fetch` calls to `/poll`, create a single `WebSocket` or `EventSource` object that connects to `ws://<your_host>/stream` upon page load.
    2.  **Implement Event Listener:** Add an `onmessage` event handler to the WebSocket object. This handler will receive all real-time events from the server.
    3.  **Create an Event Router:** Inside the `onmessage` handler, parse the incoming JSON event. Use a `switch` statement on `event.type` (e.g., `case "AGENT_THOUGHT":`) to call different UI update functions based on the event type.
    4.  **Refactor UI Updates:** Modify the existing UI update functions to accept data directly from the event router instead of a polling response. For example, a `TOOL_CALL_START` event will now immediately trigger the UI to show the "tool in use" animation.
    5.  **Remove Polling Logic:** Delete the `poll` function and any `setInterval` or `setTimeout` calls that trigger it.
*   **Verification:** The web UI should load and function correctly. All agent activity (thoughts, tool calls, responses) should appear in the UI in real-time without the page making repeated requests to a `/poll` endpoint (verify in the browser's Network tab).

### **Task 1.3: Browser Automation Upgrade (BrowserAgent)**

*   **Objective:** To replace the limited, hard-coded browser tools with the flexible, AI-driven BrowserAgent, enabling complex web interactions.
*   **Affected Files:**
    *   **CREATE:** `agents/browser_agent/` (directory and internal files like `browser.py`, `ai_models.py`, `actions.py`)
    *   **CREATE:** `tools/browser_agent_tool.py`
    *   **MODIFY:** `requirements.txt`
    *   **MODIFY:** `prompts/default/agent.system.tool.browser.md`
    *   **DELETE:** `python/tools/browser_open._py`, `python/tools/browser_do._py`, `python/tools/webpage_content_tool.py`
*   **Step-by-Step Instructions:**
    1.  **Implement the Backend:** Create the `agents/browser_agent/` directory. Inside, build out the necessary Python modules to interface with the Stagehand library. This involves a `BrowserManager` to handle Playwright instances and a way to call the AI models Stagehand relies on.
    2.  **Create the Tool:** Implement `tools/browser_agent_tool.py` exactly as specified in the upgrade document. This tool will expose high-level actions like `navigate`, `act`, and `extract` to the main agent.
    3.  **Update Dependencies:** Add `stagehand` to `requirements.txt`.
    4.  **Update Prompts:** Open `prompts/default/agent.system.tool.browser.md`. Delete the existing content describing the old tools. Replace it with a detailed description of the new `browser_agent_tool` and its powerful, natural-language-based actions.
    5.  **Deprecate Old Tools:** Delete the specified old browser tool files. Their functionality is now superseded by the more capable BrowserAgent.
*   **Verification:** The agent should be able to receive a task like "Open Google, search for 'Agent Zero', and extract the GitHub link," and successfully execute it using the new `browser_agent_tool`.

---

## **Phase 2: Advanced Knowledge and Memory Systems**

### **Task 2.1: Web Crawling and Ingestion (WebCrawler)**

*   **Objective:** To implement an intelligent web crawler that can automatically ingest and process documentation from websites, preparing it for the RAG system.
*   **Affected Files:**
    *   **CREATE:** `agents/web_crawler/` (directory and internal files like `crawler.py`, `processors.py`, `chunker.py`)
    *   **CREATE:** `tools/web_crawler_tool.py`
    *   **MODIFY:** `requirements.txt`
*   **Step-by-Step Instructions:**
    1.  **Implement Crawler Backend:** Create the `agents/web_crawler/` directory. Implement the core crawling logic based on the Crawl4AI architecture. This includes recursive link following, sitemap parsing, and document content extraction.
    2.  **Create the Tool:** Implement `tools/web_crawler_tool.py` as specified. This tool will allow the agent to initiate crawls on demand (e.g., "Crawl the documentation for the Chatterbox library").
    3.  **Integrate with KnowledgeAgent:** The `_crawl_site` method within the `WebCrawlerTool` must be programmed to call the `KnowledgeAgentTool`'s `ingest_chunks` action. This creates a direct pipeline from crawling to knowledge base ingestion.
    4.  **Update Dependencies:** Add `crawl4ai` and its dependencies to `requirements.txt`.
*   **Verification:** The agent can be given a URL and will successfully crawl the site, with progress updates being sent via the `StreamProtocol`. The crawled content should be passed to the (yet to be fully implemented) KnowledgeAgent.

### **Task 2.2: RAG System Overhaul (KnowledgeAgent)**

*   **Objective:** To replace the existing FAISS/ChromaDB vector store with the more robust Foundational RAG agent, which uses a scalable Supabase/pgvector backend.
*   **Affected Files:**
    *   **CREATE:** `agents/knowledge_agent/` (directory and internal files like `database.py`, `retrieval.py`)
    *   **CREATE:** `tools/knowledge_agent_tool.py`
    *   **MODIFY:** `.env.example`
    *   **DELETE:** `python/tools/knowledge_tool.py`, `python/api/import_knowledge.py`
*   **Step-by-Step Instructions:**
    1.  **Implement RAG Backend:** Create the `agents/knowledge_agent/` directory. The `database.py` module is critical and must contain functions to connect to Supabase and perform vector similarity searches using pgvector SQL queries.
    2.  **Create the Tool:** Implement `tools/knowledge_agent_tool.py`. This tool will expose `ingest` and `query` actions.
    3.  **Update Configuration:** Add `SUPABASE_URL` and `SUPABASE_KEY` to the `.env.example` file.
    4.  **Deprecate Old System:** Delete the old `knowledge_tool.py` and the `import_knowledge.py` API endpoint. The new system is far more capable.
*   **Verification:** After the WebCrawler runs, data should be visible in your Supabase project's database. A query to the agent that requires this knowledge should trigger the `KnowledgeAgentTool`, which should successfully retrieve relevant chunks from Supabase and provide a sourced answer.

### **Task 2.3: Hybrid Memory System (Mem0 Integration)**

*   **Objective:** To create a dual-memory system where the agent benefits from both its original structured memory and a new, intelligent, self-organizing memory graph.
*   **Affected Files:**
    *   **CREATE:** `agents/memory_agent/` (directory and internal files)
    *   **CREATE:** `tools/memory_agent_tool.py`
    *   **CREATE:** `memory/hybrid_system.py`
    *   **MODIFY:** `agent.py`
*   **Step-by-Step Instructions:**
    1.  **Implement MemoryAgent Backend:** Create the `agents/memory_agent/` directory and its internal modules based on the Mem0 architecture.
    2.  **Create the Tool:** Implement `tools/memory_agent_tool.py` to expose Mem0's capabilities (`add`, `search`, `update`) to the agent ecosystem.
    3.  **Implement the Hybrid Orchestrator:** This is the most complex part. Create `memory/hybrid_system.py`. The `HybridMemorySystem` class must have a `retrieve_context` method. This method will asynchronously call *both* the old `memory_load` tool and the new `memory_agent_tool`. It will then receive two sets of results, which it must combine, rank based on relevance and recency, and then format into a single, coherent context block for the main agent.
    4.  **Refactor the Core Agent:** In the main `agent.py`, find the part of the agent's reasoning loop where it recalls memories. Replace the direct call to `memory_load` with a call to the `HybridMemorySystem`'s `retrieve_context` method.
*   **Verification:** After a conversation, you should be able to inspect the memory and see data stored in both the old `memory/` directory structure and in the new system managed by Mem0. When the agent recalls a memory, the log should show that it's querying the hybrid system and receiving a combined context.

---

## **Phase 3: User Experience Polish**

### **Task 3.1: Conversational TTS Upgrade (Chatterbox)**

*   **Objective:** To replace the current, non-streaming TTS with Chatterbox for a fluid, low-latency conversational experience.
*   **Affected Files:**
    *   **CREATE:** `python/helpers/tts_chatterbox.py`
    *   **MODIFY:** `tools/stream_protocol_tool.py` (or a related handler)
    *   **MODIFY:** `webui/js/speech.js`
    *   **MODIFY:** `requirements.txt`
    *   **MODIFY:** `.env.example`
    *   **DELETE:** All files related to the old TTS system.
*   **Step-by-Step Instructions:**
    1.  **Add Dependency & Config:** Add `chatterbox-python` to `requirements.txt` and `CHATTERBOX_API_KEY` to `.env.example`.
    2.  **Create TTS Helper:** Implement `python/helpers/tts_chatterbox.py`. This module will contain a class that initializes the Chatterbox client and has a method like `start_streaming_tts(text)`. This method will not return the full audio but will yield audio chunks as they are generated by the Chatterbox service.
    3.  **Integrate with Communication Protocol:** Modify the `StreamProtocolTool` or the main server logic in `run_ui.py`. When an event of type `TEXT_MESSAGE_CONTENT` is generated by the assistant, it should immediately trigger the `tts_chatterbox` helper. As the helper yields audio chunks, they must be wrapped in a new custom stream event (e.g., `AUDIO_CHUNK`) and sent to the frontend via the WebSocket connection.
    4.  **Upgrade Frontend Audio Player:** In `webui/js/speech.js`, the logic must be rewritten. It will now receive a stream of `AUDIO_CHUNK` events. Use the browser's Web Audio API (`AudioContext`, `SourceBuffer`) to append these incoming audio chunks to a buffer and play them seamlessly. This is the key to achieving low-latency playback.
    5.  **Cleanup:** Thoroughly remove all code, helper files, and UI elements related to the old TTS system.
*   **Verification:** When the agent generates a response, audio should begin playing almost instantly, well before the full text has been displayed in the UI. The audio should be natural and uninterrupted.