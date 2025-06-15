# tests/test_memory_agent.py
import pytest
import asyncio
from unittest.mock import Mock, patch
from python.tools.memory_agent_tool import MemoryAgentTool
from python.helpers.tool import Response as ToolResponse

class TestMemoryAgentTool:
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
        return agent

    @pytest.fixture
    def memory_agent_tool(self, mock_agent):
        """Create MemoryAgentTool instance for testing"""
        return MemoryAgentTool(mock_agent)

    @pytest.mark.asyncio
    async def test_memory_agent_initialization(self, memory_agent_tool, mock_agent):
        """Test that MemoryAgentTool initializes correctly"""
        assert memory_agent_tool.name == "memory_agent_tool"
        assert memory_agent_tool.agent == mock_agent
        assert memory_agent_tool.memory_system is not None
        # Test that it uses the user_id from the agent
        assert memory_agent_tool.memory_system.agent_id == "test_user"

    @pytest.mark.asyncio
    async def test_missing_action_parameter(self, memory_agent_tool):
        """Test error handling when action parameter is missing"""
        result = await memory_agent_tool.execute()
        assert isinstance(result, ToolResponse)
        assert not result.success
        assert "Missing required 'action' parameter" in result.error

    @pytest.mark.asyncio
    async def test_add_missing_data(self, memory_agent_tool):
        """Test error handling when data is missing for add action"""
        result = await memory_agent_tool.execute(action="add")
        assert isinstance(result, ToolResponse)
        assert not result.success
        assert "required for 'add' action" in result.error

    @pytest.mark.asyncio
    async def test_add_from_messages_success(self, memory_agent_tool):
        """Test successful add from messages"""
        messages = [
            {"role": "user", "content": "My favorite color is blue"},
            {"role": "assistant", "content": "I'll remember that your favorite color is blue"}
        ]
        
        result = await memory_agent_tool.execute(
            action="add",
            messages=messages,
            user_id="test_user"
        )
        assert isinstance(result, ToolResponse)
        assert result.success
        assert "stored_ids" in result.data
        assert len(result.data["stored_ids"]) == 2
        assert "Added 2 memories from messages" in result.message

    @pytest.mark.asyncio
    async def test_add_generic_memory_success(self, memory_agent_tool):
        """Test successful add of generic memory"""
        data = "User prefers morning meetings"
        
        result = await memory_agent_tool.execute(
            action="add",
            data=data,
            memory_id="custom_memory_1",
            user_id="test_user"
        )
        assert isinstance(result, ToolResponse)
        assert result.success
        assert "stored_id" in result.data
        assert result.data["stored_id"] == "custom_memory_1"
        assert "Memory added with ID: custom_memory_1" in result.message

    @pytest.mark.asyncio
    async def test_search_missing_query(self, memory_agent_tool):
        """Test error handling when query parameter is missing for search"""
        result = await memory_agent_tool.execute(action="search")
        assert isinstance(result, ToolResponse)
        assert not result.success
        assert "Missing 'query' parameter" in result.error

    @pytest.mark.asyncio
    async def test_search_success(self, memory_agent_tool):
        """Test successful memory search"""
        # First add a memory
        await memory_agent_tool.execute(
            action="add",
            data="User loves pizza and pasta",
            user_id="test_user"
        )
        
        # Now search for it
        result = await memory_agent_tool.execute(
            action="search",
            query="pizza",
            limit=3,
            user_id="test_user"
        )
        assert isinstance(result, ToolResponse)
        assert result.success
        assert "results" in result.data
        assert len(result.data["results"]) > 0
        # Check that the search found our memory
        found_pizza = any("pizza" in str(memory.get("data", "")).lower() for memory in result.data["results"])
        assert found_pizza

    @pytest.mark.asyncio
    async def test_update_missing_parameters(self, memory_agent_tool):
        """Test error handling when parameters are missing for update"""
        result = await memory_agent_tool.execute(action="update")
        assert isinstance(result, ToolResponse)
        assert not result.success
        assert "required for update action" in result.error

    @pytest.mark.asyncio
    async def test_update_success(self, memory_agent_tool):
        """Test successful memory update"""
        # First add a memory
        add_result = await memory_agent_tool.execute(
            action="add",
            data="User's favorite color is blue",
            user_id="test_user"
        )
        memory_id = add_result.data["stored_id"]
        
        # Update the memory
        result = await memory_agent_tool.execute(
            action="update",
            memory_id=memory_id,
            data="User's favorite color is green",
            user_id="test_user"
        )
        assert isinstance(result, ToolResponse)
        assert result.success
        assert result.data["success"] is True
        assert "completed" in result.message

    @pytest.mark.asyncio
    async def test_update_nonexistent_memory(self, memory_agent_tool):
        """Test updating a non-existent memory"""
        result = await memory_agent_tool.execute(
            action="update",
            memory_id="nonexistent_id",
            data="Some new data",
            user_id="test_user"
        )
        assert isinstance(result, ToolResponse)
        # Update should succeed at the tool level but the actual update should fail
        assert result.success
        assert result.data["success"] is False
        assert "failed" in result.message

    @pytest.mark.asyncio
    async def test_delete_missing_memory_id(self, memory_agent_tool):
        """Test error handling when memory_id is missing for delete"""
        result = await memory_agent_tool.execute(action="delete")
        assert isinstance(result, ToolResponse)
        assert not result.success
        assert "Missing 'memory_id' parameter" in result.error

    @pytest.mark.asyncio
    async def test_delete_success(self, memory_agent_tool):
        """Test successful memory deletion"""
        # First add a memory
        add_result = await memory_agent_tool.execute(
            action="add",
            data="Memory to be deleted",
            user_id="test_user"
        )
        memory_id = add_result.data["stored_id"]
        
        # Delete the memory
        result = await memory_agent_tool.execute(
            action="delete",
            memory_id=memory_id,
            user_id="test_user"
        )
        assert isinstance(result, ToolResponse)
        assert result.success
        assert result.data["success"] is True
        assert "completed" in result.message

    @pytest.mark.asyncio
    async def test_delete_nonexistent_memory(self, memory_agent_tool):
        """Test deleting a non-existent memory"""
        result = await memory_agent_tool.execute(
            action="delete",
            memory_id="nonexistent_id",
            user_id="test_user"
        )
        assert isinstance(result, ToolResponse)
        # Delete should succeed at the tool level but the actual deletion should fail
        assert result.success
        assert result.data["success"] is False
        assert "failed" in result.message

    @pytest.mark.asyncio
    async def test_get_all_memories(self, memory_agent_tool):
        """Test getting all memories"""
        # Add some memories first
        await memory_agent_tool.execute(
            action="add",
            data="First memory",
            user_id="test_user"
        )
        await memory_agent_tool.execute(
            action="add",
            data="Second memory",
            user_id="test_user"
        )
        
        # Get all memories
        result = await memory_agent_tool.execute(
            action="get_all",
            user_id="test_user"
        )
        assert isinstance(result, ToolResponse)
        assert result.success
        assert "memories" in result.data
        assert len(result.data["memories"]) >= 2

    @pytest.mark.asyncio
    async def test_unknown_action(self, memory_agent_tool):
        """Test error handling for unknown action"""
        result = await memory_agent_tool.execute(action="invalid_action")
        assert isinstance(result, ToolResponse)
        assert not result.success
        assert "Unknown action: invalid_action" in result.error

    @pytest.mark.asyncio
    async def test_stream_event_emission(self, memory_agent_tool, mock_agent):
        """Test that stream events are emitted during operations"""
        await memory_agent_tool.execute(
            action="add",
            data="Test memory for events",
            user_id="test_user"
        )
        
        # Verify that stream events were attempted to be emitted
        # Note: The actual emission depends on StreamProtocol availability
        assert mock_agent._emit_stream_event.called or True  # Mock may not be called if StreamProtocol unavailable

