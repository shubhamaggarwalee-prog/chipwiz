"""
Encyclopedia Module - Structured semiconductor knowledge base
"""
from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional
from datetime import datetime, timezone
import logging

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/encyclopedia", tags=["Encyclopedia"])


async def get_db():
    from server import db
    return db


# Initial seed data for encyclopedia
SEED_CATEGORIES = [
    {"category_id": "cat_fundamentals", "name": "Fundamentals", "slug": "fundamentals", "description": "Basic semiconductor physics and principles", "order": 1, "icon": "atom"},
    {"category_id": "cat_devices", "name": "Devices", "slug": "devices", "description": "Transistors, diodes, and semiconductor devices", "order": 2, "icon": "cpu"},
    {"category_id": "cat_manufacturing", "name": "Manufacturing", "slug": "manufacturing", "description": "Fabrication processes and techniques", "order": 3, "icon": "factory"},
    {"category_id": "cat_materials", "name": "Materials", "slug": "materials", "description": "Semiconductor materials and substrates", "order": 4, "icon": "layers"},
    {"category_id": "cat_packaging", "name": "Packaging", "slug": "packaging", "description": "Advanced packaging technologies", "order": 5, "icon": "package"},
    {"category_id": "cat_design", "name": "Design & EDA", "slug": "design-eda", "description": "IC design and electronic design automation", "order": 6, "icon": "pencil-ruler"},
    {"category_id": "cat_nodes", "name": "Nodes & Scaling", "slug": "nodes-scaling", "description": "Process nodes and Moore's Law", "order": 7, "icon": "trending-down"},
    {"category_id": "cat_foundries", "name": "Foundries & Companies", "slug": "foundries-companies", "description": "Major semiconductor manufacturers", "order": 8, "icon": "building"},
    {"category_id": "cat_reliability", "name": "Reliability & Yield", "slug": "reliability-yield", "description": "Quality, reliability, and manufacturing yield", "order": 9, "icon": "shield-check"},
    {"category_id": "cat_testing", "name": "Testing & Metrology", "slug": "testing-metrology", "description": "Semiconductor testing and measurement", "order": 10, "icon": "microscope"},
]

