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
                        "enum": ["crawl_site", "crawl_sitemap", "crawl_markdown_file_url", "discover_sitemap", "analyze_site"],
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
                    },
                    "delay": {
                        "type": "number",
                        "description": "Delay between requests in seconds (default: 1.0)"
                    }
                },
                "required": ["action"]
            },
            **kwargs
        )
        # Initialize with default settings - will be updated per request
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
            
        # Configure chunker for this request
        chunk_size = int(kwargs.get("chunk_size", 1000)) # Ensure it's int
        # Overlap can also be a parameter if HierarchicalChunker uses it
        chunker_instance = HierarchicalChunker(chunk_size=chunk_size)

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
                return await self._crawl_site(url, max_depth, max_pages, chunker_instance)
                
            elif action == "crawl_sitemap":
                sitemap_url = kwargs.get("sitemap_url")
                urls_from_sitemap = kwargs.get("urls", [])
                if not sitemap_url and not urls_from_sitemap:
                    return ToolResponse(
                        success=False,
                        error="Missing required parameters",
                        message="Error: 'sitemap_url' or 'urls' list is required for crawl_sitemap action."
                    )
                if sitemap_url and not urls_from_sitemap:
                    # Use crawl_sitemap_urls with sitemap URL directly
                    print(f"WebCrawlerTool: Using sitemap URL directly: {sitemap_url}")
                    return await self._crawl_sitemap_urls(sitemap_url, chunker_instance)
                return await self._crawl_sitemap_urls(urls_from_sitemap, chunker_instance)

            elif action == "crawl_markdown_file_url":
                url = kwargs.get("url")
                if not url:
                    return ToolResponse(
                        success=False,
                        error="Missing 'url' parameter",
                        message="Error: 'url' is required for crawl_markdown_file_url action."
                    )
                return await self._crawl_markdown_file_url(url, chunker_instance)



            elif action == "discover_sitemap":
                url = kwargs.get("url")
                if not url:
                    return ToolResponse(
                        success=False,
                        error="Missing 'url' parameter",
                        message="Error: 'url' is required for discover_sitemap action."
                    )
                return await self._discover_sitemap(url)

            elif action == "analyze_site":
                url = kwargs.get("url")
                if not url:
                    return ToolResponse(
                        success=False,
                        error="Missing 'url' parameter",
                        message="Error: 'url' is required for analyze_site action."
                    )
                return await self._analyze_site(url)

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

    async def _process_and_ingest_crawled_doc(self, crawl_result: Any, chunker_instance: HierarchicalChunker) -> int:
        """Helper to process a single Crawl4AI result, chunk it, and ingest via KnowledgeAgentTool."""
        if not crawl_result.success:
            msg = f"Skipping failed crawl for {crawl_result.url}: {crawl_result.error_message}"
            print(f"WebCrawlerTool: {msg}")
            await self._emit_crawl_event("page_processing", "error", {"url": crawl_result.url, "error": crawl_result.error_message})
            return 0

        processed_doc_dict = await self.processor.process_document(crawl_result)

        if not processed_doc_dict.get("markdown"):
            msg = f"No markdown content after processing {crawl_result.url}"
            print(f"WebCrawlerTool: {msg}")
            await self._emit_crawl_event("page_processing", "warning", {"url": crawl_result.url, "message": msg})
            return 0

        # Use the passed chunker_instance
        chunks_with_metadata_and_ids = await chunker_instance.chunk_document(processed_doc_dict)

        if not chunks_with_metadata_and_ids:
            msg = f"No chunks generated for {crawl_result.url}"
            print(f"WebCrawlerTool: {msg}")
            await self._emit_crawl_event("chunking", "warning", {"url": crawl_result.url, "message": msg})
            return 0

        # Actual ingestion via KnowledgeAgentTool
        # KnowledgeAgentTool._ingest_chunks expects `chunks_data` where each item has "text", "metadata", "id", and optionally "embedding".
        # Our chunker_instance.chunk_document already returns this format.

        print(f"WebCrawlerTool: Attempting to ingest {len(chunks_with_metadata_and_ids)} chunks for {crawl_result.url} via KnowledgeAgentTool.")
        await self._emit_crawl_event("ingestion_knowledge_agent", "starting", {"url": crawl_result.url, "chunk_count": len(chunks_with_metadata_and_ids)})

        try:
            # Call the KnowledgeAgentTool
            # The `chunks_data` from `HierarchicalChunker` should be suitable.
            # Embedding generation will happen inside KnowledgeAgentTool if not provided.
            ingestion_response = await self.agent.call_tool(
                "knowledge_agent_tool",
                {
                    "action": "ingest_chunks",
                    "chunks_data": chunks_with_metadata_and_ids
                }
            )
            if ingestion_response and not ingestion_response.error:
                ingested_count = ingestion_response.data.get("count", 0) if ingestion_response.data else 0
                print(f"WebCrawlerTool: KnowledgeAgentTool ingested {ingested_count} chunks for {crawl_result.url}.")
                await self._emit_crawl_event("ingestion_knowledge_agent", "completed", {"url": crawl_result.url, "ingested_count": ingested_count, "response": ingestion_response.message})
                return ingested_count
            else:
                error_msg = ingestion_response.message if ingestion_response else "Unknown ingestion error"
                print(f"WebCrawlerTool: KnowledgeAgentTool ingestion failed for {crawl_result.url}: {error_msg}")
                await self._emit_crawl_event("ingestion_knowledge_agent", "error", {"url": crawl_result.url, "error": error_msg})
                return 0
        except Exception as e:
            import traceback
            error_msg = f"Exception calling KnowledgeAgentTool for {crawl_result.url}: {e}\n{traceback.format_exc()}"
            print(f"WebCrawlerTool: {error_msg}")
            await self._emit_crawl_event("ingestion_knowledge_agent", "error", {"url": crawl_result.url, "error": str(e)})
            return 0

    async def _crawl_site(self, url: str, max_depth: int, max_pages: int, chunker_instance: HierarchicalChunker) -> ToolResponse:
        await self._emit_crawl_event("crawl_site", "starting", {"url": url, "max_depth": max_depth, "max_pages": max_pages})

        total_chunks_ingested = 0
        pages_processed_count = 0

        async for crawl_result_obj in self.crawler.crawl_recursive(url, max_depth, max_pages):
            chunks_i = await self._process_and_ingest_crawled_doc(crawl_result_obj, chunker_instance)
            total_chunks_ingested += chunks_i
            if crawl_result_obj.success: pages_processed_count += 1
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

    async def _crawl_sitemap_urls(self, sitemap_url_or_urls, chunker_instance: HierarchicalChunker) -> ToolResponse:
        # Handle both sitemap URL string and list of URLs
        if isinstance(sitemap_url_or_urls, str):
            await self._emit_crawl_event("crawl_sitemap", "starting", {"sitemap_url": sitemap_url_or_urls})
            url_count_estimate = "unknown"
        else:
            await self._emit_crawl_event("crawl_sitemap", "starting", {"url_count": len(sitemap_url_or_urls)})
            url_count_estimate = len(sitemap_url_or_urls)

        total_chunks_ingested = 0
        pages_processed_count = 0

        async for crawl_result_obj in self.crawler.crawl_sitemap_urls(sitemap_url_or_urls):
            chunks_i = await self._process_and_ingest_crawled_doc(crawl_result_obj, chunker_instance)
            total_chunks_ingested += chunks_i
            if crawl_result_obj.success: pages_processed_count += 1
            if isinstance(sitemap_url_or_urls, list) and pages_processed_count % 5 == 0:
                 await self._emit_crawl_event("crawl_sitemap", "progress", {
                    "processed_urls": pages_processed_count, "total_urls_in_list": len(sitemap_url_or_urls),
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

    async def _crawl_markdown_file_url(self, url: str, chunker_instance: HierarchicalChunker) -> ToolResponse:
        await self._emit_crawl_event("crawl_markdown_file_url", "starting", {"url": url})
        total_chunks_ingested = 0

        async for crawl_result_obj in self.crawler.crawl_markdown_file_url(url): # Expects an async generator
            chunks_i = await self._process_and_ingest_crawled_doc(crawl_result_obj, chunker_instance)
            total_chunks_ingested += chunks_i

        summary = f"Markdown file crawl completed for {url}. Ingested {total_chunks_ingested} chunks."
        await self._emit_crawl_event("crawl_markdown_file_url", "completed", {
            "url": url, "total_chunks_ingested": total_chunks_ingested
        })
        return ToolResponse(
            success=True,
            data={"url": url, "total_chunks_ingested": total_chunks_ingested},
            message=summary
        )



    async def _discover_sitemap(self, url: str) -> ToolResponse:
        """Discover sitemap URLs for a website."""
        await self._emit_crawl_event("discover_sitemap", "starting", {"url": url})

        try:
            # Use basic sitemap discovery logic
            from urllib.parse import urlparse
            parsed_base = urlparse(url)
            base_domain = f"{parsed_base.scheme}://{parsed_base.netloc}"

            # Common sitemap locations
            sitemap_candidates = [
                f"{base_domain}/sitemap.xml",
                f"{base_domain}/sitemap_index.xml",
                f"{base_domain}/sitemaps.xml"
            ]

            summary = f"Sitemap discovery completed for {url}. Found {len(sitemap_candidates)} candidate URLs."
            await self._emit_crawl_event("discover_sitemap", "completed", {
                "url": url, "sitemap_urls_found": len(sitemap_candidates)
            })

            return ToolResponse(
                success=True,
                data={"url": url, "sitemap_urls": sitemap_candidates, "count": len(sitemap_candidates)},
                message=summary
            )
        except Exception as e:
            error_msg = f"Sitemap discovery failed for {url}: {str(e)}"
            await self._emit_crawl_event("discover_sitemap", "error", {"url": url, "error": str(e)})
            return ToolResponse(
                success=False,
                error=str(e),
                message=error_msg
            )

    async def _analyze_site(self, url: str) -> ToolResponse:
        """Analyze a website structure and provide crawling recommendations."""
        await self._emit_crawl_event("analyze_site", "starting", {"url": url})

        try:
            # Crawl the main page to analyze structure
            analysis_data = {
                "url": url,
                "sitemap_urls": [],
                "internal_links": [],
                "external_links": [],
                "content_quality": 0.0,
                "recommendations": []
            }

            # Basic sitemap discovery
            from urllib.parse import urlparse
            parsed_base = urlparse(url)
            base_domain = f"{parsed_base.scheme}://{parsed_base.netloc}"
            sitemap_candidates = [f"{base_domain}/sitemap.xml"]
            analysis_data["sitemap_urls"] = sitemap_candidates

            # Analyze main page using markdown file crawler as a single URL crawler
            async for raw_doc_data in self.crawler.crawl_markdown_file_url(url):
                processed_doc = await self.processor.process_document(raw_doc_data)
                analysis_data["content_quality"] = processed_doc.get("quality_score", 0.0)

                # Extract links from WebCrawlerResult
                if hasattr(raw_doc_data, 'links'):
                    links = raw_doc_data.links
                    analysis_data["internal_links"] = links.get("internal", [])
                    analysis_data["external_links"] = links.get("external", [])

                # Generate recommendations
                recommendations = []
                recommendations.append("Check sitemap.xml for comprehensive crawling")
                if len(analysis_data["internal_links"]) > 10:
                    recommendations.append("Site has many internal links - recommend recursive crawling with depth 2-3")
                if analysis_data["content_quality"] > 0.7:
                    recommendations.append("High quality content detected - good candidate for knowledge base")
                if analysis_data["content_quality"] < 0.3:
                    recommendations.append("Low quality content - may need content filtering")

                analysis_data["recommendations"] = recommendations

            summary = f"Site analysis completed for {url}. Quality score: {analysis_data['content_quality']:.2f}"
            await self._emit_crawl_event("analyze_site", "completed", {
                "url": url, "quality_score": analysis_data["content_quality"]
            })

            return ToolResponse(
                success=True,
                data=analysis_data,
                message=summary
            )
        except Exception as e:
            error_msg = f"Site analysis failed for {url}: {str(e)}"
            await self._emit_crawl_event("analyze_site", "error", {"url": url, "error": str(e)})
            return ToolResponse(
                success=False,
                error=str(e),
                message=error_msg
            )