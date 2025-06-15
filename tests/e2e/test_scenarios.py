"""
Predefined test scenarios for Agent Zero E2E testing.

This module contains comprehensive test scenarios covering all major features
of the Agent Zero Phoenix upgrade.
"""

from tests.e2e.test_framework import TestScenario

# Scenario 1: Full RAG Pipeline Test
RAG_PIPELINE_TEST = TestScenario(
    name="rag_pipeline_test",
    description="Test complete RAG pipeline from web crawling to knowledge retrieval",
    setup_actions=[
        {
            "type": "tool_call",
            "tool": "knowledge_agent_tool",
            "args": {
                "action": "setup_database",
                "force_recreate": True
            }
        }
    ],
    test_actions=[
        {
            "type": "tool_call",
            "tool": "web_crawler_tool",
            "args": {
                "action": "crawl_url",
                "url": "https://docs.python.org/3/library/asyncio.html",
                "max_pages": 3,
                "auto_ingest": True
            }
        },
        {
            "type": "wait",
            "seconds": 5
        },
        {
            "type": "tool_call",
            "tool": "knowledge_agent_tool",
            "args": {
                "action": "search",
                "query": "asyncio event loop",
                "limit": 5
            }
        },
        {
            "type": "tool_call",
            "tool": "knowledge_agent_tool",
            "args": {
                "action": "generate_answer",
                "query": "How do you create an asyncio event loop?",
                "context_limit": 3
            }
        }
    ],
    expected_outcomes=[
        {
            "type": "event_emitted",
            "event_type": "crawl_progress"
        },
        {
            "type": "event_emitted",
            "event_type": "knowledge_result"
        },
        {
            "type": "tool_response",
            "tool": "knowledge_agent_tool",
            "success": True
        },
        {
            "type": "performance",
            "metric": "total_events",
            "max_value": 50
        }
    ],
    cleanup_actions=[],
    timeout_seconds=300,
    tags=["rag", "crawling", "knowledge", "integration"]
)

# Scenario 2: Browser Automation Test
BROWSER_AUTOMATION_TEST = TestScenario(
    name="browser_automation_test",
    description="Test browser automation with navigation and data extraction",
    setup_actions=[],
    test_actions=[
        {
            "type": "tool_call",
            "tool": "browser_agent_tool",
            "args": {
                "action": "navigate",
                "url": "https://httpbin.org/forms/post"
            }
        },
        {
            "type": "tool_call",
            "tool": "browser_agent_tool",
            "args": {
                "action": "act",
                "instruction": "Fill in the customer name field with 'Test User'"
            }
        },
        {
            "type": "tool_call",
            "tool": "browser_agent_tool",
            "args": {
                "action": "extract",
                "instruction": "Extract all form field labels and their current values",
                "schema": {
                    "type": "object",
                    "properties": {
                        "form_fields": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "label": {"type": "string"},
                                    "value": {"type": "string"}
                                }
                            }
                        }
                    }
                }
            }
        }
    ],
    expected_outcomes=[
        {
            "type": "event_emitted",
            "event_type": "browser_action"
        },
        {
            "type": "tool_response",
            "tool": "browser_agent_tool",
            "success": True
        }
    ],
    cleanup_actions=[
        {
            "type": "tool_call",
            "tool": "browser_agent_tool",
            "args": {
                "action": "close_browser"
            }
        }
    ],
    timeout_seconds=120,
    tags=["browser", "automation", "extraction"]
)

# Scenario 3: Memory System Integration Test
MEMORY_INTEGRATION_TEST = TestScenario(
    name="memory_integration_test",
    description="Test hybrid memory system with both structured and intelligent memory",
    setup_actions=[],
    test_actions=[
        {
            "type": "tool_call",
            "tool": "memory_agent_tool",
            "args": {
                "action": "add",
                "data": "The user prefers dark mode themes and uses Python for development",
                "user_id": "test_user_123"
            }
        },
        {
            "type": "tool_call",
            "tool": "memory_agent_tool",
            "args": {
                "action": "add",
                "data": "The user's favorite programming language is Python and they work on AI projects",
                "user_id": "test_user_123"
            }
        },
        {
            "type": "tool_call",
            "tool": "hybrid_memory_tool",
            "args": {
                "action": "search_and_synthesize",
                "query": "user programming preferences",
                "user_id": "test_user_123",
                "max_chunks_per_source": 3,
                "top_n_final": 5,
                "enable_synthesis": True
            }
        },
        {
            "type": "tool_call",
            "tool": "memory_agent_tool",
            "args": {
                "action": "search",
                "query": "Python development",
                "user_id": "test_user_123"
            }
        }
    ],
    expected_outcomes=[
        {
            "type": "event_emitted",
            "event_type": "memory_update"
        },
        {
            "type": "tool_response",
            "tool": "memory_agent_tool",
            "success": True
        },
        {
            "type": "tool_response",
            "tool": "hybrid_memory_tool",
            "success": True
        }
    ],
    cleanup_actions=[],
    timeout_seconds=60,
    tags=["memory", "hybrid", "search", "synthesis"]
)

