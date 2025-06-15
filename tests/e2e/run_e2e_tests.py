#!/usr/bin/env python3
"""
E2E Test Runner for Agent Zero Phoenix Upgrade

This script runs comprehensive end-to-end tests for the upgraded Agent Zero system.
It can run individual scenarios, scenario groups, or all tests.

Usage:
    python run_e2e_tests.py --all                    # Run all scenarios
    python run_e2e_tests.py --core                   # Run core scenarios only
    python run_e2e_tests.py --browser                # Run browser scenarios only
    python run_e2e_tests.py --scenario rag_pipeline_test  # Run specific scenario
    python run_e2e_tests.py --list                   # List all available scenarios
"""

import asyncio
import argparse
import json
import logging
import sys
from pathlib import Path
from typing import List, Optional

# Add project root to path
sys.path.append(str(Path(__file__).parent.parent.parent))

from tests.e2e.test_framework import E2ETestFramework, TestScenario
from tests.e2e.test_scenarios import (
    ALL_SCENARIOS, CORE_SCENARIOS, BROWSER_SCENARIOS, 
    STREAMING_SCENARIOS, RESILIENCE_SCENARIOS
)

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('e2e_test_results.log')
    ]
)

logger = logging.getLogger(__name__)

class E2ETestRunner:
    """Main test runner for E2E scenarios."""
    
    def __init__(self, config_path: Optional[str] = None):
        self.framework = E2ETestFramework(config_path)
        self.results = []
    
    async def run_scenarios(self, scenarios: List[TestScenario], 
                          stop_on_failure: bool = False) -> bool:
        """Run a list of test scenarios."""
        logger.info(f"Starting E2E test run with {len(scenarios)} scenarios")
        
        # Setup test environment
        setup_success = await self.framework.setup_test_environment()
        if not setup_success:
            logger.error("Failed to setup test environment")
            return False
        
        all_passed = True
        
        try:
            for i, scenario in enumerate(scenarios, 1):
                logger.info(f"Running scenario {i}/{len(scenarios)}: {scenario.name}")
                
                result = await self.framework.execute_scenario(scenario)
                self.results.append(result)
                
                if result.success:
                    logger.info(f"✅ {scenario.name} PASSED ({result.execution_time:.2f}s)")
                else:
                    logger.error(f"❌ {scenario.name} FAILED ({result.execution_time:.2f}s)")
                    if result.error_message:
                        logger.error(f"   Error: {result.error_message}")
                    all_passed = False
                    
                    if stop_on_failure:
                        logger.info("Stopping test run due to failure")
                        break
                
                # Brief pause between scenarios
                await asyncio.sleep(1)
        
        finally:
            # Cleanup test environment
            await self.framework.cleanup_test_environment()
        
        return all_passed
    
    def generate_report(self, output_file: Optional[str] = None) -> dict:
        """Generate and optionally save test report."""
        report = self.framework.generate_test_report()
        
        # Add additional summary information
        report["test_run_summary"] = {
            "total_scenarios": len(self.results),
            "passed_scenarios": sum(1 for r in self.results if r.success),
            "failed_scenarios": sum(1 for r in self.results if not r.success),
            "total_execution_time": sum(r.execution_time for r in self.results),
            "scenarios_by_tag": self._group_scenarios_by_tag()
        }
        
        if output_file:
            with open(output_file, 'w') as f:
                json.dump(report, f, indent=2, default=str)
            logger.info(f"Test report saved to {output_file}")
        
        return report
    
    def _group_scenarios_by_tag(self) -> dict:
        """Group test results by scenario tags."""
        tag_groups = {}
        
        for result in self.results:
            # Find the original scenario to get tags
            scenario = next((s for s in ALL_SCENARIOS if s.name == result.scenario_name), None)
            if scenario:
                for tag in scenario.tags:
                    if tag not in tag_groups:
                        tag_groups[tag] = {"total": 0, "passed": 0, "failed": 0}
                    
                    tag_groups[tag]["total"] += 1
                    if result.success:
                        tag_groups[tag]["passed"] += 1
                    else:
                        tag_groups[tag]["failed"] += 1
        
        return tag_groups
    
    def print_summary(self):
        """Print a summary of test results."""
        if not self.results:
            print("No test results to display")
            return
        
        total = len(self.results)
        passed = sum(1 for r in self.results if r.success)
        failed = total - passed
        
        print("\n" + "="*60)
        print("E2E TEST RESULTS SUMMARY")
        print("="*60)
        print(f"Total Scenarios: {total}")
        print(f"Passed: {passed} ({passed/total*100:.1f}%)")
        print(f"Failed: {failed} ({failed/total*100:.1f}%)")
        print(f"Total Execution Time: {sum(r.execution_time for r in self.results):.2f}s")
        
        if failed > 0:
            print(f"\nFailed Scenarios:")
            for result in self.results:
                if not result.success:
                    print(f"  ❌ {result.scenario_name}: {result.error_message or 'Unknown error'}")
        
        print("\nPassed Scenarios:")
        for result in self.results:
            if result.success:
                print(f"  ✅ {result.scenario_name} ({result.execution_time:.2f}s)")
        
        print("="*60)

