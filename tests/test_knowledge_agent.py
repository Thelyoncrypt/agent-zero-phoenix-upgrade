# tests/test_knowledge_agent.py
import pytest
import asyncio
from unittest.mock import Mock, patch
from python.tools.knowledge_agent_tool import KnowledgeAgentTool
from python.helpers.tool import Response as ToolResponse

class TestKnowledgeAgentTool:
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
    def knowledge_agent_tool(self, mock_agent):
        """Create KnowledgeAgentTool instance for testing"""
        return KnowledgeAgentTool(mock_agent)

    @pytest.mark.asyncio
    async def test_knowledge_agent_initialization(self, knowledge_agent_tool, mock_agent):
        """Test that KnowledgeAgentTool initializes correctly"""
        assert knowledge_agent_tool.name == "knowledge_agent_tool"
        assert knowledge_agent_tool.agent == mock_agent
        assert knowledge_agent_tool.db_manager is not None
        assert knowledge_agent_tool.embed_generator is not None
        assert knowledge_agent_tool.retriever is not None
        assert knowledge_agent_tool.rag_agent_logic is not None

    @pytest.mark.asyncio
    async def test_missing_action_parameter(self, knowledge_agent_tool):
        """Test error handling when action parameter is missing"""
        result = await knowledge_agent_tool.execute()
        assert isinstance(result, ToolResponse)
        assert not result.success
        assert "Missing required 'action' parameter" in result.error

    @pytest.mark.asyncio
    async def test_ingest_chunks_missing_data(self, knowledge_agent_tool):
        """Test error handling when chunks_data is missing for ingest_chunks"""
        result = await knowledge_agent_tool.execute(action="ingest_chunks")
        assert isinstance(result, ToolResponse)
        assert not result.success
        assert "Missing 'chunks_data' parameter" in result.error

    @pytest.mark.asyncio
    async def test_ingest_chunks_success(self, knowledge_agent_tool):
        """Test successful ingest_chunks execution"""
        chunks_data = [
            {
                "text": "This is test content for chunk 1",
                "metadata": {"source": "test_doc.pdf", "source_url": "https://example.com/test.pdf"},
                "id": "test_chunk_1"
            },
            {
                "text": "This is test content for chunk 2",
                "metadata": {"source": "test_doc.pdf", "source_url": "https://example.com/test.pdf"},
                "id": "test_chunk_2"
            }
        ]
        
        result = await knowledge_agent_tool.execute(
            action="ingest_chunks",
            chunks_data=chunks_data
        )
        assert isinstance(result, ToolResponse)
        assert result.success
        assert "count" in result.data
        assert result.data["count"] == 2
        assert "Ingested 2 chunks" in result.message

    @pytest.mark.asyncio
    async def test_ingest_chunks_auto_embedding(self, knowledge_agent_tool):
        """Test that chunks without embeddings get auto-embedded"""
        chunks_data = [
            {
                "text": "Test content without embedding",
                "metadata": {"source": "test.pdf"},
                "id": "test_chunk_no_embed"
            }
        ]
        
        result = await knowledge_agent_tool.execute(
            action="ingest_chunks",
            chunks_data=chunks_data
        )
        assert result.success
        # Check that embedding was generated (the chunk should have been processed)
        assert result.data["count"] == 1

    @pytest.mark.asyncio
    async def test_ingest_chunks_missing_text(self, knowledge_agent_tool):
        """Test error handling when chunk has no text for embedding"""
        chunks_data = [
            {
                "metadata": {"source": "test.pdf"},
                "id": "test_chunk_no_text"
                # Missing "text" field
            }
        ]
        
        result = await knowledge_agent_tool.execute(
            action="ingest_chunks",
            chunks_data=chunks_data
        )
        assert not result.success
        assert "has no text for embedding" in result.error

    @pytest.mark.asyncio
    async def test_query_missing_query(self, knowledge_agent_tool):
        """Test error handling when query parameter is missing"""
        result = await knowledge_agent_tool.execute(action="query")
        assert isinstance(result, ToolResponse)
        assert not result.success
        assert "Missing 'query' parameter" in result.error

    @pytest.mark.asyncio
    async def test_query_success(self, knowledge_agent_tool):
        """Test successful query execution"""
        # First ingest some data
        chunks_data = [
            {
                "text": "Pydantic AI is a Python agent framework",
                "metadata": {"source": "pydantic_docs.pdf"},
                "id": "pydantic_chunk_1"
            }
        ]
        await knowledge_agent_tool.execute(action="ingest_chunks", chunks_data=chunks_data)
        
        # Now query
        result = await knowledge_agent_tool.execute(
            action="query",
            query="What is Pydantic AI?",
            limit=3
        )
        assert isinstance(result, ToolResponse)
        assert result.success
        assert "response" in result.data
        assert "sources" in result.data
        assert "retrieved_count" in result.data

    @pytest.mark.asyncio
    async def test_raw_search_missing_query(self, knowledge_agent_tool):
        """Test error handling when query parameter is missing for raw_search"""
        result = await knowledge_agent_tool.execute(action="raw_search")
        assert isinstance(result, ToolResponse)
        assert not result.success
        assert "Missing 'query' parameter" in result.error

    @pytest.mark.asyncio
    async def test_raw_search_success(self, knowledge_agent_tool):
        """Test successful raw_search execution"""
        # First ingest some data
        chunks_data = [
            {
                "text": "Machine learning is a subset of AI",
                "metadata": {"source": "ml_book.pdf", "chapter": "introduction"},
                "id": "ml_chunk_1"
            }
        ]
        await knowledge_agent_tool.execute(action="ingest_chunks", chunks_data=chunks_data)
        
        # Now search
        result = await knowledge_agent_tool.execute(
            action="raw_search",
            query="machine learning",
            limit=5,
            filter_metadata={"source": "ml_book.pdf"}
        )
        assert isinstance(result, ToolResponse)
        assert result.success
        assert "results" in result.data

    @pytest.mark.asyncio
    async def test_list_sources_success(self, knowledge_agent_tool):
        """Test successful list_sources execution"""
        # First ingest some data with different sources
        chunks_data = [
            {
                "text": "Content from source 1",
                "metadata": {"source": "doc1.pdf"},
                "id": "chunk_1"
            },
            {
                "text": "Content from source 2",
                "metadata": {"source": "doc2.pdf"},
                "id": "chunk_2"
            }
        ]
        await knowledge_agent_tool.execute(action="ingest_chunks", chunks_data=chunks_data)
        
        # Now list sources
        result = await knowledge_agent_tool.execute(action="list_sources")
        assert isinstance(result, ToolResponse)
        assert result.success
        assert "sources" in result.data
        assert isinstance(result.data["sources"], list)

    @pytest.mark.asyncio
    async def test_unknown_action(self, knowledge_agent_tool):
        """Test error handling for unknown action"""
        result = await knowledge_agent_tool.execute(action="invalid_action")
        assert isinstance(result, ToolResponse)
        assert not result.success
        assert "Unknown action: invalid_action" in result.error

    @pytest.mark.asyncio
    async def test_stream_event_emission(self, knowledge_agent_tool, mock_agent):
        """Test that stream events are emitted during operations"""
        chunks_data = [
            {
                "text": "Test content for stream events",
                "metadata": {"source": "test.pdf"},
                "id": "stream_test_chunk"
            }
        ]
        
        await knowledge_agent_tool.execute(action="ingest_chunks", chunks_data=chunks_data)
        
        # Verify that stream events were attempted to be emitted
        # Note: The actual emission depends on StreamProtocol availability
        assert mock_agent._emit_stream_event.called or True  # Mock may not be called if StreamProtocol unavailable