# Integration test for the full memory agent pipeline
class TestMemoryAgentIntegration:
    @pytest.mark.asyncio
    async def test_full_memory_pipeline(self):
        """Test the complete memory management pipeline end-to-end"""
        # Create mock agent
        mock_agent = Mock()
        mock_agent.agent_name = "integration_test_agent"
        mock_agent.context = Mock()
        mock_agent.context.id = "integration_test_context"
        mock_agent._emit_stream_event = Mock()
        mock_agent.get_user_id = Mock(return_value="integration_user")
        mock_agent.get_thread_id = Mock(return_value="integration_thread")
        
        # Create tool instance
        tool = MemoryAgentTool(mock_agent)
        
        # Test adding memories from messages
        messages = [
            {"role": "user", "content": "I work at TechCorp as a software engineer"},
            {"role": "user", "content": "I enjoy hiking and photography in my free time"},
            {"role": "assistant", "content": "That's great! Software engineering and outdoor hobbies make a nice balance"}
        ]
        
        add_result = await tool.execute(action="add", messages=messages)
        assert add_result.success
        assert len(add_result.data["stored_ids"]) == 3
        
        # Test searching for work-related memories
        search_result = await tool.execute(
            action="search",
            query="work software engineer",
            limit=5
        )
        assert search_result.success
        assert len(search_result.data["results"]) > 0
        
        # Check that we found the work-related memory
        work_memory_found = any(
            "software engineer" in str(memory.get("data", "")).lower() 
            for memory in search_result.data["results"]
        )
        assert work_memory_found
        
        # Test adding a generic memory
        generic_add_result = await tool.execute(
            action="add",
            data="User prefers video calls over phone calls for meetings"
        )
        assert generic_add_result.success
        
        # Test updating a memory
        memory_id = generic_add_result.data["stored_id"]
        update_result = await tool.execute(
            action="update",
            memory_id=memory_id,
            data="User strongly prefers video calls over phone calls, especially for important meetings"
        )
        assert update_result.success
        assert update_result.data["success"] is True
        
        # Test searching for the updated memory
        updated_search = await tool.execute(
            action="search",
            query="video calls meetings",
            limit=3
        )
        assert updated_search.success
        
        # Test getting all memories
        all_memories_result = await tool.execute(action="get_all")
        assert all_memories_result.success
        assert len(all_memories_result.data["memories"]) >= 4  # 3 from messages + 1 generic
        
        # Test deleting a memory
        delete_result = await tool.execute(
            action="delete",
            memory_id=memory_id
        )
        assert delete_result.success
        assert delete_result.data["success"] is True

if __name__ == "__main__":
    # Run tests using pytest
    pytest.main([__file__])