def list_scenarios():
    """List all available test scenarios."""
    print("\nAvailable Test Scenarios:")
    print("-" * 40)
    
    for scenario in ALL_SCENARIOS:
        tags_str = ", ".join(scenario.tags) if scenario.tags else "no tags"
        print(f"  {scenario.name}")
        print(f"    Description: {scenario.description}")
        print(f"    Tags: {tags_str}")
        print(f"    Timeout: {scenario.timeout_seconds}s")
        print()

async def main():
    """Main entry point for the test runner."""
    parser = argparse.ArgumentParser(description="Agent Zero E2E Test Runner")
    parser.add_argument("--all", action="store_true", help="Run all test scenarios")
    parser.add_argument("--core", action="store_true", help="Run core scenarios only")
    parser.add_argument("--browser", action="store_true", help="Run browser scenarios only")
    parser.add_argument("--streaming", action="store_true", help="Run streaming scenarios only")
    parser.add_argument("--resilience", action="store_true", help="Run resilience scenarios only")
    parser.add_argument("--scenario", type=str, help="Run specific scenario by name")
    parser.add_argument("--list", action="store_true", help="List all available scenarios")
    parser.add_argument("--config", type=str, help="Path to configuration file")
    parser.add_argument("--output", type=str, help="Output file for test report")
    parser.add_argument("--stop-on-failure", action="store_true", help="Stop on first failure")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose logging")
    
    args = parser.parse_args()
    
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
    
    if args.list:
        list_scenarios()
        return
    
    # Determine which scenarios to run
    scenarios_to_run = []
    
    if args.all:
        scenarios_to_run = ALL_SCENARIOS
    elif args.core:
        scenarios_to_run = CORE_SCENARIOS
    elif args.browser:
        scenarios_to_run = BROWSER_SCENARIOS
    elif args.streaming:
        scenarios_to_run = STREAMING_SCENARIOS
    elif args.resilience:
        scenarios_to_run = RESILIENCE_SCENARIOS
    elif args.scenario:
        scenario = next((s for s in ALL_SCENARIOS if s.name == args.scenario), None)
        if scenario:
            scenarios_to_run = [scenario]
        else:
            print(f"Error: Scenario '{args.scenario}' not found")
            list_scenarios()
            return
    else:
        print("Error: No test scenarios specified")
        parser.print_help()
        return
    
    # Run the tests
    runner = E2ETestRunner(args.config)
    
    try:
        success = await runner.run_scenarios(scenarios_to_run, args.stop_on_failure)
        
        # Generate and display results
        report = runner.generate_report(args.output)
        runner.print_summary()
        
        # Exit with appropriate code
        sys.exit(0 if success else 1)
        
    except KeyboardInterrupt:
        logger.info("Test run interrupted by user")
        sys.exit(130)
    except Exception as e:
        logger.error(f"Test run failed with error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(main())
