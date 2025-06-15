# Agent Zero Tools Reference

## Available Tools

This document provides comprehensive descriptions of all available tools in the Agent Zero Phoenix system. Each tool includes detailed parameter specifications, usage examples, and integration notes.

## Core Response Tools

### response
**Purpose**: Send a final response to the user and optionally end the conversation.

**Parameters**:
- `text` (required): The response text to send to the user

**Usage**: Use this tool to provide final answers, conclusions, or when the task is complete.

**Example**:
```json
{"tool_name": "response", "tool_args": {"text": "Task completed successfully. Here are the results..."}}
```

## Browser Automation Tools

### browser_agent
**Purpose**: Controls a browser for interactive tasks including navigation, element interaction, and data extraction.

**Actions**:
- `navigate`: Navigate to a specific URL
- `act`: Perform AI-powered actions on the current page
- `extract`: Extract structured data from the current page
- `agent_execute`: Execute complex multi-step browser automation tasks
- `get_page_content`: Get current page content and metadata
- `new_page`: Open a new page in the browser session
- `close_page`: Close a specific page
- `close_context_session`: Close the entire browser session

**Parameters**:
- `action` (required): Type of browser operation
- `session_id` (optional): Browser session identifier (defaults to thread_id)
- `page_index` (optional): Target page index within session (default: 0)
- `url`: Target URL (for navigate action)
- `instructions`: Natural language instructions (for act and extract actions)
- `schema`: JSON schema for structured extraction (optional, for extract action)
- `model`: Specific model for task planning (optional, for agent_execute action)

**Events**: Emits BROWSER_ACTION events for all operations with detailed progress tracking.

**Examples**:
```json
{"tool_name": "browser_agent", "tool_args": {"action": "navigate", "url": "https://example.com"}}
{"tool_name": "browser_agent", "tool_args": {"action": "act", "instructions": "Click the login button and fill username with 'user'"}}
{"tool_name": "browser_agent", "tool_args": {"action": "extract", "instructions": "Get article title and author", "schema": {"type": "object", "properties": {"title": {"type": "string"}, "author": {"type": "string"}}}}}
```

### web_crawler_tool

**Purpose**: Crawls websites, sitemaps, or markdown files, processes content, and prepares it for knowledge base ingestion using Crawl4AI-inspired techniques.

**Actions**:
- `crawl_site`: Recursively crawl a website starting from a URL
- `crawl_sitemap`: Crawl URLs from a sitemap or URL list
- `crawl_markdown_file_url`: Crawl a single markdown/text file from URL

**Parameters**:
- `action` (required): Type of crawl operation
- `url`: Target URL for crawl_site and crawl_markdown_file_url
- `sitemap_url`: Sitemap URL for crawl_sitemap
- `urls`: List of URLs for crawl_sitemap
- `max_depth`: Maximum recursion depth (default: 3)
- `max_pages`: Maximum pages to crawl (default: 100)
- `chunk_size`: Maximum characters per chunk (default: 1000)

**Events**: Emits CRAWL_PROGRESS events via StreamProtocol for real-time progress tracking.

**Example**:
```
Action: web_crawler_tool
Parameters: {"action": "crawl_site", "url": "https://example.com", "max_depth": 2, "max_pages": 50}
```

### knowledge_agent_tool

**Purpose**: Manages and queries a knowledge base using RAG (Retrieval-Augmented Generation) principles for intelligent document ingestion and retrieval.

**Actions**:
- `ingest_chunks`: Ingest pre-processed document chunks into the knowledge base
- `query`: Query the knowledge base and generate RAG-enhanced responses
- `raw_search`: Perform direct semantic search without response generation
- `list_sources`: List all unique sources in the knowledge base

**Parameters**:
- `action` (required): Type of knowledge operation
- `chunks_data`: List of chunks to ingest (for ingest_chunks) - each dict needs "text", "metadata", "id". "embedding" is optional
- `query`: Search query or question (for query and raw_search)
- `limit`: Maximum number of results to return (default: 5)
- `filter_metadata`: Metadata filters for search (for raw_search)

**Events**: Emits KNOWLEDGE_RESULT and PROGRESS_UPDATE events via StreamProtocol for real-time feedback.

**Example for ingesting chunks**:
```
Action: knowledge_agent_tool
Parameters: {
  "action": "ingest_chunks",
  "chunks_data": [
    {
      "text": "Content of chunk 1",
      "metadata": {"source": "doc1.pdf", "source_url": "https://example.com/doc1.pdf"},
      "id": "doc1_chunk0"
    }
  ]
}
```

**Example for querying**:
```
Action: knowledge_agent_tool
Parameters: {"action": "query", "query": "What is Pydantic AI?", "limit": 3}
```

