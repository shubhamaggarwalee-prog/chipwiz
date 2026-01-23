"""
Extended Encyclopedia Topics - Part 2
Adds ~70 more topics to reach 100+ total
Focus: Manufacturing, Materials, Packaging, Design, Fundamentals
"""

EXTENDED_TOPICS_PART2 = [
    # ==================== FUNDAMENTALS ====================
    {
        "topic_id": "topic_band_theory",
        "category_id": "cat_fundamentals",
        "title": "Band Theory of Solids",
        "slug": "band-theory-solids",
        "overview": "Band theory explains how electron energy levels form continuous bands in solids, determining whether a material is a conductor, insulator, or semiconductor based on band gap and electron filling.",
        "content_beginner": """Band theory explains why some materials conduct electricity and others don't.

**Energy Bands:**
- In atoms, electrons have specific energy levels
- In solids, these levels spread into bands
- Valence band: Where electrons normally are
- Conduction band: Where electrons can move freely

**Types of Materials:**
- **Conductors (metals):** Bands overlap, electrons flow easily
- **Insulators:** Large gap, electrons can't jump
- **Semiconductors:** Small gap, controllable conduction

**Why Silicon Works:**
- Band gap of 1.1 eV - just right
- Can control conductivity with doping
- Stable oxide for insulation""",
        "content_advanced": """Band theory provides the quantum mechanical framework for understanding semiconductor behavior.

**Band Structure:**
| Material | Band Gap (eV) | Type |
|----------|---------------|------|
| Silicon | 1.12 | Indirect |
| GaAs | 1.42 | Direct |
| SiO2 | ~9 | Insulator |
| Ge | 0.67 | Indirect |

**Key Concepts:**
- Fermi level: Highest occupied energy at 0K
- Effective mass: Curvature of E-k relationship
- Density of states: Available electron states
- Direct vs indirect gap: Momentum conservation""",
        "diagrams": [],
        "equations": [
            {"latex": "E_g = E_c - E_v", "description": "Band gap energy"},
            {"latex": "n_i = \\sqrt{N_c N_v} e^{-E_g/2kT}", "description": "Intrinsic carrier concentration"}
        ],
        "manufacturing_challenges": [],
        "applications": ["Transistor design", "Solar cells", "LEDs", "Lasers"],
        "advantages": ["Predictive framework", "Material selection guide"],
        "limitations": ["Simplified model", "Temperature effects complex"],
        "related_topics": ["topic_doping", "topic_pn_junction"],
        "references": [],
        "difficulty": "beginner",
        "author": "system",
        "views": 0
    },
    {
        "topic_id": "topic_doping",
        "category_id": "cat_fundamentals",
        "title": "Semiconductor Doping",
        "slug": "semiconductor-doping",
        "overview": "Doping introduces impurity atoms into semiconductors to control electrical properties. N-type doping adds electrons (donors), while P-type adds holes (acceptors), enabling precise conductivity control.",
        "content_beginner": """Doping is adding special atoms to silicon to control its electrical behavior.

**Pure Silicon:**
- 4 electrons in outer shell
- Forms bonds with 4 neighbors
- Poor conductor at room temperature

**N-type Doping:**
- Add atoms with 5 electrons (Phosphorus, Arsenic)
- Extra electron is free to move
- Creates negative charge carriers

**P-type Doping:**
- Add atoms with 3 electrons (Boron)
- Missing bond creates a "hole"
- Holes act as positive charge carriers

**Why Doping Matters:**
- Controls where current flows
- Creates transistor junctions
- Enables integrated circuits""",
        "content_advanced": """Dopant engineering is critical for transistor performance at advanced nodes.

**Common Dopants:**
| Dopant | Type | Diffusivity | Activation |
|--------|------|-------------|------------|
| Boron | P | High | ~800°C |
| Phosphorus | N | Medium | ~900°C |
| Arsenic | N | Low | ~950°C |
| Antimony | N | Very low | ~1000°C |

**Advanced Concepts:**
- Solid solubility limits
- Transient enhanced diffusion (TED)
- Dopant deactivation mechanisms
- Abrupt junction formation
- Ultra-shallow junctions (<10nm)""",
        "diagrams": [],
        "equations": [
            {"latex": "n = N_D - N_A", "description": "Net electron concentration"},
            {"latex": "\\sigma = q(n\\mu_n + p\\mu_p)", "description": "Conductivity with doping"}
        ],
        "manufacturing_challenges": ["Junction depth control", "Dopant activation", "Diffusion during anneal"],
        "applications": ["CMOS transistors", "Diodes", "Solar cells", "Power devices"],
        "advantages": ["Precise control", "Wide range", "Stable"],
        "limitations": ["Solid solubility limits", "Diffusion during processing"],
        "related_topics": ["topic_ion_implantation", "topic_finfet"],
        "references": [],
        "difficulty": "beginner",
        "author": "system",
        "views": 0
    },
    {
        "topic_id": "topic_pn_junction",
        "category_id": "cat_fundamentals",
        "title": "PN Junction",
        "slug": "pn-junction",
        "overview": "The PN junction forms when P-type and N-type semiconductors meet, creating a depletion region and built-in potential. It's the fundamental building block for diodes, transistors, and solar cells.",
        "content_beginner": """A PN junction is where P-type and N-type silicon meet - it's the heart of all semiconductor devices.

**What Happens at the Junction:**
1. Electrons from N-side diffuse to P-side
2. Holes from P-side diffuse to N-side
3. Creates a depleted region with no free carriers
4. Built-in electric field stops further diffusion

**Key Behaviors:**
- **Forward bias:** Current flows easily
- **Reverse bias:** Almost no current flows
- **Breakdown:** High reverse voltage causes current

**Where It's Used:**
- Diodes (one-way current)
- Transistor source/drain junctions
- Solar cells (light creates current)
- LEDs (current creates light)""",
        "content_advanced": """PN junction physics governs transistor leakage, capacitance, and breakdown characteristics.

**Junction Parameters:**
| Parameter | Expression | Impact |
|-----------|------------|--------|
| Built-in potential | Vbi = (kT/q)ln(NaNd/ni²) | Threshold |
| Depletion width | W = √(2ε(Vbi-V)/qN) | Capacitance |
| Junction capacitance | Cj = εA/W | Speed |

**Advanced Topics:**
- Abrupt vs graded junctions
- Avalanche breakdown
- Zener tunneling
- Temperature coefficients
- High-field effects""",
        "diagrams": [],
        "equations": [
            {"latex": "I = I_s(e^{qV/kT} - 1)", "description": "Diode equation"},
            {"latex": "V_{bi} = \\frac{kT}{q}\\ln\\frac{N_a N_d}{n_i^2}", "description": "Built-in potential"}
        ],
        "manufacturing_challenges": ["Junction depth control", "Abrupt profiles", "Leakage minimization"],
        "applications": ["Diodes", "Transistors", "Solar cells", "LEDs", "Photodetectors"],
        "advantages": ["Fundamental building block", "Well understood", "Controllable"],
        "limitations": ["Leakage current", "Temperature sensitivity", "Breakdown voltage limits"],
        "related_topics": ["topic_doping", "topic_finfet", "topic_band_theory"],
        "references": [],
        "difficulty": "intermediate",
        "author": "system",
        "views": 0
    },
    {
        "topic_id": "topic_mosfet_basics",
        "category_id": "cat_fundamentals",
        "title": "MOSFET Fundamentals",
        "slug": "mosfet-fundamentals",
        "overview": "The Metal-Oxide-Semiconductor Field-Effect Transistor (MOSFET) is the fundamental building block of modern ICs. Gate voltage controls current flow between source and drain through an oxide-insulated channel.",
        "content_beginner": """MOSFET is the basic switch used in all modern chips - billions of them in your phone!

**How It Works:**
- Source: Where current enters
- Drain: Where current exits
- Gate: Controls the switch (like a valve)
- Channel: Path for current

**Switching Action:**
1. No gate voltage → Channel off → No current
2. Apply gate voltage → Channel forms → Current flows
3. More voltage → More current (up to a limit)

**Two Types:**
- NMOS: Turns on with positive gate voltage
- PMOS: Turns on with negative gate voltage

**Why MOSFETs Rule:**
- Very low power (no DC gate current)
- Very small (billions per chip)
- Very fast (GHz switching)""",
        "content_advanced": """MOSFET physics encompasses channel formation, transport, and short-channel effects.

**Key Parameters:**
| Parameter | Symbol | Impact |
|-----------|--------|--------|
| Threshold voltage | Vth | On/off transition |
| Subthreshold slope | SS | Leakage |
| Transconductance | gm | Gain |
| Output conductance | gds | Drive |

**Scaling Challenges:**
- Vth variation with channel length
- DIBL (drain-induced barrier lowering)
- Subthreshold leakage
- Gate leakage tunneling
- Velocity saturation

**Modern Solutions:**
- High-K/metal gate
- Strained silicon
- FinFET/GAA architectures
- SOI substrates""",
        "diagrams": [],
        "equations": [
            {"latex": "I_D = \\mu C_{ox} \\frac{W}{L}(V_{GS}-V_{th})V_{DS}", "description": "Linear region"},
            {"latex": "I_D = \\frac{1}{2}\\mu C_{ox} \\frac{W}{L}(V_{GS}-V_{th})^2", "description": "Saturation region"}
        ],
        "manufacturing_challenges": ["Gate oxide quality", "Threshold control", "Channel doping uniformity"],
        "applications": ["Logic gates", "Memory", "Amplifiers", "Power switches"],
        "advantages": ["Low power", "Scalable", "High density", "Fast"],
        "limitations": ["Short-channel effects", "Leakage at small sizes", "Variability"],
        "related_topics": ["topic_finfet", "topic_gaafet", "topic_cmos"],
        "references": [],
        "difficulty": "beginner",
        "author": "system",
        "views": 0
    },
    {
        "topic_id": "topic_cmos",
        "category_id": "cat_fundamentals",
        "title": "CMOS Technology",
        "slug": "cmos-technology",
        "overview": "Complementary MOS (CMOS) pairs NMOS and PMOS transistors to create logic circuits with near-zero static power. CMOS is the dominant technology for digital ICs, from microprocessors to memory.",
        "content_beginner": """CMOS uses both types of transistors (N and P) together for super-efficient circuits.

**The Brilliant Idea:**
- NMOS pulls output to ground (0)
- PMOS pulls output to power (1)
- One is always off → Almost no standby power!

**CMOS Inverter (NOT gate):**
- Input 0: PMOS on, NMOS off → Output 1
- Input 1: NMOS on, PMOS off → Output 0
- Only draws power when switching

**Why CMOS Won:**
- Ultra-low standby power
- Full voltage swing (0 to VDD)
- High noise immunity
- Scalable to tiny sizes""",
        "content_advanced": """CMOS design involves complex trade-offs between speed, power, and area.

**Power Components:**
| Type | Formula | Reduction |
|------|---------|-----------|
| Dynamic | CV²f | Lower V, C |
| Short-circuit | Isc×V×f | Fast edges |
| Leakage | Ileak×V | Lower V, high Vth |

**Advanced CMOS:**
- Multi-Vth libraries
- Power gating
- Clock gating
- Dynamic voltage scaling
- Body biasing
- FinFET/GAA integration""",
        "diagrams": [],
        "equations": [
            {"latex": "P_{dyn} = \\alpha C V_{DD}^2 f", "description": "Dynamic power"},
            {"latex": "P_{leak} = I_{leak} V_{DD}", "description": "Static power"}
        ],
        "manufacturing_challenges": ["N/P balance", "Well isolation", "Latch-up prevention"],
        "applications": ["Microprocessors", "Memory", "ASICs", "FPGAs", "SoCs"],
        "advantages": ["Low power", "High density", "Noise immunity", "Scalable"],
        "limitations": ["Leakage at small nodes", "Complexity", "Cost"],
        "related_topics": ["topic_mosfet_basics", "topic_finfet", "topic_power_management"],
        "references": [],
        "difficulty": "beginner",
        "author": "system",
        "views": 0
    },
    # ==================== MATERIALS ====================
    {
        "topic_id": "topic_silicon",
        "category_id": "cat_materials",
        "title": "Silicon Material Properties",
        "slug": "silicon-material-properties",
        "overview": "Silicon is the foundation of the semiconductor industry due to its abundant availability, excellent oxide, and ideal band gap. Ultra-pure single-crystal silicon wafers enable modern IC fabrication.",
        "content_beginner": """Silicon is the most important material in electronics - it's why we call it "Silicon Valley"!

**Why Silicon?**
- Second most abundant element on Earth (sand!)
- Band gap perfect for room temperature electronics
- Forms excellent insulating oxide (SiO2)
- Can be made extremely pure

**Silicon Wafers:**
- Grown as large single crystals
- Sliced into thin wafers (775µm)
- Polished to atomic smoothness
- Typical sizes: 200mm, 300mm diameter

**Crystal Structure:**
- Diamond cubic structure
- Each atom bonds to 4 neighbors
- Regular, repeatable pattern
- Can be doped precisely""",
        "content_advanced": """Silicon material engineering encompasses crystal growth, defect control, and surface preparation.

**Silicon Properties:**
| Property | Value | Significance |
|----------|-------|--------------|
| Band gap | 1.12 eV | Operating temp |
| Mobility (e-) | 1450 cm²/Vs | Speed |
| Mobility (h+) | 500 cm²/Vs | PMOS slower |
| Thermal cond. | 150 W/mK | Heat dissipation |

**Wafer Specifications:**
- Resistivity: 1-20 Ω-cm (typical)
- Oxygen: <10 ppma (interstitial)
- Crystal orientation: (100), (111)
- Bow/warp: <40µm
- Surface roughness: <0.5nm RMS

**Advanced Topics:**
- Czochralski vs Float-zone growth
- Epitaxial layer engineering
- SOI wafer fabrication
- Strained silicon techniques""",
        "diagrams": [],
        "equations": [
            {"latex": "n_i = 1.5 \\times 10^{10} cm^{-3}", "description": "Intrinsic carrier concentration at 300K"},
            {"latex": "\\mu = \\frac{q\\tau}{m^*}", "description": "Carrier mobility"}
        ],
        "manufacturing_challenges": ["Crystal defect control", "Contamination prevention", "Wafer flatness"],
        "applications": ["All CMOS ICs", "Power devices", "Solar cells", "MEMS"],
        "advantages": ["Abundant", "Excellent oxide", "Well understood", "Scalable"],
        "limitations": ["Indirect band gap", "Lower mobility than III-V"],
        "related_topics": ["topic_wafer_fabrication", "topic_epitaxy", "topic_soi"],
        "references": [],
        "difficulty": "beginner",
        "author": "system",
        "views": 0
    },
    {
        "topic_id": "topic_high_k",
        "category_id": "cat_materials",
        "title": "High-K Dielectrics",
        "slug": "high-k-dielectrics",
        "overview": "High-K dielectrics replaced SiO2 as gate insulators when traditional oxide became too thin. Materials like HfO2 provide equivalent capacitance with physically thicker films, reducing tunneling leakage.",
        "content_beginner": """High-K dielectrics solved a major problem: gate oxide was getting too thin!

**The Problem:**
- Smaller transistors need thinner gate oxide
- Below ~1nm, electrons tunnel through
- Tunneling causes unacceptable leakage

**The Solution: High-K Materials:**
- "K" means dielectric constant
- Higher K = same capacitance with thicker film
- HfO2 has K ≈ 25 (vs SiO2 K ≈ 4)
- Can be 5x thicker for same effect

**Why It Works:**
- Thicker film blocks tunneling
- Same electrical effect on transistor
- Enabled continued scaling past 45nm""",
        "content_advanced": """High-K integration requires careful interface engineering and metal gate compatibility.

**High-K Materials:**
| Material | K Value | Band Gap | Stability |
|----------|---------|----------|-----------|
| SiO2 | 3.9 | 9 eV | Excellent |
| HfO2 | 25 | 5.8 eV | Good |
| ZrO2 | 25 | 5.8 eV | Good |
| Al2O3 | 9 | 8.8 eV | Excellent |

**Integration Challenges:**
- Interface layer formation
- Fixed charge and traps
- Fermi level pinning
- Reliability (PBTI, NBTI)
- Metal gate work function

**EOT Calculation:**
- EOT = (3.9/K) × t_physical
- Target EOT: <1nm for advanced nodes
- Interface layer adds ~0.3-0.5nm""",
        "diagrams": [],
        "equations": [
            {"latex": "EOT = \\frac{3.9}{K_{high-K}} \\times t_{high-K}", "description": "Equivalent oxide thickness"},
            {"latex": "C = \\frac{K \\epsilon_0 A}{t}", "description": "Capacitance"}
        ],
        "manufacturing_challenges": ["Interface quality", "Crystallization control", "Work function tuning"],
        "applications": ["Logic transistors", "DRAM capacitors", "Flash memory", "MIM capacitors"],
        "advantages": ["Reduced leakage", "Enables scaling", "Mature"],
        "limitations": ["Interface complexity", "Reliability concerns", "Higher K materials needed"],
        "related_topics": ["topic_ald", "topic_finfet", "topic_gaafet"],
        "references": [],
        "difficulty": "intermediate",
        "author": "system",
        "views": 0
    },
    {
        "topic_id": "topic_copper_interconnects",
        "category_id": "cat_materials",
        "title": "Copper Interconnects",
        "slug": "copper-interconnects",
        "overview": "Copper replaced aluminum as the interconnect metal starting at 180nm due to its 40% lower resistivity. Damascene processing and barrier metals enable reliable copper integration in advanced nodes.",
        "content_beginner": """Copper wires connect billions of transistors inside a chip - replacing aluminum made chips faster!

**Why Copper?**
- 40% lower resistance than aluminum
- Less heat, faster signals
- More reliable at high current

**The Challenge:**
- Copper poisons silicon (diffuses into it)
- Can't be etched like aluminum
- Needs special processing

**Damascene Process:**
1. Etch trenches in insulator
2. Deposit barrier layer (blocks copper)
3. Fill with copper
4. Polish flat (CMP)

**Barrier Layer:**
- TaN/Ta is most common
- Blocks copper diffusion
- Provides adhesion""",
        "content_advanced": """Copper interconnect scaling faces resistivity rise and reliability challenges.

**Resistivity Scaling:**
| Feature | Resistivity | Cause |
|---------|-------------|-------|
| Bulk Cu | 1.7 µΩ-cm | Ideal |
| 100nm line | 2.2 µΩ-cm | Grain boundary |
| 20nm line | 4-5 µΩ-cm | Surface scattering |
| 10nm line | 8-10 µΩ-cm | All effects |

**Advanced Integration:**
- Cobalt liner/cap for reliability
- Ruthenium barrier at small pitch
- Hybrid Cu/Ru metallization
- Subtractive patterning exploration

**Reliability Concerns:**
- Electromigration (EM)
- Stress migration (SM)
- Time-dependent dielectric breakdown
- Via reliability""",
        "diagrams": [],
        "equations": [
            {"latex": "\\rho = \\rho_0(1 + \\frac{\\lambda}{d})", "description": "Size-dependent resistivity"},
            {"latex": "MTTF = A j^{-n} e^{E_a/kT}", "description": "Electromigration lifetime"}
        ],
        "manufacturing_challenges": ["Barrier scaling", "Void-free fill", "Resistivity rise", "EM reliability"],
        "applications": ["All advanced logic ICs", "Memory interconnects", "Advanced packaging"],
        "advantages": ["Low resistivity", "High reliability with barriers", "Mature process"],
        "limitations": ["Resistivity increase at small sizes", "Barrier overhead", "EM limits"],
        "related_topics": ["topic_cmp", "topic_damascene", "topic_low_k"],
        "references": [],
        "difficulty": "intermediate",
        "author": "system",
        "views": 0
    },
    {
        "topic_id": "topic_low_k",
        "category_id": "cat_materials",
        "title": "Low-K Dielectrics",
        "slug": "low-k-dielectrics",
        "overview": "Low-K dielectrics reduce interconnect capacitance by replacing SiO2 (K=4) with materials having K<3. This decreases RC delay and power consumption in the back-end-of-line.",
        "content_beginner": """Low-K materials help signals travel faster through the chip's wiring.

**The Problem:**
- Wires have resistance (R) and capacitance (C)
- RC delay slows signals
- Capacitance depends on dielectric material

**The Solution:**
- Use insulators with lower K (dielectric constant)
- Lower K = lower capacitance
- Faster signals, less power

**Low-K Materials:**
- SiO2: K = 4.0 (baseline)
- FSG (F-doped SiO2): K = 3.5
- SiCOH: K = 2.5-3.0
- Porous low-K: K = 2.0-2.5
- Air gaps: K = 1.0 (ideal)""",
        "content_advanced": """Low-K integration presents significant mechanical and process challenges.

**Low-K Options:**
| Material | K Value | Porosity | Modulus |
|----------|---------|----------|---------|
| TEOS SiO2 | 4.0 | 0% | 70 GPa |
| FSG | 3.5 | 0% | 60 GPa |
| Dense SiCOH | 3.0 | 0-5% | 15 GPa |
| Porous SiCOH | 2.5 | 15-25% | 8 GPa |
| ULK | 2.2 | 25-35% | 5 GPa |

**Integration Challenges:**
- Mechanical weakness (CMP, packaging)
- Moisture absorption
- Plasma damage during etch
- Barrier adhesion
- Thermal stability

**Advanced Approaches:**
- Air gap integration
- Self-assembled monolayers
- Metal capping layers
- Hybrid integration schemes""",
        "diagrams": [],
        "equations": [
            {"latex": "RC = \\rho \\epsilon K \\frac{L^2}{tw}", "description": "RC delay"},
            {"latex": "K_{eff} = \\frac{t_{total}}{\\sum(t_i/K_i)}", "description": "Effective K for stack"}
        ],
        "manufacturing_challenges": ["Mechanical integrity", "Plasma damage", "Moisture sensitivity", "Integration complexity"],
        "applications": ["Advanced logic BEOL", "High-frequency circuits", "Low-power designs"],
        "advantages": ["Lower RC delay", "Reduced power", "Enables scaling"],
        "limitations": ["Weak mechanical properties", "Process complexity", "Reliability concerns"],
        "related_topics": ["topic_copper_interconnects", "topic_cmp", "topic_beol"],
        "references": [],
        "difficulty": "intermediate",
        "author": "system",
        "views": 0
    },
    {
        "topic_id": "topic_iii_v",
        "category_id": "cat_materials",
        "title": "III-V Semiconductors",
        "slug": "iii-v-semiconductors",
        "overview": "III-V semiconductors like GaAs, InP, and GaN offer superior electron mobility and direct band gaps compared to silicon. They're essential for RF, photonics, and high-power applications.",
        "content_beginner": """III-V semiconductors are special materials that do things silicon can't.

**What are III-V Materials?**
- Made from Group III (Ga, In, Al) + Group V (As, P, N)
- Examples: GaAs, InP, GaN, InGaAs

**Why They're Special:**
- Much faster electron movement (mobility)
- Direct band gap (efficient light emission)
- Can handle high power and frequency

**Where They're Used:**
- 5G cell phone amplifiers
- Lasers in fiber optics
- LED lights
- Satellite communications
- Power electronics (GaN)""",
        "content_advanced": """III-V materials enable performance impossible with silicon alone.

**Material Properties:**
| Material | Band Gap | Mobility (e-) | Application |
|----------|----------|---------------|-------------|
| GaAs | 1.42 eV | 8500 | RF, solar |
| InP | 1.35 eV | 5400 | Photonics |
| GaN | 3.4 eV | 1500 | Power, RF |
| InGaAs | Tunable | 12000 | Channels |

**Integration Approaches:**
- Heterogeneous integration on Si
- Wafer bonding
- Epitaxial growth on Si
- Chiplet integration

**Challenges:**
- Lattice mismatch with Si
- Higher cost than Si
- Smaller wafer sizes
- Defect density control""",
        "diagrams": [],
        "equations": [
            {"latex": "v_{sat} = \\mu E", "description": "Saturation velocity"},
            {"latex": "f_T = \\frac{g_m}{2\\pi C_{gs}}", "description": "Cutoff frequency"}
        ],
        "manufacturing_challenges": ["Lattice mismatch", "Defect control", "Cost", "Integration with Si"],
        "applications": ["5G RF", "Power amplifiers", "Lasers", "LEDs", "High-speed logic"],
        "advantages": ["High mobility", "Direct band gap", "High frequency", "High power"],
        "limitations": ["Cost", "Wafer size", "Integration complexity", "No good native oxide"],
        "related_topics": ["topic_gan_power", "topic_rf_devices", "topic_photonics"],
        "references": [],
        "difficulty": "intermediate",
        "author": "system",
        "views": 0
    },
    {
        "topic_id": "topic_sic",
        "category_id": "cat_materials",
        "title": "Silicon Carbide (SiC)",
        "slug": "silicon-carbide",
        "overview": "Silicon Carbide is a wide band gap semiconductor enabling high-voltage, high-temperature power electronics. SiC devices offer 10x lower switching losses than silicon for EV inverters and power conversion.",
        "content_beginner": """Silicon Carbide (SiC) is transforming electric vehicles and power electronics.

**Why SiC?**
- Can handle much higher voltages
- Works at higher temperatures
- Switches on/off much faster
- Lower energy losses

**Compared to Silicon:**
- 3x higher band gap (3.3 eV vs 1.1 eV)
- 10x higher breakdown field
- 3x better thermal conductivity
- Smaller, lighter power systems

**Where It's Used:**
- Electric vehicle inverters
- EV charging stations
- Solar inverters
- Industrial power supplies
- Train traction systems""",
        "content_advanced": """SiC device technology has matured significantly with 150mm and 200mm wafer production.

**SiC vs Si Properties:**
| Property | Si | 4H-SiC | Advantage |
|----------|-----|--------|-----------|
| Band gap | 1.1 eV | 3.3 eV | High temp |
| Breakdown | 0.3 MV/cm | 3 MV/cm | High voltage |
| Thermal | 150 W/mK | 490 W/mK | Cooling |
| Mobility | 1450 | 900 | Lower |

**Device Types:**
- SiC MOSFETs: 650V-3.3kV
- SiC Schottky diodes: Fast recovery
- SiC JFETs: Normally-on devices

**Manufacturing Challenges:**
- Crystal defect density
- Gate oxide reliability
- Substrate cost
- Epitaxy quality""",
        "diagrams": [],
        "equations": [
            {"latex": "BV = \\frac{E_c^2 \\epsilon}{2qN_D}", "description": "Breakdown voltage"},
            {"latex": "R_{on} \\propto BV^{2.5}", "description": "On-resistance vs voltage"}
        ],
        "manufacturing_challenges": ["Substrate defects", "Gate oxide reliability", "Cost reduction", "Wafer size scaling"],
        "applications": ["EV inverters", "EV chargers", "Solar", "Industrial", "Grid"],
        "advantages": ["High voltage", "High efficiency", "High temperature", "Fast switching"],
        "limitations": ["Higher cost than Si", "Gate oxide reliability", "Lower mobility"],
        "related_topics": ["topic_automotive_chips", "topic_power_devices", "topic_iii_v"],
        "references": [],
        "difficulty": "intermediate",
        "author": "system",
        "views": 0
    },
    # ==================== MORE MANUFACTURING ====================
    {
        "topic_id": "topic_ald",
        "category_id": "cat_manufacturing",
        "title": "Atomic Layer Deposition (ALD)",
        "slug": "atomic-layer-deposition",
        "overview": "ALD deposits thin films one atomic layer at a time through self-limiting surface reactions. This enables angstrom-level thickness control and conformal coating of high-aspect-ratio structures.",
        "content_beginner": """ALD builds ultra-thin layers one atom at a time - like painting with molecules!

**How ALD Works:**
1. First chemical sticks to surface (self-limiting)
2. Purge away excess
3. Second chemical reacts with first
4. Purge again
5. Repeat for each atomic layer

**Why It's Special:**
- Precise thickness control (angstroms!)
- Coats everything uniformly
- Even inside deep holes and trenches
- Perfect for atomic-scale structures

**Where It's Used:**
- Gate dielectrics (HfO2)
- DRAM capacitors
- 3D NAND word lines
- Barrier layers""",
        "content_advanced": """ALD is essential for conformal films in 3D device architectures.

**ALD Process Types:**
| Type | Mechanism | Rate | Application |
|------|-----------|------|-------------|
| Thermal | Heat-activated | Slow | High quality |
| Plasma | Plasma-enhanced | Medium | Lower temp |
| Spatial | Continuous | Fast | High volume |

**Key Parameters:**
- Growth per cycle: 0.5-2 Å
- Temperature window: 200-400°C
- Precursor dose time: 0.1-1s
- Purge time: 1-10s
- Conformality: >95% typical

**Materials:**
- High-K: HfO2, ZrO2, Al2O3
- Metals: TaN, TiN, Ru, W
- Barrier: TaN, TiN
- Spacers: SiN, SiO2""",
        "diagrams": [],
        "equations": [
            {"latex": "t = GPC \\times N_{cycles}", "description": "Film thickness"},
            {"latex": "Conformality = \\frac{t_{bottom}}{t_{top}} \\times 100\\%", "description": "Step coverage"}
        ],
        "manufacturing_challenges": ["Throughput", "Precursor cost", "Particle control", "Uniformity"],
        "applications": ["Gate dielectrics", "DRAM", "3D NAND", "Barrier layers", "Advanced packaging"],
        "advantages": ["Atomic precision", "Excellent conformality", "Low temperature possible", "Wide material range"],
        "limitations": ["Slow deposition", "Equipment cost", "Precursor availability"],
        "related_topics": ["topic_high_k", "topic_nand", "topic_gaafet"],
        "references": [],
        "difficulty": "intermediate",
        "author": "system",
        "views": 0
    },
    {
        "topic_id": "topic_cvd",
        "category_id": "cat_manufacturing",
        "title": "Chemical Vapor Deposition (CVD)",
        "slug": "chemical-vapor-deposition",
        "overview": "CVD deposits thin films from gas-phase chemical reactions at the wafer surface. Variants include LPCVD, PECVD, and MOCVD, each optimized for different materials and applications.",
        "content_beginner": """CVD grows thin films on wafers using chemical reactions from gases.

**Basic Process:**
1. Precursor gases flow into chamber
2. Gases react at hot wafer surface
3. Film deposits atom by atom
4. Byproducts pumped away

**Types of CVD:**
- **LPCVD:** Low pressure, very uniform
- **PECVD:** Plasma helps at lower temperature
- **MOCVD:** Metal-organic precursors

**What's Made with CVD:**
- Silicon dioxide insulation
- Silicon nitride barriers
- Polysilicon gates
- Tungsten metal fill
- Epitaxial silicon layers""",
        "content_advanced": """CVD encompasses multiple techniques optimized for different film requirements.

**CVD Variants:**
| Type | Pressure | Temp | Conformality |
|------|----------|------|--------------|
| LPCVD | 0.1-1 Torr | 600-800°C | Excellent |
| PECVD | 0.5-5 Torr | 200-400°C | Good |
| HDPCVD | mTorr | 400°C | Gap fill |
| MOCVD | 50-760 Torr | 500-1000°C | III-V |

**Key Reactions:**
- SiH4 + O2 → SiO2 + H2
- SiH4 + NH3 → SiNx + H2
- WF6 + SiH4 → W + SiF4 + H2

**Process Control:**
- Temperature uniformity
- Gas flow distribution
- Pressure stability
- Plasma power (PECVD)""",
        "diagrams": [],
        "equations": [
            {"latex": "Rate = k_0 e^{-E_a/RT} P^n", "description": "Arrhenius deposition rate"},
            {"latex": "Nu = \\frac{\\sigma}{mean} \\times 100\\%", "description": "Non-uniformity"}
        ],
        "manufacturing_challenges": ["Particle control", "Uniformity", "Step coverage", "Film stress"],
        "applications": ["Dielectrics", "Hard masks", "Tungsten fill", "Epitaxy", "III-V growth"],
        "advantages": ["High quality films", "Good uniformity", "Wide material range", "Scalable"],
        "limitations": ["High temperature (some types)", "Conformality limits", "Precursor handling"],
        "related_topics": ["topic_ald", "topic_epitaxy", "topic_pecvd"],
        "references": [],
        "difficulty": "intermediate",
        "author": "system",
        "views": 0
    },
    {
        "topic_id": "topic_pvd",
        "category_id": "cat_manufacturing",
        "title": "Physical Vapor Deposition (PVD)",
        "slug": "physical-vapor-deposition",
        "overview": "PVD deposits thin films through physical processes like sputtering or evaporation. It's essential for metal films including copper seed layers, barrier metals, and aluminum interconnects.",
        "content_beginner": """PVD deposits metals by physically moving atoms from a source to the wafer.

**Two Main Methods:**

**Sputtering:**
- Bombard target with argon ions
- Atoms knocked off target
- Atoms land on wafer
- Most common PVD method

**Evaporation:**
- Heat source until it evaporates
- Atoms travel to wafer
- Used for some metals

**What PVD Makes:**
- Aluminum wiring
- Copper seed layers
- Barrier metals (TaN, TiN)
- Silicide contacts""",
        "content_advanced": """PVD technology has evolved to enable conformal deposition and atomic-level control.

**PVD Variants:**
| Type | Mechanism | Coverage | Use |
|------|-----------|----------|-----|
| DC sputter | Ion bombardment | Directional | Metals |
| RF sputter | RF plasma | Better | Insulators |
| Magnetron | Magnetic confinement | High rate | Production |
| IMP | Ionized metal | Conformal | Barriers |
| HiPIMS | High power impulse | Dense films | Advanced |

**Key Parameters:**
- Deposition rate: 1-100 nm/min
- Uniformity: <2% 3σ
- Step coverage: 10-50% (standard)
- Film stress: Controlled

**Advanced Techniques:**
- Collimated sputtering
- Long-throw sputtering
- Ionized PVD for conformality""",
        "diagrams": [],
        "equations": [
            {"latex": "Y = \\frac{atoms\\ ejected}{incident\\ ion}", "description": "Sputter yield"},
            {"latex": "Rate \\propto \\frac{P \\times Y}{d^2}", "description": "Deposition rate"}
        ],
        "manufacturing_challenges": ["Step coverage", "Particle control", "Target utilization", "Film stress"],
        "applications": ["Metal interconnects", "Barrier layers", "Seed layers", "Hard masks"],
        "advantages": ["High purity", "Wide material range", "Good adhesion", "Controllable stress"],
        "limitations": ["Poor step coverage", "Target cost", "Particle generation"],
        "related_topics": ["topic_copper_interconnects", "topic_barrier_metals", "topic_damascene"],
        "references": [],
        "difficulty": "intermediate",
        "author": "system",
        "views": 0
    },
    {
        "topic_id": "topic_epitaxy",
        "category_id": "cat_manufacturing",
        "title": "Epitaxial Growth",
        "slug": "epitaxial-growth",
        "overview": "Epitaxy grows single-crystal semiconductor layers on crystalline substrates while maintaining crystal structure. It enables doping profiles, strain engineering, and heterojunction devices.",
        "content_beginner": """Epitaxy grows perfectly aligned crystal layers on top of a wafer.

**What Makes It Special:**
- New layer copies crystal structure below
- Can change doping as you grow
- Can add different materials (heteroepitaxy)
- Enables advanced transistor designs

**Types of Epitaxy:**
- **Homoepitaxy:** Same material (Si on Si)
- **Heteroepitaxy:** Different materials (SiGe on Si)

**Where It's Used:**
- Transistor source/drain (SiGe)
- Channel strain engineering
- III-V device layers
- Power device drift regions""",
        "content_advanced": """Epitaxial processes enable strain engineering and heterojunction integration.

**Epitaxy Methods:**
| Method | Temp | Rate | Application |
|--------|------|------|-------------|
| CVD | 500-1000°C | Fast | Si, SiGe |
| MBE | 400-700°C | Slow | III-V, research |
| MOCVD | 500-1000°C | Medium | III-V production |

**Strain Engineering:**
- SiGe S/D: Compressive in channel (PMOS boost)
- Si:C S/D: Tensile in channel (NMOS boost)
- Strain transfer efficiency: 60-80%

**Key Parameters:**
- Growth rate: 1-100 nm/min
- Thickness control: <1%
- Doping abruptness: <2 nm/decade
- Defect density: <100/cm²""",
        "diagrams": [],
        "equations": [
            {"latex": "\\epsilon = \\frac{a_f - a_s}{a_s}", "description": "Lattice mismatch strain"},
            {"latex": "h_c = \\frac{b}{8\\pi\\epsilon}", "description": "Critical thickness"}
        ],
        "manufacturing_challenges": ["Defect control", "Uniformity", "Selectivity", "Strain relaxation"],
        "applications": ["Strained channels", "Source/drain", "III-V integration", "Power devices"],
        "advantages": ["Crystal quality", "Doping control", "Strain engineering", "Heterostructures"],
        "limitations": ["High temperature", "Defects from mismatch", "Cost", "Throughput"],
        "related_topics": ["topic_finfet", "topic_sige", "topic_iii_v"],
        "references": [],
        "difficulty": "intermediate",
        "author": "system",
        "views": 0
    },
    {
        "topic_id": "topic_wet_clean",
        "category_id": "cat_manufacturing",
        "title": "Wet Cleaning Processes",
        "slug": "wet-cleaning-processes",
        "overview": "Wet cleaning removes contaminants, particles, and residues using chemical solutions. Clean wafer surfaces are critical for device performance, with contamination specs at parts-per-trillion levels.",
        "content_beginner": """Wet cleaning keeps wafers incredibly clean using special chemical baths.

**Why Cleaning Matters:**
- Even tiny particles ruin devices
- Metal contamination causes failures
- Organic residues affect film growth
- Cleanliness enables yield

**Standard Clean Sequence:**
1. **SC-1 (APM):** NH4OH + H2O2 - removes particles
2. **SC-2 (HPM):** HCl + H2O2 - removes metals
3. **HF dip:** Removes native oxide

**Contamination Types:**
- Particles: Physical defects
- Metals: Electrical contamination
- Organics: Surface residues
- Native oxide: Interfacial layer""",
        "content_advanced": """Advanced cleaning requires atomic-level surface preparation with minimal material loss.

**Cleaning Chemistries:**
| Solution | Composition | Target |
|----------|-------------|--------|
| SC-1/APM | NH4OH:H2O2:H2O | Particles, organics |
| SC-2/HPM | HCl:H2O2:H2O | Metals |
| Piranha | H2SO4:H2O2 | Heavy organics |
| DHF | Dilute HF | Oxide removal |
| ozonated DI | O3 in H2O | Organics |

**Process Challenges:**
- Material selectivity
- Surface roughening
- Etch uniformity
- Chemical consumption
- Environmental concerns

**Advanced Techniques:**
- Single wafer processing
- Ozone-based cleaning
- Supercritical CO2
- Plasma pre-clean
- Megasonic agitation""",
        "diagrams": [],
        "equations": [
            {"latex": "Etch\\ Rate = k_0 e^{-E_a/RT} C^n", "description": "Chemical etch rate"},
            {"latex": "PRE = \\frac{Particles_{before} - Particles_{after}}{Particles_{before}}", "description": "Particle removal efficiency"}
        ],
        "manufacturing_challenges": ["Material loss", "Selectivity", "Throughput", "Chemical cost", "Environmental"],
        "applications": ["Pre-gate clean", "Pre-metal clean", "Post-etch residue removal", "Particle removal"],
        "advantages": ["Effective contamination removal", "Selective etching", "Mature technology"],
        "limitations": ["Chemical handling", "Material consumption", "Environmental impact"],
        "related_topics": ["topic_cmp", "topic_etch", "topic_contamination"],
        "references": [],
        "difficulty": "intermediate",
        "author": "system",
        "views": 0
    },
    # ==================== MORE PACKAGING ====================
    {
        "topic_id": "topic_wire_bonding",
        "category_id": "cat_packaging",
        "title": "Wire Bonding Technology",
        "slug": "wire-bonding-technology",
        "overview": "Wire bonding creates electrical connections between die and package using thin gold, copper, or aluminum wires. It remains the most cost-effective interconnect method for most semiconductor packages.",
        "content_beginner": """Wire bonding connects the chip to the outside world using tiny wires.

**How It Works:**
1. Bond wire to chip pad (first bond)
2. Loop wire to package lead
3. Bond to lead frame (second bond)
4. Cut wire, move to next pad

**Wire Materials:**
- **Gold:** Traditional, reliable, expensive
- **Copper:** Lower cost, harder to bond
- **Aluminum:** Used for power devices

**Bond Types:**
- Ball bond: Melts wire tip into ball
- Wedge bond: Presses wire flat

**Still Popular Because:**
- Very low cost
- Flexible routing
- Proven reliability
- Works with any die size""",
        "content_advanced": """Wire bonding technology continues to evolve with finer pitches and new materials.

**Wire Bonding Parameters:**
| Parameter | Gold | Copper | Aluminum |
|-----------|------|--------|----------|
| Diameter | 15-50µm | 15-50µm | 25-500µm |
| Pitch | 35-60µm | 40-60µm | 100µm+ |
| Speed | 15-30/s | 10-20/s | 5-15/s |

**Process Window:**
- Bond force: 15-100 grams
- Ultrasonic power: 50-200mW
- Temperature: 150-220°C
- Time: 5-20ms per bond

**Advanced Techniques:**
- Copper wire with palladium coating
- Heavy aluminum wire for power
- Stacked die bonding
- Fine pitch (<35µm) bonding""",
        "diagrams": [],
        "equations": [
            {"latex": "I_{max} = k \\cdot d^{1.5}", "description": "Wire current capacity"},
            {"latex": "L = \\pi r^2 \\cdot \\rho \\cdot l / A", "description": "Wire inductance"}
        ],
        "manufacturing_challenges": ["Fine pitch bonding", "Copper oxidation", "Loop control", "Pad damage"],
        "applications": ["Memory packages", "Low-cost ICs", "Power modules", "Sensors"],
        "advantages": ["Low cost", "Flexible", "Proven reliability", "Easy repair"],
        "limitations": ["Inductance", "Speed limits", "Pad pitch limits", "Form factor"],
        "related_topics": ["topic_flip_chip", "topic_packaging_basics", "topic_lead_frame"],
        "references": [],
        "difficulty": "beginner",
        "author": "system",
        "views": 0
    },
    {
        "topic_id": "topic_flip_chip",
        "category_id": "cat_packaging",
        "title": "Flip Chip Technology",
        "slug": "flip-chip-technology",
        "overview": "Flip chip mounts die face-down with solder bumps directly connecting to the substrate. This eliminates wire bond inductance, enables higher I/O density, and improves thermal and electrical performance.",
        "content_beginner": """Flip chip turns the die upside down and connects it directly with solder bumps.

**How It Works:**
1. Create solder bumps on die pads
2. Flip die over (face down)
3. Align bumps to substrate pads
4. Reflow solder to make connections
5. Fill gap with underfill epoxy

**Advantages over Wire Bonding:**
- Shorter connections (less inductance)
- All connections at once
- Better thermal path
- Higher I/O density possible

**Where It's Used:**
- High-performance processors
- Graphics chips
- Mobile SoCs
- RF devices""",
        "content_advanced": """Flip chip technology has evolved to support fine pitch and high-density interconnects.

**Bump Technologies:**
| Type | Pitch | Height | Application |
|------|-------|--------|-------------|
| C4 (solder) | 150-250µm | 75-100µm | Legacy |
| µbump | 40-80µm | 25-40µm | 2.5D |
| Cu pillar | 40-130µm | 30-60µm | Advanced |
| Hybrid bond | <10µm | Cu-Cu | 3D |

**Process Considerations:**
- Underfill for reliability
- CTE mismatch management
- Bump coplanarity
- Intermetallic formation

**Advanced Variants:**
- Copper pillar bumps
- Micro-bumps for 2.5D/3D
- Thermocompression bonding
- Mass reflow vs TCB""",
        "diagrams": [],
        "equations": [
            {"latex": "L_{bump} << L_{wire}", "description": "Inductance advantage"},
            {"latex": "R_{thermal} = \\frac{t}{k \\cdot A}", "description": "Thermal resistance"}
        ],
        "manufacturing_challenges": ["Bump coplanarity", "Underfill voids", "CTE stress", "Fine pitch yield"],
        "applications": ["CPUs", "GPUs", "Mobile SoCs", "RF", "HBM integration"],
        "advantages": ["Low inductance", "High I/O density", "Good thermal", "Short interconnects"],
        "limitations": ["Cost", "Underfill required", "Inspection difficult", "Known good die needed"],
        "related_topics": ["topic_hybrid_bonding", "topic_cowos", "topic_hbm"],
        "references": [],
        "difficulty": "intermediate",
        "author": "system",
        "views": 0
    },
    {
        "topic_id": "topic_fan_out",
        "category_id": "cat_packaging",
        "title": "Fan-Out Wafer Level Packaging",
        "slug": "fan-out-packaging",
        "overview": "Fan-out packaging redistributes die I/O to a larger area using RDL on a reconstituted wafer. It enables thin packages, heterogeneous integration, and system-in-package solutions without interposers.",
        "content_beginner": """Fan-out packaging spreads connections beyond the die edge for more I/O.

**The Problem:**
- Die shrinks but needs same/more I/O
- Traditional packages have size limits
- Need thin packages for mobile

**Fan-Out Solution:**
1. Place dies on carrier (face down)
2. Mold compound around dies
3. Remove carrier
4. Build wiring layers (RDL) over dies
5. Add solder balls

**Benefits:**
- Thinner than flip chip packages
- More I/O without bigger die
- Can combine multiple dies
- Good for mobile devices""",
        "content_advanced": """Fan-out has evolved from single-die to complex multi-die integration.

**Fan-Out Variants:**
| Type | Density | RDL | Application |
|------|---------|-----|-------------|
| eWLB | Low | 2L | Mobile |
| FOWLP | Medium | 3-4L | AP, RF |
| InFO | High | 4-6L | Apple |
| SWIFT | High | 6-8L | HPC |

**Key Parameters:**
- Die shift: <±5µm target
- RDL L/S: 2/2µm leading edge
- Package thickness: <0.4mm
- Warpage control critical

**Integration Options:**
- Side-by-side dies
- Passive integration
- Antenna in package (AiP)
- InFO_PoP (memory on logic)""",
        "diagrams": [],
        "equations": [
            {"latex": "I/O\\ density = \\frac{N_{balls}}{Package\\ area}", "description": "I/O density"},
            {"latex": "Fan-out\\ ratio = \\frac{Package\\ area}{Die\\ area}", "description": "Fan-out ratio"}
        ],
        "manufacturing_challenges": ["Die shift control", "Warpage", "RDL yield", "Mold compound selection"],
        "applications": ["Mobile processors", "RF modules", "Baseband", "IoT", "Automotive"],
        "advantages": ["Thin package", "Low cost vs interposer", "Heterogeneous integration", "Good thermal"],
        "limitations": ["Die shift", "Line/space limits", "Warpage", "Multi-die complexity"],
        "related_topics": ["topic_cowos", "topic_rdl", "topic_wafer_level"],
        "references": [],
        "difficulty": "intermediate",
        "author": "system",
        "views": 0
    },
    {
        "topic_id": "topic_tsv",
        "category_id": "cat_packaging",
        "title": "Through-Silicon Via (TSV)",
        "slug": "through-silicon-via",
        "overview": "TSVs are vertical electrical connections passing through silicon dies or interposers. They enable 3D stacking and 2.5D integration with short interconnects and high bandwidth between dies.",
        "content_beginner": """TSVs are tiny holes through silicon filled with metal to connect stacked chips.

**Why TSVs?**
- Connect stacked dies vertically
- Much shorter than going around edges
- Higher bandwidth possible
- Enables 3D chip stacking

**How TSVs are Made:**
1. Etch deep holes through silicon
2. Insulate the sidewalls
3. Fill with copper
4. Thin the wafer from back
5. TSVs now exposed for connection

**Where They're Used:**
- HBM memory stacks
- CMOS image sensors
- 2.5D interposers
- 3D integrated circuits""",
        "content_advanced": """TSV technology varies by diameter, aspect ratio, and integration point.

**TSV Types:**
| Type | Diameter | Aspect Ratio | Application |
|------|----------|--------------|-------------|
| Via-first | 1-2µm | 5-10:1 | Advanced logic |
| Via-middle | 4-10µm | 8-15:1 | Interposers |
| Via-last | 20-50µm | 5-8:1 | Memory |

**Key Parameters:**
- TSV pitch: 10-100µm
- Copper fill: Electroplating
- Liner: SiO2 + barrier
- Keep-out zone: 5-20µm

**Integration Challenges:**
- Stress from Cu/Si CTE mismatch
- Keep-out zone impact on density
- Wafer thinning and handling
- Electrical characterization""",
        "diagrams": [],
        "equations": [
            {"latex": "R_{TSV} = \\frac{\\rho L}{\\pi r^2}", "description": "TSV resistance"},
            {"latex": "C_{TSV} = \\frac{2\\pi \\epsilon L}{\\ln(r_o/r_i)}", "description": "TSV capacitance"}
        ],
        "manufacturing_challenges": ["High aspect ratio etch", "Void-free fill", "Wafer handling", "Stress management"],
        "applications": ["HBM", "Image sensors", "Interposers", "3D ICs", "MEMS"],
        "advantages": ["Short vertical paths", "High bandwidth", "3D integration", "Small footprint"],
        "limitations": ["Cost", "Keep-out zones", "Stress", "Yield"],
        "related_topics": ["topic_cowos", "topic_hbm", "topic_3d_ic"],
        "references": [],
        "difficulty": "intermediate",
        "author": "system",
        "views": 0
    },
    # ==================== MORE DESIGN/EDA ====================
    {
        "topic_id": "topic_logic_synthesis",
        "category_id": "cat_design",
        "title": "Logic Synthesis",
        "slug": "logic-synthesis",
        "overview": "Logic synthesis transforms RTL descriptions into optimized gate-level netlists using technology libraries. It balances area, timing, and power while meeting design constraints.",
        "content_beginner": """Logic synthesis converts your design description into actual gates.

**The Process:**
1. Read RTL code (Verilog/VHDL)
2. Understand the logic behavior
3. Map to library gates
4. Optimize for speed, area, power

**What the Tool Does:**
- Converts if/case to MUX/logic
- Maps to AND, OR, NOT gates
- Optimizes gate count
- Meets timing requirements

**Key Outputs:**
- Gate-level netlist
- Timing reports
- Area estimates
- Power estimates""",
        "content_advanced": """Modern synthesis employs sophisticated algorithms for multi-objective optimization.

**Synthesis Flow:**
| Stage | Function | Tools |
|-------|----------|-------|
| Elaboration | Parse RTL | Frontend |
| Generic opt | Technology-independent | Synth |
| Mapping | Library binding | Synth |
| Incremental | Refinement | Synth |

**Optimization Techniques:**
- Restructuring (factoring, balancing)
- Retiming (register movement)
- Logic duplication
- Resource sharing
- Clock gating insertion

**Constraints (SDC):**
- Clock definitions
- Input/output delays
- False/multi-cycle paths
- Max capacitance/transition""",
        "diagrams": [],
        "equations": [
            {"latex": "Slack = Required - Arrival", "description": "Timing slack"},
            {"latex": "WNS = min(Slack)", "description": "Worst negative slack"}
        ],
        "manufacturing_challenges": [],
        "applications": ["ASIC design", "FPGA design", "SoC development"],
        "advantages": ["Automation", "Optimization", "Design exploration", "Constraint-driven"],
        "limitations": ["QoR depends on constraints", "Runtime for large designs", "Manual guidance needed"],
        "related_topics": ["topic_rtl_design", "topic_physical_design", "topic_timing_analysis"],
        "references": [],
        "difficulty": "intermediate",
        "author": "system",
        "views": 0
    },
    {
        "topic_id": "topic_dft",
        "category_id": "cat_design",
        "title": "Design for Test (DFT)",
        "slug": "design-for-test",
        "overview": "DFT adds testability features to chip designs including scan chains, BIST, and boundary scan. These structures enable high fault coverage during manufacturing test while minimizing test time and cost.",
        "content_beginner": """DFT makes chips testable - because you can't probe billions of transistors!

**The Problem:**
- Modern chips have billions of transistors
- Can't test each one directly
- Need to find defective chips before shipping

**DFT Solutions:**

**Scan Chains:**
- Convert flip-flops to scannable
- Shift test patterns in
- Capture results
- Shift results out

**BIST (Built-In Self-Test):**
- Chip tests itself
- Logic BIST for random logic
- Memory BIST for RAM/ROM

**Why DFT Matters:**
- Finds manufacturing defects
- Enables high test coverage
- Reduces test time and cost""",
        "content_advanced": """DFT architecture significantly impacts area, power, and test economics.

**DFT Metrics:**
| Metric | Target | Impact |
|--------|--------|--------|
| Fault coverage | >98% | Quality |
| Test time | <1s | Cost |
| DFT area | <5% | Overhead |
| Pattern count | <100K | Memory |

**Advanced DFT:**
- Compression (EDT, DFTMAX)
- IEEE 1500 wrapper
- Hierarchical DFT
- Adaptive test
- In-system test

**ATPG Coverage:**
- Stuck-at faults
- Transition faults
- Path delay faults
- IDDQ testing""",
        "diagrams": [],
        "equations": [
            {"latex": "FC = \\frac{Detected + Untestable}{Total}", "description": "Fault coverage"},
            {"latex": "DPPM = (1-FC) \\times Defect\\_Rate", "description": "Defect escape"}
        ],
        "manufacturing_challenges": [],
        "applications": ["Volume production test", "Engineering debug", "In-field diagnosis"],
        "advantages": ["High coverage", "Automated generation", "Cost reduction", "Diagnosis capability"],
        "limitations": ["Area overhead", "Timing impact", "Power during test", "Pattern volume"],
        "related_topics": ["topic_ate", "topic_yield", "topic_physical_design"],
        "references": [],
        "difficulty": "intermediate",
        "author": "system",
        "views": 0
    },
    {
        "topic_id": "topic_verification",
        "category_id": "cat_design",
        "title": "Functional Verification",
        "slug": "functional-verification",
        "overview": "Functional verification ensures designs behave correctly before manufacturing. Modern verification uses simulation, formal methods, emulation, and coverage-driven methodologies like UVM.",
        "content_beginner": """Verification makes sure the chip does what it's supposed to do.

**Why Verification is Hard:**
- Can't test every possible input
- Modern chips are incredibly complex
- Bugs after manufacturing are very expensive

**Verification Methods:**

**Simulation:**
- Run design with test inputs
- Check outputs match expected
- Slow but detailed

**Formal Verification:**
- Mathematical proof of correctness
- Exhaustive but limited scope

**Emulation:**
- Run design on special hardware
- Much faster than simulation
- Used for software development

**Coverage:**
- Track what's been tested
- Find verification gaps""",
        "content_advanced": """Verification consumes 60-70% of design effort for complex SoCs.

**Verification Approaches:**
| Method | Speed | Coverage | Use |
|--------|-------|----------|-----|
| Simulation | 1x | Sample | Unit |
| Formal | N/A | Exhaustive | Protocols |
| Emulation | 1000x | Sample | System |
| FPGA proto | 10000x | Sample | SW dev |

**UVM Methodology:**
- Constrained random testing
- Functional coverage
- Scoreboarding
- Reusable VIP

**Coverage Types:**
- Code coverage (line, branch, FSM)
- Functional coverage (features)
- Assertion coverage
- Cross coverage""",
        "diagrams": [],
        "equations": [
            {"latex": "Confidence = 1 - (1-p)^n", "description": "Bug escape probability"},
            {"latex": "Coverage\\ hole = Expected - Actual", "description": "Coverage gap"}
        ],
        "manufacturing_challenges": [],
        "applications": ["RTL verification", "SoC validation", "IP verification", "Compliance checking"],
        "advantages": ["Find bugs early", "Reduce risk", "Enable confidence", "Reusable infrastructure"],
        "limitations": ["Time consuming", "Never complete", "Environment complexity", "Tool cost"],
        "related_topics": ["topic_rtl_design", "topic_uvm", "topic_formal"],
        "references": [],
        "difficulty": "intermediate",
        "author": "system",
        "views": 0
    },
    {
        "topic_id": "topic_power_analysis",
        "category_id": "cat_design",
        "title": "Power Analysis and Optimization",
        "slug": "power-analysis-optimization",
        "overview": "Power analysis estimates dynamic, leakage, and short-circuit power consumption. Optimization techniques include clock gating, multi-Vth, power gating, and DVFS to meet power budgets.",
        "content_beginner": """Power analysis tells you how much energy your chip will use.

**Why Power Matters:**
- Battery life in mobile devices
- Heat generation in data centers
- Energy costs for operation
- Reliability concerns

**Power Components:**

**Dynamic Power:**
- From switching gates
- Proportional to frequency
- Proportional to voltage squared

**Leakage Power:**
- Always flowing, even when idle
- Gets worse at smaller nodes
- Major concern today

**Optimization Techniques:**
- Clock gating: Turn off unused clocks
- Power gating: Shut down unused blocks
- Multi-Vth: Fast where needed, low-leak elsewhere""",
        "content_advanced": """Power optimization spans architecture to physical implementation.

**Power Breakdown (typical SoC):**
| Component | Dynamic | Leakage |
|-----------|---------|---------|
| Logic | 40-50% | 30-40% |
| Clock | 30-40% | - |
| Memory | 15-20% | 40-50% |
| I/O | 5-10% | 5-10% |

**Optimization Techniques:**
- Clock gating (30-50% dynamic reduction)
- Multi-Vth (50% leakage reduction)
- Power gating (>90% leakage reduction)
- DVFS (voltage scaling)
- Body biasing
- Operand isolation

**Power Intent (UPF/CPF):**
- Power domains
- Level shifters
- Isolation cells
- Retention registers""",
        "diagrams": [],
        "equations": [
            {"latex": "P_{dyn} = \\alpha C V^2 f", "description": "Dynamic power"},
            {"latex": "P_{leak} = I_0 e^{-qV_{th}/nkT}", "description": "Leakage power"}
        ],
        "manufacturing_challenges": [],
        "applications": ["Mobile SoCs", "Data center chips", "IoT devices", "Wearables"],
        "advantages": ["Predictive analysis", "Guided optimization", "Power budgeting"],
        "limitations": ["Accuracy depends on activity", "Complex multi-domain analysis", "Runtime"],
        "related_topics": ["topic_cmos", "topic_physical_design", "topic_low_power"],
        "references": [],
        "difficulty": "intermediate",
        "author": "system",
        "views": 0
    },
    # ==================== MORE NODES ====================
    {
        "topic_id": "topic_3nm",
        "category_id": "cat_nodes",
        "title": "3nm Process Technology",
        "slug": "3nm-process-technology",
        "overview": "3nm represents the current leading edge with FinFET (TSMC N3) or GAA (Samsung 3GAE) transistors. It offers 10-15% performance improvement or 25-30% power reduction over 5nm.",
        "content_beginner": """3nm is one of the most advanced chip manufacturing processes available today.

**What Does 3nm Mean?**
- NOT the actual transistor size
- Marketing name for a generation
- Real features are larger than 3nm
- Measures manufacturing capability

**Who Makes 3nm Chips?**
- TSMC (N3, N3E, N3P)
- Samsung (3GAE, 3GAP)
- Intel catching up with Intel 3

**Where It's Used:**
- Apple A17 Pro, M3 chips
- High-end smartphones
- Advanced AI chips
- Next-gen laptops""",
        "content_advanced": """3nm implementations vary significantly between manufacturers.

**3nm Comparison:**
| Metric | TSMC N3E | Samsung 3GAE | Intel 3 |
|--------|----------|--------------|---------|
| Transistor | FinFET | GAA | FinFET |
| Density | 60MT/mm² | 50MT/mm² | 60MT/mm² |
| Metal pitch | 21nm | 23nm | 24nm |
| Gate pitch | 48nm | 48nm | 50nm |

**Key Improvements over 5nm:**
- 10-15% speed at same power
- 25-30% power at same speed
- 30% area reduction
- Higher transistor density

**Manufacturing Challenges:**
- EUV layers: 20+ (vs 15 at 5nm)
- Edge placement error
- Pattern fidelity
- Yield ramp""",
        "diagrams": [],
        "equations": [
            {"latex": "Density = \\frac{Transistors}{Area}", "description": "Transistor density"},
            {"latex": "PPA = Performance \\times Power \\times Area", "description": "PPA metric"}
        ],
        "manufacturing_challenges": ["EUV intensity", "Pattern variability", "Yield", "Cost per wafer"],
        "applications": ["Mobile SoCs", "HPC", "AI accelerators", "Client CPUs"],
        "advantages": ["Best PPA", "High density", "Production ready"],
        "limitations": ["Very high cost", "Long design cycle", "Limited capacity"],
        "related_topics": ["topic_2nm", "topic_finfet", "topic_gaafet"],
        "references": [],
        "difficulty": "intermediate",
        "author": "system",
        "views": 0
    },
    {
        "topic_id": "topic_2nm",
        "category_id": "cat_nodes",
        "title": "2nm Process Technology",
        "slug": "2nm-process-technology",
        "overview": "2nm marks the industry transition to GAA/nanosheet transistors for all major foundries. Expected in 2025-2026, it promises 25% better performance or 40% power reduction versus 3nm.",
        "content_beginner": """2nm is the next major chip manufacturing milestone, coming soon.

**Major Changes at 2nm:**
- New transistor type: Gate-All-Around (GAA)
- Better control over electron flow
- Continuation of Moore's Law
- All major fabs switching to GAA

**Who's Working on 2nm:**
- TSMC N2 (2025)
- Intel 20A (2024) - already GAA
- Samsung SF2 (2025-2026)

**Expected Benefits:**
- 25% faster chips
- 40% less power
- Smaller die sizes
- More transistors per chip""",
        "content_advanced": """2nm represents the industry-wide GAA transition point.

**2nm Technology Landscape:**
| Foundry | Node | Transistor | Timeline |
|---------|------|------------|----------|
| TSMC | N2 | Nanosheet | 2H 2025 |
| Intel | 20A | RibbonFET | 2024 |
| Samsung | SF2 | MBCFET | 2025-26 |

**Expected Specifications:**
- Metal pitch: 20-21nm
- Gate pitch: 45-48nm
- SRAM cell: ~0.012µm²
- EUV layers: 25-30

**GAA Advantages:**
- Better electrostatic control
- Steeper subthreshold slope
- Lower leakage
- Width modulation flexibility

**Challenges:**
- Inner spacer formation
- Work function metal fill
- Sheet-to-sheet variability
- Cost increase""",
        "diagrams": [],
        "equations": [
            {"latex": "I_{drive} \\propto W_{eff} \\times N_{sheets}", "description": "Drive current scaling"},
            {"latex": "SS = \\frac{dV_g}{d(\\log I_d)}", "description": "Subthreshold slope"}
        ],
        "manufacturing_challenges": ["GAA yield", "Nanosheet formation", "Inner spacer", "Cost structure"],
        "applications": ["Next-gen mobile", "HPC", "AI", "Client CPUs"],
        "advantages": ["Better control", "Lower leakage", "Continued scaling"],
        "limitations": ["High cost", "Manufacturing complexity", "Design challenges"],
        "related_topics": ["topic_gaafet", "topic_3nm", "topic_intel_18a"],
        "references": [],
        "difficulty": "advanced",
        "author": "system",
        "views": 0
    },
    # ==================== RELIABILITY/YIELD ====================
    {
        "topic_id": "topic_yield_management",
        "category_id": "cat_reliability",
        "title": "Yield Management",
        "slug": "yield-management",
        "overview": "Yield management optimizes the percentage of good dies per wafer through defect reduction, process control, and systematic analysis. It directly impacts manufacturing cost and profitability.",
        "content_beginner": """Yield is the percentage of working chips on each wafer - higher is better!

**Why Yield Matters:**
- Each wafer costs thousands of dollars
- Low yield = expensive chips
- High yield = competitive advantage
- Critical for profitability

**What Kills Yield:**
- Particles (dust, contamination)
- Process variations
- Design weaknesses
- Equipment problems
- Random defects

**Yield Improvement:**
- Find defects with inspection
- Trace causes with analysis
- Fix problems at source
- Monitor continuously""",
        "content_advanced": """Yield modeling combines systematic and random defect components.

**Yield Models:**
| Model | Formula | Application |
|-------|---------|-------------|
| Poisson | Y = e^(-AD) | Random defects |
| Murphy | Y = ((1-e^(-AD))/AD)² | Clustered |
| Seeds | Y = (1+AD/α)^(-α) | Negative binomial |

**Yield Components:**
- Line yield: Process issues
- Die yield: Defect density
- Probe yield: Electrical test
- Package yield: Assembly
- Final yield: All combined

**Systematic Yield Loss:**
- Design marginality
- Process centering
- Equipment matching
- Material variation

**Random Yield Loss:**
- Defect density (D0)
- Critical area
- Killer defect ratio""",
        "diagrams": [],
        "equations": [
            {"latex": "Y = e^{-A \\times D_0}", "description": "Poisson yield model"},
            {"latex": "Cost/good\\_die = \\frac{Wafer\\_cost}{Dies \\times Y}", "description": "Die cost"}
        ],
        "manufacturing_challenges": ["Defect reduction", "Process control", "Root cause analysis", "Prediction"],
        "applications": ["Fab operations", "Cost modeling", "Process development", "Product ramp"],
        "advantages": ["Cost reduction", "Quality improvement", "Competitive advantage"],
        "limitations": ["Complex analysis", "Data requirements", "Continuous effort"],
        "related_topics": ["topic_wafer_inspection", "topic_metrology", "topic_ate"],
        "references": [],
        "difficulty": "intermediate",
        "author": "system",
        "views": 0
    },
    {
        "topic_id": "topic_electromigration",
        "category_id": "cat_reliability",
        "title": "Electromigration",
        "slug": "electromigration",
        "overview": "Electromigration is the transport of metal atoms by high current density, causing voids and hillocks in interconnects. It's a critical reliability concern addressed through design rules and material engineering.",
        "content_beginner": """Electromigration is when electric current slowly moves metal atoms around.

**What Happens:**
- High current pushes metal atoms
- Atoms move in current direction
- Creates voids (gaps) in wires
- Can cause wire to break open

**Why It's a Problem:**
- Chips run for years
- Small currents add up over time
- Wires can fail after years of use
- Must design to prevent it

**Prevention:**
- Limit current in each wire
- Use better metal barriers
- Design rules from foundry
- Avoid current hotspots""",
        "content_advanced": """Electromigration limits interconnect current density and reliability.

**Black's Equation:**
MTTF = A × j^(-n) × exp(Ea/kT)
- A: Process-dependent constant
- j: Current density
- n: Current exponent (~2)
- Ea: Activation energy

**EM Parameters by Metal:**
| Metal | Ea (eV) | Jmax (MA/cm²) |
|-------|---------|---------------|
| Al | 0.5-0.7 | 0.5-1 |
| Cu | 0.8-1.0 | 1-2 |
| Co | 1.0-1.2 | 2-3 |

**Design Considerations:**
- Wire width for current
- Via count and redundancy
- Metal slotting rules
- Reservoirs at line ends

**Advanced Solutions:**
- Cobalt cap layers
- Ruthenium barrier
- SAV (selective atomic layer via)
- Via pillar designs""",
        "diagrams": [],
        "equations": [
            {"latex": "MTTF = A j^{-n} e^{E_a/kT}", "description": "Black's equation"},
            {"latex": "J_{crit} = \\frac{1}{\\rho \\Omega} \\nabla \\sigma", "description": "Critical current"}
        ],
        "manufacturing_challenges": ["Current density limits", "Barrier effectiveness", "Testing acceleration"],
        "applications": ["Interconnect design", "Reliability qualification", "Lifetime prediction"],
        "advantages": ["Predictable with models", "Design rules available", "Improvable with materials"],
        "limitations": ["Limits wire scaling", "Testing time", "Design constraints"],
        "related_topics": ["topic_copper_interconnects", "topic_reliability", "topic_beol"],
        "references": [],
        "difficulty": "intermediate",
        "author": "system",
        "views": 0
    }
]


def get_extended_topics_part2():
    """Return extended topics part 2 for encyclopedia expansion"""
    return EXTENDED_TOPICS_PART2
