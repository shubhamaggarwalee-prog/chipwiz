"""
Semiconductor Intelligence Platform - Main Server
"""
from fastapi import FastAPI, APIRouter
from dotenv import load_dotenv
from starlette.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
import os
import logging
from pathlib import Path

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

# Create FastAPI app
app = FastAPI(
    title="Semiconductor Intelligence Platform",
    description="AI-powered semiconductor knowledge and research platform",
    version="1.0.0"
)

# Create main API router
api_router = APIRouter(prefix="/api")


# Health check
@api_router.get("/")
async def root():
    return {"message": "Semiconductor Intelligence Platform API", "status": "healthy"}


@api_router.get("/health")
async def health_check():
    return {"status": "healthy", "database": "connected"}


# Import and include routers
from auth import router as auth_router
from encyclopedia import router as encyclopedia_router
from news_routes import router as news_router
from ai_assistant import router as assistant_router
from reports import router as reports_router
from subscriptions import router as subscriptions_router

api_router.include_router(auth_router)
api_router.include_router(encyclopedia_router)
api_router.include_router(news_router)
api_router.include_router(assistant_router)
api_router.include_router(reports_router)
api_router.include_router(subscriptions_router)

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


@app.on_event("startup")
async def startup_event():
    """Initialize database indexes on startup"""
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


@app.on_event("shutdown")
async def shutdown_db_client():
    """Close MongoDB connection on shutdown"""
    client.close()
    logger.info("Database connection closed")
