#!/usr/bin/env python3
"""
End-to-End Testing Framework for Phoenix Agent System
Comprehensive testing of all integrated components and workflows.
"""

import asyncio
import json
import time
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional
import requests
import websocket
import threading

# Add project root to path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

class E2ETestFramework:
    """Comprehensive E2E testing framework for Phoenix system."""
    
    def __init__(self, backend_url: str = "http://localhost:8000", ws_url: str = "ws://localhost:8000/ws"):
        self.backend_url = backend_url
        self.ws_url = ws_url
        self.test_results = []
        self.current_test = None
        self.ws_events = []
        self.ws_connection = None
        self.test_start_time = None
        
    def log(self, message: str, level: str = "INFO"):
        """Log test messages with timestamp."""
        timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
        print(f"[{timestamp}] [{level}] {message}")
        
    def start_test(self, test_name: str, description: str):
        """Start a new test scenario."""
        self.current_test = {
            "name": test_name,
            "description": description,
            "start_time": datetime.now(),
            "status": "RUNNING",
            "events": [],
            "errors": [],
            "performance": {},
            "data_verification": {}
        }
        self.test_start_time = time.time()
        self.ws_events = []
        self.log(f"🧪 STARTING TEST: {test_name}", "TEST")
        self.log(f"📝 Description: {description}")
        
    def end_test(self, status: str = "PASS", notes: str = ""):
        """End the current test scenario."""
        if self.current_test:
            self.current_test["end_time"] = datetime.now()
            self.current_test["duration"] = time.time() - self.test_start_time
            self.current_test["status"] = status
            self.current_test["notes"] = notes
            self.current_test["ws_events"] = self.ws_events.copy()
            self.test_results.append(self.current_test.copy())
            
            duration = self.current_test["duration"]
            self.log(f"🏁 TEST COMPLETED: {self.current_test['name']} - {status} ({duration:.2f}s)", "TEST")
            if notes:
                self.log(f"📋 Notes: {notes}")
                
    def add_error(self, error: str, error_type: str = "ERROR"):
        """Add an error to the current test."""
        if self.current_test:
            self.current_test["errors"].append({
                "type": error_type,
                "message": error,
                "timestamp": datetime.now()
            })
        self.log(f"❌ {error_type}: {error}", "ERROR")
        
    def add_performance_metric(self, metric_name: str, value: float, unit: str = "ms"):
        """Add a performance metric to the current test."""
        if self.current_test:
            self.current_test["performance"][metric_name] = {
                "value": value,
                "unit": unit,
                "timestamp": datetime.now()
            }
        self.log(f"📊 Performance: {metric_name} = {value}{unit}")
        
    def verify_data(self, check_name: str, expected: Any, actual: Any, passed: bool = None):
        """Verify data and record the result."""
        if passed is None:
            passed = expected == actual
            
        if self.current_test:
            self.current_test["data_verification"][check_name] = {
                "expected": expected,
                "actual": actual,
                "passed": passed,
                "timestamp": datetime.now()
            }
            
        status = "✅ PASS" if passed else "❌ FAIL"
        self.log(f"🔍 Data Check: {check_name} - {status}")
        if not passed:
            self.log(f"   Expected: {expected}")
            self.log(f"   Actual: {actual}")
            
    def check_system_status(self) -> bool:
        """Check if all system components are running."""
        self.log("🔧 Checking system status...")
        
        # Check backend API
        try:
            response = requests.get(f"{self.backend_url}/health", timeout=5)
            if response.status_code == 200:
                self.log("✅ Backend API is running")
            else:
                self.add_error(f"Backend API returned status {response.status_code}")
                return False
        except Exception as e:
            self.add_error(f"Backend API not accessible: {str(e)}")
            return False
            
        # Check WebSocket endpoint
        try:
            def on_message(ws, message):
                pass
            def on_error(ws, error):
                pass
            def on_close(ws, close_status_code, close_msg):
                pass
            def on_open(ws):
                ws.close()
                
            ws = websocket.WebSocketApp(self.ws_url,
                                      on_open=on_open,
                                      on_message=on_message,
                                      on_error=on_error,
                                      on_close=on_close)
            
            # Test connection briefly
            ws.run_forever(timeout=5)
            self.log("✅ WebSocket endpoint is accessible")
        except Exception as e:
            self.add_error(f"WebSocket endpoint not accessible: {str(e)}")
            return False
            
        # Check environment variables
        required_env_vars = ["OPENAI_API_KEY", "SUPABASE_URL", "SUPABASE_KEY"]
        for var in required_env_vars:
            if not os.getenv(var):
                self.add_error(f"Missing required environment variable: {var}")
                return False
        self.log("✅ Required environment variables are set")
        
        # Check work directory
        work_dir = Path("work_dir")
        if not work_dir.exists():
            work_dir.mkdir(parents=True, exist_ok=True)
        self.log("✅ Work directory is available")
        
        return True
        
    def connect_websocket(self, user_id: str = "test_user", thread_id: str = "test_thread"):
        """Connect to WebSocket for event monitoring."""
        self.ws_events = []
        
        def on_message(ws, message):
            try:
                event = json.loads(message)
                self.ws_events.append({
                    "timestamp": datetime.now(),
                    "event": event
                })
                self.log(f"📡 WS Event: {event.get('type', 'unknown')}")
            except Exception as e:
                self.add_error(f"Failed to parse WebSocket message: {str(e)}")
                
        def on_error(ws, error):
            self.add_error(f"WebSocket error: {str(error)}")
            
        def on_close(ws, close_status_code, close_msg):
            self.log("🔌 WebSocket connection closed")
            
        def on_open(ws):
            self.log("🔌 WebSocket connection opened")
            # Send initialization message
            init_message = {
                "type": "init",
                "user_id": user_id,
                "thread_id": thread_id
            }
            ws.send(json.dumps(init_message))
            
        ws_url_with_params = f"{self.ws_url}?user_id={user_id}&thread_id={thread_id}"
        self.ws_connection = websocket.WebSocketApp(ws_url_with_params,
                                                  on_open=on_open,
                                                  on_message=on_message,
                                                  on_error=on_error,
                                                  on_close=on_close)
        
        # Start WebSocket in a separate thread
        def run_ws():
            self.ws_connection.run_forever()
            
        ws_thread = threading.Thread(target=run_ws, daemon=True)
        ws_thread.start()
        time.sleep(2)  # Give connection time to establish
        
    def send_user_message(self, message: str, user_id: str = "test_user", thread_id: str = "test_thread"):
        """Send a user message via WebSocket."""
        if not self.ws_connection:
            self.add_error("WebSocket not connected")
            return False
            
        try:
            message_data = {
                "type": "user_message",
                "content": message,
                "user_id": user_id,
                "thread_id": thread_id,
                "timestamp": datetime.now().isoformat()
            }
            self.ws_connection.send(json.dumps(message_data))
            self.log(f"💬 Sent message: {message}")
            return True
        except Exception as e:
            self.add_error(f"Failed to send message: {str(e)}")
            return False
            
    def wait_for_event(self, event_type: str, timeout: float = 30.0) -> Optional[Dict]:
        """Wait for a specific event type."""
        start_time = time.time()
        while time.time() - start_time < timeout:
            for event_data in reversed(self.ws_events):
                event = event_data["event"]
                if event.get("type") == event_type:
                    return event
            time.sleep(0.1)
        return None
        
    def wait_for_events(self, event_types: List[str], timeout: float = 30.0) -> List[Dict]:
        """Wait for multiple event types."""
        found_events = []
        start_time = time.time()
        
        while len(found_events) < len(event_types) and time.time() - start_time < timeout:
            for event_data in self.ws_events:
                event = event_data["event"]
                event_type = event.get("type")
                if event_type in event_types and event not in found_events:
                    found_events.append(event)
            time.sleep(0.1)
            
        return found_events
        
    def disconnect_websocket(self):
        """Disconnect WebSocket."""
        if self.ws_connection:
            self.ws_connection.close()
            self.ws_connection = None
            
    def generate_test_report(self) -> str:
        """Generate a comprehensive test report."""
        report = []
        report.append("# Phoenix Agent System - End-to-End Test Report")
        report.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append("")
        
        # Summary
        total_tests = len(self.test_results)
        passed_tests = len([t for t in self.test_results if t["status"] == "PASS"])
        failed_tests = total_tests - passed_tests
        
        report.append("## Test Summary")
        report.append(f"- **Total Tests**: {total_tests}")
        report.append(f"- **Passed**: {passed_tests}")
        report.append(f"- **Failed**: {failed_tests}")
        report.append(f"- **Success Rate**: {(passed_tests/total_tests*100):.1f}%" if total_tests > 0 else "- **Success Rate**: N/A")
        report.append("")
        
        # Detailed results
        report.append("## Detailed Test Results")
        for i, test in enumerate(self.test_results, 1):
            status_emoji = "✅" if test["status"] == "PASS" else "❌"
            report.append(f"### {i}. {test['name']} {status_emoji}")
            report.append(f"**Description**: {test['description']}")
            report.append(f"**Status**: {test['status']}")
            report.append(f"**Duration**: {test['duration']:.2f}s")
            
            if test.get("notes"):
                report.append(f"**Notes**: {test['notes']}")
                
            if test["errors"]:
                report.append("**Errors**:")
                for error in test["errors"]:
                    report.append(f"- {error['type']}: {error['message']}")
                    
            if test["performance"]:
                report.append("**Performance Metrics**:")
                for metric, data in test["performance"].items():
                    report.append(f"- {metric}: {data['value']}{data['unit']}")
                    
            if test["data_verification"]:
                report.append("**Data Verification**:")
                for check, data in test["data_verification"].items():
                    status = "✅" if data["passed"] else "❌"
                    report.append(f"- {check}: {status}")
                    
            report.append("")
            
        return "\n".join(report)
        
    def save_test_report(self, filename: str = None):
        """Save test report to file."""
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"e2e_test_report_{timestamp}.md"
            
        report_content = self.generate_test_report()
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(report_content)
            
        self.log(f"📄 Test report saved to: {filename}")
        return filename

