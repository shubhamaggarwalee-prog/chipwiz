"""
Research Reports Module - TechInsights-style AI-generated reports
Based on public/OSINT sources only
"""
from fastapi import APIRouter, HTTPException, Request, Query
from typing import Optional, List
from datetime import datetime, timezone
import logging
import os
import uuid

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/reports", tags=["Reports"])


async def get_db():
    from server import db
    return db


# Seed report data
SEED_REPORTS = [
    {
        "report_id": "report_3nm_analysis",
        "title": "3nm Process Node Analysis: TSMC vs Samsung vs Intel",
        "slug": "3nm-process-node-analysis",
        "report_type": "node_analysis",
        "executive_summary": """The 3nm node represents a critical inflection point in semiconductor manufacturing, with TSMC, Samsung, and Intel deploying different architectural approaches. TSMC leads with its N3 family using FinFET architecture, while Samsung pioneered GAA at 3nm. Intel's Intel 3 node serves as a bridge to its upcoming Intel 18A.

Key findings:
- TSMC N3E shows 18% logic density improvement over N5
- Samsung 3nm GAA achieves 16% performance gain vs 5nm
- Intel 3 focuses on performance/power optimization over density
- Yield maturity varies significantly across foundries""",
        "content_sections": [
            {
                "title": "Technology Overview",
                "content": """## Transistor Architectures

### TSMC N3 Family (FinFET)
TSMC's 3nm family maintains FinFET architecture with enhanced performance:
- **N3**: Initial 3nm node (HVM Q4 2022)
- **N3E**: Enhanced version with better yield/performance balance
- **N3P**: Performance-optimized variant
- **N3X**: High-performance derivative

### Samsung 3nm (GAA)
Samsung's 3nm represents the industry's first GAA production:
- Gate-All-Around nanosheet architecture
- Variable sheet width for power/performance optimization
- Second generation (SF3) improving defect density

### Intel 3
Intel's node focusing on:
- High-performance optimization
- Enhanced power efficiency
- Bridge to Intel 18A (with backside power)"""
            },
            {
                "title": "Performance Comparison",
                "content": """## Comparative Analysis

| Metric | TSMC N3E | Samsung 3nm | Intel 3 |
|--------|----------|-------------|---------|
| Architecture | FinFET | GAA | FinFET |
| Density (MTr/mm²) | ~291 | ~230* | ~260* |
| Performance vs 5nm | +15% | +16% | +18% |
| Power vs 5nm | -30% | -25% | -20% |
| EUV Layers | 20+ | 20+ | Limited |

*Estimated based on public data

## Key Observations

1. **TSMC Density Lead**: Despite using FinFET, TSMC achieves highest density through layout optimization
2. **Samsung GAA Innovation**: First-mover advantage offset by yield challenges
3. **Intel Focus**: Prioritizing performance over density"""
            },
            {
                "title": "Manufacturing Considerations",
                "content": """## Yield and Maturity

### TSMC
- N3E reaching mature yields (>80% estimated)
- High EUV layer count requires tool availability
- CoWoS integration critical for AI customers

### Samsung
- GAA complexity impacting initial yields
- Improving with SF3 generation
- Customer diversification ongoing

### Intel
- Improving yield on Intel 3
- Focus on internal products
- External foundry ambitions (IFS)

## Supply Chain Implications

- EUV tool allocation remains constrained
- Advanced packaging capacity critical
- Geopolitical factors affecting location decisions"""
            }
        ],
        "data_sources": [
            "Company press releases and earnings calls",
            "Published technical papers (IEDM, VLSI Symposium)",
            "Patent filings and analysis",
            "Public roadmap disclosures"
        ],
        "assumptions": [
            "Density figures estimated from die analysis reports",
            "Yield data inferred from production ramp commentary",
            "Cost comparisons based on public pricing discussions"
        ],
        "risks_unknowns": [
            "Actual customer yields vary significantly",
            "Defect density improvements not publicly disclosed",
            "True cost structures are proprietary"
        ],
        "references": [
            {"title": "TSMC N3 Technology Overview", "url": "https://www.tsmc.com/english/dedicatedFoundry/technology/n3", "source": "TSMC"},
            {"title": "Samsung 3nm Press Release", "url": "https://semiconductor.samsung.com/foundry/", "source": "Samsung"},
            {"title": "Intel Technology Roadmap", "url": "https://www.intel.com/content/www/us/en/newsroom/", "source": "Intel"}
        ],
        "is_public": True,
        "premium_only": False
    },
    {
        "report_id": "report_ai_chip_packaging",
        "title": "Advanced Packaging for AI Accelerators: The CoWoS Capacity Challenge",
        "slug": "ai-chip-packaging-cowos",
        "report_type": "packaging",
        "executive_summary": """The explosive growth in AI accelerator demand has created unprecedented pressure on advanced packaging capacity, particularly TSMC's CoWoS platform. This report analyzes the packaging landscape, capacity constraints, and competitive dynamics shaping AI chip manufacturing.

Key findings:
- CoWoS demand exceeds supply by estimated 20-30%
- NVIDIA, AMD, and hyperscalers competing for limited capacity
- Alternative packaging solutions emerging (Intel EMIB, Samsung I-Cube)
- Capacity expansion requiring 18-24 month lead times""",
        "content_sections": [
            {
                "title": "Market Overview",
                "content": """## AI Accelerator Packaging Requirements

Modern AI accelerators require advanced packaging for:
- **High Bandwidth Memory (HBM)** integration
- **Multi-die architectures** (chiplets)
- **Thermal management** at >500W TDP
- **Signal integrity** for high-speed SerDes

### Key Customers
- NVIDIA: H100/H200/B100 (CoWoS-S)
- AMD: MI300A/X (silicon interposer)
- Google: TPU (multiple approaches)
- AWS, Microsoft: Custom accelerators"""
            },
            {
                "title": "Technology Analysis",
                "content": """## CoWoS Technology Deep Dive

### CoWoS-S (Silicon Interposer)
- Largest silicon interposer: up to 6 reticle
- Maximum HBM integration: 8 stacks
- Best for highest bandwidth requirements

### CoWoS-R (Organic RDL)
- Lower cost than silicon interposer
- Suitable for 2-4 HBM stacks
- Growing adoption for mid-range accelerators

### CoWoS-L (Local Interconnect)
- Hybrid approach extending interposer size
- Enables >6 reticle effective area
- Critical for next-gen accelerators

## Competitive Alternatives

| Technology | Provider | Maturity | Use Case |
|------------|----------|----------|----------|
| EMIB | Intel | Production | Ponte Vecchio |
| I-Cube | Samsung | Ramping | Limited |
| Fan-out | TSMC (InFO) | Production | Mobile/cost-sensitive |"""
            }
        ],
        "data_sources": [
            "Foundry technology announcements",
            "Customer product specifications",
            "Industry analyst estimates",
            "Earnings call commentary"
        ],
        "assumptions": [
            "Demand estimates based on datacenter buildout projections",
            "Capacity figures from public statements",
            "Pricing trends from industry sources"
        ],
        "risks_unknowns": [
            "Actual allocation decisions are confidential",
            "New capacity timelines may shift",
            "Alternative technologies may mature faster"
        ],
        "references": [
            {"title": "TSMC CoWoS Overview", "url": "https://www.tsmc.com/english/dedicatedFoundry/technology/cowos", "source": "TSMC"},
            {"title": "HBM Industry Analysis", "url": "https://www.skhynix.com/", "source": "SK Hynix"}
        ],
        "is_public": True,
        "premium_only": False
    }
]


