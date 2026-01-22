"""
Background Job Scheduler - News scraping and report generation
Implements controlled crawl frequency, deduplication, and failure monitoring
"""
import asyncio
import logging
from datetime import datetime, timezone, timedelta
from typing import Dict, List
import os

logger = logging.getLogger(__name__)

# Job status tracking
job_status: Dict[str, dict] = {
    "news_scrape": {
        "last_run": None,
        "last_success": None,
        "failures": 0,
        "articles_scraped": 0,
        "status": "idle"
    }
}

# Configuration
SCRAPE_INTERVAL_HOURS = 6  # Scrape every 6 hours
MAX_FAILURES_BEFORE_ALERT = 3
RETRY_DELAY_MINUTES = 30


async def scrape_news_job(db):
    """
    Scheduled news scraping job with retry logic and monitoring
    """
    from news_scraper import scrape_all_news, store_articles, generate_impact_analysis
    
    job = job_status["news_scrape"]
    job["status"] = "running"
    job["last_run"] = datetime.now(timezone.utc).isoformat()
    
    try:
        logger.info("Starting scheduled news scrape...")
        
        # Scrape news from all sources
        articles = await scrape_all_news()
        logger.info(f"Scraped {len(articles)} articles from sources")
        
        if not articles:
            logger.warning("No articles scraped - sources may be unavailable")
            job["status"] = "completed_empty"
            return
        
        # Deduplicate against existing articles
        new_articles = []
        for article in articles:
            existing = await db.news_articles.find_one(
                {"article_id": article["article_id"]},
                {"_id": 0}
            )
            if not existing:
                new_articles.append(article)
        
        logger.info(f"Found {len(new_articles)} new articles after deduplication")
        
        # Generate impact analysis for new articles (if LLM key available)
        llm_key = os.environ.get("EMERGENT_LLM_KEY")
        if llm_key and new_articles:
            logger.info("Generating impact analysis for new articles...")
            for article in new_articles[:5]:  # Limit to avoid rate limits
                try:
                    analysis = await generate_impact_analysis(article, llm_key)
                    article["impact_analysis"] = analysis.get("impact_analysis", "")
                    article["why_it_matters"] = analysis.get("why_it_matters", "")
                except Exception as e:
                    logger.error(f"Impact analysis failed for {article['article_id']}: {e}")
        
        # Store new articles
        stored = await store_articles(db, new_articles)
        
        # Update job status
        job["last_success"] = datetime.now(timezone.utc).isoformat()
        job["failures"] = 0
        job["articles_scraped"] = stored
        job["status"] = "completed"
        
        logger.info(f"News scrape completed: {stored} new articles stored")
        
    except Exception as e:
        logger.error(f"News scrape job failed: {e}")
        job["failures"] += 1
        job["status"] = "failed"
        job["last_error"] = str(e)
        
        # Alert if too many failures
        if job["failures"] >= MAX_FAILURES_BEFORE_ALERT:
            logger.critical(f"News scrape has failed {job['failures']} times consecutively!")


async def run_scheduler(db):
    """
    Main scheduler loop - runs news scraping at configured intervals
    """
    logger.info(f"Starting scheduler - news scrape every {SCRAPE_INTERVAL_HOURS} hours")
    
    while True:
        try:
            # Check if it's time to scrape
            job = job_status["news_scrape"]
            should_run = False
            
            if job["last_run"] is None:
                should_run = True
            else:
                last_run = datetime.fromisoformat(job["last_run"].replace("Z", "+00:00"))
                if last_run.tzinfo is None:
                    last_run = last_run.replace(tzinfo=timezone.utc)
                next_run = last_run + timedelta(hours=SCRAPE_INTERVAL_HOURS)
                
                if datetime.now(timezone.utc) >= next_run:
                    should_run = True
                    
                # Retry failed jobs sooner
                if job["status"] == "failed" and job["failures"] < MAX_FAILURES_BEFORE_ALERT:
                    retry_time = last_run + timedelta(minutes=RETRY_DELAY_MINUTES)
                    if datetime.now(timezone.utc) >= retry_time:
                        should_run = True
            
            if should_run:
                await scrape_news_job(db)
            
            # Sleep for 5 minutes before checking again
            await asyncio.sleep(300)
            
        except Exception as e:
            logger.error(f"Scheduler error: {e}")
            await asyncio.sleep(60)  # Wait a minute on error


def get_job_status():
    """Get current status of all background jobs"""
    return job_status


async def trigger_immediate_scrape(db):
    """Manually trigger an immediate news scrape"""
    await scrape_news_job(db)
    return job_status["news_scrape"]
