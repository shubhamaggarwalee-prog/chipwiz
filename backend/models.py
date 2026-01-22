"""
Database Models for Semiconductor Intelligence Platform
"""
from pydantic import BaseModel, Field, EmailStr, ConfigDict
from typing import List, Optional, Dict, Any
from datetime import datetime, timezone
import uuid


def generate_id(prefix: str = "") -> str:
    """Generate a unique ID with optional prefix"""
    return f"{prefix}_{uuid.uuid4().hex[:12]}" if prefix else uuid.uuid4().hex[:12]


# User Models
class User(BaseModel):
    model_config = ConfigDict(extra="ignore")
    
    user_id: str = Field(default_factory=lambda: generate_id("user"))
    email: str
    name: str
    picture: Optional[str] = None
    role: str = "user"  # user, premium, admin
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    preferences: Dict[str, Any] = Field(default_factory=dict)


class UserSession(BaseModel):
    model_config = ConfigDict(extra="ignore")
    
    session_id: str = Field(default_factory=lambda: generate_id("sess"))
    user_id: str
    session_token: str
    expires_at: datetime
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


# Encyclopedia Models
class EncyclopediaCategory(BaseModel):
    model_config = ConfigDict(extra="ignore")
    
    category_id: str = Field(default_factory=lambda: generate_id("cat"))
    name: str
    slug: str
    description: str
    parent_id: Optional[str] = None
    order: int = 0
    icon: Optional[str] = None


class EncyclopediaTopic(BaseModel):
    model_config = ConfigDict(extra="ignore")
    
    topic_id: str = Field(default_factory=lambda: generate_id("topic"))
    category_id: str
    title: str
    slug: str
    overview: str
    content_beginner: str
    content_advanced: str
    diagrams: List[Dict[str, str]] = Field(default_factory=list)  # [{type, content, caption}]
    equations: List[Dict[str, str]] = Field(default_factory=list)  # [{latex, description}]
    manufacturing_challenges: List[str] = Field(default_factory=list)
    applications: List[str] = Field(default_factory=list)
    advantages: List[str] = Field(default_factory=list)
    limitations: List[str] = Field(default_factory=list)
    related_topics: List[str] = Field(default_factory=list)  # topic_ids
    references: List[Dict[str, str]] = Field(default_factory=list)  # [{title, url, source}]
    difficulty: str = "beginner"  # beginner, intermediate, advanced
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    author: str = "system"
    views: int = 0


# News Models
class NewsArticle(BaseModel):
    model_config = ConfigDict(extra="ignore")
    
    article_id: str = Field(default_factory=lambda: generate_id("news"))
    title: str
    summary: str
    content: str
    source: str
    source_url: str
    category: str  # euv, packaging, foundry, materials, design, etc.
    tags: List[str] = Field(default_factory=list)
    impact_analysis: str = ""
    why_it_matters: str = ""
    technical_depth: str = "general"  # general, technical, deep-dive
    confidence_score: float = 0.9
    published_at: datetime
    scraped_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    is_breaking: bool = False
    is_featured: bool = False


# Research Reports Models
class ResearchReport(BaseModel):
    model_config = ConfigDict(extra="ignore")
    
    report_id: str = Field(default_factory=lambda: generate_id("report"))
    title: str
    slug: str
    report_type: str  # node_analysis, foundry_comparison, cost_trends, packaging, materials, ai_chips
    executive_summary: str
    content_sections: List[Dict[str, Any]] = Field(default_factory=list)  # [{title, content, charts}]
    data_sources: List[str] = Field(default_factory=list)
    assumptions: List[str] = Field(default_factory=list)
    risks_unknowns: List[str] = Field(default_factory=list)
    references: List[Dict[str, str]] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    author: str = "AI Research Team"
    is_public: bool = True
    premium_only: bool = False


# Subscription Models
class Subscription(BaseModel):
    model_config = ConfigDict(extra="ignore")
    
    subscription_id: str = Field(default_factory=lambda: generate_id("sub"))
    user_id: str
    topic: str  # euv, tsmc, gan, packaging, ai_accelerators, etc.
    frequency: str = "daily"  # instant, daily, weekly, monthly
    is_active: bool = True
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


# Chat/AI Assistant Models
class ChatMessage(BaseModel):
    model_config = ConfigDict(extra="ignore")
    
    message_id: str = Field(default_factory=lambda: generate_id("msg"))
    session_id: str
    role: str  # user, assistant
    content: str
    citations: List[Dict[str, Any]] = Field(default_factory=list)
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class ChatSession(BaseModel):
    model_config = ConfigDict(extra="ignore")
    
    session_id: str = Field(default_factory=lambda: generate_id("chat"))
    user_id: str
    title: str = "New Research Session"
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


# Request/Response Models
class ChatRequest(BaseModel):
    message: str
    session_id: Optional[str] = None
    difficulty: str = "intermediate"  # beginner, intermediate, expert


class ChatResponse(BaseModel):
    message_id: str
    session_id: str
    response: str
    citations: List[Dict[str, Any]]
    follow_up_questions: List[str]


class SubscriptionCreate(BaseModel):
    topic: str
    frequency: str = "daily"


class UserPreferencesUpdate(BaseModel):
    theme: Optional[str] = None
    difficulty_default: Optional[str] = None
    email_notifications: Optional[bool] = None
