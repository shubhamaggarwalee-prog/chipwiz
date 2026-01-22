"""
Expanded Encyclopedia Content - Manufacturing, Packaging, Materials, Nodes
Deep technical content with proper citations and multiple difficulty levels
"""

EXPANDED_TOPICS = [
    # ==================== MANUFACTURING - LITHOGRAPHY ====================
    {
        "topic_id": "topic_duv_lithography",
        "category_id": "cat_manufacturing",
        "title": "DUV Lithography",
        "slug": "duv-lithography",
        "overview": "Deep Ultraviolet (DUV) lithography using 193nm ArF and 248nm KrF sources remains the workhorse of semiconductor manufacturing, handling the majority of non-critical layers even at advanced nodes.",
        "content_beginner": """DUV (Deep Ultraviolet) lithography is like a projector that shines very short wavelength light through a mask to print tiny patterns on silicon wafers. It's been the main technology for chip-making for over 20 years.

**Two Main Types:**
- **KrF (248nm)**: Older, used for less critical layers
- **ArF (193nm)**: More advanced, still widely used today

**How It Works:**
1. Light passes through a mask (like a stencil)
2. Lenses shrink the pattern by 4x
3. Pattern is printed on light-sensitive resist on the wafer

**Why Still Important:**
- Most chip layers don't need EUV
- Much cheaper than EUV ($50M vs $150M per tool)
- Very mature and reliable technology
- Higher throughput than EUV""",
        "content_advanced": """DUV lithography encompasses 193nm ArF (dry and immersion) and 248nm KrF systems, with ArF immersion (ArFi) representing the most advanced DUV technology.

**ArF Immersion Technology:**
- Wavelength: 193nm
- Immersion fluid: Ultra-pure water (n=1.44)
- Effective NA: Up to 1.35 (vs 0.93 dry)
- Resolution: ~38nm half-pitch (single exposure)
- Multi-patterning enables sub-20nm features

**Optical System:**
- Catadioptric projection optics
- Fused silica and CaF2 lens elements
- Pellicle protection standard
- Dose: 20-40 mJ/cm²

**Multi-Patterning Techniques:**
1. **LELE (Litho-Etch-Litho-Etch)**: Two separate exposures
2. **SADP (Self-Aligned Double Patterning)**: Spacer-based pitch doubling
3. **SAQP (Self-Aligned Quadruple Patterning)**: 4x pitch reduction

**Process Windows:**
- Focus latitude: ±100nm typical
- Dose latitude: ±5%
- Overlay: <3nm (matched machine)

**Cost Comparison (per layer):**
- DUV single: $1
- DUV multi-patterning (3x): $3
- EUV single: $2-3 (but simpler process)""",
        "diagrams": [
            {"type": "mermaid", "content": "graph TD\n    A[ArF Laser 193nm] --> B[Illumination System]\n    B --> C[Mask/Reticle]\n    C --> D[Projection Optics]\n    D --> E[Immersion Fluid]\n    E --> F[Wafer + Resist]", "caption": "ArF Immersion Lithography System"}
        ],
        "equations": [
            {"latex": "R = k_1 \\frac{\\lambda}{NA}", "description": "Resolution (Rayleigh criterion)"},
            {"latex": "NA = n \\cdot \\sin(\\theta)", "description": "Numerical aperture with immersion"},
            {"latex": "DoF = \\pm k_2 \\frac{\\lambda}{NA^2}", "description": "Depth of focus"}
        ],
        "manufacturing_challenges": [
            "Immersion defects (watermarks, bubbles)",
            "Pellicle contamination",
            "Multi-patterning overlay requirements",
            "Resist pattern collapse at high aspect ratios",
            "CD uniformity across exposure field"
        ],
        "applications": ["Non-critical layers at all nodes", "Back-end-of-line (BEOL) metallization", "Memory (DRAM, NAND)", "Mature node production"],
        "advantages": ["Mature, reliable technology", "Lower cost than EUV", "Higher throughput", "Well-understood process windows"],
        "limitations": ["Resolution limited without multi-patterning", "Complex multi-patterning increases cost", "Overlay challenges", "Limited to ~7nm node as primary patterning"],
        "related_topics": ["topic_euv", "topic_photoresist", "topic_overlay"],
        "references": [
            {"title": "ArF Immersion Lithography", "url": "https://www.nikon.com/products/semiconductor/", "source": "Nikon"},
            {"title": "Multi-Patterning Overview", "url": "https://www.asml.com/en/technology/lithography-principles", "source": "ASML"}
        ],
        "difficulty": "intermediate",
        "author": "system",
        "views": 0
    },
    {
        "topic_id": "topic_photoresist",
        "category_id": "cat_manufacturing",
        "title": "Photoresist Technology",
        "slug": "photoresist-technology",
        "overview": "Photoresists are light-sensitive polymeric materials that define patterns during lithography. Modern chemically amplified resists (CARs) and metal oxide resists enable nanometer-scale patterning.",
        "content_beginner": """Photoresist is like a special paint that changes when light hits it. It's how we transfer the tiny circuit patterns onto silicon wafers.

**Two Types:**
- **Positive Resist**: Light makes it soluble (exposed areas wash away)
- **Negative Resist**: Light makes it insoluble (exposed areas stay)

**The Process:**
1. Spin-coat resist onto wafer
2. Expose with light through mask
3. Develop (wash away unwanted areas)
4. Pattern left behind guides next process step

**Why It Matters:**
- Determines the smallest features you can print
- Must be sensitive enough but not too sensitive
- Must survive subsequent etching or implant""",
        "content_advanced": """Modern photoresists are highly engineered materials optimized for specific wavelengths and process requirements.

**Chemically Amplified Resists (CARs):**
- Photoacid generator (PAG) creates acid upon exposure
- Acid catalytically deprotects polymer during PEB
- Amplification factor: 100-1000x
- Enables low dose requirements

**EUV-Specific Challenges:**
- Photon shot noise at 13.5nm
- Secondary electron blur (~2nm)
- Out-of-band radiation sensitivity
- Stochastic defects (missing/bridging contacts)

**Resist Metrics:**
- Sensitivity: mJ/cm² (EUV: 20-40, ArF: 20-30)
- Resolution: minimum half-pitch achievable
- LER/LWR: Line edge/width roughness (target: <2nm 3σ)
- Etch resistance: selectivity to underlayer

**Metal Oxide Resists:**
- Inorganic (Sn, Hf, Zr oxides)
- Higher absorption at EUV
- Better etch resistance
- Lower sensitivity but improving
- Key for high-NA EUV

**Process Stack:**
1. Adhesion promoter (HMDS)
2. Bottom anti-reflective coating (BARC)
3. Photoresist (50-100nm for EUV)
4. Top coat (immersion) or none (EUV)""",
        "diagrams": [],
        "equations": [
            {"latex": "Dose = \\frac{E_{photon} \\cdot N_{photons}}{Area}", "description": "Exposure dose calculation"},
            {"latex": "LER \\propto \\sqrt{\\frac{1}{Dose \\cdot \\eta}}", "description": "Line edge roughness vs dose"}
        ],
        "manufacturing_challenges": [
            "Stochastic defects at low doses",
            "Pattern collapse in high aspect ratio features",
            "Outgassing contamination in EUV",
            "Metal contamination from metal oxide resists",
            "CD uniformity across wafer"
        ],
        "applications": ["All lithography steps", "Critical patterning layers", "EUV and DUV processes", "Advanced memory and logic"],
        "advantages": ["High resolution capability", "Good process latitude", "Mature supply chain", "Continuously improving performance"],
        "limitations": ["Stochastic effects at small features", "Outgassing in EUV", "Pattern collapse limits aspect ratio", "Trade-off between sensitivity and resolution"],
        "related_topics": ["topic_euv", "topic_duv_lithography", "topic_etching"],
        "references": [
            {"title": "EUV Resist Overview", "url": "https://www.jsrlifesciences.com/", "source": "JSR"},
            {"title": "Photoresist Technology", "url": "https://pubs.acs.org/", "source": "ACS Publications"}
        ],
        "difficulty": "advanced",
        "author": "system",
        "views": 0
    },
    # ==================== MANUFACTURING - ETCHING ====================
    {
        "topic_id": "topic_etching",
        "category_id": "cat_manufacturing",
        "title": "Plasma Etching",
        "slug": "plasma-etching",
        "overview": "Plasma etching uses reactive gases in a plasma state to selectively remove material, enabling the transfer of lithographic patterns into underlying films with nanometer precision.",
        "content_beginner": """Plasma etching is like controlled sandblasting at the atomic level. Instead of sand, we use energetic gas particles (plasma) to carve patterns into materials.

**Why Plasma?**
- Extremely precise (single nanometer control)
- Can etch vertically (anisotropic)
- Very selective (etch one material, not another)

**The Process:**
1. Gas flows into vacuum chamber
2. RF power creates plasma (ionized gas)
3. Ions and radicals react with wafer surface
4. Volatile products are pumped away

**Key Terms:**
- **Selectivity**: How much faster you etch the target vs. mask
- **Anisotropy**: Vertical vs. lateral etch rate
- **Etch rate**: How fast material is removed (nm/min)""",
        "content_advanced": """Plasma etching combines physical ion bombardment and chemical reactions for precise pattern transfer.

**Etch Mechanisms:**
1. **Reactive Ion Etching (RIE)**: Ion-enhanced chemical etching
2. **Atomic Layer Etching (ALE)**: Self-limiting monolayer removal
3. **Ion Beam Etching**: Physical sputtering
4. **Downstream Plasma**: Remote plasma for gentle processing

**Process Parameters:**
- Pressure: 1-100 mTorr
- RF Power: 100W-5kW (source + bias)
- Gas flows: 10-500 sccm
- Temperature: -20°C to 80°C (wafer)

**Common Etch Chemistries:**
- Silicon: SF6, CF4, Cl2, HBr
- SiO2: C4F8, CHF3, CF4 + O2
- Si3N4: CHF3, CH2F2
- Metals: Cl2, BCl3 (Al), SF6 (W)
- Organics: O2, N2/H2

**Advanced Etch Challenges:**
- HAR (High Aspect Ratio) etching: 100:1 for 3D NAND
- Selectivity: >100:1 for spacer-based patterning
- Damage control: <2nm amorphous layer
- CD uniformity: <1nm 3σ across wafer

**Atomic Layer Etching (ALE):**
- Self-limiting surface modification
- Gentle ion bombardment to remove modified layer
- Sub-nm etch precision
- Critical for FinFET/GAA transistors""",
        "diagrams": [
            {"type": "mermaid", "content": "graph TD\n    A[Process Gas] --> B[Plasma Chamber]\n    C[RF Power] --> B\n    B --> D[Plasma: Ions + Radicals]\n    D --> E[Wafer Surface]\n    E --> F[Volatile Products]\n    F --> G[Vacuum Pump]", "caption": "Plasma Etch System"}
        ],
        "equations": [
            {"latex": "Selectivity = \\frac{ER_{target}}{ER_{mask}}", "description": "Etch selectivity ratio"},
            {"latex": "Anisotropy = 1 - \\frac{L_{lateral}}{L_{vertical}}", "description": "Anisotropy factor (1 = perfect vertical)"},
            {"latex": "ER = k \\cdot [Radical] \\cdot \\exp(-E_a/kT)", "description": "Etch rate Arrhenius equation"}
        ],
        "manufacturing_challenges": [
            "High aspect ratio etching (>50:1)",
            "Selectivity maintenance over process",
            "Pattern loading effects",
            "Etch uniformity across wafer",
            "Plasma-induced damage",
            "Micro-loading between dense and isolated features"
        ],
        "applications": ["Gate patterning", "Contact/via formation", "Fin/nanosheet release", "3D NAND channel holes", "BEOL metallization"],
        "advantages": ["High precision and control", "Excellent anisotropy", "High selectivity achievable", "Scalable to atomic dimensions"],
        "limitations": ["Plasma damage to sensitive materials", "Aspect ratio dependent effects", "Chamber conditioning required", "Complex multi-step processes"],
        "related_topics": ["topic_deposition", "topic_gaafet", "topic_3d_nand"],
        "references": [
            {"title": "Plasma Etching Fundamentals", "url": "https://www.lamresearch.com/", "source": "Lam Research"},
            {"title": "ALE Technology", "url": "https://www.appliedmaterials.com/", "source": "Applied Materials"}
        ],
        "difficulty": "intermediate",
        "author": "system",
        "views": 0
    },
    # ==================== MANUFACTURING - DEPOSITION ====================
    {
        "topic_id": "topic_deposition",
        "category_id": "cat_manufacturing",
        "title": "Thin Film Deposition",
        "slug": "thin-film-deposition",
        "overview": "Thin film deposition techniques including CVD, PVD, ALD, and epitaxy enable the precise layering of materials that form transistors, interconnects, and device structures.",
        "content_beginner": """Thin film deposition is like painting, but at the atomic level. We carefully add ultra-thin layers of materials to build up the complex structures in chips.

**Main Methods:**
- **CVD (Chemical Vapor Deposition)**: Gases react on the surface to form solid films
- **PVD (Physical Vapor Deposition)**: Material is physically transferred (like evaporation)
- **ALD (Atomic Layer Deposition)**: One atomic layer at a time, very precise
- **Epitaxy**: Growing crystal layers that match the substrate

**Why Important:**
- Build transistor gates, insulators, contacts
- Create interconnect wiring
- Deposit barrier and liner films
- Control film properties atom-by-atom""",
        "content_advanced": """Modern deposition achieves atomic-scale precision for advanced device fabrication.

**Chemical Vapor Deposition (CVD):**
- PECVD: Plasma-enhanced, lower temperature
- LPCVD: Low pressure, conformal coverage
- MOCVD: Metal-organic precursors, III-V growth
- Temperature: 200-800°C depending on process

**Atomic Layer Deposition (ALD):**
- Self-limiting surface reactions
- Precursor pulse → Purge → Co-reactant → Purge
- Growth rate: 0.5-1.5 Å/cycle
- Conformality: >95% in HAR structures
- Critical for high-k gate dielectrics, liners

**Physical Vapor Deposition (PVD):**
- Sputtering: Ion bombardment of target
- Evaporation: Thermal/e-beam heating
- Used for metals: Cu seed, barrier metals
- Directional deposition

**Epitaxy:**
- MBE (Molecular Beam Epitaxy): Ultra-pure, slow
- CVD Epitaxy: Higher throughput
- SiGe source/drain stressors
- III-V on Si integration

**Key Film Properties:**
- Thickness: ±1% uniformity
- Stress: Tensile/compressive control
- Composition: Stoichiometry control
- Conformality: Step coverage in 3D structures
- Impurity levels: <1e18 atoms/cm³""",
        "diagrams": [],
        "equations": [
            {"latex": "GPC = \\frac{\\Delta t}{N_{cycles}}", "description": "Growth per cycle (ALD)"},
            {"latex": "Conformality = \\frac{t_{bottom}}{t_{top}} \\times 100\\%", "description": "Step coverage percentage"}
        ],
        "manufacturing_challenges": [
            "Conformality in high aspect ratio features",
            "Precursor cost and availability",
            "Particle defects from chamber",
            "Film stress management",
            "Gap fill without voids",
            "Throughput vs. quality trade-offs"
        ],
        "applications": ["High-k gate dielectrics", "Metal gates", "Barrier/liner films", "Interconnect copper", "Epitaxial channel", "3D NAND wordlines"],
        "advantages": ["Atomic-level control (ALD)", "Wide material selection", "Good conformality achievable", "Scalable to advanced nodes"],
        "limitations": ["Throughput limitations (ALD)", "Precursor costs", "Temperature constraints", "Seam/void formation in narrow gaps"],
        "related_topics": ["topic_etching", "topic_high_k", "topic_interconnects"],
        "references": [
            {"title": "ALD Technology", "url": "https://www.asminternational.com/", "source": "ASM International"},
            {"title": "CVD/PVD Overview", "url": "https://www.appliedmaterials.com/", "source": "Applied Materials"}
        ],
        "difficulty": "intermediate",
        "author": "system",
        "views": 0
    },
    # ==================== MANUFACTURING - YIELD ====================
    {
        "topic_id": "topic_yield",
        "category_id": "cat_reliability",
        "title": "Semiconductor Yield",
        "slug": "semiconductor-yield",
        "overview": "Semiconductor yield represents the percentage of functional dies on a wafer, directly impacting manufacturing cost and profitability. Yield engineering is critical for advanced node viability.",
        "content_beginner": """Yield is simply: how many good chips do you get from each wafer? If a wafer can hold 1000 chips but only 800 work, that's 80% yield.

**Why Yield Matters:**
- Higher yield = lower cost per chip
- Critical for profitability
- Can make or break a new process node

**What Causes Defects:**
- Particles (dust, contamination)
- Process variations (thickness, alignment)
- Equipment problems
- Design issues

**Yield Improvement:**
- Cleaner manufacturing (fewer particles)
- Better process control
- Design for manufacturability
- Continuous monitoring and adjustment""",
        "content_advanced": """Yield modeling and improvement is a complex discipline combining statistics, physics, and manufacturing engineering.

**Yield Models:**
1. **Poisson Model**: Y = exp(-D₀ × A)
2. **Murphy Model**: Y = [(1-exp(-D₀×A))/(D₀×A)]²
3. **Negative Binomial**: Accounts for defect clustering

**Defect Categories:**
- **Random defects**: Particles, contamination
- **Systematic defects**: Process-induced
- **Parametric defects**: Out-of-spec electrical performance

**Defect Density Trends:**
- Mature node: 0.01-0.1 defects/cm²
- Advanced logic: 0.05-0.2 defects/cm²
- Critical for large die sizes (>100mm²)

**Yield Learning:**
- D₀ learning curve: D₀(t) = D₀∞ + (D₀₀ - D₀∞)exp(-t/τ)
- Typical learning time: 12-24 months to mature yield
- Requires systematic defect reduction

**Key Metrics:**
- Die yield: Good dies / Total dies
- Wafer yield: Good wafers / Total wafers
- Probe yield: Pass at wafer test
- Final test yield: Pass at package test
- Defect density (D₀): defects/cm²

**Yield Enhancement Techniques:**
- In-line inspection (optical, e-beam)
- Process monitor wafers
- Statistical process control (SPC)
- Design for manufacturability (DFM)
- Redundancy (memory repair)""",
        "diagrams": [],
        "equations": [
            {"latex": "Y = e^{-D_0 \\cdot A}", "description": "Poisson yield model"},
            {"latex": "Y = \\left(\\frac{1-e^{-D_0 A}}{D_0 A}\\right)^2", "description": "Murphy yield model"},
            {"latex": "Cost_{die} = \\frac{Cost_{wafer}}{N_{die} \\cdot Y}", "description": "Die cost including yield"}
        ],
        "manufacturing_challenges": [
            "Defect detection at <10nm sizes",
            "Systematic defect root cause analysis",
            "Yield ramp time pressure",
            "Large die yield challenges",
            "EUV stochastic defects"
        ],
        "applications": ["Fab process development", "Manufacturing monitoring", "Cost modeling", "Product qualification"],
        "advantages": ["Direct impact on profitability", "Enables advanced node economics", "Drives continuous improvement"],
        "limitations": ["Complex multi-variable optimization", "Long learning cycles", "Expensive inspection tools", "Design-process interactions"],
        "related_topics": ["topic_defect_inspection", "topic_dfm", "topic_reliability"],
        "references": [
            {"title": "Yield Engineering", "url": "https://www.kla.com/", "source": "KLA Corporation"},
            {"title": "Semiconductor Manufacturing", "url": "https://semiengineering.com/", "source": "Semiconductor Engineering"}
        ],
        "difficulty": "intermediate",
        "author": "system",
        "views": 0
    },
    # ==================== ADVANCED PACKAGING ====================
    {
        "topic_id": "topic_chiplet",
        "category_id": "cat_packaging",
        "title": "Chiplet Architecture",
        "slug": "chiplet-architecture",
        "overview": "Chiplet architecture disaggregates monolithic SoCs into smaller, specialized dies connected via advanced packaging, enabling better yield, heterogeneous integration, and faster time-to-market.",
        "content_beginner": """Chiplets are like LEGO blocks for chips. Instead of making one giant chip, you make smaller pieces and connect them together.

**Why Chiplets?**
- Smaller chips have better yield (fewer defects)
- Mix different technologies (memory, logic, I/O)
- Reuse designs across products
- Don't need most advanced node for everything

**How They Connect:**
- Advanced packaging puts them close together
- High-speed connections between chiplets
- Interposer or bridge provides wiring

**Real Examples:**
- AMD Ryzen/EPYC processors
- Apple M-series (compute + memory)
- Intel Ponte Vecchio GPU""",
        "content_advanced": """Chiplet architecture represents a paradigm shift from monolithic integration to heterogeneous, modular design.

**Chiplet Interconnect Technologies:**
1. **UCIe (Universal Chiplet Interconnect Express)**
   - Industry standard (2022)
   - Advanced package: 32GT/s per lane
   - Standard package: 16GT/s per lane
   - Power: 0.5 pJ/bit (advanced)

2. **Proprietary Solutions:**
   - AMD Infinity Fabric
   - Intel EMIB
   - TSMC SoIC

**Design Trade-offs:**
- Partitioning granularity
- Interconnect bandwidth vs. power
- Thermal management complexity
- Known good die (KGD) testing

**Economic Analysis:**
- Yield benefit: Y_chiplet > Y_monolithic^n
- Cost crossover: Typically >200mm² die area
- NRE amortization across product variants
- Mix-and-match node optimization

**Interconnect Density:**
- µbump pitch: 25-55µm
- Hybrid bonding: <10µm pitch
- Bandwidth density: >1TB/s/mm²

**Thermal Considerations:**
- Localized hotspots from stacking
- Power density: >100W/cm²
- Thermal interface materials
- Active cooling requirements""",
        "diagrams": [],
        "equations": [
            {"latex": "Y_{chiplet} = \\prod_{i=1}^{n} Y_i > Y_{mono}", "description": "Chiplet yield advantage"},
            {"latex": "BW = N_{lanes} \\times DataRate \\times Width", "description": "Interconnect bandwidth"}
        ],
        "manufacturing_challenges": [
            "Known good die testing before assembly",
            "Chiplet-to-chiplet alignment (<1µm)",
            "Thermal management in 3D stacks",
            "Supply chain complexity",
            "Standardization (UCIe adoption)"
        ],
        "applications": ["High-performance computing", "Data center processors", "AI accelerators", "Consumer SoCs", "Automotive"],
        "advantages": ["Better yield economics", "Heterogeneous integration", "Design reuse", "Flexible product SKUs", "Mix nodes optimization"],
        "limitations": ["Interconnect overhead", "Increased packaging complexity", "Testing challenges", "Thermal constraints", "Ecosystem maturity"],
        "related_topics": ["topic_cowos", "topic_hybrid_bonding", "topic_ucie"],
        "references": [
            {"title": "UCIe Specification", "url": "https://www.uciexpress.org/", "source": "UCIe Consortium"},
            {"title": "Chiplet Design", "url": "https://www.amd.com/en/technologies/infinity-architecture", "source": "AMD"}
        ],
        "difficulty": "intermediate",
        "author": "system",
        "views": 0
    },
    {
        "topic_id": "topic_hybrid_bonding",
        "category_id": "cat_packaging",
        "title": "Hybrid Bonding",
        "slug": "hybrid-bonding",
        "overview": "Hybrid bonding enables direct Cu-Cu and dielectric-dielectric bonding between dies at sub-10µm pitch, providing the highest interconnect density for 3D integration.",
        "content_beginner": """Hybrid bonding is like gluing two chip surfaces together so perfectly that the metal connections line up and touch directly - no bumps or wires needed.

**Why It's Special:**
- Much smaller connections than traditional bumps
- Can pack connections very close together
- Enables true 3D chip stacking

**The Process:**
1. Polish both chip surfaces ultra-flat
2. Activate the surfaces (make them sticky)
3. Align precisely (within 0.5µm)
4. Bond together with heat and pressure

**Where It's Used:**
- CMOS image sensors (camera chips)
- Memory-on-logic stacking
- High-bandwidth memory""",
        "content_advanced": """Hybrid bonding (also called direct bond interconnect - DBI) achieves the ultimate interconnect density for 3D integration.

**Process Requirements:**
- Surface roughness: <0.5nm RMS
- Dishing/erosion: <5nm
- Particle count: <0.01/cm²
- Alignment accuracy: <200nm

**Bonding Sequence:**
1. CMP planarization
2. Plasma activation
3. Room temperature pre-bond
4. Thermal anneal (300-400°C)
5. Cu expansion bonds pads

**Pitch Capabilities:**
- Production: 9µm (Sony CIS)
- Development: <1µm demonstrated
- vs. µbump: 25-55µm
- vs. TSV: 5-10µm

**Electrical Performance:**
- Contact resistance: <50mΩ per bond
- Capacitance: <1fF per bond
- Current density: >10⁶ A/cm²

**Key Enablers:**
- Ultra-flat CMP (<0.5nm roughness)
- Clean room class 1 environment
- Sub-micron alignment tools
- Thermal stability matching

**Applications:**
- CMOS image sensors (Sony, Samsung)
- HBM-next generation
- Logic-on-logic (AMD 3D V-Cache)
- Memory-on-logic integration""",
        "diagrams": [],
        "equations": [
            {"latex": "\\sigma < 0.5nm", "description": "Surface roughness requirement"},
            {"latex": "Density = \\frac{1}{pitch^2}", "description": "Bond density vs pitch"}
        ],
        "manufacturing_challenges": [
            "Surface preparation uniformity",
            "Particle control (<0.01/cm²)",
            "Alignment across large areas",
            "Thermal expansion mismatch",
            "Known good die requirements"
        ],
        "applications": ["CMOS image sensors", "3D SRAM cache", "Memory stacking", "Heterogeneous integration"],
        "advantages": ["Highest interconnect density", "Lowest power per bit", "Excellent thermal path", "No underfill required"],
        "limitations": ["Stringent surface requirements", "Limited repair capability", "High capital cost", "Yield sensitivity"],
        "related_topics": ["topic_chiplet", "topic_cowos", "topic_3d_ic"],
        "references": [
            {"title": "Hybrid Bonding Technology", "url": "https://www.sony-semicon.com/", "source": "Sony Semiconductor"},
            {"title": "Direct Bond Interconnect", "url": "https://xperi.com/", "source": "Xperi"}
        ],
        "difficulty": "advanced",
        "author": "system",
        "views": 0
    },
    {
        "topic_id": "topic_hbm",
        "category_id": "cat_packaging",
        "title": "High Bandwidth Memory (HBM)",
        "slug": "high-bandwidth-memory",
        "overview": "High Bandwidth Memory (HBM) stacks multiple DRAM dies using TSVs and hybrid bonding, achieving unprecedented memory bandwidth essential for AI accelerators and high-performance computing.",
        "content_beginner": """HBM is like a skyscraper for memory chips. Instead of spreading memory out flat, we stack multiple memory layers on top of each other with tiny vertical connections.

**Why Stack Memory?**
- Much more bandwidth (data speed)
- Smaller footprint
- Less power per bit transferred

**How It Works:**
- 4-16 DRAM layers stacked
- Thousands of tiny vertical wires (TSVs)
- Connected to processor via interposer

**The Numbers:**
- HBM3E: >1TB/s bandwidth
- Regular DDR5: ~50GB/s
- That's 20x more data speed!

**Where It's Used:**
- AI training GPUs (NVIDIA H100)
- AI inference chips
- Supercomputers""",
        "content_advanced": """HBM represents the pinnacle of memory bandwidth technology, essential for AI workloads.

**HBM Generations:**
| Gen | Bandwidth | Capacity | Interface |
|-----|-----------|----------|-----------|
| HBM1 | 128GB/s | 4GB | 1024-bit |
| HBM2 | 256GB/s | 8GB | 1024-bit |
| HBM2E | 460GB/s | 16GB | 1024-bit |
| HBM3 | 819GB/s | 24GB | 1024-bit |
| HBM3E | 1.15TB/s | 36GB | 1024-bit |

**Architecture:**
- Stack height: 8-12 DRAM dies + 1 base die
- TSV count: >5000 per stack
- TSV pitch: 40-55µm
- Channel width: 1024 bits (8 channels × 128b)

**Power Efficiency:**
- HBM3: ~3.9 pJ/bit
- DDR5: ~8 pJ/bit
- GDDR6X: ~15 pJ/bit

**Manufacturing Flow:**
1. DRAM wafer processing
2. TSV formation (via-middle or via-last)
3. Wafer thinning (~40µm)
4. Micro-bump formation
5. Die stacking (TC bonding)
6. Base die integration
7. CoWoS assembly

**Thermal Challenges:**
- Stack TDP: 20-30W per stack
- Operating temp: <95°C junction
- Thermal resistance: Critical in stack
- Heat spreader integration""",
        "diagrams": [],
        "equations": [
            {"latex": "BW = Channels \\times Width \\times DataRate", "description": "HBM bandwidth calculation"},
            {"latex": "Energy = \\frac{Power}{BW} \\times 8", "description": "Energy per bit (pJ/bit)"}
        ],
        "manufacturing_challenges": [
            "TSV yield and reliability",
            "Thin wafer handling (40µm)",
            "Stack alignment and bonding",
            "Thermal management",
            "Known good die testing"
        ],
        "applications": ["AI/ML training", "AI inference", "HPC", "Graphics", "Networking"],
        "advantages": ["Highest bandwidth available", "Excellent power efficiency", "Small footprint", "Wide interface"],
        "limitations": ["High cost", "Capacity limited by stacking", "Thermal constraints", "Single-vendor integration"],
        "related_topics": ["topic_cowos", "topic_tsv", "topic_ai_chips"],
        "references": [
            {"title": "HBM Technology", "url": "https://www.skhynix.com/", "source": "SK Hynix"},
            {"title": "HBM Specifications", "url": "https://www.jedec.org/", "source": "JEDEC"}
        ],
        "difficulty": "intermediate",
        "author": "system",
        "views": 0
    },
    # ==================== MATERIALS ====================
    {
        "topic_id": "topic_silicon",
        "category_id": "cat_materials",
        "title": "Silicon (Si) Substrates",
        "slug": "silicon-substrates",
        "overview": "Silicon is the foundation of modern semiconductors, providing an abundant, well-characterized semiconductor with excellent oxide properties that has enabled 60+ years of Moore's Law scaling.",
        "content_beginner": """Silicon is the #2 most common element in Earth's crust (after oxygen) and the foundation of nearly all computer chips.

**Why Silicon?**
- Abundant (sand is silicon dioxide)
- Forms a great natural insulator (SiO2)
- Can be made extremely pure
- Well-understood over 60+ years

**How It's Made:**
1. Purify sand into metallurgical silicon
2. Further purify to 99.9999999% (9-nines pure)
3. Grow large single crystals
4. Slice into thin wafers

**Wafer Sizes:**
- 200mm (8 inch): Older fabs
- 300mm (12 inch): Modern fabs
- 450mm: Abandoned (too expensive)""",
        "content_advanced": """Silicon wafer technology continues to evolve for advanced device requirements.

**Crystal Growth:**
- Czochralski (CZ): Standard method, ~1m/hour
- Float Zone (FZ): Higher purity, lower O2
- Crystal orientation: (100) for CMOS, (111) for bipolar

**Wafer Specifications:**
- Diameter: 300mm standard
- Thickness: 775µm nominal
- TTV (Total Thickness Variation): <1µm
- Bow/Warp: <40µm
- Resistivity: 1-50 Ω·cm (varies by application)
- Oxygen: 10-20 ppma (CZ)

**Epitaxial Silicon:**
- CVD-grown single crystal layer
- Thickness: 2-20µm
- Enables buried layers, improved doping control
- Critical for BiCMOS, power devices

**SOI (Silicon-on-Insulator):**
- Thin Si layer on buried oxide (BOX)
- FD-SOI: 5-20nm Si, ~20nm BOX
- Reduced parasitic capacitance
- Better isolation, lower leakage

**Emerging Substrates:**
- High-resistivity (>1kΩ·cm) for RF
- SOI for mobile/automotive
- Engineered substrates for power/RF""",
        "diagrams": [],
        "equations": [
            {"latex": "E_g = 1.12 eV", "description": "Silicon bandgap at 300K"},
            {"latex": "\\mu_n = 1400 cm^2/V·s", "description": "Electron mobility in silicon"}
        ],
        "manufacturing_challenges": [
            "Crystal defect control (dislocations)",
            "Contamination control (<1e10 atoms/cm³)",
            "Wafer flatness requirements",
            "Oxygen precipitation control",
            "Epitaxy uniformity"
        ],
        "applications": ["Logic ICs", "Memory (DRAM, NAND)", "Analog/Mixed-signal", "Power management", "RF/Wireless"],
        "advantages": ["Abundant, low cost", "Excellent native oxide", "Mature technology", "Extensive infrastructure"],
        "limitations": ["Indirect bandgap (poor for light emission)", "Mobility limits vs III-V", "Breakdown voltage vs SiC/GaN"],
        "related_topics": ["topic_sic", "topic_gan", "topic_fdsoi"],
        "references": [
            {"title": "Silicon Wafer Technology", "url": "https://www.shin-etsu.com/", "source": "Shin-Etsu"},
            {"title": "SEMI Wafer Standards", "url": "https://www.semi.org/", "source": "SEMI"}
        ],
        "difficulty": "beginner",
        "author": "system",
        "views": 0
    },
    {
        "topic_id": "topic_sic",
        "category_id": "cat_materials",
        "title": "Silicon Carbide (SiC)",
        "slug": "silicon-carbide",
        "overview": "Silicon Carbide is a wide bandgap semiconductor enabling high-voltage, high-temperature power electronics with superior efficiency for EVs, renewable energy, and industrial applications.",
        "content_beginner": """Silicon Carbide (SiC) is like silicon's stronger cousin. It can handle much higher voltages and temperatures, making it perfect for power electronics.

**Why SiC?**
- Can block 10x higher voltages than silicon
- Works at higher temperatures
- Switches faster with less loss
- Critical for electric vehicles

**Key Applications:**
- EV traction inverters (drive motors)
- EV charging stations
- Solar inverters
- Industrial motor drives

**Market Growth:**
- EVs driving massive demand
- Tesla, BYD using SiC inverters
- Market growing >30%/year""",
        "content_advanced": """Silicon Carbide offers superior material properties for power electronics applications.

**Material Properties (4H-SiC):**
| Property | Si | 4H-SiC | Advantage |
|----------|-----|--------|-----------|
| Bandgap (eV) | 1.12 | 3.26 | Higher blocking voltage |
| Critical field (MV/cm) | 0.3 | 2.8 | 10x voltage capability |
| Thermal conductivity (W/m·K) | 150 | 490 | Better heat removal |
| Electron mobility (cm²/V·s) | 1400 | 900 | Slightly lower |

**Device Types:**
- MOSFETs: 650V-3.3kV ratings
- Schottky diodes: Fast switching
- JBS (Junction Barrier Schottky)
- IGBTs: Emerging for >3.3kV

**Crystal Growth Challenges:**
- Polytypes: 4H-SiC preferred (highest mobility)
- Defect density: 0.1-0.5/cm² (vs ~0 for Si)
- Wafer cost: ~10x silicon
- Maximum diameter: 200mm (ramping)

**Device Manufacturing:**
- High-temperature implant activation (1600-1700°C)
- Gate oxide quality (SiO2/SiC interface)
- Ohmic contact formation
- Edge termination design

**EV Application:**
- Traction inverter: 100-200kW
- 400V or 800V battery systems
- Range improvement: 5-10%
- Efficiency: >99% possible""",
        "diagrams": [],
        "equations": [
            {"latex": "E_g = 3.26 eV", "description": "4H-SiC bandgap"},
            {"latex": "P_{loss} \\propto R_{DS(on)} \\cdot I^2", "description": "Conduction loss"},
            {"latex": "BV \\propto E_c \\cdot W_d", "description": "Breakdown voltage vs drift width"}
        ],
        "manufacturing_challenges": [
            "Substrate defect density",
            "Gate oxide reliability",
            "High temperature processing",
            "Wafer cost (10x silicon)",
            "200mm transition ongoing"
        ],
        "applications": ["EV inverters", "Industrial drives", "Solar inverters", "Rail traction", "Grid infrastructure"],
        "advantages": ["High voltage capability", "High temperature operation", "Lower switching losses", "Smaller passive components"],
        "limitations": ["High cost", "Gate oxide reliability concerns", "Limited wafer sizes", "Defect density"],
        "related_topics": ["topic_gan", "topic_silicon", "topic_power_devices"],
        "references": [
            {"title": "SiC Power Devices", "url": "https://www.wolfspeed.com/", "source": "Wolfspeed"},
            {"title": "SiC Market Analysis", "url": "https://www.onsemi.com/", "source": "onsemi"}
        ],
        "difficulty": "intermediate",
        "author": "system",
        "views": 0
    },
    {
        "topic_id": "topic_gan",
        "category_id": "cat_materials",
        "title": "Gallium Nitride (GaN)",
        "slug": "gallium-nitride",
        "overview": "Gallium Nitride enables high-frequency, high-efficiency power electronics and RF devices, powering fast chargers, data center power supplies, 5G infrastructure, and defense radar systems.",
        "content_beginner": """Gallium Nitride (GaN) is a super-fast switching material. While SiC handles high voltages, GaN excels at switching extremely quickly.

**Why GaN?**
- Switches 10x faster than silicon
- Higher efficiency at high frequencies
- Enables smaller, lighter power supplies

**Where You See GaN:**
- Fast phone/laptop chargers (tiny & powerful)
- Data center power supplies
- 5G cell towers
- Electric vehicle chargers

**GaN vs SiC:**
- GaN: Speed champion (<650V typically)
- SiC: High voltage champion (>650V)""",
        "content_advanced": """Gallium Nitride combines wide bandgap properties with unique heterostructure physics enabling HEMTs.

**Material Properties:**
| Property | Si | GaN | Advantage |
|----------|-----|-----|-----------|
| Bandgap (eV) | 1.12 | 3.4 | Higher voltage |
| Critical field (MV/cm) | 0.3 | 3.3 | Compact devices |
| 2DEG mobility (cm²/V·s) | N/A | 2000 | High frequency |
| Saturation velocity (cm/s) | 1e7 | 2.5e7 | RF performance |

**HEMT Structure:**
- AlGaN/GaN heterostructure
- 2D Electron Gas (2DEG) at interface
- Normally-on (depletion mode) naturally
- Enhancement mode via p-GaN or recessed gate

**GaN-on-Si:**
- Cost-effective substrate
- 200mm production
- Lattice mismatch management
- Buffer layer engineering

**GaN-on-SiC:**
- Better thermal conductivity
- RF/microwave applications
- Higher cost

**Device Types:**
- Power: 30V-650V HEMTs
- RF: 5G, radar, satellite
- LED: Lighting, displays

**Reliability Challenges:**
- Dynamic Rds(on) increase
- Charge trapping
- Current collapse
- Gate reliability""",
        "diagrams": [],
        "equations": [
            {"latex": "E_g = 3.4 eV", "description": "GaN bandgap"},
            {"latex": "n_{2DEG} \\approx 1 \\times 10^{13} cm^{-2}", "description": "2DEG sheet density"},
            {"latex": "f_T = \\frac{g_m}{2\\pi C_{gs}}", "description": "Cutoff frequency"}
        ],
        "manufacturing_challenges": [
            "Lattice mismatch (GaN on Si)",
            "Dynamic Rds(on) reliability",
            "Thermal management",
            "Cost reduction ongoing",
            "Enhancement mode complexity"
        ],
        "applications": ["Fast chargers", "Data center power", "5G infrastructure", "Automotive onboard chargers", "Lidar"],
        "advantages": ["High frequency operation", "High efficiency", "Small form factor", "Fast switching"],
        "limitations": ["Voltage limited (<650V typical)", "Thermal management", "Reliability maturation", "Cost premium"],
        "related_topics": ["topic_sic", "topic_silicon", "topic_rf_devices"],
        "references": [
            {"title": "GaN Technology", "url": "https://www.ti.com/", "source": "Texas Instruments"},
            {"title": "GaN Power ICs", "url": "https://www.navitassemi.com/", "source": "Navitas Semiconductor"}
        ],
        "difficulty": "intermediate",
        "author": "system",
        "views": 0
    },
    # ==================== NODES & SCALING ====================
    {
        "topic_id": "topic_2nm",
        "category_id": "cat_nodes",
        "title": "2nm Process Node",
        "slug": "2nm-process-node",
        "overview": "The 2nm node introduces Gate-All-Around (GAA) nanosheet transistors at TSMC and Samsung, with Intel's comparable 20A/18A nodes targeting similar density and performance levels.",
        "content_beginner": """2nm is the next frontier in chip manufacturing. The name doesn't mean features are actually 2nm - it's a marketing term indicating the generation of technology.

**What's New at 2nm:**
- TSMC and Samsung switching to GAA transistors
- Intel calls their version "20A" then "18A"
- About 15-20% faster than 3nm
- ~25% less power consumption

**Key Changes:**
- Transistor structure changes from FinFET to GAA
- More EUV lithography layers
- Backside power delivery (Intel)
- Higher transistor density

**Timeline:**
- TSMC N2: Production in 2025
- Samsung 2nm: Production in 2025
- Intel 20A: Production in 2024""",
        "content_advanced": """The 2nm node represents a major architectural transition to nanosheet transistors.

**TSMC N2:**
- Architecture: Nanosheet GAA
- Density: ~300 MTr/mm² (estimated)
- Performance: +10-15% vs N3E at iso-power
- Power: -25-30% vs N3E at iso-performance
- EUV layers: >20 (estimated)
- Production: 2H 2025

**Samsung 2nm GAA:**
- Second-generation GAA
- Improved vs SF3 yield
- Backside power delivery (later variants)
- Competing for foundry customers

**Intel 20A/18A:**
- RibbonFET (Intel's GAA)
- PowerVia (backside power delivery)
- 20A: 2024 (internal)
- 18A: 2025 (external foundry)

**Key Enablers:**
- High-NA EUV (resolution)
- Nanosheet channel formation
- Inner spacer engineering
- Contact resistance reduction
- Backside power (Intel)

**Density Comparison:**
| Node | MTr/mm² | Company |
|------|---------|---------|
| Intel 7 | 100 | Intel |
| N3E | 200 | TSMC |
| N2 | ~300 | TSMC |
| 18A | ~350 | Intel |

**Challenges:**
- GAA process complexity
- Yield ramp
- Cost per transistor trend
- High-NA EUV introduction""",
        "diagrams": [],
        "equations": [
            {"latex": "Density \\propto \\frac{1}{CPP \\times MMP}", "description": "Density vs contacted pitch × metal pitch"}
        ],
        "manufacturing_challenges": [
            "GAA nanosheet formation",
            "Inner spacer uniformity",
            "Channel release selectivity",
            "Backside power integration",
            "High-NA EUV adoption"
        ],
        "applications": ["High-performance computing", "Mobile SoCs", "AI accelerators", "Data center"],
        "advantages": ["Continued scaling", "Better power efficiency", "Higher density", "GAA benefits"],
        "limitations": ["Extreme cost", "Complex manufacturing", "Yield challenges", "Design complexity"],
        "related_topics": ["topic_gaafet", "topic_euv", "topic_3nm"],
        "references": [
            {"title": "TSMC N2 Technology", "url": "https://www.tsmc.com/", "source": "TSMC"},
            {"title": "Intel Process Roadmap", "url": "https://www.intel.com/", "source": "Intel"}
        ],
        "difficulty": "advanced",
        "author": "system",
        "views": 0
    },
    {
        "topic_id": "topic_3nm",
        "category_id": "cat_nodes",
        "title": "3nm Process Node",
        "slug": "3nm-process-node",
        "overview": "The 3nm node represents the most advanced production technology, with TSMC N3 using optimized FinFET and Samsung 3GAE introducing the industry's first GAA transistors in high-volume manufacturing.",
        "content_beginner": """3nm chips are in your newest phones and computers right now. Apple's M3 and A17 Pro use TSMC's 3nm process.

**What 3nm Offers:**
- ~30% more transistors than 5nm
- ~15% faster performance
- ~30% lower power consumption

**Who Makes 3nm:**
- TSMC: N3, N3E, N3P (FinFET)
- Samsung: 3GAE, 3GAP (GAA)
- Intel: Intel 3 (FinFET)

**Key Products:**
- Apple M3, M3 Pro, M3 Max
- Apple A17 Pro
- Coming: AMD, NVIDIA, Qualcomm""",
        "content_advanced": """3nm showcases different architectural approaches between major foundries.

**TSMC N3 Family:**
- **N3**: First 3nm, limited customers
- **N3E**: Enhanced yield/performance balance
- **N3P**: Performance optimized
- **N3X**: High-performance variant

**N3E Specifications:**
- Architecture: FinFET
- Density: ~291 MTr/mm²
- Performance: +18% vs N5 at iso-power
- Power: -32% vs N5 at iso-performance
- EUV layers: ~20
- Metal pitch: 21nm

**Samsung 3nm GAA:**
- First production GAA transistors
- Sheet width tunability
- Yield improvements with SF3
- Targeting HPC and mobile

**Process Comparison:**
| Metric | TSMC N3E | Samsung 3GAA | Intel 3 |
|--------|----------|--------------|---------|
| Architecture | FinFET | GAA | FinFET |
| Density | ~291 | ~230* | ~260* |
| Performance | Baseline | -10%* | +5%* |
*Estimated from public data

**Design Considerations:**
- Library complexity increase
- Power delivery challenges
- Thermal management
- EDA tool requirements""",
        "diagrams": [],
        "equations": [
            {"latex": "PPA = f(Density, Speed, Power)", "description": "Power-Performance-Area metric"}
        ],
        "manufacturing_challenges": [
            "EUV layer count increase",
            "Fin/nanosheet uniformity",
            "Interconnect resistance",
            "Yield optimization",
            "Cost management"
        ],
        "applications": ["Flagship smartphones", "Apple Silicon", "High-performance computing", "AI chips"],
        "advantages": ["Highest production density", "Best power efficiency", "Proven in HVM", "Multiple variants"],
        "limitations": ["High cost", "Limited capacity", "Complex design rules", "Yield variability"],
        "related_topics": ["topic_2nm", "topic_gaafet", "topic_finfet"],
        "references": [
            {"title": "TSMC N3 Technology", "url": "https://www.tsmc.com/english/dedicatedFoundry/technology/n3", "source": "TSMC"},
            {"title": "Samsung 3nm", "url": "https://semiconductor.samsung.com/", "source": "Samsung Foundry"}
        ],
        "difficulty": "intermediate",
        "author": "system",
        "views": 0
    },
    {
        "topic_id": "topic_bspd",
        "category_id": "cat_nodes",
        "title": "Backside Power Delivery",
        "slug": "backside-power-delivery",
        "overview": "Backside Power Delivery Network (BSPDN) moves power delivery to the wafer backside, freeing front-side routing for signals and enabling significant improvements in power efficiency and performance.",
        "content_beginner": """Backside power delivery is like adding a second floor to a building for all the electrical wiring, freeing up the main floor for the important stuff.

**The Problem:**
- Chips need lots of power connections
- These compete with signal connections for space
- Current design stacks everything on one side

**The Solution:**
- Put power wiring on the back of the chip
- Signal wiring gets the whole front side
- Better power delivery (lower resistance)
- More room for signals

**Who's Doing It:**
- Intel: PowerVia in 20A/18A nodes
- TSMC: Exploring for N2+
- Samsung: Future roadmaps""",
        "content_advanced": """Backside Power Delivery represents a fundamental shift in chip architecture.

**Conventional vs. BSPDN:**
| Aspect | Conventional | BSPDN |
|--------|--------------|-------|
| Power delivery | Front-side | Backside |
| Signal routing | Shared space | Full front-side |
| Via count | High (>20 layers) | Reduced |
| IR drop | Higher | Lower |
| Cell density | Limited | Improved |

**Implementation Approaches:**
1. **Buried Power Rails (BPR)**: Rails below transistors
2. **Nano-TSV**: Backside to front-side connection
3. **Direct Backside Contact**: Landing on source/drain

**Intel PowerVia:**
- Production with 20A (2024)
- Nano-TSV backside connection
- Eliminates front-side power rails
- >90% power rail utilization

**Key Benefits:**
- 5-10% frequency improvement
- Reduced IR drop (>50%)
- Improved standard cell density
- Lower interconnect resistance
- Better thermal path

**Manufacturing Challenges:**
- Wafer thinning (<50µm)
- Nano-TSV formation
- Backside metallization
- Wafer handling
- Alignment front-to-back

**Process Integration:**
1. Front-side transistors + lower metal
2. Bonding to carrier wafer
3. Wafer thinning
4. Backside via and metal
5. Final integration""",
        "diagrams": [],
        "equations": [
            {"latex": "IR_{drop} = I \\times R_{PDN}", "description": "IR drop in power delivery network"},
            {"latex": "R \\propto \\frac{\\rho L}{A}", "description": "Resistance vs geometry"}
        ],
        "manufacturing_challenges": [
            "Ultra-thin wafer handling",
            "Nano-TSV formation and fill",
            "Front-to-back alignment",
            "Backside contamination control",
            "Thermal management"
        ],
        "applications": ["High-performance logic", "AI accelerators", "Mobile SoCs", "Data center chips"],
        "advantages": ["Improved power delivery", "Higher signal routing density", "Better performance", "Lower power loss"],
        "limitations": ["Manufacturing complexity", "Cost increase", "New failure modes", "Design ecosystem changes"],
        "related_topics": ["topic_2nm", "topic_interconnects", "topic_power_devices"],
        "references": [
            {"title": "Intel PowerVia", "url": "https://www.intel.com/", "source": "Intel"},
            {"title": "Backside PDN Research", "url": "https://www.imec-int.com/", "source": "imec"}
        ],
        "difficulty": "advanced",
        "author": "system",
        "views": 0
    }
]

def get_expanded_topics():
    return EXPANDED_TOPICS
