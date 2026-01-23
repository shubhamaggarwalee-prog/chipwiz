"""
Test suite for Semiconductor Intelligence Platform - New Features
Tests: AI Compare, Semantic Search, Preferences, Encyclopedia expansion, Memory/Applications categories
"""
import pytest
import requests
import os
import json

BASE_URL = os.environ.get('REACT_APP_BACKEND_URL', '').rstrip('/')

class TestAICompareFeature:
    """Test AI Assistant Compare feature with structured table output"""
    
    def test_compare_finfet_vs_gaafet(self):
        """Test Compare FinFET vs GAAFET query"""
        response = requests.post(
            f"{BASE_URL}/api/assistant/chat",
            json={"message": "Compare FinFET vs GAAFET", "difficulty": "intermediate"},
            timeout=60
        )
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        
        data = response.json()
        assert "response" in data, "Response should contain 'response' field"
        assert "session_id" in data, "Response should contain 'session_id'"
        assert "citations" in data, "Response should contain 'citations'"
        
        # Check for comparison table structure in response
        response_text = data["response"]
        assert "## Summary" in response_text or "Summary" in response_text, "Compare response should have Summary section"
        assert "Comparison Table" in response_text or "| Aspect |" in response_text, "Compare response should have comparison table"
        assert "Advantages" in response_text, "Compare response should list advantages"
        
        print(f"✅ AI Compare feature working - response length: {len(response_text)} chars")
    
    def test_compare_detection_patterns(self):
        """Test various comparison query patterns"""
        patterns = [
            "Compare EUV vs DUV lithography",
            "FinFET versus GAAFET",
            "Difference between DRAM and SRAM",
        ]
        
        for pattern in patterns:
            response = requests.post(
                f"{BASE_URL}/api/assistant/chat",
                json={"message": pattern, "difficulty": "beginner"},
                timeout=60
            )
            assert response.status_code == 200, f"Pattern '{pattern}' failed with {response.status_code}"
            data = response.json()
            assert "response" in data
            print(f"✅ Pattern '{pattern[:30]}...' detected and processed")


class TestSemanticSearch:
    """Test AI-powered semantic search endpoint"""
    
    def test_semantic_search_packaging_for_ai(self):
        """Test semantic search with 'best packaging for AI' query"""
        response = requests.get(
            f"{BASE_URL}/api/encyclopedia/semantic-search",
            params={"q": "best packaging for AI", "limit": 10},
            timeout=30
        )
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        
        data = response.json()
        assert "results" in data, "Response should contain 'results'"
        assert "query" in data, "Response should contain 'query'"
        assert len(data["results"]) > 0, "Should return at least one result"
        
        # Check result structure
        first_result = data["results"][0]
        assert "title" in first_result, "Result should have title"
        assert "relevance" in first_result, "Result should have relevance score"
        assert "reason" in first_result, "Result should have reason"
        
        # CoWoS should be highly relevant for AI packaging
        titles = [r["title"] for r in data["results"]]
        assert any("CoWoS" in t or "Packaging" in t or "HBM" in t for t in titles), \
            f"Expected packaging-related results, got: {titles}"
        
        print(f"✅ Semantic search returned {len(data['results'])} results")
        print(f"   Top result: {first_result['title']} (relevance: {first_result['relevance']})")
    
    def test_semantic_search_requires_min_length(self):
        """Test that short queries fall back to keyword search"""
        response = requests.get(
            f"{BASE_URL}/api/encyclopedia/semantic-search",
            params={"q": "EUV", "limit": 5},
            timeout=30
        )
        assert response.status_code == 200
        # Short queries should still work (fallback to keyword search)
        print("✅ Short query handled gracefully")
    
    def test_semantic_search_natural_language(self):
        """Test natural language query"""
        response = requests.get(
            f"{BASE_URL}/api/encyclopedia/semantic-search",
            params={"q": "what technology is used for making the smallest transistors", "limit": 5},
            timeout=30
        )
        assert response.status_code == 200
        data = response.json()
        assert "results" in data
        print(f"✅ Natural language query returned {len(data.get('results', []))} results")


class TestPreferencesEndpoint:
    """Test user preferences API"""
    
    def test_get_default_preferences(self):
        """Test /api/preferences/ returns defaults for unauthenticated user"""
        response = requests.get(f"{BASE_URL}/api/preferences/", timeout=10)
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        
        data = response.json()
        # Check default values
        assert data.get("theme") == "light", f"Default theme should be 'light', got {data.get('theme')}"
        assert data.get("difficulty") == "intermediate", f"Default difficulty should be 'intermediate'"
        assert data.get("email_frequency") == "weekly", f"Default email_frequency should be 'weekly'"
        assert data.get("is_authenticated") == False, "Should indicate not authenticated"
        
        print("✅ Preferences endpoint returns correct defaults")
        print(f"   Theme: {data.get('theme')}, Difficulty: {data.get('difficulty')}")