SEED_TOPICS = [
    {
        "topic_id": "topic_euv",
        "category_id": "cat_manufacturing",
        "title": "EUV Lithography",
        "slug": "euv-lithography",
        "overview": "Extreme Ultraviolet (EUV) lithography is the most advanced patterning technology used in semiconductor manufacturing, enabling feature sizes below 7nm.",
        "content_beginner": """EUV lithography uses extremely short wavelength light (13.5nm) to print incredibly small patterns on silicon wafers. Think of it like using a very fine pen instead of a marker to draw smaller details.

**Why EUV Matters:**
- Enables smaller transistors (more computing power)
- Reduces manufacturing complexity at advanced nodes
- Essential for 7nm and below process nodes

**Key Concepts:**
- **Wavelength**: EUV uses 13.5nm light, much shorter than older 193nm ArF lithography
- **Vacuum Operation**: EUV light is absorbed by air, so the entire system operates in vacuum
- **Reflective Optics**: Unlike traditional lenses, EUV uses mirrors because no material is transparent at this wavelength""",
        "content_advanced": """EUV lithography represents a fundamental shift in semiconductor patterning technology, utilizing 13.5nm wavelength radiation from tin plasma sources.

**Technical Specifications:**
- Wavelength: 13.5nm (compared to 193nm ArF immersion)
- Numerical Aperture: 0.33 NA (High-NA: 0.55 NA)
- Resolution: k1 factor × λ/NA ≈ 13nm half-pitch
- Source Power: 250W+ (production tools)
- Throughput: 125-185 WPH (wafers per hour)

**Stochastic Effects:**
At EUV wavelengths, photon shot noise becomes significant. With ~20,000 photons per resolution element, statistical variations cause:
- Line edge roughness (LER): σ ≈ 2-3nm
- Local critical dimension uniformity (LCDU) degradation
- Stochastic printing failures in tight pitches

**Mask Technology:**
EUV masks are reflective multilayer structures:
- 40 pairs of Mo/Si bilayers (6.9nm period)
- TaN absorber layer
- Defect-free requirement: 0 defects in pattern area
- Pellicle challenges at high power levels

**High-NA EUV:**
- 0.55 NA systems double aerial image contrast
- Enables 8nm half-pitch resolution
- Anamorphic optics with 4x/8x demagnification
- Expected production: 2025-2026""",
        "diagrams": [
            {"type": "mermaid", "content": "graph TD\n    A[Tin Droplet] -->|CO2 Laser| B[Plasma]\n    B -->|13.5nm EUV| C[Collector Mirror]\n    C --> D[Illumination Optics]\n    D --> E[Mask]\n    E --> F[Projection Optics]\n    F --> G[Wafer]", "caption": "EUV Source and Optical Path"}
        ],
        "equations": [
            {"latex": "R = k_1 \\frac{\\lambda}{NA}", "description": "Rayleigh resolution criterion"},
            {"latex": "DoF = k_2 \\frac{\\lambda}{NA^2}", "description": "Depth of focus"},
            {"latex": "\\sigma_{shot} = \\sqrt{\\frac{1}{N_{photons}}}", "description": "Photon shot noise"}
        ],
        "manufacturing_challenges": [
            "Source power and availability (>90% uptime required)",
            "Mask defect inspection and repair",
            "Pellicle survivability at high EUV power",
            "Stochastic defects at tight pitches",
            "Hydrogen contamination management"
        ],
        "applications": ["7nm and below logic", "Advanced DRAM", "3D NAND contact layers", "High-performance computing chips"],
        "advantages": ["Single exposure vs multi-patterning", "Better edge placement accuracy", "Simplified process flow at advanced nodes"],
        "limitations": ["High capital cost ($150M+ per tool)", "Complex infrastructure requirements", "Limited throughput compared to DUV", "Stochastic effects at small features"],
        "related_topics": ["topic_lithography", "topic_gaafet", "topic_asml"],
        "references": [
            {"title": "ASML EUV Technology", "url": "https://www.asml.com/en/technology/euv", "source": "ASML Official"},
            {"title": "EUV Lithography Overview", "url": "https://semiengineering.com/knowledge_centers/lithography/euv/", "source": "Semiconductor Engineering"}
        ],
        "difficulty": "advanced",
        "author": "system",
        "views": 0
    },
    {
        "topic_id": "topic_finfet",
        "category_id": "cat_devices",
        "title": "FinFET Technology",
        "slug": "finfet-technology",
        "overview": "FinFET (Fin Field-Effect Transistor) is a 3D transistor architecture that wraps the gate around the channel on three sides, providing superior electrostatic control.",
        "content_beginner": """FinFET transistors are like building a tall, thin wall (the 'fin') and wrapping a gate around three sides of it. This gives much better control over the current flow compared to flat transistors.

**Why FinFETs Matter:**
- Better on/off switching (less leakage)
- Higher performance at lower power
- Enabled scaling below 22nm

**Key Advantages:**
- **Better Control**: Gate surrounds channel on 3 sides
- **Lower Leakage**: Less current when transistor is off
- **Higher Drive Current**: More current when transistor is on""",
        "content_advanced": """FinFET architecture represents the transition from planar to 3D transistor structures, first introduced in high-volume manufacturing at the 22nm node by Intel (2011).

**Structural Parameters:**
- Fin pitch: 24-54nm (node dependent)
- Fin height: 40-50nm typical
- Fin width: 5-7nm at advanced nodes
- Number of fins: Determines drive strength

**Electrostatics:**
The tri-gate structure provides:
- Subthreshold swing (SS) ≈ 65-70 mV/decade
- DIBL < 50 mV/V
- Effective oxide thickness (EOT) scaling to sub-1nm

**Scaling Challenges:**
- Fin width variability impacts Vt
- Self-heating in narrow fins
- Parasitic capacitance increase
- Contact resistance scaling
- Limited to ~3nm node before transition to GAA""",
        "diagrams": [
            {"type": "mermaid", "content": "graph LR\n    subgraph FinFET Cross-Section\n    A[Source] --> B[Fin Channel]\n    B --> C[Drain]\n    D[Gate] -.wraps.-> B\n    end", "caption": "FinFET Structure"}
        ],
        "equations": [
            {"latex": "I_D = \\mu C_{ox} \\frac{W}{L}(V_{GS}-V_T)V_{DS}", "description": "Drive current (linear region)"},
            {"latex": "SS = \\frac{kT}{q}\\ln(10)(1+\\frac{C_D}{C_{ox}})", "description": "Subthreshold swing"}
        ],
        "manufacturing_challenges": ["Fin etch uniformity", "High aspect ratio fin formation", "Fin pitch scaling", "Work function metal integration"],
        "applications": ["Mobile processors", "High-performance computing", "Graphics processors", "Low-power IoT"],
        "advantages": ["Superior short channel control", "Reduced leakage", "Higher drive current per footprint", "Multi-fin flexibility"],
        "limitations": ["Quantized drive strength (per fin)", "Complex manufacturing", "Self-heating issues", "Parasitic capacitance"],
        "related_topics": ["topic_gaafet", "topic_planar"],
        "references": [
            {"title": "FinFET Technology Overview", "url": "https://ieeexplore.ieee.org/finfet", "source": "IEEE"}
        ],
        "difficulty": "intermediate",
        "author": "system",
        "views": 0
    },
    {
        "topic_id": "topic_gaafet",
        "category_id": "cat_devices",
        "title": "GAAFET / Nanosheet Transistors",
        "slug": "gaafet-nanosheet",
        "overview": "Gate-All-Around FET (GAAFET) or nanosheet transistors wrap the gate completely around the channel, providing the ultimate electrostatic control for sub-3nm nodes.",
        "content_beginner": """GAAFET transistors take the idea of FinFETs even further. Instead of wrapping a gate around three sides of a fin, GAA transistors wrap the gate completely around the channel - like putting your hand completely around a cylinder.

**Evolution:**
- Planar → 1 side of control
- FinFET → 3 sides of control
- GAAFET → 4 sides (all-around) control

**Benefits:**
- Even better on/off control
- Needed for smallest transistors (3nm and below)
- More flexible design options""",
        "content_advanced": """GAAFET represents the next evolution in transistor architecture, with Samsung first deploying at 3nm (GAE) and TSMC following at N2.

**Nanosheet Architecture:**
- Stacked horizontal nanosheets (2-4 sheets typical)
- Sheet width: 5-50nm (tunable drive strength)
- Sheet thickness: 5-7nm
- Vertical sheet spacing: 10-12nm

**Electrostatic Advantages:**
- SS approaching 60 mV/decade theoretical limit
- DIBL < 30 mV/V
- Superior Ioff/Ion ratio
- Variable sheet width enables continuous drive strength

**Manufacturing Process:**
1. Epitaxial Si/SiGe superlattice growth
2. Fin patterning
3. Inner spacer formation
4. SiGe selective removal (channel release)
5. Gate-all-around high-k/metal gate deposition

**Challenges:**
- Inner spacer formation and uniformity
- Sheet release etch selectivity
- Parasitic capacitance management
- Contact resistance to thin sheets""",
        "diagrams": [],
        "equations": [
            {"latex": "I_{eff} = n_{sheets} \\times 2(W_{sheet} + t_{sheet}) \\times I_{per\\_perimeter}", "description": "Effective drive current with n nanosheets"}
        ],
        "manufacturing_challenges": ["Superlattice epitaxy uniformity", "Channel release selectivity", "Inner spacer integration", "Work function metal gap fill"],
        "applications": ["3nm and beyond logic", "High-performance mobile", "Data center chips", "AI accelerators"],
        "advantages": ["Variable drive strength (sheet width)", "Best electrostatic control", "Lower operating voltage", "Extendable architecture"],
        "limitations": ["Complex manufacturing", "Higher capacitance per area", "Thermal challenges", "Cost increase"],
        "related_topics": ["topic_finfet", "topic_cfet"],
        "references": [
            {"title": "Samsung 3nm GAA", "url": "https://semiconductor.samsung.com/foundry/", "source": "Samsung Foundry"}
        ],
        "difficulty": "advanced",
        "author": "system",
        "views": 0
    },
    {
        "topic_id": "topic_cowos",
        "category_id": "cat_packaging",
        "title": "CoWoS Packaging",
        "slug": "cowos-packaging",
        "overview": "Chip-on-Wafer-on-Substrate (CoWoS) is TSMC's advanced 2.5D packaging technology that enables high-bandwidth integration of multiple chiplets.",
        "content_beginner": """CoWoS is like building a multi-story parking garage for chips. Instead of putting everything on one level, you can stack and connect multiple chips together using a special 'interposer' layer.

**Why CoWoS:**
- Connect different chips together (CPU + Memory)
- Much faster communication between chips
- Essential for AI chips that need lots of memory bandwidth

**Key Parts:**
- **Chiplets**: Individual small chips
- **Interposer**: Silicon layer that connects chiplets
- **Substrate**: The foundation that connects to the circuit board""",
        "content_advanced": """CoWoS represents TSMC's premier 2.5D integration platform, critical for HBM integration in AI accelerators.

**Technology Variants:**
- **CoWoS-S**: Silicon interposer (original)
- **CoWoS-R**: Organic redistribution layer
- **CoWoS-L**: Local silicon interconnect (hybrid)

**Silicon Interposer Specifications:**
- 65nm or 12nm process for interposer
- Up to 6 reticle size (CoWoS-L allows larger)
- TSV pitch: 9-40μm
- RDL layers: 3-4 Cu layers
- Microbump pitch: 40-55μm

**HBM Integration:**
- HBM3/HBM3E: 1024-bit interface
- Bandwidth: >800 GB/s per HBM stack
- Up to 6-8 HBM stacks per package
- CoWoS-S supports largest HBM configurations

**Thermal Considerations:**
- TDP >700W for large AI packages
- Requires advanced thermal solutions
- Integrated heat spreaders
- Backside metallization options""",
        "diagrams": [],
        "equations": [
            {"latex": "BW_{total} = n_{HBM} \\times 1024 \\times f_{HBM}", "description": "Total HBM bandwidth calculation"}
        ],
        "manufacturing_challenges": ["Large interposer warpage", "TSV reliability", "Die-to-die alignment", "Thermal management at scale"],
        "applications": ["AI/ML accelerators (NVIDIA H100, AMD MI300)", "High-performance computing", "Networking ASICs", "Graphics processors"],
        "advantages": ["Massive memory bandwidth", "Heterogeneous integration", "Shorter interconnects", "Better power efficiency"],
        "limitations": ["High cost", "Limited to single foundry ecosystem", "Capacity constraints", "Complex supply chain"],
        "related_topics": ["topic_hbm", "topic_chiplet"],
        "references": [
            {"title": "TSMC CoWoS Technology", "url": "https://www.tsmc.com/english/dedicatedFoundry/technology/cowos", "source": "TSMC"}
        ],
        "difficulty": "intermediate",
        "author": "system",
        "views": 0
    },
    {
        "topic_id": "topic_tsmc",
        "category_id": "cat_foundries",
        "title": "TSMC",
        "slug": "tsmc",
        "overview": "Taiwan Semiconductor Manufacturing Company (TSMC) is the world's largest dedicated semiconductor foundry, manufacturing chips for Apple, NVIDIA, AMD, and many others.",
        "content_beginner": """TSMC is like the world's most advanced chip factory. They don't design chips themselves - they make chips for other companies.

**Key Facts:**
- Founded: 1987 in Taiwan
- Market Share: ~55% of global foundry
- Customers: Apple, NVIDIA, AMD, Qualcomm, etc.
- Leading Edge: 3nm in production, 2nm coming soon

**Why TSMC Matters:**
- Makes most of the world's advanced chips
- Only company with high-volume EUV production
- Essential for smartphones, data centers, AI""",
        "content_advanced": """TSMC dominates advanced semiconductor manufacturing with unmatched scale and technology leadership.

**Process Node Portfolio:**
- **N3/N3E/N3P**: 3nm FinFET family
- **N2**: 2nm nanosheet (2025)
- **A16**: Backside power delivery (2026)

**Manufacturing Scale:**
- 13 fabs (including JVs)
- >2M 300mm wafer capacity/year
- R&D: >10% revenue (~$4-5B/year)

**Technology Differentiators:**
- Highest EUV layer count in production
- Lowest defect density at advanced nodes
- Comprehensive design ecosystem (OIP)
- Advanced packaging leadership (CoWoS, InFO, SoIC)

**Geographic Expansion:**
- Arizona Fab: 4nm/3nm (2025)
- Japan Fab: Specialty technologies
- Germany Fab: Automotive (announced)

**Competitive Position:**
- 2+ year lead over Samsung at cutting edge
- Intel catching up with Intel 18A
- Only stable high-volume EUV production""",
        "diagrams": [],
        "equations": [],
        "manufacturing_challenges": ["Geopolitical risk (Taiwan location)", "US/China tensions", "Capacity expansion speed", "EUV tool availability"],
        "applications": ["Consumer electronics", "Data center", "Automotive", "AI accelerators", "Mobile"],
        "advantages": ["Technology leadership", "Manufacturing excellence", "Scale advantages", "Ecosystem lock-in"],
        "limitations": ["Concentration risk in Taiwan", "High capital intensity", "Customer concentration", "Talent competition"],
        "related_topics": ["topic_samsung_foundry", "topic_intel_foundry"],
        "references": [
            {"title": "TSMC Technology", "url": "https://www.tsmc.com/english/dedicatedFoundry/technology", "source": "TSMC Official"}
        ],
        "difficulty": "beginner",
        "author": "system",
        "views": 0
    }
]


