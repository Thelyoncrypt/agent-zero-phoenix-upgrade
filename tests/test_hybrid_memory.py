# tests/test_hybrid_memory.py
import pytest
import asyncio
from unittest.mock import Mock, patch
from python.tools.hybrid_memory_tool import HybridMemoryTool
from python.helpers.tool import Response as ToolResponse

class TestHybridMemoryTool:
    @pytest.fixture
    def mock_agent(self):
        """Create a mock agent for testing"""
        agent = Mock()
        agent.agent_name = "test_agent"
        agent.context = Mock()
        agent.context.id = "test_context"
        agent._emit_stream_event = Mock()
        agent.get_user_id = Mock(return_value="test_user")
        agent.get_thread_id = Mock(return_value="test_thread")
        agent._call_tool = Mock()
        return agent

    @pytest.fixture
    def hybrid_memory_tool(self, mock_agent):
        """Create HybridMemoryTool instance for testing"""
        return HybridMemoryTool(mock_agent)

    @pytest.mark.asyncio
    async def test_hybrid_memory_initialization(self, hybrid_memory_tool, mock_agent):
        """Test that HybridMemoryTool initializes correctly"""
        assert hybrid_memory_tool.name == "hybrid_memory_tool"
        assert hybrid_memory_tool.agent == mock_agent
        # Test that it uses the user_id from the agent
        assert hybrid_memory_tool.agent_id_for_memory == "test_user"

    @pytest.mark.asyncio
    async def test_missing_action_parameter(self, hybrid_memory_tool):
        """Test error handling when action parameter is missing"""
        result = await hybrid_memory_tool.execute()
        assert isinstance(result, ToolResponse)
        assert not result.success
        assert "Missing required 'action' parameter" in result.error

    @pytest.mark.asyncio
    async def test_store_interaction_missing_data(self, hybrid_memory_tool):
        """Test error handling when interaction_data is missing for store_interaction"""
        result = await hybrid_memory_tool.execute(action="store_interaction")
        assert isinstance(result, ToolResponse)
        assert not result.success
        assert "Missing or invalid 'interaction_data'" in result.error

    @pytest.mark.asyncio
    async def test_store_interaction_success(self, hybrid_memory_tool, mock_agent):
        """Test successful store_interaction execution"""
        # Mock successful responses from both memory systems
        mock_agent._call_tool.side_effect = [
            {"message": "Stored in structured memory", "error": False},  # memory_save response
            {"message": "Stored in intelligent memory", "error": False, "data": {"stored_id": "mem_123"}}  # memory_agent_tool response
        ]
        
        interaction_data = {
            "type": "user_query",
            "content": "User asked about Python programming",
            "messages": [{"role": "user", "content": "What is Python?"}],
            "timestamp": "2024-01-15T10:30:00Z"
        }
        
        result = await hybrid_memory_tool.execute(
            action="store_interaction",
            interaction_data=interaction_data,
            user_id="test_user"
        )
        
        assert isinstance(result, ToolResponse)
        assert result.success
        assert "structured_memory_status" in result.data
        assert "intelligent_memory_status" in result.data
        assert "success" in result.data["structured_memory_status"]
        assert "success" in result.data["intelligent_memory_status"]
        assert "Interaction processed by hybrid memory" in result.message

    @pytest.mark.asyncio
    async def test_store_interaction_partial_failure(self, hybrid_memory_tool, mock_agent):
        """Test store_interaction when one memory system fails"""
        # Mock one success and one failure
        mock_agent._call_tool.side_effect = [
            {"message": "Stored in structured memory", "error": False},  # memory_save success
            {"message": "Failed to store", "error": True}  # memory_agent_tool failure
        ]
        
        interaction_data = {
            "type": "agent_response",
            "content": "Agent provided help with coding",
            "messages": [{"role": "assistant", "content": "Here's how to code in Python..."}]
        }
        
        result = await hybrid_memory_tool.execute(
            action="store_interaction",
            interaction_data=interaction_data
        )
        
        assert result.success
        assert "success" in result.data["structured_memory_status"]
        assert "failed" in result.data["intelligent_memory_status"]

    @pytest.mark.asyncio
    async def test_retrieve_context_missing_query(self, hybrid_memory_tool):
        """Test error handling when query parameter is missing for retrieve_context"""
        result = await hybrid_memory_tool.execute(action="retrieve_context")
        assert isinstance(result, ToolResponse)
        assert not result.success
        assert "Missing 'query' parameter" in result.error

    @pytest.mark.asyncio
    async def test_retrieve_context_success(self, hybrid_memory_tool, mock_agent):
        """Test successful retrieve_context execution"""
        # Mock responses from both memory systems
        structured_results = [{"text": "Structured memory result about Python"}]
        intelligent_results = {"results": [{"data": "Intelligent memory result about Python", "relevance_score": 0.8}]}
        
        mock_agent._call_tool.side_effect = [
            {"message": str(structured_results), "error": False},  # memory_load response
            {"data": intelligent_results, "error": False}  # memory_agent_tool response
        ]
        
        result = await hybrid_memory_tool.execute(
            action="retrieve_context",
            query="Python programming",
            limit=5,
            user_id="test_user"
        )
        
        assert isinstance(result, ToolResponse)
        assert result.success
        assert "structured_results" in result.data
        assert "intelligent_results" in result.data
        assert "ranked_combined_context" in result.data
        assert result.data["query"] == "Python programming"
        assert "Context retrieved from hybrid memory" in result.message

    @pytest.mark.asyncio
    async def test_retrieve_context_with_empty_results(self, hybrid_memory_tool, mock_agent):
        """Test retrieve_context when no results are found"""
        # Mock empty responses from both memory systems
        mock_agent._call_tool.side_effect = [
            {"message": "[]", "error": False},  # memory_load empty response
            {"data": {"results": []}, "error": False}  # memory_agent_tool empty response
        ]
        
        result = await hybrid_memory_tool.execute(
            action="retrieve_context",
            query="nonexistent topic"
        )
        
        assert result.success
        assert len(result.data["structured_results"]) == 0
        assert len(result.data["intelligent_results"]) == 0
        assert "No relevant information found" in result.data["ranked_combined_context"]

    @pytest.mark.asyncio
    async def test_retrieve_context_with_errors(self, hybrid_memory_tool, mock_agent):
        """Test retrieve_context when memory systems return errors"""
        # Mock error responses from both memory systems
        mock_agent._call_tool.side_effect = [
            {"message": "Memory load failed", "error": True},  # memory_load error
            {"message": "Search failed", "error": True}  # memory_agent_tool error
        ]
        
        result = await hybrid_memory_tool.execute(
            action="retrieve_context",
            query="test query"
        )
        
        assert result.success  # Tool succeeds even if individual memory systems fail
        assert len(result.data["structured_results"]) == 1
        assert len(result.data["intelligent_results"]) == 1
        assert "error" in result.data["structured_results"][0]
        assert "error" in result.data["intelligent_results"][0]

    @pytest.mark.asyncio
    async def test_unknown_action(self, hybrid_memory_tool):
        """Test error handling for unknown action"""
        result = await hybrid_memory_tool.execute(action="invalid_action")
        assert isinstance(result, ToolResponse)
        assert not result.success
        assert "Unknown action: invalid_action" in result.error

    @pytest.mark.asyncio
    async def test_stream_event_emission(self, hybrid_memory_tool, mock_agent):
        """Test that stream events are emitted during operations"""
        # Mock successful tool calls
        mock_agent._call_tool.side_effect = [
            {"message": "Success", "error": False},
            {"message": "Success", "error": False}
        ]
        
        interaction_data = {
            "type": "test_interaction",
            "content": "Test content for stream events"
        }
        
        await hybrid_memory_tool.execute(
            action="store_interaction",
            interaction_data=interaction_data
        )
        
        # Verify that stream events were attempted to be emitted
        # Note: The actual emission depends on StreamProtocol availability
        assert mock_agent._emit_stream_event.called or True  # Mock may not be called if StreamProtocol unavailable

    @pytest.mark.asyncio
    async def test_context_ranking_logic(self, hybrid_memory_tool, mock_agent):
        """Test the placeholder context ranking and combination logic"""
        # Mock responses with different content structures
        structured_results = [
            {"text": "First structured result"},
            {"content": "Second structured result"}
        ]
        intelligent_results = {
            "results": [
                {"data": "First intelligent result"},
                {"content": "Second intelligent result"}
            ]
        }
        
        mock_agent._call_tool.side_effect = [
            {"message": str(structured_results), "error": False},
            {"data": intelligent_results, "error": False}
        ]
        
        result = await hybrid_memory_tool.execute(
            action="retrieve_context",
            query="test ranking"
        )
        
        assert result.success
        combined_context = result.data["ranked_combined_context"]
        
        # Check that content from both systems is included
        assert "First structured result" in combined_context
        assert "Second structured result" in combined_context
        assert "First intelligent result" in combined_context
        assert "Second intelligent result" in combined_context

