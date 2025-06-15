#!/usr/bin/env python3
"""
Test script for Agent Zero StreamProtocol implementation
Demonstrates the complete workflow from message input to streamed events
"""

import asyncio
import sys
import os

# Add the project root to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from python.agent import AgentContext, Agent
from python.tools.stream_protocol_tool import StreamProtocolTool, StreamTransport, RunAgentInput

async def test_stream_protocol():
    """Test the complete StreamProtocol workflow"""
    print("=== Agent Zero StreamProtocol Test ===\n")
    
    # 1. Create a global transport (simulating run_ui.py)
    print("1. Creating StreamTransport...")
    transport = StreamTransport()
    
    # 2. Create agent context with stream support
    print("2. Creating AgentContext...")
    context = AgentContext.get(
        name="StreamProtocol Test",
        thread_id="test-thread-123",
        user_id="test-user-456"
    )
    context.set_custom_data('stream_transport', transport)
    
    # 3. Create agent
    print("3. Creating Agent...")
    agent = Agent(
        agent_id="stream-test-agent",
        agent_name="StreamTestAgent", 
        context=context
    )
    
    # 4. Create StreamProtocolTool
    print("4. Creating StreamProtocolTool...")
    stream_tool = StreamProtocolTool(agent)
    
    # 5. Test direct event emission
    print("\n5. Testing direct event emission...")
    await stream_tool.execute(
        action="emit_event",
        event_type="session_start",
        payload={"threadId": context.thread_id, "userId": context.user_id}
    )
    
    # 6. Test RunAgentInput handling
    print("\n6. Testing RunAgentInput handling...")
    test_input = {
        "threadId": context.thread_id,
        "userId": context.user_id,
        "messages": [
            {
                "role": "user",
                "content": "Hello, can you help me with a task?",
                "id": "msg-123"
            }
        ],
        "state": {"test": True},
        "metadata": {"source": "test_script"}
    }
    
    result = await stream_tool.execute(
        action="handle_input",
        input_data=test_input
    )
    print(f"RunAgentInput result: {result}")
    
    # 7. Test direct agent message processing (triggers full monologue)
    print("\n7. Testing agent message processing with full event stream...")
    response = await agent.process_streamed_message(
        content="What's the weather like today?",
        role="user"
    )
    print(f"Agent response: {response}")
    
    # 8. Test session end
    print("\n8. Testing session end...")
    await stream_tool.execute(
        action="end_session",
        thread_id=context.thread_id
    )
    
    print("\n=== Test Complete ===")

async def test_websocket_simulation():
    """Simulate WebSocket connection and message flow"""
    print("\n=== WebSocket Simulation Test ===\n")
    
    # Simulate the WebSocket server setup from run_ui.py
    transport = StreamTransport()
    
    # Mock WebSocket connection
    class MockWebSocket:
        def __init__(self, name):
            self.name = name
            self.closed = False
            self.messages = []
        
        async def send(self, data):
            print(f"[WebSocket {self.name}] Sent: {data}")
            self.messages.append(data)
        
        async def receive(self):
            # Simulate client ping
            return '{"type": "ping"}'
        
        def close(self):
            self.closed = True
    
    # Register mock WebSocket
    mock_ws = MockWebSocket("test-client")
    conn_id = await transport.register_connection(mock_ws, "test-thread-ws", "test-user-ws")
    
    # Create agent context and agent
    context = AgentContext.get(thread_id="test-thread-ws", user_id="test-user-ws")
    context.set_custom_data('stream_transport', transport)
    agent = Agent("ws-test-agent", "WebSocketTestAgent", context)
    
    # Process a message (this will emit events to the WebSocket)
    await agent.process_streamed_message("Tell me a joke!", "user")
    
    # Cleanup
    await transport.unregister_connection(conn_id)
    
    print(f"WebSocket received {len(mock_ws.messages)} messages")
    print("=== WebSocket Simulation Complete ===")

if __name__ == "__main__":
    print("Starting Agent Zero StreamProtocol tests...\n")
    
    # Run tests
    asyncio.run(test_stream_protocol())
    asyncio.run(test_websocket_simulation())
    
    print("\nAll tests completed successfully!")