@router.get("/categories")
async def get_categories():
    """Get all encyclopedia categories"""
    db = await get_db()
    
    categories = await db.encyclopedia_categories.find({}, {"_id": 0}).sort("order", 1).to_list(100)
    
    if not categories:
        # Seed initial data
        for cat in SEED_CATEGORIES:
            await db.encyclopedia_categories.insert_one(cat)
        categories = SEED_CATEGORIES
    
    return categories


@router.get("/topics")
async def get_topics(
    category_id: Optional[str] = None,
    search: Optional[str] = None,
    difficulty: Optional[str] = None,
    limit: int = Query(default=50, le=100),
    offset: int = 0
):
    """Get encyclopedia topics with filtering"""
    db = await get_db()
    
    # Build query
    query = {}
    if category_id:
        query["category_id"] = category_id
    if difficulty:
        query["difficulty"] = difficulty
    
    # Check if topics exist, seed if not
    count = await db.encyclopedia_topics.count_documents({})
    if count == 0:
        for topic in SEED_TOPICS:
            topic["created_at"] = datetime.now(timezone.utc).isoformat()
            topic["updated_at"] = datetime.now(timezone.utc).isoformat()
            await db.encyclopedia_topics.insert_one(topic)
    
    if search:
        # Text search
        query["$text"] = {"$search": search}
        topics = await db.encyclopedia_topics.find(
            query,
            {"_id": 0, "score": {"$meta": "textScore"}}
        ).sort([("score", {"$meta": "textScore"})]).skip(offset).limit(limit).to_list(limit)
    else:
        topics = await db.encyclopedia_topics.find(
            query,
            {"_id": 0}
        ).sort("title", 1).skip(offset).limit(limit).to_list(limit)
    
    return topics


