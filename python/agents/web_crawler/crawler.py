# python/agents/web_crawler/crawler.py
import asyncio
from typing import List, AsyncGenerator, Optional, Set, Tuple, Union
from urllib.parse import urlparse, urldefrag, urljoin
from xml.etree import ElementTree
import requests # For synchronous sitemap parsing
import httpx # For async sitemap fetching
import logging

logger = logging.getLogger(__name__)

try:
    from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode, WebCrawlerResult, MemoryAdaptiveDispatcher
    from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator # For HTML to Markdown
    CRAWL4AI_AVAILABLE = True
except ImportError:
    logger.warning("WebCrawlerTool: crawl4ai library not found. Crawler will be severely limited.")
    CRAWL4AI_AVAILABLE = False
    # Define placeholder classes if crawl4ai is not available
    class WebCrawlerResult: # type: ignore
        def __init__(self, url, success, markdown=None, html=None, links=None, error_message=None, title=None):
            self.url = url; self.success = success; self.markdown = markdown
            self.html_content = html; self.links = links or {}; self.error_message = error_message; self.title = title
    class DefaultMarkdownGenerator: # type: ignore
        async def generate(self, html_content, url): return html_content # Fallback
    class MemoryAdaptiveDispatcher: # type: ignore
        def __init__(self, *args, **kwargs): pass

