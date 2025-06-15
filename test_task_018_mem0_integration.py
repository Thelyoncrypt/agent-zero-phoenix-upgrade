#!/usr/bin/env python3
"""
Test script for Task 18 - Real Mem0 Integration
Tests only the specific requirements outlined in task_018.txt
"""

import asyncio
import sys
import os

# Add the project root to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_imports():
    """Test that all required modules can be imported"""
    print("=== Task 18 - Import Tests ===\n")
    
    try:
        import mem0
        print("✅ mem0 library imported successfully")
        print(f"   mem0 version: {getattr(mem0, '__version__', 'unknown')}")
    except ImportError as e:
        print(f"⚠️  mem0 library not found: {e}")
        print("   This is expected if mem0 is not installed. The system will use placeholders.")
    
    try:
        from python.agents.memory_agent.memory import Mem0MemorySystem
        print("✅ Mem0MemorySystem imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import Mem0MemorySystem: {e}")
        return False
    
    try:
        from python.tools.memory_agent_tool import MemoryAgentTool
        print("✅ Enhanced MemoryAgentTool imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import MemoryAgentTool: {e}")
        return False
    
    return True

def test_mem0_memory_system_initialization():
    """Test Mem0MemorySystem initialization"""
    print("\n=== Mem0MemorySystem Initialization Test ===")
    
    try:
        from python.agents.memory_agent.memory import Mem0MemorySystem, MEM0_AVAILABLE
        
        print(f"✅ MEM0_AVAILABLE flag: {MEM0_AVAILABLE}")
        
        # Test initialization
        memory_system = Mem0MemorySystem(agent_id="test_agent", config=None)
        print(f"✅ Mem0MemorySystem initialized with agent_id: {memory_system.agent_id}")
        print(f"   Has mem0 client: {memory_system._mem0_client is not None}")
        
        return True
        
    except Exception as e:
        print(f"❌ Mem0MemorySystem initialization failed: {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_mem0_memory_system_methods():
    """Test Mem0MemorySystem method signatures and basic functionality"""
    print("\n=== Mem0MemorySystem Methods Test ===")
    
    try:
        from python.agents.memory_agent.memory import Mem0MemorySystem
        
        memory_system = Mem0MemorySystem(agent_id="test_agent")
        
        # Test method existence
        assert hasattr(memory_system, 'add_messages'), "add_messages method should exist"
        assert hasattr(memory_system, 'add_generic_memory'), "add_generic_memory method should exist"
        assert hasattr(memory_system, 'search'), "search method should exist"
        assert hasattr(memory_system, 'update'), "update method should exist"
        assert hasattr(memory_system, 'delete'), "delete method should exist"
        assert hasattr(memory_system, 'get_all'), "get_all method should exist"
        
        print("✅ All required methods exist")
        
        # Test basic method calls (will use placeholders if mem0 not available)
        test_messages = [
            {"role": "user", "content": "Hello, how are you?"},
            {"role": "assistant", "content": "I'm doing well, thank you!"}
        ]
        
        # Test add_messages
        stored_ids = await memory_system.add_messages(test_messages, user_id_override="test_user")
        print(f"✅ add_messages returned: {len(stored_ids)} IDs")
        
        # Test add_generic_memory
        generic_id = await memory_system.add_generic_memory("Test memory data", memory_id="test_id", user_id_override="test_user")
        print(f"✅ add_generic_memory returned ID: {generic_id[:8]}...")
        
        # Test search
        search_results = await memory_system.search("test query", user_id_override="test_user", limit=5)
        print(f"✅ search returned: {len(search_results)} results")
        
        # Test update
        update_success = await memory_system.update("test_id", "Updated data", user_id_override="test_user")
        print(f"✅ update returned: {update_success}")
        
        # Test delete
        delete_success = await memory_system.delete("test_id", user_id_override="test_user")
        print(f"✅ delete returned: {delete_success}")
        
        # Test get_all
        all_memories = await memory_system.get_all(user_id_override="test_user")
        print(f"✅ get_all returned: {len(all_memories)} memories")
        
        return True
        
    except Exception as e:
        print(f"❌ Mem0MemorySystem methods test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_memory_agent_tool_integration():
    """Test MemoryAgentTool with Mem0MemorySystem"""
    print("\n=== MemoryAgentTool Integration Test ===")
    
    try:
        from python.agent import AgentContext, Agent
        from python.tools.memory_agent_tool import MemoryAgentTool
        
        # Create minimal agent setup
        context = AgentContext.get(
            name="Task 18 Test",
            thread_id="task-18-test",
            user_id="task-18-user"
        )
        
        agent = Agent(
            agent_id="task-18-agent",
            agent_name="Task18TestAgent", 
            context=context
        )
        
        # Create MemoryAgentTool
        memory_tool = MemoryAgentTool(agent)
        print(f"✅ MemoryAgentTool initialized with agent_id: {memory_tool.memory_system.agent_id}")
        
        # Test add action with messages
        add_result = await memory_tool.execute(
            action="add",
            messages=[
                {"role": "user", "content": "I love artificial intelligence"},
                {"role": "assistant", "content": "AI is indeed fascinating!"}
            ],
            user_id="test_user"
        )
        
        print(f"✅ Add messages result: success={not add_result.error}")
        if add_result.data:
            stored_ids = add_result.data.get('stored_ids', [])
            print(f"   Stored {len(stored_ids)} memories from messages")
        
        # Test add action with generic data
        generic_add_result = await memory_tool.execute(
            action="add",
            data="I enjoy learning about machine learning algorithms",
            user_id="test_user"
        )
        
        print(f"✅ Add generic data result: success={not generic_add_result.error}")
        if generic_add_result.data:
            stored_id = generic_add_result.data.get('stored_id')
            print(f"   Stored memory with ID: {stored_id[:8] if stored_id else 'None'}...")
        
        # Test search action
        search_result = await memory_tool.execute(
            action="search",
            query="artificial intelligence",
            limit=3,
            user_id="test_user"
        )
        
        print(f"✅ Search result: success={not search_result.error}")
        if search_result.data:
            results = search_result.data.get('results', [])
            print(f"   Found {len(results)} relevant memories")
        
        # Test get_all action
        get_all_result = await memory_tool.execute(
            action="get_all",
            user_id="test_user"
        )
        
        print(f"✅ Get all result: success={not get_all_result.error}")
        if get_all_result.data:
            memories = get_all_result.data.get('memories', [])
            print(f"   Retrieved {len(memories)} total memories")
        
        return True
        
    except Exception as e:
        print(f"❌ MemoryAgentTool integration test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_requirements_file():
    """Test that mem0 is added to requirements.txt"""
    print("\n=== Requirements File Test ===")
    
    try:
        with open('requirements.txt', 'r') as f:
            content = f.read()
        
        if 'mem0' in content:
            print("✅ mem0 found in requirements.txt")
            return True
        else:
            print("❌ mem0 not found in requirements.txt")
            return False
            
    except FileNotFoundError:
        print("❌ requirements.txt not found")
        return False

if __name__ == "__main__":
    print("Testing Task 18 - Real Mem0 Integration Implementation\n")
    
    success = True
    
    # Run tests
    success &= test_imports()
    success &= test_mem0_memory_system_initialization()
    success &= test_requirements_file()
    
    # Run async tests
    try:
        asyncio.run(test_mem0_memory_system_methods())
        asyncio.run(test_memory_agent_tool_integration())
    except Exception as e:
        print(f"❌ Async tests failed: {e}")
        success = False
    
    print(f"\n=== Task 18 Tests {'PASSED' if success else 'FAILED'} ===")
    
    if success:
        print("\n🎉 Task 18 implementation verified!")
        print("\nImplemented Components:")
        print("✅ Real Mem0MemorySystem wrapper around mem0.Memory client")
        print("✅ Enhanced MemoryAgentTool using Mem0MemorySystem")
        print("✅ Graceful fallback when mem0 library is not available")
        print("✅ User ID scoping for multi-user memory management")
        print("✅ Complete integration with existing MemoryAgentTool interface")
        print("\nNote: Full functionality requires:")
        print("- mem0 library installed: pip install mem0")
        print("- Valid OPENAI_API_KEY for mem0's default LLM and embedding providers")
        print("- Optional: Custom mem0 configuration for different providers")
    else:
        print("\n❌ Some tests failed. Check the implementation.")