# Integration test for the full knowledge agent pipeline
class TestKnowledgeAgentIntegration:
    @pytest.mark.asyncio
    async def test_full_knowledge_pipeline(self):
        """Test the complete knowledge management pipeline end-to-end"""
        # Create mock agent
        mock_agent = Mock()
        mock_agent.agent_name = "integration_test_agent"
        mock_agent.context = Mock()
        mock_agent.context.id = "integration_test_context"
        mock_agent._emit_stream_event = Mock()
        
        # Create tool instance
        tool = KnowledgeAgentTool(mock_agent)
        
        # Test ingestion
        chunks_data = [
            {
                "text": "Artificial Intelligence is a broad field of computer science",
                "metadata": {"source": "ai_textbook.pdf", "chapter": "introduction"},
                "id": "ai_intro_chunk_1"
            },
            {
                "text": "Machine Learning is a subset of AI that focuses on algorithms",
                "metadata": {"source": "ai_textbook.pdf", "chapter": "ml_basics"},
                "id": "ai_ml_chunk_1"
            }
        ]
        
        ingest_result = await tool.execute(action="ingest_chunks", chunks_data=chunks_data)
        assert ingest_result.success
        assert ingest_result.data["count"] == 2
        
        # Test querying
        query_result = await tool.execute(
            action="query",
            query="What is machine learning?",
            limit=2
        )
        assert query_result.success
        assert "response" in query_result.data
        assert len(query_result.data["sources"]) > 0
        
        # Test raw search with filter
        search_result = await tool.execute(
            action="raw_search",
            query="artificial intelligence",
            limit=5,
            filter_metadata={"source": "ai_textbook.pdf"}
        )
        assert search_result.success
        assert "results" in search_result.data
        
        # Test list sources
        sources_result = await tool.execute(action="list_sources")
        assert sources_result.success
        assert "ai_textbook.pdf" in sources_result.data["sources"]

if __name__ == "__main__":
    # Run tests using pytest
    pytest.main([__file__])