# python/tools/web_crawler_tool.py
from python.helpers.tool import Tool, Response as ToolResponse
from typing import Dict, Any, List, Optional

# Import StreamProtocol components if available
try:
    from python.tools.stream_protocol_tool import StreamEventType
    STREAM_PROTOCOL_AVAILABLE = True
except ImportError:
    STREAM_PROTOCOL_AVAILABLE = False
    StreamEventType = None

# Import web crawler components
from python.agents.web_crawler.crawler import DocumentCrawler
from python.agents.web_crawler.processors import DocumentProcessor
from python.agents.web_crawler.chunker import HierarchicalChunker

class WebCrawlerTool(Tool):
    """
    WebCrawler (Crawl4AI-inspired) integration for Agent Zero.
    Provides intelligent web crawling and documentation processing.
    """
    
    def __init__(self, agent, **kwargs):
        super().__init__(
            agent=agent, 
            name="web_crawler_tool", 
            description="Crawls websites, sitemaps, or markdown files, processes content, and prepares it for knowledge base ingestion.",
            args_schema={
                "type": "object",
                "properties": {
                    "action": {
                        "type": "string",
                        "enum": ["crawl_site", "crawl_sitemap", "crawl_markdown_file_url"],
                        "description": "Type of crawl to perform"
                    },
                    "url": {
                        "type": "string",
                        "description": "URL to crawl (required for crawl_site and crawl_markdown_file_url)"
                    },
                    "sitemap_url": {
                        "type": "string",
                        "description": "Sitemap URL to parse (optional for crawl_sitemap)"
                    },
                    "urls": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "List of URLs to crawl (optional for crawl_sitemap)"
                    },
                    "max_depth": {
                        "type": "integer",
                        "description": "Maximum recursion depth for crawl_site (default: 3)"
                    },
                    "max_pages": {
                        "type": "integer", 
                        "description": "Maximum pages to crawl for crawl_site (default: 100)"
                    },
                    "chunk_size": {
                        "type": "integer",
                        "description": "Maximum characters per chunk (default: 1000)"
                    }
                },
                "required": ["action"]
            },
            **kwargs
        )
        self.crawler = DocumentCrawler()
        self.processor = DocumentProcessor()
        self.chunker = HierarchicalChunker()  # Default chunk size
        print(f"WebCrawlerTool initialized for agent {agent.agent_name} (context: {agent.context.id})")

    async def _emit_crawl_event(self, action_name: str, status: str, details: Optional[Dict[str, Any]] = None):
        """Helper to emit CRAWL_PROGRESS events."""
        if not STREAM_PROTOCOL_AVAILABLE:
            print(f"WebCrawlerTool: StreamProtocol not available, logging event: {action_name} - {status}")
            return
            
        payload = {"action": action_name, "status": status}
        if details:
            payload.update(details)
        
        if hasattr(self.agent, '_emit_stream_event'):
            await self.agent._emit_stream_event(StreamEventType.CRAWL_PROGRESS, payload)
        else:
            print(f"WebCrawlerTool: Agent does not have _emit_stream_event method. Cannot emit CRAWL_PROGRESS.")

    async def execute(self, **kwargs) -> ToolResponse:
        """
        Execute WebCrawler operations.
        
        Args:
            action (str): Crawling action (e.g., "crawl_site", "crawl_sitemap", "crawl_markdown_file_url").
            **kwargs: Arguments for the action.
        """
        action = kwargs.get("action")
        if not action:
            return ToolResponse(
                success=False,
                error="Missing required 'action' parameter",
                message="Error: 'action' is required for WebCrawler operations."
            )
            
        chunk_size = kwargs.get("chunk_size", 1000)  # Allow overriding default chunk size
        self.chunker = HierarchicalChunker(chunk_size=chunk_size)  # Re-init with potentially new chunk_size

        try:
            if action == "crawl_site":
                url = kwargs.get("url")
                max_depth = kwargs.get("max_depth", 3)
                max_pages = kwargs.get("max_pages", 100)
                if not url:
                    return ToolResponse(
                        success=False,
                        error="Missing 'url' parameter",
                        message="Error: 'url' is required for crawl_site action."
                    )
                return await self._crawl_site(url, max_depth, max_pages)
                
            elif action == "crawl_sitemap":
                sitemap_url = kwargs.get("sitemap_url")
                urls_from_sitemap = kwargs.get("urls", [])
                if not sitemap_url and not urls_from_sitemap:
                    return ToolResponse(
                        success=False,
                        error="Missing required parameters",
                        message="Error: 'sitemap_url' or 'urls' list is required for crawl_sitemap action."
                    )
                if sitemap_url and not urls_from_sitemap:  # Mock parsing if only URL given
                    print(f"WebCrawlerTool: Mock parsing sitemap URL {sitemap_url}")
                    urls_from_sitemap = [f"{sitemap_url.rsplit('/',1)[0]}/mock_page_{i}" for i in range(3)]
                return await self._crawl_sitemap_urls(urls_from_sitemap)
                
            elif action == "crawl_markdown_file_url":
                url = kwargs.get("url")
                if not url:
                    return ToolResponse(
                        success=False,
                        error="Missing 'url' parameter",
                        message="Error: 'url' is required for crawl_markdown_file_url action."
                    )
                return await self._crawl_markdown_file_url(url)
                
            else:
                return ToolResponse(
                    success=False,
                    error=f"Unknown action: {action}",
                    message=f"Unknown WebCrawler action: {action}"
                )
                
        except Exception as e:
            import traceback
            error_message = f"WebCrawlerTool error during action '{action}': {str(e)}"
            print(f"{error_message}\n{traceback.format_exc()}")
            await self._emit_crawl_event(action, "error", {"error": str(e)})
            return ToolResponse(
                success=False,
                error=str(e),
                message=error_message
            )

    async def _process_and_ingest_crawled_doc(self, raw_doc_data: Dict[str, Any]) -> int:
        """Helper to process a single raw doc, chunk it, and 'ingest' (log for now)."""
        processed_doc = await self.processor.process_document(raw_doc_data)
        if not processed_doc.get("markdown"):
            print(f"WebCrawlerTool: No markdown content after processing {raw_doc_data.get('url')}")
            return 0
            
        chunks_with_metadata = await self.chunker.chunk_document(processed_doc)
        
        if not chunks_with_metadata:
            print(f"WebCrawlerTool: No chunks generated for {processed_doc.get('url')}")
            return 0

        # Placeholder for actual ingestion via KnowledgeAgentTool
        # In a later task, this will call:
        # await self.agent.call_tool("knowledge_agent_tool", {
        #     "action": "ingest_chunks",
        #     "chunks": chunks_with_metadata,
        #     "metadatas": [chunk['metadata'] for chunk in chunks_with_metadata],
        #     "ids": [f"{processed_doc.get('url')}_chunk_{i}" for i in range(len(chunks_with_metadata))]
        # })
        print(f"WebCrawlerTool (Mock Ingestion): Would ingest {len(chunks_with_metadata)} chunks for {processed_doc.get('url')}.")
        for i, chunk_data in enumerate(chunks_with_metadata):
             print(f"  Chunk {i}: {chunk_data['text'][:80]}... Metadata: {chunk_data['metadata']}")
        
        return len(chunks_with_metadata)

    async def _crawl_site(self, url: str, max_depth: int, max_pages: int) -> ToolResponse:
        await self._emit_crawl_event("crawl_site", "starting", {"url": url, "max_depth": max_depth, "max_pages": max_pages})
        
        total_chunks_ingested = 0
        pages_processed_count = 0
        
        async for raw_doc_data in self.crawler.crawl_recursive(url, max_depth, max_pages):
            chunks_ingested = await self._process_and_ingest_crawled_doc(raw_doc_data)
            total_chunks_ingested += chunks_ingested
            pages_processed_count += 1
            if pages_processed_count % 5 == 0:  # Emit progress periodically
                await self._emit_crawl_event("crawl_site", "progress", {
                    "url": url, "pages_processed": pages_processed_count, 
                    "chunks_ingested_so_far": total_chunks_ingested
                })
        
        summary = f"Site crawl completed for {url}. Processed {pages_processed_count} pages, ingested {total_chunks_ingested} chunks."
        await self._emit_crawl_event("crawl_site", "completed", {
            "url": url, "pages_processed": pages_processed_count, "total_chunks_ingested": total_chunks_ingested
        })
        return ToolResponse(
            success=True,
            data={"pages_processed": pages_processed_count, "total_chunks_ingested": total_chunks_ingested},
            message=summary
        )

    async def _crawl_sitemap_urls(self, urls: List[str]) -> ToolResponse:
        await self._emit_crawl_event("crawl_sitemap", "starting", {"url_count": len(urls)})
        total_chunks_ingested = 0
        pages_processed_count = 0
        
        async for raw_doc_data in self.crawler.crawl_sitemap_urls(urls):
            chunks_ingested = await self._process_and_ingest_crawled_doc(raw_doc_data)
            total_chunks_ingested += chunks_ingested
            pages_processed_count += 1
            if pages_processed_count % 5 == 0:
                 await self._emit_crawl_event("crawl_sitemap", "progress", {
                    "processed_urls": pages_processed_count, "total_urls": len(urls),
                    "chunks_ingested_so_far": total_chunks_ingested
                })

        summary = f"Sitemap crawl completed. Processed {pages_processed_count} URLs, ingested {total_chunks_ingested} chunks."
        await self._emit_crawl_event("crawl_sitemap", "completed", {
            "processed_urls": pages_processed_count, "total_chunks_ingested": total_chunks_ingested
        })
        return ToolResponse(
            success=True,
            data={"processed_urls": pages_processed_count, "total_chunks_ingested": total_chunks_ingested},
            message=summary
        )

    async def _crawl_markdown_file_url(self, url: str) -> ToolResponse:
        await self._emit_crawl_event("crawl_markdown_file_url", "starting", {"url": url})
        total_chunks_ingested = 0
        
        async for raw_doc_data in self.crawler.crawl_markdown_file_url(url):
            chunks_ingested = await self._process_and_ingest_crawled_doc(raw_doc_data)
            total_chunks_ingested += chunks_ingested
        
        summary = f"Markdown file crawl completed for {url}. Ingested {total_chunks_ingested} chunks."
        await self._emit_crawl_event("crawl_markdown_file_url", "completed", {
            "url": url, "total_chunks_ingested": total_chunks_ingested
        })
        return ToolResponse(
            success=True,
            data={"url": url, "total_chunks_ingested": total_chunks_ingested},
            message=summary
        )