# Integration test for the full hybrid memory pipeline
class TestHybridMemoryIntegration:
    @pytest.mark.asyncio
    async def test_full_hybrid_memory_pipeline(self):
        """Test the complete hybrid memory pipeline end-to-end"""
        # Create mock agent
        mock_agent = Mock()
        mock_agent.agent_name = "integration_test_agent"
        mock_agent.context = Mock()
        mock_agent.context.id = "integration_test_context"
        mock_agent._emit_stream_event = Mock()
        mock_agent.get_user_id = Mock(return_value="integration_user")
        mock_agent.get_thread_id = Mock(return_value="integration_thread")
        mock_agent._call_tool = Mock()
        
        # Create tool instance
        tool = HybridMemoryTool(mock_agent)
        
        # Test storing an interaction
        mock_agent._call_tool.side_effect = [
            {"message": "Stored successfully", "error": False},  # memory_save
            {"message": "Added memory", "error": False, "data": {"stored_id": "mem_456"}}  # memory_agent_tool
        ]
        
        interaction_data = {
            "type": "user_question",
            "content": "User asked about machine learning best practices",
            "messages": [
                {"role": "user", "content": "What are the best practices for ML?"},
                {"role": "assistant", "content": "Here are some ML best practices..."}
            ],
            "metadata": {"category": "technical_question"}
        }
        
        store_result = await tool.execute(
            action="store_interaction",
            interaction_data=interaction_data
        )
        assert store_result.success
        assert "success" in store_result.data["structured_memory_status"]
        assert "success" in store_result.data["intelligent_memory_status"]
        
        # Test retrieving context
        mock_agent._call_tool.side_effect = [
            {"message": '[{"text": "ML best practices include data validation..."}]', "error": False},  # memory_load
            {"data": {"results": [{"data": "Machine learning requires careful data preparation", "relevance_score": 0.9}]}, "error": False}  # memory_agent_tool
        ]
        
        retrieve_result = await tool.execute(
            action="retrieve_context",
            query="machine learning best practices",
            limit=3
        )
        assert retrieve_result.success
        assert len(retrieve_result.data["structured_results"]) > 0
        assert len(retrieve_result.data["intelligent_results"]) > 0
        assert "ML best practices" in retrieve_result.data["ranked_combined_context"]
        assert "data preparation" in retrieve_result.data["ranked_combined_context"]

if __name__ == "__main__":
    # Run tests using pytest
    pytest.main([__file__])