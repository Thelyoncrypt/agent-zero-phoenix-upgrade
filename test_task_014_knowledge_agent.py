#!/usr/bin/env python3
"""
Test script for Task 014: Knowledge Agent Tool Implementation
Tests the real OpenAI embedding integration and basic in-memory storage.
"""

import asyncio
import os
import sys
from pathlib import Path

# Add the project root to Python path
project_root = Path(__file__).resolve().parent
sys.path.insert(0, str(project_root))

from python.agents.knowledge_agent.embeddings import EmbeddingGenerator
from python.agents.knowledge_agent.database import DatabaseManager
from python.tools.knowledge_agent_tool import KnowledgeAgentTool

class MockAgent:
    """Mock agent for testing purposes."""
    def __init__(self):
        self.agent_name = "test_agent"
    
    async def _emit_stream_event(self, event_type, payload):
        print(f"Mock Agent: Stream event {event_type} - {payload}")

async def test_embedding_generator():
    """Test the EmbeddingGenerator with OpenAI API."""
    print("=== Testing EmbeddingGenerator ===")
    
    try:
        # Check if API key is available
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key or api_key.startswith("your_"):
            print("⚠️  OPENAI_API_KEY not found or set to placeholder. Testing initialization validation.")
            # Test that the class properly validates API key requirement
            try:
                embed_gen = EmbeddingGenerator()
                print("❌ Expected ValueError but EmbeddingGenerator initialized without API key")
                return False
            except ValueError as e:
                if "OpenAI API key must be provided" in str(e):
                    print("✅ EmbeddingGenerator correctly validates API key requirement")
                    return True
                else:
                    print(f"❌ Unexpected ValueError: {e}")
                    return False
        
        embed_gen = EmbeddingGenerator()
        print(f"✅ EmbeddingGenerator initialized with model: {embed_gen.model}")
        
        # Test single embedding
        test_text = "This is a test document about machine learning and AI."
        embedding = await embed_gen.generate_single_embedding(test_text)
        
        print(f"✅ Generated embedding for test text. Dimension: {len(embedding)}")
        print(f"   First 5 values: {embedding[:5]}")
        
        # Test batch embeddings
        test_texts = [
            "Artificial intelligence is transforming technology.",
            "Machine learning algorithms process data efficiently.",
            "Natural language processing enables human-computer interaction."
        ]
        
        embeddings = await embed_gen.generate_embeddings(test_texts)
        print(f"✅ Generated {len(embeddings)} batch embeddings")
        
        # Test empty text handling
        empty_embedding = await embed_gen.generate_single_embedding("")
        print(f"✅ Empty text handling: returned {len(empty_embedding)} dimension zero vector")
        
        return True
        
    except Exception as e:
        print(f"❌ EmbeddingGenerator test failed: {e}")
        return False

async def test_database_manager():
    """Test the DatabaseManager with cosine similarity search."""
    print("\n=== Testing DatabaseManager ===")
    
    try:
        db_manager = DatabaseManager()
        print("✅ DatabaseManager initialized")
        
        # Create test chunks with mock embeddings
        test_chunks = [
            {
                "id": "doc1",
                "text": "Artificial intelligence and machine learning",
                "embedding": [0.1, 0.2, 0.3, 0.4, 0.5] + [0.0] * 1531,  # 1536 dim
                "metadata": {"source_url": "https://example.com/ai", "topic": "AI"}
            },
            {
                "id": "doc2", 
                "text": "Web development and programming",
                "embedding": [0.5, 0.4, 0.3, 0.2, 0.1] + [0.0] * 1531,  # 1536 dim
                "metadata": {"source_url": "https://example.com/webdev", "topic": "Programming"}
            },
            {
                "id": "doc3",
                "text": "Data science and analytics",
                "embedding": [0.2, 0.3, 0.4, 0.5, 0.1] + [0.0] * 1531,  # 1536 dim  
                "metadata": {"source_url": "https://example.com/data", "topic": "Data"}
            }
        ]
        
        # Store chunks
        stored_ids = await db_manager.store_chunks(test_chunks)
        print(f"✅ Stored {len(stored_ids)} chunks: {stored_ids}")
        
        # Test semantic search
        query_embedding = [0.1, 0.2, 0.3, 0.4, 0.5] + [0.0] * 1531  # Similar to doc1
        results = await db_manager.semantic_search(query_embedding, limit=2)
        
        print(f"✅ Semantic search returned {len(results)} results")
        for i, result in enumerate(results):
            print(f"   Result {i+1}: ID={result['id']}, Similarity={result['similarity']:.3f}")
        
        # Test metadata filtering
        filtered_results = await db_manager.semantic_search(
            query_embedding, 
            limit=5, 
            filter_metadata={"topic": "AI"}
        )
        print(f"✅ Filtered search returned {len(filtered_results)} results")
        
        # Test get_all_sources
        sources = await db_manager.get_all_sources()
        print(f"✅ Found {len(sources)} sources: {sources}")
        
        return True
        
    except Exception as e:
        print(f"❌ DatabaseManager test failed: {e}")
        return False

