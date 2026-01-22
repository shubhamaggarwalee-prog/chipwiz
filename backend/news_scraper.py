"""
News Scraper Module - Scrapes semiconductor news from allowed public sources
Only uses legally permitted, public, open-access sources.
"""
import asyncio
import aiohttp
from bs4 import BeautifulSoup
from datetime import datetime, timezone, timedelta
import hashlib
import logging
import feedparser
from typing import List, Dict, Any, Optional
import re

logger = logging.getLogger(__name__)

# Allowed public news sources - press releases and official blogs only
NEWS_SOURCES = [
    {
        "name": "Intel Newsroom",
        "url": "https://www.intc.com/news-events/press-releases",
        "type": "press_release",
        "category": "foundry",
        "rss": None
    },
    {
        "name": "TSMC Press",
        "url": "https://pr.tsmc.com/english/news/releases",
        "type": "press_release", 
        "category": "foundry",
        "rss": None
    },
    {
        "name": "Samsung Semiconductor",
        "url": "https://semiconductor.samsung.com/us/news/",
        "type": "press_release",
        "category": "foundry",
        "rss": None
    },
    {
        "name": "NVIDIA Blog",
        "url": "https://blogs.nvidia.com/",
        "type": "blog",
        "category": "ai_chips",
        "rss": "https://blogs.nvidia.com/feed/"
    },
    {
        "name": "AMD Press",
        "url": "https://ir.amd.com/news-events/press-releases",
        "type": "press_release",
        "category": "design",
        "rss": None
    },
    {
        "name": "ASML News",
        "url": "https://www.asml.com/en/news",
        "type": "press_release",
        "category": "euv",
        "rss": None
    },
    {
        "name": "ArXiv Semiconductors",
        "url": "https://arxiv.org/list/cond-mat.mtrl-sci/recent",
        "type": "academic",
        "category": "materials",
        "rss": "https://rss.arxiv.org/rss/cond-mat.mtrl-sci"
    }
]

# Categories for news classification
NEWS_CATEGORIES = {
    "euv": ["euv", "extreme ultraviolet", "lithography", "asml", "high-na"],
    "packaging": ["packaging", "cowos", "chiplet", "2.5d", "3d-ic", "interposer", "tsv"],
    "foundry": ["tsmc", "samsung foundry", "intel foundry", "globalfoundries", "fab", "wafer"],
    "materials": ["silicon", "gan", "sic", "gaas", "compound semiconductor", "substrate"],
    "design": ["eda", "synopsys", "cadence", "arm", "risc-v", "ip core"],
    "ai_chips": ["gpu", "tpu", "npu", "ai accelerator", "nvidia", "inference", "training"],
    "nodes": ["3nm", "2nm", "1.4nm", "a16", "n2", "intel 18a", "process node"],
    "memory": ["dram", "nand", "hbm", "mram", "reram", "storage class memory"]
}


def categorize_article(title: str, content: str) -> str:
    """Categorize article based on keywords"""
    text = (title + " " + content).lower()
    
    scores = {}
    for category, keywords in NEWS_CATEGORIES.items():
        score = sum(1 for kw in keywords if kw in text)
        if score > 0:
            scores[category] = score
    
    if scores:
        return max(scores, key=scores.get)
    return "general"


def extract_tags(title: str, content: str) -> List[str]:
    """Extract relevant tags from article"""
    text = (title + " " + content).lower()
    tags = []
    
    # Company tags
    companies = ["intel", "tsmc", "samsung", "nvidia", "amd", "asml", "qualcomm", "apple", "arm"]
    for company in companies:
        if company in text:
            tags.append(company.upper())
    
    # Technology tags
    techs = ["euv", "gaafet", "finfet", "cowos", "chiplet", "hbm", "ddr5"]
    for tech in techs:
        if tech in text:
            tags.append(tech.upper())
    
    return tags[:5]  # Limit to 5 tags


def generate_article_id(url: str) -> str:
    """Generate unique ID from URL"""
    return f"news_{hashlib.md5(url.encode()).hexdigest()[:12]}"


async def fetch_rss_feed(session: aiohttp.ClientSession, source: Dict) -> List[Dict]:
    """Fetch and parse RSS feed"""
    articles = []
    
    if not source.get("rss"):
        return articles
    
    try:
        async with session.get(source["rss"], timeout=aiohttp.ClientTimeout(total=30)) as response:
            if response.status == 200:
                content = await response.text()
                feed = feedparser.parse(content)
                
                for entry in feed.entries[:10]:  # Limit to 10 per source
                    published = entry.get("published_parsed")
                    if published:
                        pub_date = datetime(*published[:6], tzinfo=timezone.utc)
                    else:
                        pub_date = datetime.now(timezone.utc)
                    
                    summary = entry.get("summary", "")
                    # Clean HTML from summary
                    if summary:
                        soup = BeautifulSoup(summary, "lxml")
                        summary = soup.get_text()[:500]
                    
                    article = {
                        "article_id": generate_article_id(entry.get("link", "")),
                        "title": entry.get("title", "Untitled"),
                        "summary": summary,
                        "content": summary,  # Will be enriched later
                        "source": source["name"],
                        "source_url": entry.get("link", ""),
                        "category": categorize_article(entry.get("title", ""), summary),
                        "tags": extract_tags(entry.get("title", ""), summary),
                        "published_at": pub_date.isoformat(),
                        "scraped_at": datetime.now(timezone.utc).isoformat(),
                        "is_breaking": False,
                        "is_featured": False,
                        "confidence_score": 0.85,
                        "technical_depth": "general"
                    }
                    articles.append(article)
                    
    except Exception as e:
        logger.error(f"Error fetching RSS {source['name']}: {e}")
    
    return articles


