# python/agents/web_crawler/crawler.py
import asyncio
from typing import List, Dict, Any, AsyncGenerator

class DocumentCrawler:
    """
    Manages document crawling (mocked for now).
    In a real implementation, this would use Crawl4AI or similar.
    """
    def __init__(self):
        print("DocumentCrawler (Mock) initialized.")

    async def crawl_recursive(self, url: str, max_depth: int, max_pages: int) -> AsyncGenerator[Dict[str, Any], None]:
        """Simulates recursive crawling."""
        print(f"DocumentCrawler (Mock): Starting recursive crawl for URL: {url}, depth: {max_depth}, max_pages: {max_pages}")
        for i in range(min(5, max_pages)):  # Simulate finding a few pages
            await asyncio.sleep(0.1)
            page_url = f"{url}/page{i+1}"
            yield {
                "url": page_url,
                "raw_content": f"Mock content for {page_url}. Depth {min(i//2 + 1, max_depth)}",  # Simulate some content
                "title": f"Mock Title for Page {i+1}",
                "depth": min(i//2 + 1, max_depth),
                "links": {"internal": [f"{url}/page{i+2}"], "external": []} if i < 4 else {"internal": [], "external": []}
            }
        print(f"DocumentCrawler (Mock): Finished recursive crawl for URL: {url}")

    async def crawl_sitemap_urls(self, urls: List[str]) -> AsyncGenerator[Dict[str, Any], None]:
        """Simulates crawling a list of URLs from a sitemap."""
        print(f"DocumentCrawler (Mock): Starting sitemap crawl for {len(urls)} URLs.")
        for i, url in enumerate(urls):
            if i >= 10:  # Limit mock processing
                print("DocumentCrawler (Mock): Sitemap crawl limit reached.")
                break
            await asyncio.sleep(0.1)
            yield {
                "url": url,
                "raw_content": f"Mock sitemap content for {url}.",
                "title": f"Mock Sitemap Title for {url.split('/')[-1] or url}",
            }
        print(f"DocumentCrawler (Mock): Finished sitemap crawl.")

    async def crawl_markdown_file_url(self, url: str) -> AsyncGenerator[Dict[str, Any], None]:
        """Simulates crawling a single markdown/txt file URL."""
        print(f"DocumentCrawler (Mock): Starting markdown file crawl for URL: {url}")
        await asyncio.sleep(0.1)
        yield {
            "url": url,
            "raw_content": f"# Mock Markdown Content for {url}\n\nThis is some mock markdown text.",
            "title": f"Mock Markdown Document: {url.split('/')[-1]}",
        }
        print(f"DocumentCrawler (Mock): Finished markdown file crawl for URL: {url}")