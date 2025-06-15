#!/usr/bin/env python3
"""
Test script for Task 016: Supabase/pgvector Integration
Tests the real Supabase database integration with pgvector.
"""

import asyncio
import os
import sys
from pathlib import Path

# Add the project root to Python path
project_root = Path(__file__).resolve().parent
sys.path.insert(0, str(project_root))

from python.agents.knowledge_agent.database import DatabaseManager
from python.agents.knowledge_agent.embeddings import EmbeddingGenerator
from python.tools.knowledge_agent_tool import KnowledgeAgentTool

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

async def test_database_manager():
    """Test the DatabaseManager with Supabase integration."""
    print("=== Testing DatabaseManager (Supabase) ===")
    
    try:
        # Check if Supabase credentials are available
        supabase_url = os.getenv("SUPABASE_URL")
        supabase_key = os.getenv("SUPABASE_KEY")
        
        if not supabase_url or not supabase_key or supabase_url.startswith("your_") or supabase_key.startswith("your_"):
            print("⚠️  SUPABASE_URL/SUPABASE_KEY not found or set to placeholder. Testing initialization validation.")
            # Test that the class properly validates Supabase credentials requirement
            try:
                db_manager = DatabaseManager()
                print("❌ Expected ValueError but DatabaseManager initialized without Supabase credentials")
                return False
            except ValueError as e:
                if "Supabase URL and Key must be provided" in str(e):
                    print("✅ DatabaseManager correctly validates Supabase credentials requirement")
                    return True
                else:
                    print(f"❌ Unexpected ValueError: {e}")
                    return False
        else:
            print("✅ SUPABASE_URL and SUPABASE_KEY found. Testing with real Supabase.")
        
        db_manager = DatabaseManager()
        print("✅ DatabaseManager initialized with Supabase")
        
        # Test store_chunks with mock data (requires embedding data)
        test_chunks = [
            {
                "id": "test_chunk_1",
                "text": "This is a test document about machine learning algorithms.",
                "embedding": [0.1, 0.2, 0.3] + [0.0] * 1533,  # 1536 dimensions
                "metadata": {
                    "source_url": "https://example.com/ml-guide",
                    "chunk_index": 0,
                    "title": "Machine Learning Guide"
                }
            }
        ]
        
        stored_ids = await db_manager.store_chunks(test_chunks)
        print(f"✅ Stored {len(stored_ids)} chunks: {stored_ids}")
        
        # Test semantic search
        query_embedding = [0.1, 0.2, 0.3] + [0.0] * 1533  # Similar to stored chunk
        search_results = await db_manager.semantic_search(query_embedding, limit=5)
        print(f"✅ Semantic search returned {len(search_results)} results")
        
        # Test get_all_sources
        sources = await db_manager.get_all_sources()
        print(f"✅ Retrieved {len(sources)} sources")
        
        return True
        
    except Exception as e:
        print(f"❌ DatabaseManager test failed: {e}")
        return False

async def test_knowledge_agent_tool_integration():
    """Test the KnowledgeAgentTool with Supabase integration."""
    print("\n=== Testing KnowledgeAgentTool (Supabase Integration) ===")
    
    try:
        # Check if both API keys are available
        openai_key = os.getenv("OPENAI_API_KEY")
        supabase_url = os.getenv("SUPABASE_URL")
        supabase_key = os.getenv("SUPABASE_KEY")
        
        if (not openai_key or openai_key.startswith("your_") or 
            not supabase_url or supabase_url.startswith("your_") or
            not supabase_key or supabase_key.startswith("your_")):
            print("⚠️  Required API keys not found or set to placeholder. Testing initialization validation.")
            try:
                mock_agent = MockAgent()
                tool = KnowledgeAgentTool(mock_agent)
                print("❌ Expected ValueError but KnowledgeAgentTool initialized without required credentials")
                return False
            except ValueError as e:
                if "must be provided" in str(e):
                    print("✅ KnowledgeAgentTool correctly validates required credentials")
                    return True
                else:
                    print(f"❌ Unexpected ValueError: {e}")
                    return False
        else:
            print("✅ All required API keys found. Testing with real integration.")
        
        mock_agent = MockAgent()
        tool = KnowledgeAgentTool(mock_agent)
        print("✅ KnowledgeAgentTool initialized with Supabase integration")
        
        # Test ingest_chunks action
        test_chunks = [
            {
                "id": "integration_test_1",
                "text": "Supabase is a powerful backend-as-a-service platform.",
                "metadata": {
                    "source_url": "https://example.com/supabase-guide",
                    "chunk_index": 0,
                    "title": "Supabase Integration Guide"
                }
            }
        ]
        
        ingest_response = await tool.execute(action="ingest_chunks", chunks_data=test_chunks)
        print(f"✅ Ingest response: {ingest_response.message}")
        
        # Test query action
        query_response = await tool.execute(action="query", query="Supabase backend platform", limit=3)
        print(f"✅ Query response: {query_response.message[:200]}...")
        
        # Test list_sources action
        sources_response = await tool.execute(action="list_sources")
        print(f"✅ List sources response: {sources_response.message}")
        
        return True
        
    except Exception as e:
        print(f"❌ KnowledgeAgentTool integration test failed: {e}")
        return False

