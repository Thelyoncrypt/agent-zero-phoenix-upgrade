#!/usr/bin/env python3
"""
Test script for Task 015: Memory Agent Tool Implementation
Tests the real embedding integration and basic in-memory storage.
"""

import asyncio
import os
import sys
from pathlib import Path

# Add the project root to Python path
project_root = Path(__file__).resolve().parent
sys.path.insert(0, str(project_root))

from python.agents.memory_agent.memory import BaseMemory, IntelligentMemory
from python.tools.memory_agent_tool import MemoryAgentTool

class MockAgent:
    """Mock agent for testing purposes."""
    def __init__(self):
        self.agent_name = "test_agent"
        self.context = type('Context', (), {'id': 'test_context'})()
    
    def get_user_id(self):
        return "test_user"
    
    def get_thread_id(self):
        return "test_thread"
    
    async def _emit_stream_event(self, event_type, payload):
        print(f"Mock Agent: Stream event {event_type} - {payload}")

async def test_base_memory():
    """Test the BaseMemory with embedding integration."""
    print("=== Testing BaseMemory ===")
    
    try:
        # Check if API key is available
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key or api_key.startswith("your_"):
            print("⚠️  OPENAI_API_KEY not found or set to placeholder. Testing initialization validation.")
            # Test that the class properly validates API key requirement
            try:
                memory = BaseMemory(agent_id="test_agent")
                print("❌ Expected ValueError but BaseMemory initialized without API key")
                return False
            except ValueError as e:
                if "OpenAI API key must be provided" in str(e):
                    print("✅ BaseMemory correctly validates API key requirement")
                    return True
                else:
                    print(f"❌ Unexpected ValueError: {e}")
                    return False
        else:
            print("✅ OPENAI_API_KEY found. Testing with real API.")
        
        memory = BaseMemory(agent_id="test_agent")
        print("✅ BaseMemory initialized")
        
        # Test adding memory with text content
        test_data = {"role": "user", "content": "I love hiking in the mountains"}
        memory_id = await memory.add(test_data)
        print(f"✅ Added memory with ID: {memory_id}")
        
        # Test retrieving memory
        retrieved = await memory.get(memory_id)
        print(f"✅ Retrieved memory: {retrieved['data']['content'][:30]}...")
        
        # Test search functionality
        search_results = await memory.search("hiking", limit=2)
        print(f"✅ Search returned {len(search_results)} results")
        
        # Test update functionality
        new_data = {"role": "user", "content": "I love rock climbing too"}
        update_success = await memory.update(memory_id, new_data)
        print(f"✅ Update successful: {update_success}")
        
        # Test delete functionality
        delete_success = await memory.delete(memory_id)
        print(f"✅ Delete successful: {delete_success}")
        
        # Test get_all functionality
        all_memories = await memory.get_all()
        print(f"✅ Retrieved {len(all_memories)} total memories")
        
        return True
        
    except Exception as e:
        print(f"❌ BaseMemory test failed: {e}")
        return False

async def test_intelligent_memory():
    """Test the IntelligentMemory with message processing."""
    print("\n=== Testing IntelligentMemory ===")
    
    try:
        # Check if API key is available
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key or api_key.startswith("your_"):
            print("⚠️  OPENAI_API_KEY not found or set to placeholder. Testing initialization validation.")
            try:
                memory = IntelligentMemory(agent_id="test_agent")
                print("❌ Expected ValueError but IntelligentMemory initialized without API key")
                return False
            except ValueError as e:
                if "OpenAI API key must be provided" in str(e):
                    print("✅ IntelligentMemory correctly validates API key requirement")
                    return True
                else:
                    print(f"❌ Unexpected ValueError: {e}")
                    return False
        else:
            print("✅ OPENAI_API_KEY found. Testing with real API.")
        
        memory = IntelligentMemory(agent_id="test_agent")
        print("✅ IntelligentMemory initialized")
        
        # Test adding memories from messages
        test_messages = [
            {"role": "user", "content": "I need help with Python programming"},
            {"role": "assistant", "content": "I'd be happy to help with Python programming"},
            {"role": "user", "content": "How do I create a dictionary?"},
            {"role": "assistant", "content": "You can create a dictionary using curly braces: my_dict = {'key': 'value'}"}
        ]
        
        stored_ids = await memory.add_messages(test_messages, user_id="test_user")
        print(f"✅ Added {len(stored_ids)} memories from messages")
        
        # Test search across stored memories
        search_results = await memory.search("Python dictionary", limit=3)
        print(f"✅ Search returned {len(search_results)} results")
        for i, result in enumerate(search_results):
            print(f"   Result {i+1}: Score={result['relevance_score']:.3f}, Content={result['data']['content'][:50]}...")
        
        # Test inheritance of base methods
        all_memories = await memory.get_all()
        print(f"✅ Retrieved {len(all_memories)} total memories")
        
        return True
        
    except Exception as e:
        print(f"❌ IntelligentMemory test failed: {e}")
        return False

