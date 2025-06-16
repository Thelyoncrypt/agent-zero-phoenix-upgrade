#!/usr/bin/env python3
"""
Phoenix Agent System - Health Check Script
Quick verification of system components and configuration.
"""

import os
import sys
import json
import time
import requests
import subprocess
from pathlib import Path
from typing import Dict, List, Tuple

def check_environment_variables() -> Tuple[bool, List[str]]:
    """Check required environment variables."""
    required_vars = [
        "OPENAI_API_KEY",
        "SUPABASE_URL", 
        "SUPABASE_KEY",
        "SUPABASE_SERVICE_ROLE_KEY"
    ]
    
    missing_vars = []
    for var in required_vars:
        if not os.getenv(var):
            missing_vars.append(var)
    
    return len(missing_vars) == 0, missing_vars

def check_backend_api() -> Tuple[bool, str]:
    """Check if backend API is running and responsive."""
    try:
        response = requests.get("http://localhost:8000/health", timeout=10)
        if response.status_code == 200:
            return True, "Backend API is running"
        else:
            return False, f"Backend API returned status {response.status_code}"
    except requests.exceptions.ConnectionError:
        return False, "Backend API not accessible (connection refused)"
    except requests.exceptions.Timeout:
        return False, "Backend API timeout"
    except Exception as e:
        return False, f"Backend API error: {str(e)}"

def check_frontend() -> Tuple[bool, str]:
    """Check if frontend is running."""
    try:
        response = requests.get("http://localhost:5173", timeout=5)
        if response.status_code == 200:
            return True, "Frontend is running"
        else:
            return False, f"Frontend returned status {response.status_code}"
    except requests.exceptions.ConnectionError:
        return False, "Frontend not accessible (run 'npm run dev' in frontend directory)"
    except requests.exceptions.Timeout:
        return False, "Frontend timeout"
    except Exception as e:
        return False, f"Frontend error: {str(e)}"

def check_python_dependencies() -> Tuple[bool, List[str]]:
    """Check if required Python packages are installed."""
    required_packages = [
        "fastapi",
        "uvicorn", 
        "websockets",
        "supabase",
        "openai",
        "requests",
        "beautifulsoup4",
        "selenium",
        "asyncio"
    ]
    
    missing_packages = []
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            missing_packages.append(package)
    
    return len(missing_packages) == 0, missing_packages

def check_nodejs_dependencies() -> Tuple[bool, str]:
    """Check if Node.js and npm are available."""
    try:
        # Check Node.js
        node_result = subprocess.run(["node", "--version"], capture_output=True, text=True, timeout=5)
        if node_result.returncode != 0:
            return False, "Node.js not found"
        
        # Check npm
        npm_result = subprocess.run(["npm", "--version"], capture_output=True, text=True, timeout=5)
        if npm_result.returncode != 0:
            return False, "npm not found"
        
        node_version = node_result.stdout.strip()
        npm_version = npm_result.stdout.strip()
        return True, f"Node.js {node_version}, npm {npm_version}"
        
    except subprocess.TimeoutExpired:
        return False, "Node.js/npm check timeout"
    except FileNotFoundError:
        return False, "Node.js/npm not found in PATH"
    except Exception as e:
        return False, f"Node.js/npm check error: {str(e)}"

def check_database_connection() -> Tuple[bool, str]:
    """Check Supabase database connection."""
    try:
        from supabase import create_client, Client
        
        url = os.getenv("SUPABASE_URL")
        key = os.getenv("SUPABASE_KEY")
        
        if not url or not key:
            return False, "Supabase credentials not configured"
        
        supabase: Client = create_client(url, key)
        
        # Try a simple query
        result = supabase.table("conversations").select("id").limit(1).execute()
        
        return True, "Supabase database connection successful"
        
    except Exception as e:
        return False, f"Supabase connection error: {str(e)}"

def check_work_directory() -> Tuple[bool, str]:
    """Check work directory exists and is writable."""
    work_dir = Path("work_dir")
    
    try:
        # Create directory if it doesn't exist
        work_dir.mkdir(exist_ok=True)
        
        # Test write permissions
        test_file = work_dir / "health_check_test.txt"
        test_file.write_text("test")
        test_file.unlink()
        
        return True, f"Work directory accessible: {work_dir.absolute()}"
        
    except Exception as e:
        return False, f"Work directory error: {str(e)}"

