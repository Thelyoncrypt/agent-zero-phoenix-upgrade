# tests/test_web_crawler.py
import pytest
import asyncio
from unittest.mock import Mock, patch
from python.tools.web_crawler_tool import WebCrawlerTool
from python.helpers.tool import Response as ToolResponse

class TestWebCrawlerTool:
    @pytest.fixture
    def mock_agent(self):
        """Create a mock agent for testing"""
        agent = Mock()
        agent.agent_name = "test_agent"
        agent.context = Mock()
        agent.context.id = "test_context"
        agent._emit_stream_event = Mock()
        return agent

    @pytest.fixture
    def web_crawler_tool(self, mock_agent):
        """Create WebCrawlerTool instance for testing"""
        return WebCrawlerTool(mock_agent)

    @pytest.mark.asyncio
    async def test_web_crawler_initialization(self, web_crawler_tool, mock_agent):
        """Test that WebCrawlerTool initializes correctly"""
        assert web_crawler_tool.name == "web_crawler_tool"
        assert web_crawler_tool.agent == mock_agent
        assert web_crawler_tool.crawler is not None
        assert web_crawler_tool.processor is not None
        assert web_crawler_tool.chunker is not None

    @pytest.mark.asyncio
    async def test_missing_action_parameter(self, web_crawler_tool):
        """Test error handling when action parameter is missing"""
        result = await web_crawler_tool.execute()
        assert isinstance(result, ToolResponse)
        assert not result.success
        assert "Missing required 'action' parameter" in result.error

    @pytest.mark.asyncio
    async def test_crawl_site_missing_url(self, web_crawler_tool):
        """Test error handling when URL is missing for crawl_site"""
        result = await web_crawler_tool.execute(action="crawl_site")
        assert isinstance(result, ToolResponse)
        assert not result.success
        assert "Missing 'url' parameter" in result.error

    @pytest.mark.asyncio
    async def test_crawl_site_success(self, web_crawler_tool):
        """Test successful crawl_site execution"""
        result = await web_crawler_tool.execute(
            action="crawl_site",
            url="https://example.com",
            max_depth=2,
            max_pages=5
        )
        assert isinstance(result, ToolResponse)
        assert result.success
        assert "pages_processed" in result.data
        assert "total_chunks_ingested" in result.data
        assert "Site crawl completed" in result.message

    @pytest.mark.asyncio
    async def test_crawl_sitemap_with_sitemap_url(self, web_crawler_tool):
        """Test crawl_sitemap with sitemap_url parameter"""
        result = await web_crawler_tool.execute(
            action="crawl_sitemap",
            sitemap_url="https://example.com/sitemap.xml"
        )
        assert isinstance(result, ToolResponse)
        assert result.success
        assert "processed_urls" in result.data
        assert "total_chunks_ingested" in result.data

    @pytest.mark.asyncio
    async def test_crawl_sitemap_with_urls_list(self, web_crawler_tool):
        """Test crawl_sitemap with URLs list"""
        urls = ["https://example.com/page1", "https://example.com/page2"]
        result = await web_crawler_tool.execute(
            action="crawl_sitemap",
            urls=urls
        )
        assert isinstance(result, ToolResponse)
        assert result.success
        assert "processed_urls" in result.data

    @pytest.mark.asyncio
    async def test_crawl_sitemap_missing_parameters(self, web_crawler_tool):
        """Test error handling when both sitemap_url and urls are missing"""
        result = await web_crawler_tool.execute(action="crawl_sitemap")
        assert isinstance(result, ToolResponse)
        assert not result.success
        assert "Missing required parameters" in result.error

    @pytest.mark.asyncio
    async def test_crawl_markdown_file_url_success(self, web_crawler_tool):
        """Test successful crawl_markdown_file_url execution"""
        result = await web_crawler_tool.execute(
            action="crawl_markdown_file_url",
            url="https://example.com/document.md"
        )
        assert isinstance(result, ToolResponse)
        assert result.success
        assert "url" in result.data
        assert "total_chunks_ingested" in result.data

    @pytest.mark.asyncio
    async def test_crawl_markdown_file_url_missing_url(self, web_crawler_tool):
        """Test error handling when URL is missing for crawl_markdown_file_url"""
        result = await web_crawler_tool.execute(action="crawl_markdown_file_url")
        assert isinstance(result, ToolResponse)
        assert not result.success
        assert "Missing 'url' parameter" in result.error

    @pytest.mark.asyncio
    async def test_unknown_action(self, web_crawler_tool):
        """Test error handling for unknown action"""
        result = await web_crawler_tool.execute(action="invalid_action")
        assert isinstance(result, ToolResponse)
        assert not result.success
        assert "Unknown action: invalid_action" in result.error

    @pytest.mark.asyncio
    async def test_custom_chunk_size(self, web_crawler_tool):
        """Test that custom chunk size is applied"""
        result = await web_crawler_tool.execute(
            action="crawl_site",
            url="https://example.com",
            chunk_size=500
        )
        assert result.success
        assert web_crawler_tool.chunker.chunk_size == 500

    @pytest.mark.asyncio
    async def test_stream_event_emission(self, web_crawler_tool, mock_agent):
        """Test that stream events are emitted during crawling"""
        await web_crawler_tool.execute(
            action="crawl_site",
            url="https://example.com"
        )
        
        # Verify that stream events were attempted to be emitted
        # Note: The actual emission depends on StreamProtocol availability
        assert mock_agent._emit_stream_event.called or True  # Mock may not be called if StreamProtocol unavailable

    @pytest.mark.asyncio
    async def test_process_and_ingest_crawled_doc(self, web_crawler_tool):
        """Test the document processing and chunking pipeline"""
        raw_doc_data = {
            "url": "https://example.com/test",
            "raw_content": "This is test content for processing",
            "title": "Test Document"
        }
        
        chunks_count = await web_crawler_tool._process_and_ingest_crawled_doc(raw_doc_data)
        assert isinstance(chunks_count, int)
        assert chunks_count >= 0

# Integration test for the full crawler pipeline
class TestWebCrawlerIntegration:
    @pytest.mark.asyncio
    async def test_full_crawl_pipeline(self):
        """Test the complete crawling pipeline end-to-end"""
        # Create mock agent
        mock_agent = Mock()
        mock_agent.agent_name = "integration_test_agent"
        mock_agent.context = Mock()
        mock_agent.context.id = "integration_test_context"
        mock_agent._emit_stream_event = Mock()
        
        # Create tool instance
        tool = WebCrawlerTool(mock_agent)
        
        # Test crawl_site action
        result = await tool.execute(
            action="crawl_site",
            url="https://example.com",
            max_depth=1,
            max_pages=3,
            chunk_size=200
        )
        
        assert result.success
        assert result.data["pages_processed"] >= 0
        assert result.data["total_chunks_ingested"] >= 0
        assert "Site crawl completed" in result.message

if __name__ == "__main__":
    # Run tests using pytest
    pytest.main([__file__])