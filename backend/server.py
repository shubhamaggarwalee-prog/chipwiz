"""
Semiconductor Intelligence Platform - Main Server
"""
from fastapi import FastAPI, APIRouter
from dotenv import load_dotenv
from starlette.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
import os
import logging
import asyncio
from pathlib import Path
from contextlib import asynccontextmanager

# Load environment variables
ROOT_DIR = Path(__file__).parent
load_dotenv(ROOT_DIR / '.env')

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# MongoDB connection
mongo_url = os.environ['MONGO_URL']
client = AsyncIOMotorClient(mongo_url)
db = client[os.environ['DB_NAME']]

# Background task handle
scheduler_task = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan management"""
    global scheduler_task
    
    logger.info("Starting application...")
    
    # Initialize database indexes
    await create_indexes()
    
    # Seed expanded encyclopedia content
    await seed_expanded_content()
    
    # Start background scheduler
    from scheduler import run_scheduler
    scheduler_task = asyncio.create_task(run_scheduler(db))
    logger.info("Background scheduler started")
    
    yield
    
    # Cleanup
    if scheduler_task:
        scheduler_task.cancel()
        try:
            await scheduler_task
        except asyncio.CancelledError:
            pass
    
    client.close()
    logger.info("Application shutdown complete")


async def create_indexes():
    """Initialize database indexes"""
    logger.info("Creating database indexes...")
    
    try:
        # Encyclopedia indexes
        await db.encyclopedia_topics.create_index([("title", "text"), ("overview", "text"), ("content_beginner", "text")])
        await db.encyclopedia_topics.create_index("slug", unique=True)
        await db.encyclopedia_topics.create_index("category_id")
        
        # News indexes
        await db.news_articles.create_index([("title", "text"), ("summary", "text")])
        await db.news_articles.create_index("article_id", unique=True)
        await db.news_articles.create_index("category")
        await db.news_articles.create_index("published_at")
        
        # User indexes
        await db.users.create_index("email", unique=True)
        await db.users.create_index("user_id", unique=True)
        
        # Session indexes
        await db.user_sessions.create_index("session_token", unique=True)
        await db.user_sessions.create_index("user_id")
        await db.user_sessions.create_index("expires_at")
        
        # Chat indexes
        await db.chat_sessions.create_index("user_id")
        await db.chat_messages.create_index("session_id")
        
        # Report indexes
        await db.research_reports.create_index("slug", unique=True)
        await db.research_reports.create_index("report_type")
        
        # Subscription indexes
        await db.subscriptions.create_index([("user_id", 1), ("topic", 1)], unique=True)
        
        logger.info("Database indexes created successfully")
    except Exception as e:
        logger.error(f"Error creating indexes: {e}")


async def seed_expanded_content():
    """Seed expanded encyclopedia topics"""
    from expanded_content import get_expanded_topics
    from additional_topics import get_additional_topics
    from extended_topics_p2 import get_extended_topics_part2
    from extended_topics_p3 import get_extended_topics_part3
    from extended_topics_p4 import get_extended_topics_part4
    from final_topics import get_final_topics
    from datetime import datetime, timezone
    
    try:
        all_topic_sets = [
            ("expanded", get_expanded_topics()),
            ("additional", get_additional_topics()),
            ("extended_p2", get_extended_topics_part2()),
            ("extended_p3", get_extended_topics_part3()),
            ("extended_p4", get_extended_topics_part4()),
            ("final", get_final_topics())
        ]
        
        total_seeded = 0
        for source_name, topics in all_topic_sets:
            for topic in topics:
                existing = await db.encyclopedia_topics.find_one(
                    {"topic_id": topic["topic_id"]},
                    {"_id": 0}
                )
                if not existing:
                    topic["created_at"] = datetime.now(timezone.utc).isoformat()
                    topic["updated_at"] = datetime.now(timezone.utc).isoformat()
                    await db.encyclopedia_topics.insert_one(topic)
                    total_seeded += 1
        
        total_topics = sum(len(topics) for _, topics in all_topic_sets)
        logger.info(f"Encyclopedia seeding complete - {total_topics} topics in source, {total_seeded} new topics added")
    except Exception as e:
        logger.error(f"Error seeding content: {e}")


# Create FastAPI app with lifespan
app = FastAPI(
    title="Semiconductor Intelligence Platform",
    description="AI-powered semiconductor knowledge and research platform",
    version="1.0.0",
    lifespan=lifespan
)

# Create main API router
api_router = APIRouter(prefix="/api")


# Health check
@api_router.get("/")
async def root():
    return {"message": "Semiconductor Intelligence Platform API", "status": "healthy"}


@api_router.get("/health")
async def health_check():
    from scheduler import get_job_status
    return {
        "status": "healthy", 
        "database": "connected",
        "scheduler": get_job_status()
    }


# Import and include routers
from auth import router as auth_router
from encyclopedia import router as encyclopedia_router
from news_routes import router as news_router
from ai_assistant import router as assistant_router
from reports import router as reports_router
from subscriptions import router as subscriptions_router
from preferences import router as preferences_router

api_router.include_router(auth_router)
api_router.include_router(encyclopedia_router)
api_router.include_router(news_router)
api_router.include_router(assistant_router)
api_router.include_router(reports_router)
api_router.include_router(subscriptions_router)
api_router.include_router(preferences_router)

# Include API router
app.include_router(api_router)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=os.environ.get('CORS_ORIGINS', '*').split(','),
    allow_methods=["*"],
    allow_headers=["*"],
)
