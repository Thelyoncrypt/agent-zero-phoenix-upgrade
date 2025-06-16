#!/usr/bin/env python3
"""
Test script for HybridMemoryTool LLM re-ranking and synthesis functionality.
This script tests various scenarios to validate the tool's performance.
"""

import asyncio
import os
import sys
import json
from pathlib import Path

# Add the project root to Python path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from python.tools.hybrid_memory_tool import HybridMemoryTool

async def test_hybrid_memory_tool():
    """Test the HybridMemoryTool with various scenarios."""
    
    print("🔥 Testing HybridMemoryTool LLM Re-ranking and Synthesis")
    print("=" * 60)
    
    # Initialize the tool
    tool = HybridMemoryTool(
        agent_id="test_agent",
        llm_api_key=os.getenv("OPENAI_API_KEY"),
        llm_model="gpt-4o-mini"
    )
    
    if not tool.llm_client:
        print("❌ ERROR: No OpenAI API key found. Please set OPENAI_API_KEY environment variable.")
        return
    
    # Test scenarios
    test_scenarios = [
        {
            "name": "General Knowledge Query",
            "query": "What is machine learning and how does it work?",
            "description": "Test with a broad technical query"
        },
        {
            "name": "Specific Technical Query", 
            "query": "How do I implement a REST API with authentication in Python?",
            "description": "Test with a specific implementation question"
        },
        {
            "name": "Personal Context Query",
            "query": "What are my recent projects and their status?",
            "description": "Test with personal/contextual information"
        },
        {
            "name": "Complex Multi-part Query",
            "query": "Compare different database types and recommend the best one for a high-traffic web application",
            "description": "Test with complex comparison and recommendation request"
        }
    ]
    
    for i, scenario in enumerate(test_scenarios, 1):
        print(f"\n📋 Test {i}: {scenario['name']}")
        print(f"Description: {scenario['description']}")
        print(f"Query: '{scenario['query']}'")
        print("-" * 50)
        
        try:
            # Execute the hybrid memory search and synthesis
            result = await tool.execute(
                action="search_and_synthesize",
                query=scenario["query"],
                user_id="test_user",
                max_chunks_per_source=5,
                top_n_final=3,
                enable_synthesis=True
            )
            
            if result.success:
                data = result.data
                print(f"✅ SUCCESS: {result.message}")
                print(f"📊 Total chunks found: {data.get('total_chunks_found', 0)}")
                print(f"🎯 Selected chunks: {len(data.get('ranked_and_selected_chunks', []))}")
                print(f"🔍 Sources searched: {', '.join(data.get('sources_searched', []))}")
                print(f"📈 Overall confidence: {data.get('overall_confidence_in_context', 0):.2f}")
                
                # Display synthesized context
                synthesized = data.get('synthesized_context', '')
                if synthesized:
                    print(f"\n📝 Synthesized Context:")
                    print(f"{'─' * 40}")
                    print(synthesized)
                    print(f"{'─' * 40}")
                
                # Display selected chunks summary
                chunks = data.get('ranked_and_selected_chunks', [])
                if chunks:
                    print(f"\n🔗 Selected Chunks Summary:")
                    for j, chunk in enumerate(chunks, 1):
                        relevance = chunk.get('llm_relevance_score', 0)
                        source = chunk.get('source_type', 'Unknown')
                        reason = chunk.get('reason_for_selection', 'No reason provided')
                        content_preview = chunk.get('content', '')[:100] + '...' if len(chunk.get('content', '')) > 100 else chunk.get('content', '')
                        
                        print(f"  {j}. Source: {source} | Relevance: {relevance:.2f}")
                        print(f"     Reason: {reason}")
                        print(f"     Preview: {content_preview}")
                        print()
                
                # Check for any errors in the result
                if 'error' in data:
                    print(f"⚠️  Warning: {data['error']}")
                    
            else:
                print(f"❌ FAILED: {result.message}")
                if hasattr(result, 'error'):
                    print(f"Error: {result.error}")
                    
        except Exception as e:
            print(f"❌ EXCEPTION: {str(e)}")
            import traceback
            traceback.print_exc()
        
        print("\n" + "=" * 60)
    
    print("\n🏁 Testing completed!")

async def test_error_scenarios():
    """Test error handling scenarios."""
    
    print("\n🧪 Testing Error Scenarios")
    print("=" * 40)
    
    tool = HybridMemoryTool(
        agent_id="test_agent",
        llm_api_key=os.getenv("OPENAI_API_KEY"),
        llm_model="gpt-4o-mini"
    )
    
    # Test with empty query
    print("\n1. Testing empty query...")
    result = await tool.execute(action="search_and_synthesize", query="")
    print(f"Result: {'✅ PASS' if not result.success else '❌ FAIL'} - {result.message}")
    
    # Test with invalid action
    print("\n2. Testing invalid action...")
    result = await tool.execute(action="invalid_action", query="test")
    print(f"Result: {'✅ PASS' if not result.success else '❌ FAIL'} - {result.message}")
    
    print("\n🏁 Error scenario testing completed!")

if __name__ == "__main__":
    # Run the tests
    asyncio.run(test_hybrid_memory_tool())
    asyncio.run(test_error_scenarios())
