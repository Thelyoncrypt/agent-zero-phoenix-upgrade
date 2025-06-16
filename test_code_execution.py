#!/usr/bin/env python3
"""
Test script for GeneralCodeExecutionTool streaming functionality.
This script tests code execution with various runtimes and scenarios.
"""

import asyncio
import os
import sys
import tempfile
from pathlib import Path

# Add the project root to Python path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from python.tools.general_code_execution_tool import GeneralCodeExecutionTool

class MockAgent:
    """Mock agent for testing purposes."""
    def __init__(self):
        self.events = []
        
    async def _emit_stream_event(self, event_type, payload):
        """Mock event emission."""
        self.events.append({
            'type': event_type,
            'payload': payload,
            'timestamp': asyncio.get_event_loop().time()
        })
        print(f"📡 Event: {event_type} - {payload}")

async def test_code_execution():
    """Test the GeneralCodeExecutionTool with various scenarios."""
    
    print("💻 Testing GeneralCodeExecutionTool Streaming Functionality")
    print("=" * 60)
    
    # Initialize the tool with mock agent
    mock_agent = MockAgent()
    tool = GeneralCodeExecutionTool(agent_id="test_agent", agent=mock_agent)
    
    # Test scenarios
    test_scenarios = [
        {
            "name": "Python - Simple Print",
            "runtime": "python",
            "code": "print('Hello from Python!')\nprint('This is a test')",
            "description": "Test basic Python execution with multiple prints"
        },
        {
            "name": "Python - Loop with Output",
            "runtime": "python", 
            "code": """
import time
for i in range(5):
    print(f"Line {i}")
    time.sleep(0.1)
print("Done!")
""",
            "description": "Test Python with timed output for streaming"
        },
        {
            "name": "Python - Error Handling",
            "runtime": "python",
            "code": """
print("Before error")
raise ValueError("This is a test error")
print("After error - should not print")
""",
            "description": "Test Python error handling and stderr"
        },
        {
            "name": "Terminal - Echo Command",
            "runtime": "terminal",
            "code": "echo 'Hello from terminal!'",
            "description": "Test basic terminal command"
        },
        {
            "name": "Terminal - Multiple Commands",
            "runtime": "terminal",
            "code": "echo 'First line' && echo 'Second line' && echo 'Third line'",
            "description": "Test terminal with multiple commands"
        },
        {
            "name": "Node.js - Simple Script",
            "runtime": "nodejs",
            "code": """
console.log('Hello from Node.js!');
console.log('Testing JavaScript execution');
for (let i = 0; i < 3; i++) {
    console.log(`Count: ${i}`);
}
""",
            "description": "Test Node.js execution with loops"
        }
    ]
    
    for i, scenario in enumerate(test_scenarios, 1):
        print(f"\n🧪 Test {i}: {scenario['name']}")
        print(f"Description: {scenario['description']}")
        print(f"Runtime: {scenario['runtime']}")
        print(f"Code:\n{scenario['code']}")
        print("-" * 50)
        
        # Clear previous events
        mock_agent.events = []
        
        try:
            # Execute the code
            result = await tool.execute(
                runtime=scenario["runtime"],
                code=scenario["code"],
                timeout=10
            )
            
            if result.success:
                print(f"✅ SUCCESS: {result.message}")
                if result.data:
                    print(f"📊 Exit Code: {result.data.get('exit_code', 'N/A')}")
                    print(f"📝 STDOUT Length: {len(result.data.get('stdout', ''))}")
                    print(f"❌ STDERR Length: {len(result.data.get('stderr', ''))}")
                    
                    # Show final output
                    if result.data.get('stdout'):
                        print(f"📤 Final STDOUT:\n{result.data['stdout']}")
                    if result.data.get('stderr'):
                        print(f"📤 Final STDERR:\n{result.data['stderr']}")
                
                # Show streaming events
                print(f"📡 Streaming Events: {len(mock_agent.events)}")
                for event in mock_agent.events:
                    event_type = event['type']
                    payload = event['payload']
                    if hasattr(event_type, 'value'):
                        event_type = event_type.value
                    print(f"  - {event_type}: {payload.get('source', 'unknown')} - {len(payload.get('stdout', '') + payload.get('stderr', ''))} chars")
                    
            else:
                print(f"❌ FAILED: {result.message}")
                if hasattr(result, 'error'):
                    print(f"Error: {result.error}")
                    
        except Exception as e:
            print(f"❌ EXCEPTION: {str(e)}")
            import traceback
            traceback.print_exc()
        
        print("\n" + "=" * 60)
    
    print("\n🏁 Code execution testing completed!")

async def test_error_scenarios():
    """Test error handling scenarios."""
    
    print("\n🧪 Testing Error Scenarios")
    print("=" * 40)
    
    mock_agent = MockAgent()
    tool = GeneralCodeExecutionTool(agent_id="test_agent", agent=mock_agent)
    
    # Test with invalid runtime
    print("\n1. Testing invalid runtime...")
    result = await tool.execute(runtime="invalid", code="print('test')")
    print(f"Result: {'✅ PASS' if not result.success else '❌ FAIL'} - {result.message}")
    
    # Test with timeout
    print("\n2. Testing timeout...")
    result = await tool.execute(
        runtime="python", 
        code="import time; time.sleep(15)", 
        timeout=2
    )
    print(f"Result: {'✅ HANDLED' if not result.success or 'timeout' in result.message.lower() else '❌ UNEXPECTED'} - {result.message}")
    
    # Test with syntax error
    print("\n3. Testing syntax error...")
    result = await tool.execute(
        runtime="python",
        code="print('unclosed string"
    )
    print(f"Result: {'✅ HANDLED' if not result.success else '❌ UNEXPECTED'} - {result.message}")
    
    print("\n🏁 Error scenario testing completed!")

async def test_file_operations():
    """Test file saving and execution."""
    
    print("\n📁 Testing File Operations")
    print("=" * 30)
    
    mock_agent = MockAgent()
    tool = GeneralCodeExecutionTool(agent_id="test_agent", agent=mock_agent)
    
    # Test saving to file
    print("\n1. Testing save to file...")
    with tempfile.TemporaryDirectory() as temp_dir:
        result = await tool.execute(
            runtime="python",
            code="print('Hello from saved file!')",
            work_dir=temp_dir,
            save_to_file=True,
            filename="test_script.py"
        )
        
        if result.success:
            print(f"✅ File saved and executed successfully")
            script_path = result.data.get('script_path')
            if script_path and os.path.exists(script_path):
                print(f"📄 Script saved at: {script_path}")
                with open(script_path, 'r') as f:
                    print(f"📝 File contents: {f.read()}")
            else:
                print("❌ Script file not found")
        else:
            print(f"❌ Failed: {result.message}")
    
    print("\n🏁 File operations testing completed!")

if __name__ == "__main__":
    # Run the tests
    asyncio.run(test_code_execution())
    asyncio.run(test_error_scenarios())
    asyncio.run(test_file_operations())
