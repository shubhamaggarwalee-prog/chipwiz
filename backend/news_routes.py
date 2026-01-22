"""
News API Routes
"""
from fastapi import APIRouter, HTTPException, Query, BackgroundTasks
from typing import Optional, List
from datetime import datetime, timezone
import logging
import os

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/news", tags=["News"])


async def get_db():
    from server import db
    return db


@router.get("/")
async def get_news(
    category: Optional[str] = None,
    tag: Optional[str] = None,
    search: Optional[str] = None,
    is_featured: Optional[bool] = None,
    limit: int = Query(default=20, le=50),
    offset: int = 0
):
    """Get news articles with filtering"""
    db = await get_db()
    
    # Build query
    query = {}
    if category:
        query["category"] = category
    if tag:
        query["tags"] = tag
    if is_featured is not None:
        query["is_featured"] = is_featured
    
    if search:
        query["$text"] = {"$search": search}
        articles = await db.news_articles.find(
            query,
            {"_id": 0, "score": {"$meta": "textScore"}}
        ).sort([("score", {"$meta": "textScore"})]).skip(offset).limit(limit).to_list(limit)
    else:
        articles = await db.news_articles.find(
            query,
            {"_id": 0}
        ).sort("published_at", -1).skip(offset).limit(limit).to_list(limit)
    
    return articles


@router.get("/categories")
async def get_news_categories():
    """Get news categories with article counts"""
    db = await get_db()
    
    categories = [
        {"id": "euv", "name": "EUV Lithography", "icon": "sun"},
        {"id": "packaging", "name": "Advanced Packaging", "icon": "package"},
        {"id": "foundry", "name": "Foundries", "icon": "factory"},
        {"id": "materials", "name": "Materials", "icon": "layers"},
        {"id": "design", "name": "Design & EDA", "icon": "cpu"},
        {"id": "ai_chips", "name": "AI Chips", "icon": "brain"},
        {"id": "nodes", "name": "Process Nodes", "icon": "git-branch"},
        {"id": "memory", "name": "Memory", "icon": "database"},
        {"id": "general", "name": "General", "icon": "newspaper"}
    ]
    
    # Get counts per category
    for cat in categories:
        count = await db.news_articles.count_documents({"category": cat["id"]})
        cat["count"] = count
    
    return categories


@router.get("/featured")
async def get_featured_news(limit: int = 5):
    """Get featured/breaking news"""
    db = await get_db()
    
    featured = await db.news_articles.find(
        {"$or": [{"is_featured": True}, {"is_breaking": True}]},
        {"_id": 0}
    ).sort("published_at", -1).limit(limit).to_list(limit)
    
    return featured


@router.get("/daily-brief")
async def get_daily_brief():
    """Get AI-generated daily news brief"""
    from emergentintegrations.llm.chat import LlmChat, UserMessage
    
    db = await get_db()
    llm_key = os.environ.get("EMERGENT_LLM_KEY")
    
    # Get today's top news
    today_start = datetime.now(timezone.utc).replace(hour=0, minute=0, second=0)
    
    articles = await db.news_articles.find(
        {},
        {"_id": 0}
    ).sort("published_at", -1).limit(10).to_list(10)
    
    if not articles:
        return {"brief": "No news available today.", "articles": []}
    
    # Generate brief
    if llm_key:
        try:
            chat = LlmChat(
                api_key=llm_key,
                session_id=f"brief_{datetime.now().strftime('%Y%m%d')}",
                system_message="You are a semiconductor industry analyst. Summarize the day's top news in 3-4 concise paragraphs. Focus on technical significance and industry impact."
            ).with_model("openai", "gpt-5.2")
            
            news_text = "\n".join([f"- {a['title']}: {a['summary']}" for a in articles[:5]])
            
            brief = await chat.send_message(UserMessage(
                text=f"Summarize today's semiconductor news:\n{news_text}"
            ))
        except Exception as e:
            logger.error(f"Brief generation error: {e}")
            brief = "Daily brief generation temporarily unavailable."
    else:
        brief = "Daily brief requires AI configuration."
    
    return {
        "date": datetime.now(timezone.utc).isoformat(),
        "brief": brief,
        "articles": articles[:5]
    }


@router.get("/{article_id}")
async def get_article(article_id: str):
    """Get a single news article"""
    db = await get_db()
    
    article = await db.news_articles.find_one(
        {"article_id": article_id},
        {"_id": 0}
    )
    
    if not article:
        raise HTTPException(status_code=404, detail="Article not found")
    
    return article


@router.post("/scrape")
async def trigger_scrape(background_tasks: BackgroundTasks):
    """Trigger news scraping (admin only)"""
    from news_scraper import scrape_all_news, store_articles
    
    db = await get_db()
    
    async def run_scrape():
        articles = await scrape_all_news()
        stored = await store_articles(db, articles)
        logger.info(f"Scraped and stored {stored} new articles")
    
    background_tasks.add_task(run_scrape)
    
    return {"message": "Scraping started in background"}


@router.get("/search/global")
async def global_search(q: str, limit: int = Query(default=20, le=50)):
    """Global search across news and encyclopedia"""
    db = await get_db()
    
    results = []
    
    # Search news
    news = await db.news_articles.find(
        {"$text": {"$search": q}},
        {"_id": 0, "score": {"$meta": "textScore"}}
    ).sort([("score", {"$meta": "textScore"})]).limit(limit // 2).to_list(limit // 2)
    
    for article in news:
        results.append({
            "type": "news",
            "id": article["article_id"],
            "title": article["title"],
            "excerpt": article["summary"][:150],
            "category": article.get("category"),
            "url": f"/news/{article['article_id']}"
        })
    
    # Search encyclopedia
    topics = await db.encyclopedia_topics.find(
        {"$text": {"$search": q}},
        {"_id": 0, "score": {"$meta": "textScore"}}
    ).sort([("score", {"$meta": "textScore"})]).limit(limit // 2).to_list(limit // 2)
    
    for topic in topics:
        results.append({
            "type": "encyclopedia",
            "id": topic["topic_id"],
            "title": topic["title"],
            "excerpt": topic["overview"][:150],
            "category": topic.get("category_id"),
            "url": f"/encyclopedia/{topic['slug']}"
        })
    
    return results
