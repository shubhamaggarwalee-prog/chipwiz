"""
User Preferences Module - Persistent user settings
Stores theme, AI difficulty, subscription preferences, and session data
"""
from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from datetime import datetime, timezone
import os

router = APIRouter(prefix="/preferences", tags=["preferences"])

# Get database connection
async def get_db():
    from server import db
    return db


class UserPreferences(BaseModel):
    theme: Optional[str] = "light"  # light, dark, system
    difficulty: Optional[str] = "intermediate"  # beginner, intermediate, advanced
    email_frequency: Optional[str] = "weekly"  # daily, weekly, monthly, never
    subscribed_topics: Optional[List[str]] = []
    notification_enabled: Optional[bool] = True
    last_ai_session_id: Optional[str] = None


class PreferenceUpdate(BaseModel):
    key: str
    value: Any


@router.get("/")
async def get_preferences(request: Request):
    """Get user preferences"""
    from auth import get_current_user_from_request
    
    db = await get_db()
    user = await get_current_user_from_request(request)
    
    if not user:
        # Return defaults for anonymous users
        return {
            "theme": "light",
            "difficulty": "intermediate",
            "email_frequency": "weekly",
            "subscribed_topics": [],
            "notification_enabled": True,
            "last_ai_session_id": None,
            "is_authenticated": False
        }
    
    # Get stored preferences
    prefs = await db.user_preferences.find_one(
        {"user_id": user["user_id"]},
        {"_id": 0}
    )
    
    if not prefs:
        # Create default preferences
        prefs = {
            "user_id": user["user_id"],
            "theme": "light",
            "difficulty": "intermediate",
            "email_frequency": "weekly",
            "subscribed_topics": [],
            "notification_enabled": True,
            "last_ai_session_id": None,
            "created_at": datetime.now(timezone.utc).isoformat(),
            "updated_at": datetime.now(timezone.utc).isoformat()
        }
        await db.user_preferences.insert_one(prefs)
        prefs.pop("_id", None)
    
    prefs["is_authenticated"] = True
    return prefs


@router.put("/")
async def update_preferences(preferences: UserPreferences, request: Request):
    """Update all user preferences"""
    from auth import get_current_user_from_request
    
    db = await get_db()
    user = await get_current_user_from_request(request)
    
    if not user:
        raise HTTPException(status_code=401, detail="Authentication required")
    
    update_data = preferences.dict(exclude_unset=True)
    update_data["updated_at"] = datetime.now(timezone.utc).isoformat()
    
    result = await db.user_preferences.update_one(
        {"user_id": user["user_id"]},
        {"$set": update_data},
        upsert=True
    )
    
    return {"message": "Preferences updated", "modified": result.modified_count > 0}


@router.patch("/")
async def patch_preference(update: PreferenceUpdate, request: Request):
    """Update a single preference"""
    from auth import get_current_user_from_request
    
    db = await get_db()
    user = await get_current_user_from_request(request)
    
    if not user:
        raise HTTPException(status_code=401, detail="Authentication required")
    
    allowed_keys = ["theme", "difficulty", "email_frequency", "subscribed_topics", 
                    "notification_enabled", "last_ai_session_id"]
    
    if update.key not in allowed_keys:
        raise HTTPException(status_code=400, detail=f"Invalid preference key: {update.key}")
    
    await db.user_preferences.update_one(
        {"user_id": user["user_id"]},
        {
            "$set": {
                update.key: update.value,
                "updated_at": datetime.now(timezone.utc).isoformat()
            }
        },
        upsert=True
    )
    
    return {"message": f"Preference '{update.key}' updated", "value": update.value}


@router.get("/sync")
async def sync_preferences(request: Request):
    """
    Sync preferences across devices.
    Returns preferences with sync timestamp for conflict resolution.
    """
    from auth import get_current_user_from_request
    
    db = await get_db()
    user = await get_current_user_from_request(request)
    
    if not user:
        return {"synced": False, "reason": "Not authenticated"}
    
    prefs = await db.user_preferences.find_one(
        {"user_id": user["user_id"]},
        {"_id": 0}
    )
    
    return {
        "synced": True,
        "preferences": prefs,
        "sync_timestamp": datetime.now(timezone.utc).isoformat(),
        "user_id": user["user_id"]
    }


@router.post("/sync")
async def push_preferences(
    preferences: Dict[str, Any],
    request: Request
):
    """
    Push local preferences to server.
    Used for syncing from client to server.
    """
    from auth import get_current_user_from_request
    
    db = await get_db()
    user = await get_current_user_from_request(request)
    
    if not user:
        raise HTTPException(status_code=401, detail="Authentication required")
    
    # Filter to allowed keys
    allowed_keys = ["theme", "difficulty", "email_frequency", "subscribed_topics", 
                    "notification_enabled", "last_ai_session_id"]
    
    filtered_prefs = {k: v for k, v in preferences.items() if k in allowed_keys}
    filtered_prefs["updated_at"] = datetime.now(timezone.utc).isoformat()
    
    await db.user_preferences.update_one(
        {"user_id": user["user_id"]},
        {"$set": filtered_prefs},
        upsert=True
    )
    
    return {
        "synced": True,
        "sync_timestamp": datetime.now(timezone.utc).isoformat()
    }