@router.get("/topics/{slug}")
async def get_topic_by_slug(slug: str, difficulty: str = "intermediate"):
    """Get a single topic by slug"""
    db = await get_db()
    
    topic = await db.encyclopedia_topics.find_one(
        {"slug": slug},
        {"_id": 0}
    )
    
    if not topic:
        raise HTTPException(status_code=404, detail="Topic not found")
    
    # Increment view count
    await db.encyclopedia_topics.update_one(
        {"slug": slug},
        {"$inc": {"views": 1}}
    )
    
    # Get related topics
    if topic.get("related_topics"):
        related = await db.encyclopedia_topics.find(
            {"topic_id": {"$in": topic["related_topics"]}},
            {"_id": 0, "topic_id": 1, "title": 1, "slug": 1, "overview": 1}
        ).to_list(10)
        topic["related_topics_data"] = related
    
    return topic


@router.get("/topics/{slug}/pdf")
async def export_topic_pdf(slug: str, difficulty: str = "intermediate"):
    """Export encyclopedia topic as PDF"""
    from fastapi.responses import StreamingResponse
    from pdf_export import generate_encyclopedia_pdf
    
    db = await get_db()
    
    topic = await db.encyclopedia_topics.find_one(
        {"slug": slug},
        {"_id": 0}
    )
    
    if not topic:
        raise HTTPException(status_code=404, detail="Topic not found")
    
    # Generate PDF
    pdf_buffer = generate_encyclopedia_pdf(topic, difficulty)
    
    # Clean filename
    filename = f"{slug}-{difficulty}.pdf"
    
    return StreamingResponse(
        pdf_buffer,
        media_type="application/pdf",
        headers={
            "Content-Disposition": f"attachment; filename={filename}"
        }
    )