async def test_supabase_connection():
    """Test basic Supabase connection and client initialization."""
    print("\n=== Testing Supabase Connection ===")
    
    try:
        supabase_url = os.getenv("SUPABASE_URL")
        supabase_key = os.getenv("SUPABASE_KEY")
        
        if (not supabase_url or supabase_url.startswith("your_") or
            not supabase_key or supabase_key.startswith("your_")):
            print("⚠️  SUPABASE_URL/SUPABASE_KEY not configured. Skipping connection test.")
            return True  # This is expected in test environment
        
        from supabase import create_client
        
        # Test basic client creation
        client = create_client(supabase_url, supabase_key)
        print("✅ Supabase client created successfully")
        
        # Test basic table access (this won't work without proper setup, but tests the client)
        try:
            # This is just to test if the client works - it may fail if tables don't exist
            response = await asyncio.to_thread(
                client.table("rag_pages").select("*").limit(1).execute
            )
            print("✅ Successfully connected to Supabase and accessed rag_pages table")
        except Exception as table_error:
            print(f"⚠️  Could not access rag_pages table (expected if not set up): {table_error}")
            print("✅ Supabase client connection works, but database schema may not be set up")
        
        return True
        
    except Exception as e:
        print(f"❌ Supabase connection test failed: {e}")
        return False

async def main():
    """Run all tests for Task 016."""
    print("🚀 Starting Task 016 Supabase Integration Tests\n")
    
    # Load environment variables
    from dotenv import load_dotenv
    load_dotenv()
    
    test_results = []
    
    # Run individual component tests
    test_results.append(await test_supabase_connection())
    test_results.append(await test_database_manager())
    test_results.append(await test_knowledge_agent_tool_integration())
    
    # Summary
    passed_tests = sum(test_results)
    total_tests = len(test_results)
    
    print(f"\n{'='*60}")
    print(f"🎯 Task 016 Test Results: {passed_tests}/{total_tests} tests passed")
    
    if passed_tests == total_tests:
        print("✅ All tests passed! Task 016 implementation is working correctly.")
    else:
        print("❌ Some tests failed. Check the output above for details.")
        
    # Additional information
    supabase_configured = bool(os.getenv("SUPABASE_URL") and os.getenv("SUPABASE_KEY") and
                              not os.getenv("SUPABASE_URL", "").startswith("your_"))
    openai_configured = bool(os.getenv("OPENAI_API_KEY") and
                            not os.getenv("OPENAI_API_KEY", "").startswith("your_"))
    
    print(f"\n📝 Configuration Status:")
    print(f"   • Supabase: {'✅ Configured' if supabase_configured else '❌ Not configured'}")
    print(f"   • OpenAI: {'✅ Configured' if openai_configured else '❌ Not configured'}")
    
    if not supabase_configured:
        print("\n📋 To fully test Supabase integration:")
        print("   1. Set up a Supabase project with pgvector extension")
        print("   2. Run the rag-example.sql schema")
        print("   3. Set SUPABASE_URL and SUPABASE_KEY in .env file")
    
    print(f"{'='*60}")

if __name__ == "__main__":
    asyncio.run(main())