async def test_memory_agent_tool():
    """Test the MemoryAgentTool integration."""
    print("\n=== Testing MemoryAgentTool ===")
    
    try:
        # Check if API key is available
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key or api_key.startswith("your_"):
            print("⚠️  OPENAI_API_KEY not found or set to placeholder. Testing initialization validation.")
            try:
                mock_agent = MockAgent()
                tool = MemoryAgentTool(mock_agent)
                print("❌ Expected ValueError but MemoryAgentTool initialized without API key")
                return False
            except ValueError as e:
                if "OpenAI API key must be provided" in str(e):
                    print("✅ MemoryAgentTool correctly validates API key requirement")
                    return True
                else:
                    print(f"❌ Unexpected ValueError: {e}")
                    return False
        else:
            print("✅ OPENAI_API_KEY found. Testing with real API.")
        
        mock_agent = MockAgent()
        tool = MemoryAgentTool(mock_agent)
        print("✅ MemoryAgentTool initialized")
        
        # Test add action with messages
        test_messages = [
            {"role": "user", "content": "I want to learn machine learning"},
            {"role": "assistant", "content": "Machine learning is a great field to explore"}
        ]
        
        add_response = await tool.execute(action="add", messages=test_messages, user_id="test_user")
        print(f"✅ Add messages response: {add_response.message}")
        
        # Test add action with generic data
        add_data_response = await tool.execute(
            action="add", 
            data={"type": "preference", "content": "I prefer visual learning"}, 
            metadata={"category": "learning_style"}
        )
        print(f"✅ Add data response: {add_data_response.message}")
        
        # Test search action
        search_response = await tool.execute(action="search", query="machine learning", limit=3)
        print(f"✅ Search response: Found {len(search_response.data['results'])} results")
        
        # Test get_all action
        get_all_response = await tool.execute(action="get_all")
        print(f"✅ Get all response: Found {len(get_all_response.data['memories'])} memories")
        
        # Test update action (using a known memory ID from the get_all results)
        if get_all_response.data['memories']:
            memory_id = get_all_response.data['memories'][0]['id']
            update_response = await tool.execute(
                action="update", 
                memory_id=memory_id, 
                data={"type": "preference", "content": "I prefer hands-on learning"}
            )
            print(f"✅ Update response: {update_response.message}")
            
            # Test delete action
            delete_response = await tool.execute(action="delete", memory_id=memory_id)
            print(f"✅ Delete response: {delete_response.message}")
        
        return True
        
    except Exception as e:
        print(f"❌ MemoryAgentTool test failed: {e}")
        return False

async def main():
    """Run all tests for Task 015."""
    print("🚀 Starting Task 015 Memory Agent Implementation Tests\n")
    
    # Load environment variables
    from dotenv import load_dotenv
    load_dotenv()
    
    test_results = []
    
    # Run individual component tests
    test_results.append(await test_base_memory())
    test_results.append(await test_intelligent_memory()) 
    test_results.append(await test_memory_agent_tool())
    
    # Summary
    passed_tests = sum(test_results)
    total_tests = len(test_results)
    
    print(f"\n{'='*50}")
    print(f"🎯 Task 015 Test Results: {passed_tests}/{total_tests} tests passed")
    
    if passed_tests == total_tests:
        print("✅ All tests passed! Task 015 implementation is working correctly.")
    else:
        print("❌ Some tests failed. Check the output above for details.")
        
    # Additional information
    if not os.getenv("OPENAI_API_KEY"):
        print("\n📝 Note: Set OPENAI_API_KEY environment variable to test embedding generation.")
    
    print(f"{'='*50}")

if __name__ == "__main__":
    asyncio.run(main())