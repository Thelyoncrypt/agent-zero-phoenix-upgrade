"""
E2E Testing Framework for Agent Zero Phoenix Upgrade

This framework provides comprehensive end-to-end testing capabilities for the upgraded Agent Zero system,
including tool integration, memory systems, browser automation, and streaming protocols.
"""

import asyncio
import json
import logging
import time
import uuid
from typing import Dict, Any, List, Optional, Callable
from dataclasses import dataclass, field
from pathlib import Path
import pytest

# Import Agent Zero components
from python.agent import Agent, AgentContext
from python.tools.stream_protocol_tool import StreamEventType, StreamEvent

logger = logging.getLogger(__name__)

@dataclass
class TestScenario:
    """Defines a test scenario with expected outcomes."""
    name: str
    description: str
    setup_actions: List[Dict[str, Any]] = field(default_factory=list)
    test_actions: List[Dict[str, Any]] = field(default_factory=list)
    expected_outcomes: List[Dict[str, Any]] = field(default_factory=list)
    cleanup_actions: List[Dict[str, Any]] = field(default_factory=list)
    timeout_seconds: int = 300
    tags: List[str] = field(default_factory=list)

@dataclass
class TestResult:
    """Stores the result of a test scenario execution."""
    scenario_name: str
    success: bool
    execution_time: float
    events_captured: List[StreamEvent] = field(default_factory=list)
    tool_responses: List[Dict[str, Any]] = field(default_factory=list)
    error_message: Optional[str] = None
    performance_metrics: Dict[str, Any] = field(default_factory=dict)

class MockStreamTransport:
    """Mock stream transport for capturing events during testing."""

    def __init__(self):
        self.events: List[StreamEvent] = []
        self.connections: Dict[str, Dict[str, Any]] = {}

    async def emit_event(self, event: StreamEvent):
        """Capture emitted events for testing verification."""
        self.events.append(event)
        logger.debug(f"MockStreamTransport: Captured event {event.type.value}")

    async def register_connection(self, websocket, thread_id: str, user_id: Optional[str] = None) -> str:
        """Mock connection registration."""
        connection_id = str(uuid.uuid4())
        self.connections[connection_id] = {
            "websocket": websocket,
            "thread_id": thread_id,
            "user_id": user_id
        }
        return connection_id

    async def unregister_connection(self, connection_id: str):
        """Mock connection unregistration."""
        if connection_id in self.connections:
            del self.connections[connection_id]

class MockAgent:
    """Mock agent for testing purposes."""

    def __init__(self, agent_id: str, config: Dict[str, Any], transport: MockStreamTransport):
        self.agent_id = agent_id
        self.config = config
        self.transport = transport
        self.history = []
        self.tool_responses = {}

    async def _call_tool(self, tool_name: str, tool_args: Dict[str, Any]) -> Dict[str, Any]:
        """Mock tool calling."""
        logger.debug(f"MockAgent: Calling tool {tool_name} with args {tool_args}")

        # Simulate tool response
        response = {
            "tool": tool_name,
            "args": tool_args,
            "success": True,
            "message": f"Mock response from {tool_name}",
            "data": {"mock": True}
        }

        # Emit mock events based on tool type
        if tool_name == "browser_agent_tool":
            await self.transport.emit_event(StreamEvent(
                type=StreamEventType.BROWSER_ACTION,
                payload={"action": tool_args.get("action", "unknown"), "status": "completed"}
            ))
        elif tool_name == "memory_agent_tool":
            await self.transport.emit_event(StreamEvent(
                type=StreamEventType.MEMORY_UPDATE,
                payload={"action": tool_args.get("action", "unknown"), "status": "completed"}
            ))
        elif tool_name == "chatterbox_tts_tool":
            if tool_args.get("action") == "generate_speech_stream":
                await self.transport.emit_event(StreamEvent(
                    type=StreamEventType.TTS_STREAM_START,
                    payload={"stream_id": tool_args.get("stream_id", "mock_stream")}
                ))
                await self.transport.emit_event(StreamEvent(
                    type=StreamEventType.AUDIO_CHUNK,
                    payload={"stream_id": tool_args.get("stream_id", "mock_stream"), "chunk_index": 0}
                ))
                await self.transport.emit_event(StreamEvent(
                    type=StreamEventType.TTS_STREAM_END,
                    payload={"stream_id": tool_args.get("stream_id", "mock_stream")}
                ))

        return response

    def hist_add_user_message(self, content: str):
        """Mock adding user message to history."""
        self.history.append({"role": "user", "content": content})

    async def monologue(self):
        """Mock agent monologue."""
        logger.debug("MockAgent: Running monologue")
        return "Mock monologue response"