# Scenario 4: TTS Streaming Test
TTS_STREAMING_TEST = TestScenario(
    name="tts_streaming_test",
    description="Test text-to-speech with audio streaming capabilities",
    setup_actions=[],
    test_actions=[
        {
            "type": "tool_call",
            "tool": "chatterbox_tts_tool",
            "args": {
                "action": "generate_speech_stream",
                "text": "Hello, this is a test of the audio streaming functionality in Agent Zero.",
                "chunk_size_ms": 500,
                "stream_id": "test_stream_001"
            }
        },
        {
            "type": "wait",
            "seconds": 2
        },
        {
            "type": "tool_call",
            "tool": "chatterbox_tts_tool",
            "args": {
                "action": "generate_speech",
                "text": "This is a regular TTS generation for comparison."
            }
        }
    ],
    expected_outcomes=[
        {
            "type": "event_emitted",
            "event_type": "tts_stream_start"
        },
        {
            "type": "event_emitted",
            "event_type": "audio_chunk"
        },
        {
            "type": "event_emitted",
            "event_type": "tts_stream_end"
        },
        {
            "type": "tool_response",
            "tool": "chatterbox_tts_tool",
            "success": True
        }
    ],
    cleanup_actions=[],
    timeout_seconds=30,
    tags=["tts", "streaming", "audio"]
)

# Scenario 5: Multi-Step Browser Task Test
BROWSER_AGENT_EXECUTE_TEST = TestScenario(
    name="browser_agent_execute_test",
    description="Test complex browser automation with agent_execute",
    setup_actions=[],
    test_actions=[
        {
            "type": "tool_call",
            "tool": "browser_agent_tool",
            "args": {
                "action": "agent_execute",
                "goal": "Navigate to httpbin.org, find the JSON endpoint, and extract the response structure",
                "max_iterations": 5
            }
        }
    ],
    expected_outcomes=[
        {
            "type": "event_emitted",
            "event_type": "browser_action"
        },
        {
            "type": "tool_response",
            "tool": "browser_agent_tool",
            "success": True
        },
        {
            "type": "performance",
            "metric": "tool_call_count",
            "max_value": 10
        }
    ],
    cleanup_actions=[
        {
            "type": "tool_call",
            "tool": "browser_agent_tool",
            "args": {
                "action": "close_browser"
            }
        }
    ],
    timeout_seconds=180,
    tags=["browser", "agent_execute", "complex"]
)

# Scenario 6: Error Handling and Resilience Test
ERROR_HANDLING_TEST = TestScenario(
    name="error_handling_test",
    description="Test error handling and resilience across tools",
    setup_actions=[],
    test_actions=[
        {
            "type": "tool_call",
            "tool": "browser_agent_tool",
            "args": {
                "action": "navigate",
                "url": "https://nonexistent-domain-12345.com"
            }
        },
        {
            "type": "tool_call",
            "tool": "web_crawler_tool",
            "args": {
                "action": "crawl_url",
                "url": "https://invalid-url-format",
                "max_pages": 1
            }
        },
        {
            "type": "tool_call",
            "tool": "knowledge_agent_tool",
            "args": {
                "action": "search",
                "query": "",  # Empty query should be handled gracefully
                "limit": 5
            }
        }
    ],
    expected_outcomes=[
        {
            "type": "event_emitted",
            "event_type": "error_event"
        },
        {
            "type": "tool_response",
            "tool": "browser_agent_tool",
            "success": False
        },
        {
            "type": "tool_response",
            "tool": "web_crawler_tool",
            "success": False
        }
    ],
    cleanup_actions=[],
    timeout_seconds=60,
    tags=["error_handling", "resilience", "validation"]
)

# Scenario 7: Session Management Test
SESSION_MANAGEMENT_TEST = TestScenario(
    name="session_management_test",
    description="Test session management with multiple thread IDs",
    setup_actions=[],
    test_actions=[
        {
            "type": "tool_call",
            "tool": "stream_protocol_tool",
            "args": {
                "action": "start_session",
                "thread_id": "test_thread_001",
                "user_id": "test_user_001"
            }
        },
        {
            "type": "tool_call",
            "tool": "memory_agent_tool",
            "args": {
                "action": "add",
                "data": "User session 1 preferences",
                "user_id": "test_user_001"
            }
        },
        {
            "type": "tool_call",
            "tool": "stream_protocol_tool",
            "args": {
                "action": "start_session",
                "thread_id": "test_thread_002",
                "user_id": "test_user_002"
            }
        },
        {
            "type": "tool_call",
            "tool": "memory_agent_tool",
            "args": {
                "action": "search",
                "query": "preferences",
                "user_id": "test_user_002"  # Should not find user_001's data
            }
        }
    ],
    expected_outcomes=[
        {
            "type": "event_emitted",
            "event_type": "session_start"
        },
        {
            "type": "tool_response",
            "tool": "stream_protocol_tool",
            "success": True
        }
    ],
    cleanup_actions=[
        {
            "type": "tool_call",
            "tool": "stream_protocol_tool",
            "args": {
                "action": "end_session",
                "thread_id": "test_thread_001"
            }
        },
        {
            "type": "tool_call",
            "tool": "stream_protocol_tool",
            "args": {
                "action": "end_session",
                "thread_id": "test_thread_002"
            }
        }
    ],
    timeout_seconds=60,
    tags=["session", "isolation", "multi_user"]
)

# All test scenarios
ALL_SCENARIOS = [
    RAG_PIPELINE_TEST,
    BROWSER_AUTOMATION_TEST,
    MEMORY_INTEGRATION_TEST,
    TTS_STREAMING_TEST,
    BROWSER_AGENT_EXECUTE_TEST,
    ERROR_HANDLING_TEST,
    SESSION_MANAGEMENT_TEST
]

# Scenario groups for selective testing
CORE_SCENARIOS = [RAG_PIPELINE_TEST, MEMORY_INTEGRATION_TEST]
BROWSER_SCENARIOS = [BROWSER_AUTOMATION_TEST, BROWSER_AGENT_EXECUTE_TEST]
STREAMING_SCENARIOS = [TTS_STREAMING_TEST]
RESILIENCE_SCENARIOS = [ERROR_HANDLING_TEST, SESSION_MANAGEMENT_TEST]
