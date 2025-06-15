# tests/test_stream_transport_integration.py
import pytest
import asyncio
import json
from unittest.mock import Mock, AsyncMock, patch
from python.tools.stream_protocol_tool import StreamProtocolTool, StreamEventType, StreamEvent
from python.agent import Agent, AgentContext

class TestStreamTransportIntegration:
    @pytest.fixture
    def mock_transport(self):
        """Create a mock transport for testing"""
        transport = Mock()
        transport.emit_event_to_thread = AsyncMock()
        return transport

    @pytest.fixture
    def mock_agent_with_transport(self, mock_transport):
        """Create a mock agent with injected transport"""
        agent = Mock()
        agent.agent_name = "test_agent"
        agent.context = Mock()
        agent.context.id = "test_context"
        agent.context.get_custom_data = Mock(return_value=mock_transport)
        agent.get_thread_id = Mock(return_value="test_thread_123")
        agent.get_user_id = Mock(return_value="test_user_456")
        agent._emit_stream_event = AsyncMock()
        return agent

    @pytest.mark.asyncio
    async def test_stream_protocol_tool_with_injected_transport(self, mock_agent_with_transport, mock_transport):
        """Test that StreamProtocolTool works with injected transport"""
        tool = StreamProtocolTool(mock_agent_with_transport)
        
        # Verify transport was injected correctly
        assert tool.transport == mock_transport
        
        # Test event emission
        result = await tool.execute(
            action="emit_event",
            event_type="text_message_content",
            payload={"role": "assistant", "content": "Test message"}
        )
        
        assert result["result"]["success"] == True
        assert result["result"]["type"] == "text_message_content"
        
        # Verify transport.emit_event_to_thread was called
        mock_transport.emit_event_to_thread.assert_called_once()
        
        # Verify the event structure
        call_args = mock_transport.emit_event_to_thread.call_args[0][0]
        assert isinstance(call_args, StreamEvent)
        assert call_args.type == StreamEventType.TEXT_MESSAGE_CONTENT
        assert call_args.payload["role"] == "assistant"
        assert call_args.payload["content"] == "Test message"
        assert call_args.thread_id == "test_thread_123"
        assert call_args.user_id == "test_user_456"

    @pytest.mark.asyncio
    async def test_stream_protocol_tool_without_transport_raises_error(self):
        """Test that StreamProtocolTool raises error when transport is not available"""
        agent = Mock()
        agent.agent_name = "test_agent"
        agent.context = Mock()
        agent.context.get_custom_data = Mock(return_value=None)  # No transport
        
        with pytest.raises(RuntimeError, match="StreamTransport not properly initialized"):
            StreamProtocolTool(agent)

    @pytest.mark.asyncio
    async def test_transport_global_connection_management(self):
        """Test StreamTransportGlobal connection management"""
        # Import the class as it would be used in run_ui.py
        import sys
        import os
        sys.path.append(os.path.dirname(__file__) + '/../')
        
        # Mock the actual StreamTransportGlobal implementation
        class MockStreamTransportGlobal:
            def __init__(self):
                self.connections = {}
                self.connection_details = {}
                self.lock = asyncio.Lock()
            
            async def register_connection(self, ws, thread_id, user_id=None):
                connection_id = f"conn_{len(self.connection_details)}"
                async with self.lock:
                    if thread_id not in self.connections:
                        self.connections[thread_id] = []
                    self.connections[thread_id].append(ws)
                    self.connection_details[connection_id] = {
                        "websocket": ws, "thread_id": thread_id, "user_id": user_id
                    }
                return connection_id
            
            async def unregister_connection(self, connection_id):
                async with self.lock:
                    if connection_id in self.connection_details:
                        connection_info = self.connection_details.pop(connection_id)
                        thread_id = connection_info["thread_id"]
                        ws = connection_info["websocket"]
                        if thread_id in self.connections:
                            try:
                                self.connections[thread_id].remove(ws)
                                if not self.connections[thread_id]:
                                    del self.connections[thread_id]
                            except ValueError:
                                pass
            
            async def emit_event_to_thread(self, event):
                if not event.thread_id or event.thread_id not in self.connections:
                    return
                
                event_data = {
                    "id": event.event_id, "type": event.type.value, "payload": event.payload,
                    "timestamp": event.timestamp, "threadId": event.thread_id, "userId": event.user_id
                }
                
                for ws in self.connections[event.thread_id]:
                    await ws.send(json.dumps(event_data))
        
        transport = MockStreamTransportGlobal()
        
        # Test connection registration
        mock_ws1 = AsyncMock()
        mock_ws2 = AsyncMock()
        
        conn1 = await transport.register_connection(mock_ws1, "thread_1", "user_1")
        conn2 = await transport.register_connection(mock_ws2, "thread_1", "user_1")
        
        assert len(transport.connections["thread_1"]) == 2
        assert len(transport.connection_details) == 2
        
        # Test event emission
        test_event = StreamEvent(
            type=StreamEventType.TEXT_MESSAGE_CONTENT,
            payload={"role": "assistant", "content": "Test message"},
            thread_id="thread_1",
            user_id="user_1"
        )
        
        await transport.emit_event_to_thread(test_event)
        
        # Verify both websockets received the event
        assert mock_ws1.send.called
        assert mock_ws2.send.called
        
        # Test connection unregistration
        await transport.unregister_connection(conn1)
        assert len(transport.connections["thread_1"]) == 1
        
        await transport.unregister_connection(conn2)
        assert "thread_1" not in transport.connections

    @pytest.mark.asyncio
    async def test_agent_emit_stream_event_integration(self, mock_transport):
        """Test Agent._emit_stream_event method with transport"""
        # Create a real Agent instance with mocked dependencies
        context = Mock()
        context.id = "test_context"
        context.thread_id = "test_thread"
        context.user_id = "test_user"
        context.get_custom_data = Mock(return_value=mock_transport)
        
        agent = Agent("agent_1", "TestAgent", context)
        
        # Mock the StreamProtocolTool to verify it gets called correctly
        with patch('python.agent.StreamProtocolTool') as mock_tool_class:
            mock_tool_instance = Mock()
            mock_tool_instance.execute = AsyncMock(return_value={"success": True})
            mock_tool_class.return_value = mock_tool_instance
            
            # Test event emission
            await agent._emit_stream_event(
                StreamEventType.AGENT_THOUGHT,
                {"content": "I'm thinking about this problem"}
            )
            
            # Verify StreamProtocolTool was created and execute was called
            mock_tool_class.assert_called_once_with(agent)
            mock_tool_instance.execute.assert_called_once_with(
                action="emit_event",
                event_type="agent_thought",
                payload={"content": "I'm thinking about this problem"},
                thread_id="test_thread",
                user_id="test_user"
            )

if __name__ == "__main__":
    # Run tests using pytest
    pytest.main([__file__])