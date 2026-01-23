"""
Extended Encyclopedia Topics - Part 4 (Final)
Last batch to reach 100+ topics
"""

EXTENDED_TOPICS_PART4 = [
    # ==================== MORE MANUFACTURING ====================
    {
        "topic_id": "topic_esd_protection",
        "category_id": "cat_manufacturing",
        "title": "ESD Protection Design",
        "slug": "esd-protection-design",
        "overview": "ESD protection prevents electrostatic discharge damage to sensitive circuits. On-chip ESD structures safely shunt transient currents to ground, with designs specified by HBM, CDM, and MM models.",
        "content_beginner": """ESD protection keeps static electricity from destroying chips.

**The Problem:**
- Static shock can be thousands of volts
- Transistors operate at ~1V or less
- Even small ESD can damage gates
- Chips must survive handling and use

**Protection Methods:**
- Clamp circuits at I/O pads
- Diodes to power rails
- SCR (Silicon Controlled Rectifier)
- Power clamps for supply ESD

**ESD Standards:**
- HBM: Human Body Model (2-4kV)
- CDM: Charged Device Model (500V)
- MM: Machine Model (200V)""",
        "content_advanced": """ESD protection requires careful design to balance protection vs performance.

**ESD Protection Devices:**
| Device | Trigger | Clamping | Speed |
|--------|---------|----------|-------|
| Diode | 0.7V | ~1V | Fast |
| GGNMOS | ~6V | ~3-4V | Medium |
| SCR | ~8V | ~1.5V | Slow |
| GCNMOS | ~8V | ~4V | Medium |

**Design Considerations:**
- Trigger voltage < oxide breakdown
- Holding voltage > Vdd
- On-resistance for current handling
- Capacitance impact on signal
- Latch-up immunity

**CDM Protection:**
- Local clamps at every I/O
- Low inductance ground path
- Fast turn-on required
- Most challenging ESD type""",
        "diagrams": [],
        "equations": [
            {"latex": "V_{t1} < V_{ox\\_BD}", "description": "Trigger before damage"},
            {"latex": "I_{t2} = \\frac{V_{HBM}}{R_{HBM}}", "description": "ESD current level"}
        ],
        "manufacturing_challenges": ["Area overhead", "Capacitance impact", "Latch-up avoidance"],
        "applications": ["All I/O pins", "Power supplies", "Internal sensitive circuits"],
        "advantages": ["Essential protection", "Standard designs available", "Well characterized"],
        "limitations": ["Area cost", "Capacitance", "Speed impact"],
        "related_topics": ["topic_reliability", "topic_dft", "topic_mosfet_basics"],
        "references": [],
        "difficulty": "intermediate",
        "author": "system",
        "views": 0
    },
    {
        "topic_id": "topic_damascene",
        "category_id": "cat_manufacturing",
        "title": "Damascene Process",
        "slug": "damascene-process",
        "overview": "Damascene creates copper interconnects by etching trenches in dielectric, depositing metal, then polishing flat. Single and dual damascene variants enable multi-level metallization in modern ICs.",
        "content_beginner": """Damascene is the process used to create copper wiring inside chips.

**Why Damascene?**
- Copper can't be etched like aluminum
- Instead, we etch trenches in insulator
- Fill trenches with copper
- Polish flat to remove excess

**Process Steps:**
1. Deposit and pattern dielectric
2. Etch trenches and vias
3. Deposit barrier layer
4. Deposit copper (seed + electroplate)
5. CMP to remove overburden

**Single vs Dual Damascene:**
- Single: One level at a time
- Dual: Via and trench together
- Dual saves process steps""",
        "content_advanced": """Dual damascene integrates via and trench formation for efficiency.

**Dual Damascene Schemes:**
| Scheme | Via First | Trench First |
|--------|-----------|--------------|
| Litho | Via → Trench | Trench → Via |
| Etch | Via → Trench | Trench → Via |
| Advantage | Alignment | Profile control |

**Process Integration:**
1. Low-K dielectric deposition
2. Hard mask deposition
3. Via lithography and etch
4. Trench lithography and etch
5. Barrier/seed PVD
6. Copper electroplating
7. CMP planarization

**Key Challenges:**
- Via-to-trench alignment
- Profile control
- Barrier continuity
- Void-free fill
- Low-K damage""",
        "diagrams": [],
        "equations": [
            {"latex": "AR = \\frac{Height}{Width}", "description": "Aspect ratio"},
            {"latex": "Fill = f(AR, chemistry)", "description": "Fill capability"}
        ],
        "manufacturing_challenges": ["Aspect ratio fill", "Barrier coverage", "CMP uniformity"],
        "applications": ["All copper interconnects", "Advanced nodes", "Memory"],
        "advantages": ["Enables copper use", "Good planarity", "Scalable"],
        "limitations": ["Process complexity", "Low-K integration", "Barrier scaling"],
        "related_topics": ["topic_copper_interconnects", "topic_cmp", "topic_low_k"],
        "references": [],
        "difficulty": "intermediate",
        "author": "system",
        "views": 0
    },
    {
        "topic_id": "topic_opc",
        "category_id": "cat_manufacturing",
        "title": "Optical Proximity Correction",
        "slug": "optical-proximity-correction",
        "overview": "OPC modifies mask patterns to compensate for optical distortions during lithography. Sub-resolution assist features and systematic biases ensure printed patterns match design intent.",
        "content_beginner": """OPC adjusts mask patterns so the final chip patterns print correctly.

**The Problem:**
- Light bends around corners (diffraction)
- Printed patterns don't match mask exactly
- Small features print differently than large
- Nearby features affect each other

**OPC Solutions:**
- Add small features to corners (serifs)
- Adjust line widths (biasing)
- Add dummy shapes (SRAF)
- Never print, but help main features

**Why It's Essential:**
- Required below ~180nm
- Computer-generated corrections
- Mask much more complex than design
- Enables continued scaling""",
        "content_advanced": """OPC complexity increases dramatically with shrinking design rules.

**OPC Types:**
| Type | Method | Application |
|------|--------|-------------|
| Rule-based | Fixed rules | Simple layers |
| Model-based | Simulation | Critical layers |
| ILT | Inverse litho | EUV/leading edge |

**OPC Features:**
- Corner rounding compensation
- Line-end extensions
- Sub-resolution assist features (SRAF)
- Negative tone development adjustments

**Computational Requirements:**
- Billions of corrections per chip
- Days of computation time
- Massive parallel processing
- GPU acceleration common

**Verification:**
- Model-based simulation
- Critical dimension checking
- Process window analysis
- Mask rule checking""",
        "diagrams": [],
        "equations": [
            {"latex": "CD = k_1 \\frac{\\lambda}{NA}", "description": "Minimum feature size"},
            {"latex": "MEEF = \\frac{\\partial CD_{wafer}}{\\partial CD_{mask}}", "description": "Mask error factor"}
        ],
        "manufacturing_challenges": ["Computation time", "Model accuracy", "Mask complexity"],
        "applications": ["All lithography layers", "Critical dimension control"],
        "advantages": ["Enables scaling", "Automated", "Predictable results"],
        "limitations": ["Computation cost", "Mask complexity", "Model limitations"],
        "related_topics": ["topic_euv_lithography", "topic_photomask", "topic_duv_lithography"],
        "references": [],
        "difficulty": "intermediate",
        "author": "system",
        "views": 0
    },
    # ==================== MORE MATERIALS ====================
    {
        "topic_id": "topic_photoresist",
        "category_id": "cat_materials",
        "title": "Photoresist Materials",
        "slug": "photoresist-materials",
        "overview": "Photoresists are light-sensitive polymers that transfer circuit patterns to wafers. Chemically amplified resists (CAR) dominate DUV, while EUV requires new metal-oxide resist platforms.",
        "content_beginner": """Photoresist is the light-sensitive coating that captures chip patterns.

**How It Works:**
1. Coat wafer with liquid photoresist
2. Expose to patterned light
3. Light changes resist chemistry
4. Developer removes exposed (or unexposed) areas
5. Pattern remains for etching

**Resist Types:**
- **Positive:** Exposed area removed
- **Negative:** Exposed area stays
- **Chemically amplified:** Modern standard

**EUV Challenge:**
- EUV photons are different
- Need new resist chemistries
- Metal-oxide resists emerging
- Stochastic effects critical""",
        "content_advanced": """Advanced resists balance resolution, sensitivity, and line edge roughness.

**Resist Platforms:**
| Platform | Chemistry | Resolution | Use |
|----------|-----------|------------|-----|
| DNQ | Diazonaphthoquinone | 500nm+ | Legacy |
| CAR-DUV | PAG + polymer | 30nm | DUV |
| CAR-EUV | EUV-optimized | 20nm | EUV |
| Metal-oxide | Organo-metallic | <15nm | Next-gen |

**Key Parameters:**
- Sensitivity: mJ/cm²
- Contrast: γ
- Resolution: Smallest feature
- LER/LWR: Edge roughness

**Stochastic Effects:**
- Shot noise (photon statistics)
- Acid diffusion blur
- Resist inhomogeneity
- Pattern collapse

**Processing:**
- Spin coating uniformity
- PAB (post-apply bake)
- PEB (post-exposure bake)
- Development control""",
        "diagrams": [],
        "equations": [
            {"latex": "D = \\frac{E_0}{I \\times t}", "description": "Resist dose"},
            {"latex": "\\gamma = \\frac{1}{\\log(E_0/E_1)}", "description": "Resist contrast"}
        ],
        "manufacturing_challenges": ["Stochastic defects", "Metal contamination", "Process window"],
        "applications": ["All lithography", "Pattern transfer", "Direct patterning"],
        "advantages": ["Essential for lithography", "High resolution available", "Well characterized"],
        "limitations": ["Defectivity", "Dose requirements", "Cost of advanced resists"],
        "related_topics": ["topic_euv_lithography", "topic_duv_lithography", "topic_etch"],
        "references": [],
        "difficulty": "intermediate",
        "author": "system",
        "views": 0
    },
    {
        "topic_id": "topic_silicide",
        "category_id": "cat_materials",
        "title": "Silicide Contacts",
        "slug": "silicide-contacts",
        "overview": "Silicides form low-resistance contacts between silicon and metal interconnects. Nickel silicide (NiSi) dominates advanced nodes, formed through self-aligned salicide processes.",
        "content_beginner": """Silicides create the electrical connection between transistors and metal wires.

**What is Silicide?**
- Metal reacted with silicon
- Forms at source, drain, and gate
- Much lower resistance than silicon
- Essential for fast transistors

**Common Silicides:**
- **TiSi2:** Older processes
- **CoSi2:** 90nm-45nm nodes
- **NiSi:** 45nm and below

**Salicide Process:**
1. Deposit metal on wafer
2. Heat to react with exposed silicon
3. Unreacted metal washed away
4. Silicide only where silicon was

**Why It Matters:**
- Reduces parasitic resistance
- Self-aligned (no extra masking)
- Critical for device performance""",
        "content_advanced": """Silicide scaling faces challenges with FinFET and GAA architectures.

**Silicide Properties:**
| Silicide | Resistivity | Stability | Node |
|----------|-------------|-----------|------|
| TiSi2 | 15 µΩ-cm | Medium | >180nm |
| CoSi2 | 18 µΩ-cm | Good | 90-45nm |
| NiSi | 14 µΩ-cm | Best | <45nm |
| NiPtSi | 15 µΩ-cm | Best | <28nm |

**Formation Kinetics:**
- Nucleation temperature
- Growth rate vs temperature
- Phase transitions
- Interface quality

**Advanced Challenges:**
- FinFET wrap-around contact
- GAA inner spacer regions
- Ultra-thin body effects
- Epitaxial source/drain integration""",
        "diagrams": [],
        "equations": [
            {"latex": "R_c = \\rho_c / A", "description": "Contact resistance"},
            {"latex": "R_{sh} = \\rho / t", "description": "Sheet resistance"}
        ],
        "manufacturing_challenges": ["Uniformity on 3D structures", "Thermal budget", "Junction penetration"],
        "applications": ["CMOS transistors", "Gate contacts", "Source/drain contacts"],
        "advantages": ["Self-aligned", "Low resistance", "Mature process"],
        "limitations": ["Thermal stability", "3D structure challenges", "Junction depth limits"],
        "related_topics": ["topic_finfet", "topic_gaafet", "topic_annealing"],
        "references": [],
        "difficulty": "intermediate",
        "author": "system",
        "views": 0
    },
    # ==================== MORE DESIGN ====================
    {
        "topic_id": "topic_standard_cells",
        "category_id": "cat_design",
        "title": "Standard Cell Libraries",
        "slug": "standard-cell-libraries",
        "overview": "Standard cells are pre-designed logic elements (inverters, NAND, flip-flops) enabling automated chip design. Cell libraries are characterized for timing, power, and area across process corners.",
        "content_beginner": """Standard cells are pre-made building blocks for chip design.

**What Are Standard Cells?**
- Pre-designed logic gates
- Fixed height, variable width
- Snap together in rows
- Automated by software

**Common Cell Types:**
- Inverter, buffer
- NAND, NOR, AND, OR
- XOR, MUX
- Flip-flops, latches
- Clock cells

**Why Standard Cells:**
- Much faster than custom design
- Predictable performance
- Pre-verified for manufacturing
- Tools handle placement/routing

**Cell Library Contents:**
- Layout (shapes)
- Timing models
- Power models
- Verification views""",
        "content_advanced": """Standard cell libraries are extensively characterized for multiple PVT corners.

**Cell Library Components:**
| View | Content | Use |
|------|---------|-----|
| LEF | Abstract layout | P&R |
| Liberty (.lib) | Timing/power | Synthesis/STA |
| GDS | Full layout | Signoff |
| CDL/SPICE | Netlist | LVS/sim |
| Verilog | Behavior | Verification |

**Characterization:**
- Multiple corners (FF, TT, SS)
- Multiple voltages (0.9V-1.1V typical)
- Multiple temperatures (-40 to 125°C)
- CCS/ECSM advanced modeling

**Advanced Features:**
- Multi-Vth cells (HVT, SVT, LVT)
- Multi-drive strength versions
- Clock cells with low skew
- ECO cells for late changes
- Low power cells (sleep, retention)""",
        "diagrams": [],
        "equations": [
            {"latex": "Delay = a + b \\times C_{load}", "description": "Linear delay model"},
            {"latex": "P_{leak} = f(V_{th}, T)", "description": "Leakage vs threshold"}
        ],
        "manufacturing_challenges": [],
        "applications": ["All digital design", "SoC development", "ASIC design"],
        "advantages": ["Fast design cycle", "Predictable results", "Automation friendly"],
        "limitations": ["Not optimal for all functions", "Area overhead vs custom", "Timing model accuracy"],
        "related_topics": ["topic_physical_design", "topic_logic_synthesis", "topic_timing_analysis"],
        "references": [],
        "difficulty": "intermediate",
        "author": "system",
        "views": 0
    },
    {
        "topic_id": "topic_clock_design",
        "category_id": "cat_design",
        "title": "Clock Distribution Design",
        "slug": "clock-distribution-design",
        "overview": "Clock distribution delivers timing signals across chips with minimal skew and jitter. CTS builds balanced buffer trees, while advanced designs use mesh or H-tree structures for critical clocks.",
        "content_beginner": """Clock distribution gets the timing signal to every flip-flop in the chip.

**Why It's Hard:**
- Clock must reach millions of flip-flops
- Must arrive at nearly the same time
- Signal degrades over distance
- Uses significant power

**Clock Tree Structure:**
- Start from clock source
- Branch into smaller trees
- Buffers restore signal
- Reaches every register

**Key Goals:**
- Low skew (arrival time difference)
- Low jitter (cycle-to-cycle variation)
- Low power
- Meet timing at all corners""",
        "content_advanced": """Clock tree synthesis balances skew, power, and robustness.

**Clock Structures:**
| Type | Skew | Power | Use |
|------|------|-------|-----|
| H-tree | Best | High | Critical |
| Mesh | Low | Highest | Very critical |
| Standard CTS | Good | Medium | General |
| Low-power | Medium | Lowest | Mobile |

**CTS Targets:**
- Insertion delay: <500ps
- Skew: <30ps at advanced nodes
- Useful skew exploitation
- Power: 30-40% of chip dynamic

**Advanced Techniques:**
- Multi-source CTS
- Clock mesh for low skew
- Adaptive clock distribution
- Resonant clocking research""",
        "diagrams": [],
        "equations": [
            {"latex": "Skew = T_{max} - T_{min}", "description": "Clock skew"},
            {"latex": "T_{margin} = T_{clk} - T_{data} - T_{skew}", "description": "Timing margin"}
        ],
        "manufacturing_challenges": [],
        "applications": ["All synchronous design", "High-performance chips", "Low-power design"],
        "advantages": ["Enables synchronous operation", "Automated synthesis", "Predictable"],
        "limitations": ["Significant power", "Complexity at high frequency", "Variation sensitivity"],
        "related_topics": ["topic_physical_design", "topic_timing_analysis", "topic_power_analysis"],
        "references": [],
        "difficulty": "intermediate",
        "author": "system",
        "views": 0
    },
    # ==================== MORE PACKAGING ====================
    {
        "topic_id": "topic_substrate",
        "category_id": "cat_packaging",
        "title": "Package Substrates",
        "slug": "package-substrates",
        "overview": "Package substrates provide mechanical support, electrical routing, and thermal management between dies and boards. Advanced substrates use fine-pitch RDL and embedded components.",
        "content_beginner": """Package substrates are the circuit boards inside chip packages.

**What Substrates Do:**
- Support the chip mechanically
- Route signals to package pins
- Spread heat from chip
- Connect chip to main board

**Substrate Types:**
- **Organic:** Epoxy-glass laminate (common)
- **Ceramic:** Alumina, LTCC (high-end)
- **Silicon:** Silicon interposers (2.5D)

**Key Features:**
- Multiple metal layers (8-16+)
- Micro-vias connect layers
- Fine lines for routing
- Embedded passives possible""",
        "content_advanced": """High-density substrates enable advanced packaging with fine features.

**Substrate Technologies:**
| Type | L/S (µm) | Layers | Application |
|------|----------|--------|-------------|
| Standard | 15/15 | 4-8 | Consumer |
| HDI | 10/10 | 8-12 | Mobile/HPC |
| Ultra-HDI | 5/5 | 12-20 | Advanced |
| Silicon | 0.4/0.4 | 4-8 | 2.5D/3D |

**Manufacturing Process:**
- Core lamination
- Laser drilling
- Electroless/electrolytic plating
- SAP (semi-additive process)
- mSAP for fine lines

**Advanced Features:**
- Embedded bridge die
- Cavity for die
- Integrated passives
- Fine pitch ball grid array""",
        "diagrams": [],
        "equations": [
            {"latex": "Z_0 = \\frac{87}{\\sqrt{\\epsilon_r+1.41}} \\ln\\frac{5.98h}{0.8w+t}", "description": "Microstrip impedance"},
            {"latex": "R_{thermal} = \\frac{t}{kA}", "description": "Thermal resistance"}
        ],
        "manufacturing_challenges": ["Fine line/space", "Warpage", "Registration", "Via reliability"],
        "applications": ["All IC packages", "Flip chip", "BGA", "Advanced packaging"],
        "advantages": ["Enables high I/O", "Fine routing", "Good thermal"],
        "limitations": ["Cost for fine pitch", "Warpage", "Yield at fine features"],
        "related_topics": ["topic_flip_chip", "topic_cowos", "topic_fan_out"],
        "references": [],
        "difficulty": "intermediate",
        "author": "system",
        "views": 0
    },
    {
        "topic_id": "topic_thermal_management",
        "category_id": "cat_packaging",
        "title": "Thermal Management",
        "slug": "thermal-management",
        "overview": "Thermal management removes heat from chips to maintain reliability and performance. Solutions range from simple heat spreaders to liquid cooling for high-power processors.",
        "content_beginner": """Thermal management keeps chips cool so they work reliably.

**Why Cooling Matters:**
- Chips generate lots of heat
- Hot chips fail faster
- Performance drops with temperature
- Must stay below ~100°C

**Cooling Methods:**

**Passive:**
- Heat spreader (copper/aluminum)
- Heat sink (fins for air cooling)
- Thermal interface material (TIM)

**Active:**
- Fans (forced air)
- Liquid cooling
- Heat pipes
- Thermoelectric coolers

**Heat Path:**
Die → TIM → Heat spreader → TIM2 → Heat sink → Air""",
        "content_advanced": """Advanced thermal solutions address increasing power density.

**Thermal Interface Materials:**
| Type | Thermal Conductivity | Thickness |
|------|---------------------|-----------|
| Thermal paste | 1-5 W/mK | 50-100µm |
| Thermal pad | 3-8 W/mK | 0.5-2mm |
| Indium | 80 W/mK | 25-50µm |
| Solder | 50-60 W/mK | 10-25µm |

**Advanced Cooling:**
- Direct liquid cooling
- Immersion cooling
- Microfluidic cooling
- Phase change materials

**Thermal Metrics:**
- θ_JA: Junction to ambient
- θ_JC: Junction to case
- ψ_JT: Junction to top
- Power density: W/mm²""",
        "diagrams": [],
        "equations": [
            {"latex": "T_j = T_a + P \\times R_{\\theta JA}", "description": "Junction temperature"},
            {"latex": "Q = k A \\frac{\\Delta T}{t}", "description": "Heat conduction"}
        ],
        "manufacturing_challenges": ["TIM application", "Heat sink attach", "Thermal cycling reliability"],
        "applications": ["CPUs", "GPUs", "Power electronics", "Data centers"],
        "advantages": ["Enables high performance", "Improves reliability", "Many solutions available"],
        "limitations": ["Cost", "Size", "Power for active cooling"],
        "related_topics": ["topic_reliability", "topic_ai_chips", "topic_packaging"],
        "references": [],
        "difficulty": "beginner",
        "author": "system",
        "views": 0
    },
    # ==================== MORE NODES ====================
    {
        "topic_id": "topic_moore_law",
        "category_id": "cat_nodes",
        "title": "Moore's Law",
        "slug": "moores-law",
        "overview": "Moore's Law observes that transistor density doubles approximately every two years. This 1965 prediction guided industry scaling for decades, though the pace has slowed and methods evolved.",
        "content_beginner": """Moore's Law is the observation that chip complexity doubles every couple of years.

**The Observation:**
- Gordon Moore (Intel co-founder), 1965
- Transistor count doubles ~every 2 years
- Guided industry roadmap for decades
- More a business target than physics law

**What It Enabled:**
- Smaller, faster transistors
- More functionality per chip
- Lower cost per transistor
- The entire digital revolution

**Is It Still Valid?**
- Pure scaling has slowed
- New approaches continue progress
- 3D stacking, chiplets, new materials
- 'More than Moore' innovation""",
        "content_advanced": """Moore's Law evolution reflects changing scaling paradigms.

**Scaling History:**
| Era | Method | Improvement |
|-----|--------|-------------|
| 1970s | Dennard scaling | 50%/node |
| 1990s | Architectural | 2x/2 years |
| 2000s | Multi-core | Parallel |
| 2010s | FinFET | New architecture |
| 2020s | GAA + Packaging | Heterogeneous |

**Original vs Current:**
- Original: 2x transistors/year (1965)
- Revised: 2x transistors/2 years (1975)
- Current: ~2x/2.5-3 years

**Beyond Moore:**
- More Moore: Continue scaling
- More than Moore: Add functionality
- Beyond CMOS: New devices
- System scaling: Chiplets, 3D""",
        "diagrams": [],
        "equations": [
            {"latex": "N(t) = N_0 \\times 2^{t/T}", "description": "Transistor count growth"},
            {"latex": "Cost/transistor \\propto 1/N", "description": "Cost reduction"}
        ],
        "manufacturing_challenges": ["Physical limits", "Cost escalation", "Power density"],
        "applications": ["Industry planning", "Technology roadmaps", "Economic forecasting"],
        "advantages": ["Self-fulfilling roadmap", "Investment guidance", "Innovation driver"],
        "limitations": ["Physical limits approaching", "Economic limits", "Power wall"],
        "related_topics": ["topic_3nm", "topic_2nm", "topic_chiplet"],
        "references": [],
        "difficulty": "beginner",
        "author": "system",
        "views": 0
    },
    {
        "topic_id": "topic_high_na_euv",
        "category_id": "cat_nodes",
        "title": "High-NA EUV Lithography",
        "slug": "high-na-euv-lithography",
        "overview": "High-NA EUV increases the numerical aperture from 0.33 to 0.55, enabling sub-8nm resolution for 2nm nodes and beyond. It requires new optics, masks, and resist platforms from ASML.",
        "content_beginner": """High-NA EUV is the next generation of extreme ultraviolet lithography.

**What's Different:**
- Larger lens (higher NA = 0.55)
- Better resolution capability
- Can print smaller features
- Needed for 2nm and beyond

**Why It's Needed:**
- Current EUV has limits
- Multi-patterning is expensive
- High-NA extends single exposure
- Continues scaling roadmap

**Challenges:**
- Huge, expensive tool
- New mask requirements
- Half-field exposure (anamorphic)
- Even lower defect tolerance""",
        "content_advanced": """High-NA EUV requires fundamental changes to the lithography system.

**High-NA vs Standard EUV:**
| Parameter | EUV 0.33NA | High-NA 0.55NA |
|-----------|------------|----------------|
| Resolution | ~13nm | ~8nm |
| DOF | ~100nm | ~45nm |
| Field size | 26×33mm | 26×16.5mm |
| Mask magnification | 4× | 4×/8× anamorphic |
| Tool cost | ~$180M | ~$350M |

**Technical Changes:**
- Anamorphic optics (different X/Y magnification)
- New mask architecture
- Half-field stitching for large dies
- Tighter focus control

**Industry Timeline:**
- 2023-2024: Pilot tools at fabs
- 2025-2026: HVM insertion
- Target nodes: A14 (Intel), N2P (TSMC)""",
        "diagrams": [],
        "equations": [
            {"latex": "Resolution = k_1 \\frac{\\lambda}{NA}", "description": "Resolution improvement"},
            {"latex": "DOF = k_2 \\frac{\\lambda}{NA^2}", "description": "Depth of focus trade-off"}
        ],
        "manufacturing_challenges": ["Depth of focus", "Mask 3D effects", "Cost", "Stochastics"],
        "applications": ["Sub-2nm nodes", "Most critical layers", "Dense patterns"],
        "advantages": ["Better resolution", "Extends EUV", "Single exposure capability"],
        "limitations": ["Very high cost", "Reduced DOF", "Half-field exposure"],
        "related_topics": ["topic_euv_lithography", "topic_2nm", "topic_photomask"],
        "references": [],
        "difficulty": "advanced",
        "author": "system",
        "views": 0
    },
    # ==================== MORE APPLICATIONS ====================
    {
        "topic_id": "topic_data_center",
        "category_id": "cat_applications",
        "title": "Data Center Chips",
        "slug": "data-center-chips",
        "overview": "Data center semiconductors optimize for throughput, efficiency, and total cost of ownership. They include server CPUs, AI accelerators, network switches, and storage controllers.",
        "content_beginner": """Data center chips power the cloud computing infrastructure.

**What's Different About Data Centers:**
- Run 24/7 for years
- Power cost is critical
- High throughput matters more than peak speed
- Reliability is essential

**Key Chip Types:**
- **Server CPUs:** Intel Xeon, AMD EPYC, ARM Ampere
- **AI Accelerators:** NVIDIA, Google TPU, AMD Instinct
- **Network:** Broadcom, Intel, custom ASICs
- **Storage:** Controllers, SSDs, HBAs

**Design Focus:**
- Performance per watt
- Total cost of ownership
- Memory bandwidth
- I/O throughput""",
        "content_advanced": """Data center chip architecture balances compute, memory, and I/O.

**Server CPU Evolution:**
| Generation | Cores | TDP | Memory |
|------------|-------|-----|--------|
| Sapphire Rapids | 60 | 350W | 8ch DDR5 |
| EPYC Genoa | 96 | 360W | 12ch DDR5 |
| Ampere Altra | 128 | 250W | 8ch DDR5 |

**AI Accelerator Trends:**
- Massive parallelism
- High memory bandwidth (HBM)
- Custom precision (FP8, INT4)
- Scale-out interconnects

**Architecture Approaches:**
- Chiplet designs (AMD, Intel)
- Domain-specific accelerators
- SmartNICs/DPUs
- Composable infrastructure""",
        "diagrams": [],
        "equations": [
            {"latex": "TCO = Capital + Power \\times Time \\times Rate", "description": "Total cost of ownership"},
            {"latex": "Efficiency = \\frac{Throughput}{Power}", "description": "Performance per watt"}
        ],
        "manufacturing_challenges": ["Thermal management", "High yields for large dies", "Advanced packaging"],
        "applications": ["Cloud computing", "AI training/inference", "Storage", "Networking"],
        "advantages": ["Optimized for workloads", "High efficiency", "Scalability"],
        "limitations": ["High power", "Cooling requirements", "Cost"],
        "related_topics": ["topic_ai_chips", "topic_hbm", "topic_chiplet"],
        "references": [],
        "difficulty": "intermediate",
        "author": "system",
        "views": 0
    },
    {
        "topic_id": "topic_quantum_chips",
        "category_id": "cat_applications",
        "title": "Quantum Computing Chips",
        "slug": "quantum-computing-chips",
        "overview": "Quantum computing chips use qubits instead of classical bits, enabling certain computations exponentially faster. Technologies include superconducting, trapped ion, and silicon-based approaches.",
        "content_beginner": """Quantum chips use quantum physics for a new type of computing.

**How It's Different:**
- Uses qubits instead of bits
- Qubits can be 0, 1, or both (superposition)
- Qubits can be entangled
- Enables parallel exploration of solutions

**Qubit Technologies:**
- **Superconducting:** IBM, Google (most common)
- **Trapped Ion:** IonQ, Honeywell
- **Silicon Spin:** Intel, imec
- **Photonic:** PsiQuantum, Xanadu

**Current State:**
- 100-1000+ qubits demonstrated
- Error rates still too high for production
- Quantum error correction needed
- NISQ era (Noisy Intermediate-Scale Quantum)""",
        "content_advanced": """Quantum chip engineering faces unique challenges in coherence and control.

**Qubit Comparison:**
| Type | Coherence | Gate Speed | Connectivity |
|------|-----------|------------|--------------|
| Superconducting | 100µs | 20ns | Limited |
| Trapped Ion | >1s | 100µs | All-to-all |
| Silicon Spin | >1ms | 100ns | Limited |
| Photonic | N/A | ps | Probabilistic |

**Key Metrics:**
- T1: Energy relaxation time
- T2: Dephasing time
- Gate fidelity: >99.9% target
- Error rate: 10^-3 to 10^-4 current

**Scaling Challenges:**
- Maintaining coherence
- Interconnect complexity
- Cryogenic requirements
- Classical control electronics
- Error correction overhead""",
        "diagrams": [],
        "equations": [
            {"latex": "|\\psi\\rangle = \\alpha|0\\rangle + \\beta|1\\rangle", "description": "Qubit superposition"},
            {"latex": "N_{logical} = N_{physical} / Overhead", "description": "Error correction overhead"}
        ],
        "manufacturing_challenges": ["Extreme precision", "Cryogenic operation", "Control electronics"],
        "applications": ["Drug discovery", "Optimization", "Cryptography", "Simulation"],
        "advantages": ["Exponential speedup for some problems", "New capabilities"],
        "limitations": ["Error rates", "Limited qubits", "Cryogenics", "Narrow applications"],
        "related_topics": ["topic_cryogenic", "topic_superconducting", "topic_future_computing"],
        "references": [],
        "difficulty": "advanced",
        "author": "system",
        "views": 0
    },
    # ==================== MORE RELIABILITY ====================
    {
        "topic_id": "topic_soft_errors",
        "category_id": "cat_reliability",
        "title": "Soft Errors and Radiation Effects",
        "slug": "soft-errors-radiation",
        "overview": "Soft errors are transient bit flips caused by radiation (cosmic rays, alpha particles). They don't damage hardware but corrupt data, requiring error correction in memories and logic.",
        "content_beginner": """Soft errors are random bit flips caused by radiation hitting chips.

**What Causes Them:**
- Cosmic rays from space
- Alpha particles from materials
- Neutrons at ground level
- High-energy particles

**What Happens:**
- Particle hits silicon
- Creates electron-hole pairs
- Charge collected by circuit
- Bit flips (0→1 or 1→0)

**Why It Matters:**
- More important as chips shrink
- Critical for servers, automotive
- Aerospace/high altitude worse
- Needs error correction""",
        "content_advanced": """Soft error rate (SER) scaling drives design for reliability.

**Soft Error Sources:**
| Source | Flux | Energy | Effect |
|--------|------|--------|--------|
| Cosmic neutrons | ~20/cm²/hr | MeV | SEU, MCU |
| Alpha particles | Package-dependent | MeV | SEU |
| Thermal neutrons | Location-dependent | meV | 10B reaction |

**Error Types:**
- SEU: Single Event Upset (bit flip)
- MCU: Multi-Cell Upset
- SET: Single Event Transient (logic)
- SEFI: Functional Interrupt

**Mitigation Techniques:**
- ECC memory (SECDED, DECTED)
- Redundant logic (TMR)
- Radiation-hardened design
- Error-detecting flip-flops
- Interleaving to prevent MCU""",
        "diagrams": [],
        "equations": [
            {"latex": "SER = Flux \\times \\sigma \\times N", "description": "Soft error rate"},
            {"latex": "FIT = SER \\times 10^9", "description": "Failures in time"}
        ],
        "manufacturing_challenges": ["Low-alpha materials", "Design margin", "Testing"],
        "applications": ["Servers", "Automotive", "Aerospace", "Safety-critical"],
        "advantages": ["Can be mitigated", "Well understood", "Testing available"],
        "limitations": ["Cannot be eliminated", "ECC overhead", "Design complexity"],
        "related_topics": ["topic_reliability", "topic_memory", "topic_automotive_chips"],
        "references": [],
        "difficulty": "intermediate",
        "author": "system",
        "views": 0
    },
    # ==================== MORE FOUNDRIES ====================
    {
        "topic_id": "topic_smic",
        "category_id": "cat_foundries",
        "title": "SMIC",
        "slug": "smic",
        "overview": "Semiconductor Manufacturing International Corporation is China's largest foundry, advancing to 7nm despite US export restrictions. SMIC serves primarily Chinese customers with growing capacity.",
        "content_beginner": """SMIC is China's biggest chip manufacturer, working to catch up with global leaders.

**Key Facts:**
- Founded 2000 in Shanghai
- China's most advanced foundry
- Reached 7nm class node
- Restricted from latest equipment

**Technology Status:**
- 14nm in production
- 7nm demonstrated (N+2)
- Limited EUV access
- Multi-patterning DUV approach

**Challenges:**
- Cannot buy latest ASML EUV
- US entity list restrictions
- Equipment supply constraints
- Talent acquisition""",
        "content_advanced": """SMIC navigates export restrictions while advancing technology.

**SMIC Technology Nodes:**
| Node | Status | Equipment |
|------|--------|-----------|
| 28nm | HVM | DUV |
| 14nm | Production | DUV/immersion |
| 7nm (N+2) | Limited | DUV multi-pattern |
| 5nm | R&D | Restricted |

**Market Position:**
- ~5% global foundry market
- Dominant in China domestic
- Key customers: Chinese fabless
- Growing capacity investment

**Equipment Situation:**
- DUV immersion available
- EUV blocked by export controls
- Working around restrictions
- Domestic equipment development

**Strategic Importance:**
- China semiconductor self-sufficiency
- Government support and investment
- National security implications""",
        "diagrams": [],
        "equations": [],
        "manufacturing_challenges": ["Equipment restrictions", "Technology gap", "Yield maturity"],
        "applications": ["Chinese market", "Consumer electronics", "IoT"],
        "advantages": ["China market access", "Government support", "Growing capacity"],
        "limitations": ["Export restrictions", "Equipment gap", "Technology lag"],
        "related_topics": ["topic_tsmc", "topic_samsung_foundry", "topic_euv_lithography"],
        "references": [],
        "difficulty": "intermediate",
        "author": "system",
        "views": 0
    }
]


def get_extended_topics_part4():
    """Return extended topics part 4 (final batch) to reach 100+ total"""
    return EXTENDED_TOPICS_PART4
