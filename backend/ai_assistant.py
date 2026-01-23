"""
AI Research Assistant - GPT-5.2 powered semiconductor research assistant
with RAG, citations, and technical analysis capabilities
"""
from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel
from typing import List, Dict, Any, Optional
from datetime import datetime, timezone
import uuid
import logging
import os
import re
import json

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/assistant", tags=["AI Assistant"])


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


async def get_db():
    from server import db
    return db


def get_system_prompt(difficulty: str) -> str:
    """Get system prompt based on difficulty level"""
    base_prompt = """You are an expert semiconductor research assistant with deep knowledge of:
- Semiconductor physics and device engineering
- Manufacturing processes (lithography, etching, deposition, etc.)
- Advanced packaging (2.5D, 3D-IC, chiplets, CoWoS)
- Process nodes and scaling (FinFET, GAAFET, CFET)
- EUV lithography and high-NA EUV
- Materials science (Si, SiC, GaN, III-V compounds)
- Industry landscape (TSMC, Samsung, Intel, ASML, etc.)

IMPORTANT RULES:
1. Always provide accurate, technically sound information
2. Cite sources when possible (use [Source: description] format)
3. Distinguish between established facts and analysis/opinion
4. If uncertain, say so - never hallucinate
5. Use only public, legally accessible information
6. Transform and analyze information, never reproduce verbatim

"""
    
    difficulty_instructions = {
        "beginner": """Explain concepts for someone new to semiconductors. Use analogies, avoid jargon, 
        and build up from fundamentals. Define technical terms when first used.""",
        
        "intermediate": """Explain for engineers/students with basic semiconductor knowledge. 
        Use technical terms but explain complex concepts. Include equations where helpful.""",
        
        "expert": """Provide deep technical analysis for industry professionals. 
        Include detailed physics, manufacturing parameters, and industry context. 
        Assume familiarity with advanced concepts."""
    }
    
    return base_prompt + difficulty_instructions.get(difficulty, difficulty_instructions["intermediate"])


async def search_knowledge_base(db, query: str, limit: int = 5) -> List[Dict]:
    """Search encyclopedia and news for relevant context"""
    results = []
    
    # Search encyclopedia topics
    topics = await db.encyclopedia_topics.find(
        {"$text": {"$search": query}},
        {"_id": 0, "score": {"$meta": "textScore"}}
    ).sort([("score", {"$meta": "textScore"})]).limit(limit).to_list(limit)
    
    for topic in topics:
        results.append({
            "type": "encyclopedia",
            "title": topic.get("title", ""),
            "content": topic.get("overview", "")[:500],
            "source": f"Encyclopedia: {topic.get('title', '')}"
        })
    
    # Search news articles
    articles = await db.news_articles.find(
        {"$text": {"$search": query}},
        {"_id": 0, "score": {"$meta": "textScore"}}
    ).sort([("score", {"$meta": "textScore"})]).limit(limit).to_list(limit)
    
    for article in articles:
        results.append({
            "type": "news",
            "title": article.get("title", ""),
            "content": article.get("summary", "")[:300],
            "source": article.get("source", "News"),
            "url": article.get("source_url", "")
        })
    
    return results


def detect_comparison_query(message: str) -> tuple[bool, Optional[tuple[str, str]]]:
    """
    Detect if a message is a comparison query and extract the items being compared.
    Returns (is_comparison, (item1, item2) or None)
    """
    message_lower = message.lower()
    
    # Comparison patterns
    comparison_patterns = [
        r'compare\s+(.+?)\s+(?:vs\.?|versus|and|with|to)\s+(.+?)(?:\?|$|\.|\s+for)',
        r'(.+?)\s+(?:vs\.?|versus)\s+(.+?)(?:\?|$|\.)',
        r'difference(?:s)?\s+between\s+(.+?)\s+and\s+(.+?)(?:\?|$|\.)',
        r'(.+?)\s+or\s+(.+?)\s+(?:for|which|what)',
        r'which\s+is\s+better[,:]?\s+(.+?)\s+or\s+(.+?)(?:\?|$)',
        r'(.+?)\s+compared\s+to\s+(.+?)(?:\?|$|\.)',
    ]
    
    for pattern in comparison_patterns:
        match = re.search(pattern, message_lower, re.IGNORECASE)
        if match:
            item1 = match.group(1).strip()
            item2 = match.group(2).strip()
            # Clean up items
            item1 = re.sub(r'\b(the|a|an)\s+', '', item1).strip()
            item2 = re.sub(r'\b(the|a|an)\s+', '', item2).strip()
            if len(item1) > 2 and len(item2) > 2:
                return True, (item1, item2)
    
    return False, None