def check_browser_drivers() -> Tuple[bool, str]:
    """Check if browser drivers are available."""
    try:
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options
        
        # Try Chrome driver
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        
        driver = webdriver.Chrome(options=chrome_options)
        driver.quit()
        
        return True, "Chrome WebDriver available"
        
    except Exception as e:
        return False, f"Browser driver error: {str(e)}"

def run_health_check() -> Dict:
    """Run comprehensive health check."""
    print("🏥 Phoenix Agent System - Health Check")
    print("=" * 50)
    
    checks = [
        ("Environment Variables", check_environment_variables),
        ("Python Dependencies", check_python_dependencies),
        ("Node.js/npm", check_nodejs_dependencies),
        ("Work Directory", check_work_directory),
        ("Database Connection", check_database_connection),
        ("Backend API", check_backend_api),
        ("Frontend", check_frontend),
        ("Browser Drivers", check_browser_drivers)
    ]
    
    results = {}
    all_passed = True
    
    for check_name, check_func in checks:
        print(f"\n🔍 Checking {check_name}...")
        
        try:
            result = check_func()
            
            if isinstance(result, tuple) and len(result) == 2:
                passed, message = result
                if isinstance(message, list):
                    # Handle list of missing items
                    if passed:
                        message = "All required items available"
                    else:
                        message = f"Missing: {', '.join(message)}"
            else:
                passed = bool(result)
                message = str(result)
            
            status = "✅ PASS" if passed else "❌ FAIL"
            print(f"   {status}: {message}")
            
            results[check_name] = {
                "passed": passed,
                "message": message
            }
            
            if not passed:
                all_passed = False
                
        except Exception as e:
            print(f"   ❌ ERROR: {str(e)}")
            results[check_name] = {
                "passed": False,
                "message": f"Check failed: {str(e)}"
            }
            all_passed = False
    
    # Summary
    print("\n" + "=" * 50)
    print("📊 Health Check Summary")
    print("=" * 50)
    
    passed_count = sum(1 for r in results.values() if r["passed"])
    total_count = len(results)
    
    print(f"✅ Passed: {passed_count}/{total_count}")
    print(f"❌ Failed: {total_count - passed_count}/{total_count}")
    
    if all_passed:
        print("\n🎉 All checks passed! System is ready for E2E testing.")
    else:
        print("\n⚠️  Some checks failed. Please address the issues before running E2E tests.")
        print("\n🔧 Failed Checks:")
        for check_name, result in results.items():
            if not result["passed"]:
                print(f"   • {check_name}: {result['message']}")
    
    # Recommendations
    print("\n💡 Recommendations:")
    if not results.get("Backend API", {}).get("passed"):
        print("   • Start the backend: python run_ui.py")
    if not results.get("Frontend", {}).get("passed"):
        print("   • Start the frontend: cd frontend && npm run dev")
    if not results.get("Environment Variables", {}).get("passed"):
        print("   • Configure .env file with required API keys")
    if not results.get("Python Dependencies", {}).get("passed"):
        print("   • Install Python dependencies: pip install -r requirements.txt")
    if not results.get("Database Connection", {}).get("passed"):
        print("   • Check Supabase configuration and network connectivity")
    
    return {
        "all_passed": all_passed,
        "results": results,
        "summary": {
            "passed": passed_count,
            "total": total_count,
            "success_rate": (passed_count / total_count) * 100 if total_count > 0 else 0
        }
    }

if __name__ == "__main__":
    try:
        health_results = run_health_check()
        
        # Save results to file
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        results_file = f"health_check_results_{timestamp}.json"
        
        with open(results_file, 'w') as f:
            json.dump(health_results, f, indent=2, default=str)
        
        print(f"\n📄 Results saved to: {results_file}")
        
        # Exit with appropriate code
        sys.exit(0 if health_results["all_passed"] else 1)
        
    except KeyboardInterrupt:
        print("\n⚠️ Health check interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Health check failed: {str(e)}")
        sys.exit(1)