@router.get("/")
async def get_reports(
    report_type: Optional[str] = None,
    is_public: bool = True,
    limit: int = Query(default=20, le=50),
    offset: int = 0
):
    """Get research reports"""
    db = await get_db()
    
    # Seed if empty
    count = await db.research_reports.count_documents({})
    if count == 0:
        for report in SEED_REPORTS:
            report["created_at"] = datetime.now(timezone.utc).isoformat()
            report["updated_at"] = datetime.now(timezone.utc).isoformat()
            report["author"] = "AI Research Team"
            await db.research_reports.insert_one(report)
    
    query = {}
    if report_type:
        query["report_type"] = report_type
    if is_public:
        query["is_public"] = True
    
    reports = await db.research_reports.find(
        query,
        {"_id": 0, "content_sections": 0}  # Exclude full content in list view
    ).sort("created_at", -1).skip(offset).limit(limit).to_list(limit)
    
    return reports


@router.get("/types")
async def get_report_types():
    """Get available report types"""
    return [
        {"id": "node_analysis", "name": "Node Analysis", "description": "Process node deep dives"},
        {"id": "foundry_comparison", "name": "Foundry Comparison", "description": "Competitive analysis"},
        {"id": "cost_trends", "name": "Cost Trends", "description": "Cost per transistor analysis"},
        {"id": "packaging", "name": "Advanced Packaging", "description": "Packaging technology reports"},
        {"id": "materials", "name": "Materials", "description": "New materials adoption"},
        {"id": "ai_chips", "name": "AI Chips", "description": "AI accelerator analysis"}
    ]