def get_comparison_system_prompt(item1: str, item2: str, difficulty: str) -> str:
    """Generate a specialized system prompt for comparison queries"""
    difficulty_tone = {
        "beginner": "Use simple language and analogies. Define technical terms.",
        "intermediate": "Use technical language but explain complex concepts.",
        "expert": "Provide deep technical analysis with specific parameters and metrics."
    }
    
    return f"""You are an expert semiconductor research assistant specializing in technology comparisons.

Your task is to compare {item1} vs {item2}.

{difficulty_tone.get(difficulty, difficulty_tone["intermediate"])}

CRITICAL: Structure your response EXACTLY as follows (use these exact headers):

## Summary
[2-3 sentence executive summary of the key differences]

## Comparison Table
| Aspect | {item1.title()} | {item2.title()} |
|--------|-------|-------|
| Architecture | [details] | [details] |
| Performance | [details] | [details] |
| Power Efficiency | [details] | [details] |
| Manufacturing | [details] | [details] |
| Maturity/Availability | [details] | [details] |
| Key Applications | [details] | [details] |

## {item1.title()} Advantages
- [Advantage 1]
- [Advantage 2]
- [Advantage 3]

## {item2.title()} Advantages
- [Advantage 1]
- [Advantage 2]
- [Advantage 3]

## Manufacturing Implications
[Analysis of manufacturing challenges, yield considerations, and production readiness for each technology]

## Recommendation
[When to choose each technology based on use case]

IMPORTANT RULES:
1. Cite sources as [Source: description] where applicable
2. Be objective - present facts for both technologies
3. If information is uncertain or speculative, note it clearly
4. Use only public, legally accessible information
5. Include specific numbers/metrics where available"""


async def generate_follow_up_questions(response: str, is_comparison: bool = False) -> List[str]:
    """Generate relevant follow-up questions based on the response"""
    questions = []
    
    if is_comparison:
        # Comparison-specific follow-ups
        questions = [
            "What are the cost implications of each approach?",
            "Which technology has better long-term scaling potential?",
            "How do these technologies impact chip design methodology?"
        ]
        return questions
    
    # Standard keyword-based follow-up generation
    keywords = {
        "euv": ["What are the stochastic effects in EUV lithography?", "How does high-NA EUV improve resolution?"],
        "finfet": ["How do FinFETs compare to planar transistors?", "What are the scaling limits of FinFET technology?"],
        "gaafet": ["What advantages do GAAFETs offer over FinFETs?", "Which foundries are leading in GAAFET production?"],
        "tsmc": ["What is TSMC's N2 node roadmap?", "How does TSMC's packaging compare to Intel?"],
        "packaging": ["What is CoWoS technology?", "How do chiplets improve yield?"],
        "lithography": ["What is the resolution limit of EUV?", "How does multi-patterning work?"],
        "3nm": ["What companies offer 3nm manufacturing?", "What is the transistor density at 3nm?"],
        "2nm": ["When will 2nm be in production?", "What architecture is used at 2nm?"]
    }
    
    response_lower = response.lower()
    for keyword, qs in keywords.items():
        if keyword in response_lower:
            questions.extend(qs[:2])
    
    # Ensure we have at least some questions
    if len(questions) < 3:
        default_questions = [
            "Can you explain this in more technical detail?",
            "What are the manufacturing challenges involved?",
            "How does this compare to competing technologies?"
        ]
        questions.extend(default_questions[:3 - len(questions)])
    
    return questions[:3]


