#!/usr/bin/env python3
"""
Semiconductor Intelligence Platform - Backend API Testing
Tests all backend endpoints for functionality and integration
"""
import requests
import sys
import json
from datetime import datetime
from typing import Dict, Any, List

class SemiconductorAPITester:
    def __init__(self, base_url="https://chip-knowledge.preview.emergentagent.com"):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({'Content-Type': 'application/json'})
        self.tests_run = 0
        self.tests_passed = 0
        self.failed_tests = []
        self.results = {}

    def log_result(self, test_name: str, success: bool, details: str = "", response_data: Any = None):
        """Log test result"""
        self.tests_run += 1
        if success:
            self.tests_passed += 1
            print(f"✅ {test_name}: PASSED")
        else:
            print(f"❌ {test_name}: FAILED - {details}")
            self.failed_tests.append({
                "test": test_name,
                "error": details,
                "response": response_data
            })
        
        self.results[test_name] = {
            "success": success,
            "details": details,
            "response": response_data
        }

    def test_api_endpoint(self, name: str, method: str, endpoint: str, expected_status: int = 200, 
                         data: Dict = None, params: Dict = None) -> tuple:
        """Test a single API endpoint"""
        url = f"{self.base_url}/api/{endpoint}"
        
        try:
            if method.upper() == 'GET':
                response = self.session.get(url, params=params)
            elif method.upper() == 'POST':
                response = self.session.post(url, json=data, params=params)
            else:
                raise ValueError(f"Unsupported method: {method}")

            success = response.status_code == expected_status
            
            if success:
                try:
                    response_data = response.json()
                except:
                    response_data = response.text
                self.log_result(name, True, f"Status: {response.status_code}", response_data)
                return True, response_data
            else:
                error_msg = f"Expected {expected_status}, got {response.status_code}"
                try:
                    error_data = response.json()
                    error_msg += f" - {error_data}"
                except:
                    error_msg += f" - {response.text[:200]}"
                
                self.log_result(name, False, error_msg, response.text)
                return False, None

        except Exception as e:
            self.log_result(name, False, f"Exception: {str(e)}")
            return False, None

    def test_health_endpoints(self):
        """Test basic health and status endpoints"""
        print("\n🔍 Testing Health Endpoints...")
        
        # Root API endpoint
        self.test_api_endpoint("API Root", "GET", "")
        
        # Health check - should show scheduler status
        success, health_data = self.test_api_endpoint("Health Check", "GET", "health")
        
        # Validate scheduler status in health check
        if success and health_data:
            if 'scheduler' in health_data:
                scheduler_status = health_data['scheduler']
                if isinstance(scheduler_status, dict) and 'news_scrape' in scheduler_status:
                    self.log_result("Scheduler Status Check", True, f"Scheduler running: {scheduler_status['news_scrape'].get('status', 'unknown')}")
                else:
                    self.log_result("Scheduler Status Check", False, "Scheduler status not found in health response")
            else:
                self.log_result("Scheduler Status Check", False, "No scheduler field in health response")

    def test_encyclopedia_endpoints(self):
        """Test encyclopedia API endpoints"""
        print("\n🔍 Testing Encyclopedia Endpoints...")
        
        # Get knowledge tree
        success, tree_data = self.test_api_endpoint("Encyclopedia Tree", "GET", "encyclopedia/tree")
        
        # Validate expanded content - should have 19 topics across 10 categories
        if success and tree_data:
            # Handle both direct list and wrapped response
            tree_list = tree_data if isinstance(tree_data, list) else tree_data.get('data', [])
            total_topics = 0
            categories_count = len(tree_list)
            for category in tree_list:
                total_topics += len(category.get('topics', []))
            
            if total_topics >= 19:
                self.log_result("Encyclopedia Expanded Content", True, f"Found {total_topics} topics across {categories_count} categories")
            else:
                self.log_result("Encyclopedia Expanded Content", False, f"Expected 19+ topics, found {total_topics}")
        
        # Get categories
        success, categories = self.test_api_endpoint("Encyclopedia Categories", "GET", "encyclopedia/categories")
        
        # Get topics
        success, topics = self.test_api_endpoint("Encyclopedia Topics", "GET", "encyclopedia/topics")
        
        # Test topic filtering
        self.test_api_endpoint("Topics by Category", "GET", "encyclopedia/topics", 
                              params={"category_id": "cat_manufacturing"})
        
        self.test_api_endpoint("Topics by Difficulty", "GET", "encyclopedia/topics", 
                              params={"difficulty": "intermediate"})
        
        # Test specific topic
        self.test_api_endpoint("EUV Topic", "GET", "encyclopedia/topics/euv-lithography")
        
        # Test new expanded topics
        new_topics = [
            "duv-lithography", "photoresist-technology", "plasma-etching", 
            "thin-film-deposition", "semiconductor-yield", "chiplet-architecture",
            "hybrid-bonding", "high-bandwidth-memory", "silicon-substrates",
            "silicon-carbide", "gallium-nitride", "2nm-process-node",
            "3nm-process-node", "backside-power-delivery"
        ]
        
        for topic_slug in new_topics[:5]:  # Test first 5 to avoid too many requests
            self.test_api_endpoint(f"New Topic: {topic_slug}", "GET", f"encyclopedia/topics/{topic_slug}")
        
        # Test PDF export for encyclopedia topics
        pdf_url = f"{self.base_url}/api/encyclopedia/topics/euv-lithography/pdf"
        try:
            pdf_response = self.session.get(pdf_url, params={"difficulty": "intermediate"})
            if pdf_response.status_code == 200 and pdf_response.headers.get('content-type') == 'application/pdf':
                self.log_result("Encyclopedia PDF Export", True, f"PDF generated successfully ({len(pdf_response.content)} bytes)")
            else:
                self.log_result("Encyclopedia PDF Export", False, f"Status: {pdf_response.status_code}, Content-Type: {pdf_response.headers.get('content-type')}")
        except Exception as e:
            self.log_result("Encyclopedia PDF Export", False, f"Exception: {str(e)}")
        
        # Test search
        self.test_api_endpoint("Encyclopedia Search", "GET", "encyclopedia/search", 
                              params={"q": "EUV"})

    def test_news_endpoints(self):
        """Test news API endpoints"""
        print("\n🔍 Testing News Endpoints...")
        
        # Get news articles
        self.test_api_endpoint("News Articles", "GET", "news/")
        
        # Get news categories
        self.test_api_endpoint("News Categories", "GET", "news/categories")
        
        # Get featured news
        self.test_api_endpoint("Featured News", "GET", "news/featured")
        
        # Test news filtering
        self.test_api_endpoint("News by Category", "GET", "news/", 
                              params={"category": "euv"})
        
        # Test daily brief
        self.test_api_endpoint("Daily Brief", "GET", "news/daily-brief")
        
        # Test global search
        self.test_api_endpoint("Global Search", "GET", "news/search/global", 
                              params={"q": "semiconductor"})

    def test_ai_assistant_endpoints(self):
        """Test AI assistant endpoints"""
        print("\n🔍 Testing AI Assistant Endpoints...")
        
        # Test chat endpoint (should work without auth for basic queries)
        chat_data = {
            "message": "What is EUV lithography?",
            "difficulty": "intermediate"
        }
        
        success, response = self.test_api_endpoint("AI Chat", "POST", "assistant/chat", 
                                                  expected_status=200, data=chat_data)
        
        if success and response:
            # Validate response structure
            required_fields = ["message_id", "session_id", "response", "citations", "follow_up_questions"]
            missing_fields = [field for field in required_fields if field not in response]
            
            if missing_fields:
                self.log_result("AI Chat Response Structure", False, 
                               f"Missing fields: {missing_fields}")
            else:
                self.log_result("AI Chat Response Structure", True, 
                               "All required fields present")

    def test_reports_endpoints(self):
        """Test reports endpoints"""
        print("\n🔍 Testing Reports Endpoints...")
        
        # Test reports list
        success, reports_data = self.test_api_endpoint("Reports List", "GET", "reports/", expected_status=200)
        
        # Test report types
        self.test_api_endpoint("Report Types", "GET", "reports/types", expected_status=200)
        
        # Test PDF export for reports (if reports exist)
        if success and reports_data and isinstance(reports_data, dict) and reports_data.get('data'):
            reports = reports_data['data']
            if reports and len(reports) > 0:
                first_report_slug = reports[0].get('slug')
                if first_report_slug:
                    # Test PDF download endpoint
                    pdf_url = f"{self.base_url}/api/reports/{first_report_slug}/pdf"
                    try:
                        pdf_response = self.session.get(pdf_url)
                        if pdf_response.status_code == 200 and pdf_response.headers.get('content-type') == 'application/pdf':
                            self.log_result("Report PDF Export", True, f"PDF generated successfully ({len(pdf_response.content)} bytes)")
                        else:
                            self.log_result("Report PDF Export", False, f"Status: {pdf_response.status_code}, Content-Type: {pdf_response.headers.get('content-type')}")
                    except Exception as e:
                        self.log_result("Report PDF Export", False, f"Exception: {str(e)}")
        
        # Test specific report
        self.test_api_endpoint("Specific Report", "GET", "reports/sample-report", expected_status=404)

    def test_auth_endpoints(self):
        """Test authentication endpoints"""
        print("\n🔍 Testing Auth Endpoints...")
        
        # These might return 404 if not implemented, which is expected
        self.test_api_endpoint("Auth Login", "GET", "auth/login", expected_status=404)
        
        # Try POST method
        success, _ = self.test_api_endpoint("Auth Login POST", "POST", "auth/login", 
                                          expected_status=404, data={})

    def test_error_handling(self):
        """Test error handling for invalid requests"""
        print("\n🔍 Testing Error Handling...")
        
        # Test non-existent topic
        self.test_api_endpoint("Non-existent Topic", "GET", "encyclopedia/topics/non-existent-topic", 
                              expected_status=404)
        
        # Test invalid search
        self.test_api_endpoint("Empty Search", "GET", "encyclopedia/search", 
                              params={"q": ""})

    def run_all_tests(self):
        """Run all test suites"""
        print(f"🚀 Starting Semiconductor Intelligence Platform API Tests")
        print(f"📡 Testing against: {self.base_url}")
        print("=" * 60)
        
        try:
            self.test_health_endpoints()
            self.test_encyclopedia_endpoints()
            self.test_news_endpoints()
            self.test_ai_assistant_endpoints()
            self.test_reports_endpoints()
            self.test_auth_endpoints()
            self.test_error_handling()
            
        except KeyboardInterrupt:
            print("\n⚠️ Tests interrupted by user")
        except Exception as e:
            print(f"\n💥 Unexpected error during testing: {e}")
        
        self.print_summary()
        return self.tests_passed == self.tests_run

    def print_summary(self):
        """Print test summary"""
        print("\n" + "=" * 60)
        print("📊 TEST SUMMARY")
        print("=" * 60)
        print(f"Total Tests: {self.tests_run}")
        print(f"Passed: {self.tests_passed}")
        print(f"Failed: {len(self.failed_tests)}")
        print(f"Success Rate: {(self.tests_passed/self.tests_run*100):.1f}%" if self.tests_run > 0 else "0%")
        
        if self.failed_tests:
            print("\n❌ FAILED TESTS:")
            for failure in self.failed_tests:
                print(f"  • {failure['test']}: {failure['error']}")
        
        print("\n🎯 CRITICAL ENDPOINTS STATUS:")
        critical_endpoints = [
            "API Root", "Health Check", "Encyclopedia Tree", 
            "Encyclopedia Topics", "News Articles", "AI Chat"
        ]
        
        for endpoint in critical_endpoints:
            if endpoint in self.results:
                status = "✅" if self.results[endpoint]["success"] else "❌"
                print(f"  {status} {endpoint}")
            else:
                print(f"  ⚪ {endpoint} (not tested)")

def main():
    """Main test execution"""
    tester = SemiconductorAPITester()
    
    try:
        success = tester.run_all_tests()
        return 0 if success else 1
    except Exception as e:
        print(f"💥 Fatal error: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())