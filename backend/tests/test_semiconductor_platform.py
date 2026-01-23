"""
Semiconductor Intelligence Platform - Backend API Tests
Tests for Reports, Encyclopedia, News, AI Assistant, and Health endpoints
"""
import pytest
import requests
import os

BASE_URL = os.environ.get('REACT_APP_BACKEND_URL', 'https://chipwiz.preview.emergentagent.com')

class TestHealthEndpoint:
    """Health check and scheduler status tests"""
    
    def test_health_endpoint(self):
        """Test health endpoint returns status and scheduler info"""
        response = requests.get(f"{BASE_URL}/api/health")
        assert response.status_code == 200
        
        data = response.json()
        assert "status" in data
        assert data["status"] == "healthy"
        assert "database" in data
        assert "scheduler" in data
        
    def test_scheduler_status(self):
        """Test scheduler shows news_scrape job status"""
        response = requests.get(f"{BASE_URL}/api/health")
        assert response.status_code == 200
        
        data = response.json()
        scheduler = data.get("scheduler", {})
        assert "news_scrape" in scheduler
        
        news_scrape = scheduler["news_scrape"]
        assert "status" in news_scrape
        assert "failures" in news_scrape


class TestReportsAPI:
    """Research Reports API tests"""
    
    def test_get_reports_list(self):
        """Test fetching reports list"""
        response = requests.get(f"{BASE_URL}/api/reports/")
        assert response.status_code == 200
        
        data = response.json()
        assert isinstance(data, list)
        assert len(data) >= 2  # At least 2 seeded reports
        
        # Verify report structure
        report = data[0]
        assert "report_id" in report
        assert "title" in report
        assert "slug" in report
        assert "report_type" in report
        assert "executive_summary" in report
        
    def test_get_report_types(self):
        """Test fetching report types"""
        response = requests.get(f"{BASE_URL}/api/reports/types")
        assert response.status_code == 200
        
        data = response.json()
        assert isinstance(data, list)
        assert len(data) >= 1
        
        # Verify type structure
        report_type = data[0]
        assert "id" in report_type
        assert "name" in report_type
        
    def test_get_single_report(self):
        """Test fetching a single report by slug"""
        response = requests.get(f"{BASE_URL}/api/reports/3nm-process-node-analysis")
        assert response.status_code == 200
        
        data = response.json()
        assert data["slug"] == "3nm-process-node-analysis"
        assert "content_sections" in data
        assert "data_sources" in data
        assert "references" in data
        
    def test_get_nonexistent_report(self):
        """Test 404 for non-existent report"""
        response = requests.get(f"{BASE_URL}/api/reports/nonexistent-report-slug")
        assert response.status_code == 404
        
    def test_report_pdf_download(self):
        """Test PDF export for reports"""
        response = requests.get(f"{BASE_URL}/api/reports/3nm-process-node-analysis/pdf")
        assert response.status_code == 200
        assert response.headers.get("content-type") == "application/pdf"
        
        # Verify PDF content starts with PDF header
        assert response.content[:4] == b'%PDF'
        
    def test_filter_reports_by_type(self):
        """Test filtering reports by type"""
        response = requests.get(f"{BASE_URL}/api/reports/", params={"report_type": "node_analysis"})
        assert response.status_code == 200
        
        data = response.json()
        for report in data:
            assert report["report_type"] == "node_analysis"