### memory_agent_tool

**Purpose**: Manages an intelligent memory system with self-improving capabilities, allowing agents to store, search, update, and retrieve memories using Mem0-inspired techniques.

**Actions**:
- `add`: Add new memories from messages or generic data
- `search`: Search existing memories by query
- `update`: Update an existing memory
- `delete`: Delete a specific memory
- `get_all`: Retrieve all memories for debugging or analysis

**Parameters**:
- `action` (required): Type of memory operation
- `user_id`: Identifier for the user whose memory is being accessed (optional, defaults to current session)
- `messages`: List of messages to extract memories from (for add action) - format: [{"role": "user/assistant", "content": "..."}]
- `data`: Generic data to store as a memory (for add action)
- `memory_id`: Specific ID for memory operations (for update/delete actions)
- `query`: Search query (for search action)
- `limit`: Maximum number of results to return (default: 5)

**Events**: Emits MEMORY_UPDATE events via StreamProtocol for real-time memory operation feedback.

**Example for adding from messages**:
```
Action: memory_agent_tool
Parameters: {
  "action": "add",
  "messages": [{"role": "user", "content": "My favorite color is blue."}],
  "user_id": "user123"
}
```

**Example for searching memories**:
```
Action: memory_agent_tool
Parameters: {"action": "search", "query": "user's favorite color", "user_id": "user123", "limit": 3}
```

**Example for updating a memory**:
```
Action: memory_agent_tool
Parameters: {
  "action": "update",
  "memory_id": "mem_0",
  "data": "My favorite color is now green instead of blue.",
  "user_id": "user123"
}
```

### hybrid_memory_tool

**Purpose**: Manages a hybrid memory system that combines Agent Zero's structured memory with intelligent Mem0-inspired memory capabilities, providing a unified interface for storing and retrieving context.

**Actions**:
- `store_interaction`: Store interaction data in both structured and intelligent memory systems
- `retrieve_context`: Retrieve and combine relevant context from both memory systems

**Parameters**:
- `action` (required): Type of hybrid memory operation
- `user_id`: Identifier for the user context (optional, defaults to current session)
- `interaction_data`: Data about the interaction to store (for store_interaction) - should include 'content' for structured memory and can include 'messages' for intelligent memory
- `query`: Query to retrieve relevant context (for retrieve_context)
- `limit`: Maximum results from each memory source (default: 5)

**Events**: Emits MEMORY_UPDATE events via StreamProtocol with hybrid memory operation details.

**Example for storing an interaction**:
```
Action: hybrid_memory_tool
Parameters: {
  "action": "store_interaction",
  "interaction_data": {
    "type": "user_query",
    "content": "User asked about machine learning algorithms",
    "messages": [{"role": "user", "content": "What are the best ML algorithms for classification?"}],
    "timestamp": "2024-01-15T10:30:00Z"
  },
  "user_id": "user456"
}
```

**Example for retrieving context**:
```
Action: hybrid_memory_tool
Parameters: {
  "action": "retrieve_context",
  "query": "machine learning classification algorithms",
  "limit": 3,
  "user_id": "user456"
}
```

### chatterbox_tts_tool

**Purpose**: Generates speech from text (TTS) or performs voice conversion (VC) using Chatterbox models for high-quality AI speech synthesis.

**Actions**:
- `generate_speech`: Convert text to speech with optional voice cloning
- `convert_voice`: Convert one voice to another using voice conversion

**Parameters**:
- `action` (required): Type of TTS operation
- `text`: Text to synthesize (for generate_speech)
- `audio_prompt_path`: Path to .wav file for voice cloning (optional)
- `exaggeration`: Controls emotion/intensity (default: 0.5)
- `cfg_weight`: Controls pacing/adherence to prompt (default: 0.5)  
- `temperature`: Sampling temperature (default: 0.8)
- `source_audio_path`: Path to source .wav file (for convert_voice)
- `target_voice_path`: Path to target voice .wav file (for convert_voice)

**Events**: Emits PROGRESS_UPDATE events via StreamProtocol for TTS generation progress tracking.

**Example for TTS generation**:
```
Action: chatterbox_tts_tool
Parameters: {
  "action": "generate_speech",
  "text": "Hello, world! This is Agent Zero speaking.",
  "audio_prompt_path": "/path/to/reference_voice.wav",
  "exaggeration": 0.7,
  "temperature": 0.9
}
```

**Example for Voice Conversion**:
```
Action: chatterbox_tts_tool
Parameters: {
  "action": "convert_voice",
  "source_audio_path": "/path/to/source_audio.wav",
  "target_voice_path": "/path/to/target_voice_prompt.wav"
}
```