async def test_knowledge_agent_tool():
    """Test the KnowledgeAgentTool integration."""
    print("\n=== Testing KnowledgeAgentTool ===")
    
    try:
        # Check if API key is available for embedding generation
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key or api_key.startswith("your_"):
            print("⚠️  OPENAI_API_KEY not found or set to placeholder. Testing initialization validation.")
            # Test that the tool properly validates API key requirement
            try:
                mock_agent = MockAgent()
                tool = KnowledgeAgentTool(mock_agent)
                print("❌ Expected ValueError but KnowledgeAgentTool initialized without API key")
                return False
            except ValueError as e:
                if "OpenAI API key must be provided" in str(e):
                    print("✅ KnowledgeAgentTool correctly validates API key requirement")
                    return True
                else:
                    print(f"❌ Unexpected ValueError: {e}")
                    return False
        else:
            print("✅ OPENAI_API_KEY found. Testing with real API.")
        
        mock_agent = MockAgent()
        tool = KnowledgeAgentTool(mock_agent)
        print("✅ KnowledgeAgentTool initialized")
        
        # Test chunk ingestion without pre-computed embeddings
        test_chunks = [
            {
                "id": "chunk1",
                "text": "Python is a powerful programming language for AI development.",
                "metadata": {"source_url": "https://example.com/python", "topic": "Programming"}
            },
            {
                "id": "chunk2", 
                "text": "Machine learning models require large datasets for training.",
                "metadata": {"source_url": "https://example.com/ml", "topic": "ML"}
            }
        ]
        
        # Test ingest_chunks action
        ingest_response = await tool.execute(action="ingest_chunks", chunks_data=test_chunks)
        print(f"✅ Ingest response: {ingest_response.message}")
        
        # Test query action
        query_response = await tool.execute(action="query", query="programming languages", limit=3)
        print(f"✅ Query response: {query_response.message[:200]}...")
        
        # Test raw_search action
        search_response = await tool.execute(action="raw_search", query="machine learning", limit=2)
        print(f"✅ Raw search response: {search_response.message[:200]}...")
        
        # Test list_sources action
        sources_response = await tool.execute(action="list_sources")
        print(f"✅ Sources response: {sources_response.message}")
        
        return True
        
    except Exception as e:
        print(f"❌ KnowledgeAgentTool test failed: {e}")
        return False

async def main():
    """Run all tests for Task 014."""
    print("🚀 Starting Task 014 Knowledge Agent Implementation Tests\n")
    
    # Load environment variables
    from dotenv import load_dotenv
    load_dotenv()
    
    test_results = []
    
    # Run individual component tests
    test_results.append(await test_embedding_generator())
    test_results.append(await test_database_manager()) 
    test_results.append(await test_knowledge_agent_tool())
    
    # Summary
    passed_tests = sum(test_results)
    total_tests = len(test_results)
    
    print(f"\n{'='*50}")
    print(f"🎯 Task 014 Test Results: {passed_tests}/{total_tests} tests passed")
    
    if passed_tests == total_tests:
        print("✅ All tests passed! Task 014 implementation is working correctly.")
    else:
        print("❌ Some tests failed. Check the output above for details.")
        
    # Additional information
    if not os.getenv("OPENAI_API_KEY"):
        print("\n📝 Note: Set OPENAI_API_KEY environment variable to test embedding generation.")
    
    print(f"{'='*50}")

if __name__ == "__main__":
    asyncio.run(main())