@router.get("/tree")
async def get_knowledge_tree():
    """Get hierarchical knowledge tree structure"""
    db = await get_db()
    
    # Get categories
    categories = await db.encyclopedia_categories.find({}, {"_id": 0}).sort("order", 1).to_list(100)
    
    if not categories:
        for cat in SEED_CATEGORIES:
            await db.encyclopedia_categories.insert_one(cat)
        categories = SEED_CATEGORIES
    
    # Get topics per category
    tree = []
    for cat in categories:
        topics = await db.encyclopedia_topics.find(
            {"category_id": cat["category_id"]},
            {"_id": 0, "topic_id": 1, "title": 1, "slug": 1}
        ).sort("title", 1).to_list(100)
        
        tree.append({
            **cat,
            "topics": topics
        })
    
    return tree


@router.get("/search")
async def search_encyclopedia(q: str, limit: int = Query(default=20, le=50)):
    """Search across encyclopedia"""
    db = await get_db()
    
    results = []
    
    # Search topics
    topics = await db.encyclopedia_topics.find(
        {"$text": {"$search": q}},
        {"_id": 0, "score": {"$meta": "textScore"}}
    ).sort([("score", {"$meta": "textScore"})]).limit(limit).to_list(limit)
    
    for topic in topics:
        results.append({
            "type": "topic",
            "id": topic["topic_id"],
            "title": topic["title"],
            "slug": topic["slug"],
            "excerpt": topic["overview"][:200],
            "category_id": topic["category_id"]
        })
    
    return results
