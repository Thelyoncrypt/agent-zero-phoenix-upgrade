#!/usr/bin/env python3
"""
Phoenix Agent System - End-to-End Test Runner
Executes comprehensive E2E tests for all integrated components.
"""

import asyncio
import sys
import os
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from e2e_test_framework import E2ETestFramework, E2ETestScenarios

async def main():
    """Main E2E test execution."""
    
    print("🚀 Phoenix Agent System - End-to-End Testing")
    print("=" * 60)
    
    # Initialize test framework
    framework = E2ETestFramework()
    scenarios = E2ETestScenarios(framework)
    
    # Check system status first
    framework.log("🔧 Performing system status check...")
    if not framework.check_system_status():
        framework.log("❌ System status check failed. Please ensure all components are running.", "ERROR")
        framework.log("Required components:", "INFO")
        framework.log("  - Phoenix backend (run_ui.py)", "INFO")
        framework.log("  - Svelte frontend (npm run dev)", "INFO")
        framework.log("  - Environment variables (.env)", "INFO")
        framework.log("  - Supabase database", "INFO")
        return
    
    framework.log("✅ System status check passed. Starting E2E tests...")
    print()
    
    # Execute all test scenarios
    test_scenarios = [
        ("RAG Pipeline", scenarios.scenario_1_rag_pipeline),
        ("Browser & Memory", scenarios.scenario_2_browser_memory),
        ("Multi-Step Browser", scenarios.scenario_3_multi_step_browser),
        ("TTS Streaming", scenarios.scenario_4_tts_streaming),
        ("Code Execution", scenarios.scenario_5_code_execution),
        ("Settings & Chat", scenarios.scenario_6_settings_chat_management)
    ]
    
    framework.log(f"📋 Executing {len(test_scenarios)} test scenarios...")
    print()
    
    for i, (name, scenario_func) in enumerate(test_scenarios, 1):
        framework.log(f"🧪 [{i}/{len(test_scenarios)}] Starting scenario: {name}")
        try:
            await scenario_func()
        except Exception as e:
            framework.log(f"❌ Scenario {name} failed with exception: {str(e)}", "ERROR")
            framework.add_error(f"Scenario exception: {str(e)}")
        
        # Brief pause between scenarios
        await asyncio.sleep(2)
        print()
    
    # Generate and save test report
    framework.log("📊 Generating test report...")
    report_file = framework.save_test_report()
    
    # Print summary
    total_tests = len(framework.test_results)
    passed_tests = len([t for t in framework.test_results if t["status"] == "PASS"])
    failed_tests = total_tests - passed_tests
    
    print()
    print("🏁 E2E Testing Complete!")
    print("=" * 40)
    print(f"📊 Total Tests: {total_tests}")
    print(f"✅ Passed: {passed_tests}")
    print(f"❌ Failed: {failed_tests}")
    if total_tests > 0:
        success_rate = (passed_tests / total_tests) * 100
        print(f"📈 Success Rate: {success_rate:.1f}%")
    print(f"📄 Report: {report_file}")
    
    # Print failed tests summary
    if failed_tests > 0:
        print()
        print("❌ Failed Tests:")
        for test in framework.test_results:
            if test["status"] == "FAIL":
                print(f"  - {test['name']}: {test.get('notes', 'No details')}")
                if test["errors"]:
                    for error in test["errors"][:3]:  # Show first 3 errors
                        print(f"    • {error['message']}")
    
    # Print recommendations
    print()
    print("🔍 Next Steps:")
    if failed_tests == 0:
        print("  ✅ All tests passed! The Phoenix system is ready for production.")
        print("  🚀 Consider running additional stress tests or user acceptance testing.")
    else:
        print("  🔧 Review failed tests and fix identified issues.")
        print("  🧪 Re-run tests after fixes to ensure stability.")
        print("  📋 Check the detailed report for specific error information.")
    
    print()
    print("📖 For detailed results, see the generated test report.")
    
    return failed_tests == 0

def run_quick_connectivity_test():
    """Run a quick connectivity test to verify basic system availability."""
    print("🔌 Quick Connectivity Test")
    print("-" * 30)
    
    framework = E2ETestFramework()
    
    # Test backend connectivity
    try:
        import requests
        response = requests.get("http://localhost:8000/health", timeout=5)
        if response.status_code == 200:
            print("✅ Backend API: Connected")
        else:
            print(f"❌ Backend API: HTTP {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Backend API: {str(e)}")
        return False
    
    # Test frontend availability
    try:
        response = requests.get("http://localhost:5173", timeout=5)
        if response.status_code == 200:
            print("✅ Frontend: Available")
        else:
            print(f"❌ Frontend: HTTP {response.status_code}")
    except Exception as e:
        print(f"❌ Frontend: {str(e)}")
        print("💡 Make sure to run 'npm run dev' in the frontend directory")
    
    # Test environment variables
    required_vars = ["OPENAI_API_KEY", "SUPABASE_URL", "SUPABASE_KEY"]
    missing_vars = [var for var in required_vars if not os.getenv(var)]
    
    if missing_vars:
        print(f"❌ Environment: Missing {', '.join(missing_vars)}")
        return False
    else:
        print("✅ Environment: Variables set")
    
    print()
    return True

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Phoenix E2E Test Runner")
    parser.add_argument("--quick", action="store_true", help="Run quick connectivity test only")
    parser.add_argument("--scenario", type=str, help="Run specific scenario (1-6)")
    
    args = parser.parse_args()
    
    if args.quick:
        success = run_quick_connectivity_test()
        sys.exit(0 if success else 1)
    
    if args.scenario:
        print(f"🎯 Running specific scenario: {args.scenario}")
        # TODO: Implement specific scenario running
        print("❌ Specific scenario running not yet implemented")
        sys.exit(1)
    
    # Run full E2E test suite
    try:
        success = asyncio.run(main())
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n⚠️ Tests interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Test runner failed: {str(e)}")
        sys.exit(1)
