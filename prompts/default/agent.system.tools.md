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