@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest, req: Request):
    """Send a message to the AI research assistant"""
    from emergentintegrations.llm.chat import LlmChat, UserMessage
    from auth import get_current_user_from_request
    
    db = await get_db()
    llm_key = os.environ.get("EMERGENT_LLM_KEY")
    
    if not llm_key:
        raise HTTPException(status_code=500, detail="LLM service not configured")
    
    # Get current user (optional for chat)
    user = await get_current_user_from_request(req)
    user_id = user["user_id"] if user else "anonymous"
    
    # Get or create session
    session_id = request.session_id
    if not session_id:
        session_id = f"chat_{uuid.uuid4().hex[:12]}"
        # Create new session
        session_doc = {
            "session_id": session_id,
            "user_id": user_id,
            "title": request.message[:50] + "..." if len(request.message) > 50 else request.message,
            "created_at": datetime.now(timezone.utc).isoformat(),
            "updated_at": datetime.now(timezone.utc).isoformat()
        }
        await db.chat_sessions.insert_one(session_doc)
    
    # Get chat history for context
    history = await db.chat_messages.find(
        {"session_id": session_id},
        {"_id": 0}
    ).sort("timestamp", 1).limit(10).to_list(10)
    
    # Search knowledge base for context
    context_results = await search_knowledge_base(db, request.message)
    
    # Build context string
    context = ""
    citations = []
    if context_results:
        context = "\n\nRelevant context from knowledge base:\n"
        for i, result in enumerate(context_results, 1):
            context += f"\n[{i}] {result['title']}: {result['content']}\n"
            citations.append({
                "index": i,
                "type": result["type"],
                "title": result["title"],
                "source": result.get("source", ""),
                "url": result.get("url", "")
            })
    
    # Initialize LLM chat
    system_prompt = get_system_prompt(request.difficulty)
    if context:
        system_prompt += f"\n\nUse this context to inform your response, citing sources as [1], [2], etc.:{context}"
    
    chat_llm = LlmChat(
        api_key=llm_key,
        session_id=session_id,
        system_message=system_prompt
    ).with_model("openai", "gpt-5.2")
    
    # Build conversation context from history
    for msg in history[-6:]:  # Last 6 messages for context
        if msg["role"] == "user":
            await chat_llm.send_message(UserMessage(text=msg["content"]))
    
    # Send current message
    try:
        response = await chat_llm.send_message(UserMessage(text=request.message))
    except Exception as e:
        logger.error(f"LLM error: {e}")
        raise HTTPException(status_code=500, detail="AI service temporarily unavailable")
    
    # Generate follow-up questions
    follow_ups = await generate_follow_up_questions(response)
    
    # Store messages
    message_id = f"msg_{uuid.uuid4().hex[:12]}"
    user_msg = {
        "message_id": f"msg_{uuid.uuid4().hex[:12]}",
        "session_id": session_id,
        "role": "user",
        "content": request.message,
        "citations": [],
        "timestamp": datetime.now(timezone.utc).isoformat()
    }
    assistant_msg = {
        "message_id": message_id,
        "session_id": session_id,
        "role": "assistant",
        "content": response,
        "citations": citations,
        "timestamp": datetime.now(timezone.utc).isoformat()
    }
    
    await db.chat_messages.insert_many([user_msg, assistant_msg])
    
    # Update session
    await db.chat_sessions.update_one(
        {"session_id": session_id},
        {"$set": {"updated_at": datetime.now(timezone.utc).isoformat()}}
    )
    
    return ChatResponse(
        message_id=message_id,
        session_id=session_id,
        response=response,
        citations=citations,
        follow_up_questions=follow_ups
    )


@router.get("/sessions")
async def get_chat_sessions(req: Request):
    """Get user's chat sessions"""
    from auth import get_current_user_from_request
    
    db = await get_db()
    user = await get_current_user_from_request(req)
    
    if not user:
        raise HTTPException(status_code=401, detail="Not authenticated")
    
    sessions = await db.chat_sessions.find(
        {"user_id": user["user_id"]},
        {"_id": 0}
    ).sort("updated_at", -1).limit(50).to_list(50)
    
    return sessions


@router.get("/sessions/{session_id}/messages")
async def get_session_messages(session_id: str, req: Request):
    """Get messages from a chat session"""
    from auth import get_current_user_from_request
    
    db = await get_db()
    user = await get_current_user_from_request(req)
    
    # Verify session belongs to user
    session = await db.chat_sessions.find_one(
        {"session_id": session_id},
        {"_id": 0}
    )
    
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")
    
    if user and session["user_id"] != user["user_id"] and session["user_id"] != "anonymous":
        raise HTTPException(status_code=403, detail="Access denied")
    
    messages = await db.chat_messages.find(
        {"session_id": session_id},
        {"_id": 0}
    ).sort("timestamp", 1).to_list(100)
    
    return messages


@router.delete("/sessions/{session_id}")
async def delete_session(session_id: str, req: Request):
    """Delete a chat session"""
    from auth import get_current_user_from_request
    
    db = await get_db()
    user = await get_current_user_from_request(req)
    
    if not user:
        raise HTTPException(status_code=401, detail="Not authenticated")
    
    # Verify ownership
    session = await db.chat_sessions.find_one(
        {"session_id": session_id, "user_id": user["user_id"]},
        {"_id": 0}
    )
    
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")
    
    # Delete session and messages
    await db.chat_sessions.delete_one({"session_id": session_id})
    await db.chat_messages.delete_many({"session_id": session_id})
    
    return {"message": "Session deleted"}