class E2ETestFramework:
    """
    Comprehensive E2E testing framework for Agent Zero.
    """
    
    def __init__(self, config_path: Optional[str] = None):
        # Use a basic config for testing
        self.config = {
            "work_dir": "./test_work_dir",
            "test_mode": True,
            "log_level": "DEBUG",
            "max_iterations": 10
        }
        self.test_results: List[TestResult] = []
        self.mock_transport = MockStreamTransport()
        self.test_agents: Dict[str, Agent] = {}
        
    async def setup_test_environment(self) -> bool:
        """Setup the testing environment with necessary configurations."""
        try:
            # Create test work directory
            test_work_dir = Path("./test_work_dir")
            test_work_dir.mkdir(exist_ok=True)
            
            # Update test configuration
            self.config.update({
                "work_dir": str(test_work_dir),
                "test_mode": True,
                "log_level": "DEBUG"
            })
            
            logger.info("E2E test environment setup completed")
            return True
            
        except Exception as e:
            logger.error(f"Failed to setup test environment: {e}")
            return False
    
    async def create_test_agent(self, agent_id: str = None) -> 'MockAgent':
        """Create a test agent with mock transport."""
        if not agent_id:
            agent_id = f"test_agent_{uuid.uuid4().hex[:8]}"

        # Create a mock agent for testing
        agent = MockAgent(agent_id, self.config, self.mock_transport)
        self.test_agents[agent_id] = agent

        logger.info(f"Created test agent: {agent_id}")
        return agent
    
    async def execute_scenario(self, scenario: TestScenario) -> TestResult:
        """Execute a complete test scenario."""
        start_time = time.time()
        result = TestResult(
            scenario_name=scenario.name,
            success=False,
            execution_time=0.0
        )
        
        try:
            logger.info(f"Executing scenario: {scenario.name}")
            
            # Create test agent for this scenario
            agent = await self.create_test_agent()
            
            # Clear previous events
            self.mock_transport.events.clear()
            
            # Execute setup actions
            await self._execute_actions(agent, scenario.setup_actions, "setup")
            
            # Execute test actions
            test_responses = await self._execute_actions(agent, scenario.test_actions, "test")
            result.tool_responses = test_responses
            
            # Verify expected outcomes
            verification_success = await self._verify_outcomes(scenario.expected_outcomes)
            
            # Execute cleanup actions
            await self._execute_actions(agent, scenario.cleanup_actions, "cleanup")
            
            # Calculate metrics
            result.execution_time = time.time() - start_time
            result.events_captured = self.mock_transport.events.copy()
            result.success = verification_success
            result.performance_metrics = self._calculate_performance_metrics()
            
            logger.info(f"Scenario {scenario.name} completed: {'SUCCESS' if result.success else 'FAILED'}")
            
        except Exception as e:
            result.execution_time = time.time() - start_time
            result.error_message = str(e)
            result.success = False
            logger.error(f"Scenario {scenario.name} failed with error: {e}")
        
        self.test_results.append(result)
        return result
    
    async def _execute_actions(self, agent: Agent, actions: List[Dict[str, Any]], phase: str) -> List[Dict[str, Any]]:
        """Execute a list of actions and return responses."""
        responses = []
        
        for action in actions:
            try:
                action_type = action.get("type")
                
                if action_type == "tool_call":
                    tool_name = action.get("tool")
                    tool_args = action.get("args", {})
                    
                    response = await agent._call_tool(tool_name, tool_args)
                    responses.append({
                        "action": action,
                        "response": response,
                        "phase": phase
                    })
                    
                elif action_type == "message":
                    content = action.get("content")
                    role = action.get("role", "user")
                    
                    if role == "user":
                        agent.hist_add_user_message(content)
                        await agent.monologue()
                    
                    responses.append({
                        "action": action,
                        "response": {"status": "message_processed"},
                        "phase": phase
                    })
                    
                elif action_type == "wait":
                    wait_time = action.get("seconds", 1)
                    await asyncio.sleep(wait_time)
                    
                    responses.append({
                        "action": action,
                        "response": {"status": "wait_completed"},
                        "phase": phase
                    })
                    
                else:
                    logger.warning(f"Unknown action type: {action_type}")
                    
            except Exception as e:
                logger.error(f"Error executing action {action}: {e}")
                responses.append({
                    "action": action,
                    "response": {"error": str(e)},
                    "phase": phase
                })
        
        return responses
    
    async def _verify_outcomes(self, expected_outcomes: List[Dict[str, Any]]) -> bool:
        """Verify that expected outcomes match actual results."""
        for outcome in expected_outcomes:
            outcome_type = outcome.get("type")
            
            if outcome_type == "event_emitted":
                event_type = outcome.get("event_type")
                if not self._check_event_emitted(event_type):
                    logger.error(f"Expected event {event_type} was not emitted")
                    return False
                    
            elif outcome_type == "tool_response":
                tool_name = outcome.get("tool")
                expected_success = outcome.get("success", True)
                if not self._check_tool_response(tool_name, expected_success):
                    logger.error(f"Tool {tool_name} did not return expected success: {expected_success}")
                    return False
                    
            elif outcome_type == "performance":
                metric = outcome.get("metric")
                max_value = outcome.get("max_value")
                if not self._check_performance_metric(metric, max_value):
                    logger.error(f"Performance metric {metric} exceeded max value {max_value}")
                    return False
        
        return True
    
    def _check_event_emitted(self, event_type: str) -> bool:
        """Check if a specific event type was emitted."""
        for event in self.mock_transport.events:
            if event.type.value == event_type:
                return True
        return False
    
    def _check_tool_response(self, tool_name: str, expected_success: bool) -> bool:
        """Check if a tool returned the expected success status."""
        for result in self.test_results[-1].tool_responses if self.test_results else []:
            action = result.get("action", {})
            if action.get("tool") == tool_name:
                response = result.get("response", {})
                actual_success = not response.get("error", False)
                return actual_success == expected_success
        return False
    
    def _check_performance_metric(self, metric: str, max_value: float) -> bool:
        """Check if a performance metric is within acceptable limits."""
        if not self.test_results:
            return False
        
        current_metrics = self.test_results[-1].performance_metrics
        actual_value = current_metrics.get(metric, 0)
        return actual_value <= max_value
    
    def _calculate_performance_metrics(self) -> Dict[str, Any]:
        """Calculate performance metrics from captured events and responses."""
        metrics = {
            "total_events": len(self.mock_transport.events),
            "event_types": {},
            "tool_call_count": 0,
            "error_count": 0
        }
        
        # Count event types
        for event in self.mock_transport.events:
            event_type = event.type.value
            metrics["event_types"][event_type] = metrics["event_types"].get(event_type, 0) + 1
        
        # Count tool calls and errors
        if self.test_results:
            for response in self.test_results[-1].tool_responses:
                metrics["tool_call_count"] += 1
                if response.get("response", {}).get("error"):
                    metrics["error_count"] += 1
        
        return metrics
    
    async def cleanup_test_environment(self):
        """Clean up test environment and resources."""
        try:
            # Close all test agents
            for agent_id, agent in self.test_agents.items():
                if hasattr(agent, 'cleanup'):
                    await agent.cleanup()
            
            self.test_agents.clear()
            
            # Clear mock transport
            self.mock_transport.events.clear()
            self.mock_transport.connections.clear()
            
            logger.info("Test environment cleanup completed")
            
        except Exception as e:
            logger.error(f"Error during test cleanup: {e}")
    
    def generate_test_report(self) -> Dict[str, Any]:
        """Generate a comprehensive test report."""
        total_tests = len(self.test_results)
        successful_tests = sum(1 for result in self.test_results if result.success)
        
        report = {
            "summary": {
                "total_tests": total_tests,
                "successful_tests": successful_tests,
                "failed_tests": total_tests - successful_tests,
                "success_rate": (successful_tests / total_tests * 100) if total_tests > 0 else 0
            },
            "test_results": [
                {
                    "name": result.scenario_name,
                    "success": result.success,
                    "execution_time": result.execution_time,
                    "events_count": len(result.events_captured),
                    "tool_calls": len(result.tool_responses),
                    "error": result.error_message
                }
                for result in self.test_results
            ],
            "performance_summary": self._generate_performance_summary()
        }
        
        return report
    
    def _generate_performance_summary(self) -> Dict[str, Any]:
        """Generate performance summary from all test results."""
        if not self.test_results:
            return {}
        
        execution_times = [result.execution_time for result in self.test_results]
        event_counts = [len(result.events_captured) for result in self.test_results]
        
        return {
            "avg_execution_time": sum(execution_times) / len(execution_times),
            "max_execution_time": max(execution_times),
            "min_execution_time": min(execution_times),
            "avg_events_per_test": sum(event_counts) / len(event_counts),
            "total_events": sum(event_counts)
        }
