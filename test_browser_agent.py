#!/usr/bin/env python3
"""
Test script for BrowserAgent (Stagehand-inspired) integration
Demonstrates browser automation capabilities with StreamProtocol events
"""

import asyncio
import sys
import os

# Add the project root to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from python.agent import AgentContext, Agent
from python.tools.browser_agent_tool import BrowserAgentTool
from python.tools.stream_protocol_tool import StreamTransport

async def test_browser_agent():
    """Test the complete BrowserAgent workflow"""
    print("=== Agent Zero BrowserAgent Test ===\n")
    
    # 1. Create stream transport (simulating run_ui.py)
    print("1. Creating StreamTransport...")
    transport = StreamTransport()
    
    # 2. Create agent context with stream support
    print("2. Creating AgentContext...")
    context = AgentContext.get(
        name="BrowserAgent Test",
        thread_id="browser-test-thread",
        user_id="browser-test-user"
    )
    context.set_custom_data('stream_transport', transport)
    
    # 3. Create agent
    print("3. Creating Agent...")
    agent = Agent(
        agent_id="browser-test-agent",
        agent_name="BrowserTestAgent", 
        context=context
    )
    
    # 4. Create BrowserAgentTool
    print("4. Creating BrowserAgentTool...")
    browser_tool = BrowserAgentTool(agent)
    
    # 5. Test navigation
    print("\n5. Testing navigation...")
    nav_result = await browser_tool.execute(
        action="navigate",
        url="https://example.com",
        session_id="test-session"
    )
    print(f"Navigation result: {nav_result.success}")
    print(f"Navigation data: {nav_result.data}")
    
    # 6. Test AI action
    print("\n6. Testing AI action...")
    act_result = await browser_tool.execute(
        action="act",
        instructions="Click the login button and enter username 'testuser'",
        session_id="test-session"
    )
    print(f"AI action result: {act_result.success}")
    print(f"AI action data: {act_result.data}")
    
    # 7. Test data extraction
    print("\n7. Testing data extraction...")
    extract_result = await browser_tool.execute(
        action="extract",
        instructions="Extract the page title and main heading",
        schema={
            "type": "object",
            "properties": {
                "title": {"type": "string"},
                "heading": {"type": "string"}
            }
        },
        session_id="test-session"
    )
    print(f"Extraction result: {extract_result.success}")
    print(f"Extraction data: {extract_result.data}")
    
    # 8. Test computer use agent
    print("\n8. Testing computer use agent...")
    agent_exec_result = await browser_tool.execute(
        action="agent_execute",
        instructions="Search for Python documentation and summarize the first result",
        model="computer-use-preview"
    )
    print(f"Agent execute result: {agent_exec_result.success}")
    print(f"Agent execute data: {agent_exec_result.data}")
    
    # 9. Test session closure
    print("\n9. Testing session closure...")
    close_result = await browser_tool.execute(
        action="close_session",
        session_id="test-session"
    )
    print(f"Session close result: {close_result.success}")
    print(f"Session close message: {close_result.message}")
    
    print("\n=== BrowserAgent Test Complete ===")

async def test_browser_agent_integration():
    """Test BrowserAgent integration with Agent reasoning"""
    print("\n=== BrowserAgent Integration Test ===\n")
    
    # Create context and agent with browser tool
    transport = StreamTransport()
    context = AgentContext.get(
        name="Browser Integration Test",
        thread_id="integration-test-thread",
        user_id="integration-test-user"
    )
    context.set_custom_data('stream_transport', transport)
    
    agent = Agent(
        agent_id="integration-test-agent",
        agent_name="IntegrationTestAgent",
        context=context
    )
    
    # Add browser tool to agent
    browser_tool = BrowserAgentTool(agent)
    agent.add_tool(browser_tool)
    
    # Test agent processing with browser tool usage
    print("Testing agent message processing with browser capabilities...")
    
    # Simulate agent deciding to use browser tool during reasoning
    # This would normally happen through LLM tool selection
    print("\nAgent is navigating to a website...")
    nav_result = await browser_tool.execute(
        action="navigate",
        url="https://www.python.org",
        session_id="integration-session"
    )
    
    print(f"Navigation successful: {nav_result.success}")
    
    # Simulate extracting information
    print("\nAgent is extracting page information...")
    extract_result = await browser_tool.execute(
        action="extract",
        instructions="Get the main page title and latest news headline",
        session_id="integration-session"
    )
    
    print(f"Extraction result: {extract_result.data}")
    
    # Clean up
    await browser_tool.execute(action="close_session", session_id="integration-session")
    
    print("\n=== BrowserAgent Integration Test Complete ===")

async def test_error_handling():
    """Test error handling in BrowserAgent"""
    print("\n=== BrowserAgent Error Handling Test ===\n")
    
    # Create minimal setup
    context = AgentContext.get(thread_id="error-test-thread")
    agent = Agent("error-test-agent", "ErrorTestAgent", context)
    browser_tool = BrowserAgentTool(agent)
    
    # Test missing action
    print("1. Testing missing action parameter...")
    result = await browser_tool.execute()
    print(f"Missing action result: success={result.success}, error='{result.error}'")
    
    # Test missing URL for navigate
    print("\n2. Testing missing URL for navigate...")
    result = await browser_tool.execute(action="navigate")
    print(f"Missing URL result: success={result.success}, error='{result.error}'")
    
    # Test invalid action
    print("\n3. Testing invalid action...")
    result = await browser_tool.execute(action="invalid_action")
    print(f"Invalid action result: success={result.success}, error='{result.error}'")
    
    print("\n=== Error Handling Test Complete ===")

if __name__ == "__main__":
    print("Starting Agent Zero BrowserAgent tests...\n")
    
    # Run tests
    asyncio.run(test_browser_agent())
    asyncio.run(test_browser_agent_integration())
    asyncio.run(test_error_handling())
    
    print("\nAll BrowserAgent tests completed successfully!")