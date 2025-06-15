# python/agents/web_crawler/processors.py
import re
import hashlib
from typing import Dict, Any, List
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

# Import crawl4ai components for enhanced markdown generation
try:
    from crawl4ai import WebCrawlerResult
    from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator, MarkdownGeneratorConfig
    CRAWL4AI_AVAILABLE = True
except ImportError:
    CRAWL4AI_AVAILABLE = False
    # Fallback classes if crawl4ai is not installed
    class WebCrawlerResult: # type: ignore
        def __init__(self, url, success, markdown=None, html=None, links=None, error_message=None, title=None):
            self.url = url; self.success = success; self.markdown = markdown
            self.html_content = html; self.links = links or {}; self.error_message = error_message; self.title = title
    class DefaultMarkdownGenerator: # type: ignore
        def __init__(self, *args, **kwargs): pass
        async def generate(self, html_content, url): return html_content # Passthrough

# Import BeautifulSoup for additional HTML processing if needed
try:
    from bs4 import BeautifulSoup
    BS4_AVAILABLE = True
except ImportError:
    BS4_AVAILABLE = False

class DocumentProcessor:
    """
    Enhanced document processor for converting raw crawled content into clean, structured markdown.
    Features: Content cleaning, metadata extraction, quality validation, and format standardization.
    Now with crawl4ai DefaultMarkdownGenerator integration for superior HTML-to-Markdown conversion.
    """
    def __init__(self):
        self.min_content_length = 50
        self.max_content_length = 1000000  # 1MB limit

        if CRAWL4AI_AVAILABLE:
            # Configure the markdown generator. DefaultMarkdownGenerator has its own defaults.
            # We can customize it if needed, e.g., by passing a MarkdownGeneratorConfig.
            # config = MarkdownGeneratorConfig(use_advanced_processing=True, custom_rules=...)
            self.markdown_generator = DefaultMarkdownGenerator()
            logger.info("DocumentProcessor: Initialized with Crawl4AI's DefaultMarkdownGenerator.")
        else:
            self.markdown_generator = DefaultMarkdownGenerator() # Uses the fallback passthrough
            logger.warning("DocumentProcessor: Crawl4AI not found, using basic passthrough for markdown generation.")

        logger.info("DocumentProcessor: Enhanced processor initialized with crawl4ai markdown generation.")

    async def process_document(self, crawl_result: WebCrawlerResult) -> Dict[str, Any]:
        """
        Processes a WebCrawlerResult object. If it contains HTML content,
        it's converted to Markdown using Crawl4AI's generator.
        If it already contains markdown (e.g., from a .md or .txt file crawl),
        that markdown is used directly.
        """
        url = crawl_result.url
        # Try to get title from crawl_result, otherwise fallback
        doc_title = crawl_result.title
        if not doc_title: # Try to derive from URL if not present
            try:
                doc_title = url.split('/')[-1] if url.split('/')[-1] else url.split('/')[-2] if len(url.split('/')) > 1 else "Untitled Document"
            except:
                doc_title = "Untitled Document"

        logger.info(f"DocumentProcessor: Processing document from {url}, Title: {doc_title}")

        if not crawl_result.success:
            logger.warning(f"DocumentProcessor: Crawl failed for {url}. Error: {crawl_result.error_message}")
            return {
                "url": url, "title": doc_title, "markdown": "",
                "metadata": {"original_url": url, "crawl_error": crawl_result.error_message or "Crawl failed"}
            }

        markdown_content = ""
        # Crawl4AI's WebCrawlerResult has a `markdown` attribute which is a `MarkdownObject`
        # and `html_content` attribute.
        # If `result.markdown` is already populated by crawl4ai (e.g. from a .md file), use it.
        # Otherwise, if `html_content` is present, generate markdown from it.

        if crawl_result.markdown: # This is MarkdownObject from crawl4ai
            if isinstance(crawl_result.markdown, str): # If it's already a string (e.g. from fallback)
                markdown_content = crawl_result.markdown
            elif hasattr(crawl_result.markdown, 'raw_markdown'): # Accessing raw_markdown from MarkdownObject
                markdown_content = crawl_result.markdown.raw_markdown
            else: # Fallback if it's an unexpected type
                markdown_content = str(crawl_result.markdown)
            logger.debug(f"DocumentProcessor: Using pre-existing markdown for {url}. Length: {len(markdown_content)}")
        elif crawl_result.html_content:
            logger.debug(f"DocumentProcessor: Generating markdown from HTML for {url}. HTML length: {len(crawl_result.html_content)}")
            try:
                # The generate method of markdown_generator is async
                markdown_object = await self.markdown_generator.generate(
                    html_content=crawl_result.html_content,
                    url=url
                )
                markdown_content = markdown_object.raw_markdown if markdown_object else ""
                logger.info(f"DocumentProcessor: Successfully generated markdown from HTML for {url}. Length: {len(markdown_content)}")
            except Exception as e:
                logger.error(f"DocumentProcessor: Failed to generate markdown from HTML for {url}: {e}", exc_info=True)
                markdown_content = f"Error generating markdown from HTML: {str(e)}\n\nRaw HTML content (first 1000 chars):\n{crawl_result.html_content[:1000]}"
        else:
            logger.warning(f"DocumentProcessor: No markdown or HTML content found for {url}.")
            markdown_content = "" # Ensure it's an empty string

        # Basic check for empty or placeholder content
        if not markdown_content.strip() or markdown_content.startswith("Error generating markdown") or len(markdown_content) < 50 : # Arbitrary small length
            logger.warning(f"DocumentProcessor: Markdown content for {url} is empty or seems invalid after processing.")
            # Optionally, could try to extract text using a simpler method as a last resort if markdown_content is poor.
            # For now, we proceed with what we have or an empty string.

        # Validate content length
        if len(markdown_content) < self.min_content_length:
            logger.warning(f"DocumentProcessor: Content too short for {url} ({len(markdown_content)} chars)")
            return self._create_error_result(url, "Content too short", {"url": url, "title": doc_title})

        if len(markdown_content) > self.max_content_length:
            logger.warning(f"DocumentProcessor: Content too long for {url}, truncating")
            markdown_content = markdown_content[:self.max_content_length] + "\n\n[Content truncated...]"

        # Clean and process content further
        processed_content = await self._clean_content(markdown_content, url)

        # Extract enhanced metadata from crawl_result
        metadata = self._extract_metadata_from_crawl_result(crawl_result, processed_content)

        # Generate content hash for deduplication
        content_hash = hashlib.md5(processed_content.encode()).hexdigest()

        # Validate content quality
        quality_score = self._assess_content_quality(processed_content)

        return {
            "url": url,
            "title": self._clean_title(doc_title),
            "markdown": processed_content,
            "metadata": metadata,
            "content_hash": content_hash,
            "quality_score": quality_score,
            "processed_at": datetime.utcnow().isoformat(),
            "word_count": len(processed_content.split()),
            "char_count": len(processed_content)
        }

    async def _clean_content(self, content: str, url: str) -> str:
        """Clean and normalize content."""
        # Remove excessive whitespace
        content = re.sub(r'\n\s*\n\s*\n', '\n\n', content)
        content = re.sub(r'[ \t]+', ' ', content)

        # Remove common navigation/footer text patterns
        patterns_to_remove = [
            r'(?i)cookie\s+policy.*?(?=\n|$)',
            r'(?i)privacy\s+policy.*?(?=\n|$)',
            r'(?i)terms\s+of\s+service.*?(?=\n|$)',
            r'(?i)©\s*\d{4}.*?(?=\n|$)',
            r'(?i)all\s+rights\s+reserved.*?(?=\n|$)',
        ]

        for pattern in patterns_to_remove:
            content = re.sub(pattern, '', content)

        # Ensure proper markdown formatting
        if not content.startswith('#'):
            # Extract title from URL if content doesn't start with a header
            url_title = url.split('/')[-1].replace('-', ' ').replace('_', ' ').title()
            if url_title and url_title != url:
                content = f"# {url_title}\n\n{content}"

        # Clean up markdown formatting
        content = self._normalize_markdown(content)

        return content.strip()

    def _normalize_markdown(self, content: str) -> str:
        """Normalize markdown formatting."""
        # Fix heading spacing
        content = re.sub(r'^(#{1,6})\s*(.+)$', r'\1 \2', content, flags=re.MULTILINE)

        # Fix list formatting
        content = re.sub(r'^(\s*)[-*+]\s+', r'\1- ', content, flags=re.MULTILINE)

        # Fix link formatting
        content = re.sub(r'\[([^\]]+)\]\s*\(\s*([^)]+)\s*\)', r'[\1](\2)', content)

        # Remove excessive blank lines
        content = re.sub(r'\n{3,}', '\n\n', content)

        return content

    def _clean_title(self, title: str) -> str:
        """Clean and normalize document title."""
        if not title or title == "Untitled":
            return "Untitled Document"

        # Remove common title suffixes
        title = re.sub(r'\s*[-|]\s*.*$', '', title)

        # Clean up whitespace
        title = re.sub(r'\s+', ' ', title).strip()

        # Limit title length
        if len(title) > 100:
            title = title[:97] + "..."

        return title

    def _extract_metadata(self, raw_doc_data: Dict[str, Any], processed_content: str) -> Dict[str, Any]:
        """Extract enhanced metadata from document."""
        metadata = {
            "original_url": raw_doc_data.get("url"),
            "crawl_depth": raw_doc_data.get("depth", 0),
            "source": raw_doc_data.get("source", "unknown"),
            "status_code": raw_doc_data.get("status_code"),
            "content_type": raw_doc_data.get("content_type", "html"),
            "links_found": len(raw_doc_data.get("links", {}).get("internal", [])),
            "external_links": len(raw_doc_data.get("links", {}).get("external", [])),
        }

        # Extract language hints
        if self._detect_language_patterns(processed_content):
            metadata["language_hints"] = self._detect_language_patterns(processed_content)

        # Extract content structure info
        headers = re.findall(r'^(#{1,6})\s+(.+)$', processed_content, re.MULTILINE)
        if headers:
            metadata["header_count"] = len(headers)
            metadata["max_header_level"] = max(len(h[0]) for h in headers)

        # Extract code blocks
        code_blocks = re.findall(r'```[\s\S]*?```', processed_content)
        if code_blocks:
            metadata["code_blocks"] = len(code_blocks)

        return metadata

    def _extract_metadata_from_crawl_result(self, crawl_result: WebCrawlerResult, processed_content: str) -> Dict[str, Any]:
        """Extract enhanced metadata from WebCrawlerResult object."""
        metadata = {
            "original_url": crawl_result.url,
            "crawl_depth": getattr(crawl_result, 'depth', 0), # Depth might not be on all results
            "content_type": "text/markdown", # Indicate processed content type
            "success": crawl_result.success,
            "links_found": len(getattr(crawl_result, 'links', {}).get("internal", [])),
            "external_links": len(getattr(crawl_result, 'links', {}).get("external", [])),
        }

        if hasattr(crawl_result, 'status_code'):
            metadata["status_code"] = crawl_result.status_code

        # Extract language hints
        if self._detect_language_patterns(processed_content):
            metadata["language_hints"] = self._detect_language_patterns(processed_content)

        # Extract content structure info
        headers = re.findall(r'^(#{1,6})\s+(.+)$', processed_content, re.MULTILINE)
        if headers:
            metadata["header_count"] = len(headers)
            metadata["max_header_level"] = max(len(h[0]) for h in headers)

        # Extract code blocks
        code_blocks = re.findall(r'```[\s\S]*?```', processed_content)
        if code_blocks:
            metadata["code_blocks"] = len(code_blocks)

        return metadata

    def _detect_language_patterns(self, content: str) -> List[str]:
        """Detect programming languages or content types in the document."""
        patterns = {
            "python": [r'def\s+\w+\(', r'import\s+\w+', r'from\s+\w+\s+import'],
            "javascript": [r'function\s+\w+\(', r'const\s+\w+\s*=', r'\.addEventListener\('],
            "html": [r'<[^>]+>', r'<!DOCTYPE', r'<html'],
            "css": [r'\{[^}]*\}', r'@media', r'\.[\w-]+\s*\{'],
            "sql": [r'SELECT\s+', r'FROM\s+', r'WHERE\s+'],
            "json": [r'\{[^}]*"[^"]+"\s*:', r'\[[^]]*\]'],
        }

        detected = []
        content_lower = content.lower()

        for lang, lang_patterns in patterns.items():
            if any(re.search(pattern, content_lower) for pattern in lang_patterns):
                detected.append(lang)

        return detected

    def _assess_content_quality(self, content: str) -> float:
        """Assess content quality on a scale of 0-1."""
        score = 0.0

        # Length score (optimal around 500-2000 words)
        word_count = len(content.split())
        if 100 <= word_count <= 5000:
            score += 0.3
        elif word_count > 50:
            score += 0.1

        # Structure score (headers, lists, etc.)
        if re.search(r'^#{1,6}\s+', content, re.MULTILINE):
            score += 0.2
        if re.search(r'^\s*[-*+]\s+', content, re.MULTILINE):
            score += 0.1

        # Content diversity score
        unique_words = len(set(content.lower().split()))
        total_words = len(content.split())
        if total_words > 0:
            diversity = unique_words / total_words
            score += min(diversity * 0.4, 0.4)

        return min(score, 1.0)

    def _create_error_result(self, url: str, error: str, raw_doc_data: Dict[str, Any]) -> Dict[str, Any]:
        """Create error result for failed processing."""
        return {
            "url": url,
            "title": "Processing Error",
            "markdown": f"# Processing Error\n\nFailed to process document: {error}",
            "metadata": {
                "original_url": url,
                "error": error,
                "crawl_depth": raw_doc_data.get("depth", 0)
            },
            "content_hash": hashlib.md5(error.encode()).hexdigest(),
            "quality_score": 0.0,
            "processed_at": datetime.utcnow().isoformat(),
            "word_count": 0,
            "char_count": 0
        }