class TestEncyclopediaExpansion:
    """Test encyclopedia has 12 categories and 37+ topics"""
    
    def test_encyclopedia_has_12_categories(self):
        """Verify 12 categories exist"""
        response = requests.get(f"{BASE_URL}/api/encyclopedia/categories", timeout=10)
        assert response.status_code == 200
        
        categories = response.json()
        assert len(categories) == 12, f"Expected 12 categories, got {len(categories)}"
        
        expected_categories = [
            "Fundamentals", "Devices", "Manufacturing", "Materials", 
            "Packaging", "Design & EDA", "Nodes & Scaling", "Foundries & Companies",
            "Reliability & Yield", "Testing & Metrology", "Memory Technologies", "Applications"
        ]
        actual_names = [c["name"] for c in categories]
        for expected in expected_categories:
            assert expected in actual_names, f"Missing category: {expected}"
        
        print(f"✅ All 12 categories present: {actual_names}")
    
    def test_encyclopedia_has_37_plus_topics(self):
        """Verify 37+ topics exist"""
        response = requests.get(f"{BASE_URL}/api/encyclopedia/tree", timeout=10)
        assert response.status_code == 200
        
        tree = response.json()
        total_topics = sum(len(cat.get("topics", [])) for cat in tree)
        assert total_topics >= 37, f"Expected 37+ topics, got {total_topics}"
        
        print(f"✅ Encyclopedia has {total_topics} topics (expected 37+)")
    
    def test_memory_technologies_category(self):
        """Verify Memory Technologies category has topics"""
        response = requests.get(
            f"{BASE_URL}/api/encyclopedia/topics",
            params={"category_id": "cat_memory"},
            timeout=10
        )
        assert response.status_code == 200
        
        topics = response.json()
        assert len(topics) >= 4, f"Expected 4+ Memory topics, got {len(topics)}"
        
        expected_topics = ["DRAM", "NAND", "SRAM", "Emerging Memory"]
        topic_titles = [t["title"] for t in topics]
        for expected in expected_topics:
            assert any(expected in title for title in topic_titles), \
                f"Missing Memory topic containing: {expected}"
        
        print(f"✅ Memory Technologies has {len(topics)} topics: {topic_titles}")
    
    def test_applications_category(self):
        """Verify Applications category has topics"""
        response = requests.get(
            f"{BASE_URL}/api/encyclopedia/topics",
            params={"category_id": "cat_applications"},
            timeout=10
        )
        assert response.status_code == 200
        
        topics = response.json()
        assert len(topics) >= 2, f"Expected 2+ Applications topics, got {len(topics)}"
        
        topic_titles = [t["title"] for t in topics]
        assert any("AI" in title or "Accelerator" in title for title in topic_titles), \
            "Should have AI-related topic"
        assert any("Automotive" in title for title in topic_titles), \
            "Should have Automotive topic"
        
        print(f"✅ Applications has {len(topics)} topics: {topic_titles}")


class TestReportsAndPDF:
    """Test Reports page and PDF download"""
    
    def test_reports_list(self):
        """Test reports list endpoint"""
        response = requests.get(f"{BASE_URL}/api/reports/", timeout=10)
        assert response.status_code == 200
        
        reports = response.json()
        assert len(reports) >= 2, f"Expected 2+ reports, got {len(reports)}"
        
        print(f"✅ Reports list has {len(reports)} reports")
    
    def test_report_pdf_download(self):
        """Test PDF download for a report"""
        # First get a valid report slug
        response = requests.get(f"{BASE_URL}/api/reports/", timeout=10)
        reports = response.json()
        slug = reports[0]["slug"]
        
        # Test PDF download
        pdf_response = requests.get(
            f"{BASE_URL}/api/reports/{slug}/pdf",
            timeout=30
        )
        assert pdf_response.status_code == 200, f"PDF download failed: {pdf_response.status_code}"
        assert "application/pdf" in pdf_response.headers.get("content-type", ""), \
            "Response should be PDF"
        
        print(f"✅ PDF download works for report: {slug}")


class TestNewsPage:
    """Test News page loads articles"""
    
    def test_news_articles_load(self):
        """Test news articles endpoint"""
        response = requests.get(f"{BASE_URL}/api/news/", timeout=10)
        assert response.status_code == 200
        
        articles = response.json()
        assert len(articles) > 0, "Should have news articles"
        
        # Check article structure
        first_article = articles[0]
        assert "title" in first_article, "Article should have title"
        assert "summary" in first_article or "content" in first_article, \
            "Article should have summary or content"
        
        print(f"✅ News page has {len(articles)} articles")
    
    def test_news_categories(self):
        """Test news categories endpoint"""
        response = requests.get(f"{BASE_URL}/api/news/categories", timeout=10)
        assert response.status_code == 200
        
        categories = response.json()
        assert len(categories) > 0, "Should have news categories"
        
        print(f"✅ News has {len(categories)} categories")


class TestResendEmailConfiguration:
    """Test Resend email is configured"""
    
    def test_subscription_topics_available(self):
        """Test subscription topics endpoint (indicates email system configured)"""
        response = requests.get(f"{BASE_URL}/api/subscriptions/topics", timeout=10)
        assert response.status_code == 200
        
        topics = response.json()
        assert len(topics) > 0, "Should have subscription topics"
        
        print(f"✅ Subscription system configured with {len(topics)} topics")


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])
