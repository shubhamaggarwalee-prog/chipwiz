"""
Subscriptions Module - Topic-based email subscriptions with Resend
"""
from fastapi import APIRouter, HTTPException, Request, BackgroundTasks
from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime, timezone
import logging
import os
import asyncio
import uuid

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/subscriptions", tags=["Subscriptions"])

# Available subscription topics
SUBSCRIPTION_TOPICS = [
    {"id": "euv", "name": "EUV Lithography", "description": "Updates on extreme ultraviolet lithography technology"},
    {"id": "tsmc", "name": "TSMC News", "description": "Taiwan Semiconductor Manufacturing Company updates"},
    {"id": "intel", "name": "Intel Foundry", "description": "Intel manufacturing and process updates"},
    {"id": "samsung", "name": "Samsung Foundry", "description": "Samsung semiconductor foundry news"},
    {"id": "packaging", "name": "Advanced Packaging", "description": "CoWoS, chiplets, and 3D integration"},
    {"id": "gaafet", "name": "GAAFET/Nanosheet", "description": "Gate-all-around transistor technology"},
    {"id": "ai_chips", "name": "AI Accelerators", "description": "GPU, TPU, and AI chip developments"},
    {"id": "memory", "name": "Memory Technology", "description": "HBM, DDR, NAND developments"},
    {"id": "materials", "name": "New Materials", "description": "SiC, GaN, and compound semiconductors"},
    {"id": "nodes", "name": "Process Nodes", "description": "3nm, 2nm, and beyond"}
]


class SubscriptionCreate(BaseModel):
    topic: str
    frequency: str = "daily"  # instant, daily, weekly, monthly


class SubscriptionUpdate(BaseModel):
    frequency: Optional[str] = None
    is_active: Optional[bool] = None


class EmailNotificationRequest(BaseModel):
    topic: str
    subject: str
    content: str


async def get_db():
    from server import db
    return db


async def send_email_notification(recipient: str, subject: str, html_content: str):
    """Send email using Resend"""
    try:
        import resend
        
        resend.api_key = os.environ.get("RESEND_API_KEY")
        sender_email = os.environ.get("SENDER_EMAIL", "onboarding@resend.dev")
        
        if not resend.api_key:
            logger.warning("Resend API key not configured")
            return False
        
        params = {
            "from": sender_email,
            "to": [recipient],
            "subject": subject,
            "html": html_content
        }
        
        # Run sync SDK in thread for non-blocking
        email = await asyncio.to_thread(resend.Emails.send, params)
        logger.info(f"Email sent: {email.get('id')}")
        return True
        
    except Exception as e:
        logger.error(f"Failed to send email: {e}")
        return False


def generate_email_template(topic_name: str, content: str, unsubscribe_url: str) -> str:
    """Generate HTML email template"""
    return f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body style="margin: 0; padding: 0; font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif; background-color: #f8fafc;">
    <table width="100%" cellpadding="0" cellspacing="0" style="background-color: #f8fafc; padding: 40px 20px;">
        <tr>
            <td align="center">
                <table width="600" cellpadding="0" cellspacing="0" style="background-color: #ffffff; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.04);">
                    <!-- Header -->
                    <tr>
                        <td style="padding: 32px 32px 24px; border-bottom: 1px solid #e2e8f0;">
                            <h1 style="margin: 0; font-size: 24px; font-weight: 600; color: #0f172a;">
                                Semiconductor Intelligence
                            </h1>
                            <p style="margin: 8px 0 0; font-size: 14px; color: #64748b;">
                                {topic_name} Update
                            </p>
                        </td>
                    </tr>
                    <!-- Content -->
                    <tr>
                        <td style="padding: 32px;">
                            <div style="font-size: 16px; line-height: 1.6; color: #334155;">
                                {content}
                            </div>
                        </td>
                    </tr>
                    <!-- Footer -->
                    <tr>
                        <td style="padding: 24px 32px; background-color: #f8fafc; border-top: 1px solid #e2e8f0; border-radius: 0 0 8px 8px;">
                            <p style="margin: 0; font-size: 12px; color: #64748b; text-align: center;">
                                You received this because you subscribed to {topic_name} updates.
                                <br>
                                <a href="{unsubscribe_url}" style="color: #006fee; text-decoration: none;">Unsubscribe</a> | 
                                <a href="#" style="color: #006fee; text-decoration: none;">Manage Preferences</a>
                            </p>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
</body>
</html>
"""


@router.get("/topics")
async def get_topics():
    """Get available subscription topics"""
    return SUBSCRIPTION_TOPICS


@router.get("/")
async def get_user_subscriptions(req: Request):
    """Get current user's subscriptions"""
    from auth import get_current_user_from_request
    
    db = await get_db()
    user = await get_current_user_from_request(req)
    
    if not user:
        raise HTTPException(status_code=401, detail="Not authenticated")
    
    subscriptions = await db.subscriptions.find(
        {"user_id": user["user_id"]},
        {"_id": 0}
    ).to_list(100)
    
    # Enrich with topic details
    for sub in subscriptions:
        topic_info = next((t for t in SUBSCRIPTION_TOPICS if t["id"] == sub["topic"]), None)
        if topic_info:
            sub["topic_name"] = topic_info["name"]
            sub["topic_description"] = topic_info["description"]
    
    return subscriptions


