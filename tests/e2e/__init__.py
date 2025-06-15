"""
E2E Testing Package for Agent Zero Phoenix Upgrade

This package provides comprehensive end-to-end testing capabilities for the upgraded Agent Zero system.
It includes test frameworks, predefined scenarios, and utilities for testing all major components.

Key Components:
- test_framework.py: Core testing framework with scenario execution and result tracking
- test_scenarios.py: Predefined test scenarios covering all major features
- run_e2e_tests.py: Main test runner script with CLI interface

Usage:
    from tests.e2e import E2ETestFramework, TestScenario
    from tests.e2e.test_scenarios import ALL_SCENARIOS
    
    # Create framework and run tests
    framework = E2ETestFramework()
    await framework.setup_test_environment()
    
    for scenario in ALL_SCENARIOS:
        result = await framework.execute_scenario(scenario)
        print(f"Scenario {scenario.name}: {'PASSED' if result.success else 'FAILED'}")
"""

from .test_framework import (
    E2ETestFramework,
    TestScenario,
    TestResult,
    MockStreamTransport
)

from .test_scenarios import (
    ALL_SCENARIOS,
    CORE_SCENARIOS,
    BROWSER_SCENARIOS,
    STREAMING_SCENARIOS,
    RESILIENCE_SCENARIOS,
    RAG_PIPELINE_TEST,
    BROWSER_AUTOMATION_TEST,
    MEMORY_INTEGRATION_TEST,
    TTS_STREAMING_TEST,
    BROWSER_AGENT_EXECUTE_TEST,
    ERROR_HANDLING_TEST,
    SESSION_MANAGEMENT_TEST
)

__version__ = "1.0.0"
__author__ = "Agent Zero Development Team"

__all__ = [
    # Framework classes
    "E2ETestFramework",
    "TestScenario", 
    "TestResult",
    "MockStreamTransport",
    
    # Scenario collections
    "ALL_SCENARIOS",
    "CORE_SCENARIOS",
    "BROWSER_SCENARIOS", 
    "STREAMING_SCENARIOS",
    "RESILIENCE_SCENARIOS",
    
    # Individual scenarios
    "RAG_PIPELINE_TEST",
    "BROWSER_AUTOMATION_TEST",
    "MEMORY_INTEGRATION_TEST",
    "TTS_STREAMING_TEST",
    "BROWSER_AGENT_EXECUTE_TEST",
    "ERROR_HANDLING_TEST",
    "SESSION_MANAGEMENT_TEST"
]