class E2ETestScenarios:
    """Implementation of specific E2E test scenarios."""

    def __init__(self, framework: E2ETestFramework):
        self.framework = framework

    async def scenario_1_rag_pipeline(self):
        """Scenario 1: Full RAG Pipeline Test"""
        self.framework.start_test(
            "RAG Pipeline Test",
            "Test web crawling, knowledge ingestion, and RAG-based question answering"
        )

        try:
            # Connect WebSocket
            self.framework.connect_websocket()

            # Step 1: Crawl and index content
            test_url = "https://docs.python.org/3/tutorial/introduction.html"
            crawl_message = f"Crawl and index the content from the webpage at {test_url}"

            if not self.framework.send_user_message(crawl_message):
                self.framework.end_test("FAIL", "Failed to send crawl message")
                return

            # Wait for crawl completion events
            expected_events = ["CRAWL_PROGRESS", "TOOL_CALL_START", "TOOL_RESULT"]
            events = self.framework.wait_for_events(expected_events, timeout=60.0)

            if len(events) < 2:
                self.framework.add_error("Did not receive expected crawl events")
                self.framework.end_test("FAIL", "Crawl events missing")
                return

            # Step 2: Ask a specific question
            time.sleep(5)  # Wait for ingestion to complete
            question = "What does the Python tutorial say about using Python as a calculator?"

            if not self.framework.send_user_message(question):
                self.framework.end_test("FAIL", "Failed to send question")
                return

            # Wait for knowledge retrieval and response
            response_event = self.framework.wait_for_event("TEXT_MESSAGE_CONTENT", timeout=30.0)

            if response_event:
                response_content = response_event.get("content", "")
                self.framework.verify_data(
                    "Response contains relevant information",
                    True,
                    "calculator" in response_content.lower() or "python" in response_content.lower()
                )
                self.framework.end_test("PASS", "RAG pipeline completed successfully")
            else:
                self.framework.end_test("FAIL", "No response received to question")

        except Exception as e:
            self.framework.add_error(f"Exception in RAG pipeline test: {str(e)}")
            self.framework.end_test("FAIL", "Exception occurred")
        finally:
            self.framework.disconnect_websocket()

    async def scenario_2_browser_memory(self):
        """Scenario 2: Browser Interaction, Data Extraction, and Memory Storage"""
        self.framework.start_test(
            "Browser & Memory Test",
            "Test browser automation, data extraction, and memory operations"
        )

        try:
            self.framework.connect_websocket()

            # Step 1: Browser data extraction
            browser_message = "Use the browser to go to https://example.com and tell me the page title"

            if not self.framework.send_user_message(browser_message):
                self.framework.end_test("FAIL", "Failed to send browser message")
                return

            # Wait for browser action events
            browser_events = self.framework.wait_for_events(
                ["BROWSER_ACTION_STEP", "TOOL_CALL_START", "TOOL_RESULT"],
                timeout=45.0
            )

            if len(browser_events) < 2:
                self.framework.add_error("Did not receive expected browser events")

            # Step 2: Memory storage
            time.sleep(3)
            memory_message = "Remember that I tested the browser functionality today"

            if not self.framework.send_user_message(memory_message):
                self.framework.end_test("FAIL", "Failed to send memory message")
                return

            memory_event = self.framework.wait_for_event("MEMORY_UPDATE", timeout=20.0)

            # Step 3: Memory retrieval
            time.sleep(3)
            recall_message = "What did I tell you about testing today?"

            if not self.framework.send_user_message(recall_message):
                self.framework.end_test("FAIL", "Failed to send recall message")
                return

            recall_response = self.framework.wait_for_event("TEXT_MESSAGE_CONTENT", timeout=20.0)

            if recall_response:
                response_content = recall_response.get("content", "")
                self.framework.verify_data(
                    "Memory recall contains test information",
                    True,
                    "test" in response_content.lower() or "browser" in response_content.lower()
                )
                self.framework.end_test("PASS", "Browser and memory operations completed")
            else:
                self.framework.end_test("FAIL", "Memory recall failed")

        except Exception as e:
            self.framework.add_error(f"Exception in browser/memory test: {str(e)}")
            self.framework.end_test("FAIL", "Exception occurred")
        finally:
            self.framework.disconnect_websocket()

    async def scenario_3_multi_step_browser(self):
        """Scenario 3: Multi-Step Browser Task with Re-planning"""
        self.framework.start_test(
            "Multi-Step Browser Task",
            "Test complex browser automation with agent_execute and potential re-planning"
        )

        try:
            self.framework.connect_websocket()

            # Complex browser task
            task_message = "Use the browser to search for 'weather London' on Google and tell me what you find"

            if not self.framework.send_user_message(task_message):
                self.framework.end_test("FAIL", "Failed to send task message")
                return

            # Wait for multiple browser action steps
            start_time = time.time()
            browser_steps = []

            while time.time() - start_time < 60.0:
                for event_data in self.framework.ws_events:
                    event = event_data["event"]
                    if event.get("type") == "BROWSER_ACTION_STEP" and event not in browser_steps:
                        browser_steps.append(event)
                        self.framework.log(f"🌐 Browser step: {event.get('action', 'unknown')}")
                time.sleep(1)

                # Check if task is complete
                completion_event = self.framework.wait_for_event("TEXT_MESSAGE_CONTENT", timeout=1.0)
                if completion_event:
                    break

            self.framework.verify_data(
                "Multiple browser steps executed",
                True,
                len(browser_steps) >= 2
            )

            if len(browser_steps) >= 2:
                self.framework.end_test("PASS", f"Multi-step browser task completed with {len(browser_steps)} steps")
            else:
                self.framework.end_test("FAIL", "Insufficient browser steps executed")

        except Exception as e:
            self.framework.add_error(f"Exception in multi-step browser test: {str(e)}")
            self.framework.end_test("FAIL", "Exception occurred")
        finally:
            self.framework.disconnect_websocket()

    async def scenario_4_tts_streaming(self):
        """Scenario 4: TTS Generation and Streaming Playback"""
        self.framework.start_test(
            "TTS Streaming Test",
            "Test text-to-speech generation and audio streaming"
        )

        try:
            self.framework.connect_websocket()

            # Step 1: Get a text response
            question = "Explain what photosynthesis is in one sentence"

            if not self.framework.send_user_message(question):
                self.framework.end_test("FAIL", "Failed to send question")
                return

            text_response = self.framework.wait_for_event("TEXT_MESSAGE_CONTENT", timeout=20.0)

            if not text_response:
                self.framework.end_test("FAIL", "No text response received")
                return

            # Step 2: Request TTS
            time.sleep(2)
            tts_message = "Read your last answer aloud"

            if not self.framework.send_user_message(tts_message):
                self.framework.end_test("FAIL", "Failed to send TTS request")
                return

            # Wait for TTS events
            tts_start = self.framework.wait_for_event("TTS_STREAM_START", timeout=30.0)

            if not tts_start:
                self.framework.end_test("FAIL", "TTS stream did not start")
                return

            # Count audio chunks
            audio_chunks = 0
            start_time = time.time()

            while time.time() - start_time < 30.0:
                chunk_event = self.framework.wait_for_event("AUDIO_CHUNK", timeout=1.0)
                if chunk_event:
                    audio_chunks += 1

                # Check for stream end
                end_event = self.framework.wait_for_event("TTS_STREAM_END", timeout=1.0)
                if end_event:
                    break

            self.framework.verify_data(
                "Audio chunks received",
                True,
                audio_chunks > 0
            )

            if audio_chunks > 0:
                self.framework.end_test("PASS", f"TTS streaming completed with {audio_chunks} audio chunks")
            else:
                self.framework.end_test("FAIL", "No audio chunks received")

        except Exception as e:
            self.framework.add_error(f"Exception in TTS test: {str(e)}")
            self.framework.end_test("FAIL", "Exception occurred")
        finally:
            self.framework.disconnect_websocket()

    async def scenario_5_code_execution(self):
        """Scenario 5: Code Execution with Live Output"""
        self.framework.start_test(
            "Code Execution Test",
            "Test code execution with real-time output streaming"
        )

        try:
            self.framework.connect_websocket()

            # Request code execution
            code_message = "Run this Python code: for i in range(3): import time; print(f'Count: {i}'); time.sleep(0.5)"

            if not self.framework.send_user_message(code_message):
                self.framework.end_test("FAIL", "Failed to send code execution request")
                return

            # Wait for tool call start
            tool_start = self.framework.wait_for_event("TOOL_CALL_START", timeout=20.0)

            if not tool_start or tool_start.get("tool_name") != "code_execution":
                self.framework.end_test("FAIL", "Code execution tool not started")
                return

            # Count output events
            output_events = 0
            start_time = time.time()

            while time.time() - start_time < 30.0:
                output_event = self.framework.wait_for_event("CODE_EXECUTION_OUTPUT", timeout=1.0)
                if output_event:
                    output_events += 1
                    output_content = output_event.get("stdout", "") + output_event.get("stderr", "")
                    self.framework.log(f"📤 Code output: {output_content.strip()}")

                # Check for completion
                result_event = self.framework.wait_for_event("TOOL_RESULT", timeout=1.0)
                if result_event:
                    break

            self.framework.verify_data(
                "Code output events received",
                True,
                output_events > 0
            )

            if output_events > 0:
                self.framework.end_test("PASS", f"Code execution completed with {output_events} output events")
            else:
                self.framework.end_test("FAIL", "No code output events received")

        except Exception as e:
            self.framework.add_error(f"Exception in code execution test: {str(e)}")
            self.framework.end_test("FAIL", "Exception occurred")
        finally:
            self.framework.disconnect_websocket()

    async def scenario_6_settings_chat_management(self):
        """Scenario 6: Settings and Chat Management"""
        self.framework.start_test(
            "Settings & Chat Management",
            "Test settings viewing and chat management operations"
        )

        try:
            self.framework.connect_websocket()

            # Test basic chat functionality
            test_message = "Hello, this is a test message for chat management"

            if not self.framework.send_user_message(test_message):
                self.framework.end_test("FAIL", "Failed to send test message")
                return

            # Wait for response
            response = self.framework.wait_for_event("TEXT_MESSAGE_CONTENT", timeout=15.0)

            if response:
                self.framework.verify_data(
                    "Chat response received",
                    True,
                    True
                )
                self.framework.end_test("PASS", "Basic chat functionality working")
            else:
                self.framework.end_test("FAIL", "No chat response received")

        except Exception as e:
            self.framework.add_error(f"Exception in settings/chat test: {str(e)}")
            self.framework.end_test("FAIL", "Exception occurred")
        finally:
            self.framework.disconnect_websocket()