@router.post("/")
async def create_subscription(sub: SubscriptionCreate, req: Request):
    """Subscribe to a topic"""
    from auth import get_current_user_from_request
    
    db = await get_db()
    user = await get_current_user_from_request(req)
    
    if not user:
        raise HTTPException(status_code=401, detail="Not authenticated")
    
    # Validate topic
    if sub.topic not in [t["id"] for t in SUBSCRIPTION_TOPICS]:
        raise HTTPException(status_code=400, detail="Invalid topic")
    
    # Validate frequency
    if sub.frequency not in ["instant", "daily", "weekly", "monthly"]:
        raise HTTPException(status_code=400, detail="Invalid frequency")
    
    # Check if already subscribed
    existing = await db.subscriptions.find_one(
        {"user_id": user["user_id"], "topic": sub.topic},
        {"_id": 0}
    )
    
    if existing:
        raise HTTPException(status_code=400, detail="Already subscribed to this topic")
    
    subscription = {
        "subscription_id": f"sub_{uuid.uuid4().hex[:12]}",
        "user_id": user["user_id"],
        "topic": sub.topic,
        "frequency": sub.frequency,
        "is_active": True,
        "created_at": datetime.now(timezone.utc).isoformat()
    }
    
    await db.subscriptions.insert_one(subscription)
    
    # Send welcome email
    topic_info = next((t for t in SUBSCRIPTION_TOPICS if t["id"] == sub.topic), {})
    welcome_content = f"""
    <h2>Welcome to {topic_info.get('name', sub.topic)} Updates!</h2>
    <p>You're now subscribed to receive {sub.frequency} updates on {topic_info.get('description', '')}.</p>
    <p>Stay informed with the latest developments in semiconductor technology.</p>
    """
    
    await send_email_notification(
        user["email"],
        f"Subscribed to {topic_info.get('name', sub.topic)}",
        generate_email_template(topic_info.get('name', sub.topic), welcome_content, "#")
    )
    
    return {"subscription_id": subscription["subscription_id"], "message": "Subscribed successfully"}


@router.put("/{subscription_id}")
async def update_subscription(subscription_id: str, update: SubscriptionUpdate, req: Request):
    """Update subscription settings"""
    from auth import get_current_user_from_request
    
    db = await get_db()
    user = await get_current_user_from_request(req)
    
    if not user:
        raise HTTPException(status_code=401, detail="Not authenticated")
    
    # Verify ownership
    sub = await db.subscriptions.find_one(
        {"subscription_id": subscription_id, "user_id": user["user_id"]},
        {"_id": 0}
    )
    
    if not sub:
        raise HTTPException(status_code=404, detail="Subscription not found")
    
    # Build update
    update_doc = {}
    if update.frequency is not None:
        if update.frequency not in ["instant", "daily", "weekly", "monthly"]:
            raise HTTPException(status_code=400, detail="Invalid frequency")
        update_doc["frequency"] = update.frequency
    if update.is_active is not None:
        update_doc["is_active"] = update.is_active
    
    if update_doc:
        await db.subscriptions.update_one(
            {"subscription_id": subscription_id},
            {"$set": update_doc}
        )
    
    return {"message": "Subscription updated"}


@router.delete("/{subscription_id}")
async def unsubscribe(subscription_id: str, req: Request):
    """Unsubscribe from a topic"""
    from auth import get_current_user_from_request
    
    db = await get_db()
    user = await get_current_user_from_request(req)
    
    if not user:
        raise HTTPException(status_code=401, detail="Not authenticated")
    
    result = await db.subscriptions.delete_one(
        {"subscription_id": subscription_id, "user_id": user["user_id"]}
    )
    
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Subscription not found")
    
    return {"message": "Unsubscribed successfully"}


@router.post("/notify")
async def send_topic_notification(
    notification: EmailNotificationRequest,
    background_tasks: BackgroundTasks,
    req: Request
):
    """Send notification to all subscribers of a topic (admin only)"""
    from auth import get_current_user_from_request
    
    db = await get_db()
    user = await get_current_user_from_request(req)
    
    if not user or user.get("role") != "admin":
        raise HTTPException(status_code=403, detail="Admin access required")
    
    # Get all active subscribers
    subscriptions = await db.subscriptions.find(
        {"topic": notification.topic, "is_active": True},
        {"_id": 0}
    ).to_list(10000)
    
    if not subscriptions:
        return {"message": "No subscribers for this topic"}
    
    # Get user emails
    user_ids = [s["user_id"] for s in subscriptions]
    users = await db.users.find(
        {"user_id": {"$in": user_ids}},
        {"_id": 0, "user_id": 1, "email": 1}
    ).to_list(10000)
    
    email_map = {u["user_id"]: u["email"] for u in users}
    
    topic_info = next((t for t in SUBSCRIPTION_TOPICS if t["id"] == notification.topic), {})
    
    async def send_all():
        for sub in subscriptions:
            email = email_map.get(sub["user_id"])
            if email:
                await send_email_notification(
                    email,
                    notification.subject,
                    generate_email_template(
                        topic_info.get("name", notification.topic),
                        notification.content,
                        "#"  # Unsubscribe URL
                    )
                )
    
    background_tasks.add_task(send_all)
    
    return {"message": f"Sending notifications to {len(subscriptions)} subscribers"}