async def scrape_news_source(session: aiohttp.ClientSession, source: Dict) -> List[Dict]:
    """Scrape news from a single source"""
    # For RSS feeds, use dedicated handler
    if source.get("rss"):
        return await fetch_rss_feed(session, source)
    
    articles = []
    
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (compatible; SemiNewsBot/1.0; +https://semiconductor-intelligence.com)"
        }
        
        async with session.get(source["url"], headers=headers, timeout=aiohttp.ClientTimeout(total=30)) as response:
            if response.status == 200:
                html = await response.text()
                soup = BeautifulSoup(html, "lxml")
                
                # Generic article extraction - will need customization per source
                # Look for common article patterns
                article_elements = soup.find_all(["article", "div"], class_=re.compile(r"(news|press|article|post)", re.I))[:10]
                
                for elem in article_elements:
                    title_elem = elem.find(["h1", "h2", "h3", "a"])
                    if not title_elem:
                        continue
                    
                    title = title_elem.get_text(strip=True)
                    if len(title) < 10:
                        continue
                    
                    link = title_elem.get("href", "")
                    if not link.startswith("http"):
                        link = source["url"].rstrip("/") + "/" + link.lstrip("/")
                    
                    summary_elem = elem.find(["p", "div"], class_=re.compile(r"(summary|excerpt|desc)", re.I))
                    summary = summary_elem.get_text(strip=True) if summary_elem else ""
                    
                    article = {
                        "article_id": generate_article_id(link),
                        "title": title,
                        "summary": summary[:500],
                        "content": summary,
                        "source": source["name"],
                        "source_url": link,
                        "category": source.get("category", categorize_article(title, summary)),
                        "tags": extract_tags(title, summary),
                        "published_at": datetime.now(timezone.utc).isoformat(),
                        "scraped_at": datetime.now(timezone.utc).isoformat(),
                        "is_breaking": False,
                        "is_featured": False,
                        "confidence_score": 0.8,
                        "technical_depth": "general"
                    }
                    articles.append(article)
                    
    except Exception as e:
        logger.error(f"Error scraping {source['name']}: {e}")
    
    return articles


async def scrape_all_news() -> List[Dict]:
    """Scrape news from all sources"""
    all_articles = []
    
    async with aiohttp.ClientSession() as session:
        tasks = [scrape_news_source(session, source) for source in NEWS_SOURCES]
        results = await asyncio.gather(*tasks, return_exceptions=True)
        
        for result in results:
            if isinstance(result, list):
                all_articles.extend(result)
            elif isinstance(result, Exception):
                logger.error(f"Scraping error: {result}")
    
    # Deduplicate by article_id
    seen = set()
    unique_articles = []
    for article in all_articles:
        if article["article_id"] not in seen:
            seen.add(article["article_id"])
            unique_articles.append(article)
    
    return unique_articles


async def generate_impact_analysis(article: Dict, llm_key: str) -> Dict:
    """Generate AI-powered impact analysis for an article"""
    from emergentintegrations.llm.chat import LlmChat, UserMessage
    
    try:
        chat = LlmChat(
            api_key=llm_key,
            session_id=f"impact_{article['article_id']}",
            system_message="""You are a semiconductor industry analyst. Provide brief, technical analysis of news articles.
            Focus on: technical significance, industry impact, competitive implications.
            Be concise and factual. Cite only public information."""
        ).with_model("openai", "gpt-5.2")
        
        prompt = f"""Analyze this semiconductor news article:

Title: {article['title']}
Summary: {article['summary']}
Source: {article['source']}

Provide:
1. Impact Analysis (2-3 sentences)
2. Why It Matters (1-2 sentences for engineers/analysts)

Format as JSON with keys: impact_analysis, why_it_matters"""

        response = await chat.send_message(UserMessage(text=prompt))
        
        # Parse response
        import json
        try:
            # Try to extract JSON from response
            json_match = re.search(r'\{[^{}]*\}', response, re.DOTALL)
            if json_match:
                analysis = json.loads(json_match.group())
                return {
                    "impact_analysis": analysis.get("impact_analysis", ""),
                    "why_it_matters": analysis.get("why_it_matters", "")
                }
        except:
            pass
        
        return {"impact_analysis": response[:300], "why_it_matters": ""}
        
    except Exception as e:
        logger.error(f"Impact analysis error: {e}")
        return {"impact_analysis": "", "why_it_matters": ""}


async def store_articles(db, articles: List[Dict]) -> int:
    """Store articles in database, avoiding duplicates"""
    stored = 0
    
    for article in articles:
        # Check if already exists
        existing = await db.news_articles.find_one(
            {"article_id": article["article_id"]},
            {"_id": 0}
        )
        
        if not existing:
            await db.news_articles.insert_one(article)
            stored += 1
    
    return stored