class DocumentCrawler:
    """
    Manages document crawling using Crawl4AI.
    """
    def __init__(self, max_concurrent_crawlers: int = 5, headless_browser: bool = True):
        self.max_concurrent_crawlers = max_concurrent_crawlers # For dispatcher if used with arun_many
        self.headless_browser = headless_browser
        self._crawler_instance: Optional[AsyncWebCrawler] = None
        self._crawler_lock = asyncio.Lock()

        if CRAWL4AI_AVAILABLE:
            self.browser_config = BrowserConfig(
                headless=self.headless_browser,
                verbose=False,
                playwright_extra_args=["--disable-gpu", "--disable-dev-shm-usage", "--no-sandbox"],
            )
            self.run_config = CrawlerRunConfig(
                cache_mode=CacheMode.BYPASS, # Consider CacheMode.USE_CACHE for repeated runs
                markdown_generator=DefaultMarkdownGenerator(), # Use crawl4ai's markdown generator
                # Example: extract specific elements
                # target_elements=[{"tag": "article"}, {"tag": "main"}, {"role": "main"}]
            )
            logger.info("DocumentCrawler: Initialized with real Crawl4AI.")
        else:
            logger.warning("DocumentCrawler: WARNING - Crawl4AI not found. Using basic HTTP fetching.")

    async def get_crawler(self) -> AsyncWebCrawler:
        async with self._crawler_lock:
            if not CRAWL4AI_AVAILABLE:
                raise RuntimeError("Crawl4AI library is not available. Cannot perform crawl operations.")
            if self._crawler_instance is None:
                self._crawler_instance = AsyncWebCrawler(config=self.browser_config)
                await self._crawler_instance.start() # Start browser
            return self._crawler_instance

    async def close_crawler(self):
        async with self._crawler_lock:
            if self._crawler_instance:
                await self._crawler_instance.close()
                self._crawler_instance = None
            logger.info("DocumentCrawler: Crawl4AI instance closed.")

    async def _parse_sitemap_xml_content(self, xml_content: str, sitemap_url_base: str) -> Tuple[List[str], List[str]]:
        """Parses XML content of a sitemap, returns URLs and sub-sitemap URLs."""
        urls: List[str] = []
        sub_sitemaps: List[str] = []
        try:
            root = ElementTree.fromstring(xml_content)
            # Common namespace for sitemaps
            namespace = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}

            # Check for sitemapindex (pointing to other sitemaps)
            for sitemap_loc_element in root.findall('.//ns:sitemap/ns:loc', namespace):
                if sitemap_loc_element.text:
                    sub_sitemaps.append(urljoin(sitemap_url_base, sitemap_loc_element.text.strip()))

            # Extract regular URLs
            for url_loc_element in root.findall('.//ns:url/ns:loc', namespace):
                if url_loc_element.text:
                    urls.append(urljoin(sitemap_url_base, url_loc_element.text.strip()))
        except ElementTree.ParseError as e:
            logger.error(f"DocumentCrawler: XML ParseError for sitemap content from {sitemap_url_base}: {e}")
        except Exception as e:
            logger.error(f"DocumentCrawler: Unexpected error parsing sitemap content from {sitemap_url_base}: {e}")
        return urls, sub_sitemaps

    async def _fetch_and_parse_sitemap(self, sitemap_url: str, visited_sitemaps: Set[str], client: httpx.AsyncClient) -> Tuple[List[str], List[str]]:
        """Fetches a single sitemap URL and parses it, handling recursion for sitemap indexes."""
        if sitemap_url in visited_sitemaps:
            return [], []
        visited_sitemaps.add(sitemap_url)

        logger.info(f"DocumentCrawler: Fetching sitemap: {sitemap_url}")
        try:
            # Using httpx for async fetching of sitemap XML
            response = await client.get(sitemap_url, timeout=20.0, follow_redirects=True)
            response.raise_for_status()
            return await self._parse_sitemap_xml_content(response.text, sitemap_url)
        except httpx.RequestError as e:
            logger.error(f"DocumentCrawler: HTTP RequestError fetching sitemap {sitemap_url}: {e}")
        except httpx.HTTPStatusError as e:
             logger.error(f"DocumentCrawler: HTTP StatusError fetching sitemap {sitemap_url}: {e.response.status_code}")
        except Exception as e:
            logger.error(f"DocumentCrawler: Generic error fetching/parsing sitemap {sitemap_url}: {e}")
        return [], []

    async def get_all_urls_from_sitemap_source(self, sitemap_source: str) -> List[str]:
        """
        Recursively fetches and parses a sitemap (or sitemap index) to get all unique page URLs.
        """
        all_page_urls: Set[str] = set()
        sitemaps_to_process: asyncio.Queue[str] = asyncio.Queue()
        await sitemaps_to_process.put(sitemap_source)
        visited_sitemaps: Set[str] = set()

        async with httpx.AsyncClient() as client:
            processing_tasks = []
            # Limit concurrent sitemap fetching/parsing to avoid overwhelming the target server
            max_concurrent_sitemap_fetches = 5

            while True:
                current_batch_to_fetch = []
                while not sitemaps_to_process.empty() and len(current_batch_to_fetch) < max_concurrent_sitemap_fetches:
                    s_url = await sitemaps_to_process.get()
                    if s_url not in visited_sitemaps:
                         current_batch_to_fetch.append(s_url)
                    sitemaps_to_process.task_done() # Mark item as processed from queue immediately

                for s_url in current_batch_to_fetch:
                     if s_url not in visited_sitemaps: # Double check, helpful with concurrency
                        task = asyncio.create_task(self._fetch_and_parse_sitemap(s_url, visited_sitemaps, client))
                        processing_tasks.append(task)

                if not processing_tasks and sitemaps_to_process.empty(): # No more tasks to create or process
                    break

                if processing_tasks:
                    done, pending = await asyncio.wait(processing_tasks, return_when=asyncio.FIRST_COMPLETED)
                    processing_tasks = list(pending) # Update task list

                    for task in done:
                        try:
                            page_urls, sub_sitemaps = await task
                            for p_url in page_urls: all_page_urls.add(p_url)
                            for sub_s in sub_sitemaps:
                                if sub_s not in visited_sitemaps: # Add to queue only if not yet visited
                                    await sitemaps_to_process.put(sub_s)
                        except Exception as e:
                            logger.error(f"DocumentCrawler: Error processing a sitemap task result: {e}")

        logger.info(f"DocumentCrawler: Extracted {len(all_page_urls)} unique page URLs from sitemap source: {sitemap_source}")
        return list(all_page_urls)

    async def _fetch_single_url(self, url: str) -> WebCrawlerResult:
        """Fetches content from a single URL using an existing or new Crawl4AI instance."""
        crawler = await self.get_crawler()
        try:
            logger.info(f"DocumentCrawler: Fetching URL with Crawl4AI: {url}")
            # Use a specific session_id per URL to ensure isolation if arun is used sequentially
            # Or rely on arun_many's internal session management.
            # For single fetch, let's use a unique session or default.
            result = await crawler.arun(url=url, config=self.run_config, session_id=f"session_{hash(url)}")
            return result
        except Exception as e:
            logger.error(f"DocumentCrawler: Error fetching {url} with Crawl4AI: {e}")
            return WebCrawlerResult(url=url, success=False, error_message=str(e), title=url)

    async def crawl_recursive(self, start_url: str, max_depth: int, max_pages: int) -> AsyncGenerator[WebCrawlerResult, None]:
        """Recursively crawls a website using Crawl4AI."""
        logger.info(f"DocumentCrawler: Starting recursive crawl: URL={start_url}, Depth={max_depth}, MaxPages={max_pages}")
        crawler = await self.get_crawler()

        # Configure for recursive crawl (Crawl4AI handles recursion internally via arun)
        recursive_run_config = CrawlerRunConfig(
            cache_mode=self.run_config.cache_mode,
            markdown_generator=self.run_config.markdown_generator,
            max_pages_per_domain=max_pages,
            max_depth=max_depth,
            extract_hidden_links=False # Optional: depending on needs
        )

        try:
            # Crawl4AI's arun with max_depth handles recursion.
            # It doesn't directly yield per page in the same way as manual recursion.
            # It returns a single WebCrawlerResult for the entry URL, with 'child_pages_results'
            # if include_child_pages=True (default for recursive).
            # Or, we can manage recursion manually to yield page by page.
            # For yielding per page as in previous mock:

            visited_urls = set()
            queue = asyncio.Queue()

            start_url_norm = urldefrag(start_url)[0]
            await queue.put((start_url_norm, 0))
            visited_urls.add(start_url_norm)
            pages_crawled_count = 0

            while not queue.empty() and pages_crawled_count < max_pages:
                current_url_to_crawl, current_depth = await queue.get()

                if current_depth > max_depth:
                    continue

                logger.info(f"DocumentCrawler: Crawling (Rec): {current_url_to_crawl} at depth {current_depth}")
                # Use crawler.arun for each page to get its links for manual recursion
                # This is less efficient than letting crawl4ai handle recursion if we only need final results
                page_result: WebCrawlerResult = await crawler.arun(url=current_url_to_crawl, config=recursive_run_config, session_id=f"rec_session_{hash(current_url_to_crawl)}")
                pages_crawled_count += 1

                if page_result.success:
                    yield page_result # Yield the WebCrawlerResult object directly

                    if current_depth < max_depth:
                        for link_info in page_result.links.get("internal", []):
                            next_url = link_info.get("href")
                            if next_url:
                                next_url_norm = urldefrag(next_url)[0]
                                # Basic check to stay on the same domain
                                if urlparse(next_url_norm).netloc == urlparse(start_url_norm).netloc and next_url_norm not in visited_urls:
                                    visited_urls.add(next_url_norm)
                                    if len(visited_urls) <= max_pages * (max_depth +1): # Safety limit for queue size
                                        await queue.put((next_url, current_depth + 1))
                else:
                    logger.warning(f"DocumentCrawler: Failed to fetch (Rec): {current_url_to_crawl} - {page_result.error_message}")

                if pages_crawled_count >= max_pages:
                    logger.info(f"DocumentCrawler: Max pages ({max_pages}) reached.")
                    break
        finally:
            await self.close_crawler()

    async def crawl_sitemap_urls(self, sitemap_url_or_list: Union[str, List[str]]) -> AsyncGenerator[WebCrawlerResult, None]:
        """Crawls URLs from a provided list or extracted from a sitemap URL."""
        urls_to_crawl: List[str]
        if isinstance(sitemap_url_or_list, str): # It's a sitemap URL
            urls_to_crawl = await self.get_all_urls_from_sitemap_source(sitemap_url_or_list)
        elif isinstance(sitemap_url_or_list, list):
            urls_to_crawl = sitemap_url_or_list
        else:
            err_msg = "sitemap_url_or_list must be a sitemap URL string or a list of URLs"
            logger.error(f"DocumentCrawler: {err_msg}")
            # Yield a single error result
            yield WebCrawlerResult(url=str(sitemap_url_or_list), success=False, error_message=err_msg, title="Invalid Sitemap Source")
            return

        if not urls_to_crawl:
            logger.info("DocumentCrawler: No URLs to crawl from sitemap/list.")
            return

        logger.info(f"DocumentCrawler: Starting batch crawl of {len(urls_to_crawl)} URLs.")
        crawler = await self.get_crawler()
        dispatcher = MemoryAdaptiveDispatcher(
            max_session_permit=self.max_concurrent_crawlers,
            memory_threshold_percent=75.0, # Example threshold
            check_interval=1.0
        )
        try:
            results_stream = crawler.arun_many( # arun_many returns an async generator
                urls=list(set(urls_to_crawl)), # Crawl unique URLs
                config=self.run_config,
                dispatcher=dispatcher
            )
            async for result in results_stream:
                yield result
        except Exception as e:
            logger.error(f"DocumentCrawler: Error during arun_many for sitemap URLs: {e}", exc_info=True)
            # Yield error results for remaining URLs or a general error?
            # For now, just log and let it end. Individual errors are in result objects.
        finally:
            await self.close_crawler()

    async def crawl_markdown_file_url(self, url: str) -> AsyncGenerator[WebCrawlerResult, None]:
        """Crawls a single markdown/text file URL using Crawl4AI."""
        logger.info(f"DocumentCrawler: Crawling markdown/text file URL: {url}")
        # Crawl4AI should handle .txt/.md directly if the server serves them as text/markdown
        # Its DefaultMarkdownGenerator might just pass through the content.
        try:
            result = await self._fetch_single_url(url)
            yield result
        finally:
            await self.close_crawler()