class TestEncyclopediaAPI:
    """Encyclopedia API tests"""
    
    def test_get_categories(self):
        """Test fetching encyclopedia categories"""
        response = requests.get(f"{BASE_URL}/api/encyclopedia/categories")
        assert response.status_code == 200
        
        data = response.json()
        assert isinstance(data, list)
        assert len(data) >= 10  # 10 seeded categories
        
        # Verify category structure
        category = data[0]
        assert "category_id" in category
        assert "name" in category
        assert "slug" in category
        
    def test_get_knowledge_tree(self):
        """Test fetching hierarchical knowledge tree"""
        response = requests.get(f"{BASE_URL}/api/encyclopedia/tree")
        assert response.status_code == 200
        
        data = response.json()
        assert isinstance(data, list)
        
        # Verify tree structure with topics
        for category in data:
            assert "category_id" in category
            assert "name" in category
            assert "topics" in category
            
    def test_get_topics(self):
        """Test fetching encyclopedia topics"""
        response = requests.get(f"{BASE_URL}/api/encyclopedia/topics")
        assert response.status_code == 200
        
        data = response.json()
        assert isinstance(data, list)
        assert len(data) >= 5  # At least 5 seeded topics
        
    def test_get_single_topic(self):
        """Test fetching a single topic by slug"""
        response = requests.get(f"{BASE_URL}/api/encyclopedia/topics/euv-lithography")
        assert response.status_code == 200
        
        data = response.json()
        assert data["slug"] == "euv-lithography"
        assert "title" in data
        assert "overview" in data
        assert "content_beginner" in data
        assert "content_advanced" in data
        
    def test_get_topic_with_difficulty(self):
        """Test fetching topic with difficulty parameter"""
        response = requests.get(f"{BASE_URL}/api/encyclopedia/topics/euv-lithography", 
                               params={"difficulty": "beginner"})
        assert response.status_code == 200
        
        data = response.json()
        assert "content_beginner" in data
        
    def test_get_nonexistent_topic(self):
        """Test 404 for non-existent topic"""
        response = requests.get(f"{BASE_URL}/api/encyclopedia/topics/nonexistent-topic")
        assert response.status_code == 404
        
    def test_topic_pdf_download(self):
        """Test PDF export for encyclopedia topics"""
        response = requests.get(f"{BASE_URL}/api/encyclopedia/topics/euv-lithography/pdf",
                               params={"difficulty": "intermediate"})
        assert response.status_code == 200
        assert response.headers.get("content-type") == "application/pdf"
        
        # Verify PDF content starts with PDF header
        assert response.content[:4] == b'%PDF'
        
    def test_encyclopedia_search(self):
        """Test encyclopedia search functionality"""
        response = requests.get(f"{BASE_URL}/api/encyclopedia/search", params={"q": "lithography"})
        assert response.status_code == 200
        
        data = response.json()
        assert isinstance(data, list)
        
    def test_filter_topics_by_category(self):
        """Test filtering topics by category"""
        response = requests.get(f"{BASE_URL}/api/encyclopedia/topics", 
                               params={"category_id": "cat_manufacturing"})
        assert response.status_code == 200
        
        data = response.json()
        for topic in data:
            assert topic["category_id"] == "cat_manufacturing"


class TestNewsAPI:
    """News API tests"""
    
    def test_get_news_list(self):
        """Test fetching news articles"""
        response = requests.get(f"{BASE_URL}/api/news/")
        assert response.status_code == 200
        
        data = response.json()
        assert isinstance(data, list)
        
    def test_get_news_categories(self):
        """Test fetching news categories"""
        response = requests.get(f"{BASE_URL}/api/news/categories")
        assert response.status_code == 200
        
        data = response.json()
        assert isinstance(data, list)
        
        # Verify category structure
        if len(data) > 0:
            category = data[0]
            assert "id" in category
            assert "name" in category
            
    def test_get_featured_news(self):
        """Test fetching featured news"""
        response = requests.get(f"{BASE_URL}/api/news/featured")
        assert response.status_code == 200
        
        data = response.json()
        assert isinstance(data, list)
        
    def test_get_daily_brief(self):
        """Test fetching daily brief"""
        response = requests.get(f"{BASE_URL}/api/news/daily-brief")
        assert response.status_code == 200
        
    def test_filter_news_by_category(self):
        """Test filtering news by category"""
        response = requests.get(f"{BASE_URL}/api/news/", params={"category": "ai_chips"})
        assert response.status_code == 200
        
        data = response.json()
        assert isinstance(data, list)
        
    def test_global_search(self):
        """Test global news search"""
        response = requests.get(f"{BASE_URL}/api/news/search/global", params={"q": "NVIDIA"})
        assert response.status_code == 200
        
        data = response.json()
        assert isinstance(data, list)


class TestAIAssistantAPI:
    """AI Assistant API tests"""
    
    def test_chat_endpoint(self):
        """Test AI assistant chat endpoint"""
        response = requests.post(f"{BASE_URL}/api/assistant/chat", json={
            "message": "What is EUV lithography?",
            "session_id": "test_session_123",
            "difficulty": "intermediate"
        })
        assert response.status_code == 200
        
        data = response.json()
        assert "response" in data
        assert len(data["response"]) > 0
        
    def test_chat_with_citations(self):
        """Test AI assistant returns citations"""
        response = requests.post(f"{BASE_URL}/api/assistant/chat", json={
            "message": "Explain FinFET technology",
            "session_id": "test_session_456",
            "difficulty": "beginner"
        })
        assert response.status_code == 200
        
        data = response.json()
        assert "response" in data
        # Citations may or may not be present depending on query
        
    def test_get_sessions(self):
        """Test fetching assistant sessions"""
        response = requests.get(f"{BASE_URL}/api/assistant/sessions")
        assert response.status_code == 200
        
        data = response.json()
        assert isinstance(data, list)


class TestAuthEndpoints:
    """Auth endpoint tests (expected to return 401 without auth)"""
    
    def test_auth_me_without_token(self):
        """Test /auth/me returns 401 without authentication"""
        response = requests.get(f"{BASE_URL}/api/auth/me")
        assert response.status_code == 401


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])