@router.get("/{slug}")
async def get_report(slug: str, req: Request):
    """Get a single report by slug"""
    from auth import get_current_user_from_request
    
    db = await get_db()
    
    report = await db.research_reports.find_one(
        {"slug": slug},
        {"_id": 0}
    )
    
    if not report:
        raise HTTPException(status_code=404, detail="Report not found")
    
    # Check premium access
    if report.get("premium_only"):
        user = await get_current_user_from_request(req)
        if not user or user.get("role") not in ["premium", "admin"]:
            raise HTTPException(status_code=403, detail="Premium subscription required")
    
    return report


@router.get("/{slug}/pdf")
async def export_report_pdf(slug: str, req: Request):
    """Export report as PDF"""
    from fastapi.responses import StreamingResponse
    from pdf_export import generate_report_pdf
    from auth import get_current_user_from_request
    
    db = await get_db()
    
    report = await db.research_reports.find_one(
        {"slug": slug},
        {"_id": 0}
    )
    
    if not report:
        raise HTTPException(status_code=404, detail="Report not found")
    
    # Check premium access
    if report.get("premium_only"):
        user = await get_current_user_from_request(req)
        if not user or user.get("role") not in ["premium", "admin"]:
            raise HTTPException(status_code=403, detail="Premium subscription required")
    
    # Generate PDF
    pdf_buffer = generate_report_pdf(report)
    
    # Clean filename
    filename = f"{slug}.pdf"
    
    return StreamingResponse(
        pdf_buffer,
        media_type="application/pdf",
        headers={
            "Content-Disposition": f"attachment; filename={filename}"
        }
    )


@router.post("/generate")
async def generate_report(
    topic: str,
    report_type: str,
    req: Request
):
    """Generate a new AI research report (admin only)"""
    from auth import get_current_user_from_request
    from emergentintegrations.llm.chat import LlmChat, UserMessage
    
    db = await get_db()
    user = await get_current_user_from_request(req)
    
    if not user or user.get("role") != "admin":
        raise HTTPException(status_code=403, detail="Admin access required")
    
    llm_key = os.environ.get("EMERGENT_LLM_KEY")
    if not llm_key:
        raise HTTPException(status_code=500, detail="LLM not configured")
    
    # Generate report using AI
    chat = LlmChat(
        api_key=llm_key,
        session_id=f"report_{uuid.uuid4().hex[:8]}",
        system_message="""You are a semiconductor industry research analyst. Generate professional research reports based on public information only.

Structure your reports with:
1. Executive Summary
2. Technology Overview
3. Comparative Analysis (if applicable)
4. Manufacturing Considerations
5. Market Implications

Always cite sources and distinguish facts from analysis. Use only publicly available information."""
    ).with_model("openai", "gpt-5.2")
    
    prompt = f"""Generate a research report on: {topic}
    Report type: {report_type}
    
    Provide a comprehensive analysis using only public sources. Include:
    - Executive summary
    - Technical details
    - Competitive landscape
    - Key risks and unknowns
    
    Format sections clearly with markdown."""
    
    try:
        response = await chat.send_message(UserMessage(text=prompt))
        
        # Create report document
        report_id = f"report_{uuid.uuid4().hex[:12]}"
        slug = topic.lower().replace(" ", "-")[:50]
        
        report = {
            "report_id": report_id,
            "title": topic,
            "slug": slug,
            "report_type": report_type,
            "executive_summary": response[:500],
            "content_sections": [{"title": "Full Report", "content": response}],
            "data_sources": ["AI-generated from public sources"],
            "assumptions": ["Based on publicly available information"],
            "risks_unknowns": ["AI-generated content - verify with primary sources"],
            "references": [],
            "created_at": datetime.now(timezone.utc).isoformat(),
            "updated_at": datetime.now(timezone.utc).isoformat(),
            "author": "AI Research Team",
            "is_public": False,  # Require review before publishing
            "premium_only": False
        }
        
        await db.research_reports.insert_one(report)
        
        return {"report_id": report_id, "slug": slug, "message": "Report generated - pending review"}
        
    except Exception as e:
        logger.error(f"Report generation error: {e}")
        raise HTTPException(status_code=500, detail="Report generation failed")
