# prompts/default/agent.system.tools.md

## Available Tools

This is a placeholder for the main tools configuration file.
In a complete Agent Zero implementation, this would include all available tools.

{{ include './agent.system.tool.browser.md' }}

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