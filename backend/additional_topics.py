"""
Additional Encyclopedia Topics - Memory, Testing, Design/EDA, and expanded coverage
Targets 100+ total topics for production-ready encyclopedia
"""

ADDITIONAL_TOPICS = [
    # ==================== MEMORY TECHNOLOGIES ====================
    {
        "topic_id": "topic_dram",
        "category_id": "cat_memory",
        "title": "DRAM Technology",
        "slug": "dram-technology",
        "overview": "Dynamic Random Access Memory uses capacitors to store data, requiring periodic refresh. DRAM is the dominant main memory technology with DDR5 and LPDDR5X representing the latest standards.",
        "content_beginner": """DRAM is the main memory in your computer and phone. It stores data temporarily while programs run.

**How It Works:**
- Each memory cell is a tiny capacitor (stores charge)
- Charge represents 1 or 0 (data bit)
- Capacitors leak, so data must be refreshed regularly
- That's why it's called "Dynamic" RAM

**Types of DRAM:**
- **DDR5**: Desktop/laptop computers (up to 6400 MT/s)
- **LPDDR5X**: Mobile phones (up to 8533 MT/s)
- **HBM3**: AI accelerators, graphics (819 GB/s per stack)
- **GDDR6X**: Gaming graphics cards

**Why DRAM is Everywhere:**
- High density (lots of storage per chip)
- Relatively low cost per bit
- Good balance of speed and capacity""",
        "content_advanced": """DRAM technology continues to scale with advanced cell architectures and high-bandwidth interfaces.

**Cell Architecture Evolution:**
| Generation | Cell Type | Capacitance | Vth Challenge |
|------------|-----------|-------------|---------------|
| DDR4 | 6F² buried | ~10fF | Moderate |
| DDR5 | 4F² | ~7fF | High |
| Future | <4F² | ~5fF | Extreme |

**DDR5 Key Specifications:**
- Data rate: 4800-8800 MT/s
- Prefetch: 16n (vs 8n DDR4)
- Bank groups: 8 (vs 4)
- On-die ECC: Required
- VDD: 1.1V (vs 1.2V DDR4)
- Channel: x8 sub-channels

**High-Bandwidth Memory (HBM3):**
- Stack: 8-12 dies + base logic
- TSV pitch: 36-40µm
- Bandwidth: 819 GB/s (12-hi stack)
- Interface: 1024-bit wide
- Power: <2.5W/GB/s

**Scaling Challenges:**
- Capacitor aspect ratio >60:1
- High-K dielectrics (ZrO2, HfO2)
- Low-leakage access transistors
- Refresh rate vs temperature
- Write margin with low VDD

**Advanced Cell Concepts:**
- Buried word line (BWL)
- Saddle fin transistor
- Ruthenium electrodes
- IGZO-based transistors (low leakage)""",
        "diagrams": [],
        "equations": [
            {"latex": "Q = C \\times V", "description": "Charge stored in capacitor"},
            {"latex": "BW = DataRate \\times BusWidth / 8", "description": "Memory bandwidth"}
        ],
        "manufacturing_challenges": ["Capacitor aspect ratio scaling", "High-K dielectric integration", "TSV for HBM stacking", "Refresh power scaling", "Access transistor leakage"],
        "applications": ["Main memory (computers)", "Mobile devices", "AI accelerators", "Graphics cards", "Data centers"],
        "advantages": ["High density", "Cost-effective", "Proven scalability", "Wide ecosystem"],
        "limitations": ["Requires refresh", "Volatile (loses data when powered off)", "Capacitor scaling limits", "Power for refresh"],
        "related_topics": ["topic_hbm", "topic_nand", "topic_sram"],
        "references": [
            {"title": "DDR5 JEDEC Standard", "url": "https://www.jedec.org/", "source": "JEDEC"},
            {"title": "Samsung DRAM Technology", "url": "https://semiconductor.samsung.com/", "source": "Samsung"}
        ],
        "difficulty": "intermediate",
        "author": "system",
        "views": 0
    },
    {
        "topic_id": "topic_nand",
        "category_id": "cat_memory",
        "title": "NAND Flash Memory",
        "slug": "nand-flash-memory",
        "overview": "NAND flash is the dominant non-volatile memory for storage, using 3D vertical stacking to achieve over 200 layers. It stores data by trapping charge in floating gates or charge trap layers.",
        "content_beginner": """NAND flash is what stores data in your phone, SSD, and USB drives. Unlike DRAM, it keeps data even when power is off.

**How It Works:**
- Electrons are trapped in a special layer
- Trapped electrons = stored data
- Data stays without power (non-volatile)
- Reading checks if electrons are present

**3D NAND Revolution:**
- Instead of shrinking cells horizontally
- Stack cells vertically (like a skyscraper)
- Modern NAND has 200+ layers
- Each layer adds more storage

**Where You Find It:**
- Solid State Drives (SSDs)
- Smartphones and tablets
- USB flash drives
- Memory cards

**Key Terms:**
- SLC: 1 bit per cell (fastest, most durable)
- TLC: 3 bits per cell (good balance)
- QLC: 4 bits per cell (highest density)""",
        "content_advanced": """3D NAND has become the dominant architecture, with manufacturers racing to increase layer counts.

**3D NAND Architecture:**
| Manufacturer | Max Layers | Cell Type | Channel |
|-------------|------------|-----------|---------|
| Samsung | 236L | V-NAND | Macaroni |
| SK Hynix | 238L | CTF | Cylindrical |
| Micron | 232L | RG | Circular |
| YMTC | 232L | Xtacking | Bonded |

**Cell Technology:**
- Charge Trap Flash (CTF): Si3N4 storage layer
- Floating Gate (FG): Polysilicon storage
- Replacement Gate (RG): Metal gate electrode
- Word line: Tungsten or molybdenum

**Key Parameters:**
- Program time: ~500µs (TLC page)
- Read time: ~50µs
- Erase time: ~3ms (block)
- Endurance: 1000-3000 P/E cycles (TLC)
- Retention: 10 years (specified)

**Scaling Challenges:**
- Cell-to-cell interference
- String current degradation
- Word line resistance
- Etch profile control
- Stair-step patterning

**Advanced Concepts:**
- PUC (Peripheral Under Cell): Logic below array
- String stacking: Multiple strings bonded
- CMOS under array: Better utilization
- Xtacking: Separate logic wafer bonding""",
        "diagrams": [],
        "equations": [
            {"latex": "V_{th} = V_{th0} + \\Delta V_{trap}", "description": "Threshold voltage shift from trapped charge"},
            {"latex": "Capacity = Layers \\times Dies \\times Density", "description": "Total NAND capacity"}
        ],
        "manufacturing_challenges": ["200+ layer etch uniformity", "Channel hole aspect ratio", "Word line fill", "Stair-step patterning", "Die bonding alignment"],
        "applications": ["Consumer SSDs", "Enterprise storage", "Mobile devices", "Data centers", "Automotive"],
        "advantages": ["Non-volatile", "High density", "No moving parts", "Low power (vs HDD)", "Fast random access"],
        "limitations": ["Limited endurance (P/E cycles)", "Write amplification", "Bit errors require ECC", "Performance degrades with use"],
        "related_topics": ["topic_dram", "topic_emerging_memory", "topic_storage_controller"],
        "references": [
            {"title": "3D NAND Technology", "url": "https://www.micron.com/", "source": "Micron"},
            {"title": "Flash Memory Summit", "url": "https://flashmemorysummit.com/", "source": "FMS"}
        ],
        "difficulty": "intermediate",
        "author": "system",
        "views": 0
    },
    {
        "topic_id": "topic_sram",
        "category_id": "cat_memory",
        "title": "SRAM Technology",
        "slug": "sram-technology",
        "overview": "Static RAM uses cross-coupled inverters to store data without refresh, providing the fastest on-chip memory for caches. SRAM density is a key metric for process node competitiveness.",
        "content_beginner": """SRAM is the fastest type of memory, used for caches inside processors. Unlike DRAM, it doesn't need refresh.

**How It Works:**
- Uses 6 transistors per bit (6T cell)
- Two inverters hold data in a loop
- Data is stable without refresh
- Very fast access (nanoseconds)

**Where It's Used:**
- CPU L1, L2, L3 caches
- GPU caches
- Network chip buffers
- FPGA block RAM

**Why It's Important:**
- Cache speed determines processor performance
- SRAM density shows manufacturing capability
- 6T cell size = process node benchmark

**Trade-offs vs DRAM:**
- Much faster than DRAM
- But much larger (6T vs 1T1C)
- More expensive per bit
- Used for small, fast storage""",
        "content_advanced": """SRAM is critical for on-chip memory and serves as a key benchmark for process nodes.

**6T SRAM Cell Design:**
- 2 PMOS pull-up transistors
- 2 NMOS pull-down transistors
- 2 NMOS access transistors
- Cell stability: SNM (Static Noise Margin)

**SRAM Scaling Metrics:**
| Node | Cell Size | Density | Notes |
|------|-----------|---------|-------|
| 7nm | ~0.027µm² | ~37Mb/mm² | FinFET |
| 5nm | ~0.021µm² | ~48Mb/mm² | FinFET |
| 3nm | ~0.016µm² | ~62Mb/mm² | FinFET/GAA |
| 2nm | ~0.012µm² | ~83Mb/mm² | GAA |

**Design Parameters:**
- Read SNM: >150mV
- Write margin: >100mV
- Cell ratio (β): ~1.5-2.0
- Pull-up ratio (γ): ~1.5
- Read current: >10µA
- Leakage: <1nA/cell

**Advanced SRAM Variants:**
- 8T SRAM: Separate read port
- 10T SRAM: Dual-port
- Asymmetric cell: Area optimization
- Negative bit-line: Improved write

**Assist Techniques:**
- Word line underdrive: Stability
- Negative bit-line: Write assist
- Body biasing: Vth adjustment
- Dual-rail: Power optimization""",
        "diagrams": [],
        "equations": [
            {"latex": "SNM = \\frac{V_{DD}}{2} \\times \\left(1 - \\frac{1}{\\beta}\\right)", "description": "Static noise margin approximation"},
            {"latex": "Cell\\_Area = W_n \\times L_{gate} \\times 6", "description": "6T cell area scaling"}
        ],
        "manufacturing_challenges": ["Cell stability at low voltage", "Variability control", "Leakage management", "Read/write margins", "Process corners"],
        "applications": ["Processor caches", "GPU shared memory", "Network buffers", "FPGA", "Embedded memory"],
        "advantages": ["Fastest on-chip memory", "No refresh needed", "Simple control", "Random access"],
        "limitations": ["Large cell size (6T)", "High cost per bit", "Leakage power", "Limited density"],
        "related_topics": ["topic_dram", "topic_cache_design", "topic_power_management"],
        "references": [
            {"title": "SRAM Design", "url": "https://www.synopsys.com/", "source": "Synopsys"},
            {"title": "Advanced SRAM", "url": "https://www.arm.com/", "source": "ARM"}
        ],
        "difficulty": "intermediate",
        "author": "system",
        "views": 0
    },
    {
        "topic_id": "topic_emerging_memory",
        "category_id": "cat_memory",
        "title": "Emerging Memory Technologies",
        "slug": "emerging-memory-technologies",
        "overview": "Next-generation memories including MRAM, ReRAM, and PCM offer unique combinations of speed, density, and non-volatility to fill the gap between DRAM and NAND.",
        "content_beginner": """Scientists are developing new types of memory to combine the best features of existing technologies.

**The Memory Gap Problem:**
- SRAM: Very fast, but expensive and low density
- DRAM: Good speed, but needs refresh
- NAND: High density, but slow
- New memories try to fill these gaps

**Emerging Technologies:**

**MRAM (Magnetic RAM):**
- Uses magnets to store data
- Fast like SRAM, non-volatile like NAND
- Used in some chips already

**ReRAM (Resistive RAM):**
- Changes resistance to store data
- Simple structure, high density potential
- Good for AI applications

**PCM (Phase Change Memory):**
- Uses material phase changes
- Intel's Optane used this technology
- Very high endurance""",
        "content_advanced": """Emerging non-volatile memories (eNVMs) address the memory hierarchy gap with diverse mechanisms.

**MRAM (STT-MRAM):**
- Mechanism: Spin-transfer torque switching
- Write time: 5-20ns
- Endurance: >10^15 cycles
- Retention: 10 years @ 85°C
- Applications: Embedded MRAM, L4 cache replacement

**SOT-MRAM (Next-gen):**
- Spin-orbit torque switching
- Faster write (<1ns)
- Lower write energy
- Separate read/write paths

**ReRAM/RRAM:**
- Mechanism: Filament formation/dissolution
- Materials: HfO2, TaOx metal oxides
- Write time: ~10ns
- Endurance: 10^6-10^12 cycles
- Applications: In-memory computing, CIM

**PCM (Phase Change Memory):**
- Materials: GST (Ge2Sb2Te5)
- Mechanism: Amorphous/crystalline transition
- Multi-level: 2-4 bits/cell
- Applications: Storage class memory

**Comparison Matrix:**
| Technology | Speed | Endurance | Density | Maturity |
|------------|-------|-----------|---------|----------|
| STT-MRAM | 10ns | >10^15 | Medium | Production |
| ReRAM | 10ns | 10^6-10^9 | High | Development |
| PCM | 100ns | 10^9 | High | Limited |
| FeRAM | 50ns | 10^15 | Low | Niche |""",
        "diagrams": [],
        "equations": [
            {"latex": "R_{on} << R_{off}", "description": "Resistance states in ReRAM"},
            {"latex": "I_c = \\frac{2e}{\\hbar} \\alpha M_s V", "description": "STT-MRAM critical current"}
        ],
        "manufacturing_challenges": ["BEOL thermal budget", "Variability control", "Selector device integration", "Endurance vs speed trade-off", "Cost competitiveness"],
        "applications": ["Embedded NVM", "IoT devices", "AI accelerators", "Storage class memory", "Automotive"],
        "advantages": ["Non-volatile + fast", "Low power", "New computing paradigms", "Fill memory gap"],
        "limitations": ["Endurance limits (some types)", "Cost vs established memory", "Variability", "Ecosystem immaturity"],
        "related_topics": ["topic_dram", "topic_nand", "topic_neuromorphic"],
        "references": [
            {"title": "Emerging Memory Technologies", "url": "https://www.imec-int.com/", "source": "imec"},
            {"title": "MRAM Technology", "url": "https://www.everspin.com/", "source": "Everspin"}
        ],
        "difficulty": "advanced",
        "author": "system",
        "views": 0
    },
    # ==================== TESTING & METROLOGY ====================
    {
        "topic_id": "topic_wafer_inspection",
        "category_id": "cat_testing",
        "title": "Wafer Inspection Systems",
        "slug": "wafer-inspection-systems",
        "overview": "Wafer inspection uses optical and e-beam systems to detect defects during manufacturing. Advanced inspection is critical for yield learning and process control at sub-10nm nodes.",
        "content_beginner": """Wafer inspection is like quality control for chip manufacturing. Special machines look for tiny defects that could ruin chips.

**Why Inspection Matters:**
- A single speck of dust can kill a chip
- Defects must be caught early
- Inspection guides process improvements
- Critical for high yield

**Types of Inspection:**

**Optical (Light-based):**
- Shines bright light on wafer
- Detects particles and pattern defects
- Very fast (many wafers per hour)
- Limited by light wavelength

**E-beam (Electron-based):**
- Uses electrons instead of light
- Can see much smaller defects
- Much slower than optical
- Used for critical layers

**When to Inspect:**
- After lithography (pattern defects)
- After etch (profile issues)
- After deposition (particles)
- After CMP (scratches)""",
        "content_advanced": """Advanced inspection combines multiple technologies for comprehensive defect detection.

**Optical Inspection Platforms:**
| System | Wavelength | Sensitivity | Throughput |
|--------|------------|-------------|------------|
| Broadband | 250-800nm | ~30nm DOI | 100+ wph |
| DUV | 193nm | ~20nm | 50+ wph |
| Multi-beam | Multiple | ~15nm | Variable |

**E-beam Inspection:**
- Landing energy: 0.5-5keV
- Beam current: 1-100nA
- Resolution: <5nm
- Throughput: <5 wph (full wafer)
- Multi-beam systems: 9-100 beams

**Defect Types:**
- Particles: Contamination, residues
- Pattern: Bridging, opens, CD variation
- Film: Thickness, voids, delamination
- Electrical: Shorts, opens, leakage

**Inspection Strategy:**
- Inline: 100% wafer sampling
- Development: Dense sampling, full wafer
- Production: Statistical sampling
- Excursion: Triggered full inspection

**Advanced Techniques:**
- Die-to-die comparison
- Die-to-database comparison
- Defect source analysis (DSA)
- Systematic defect detection
- Machine learning classification""",
        "diagrams": [],
        "equations": [
            {"latex": "DOI = k \\times \\lambda / NA", "description": "Defect of interest (DOI) sensitivity"},
            {"latex": "Throughput \\propto \\frac{1}{Resolution^2}", "description": "Throughput vs resolution trade-off"}
        ],
        "manufacturing_challenges": ["Nuisance defect filtering", "Inspection of 3D structures", "E-beam charging", "Throughput vs sensitivity", "Big data management"],
        "applications": ["Process development", "Yield ramp", "Production monitoring", "Failure analysis", "Excursion detection"],
        "advantages": ["Early defect detection", "Process feedback", "Yield improvement", "Cost reduction"],
        "limitations": ["Throughput limits", "Nuisance defects", "3D inspection challenges", "High tool cost"],
        "related_topics": ["topic_metrology", "topic_yield", "topic_failure_analysis"],
        "references": [
            {"title": "Inspection Systems", "url": "https://www.kla.com/", "source": "KLA"},
            {"title": "E-beam Inspection", "url": "https://www.appliedmaterials.com/", "source": "Applied Materials"}
        ],
        "difficulty": "intermediate",
        "author": "system",
        "views": 0
    },
    {
        "topic_id": "topic_metrology",
        "category_id": "cat_testing",
        "title": "Semiconductor Metrology",
        "slug": "semiconductor-metrology",
        "overview": "Metrology measures critical dimensions, film thickness, overlay, and other parameters to ensure process control. Advanced scatterometry and X-ray techniques enable measurement of sub-nm features.",
        "content_beginner": """Metrology is the science of measurement in chip manufacturing. It ensures everything is built to exact specifications.

**What Gets Measured:**

**Critical Dimension (CD):**
- Width of transistor gates
- Line widths and spaces
- Must be within nanometers of target

**Film Thickness:**
- How thick each layer is
- Measured in nanometers or angstroms
- Affects electrical properties

**Overlay:**
- Alignment between layers
- Must be within a few nanometers
- Critical for multi-layer chips

**Measurement Tools:**

**Optical (OCD):**
- Shines light, measures reflection
- Fast and non-destructive
- Works on special test structures

**SEM (Scanning Electron Microscope):**
- Uses electron beam
- Direct imaging of features
- Slower but more flexible

**AFM (Atomic Force Microscope):**
- Tiny probe scans surface
- Measures 3D topography
- Very slow but precise""",
        "content_advanced": """Metrology enables process control for sub-nm precision manufacturing.

**Scatterometry (OCD) Techniques:**
| Method | Wavelength | Capability | TMU |
|--------|------------|------------|-----|
| SE | UV-Vis | CD, height, profile | <0.5nm |
| Mueller Matrix | Broadband | Asymmetry, overlay | <0.3nm |
| X-ray | 0.1nm | Buried features | <0.2nm |

**CD Measurement:**
- CD-SEM: Direct imaging, <0.3nm precision
- OCD: Model-based, <0.5nm TMU
- CD-SAXS: X-ray scattering, buried CD
- AFM: 3D profile, calibration reference

**Overlay Measurement:**
- Target types: Box-in-box, AIM, µDBO
- Precision: <0.5nm 3σ
- On-product (device) vs in-scribe
- Higher-order corrections: inter/intra field

**Film Metrology:**
- Spectroscopic ellipsometry: Thickness, n, k
- XRF: Composition, thickness
- XRR: Density, interface roughness
- SIMS: Dopant profiling

**Advanced Metrology:**
- Hybrid metrology: Combining techniques
- In-line CD-SAXS: Production X-ray
- Reference metrology: TEM, APT
- Virtual metrology: ML-based prediction

**Measurement Uncertainty:**
- Precision: Repeatability
- TMU: Total measurement uncertainty
- Matching: Tool-to-tool correlation
- TIS: Tool-induced shift""",
        "diagrams": [],
        "equations": [
            {"latex": "TMU = \\sqrt{P^2 + A^2 + TIS^2}", "description": "Total measurement uncertainty"},
            {"latex": "OVL = Target - Reference", "description": "Overlay measurement"}
        ],
        "manufacturing_challenges": ["3D structure measurement", "Buried feature access", "Throughput vs precision", "Model accuracy", "Reference metrology"],
        "applications": ["Process control", "APC feedback", "Yield optimization", "R&D characterization", "Quality assurance"],
        "advantages": ["Non-destructive", "Fast feedback", "Statistical process control", "Early detection"],
        "limitations": ["Model dependencies", "Test structure requirements", "Tool matching", "Measurement artifacts"],
        "related_topics": ["topic_wafer_inspection", "topic_overlay", "topic_apc"],
        "references": [
            {"title": "Metrology Solutions", "url": "https://www.kla.com/", "source": "KLA"},
            {"title": "X-ray Metrology", "url": "https://www.bruker.com/", "source": "Bruker"}
        ],
        "difficulty": "intermediate",
        "author": "system",
        "views": 0
    },
    {
        "topic_id": "topic_ate",
        "category_id": "cat_testing",
        "title": "Automatic Test Equipment (ATE)",
        "slug": "automatic-test-equipment",
        "overview": "ATE systems perform high-speed electrical testing of chips at wafer and package levels. Modern ATE combines RF, digital, and analog capabilities for complex SoC testing.",
        "content_beginner": """ATE is the machine that tests if chips work correctly before they're shipped. It checks every function at high speed.

**Testing Stages:**

**Wafer Test (Probe):**
- Tests chips while still on wafer
- Probes touch each die's pads
- Identifies bad dies before packaging
- Saves cost of packaging failures

**Final Test (Package):**
- Tests after chip is packaged
- Full speed and temperature testing
- Ensures quality before shipping

**What Gets Tested:**
- Digital logic (millions of transistors)
- Memory functions
- Analog circuits (amplifiers, ADCs)
- RF/wireless functions
- Power consumption

**Why Testing is Hard:**
- Chips have billions of transistors
- Can't test everything directly
- Must balance cost vs coverage
- Test time = money""",
        "content_advanced": """Modern ATE platforms support mixed-signal, RF, and high-speed digital testing with advanced diagnosis.

**ATE Architecture:**
- Tester resources: Digital, analog, RF, power
- Pin electronics: Per-pin configuration
- Timing: <10ps edge placement accuracy
- Pattern memory: >1Gb per channel
- Data rate: >50Gbps digital

**Test Economics:**
| Metric | Typical Value | Impact |
|--------|---------------|--------|
| Test time | 100ms-10s | Direct cost |
| Test coverage | 95-99% | Quality |
| Yield | 85-99% | Revenue |
| DPPM | <10 | Customer returns |

**Test Methods:**
- Structural: Scan, BIST, JTAG
- Functional: At-speed patterns
- Parametric: DC, leakage, Iddq
- Analog: ADC/DAC, PLL, SerDes
- RF: S-parameters, EVM, spectrum

**Design for Test (DFT):**
- Scan insertion: Sequential to combinational
- BIST: Built-in self test (memory, logic)
- Boundary scan: JTAG testing
- Compression: 10-100x pattern reduction

**Advanced Capabilities:**
- Adaptive test: ML-based test optimization
- Multi-site testing: 32-128 parallel sites
- System-level test: Functional verification
- Failure analysis: Diagnosis to layout""",
        "diagrams": [],
        "equations": [
            {"latex": "Test\\_Cost = \\frac{ATE\\_Cost \\times Test\\_Time}{Sites \\times Utilization}", "description": "Per-die test cost"},
            {"latex": "DPPM = \\frac{Defects}{10^6\\_Units}", "description": "Defective parts per million"}
        ],
        "manufacturing_challenges": ["Test time reduction", "Parallel testing", "Diagnosis capability", "Multi-die testing", "Cost per test"],
        "applications": ["Volume production", "Engineering characterization", "Quality assurance", "Failure analysis", "Reliability screening"],
        "advantages": ["High throughput", "Comprehensive coverage", "Automated operation", "Diagnosis capability"],
        "limitations": ["High capital cost", "Test time vs coverage", "Limited defect types", "DFT requirements"],
        "related_topics": ["topic_dft", "topic_wafer_inspection", "topic_yield"],
        "references": [
            {"title": "ATE Systems", "url": "https://www.teradyne.com/", "source": "Teradyne"},
            {"title": "Test Solutions", "url": "https://www.advantest.com/", "source": "Advantest"}
        ],
        "difficulty": "intermediate",
        "author": "system",
        "views": 0
    },
    # ==================== DESIGN & EDA ====================
    {
        "topic_id": "topic_rtl_design",
        "category_id": "cat_design",
        "title": "RTL Design Flow",
        "slug": "rtl-design-flow",
        "overview": "Register Transfer Level (RTL) design uses hardware description languages to specify digital logic behavior. Modern RTL flows include synthesis, simulation, and formal verification.",
        "content_beginner": """RTL design is how engineers describe what a chip should do using special programming languages.

**What is RTL?**
- Describes chip behavior as data moving between registers
- Uses languages like Verilog or VHDL
- More abstract than drawing transistors
- Enables complex chip design

**The Design Flow:**

1. **Specification**: What should the chip do?
2. **Architecture**: How to organize the design
3. **RTL Coding**: Write in Verilog/VHDL
4. **Simulation**: Does it work correctly?
5. **Synthesis**: Convert to gates
6. **Place & Route**: Physical layout

**Hardware Description Languages:**
- **Verilog**: Most common, C-like syntax
- **VHDL**: Very verbose, Ada-like syntax
- **SystemVerilog**: Modern Verilog extension

**Example (Verilog):**
```
always @(posedge clk)
    if (enable)
        counter <= counter + 1;
```""",
        "content_advanced": """Modern RTL design flows encompass specification through implementation with sophisticated verification.

**Design Abstraction Levels:**
| Level | Abstraction | Tools | Purpose |
|-------|-------------|-------|---------|
| System | Transaction | SystemC | Architecture |
| RTL | Cycle | Verilog/VHDL | Behavior |
| Gate | Logic | Synthesis | Structure |
| Physical | Transistor | P&R | Layout |

**RTL Coding Guidelines:**
- Synchronous design with clock domains
- Reset strategy (sync vs async)
- FSM coding style (one-hot, binary)
- Synthesis-friendly constructs
- Lint rule compliance

**Synthesis Flow:**
1. RTL elaboration: Parse HDL
2. Technology mapping: Library gates
3. Optimization: Area, timing, power
4. Timing constraints: SDC format
5. Netlist generation: Gate-level output

**Verification Methods:**
- Simulation: Direct HDL execution
- Formal: Mathematical proof
- Emulation: FPGA-based acceleration
- UVM: Universal Verification Methodology

**Power Considerations:**
- Clock gating: Disable unused clocks
- Power domains: Multiple VDD islands
- DVFS: Dynamic voltage/frequency
- Retention: State preservation
- UPF/CPF: Power intent specification

**Modern Flows:**
- High-level synthesis: C to RTL
- AI-assisted design: Optimization
- IP integration: Pre-verified blocks
- Continuous integration: CI/CD for RTL""",
        "diagrams": [],
        "equations": [
            {"latex": "T_{clk} \\geq T_{cq} + T_{logic} + T_{setup}", "description": "Timing constraint for registers"},
            {"latex": "Power = \\alpha C V^2 f", "description": "Dynamic power equation"}
        ],
        "manufacturing_challenges": ["Design rule compliance", "Timing closure", "Power optimization", "Verification coverage", "IP integration"],
        "applications": ["ASIC design", "FPGA design", "SoC development", "IP creation", "Processor design"],
        "advantages": ["Abstraction", "Reusability", "Verification", "Portability"],
        "limitations": ["Simulation speed", "Manual optimization needed", "Complex verification", "Learning curve"],
        "related_topics": ["topic_physical_design", "topic_verification", "topic_synthesis"],
        "references": [
            {"title": "RTL Design", "url": "https://www.synopsys.com/", "source": "Synopsys"},
            {"title": "SystemVerilog", "url": "https://www.cadence.com/", "source": "Cadence"}
        ],
        "difficulty": "intermediate",
        "author": "system",
        "views": 0
    },
    {
        "topic_id": "topic_physical_design",
        "category_id": "cat_design",
        "title": "Physical Design Flow",
        "slug": "physical-design-flow",
        "overview": "Physical design transforms gate-level netlists into manufacturable layouts through floorplanning, placement, clock tree synthesis, and routing. It's critical for timing, power, and area optimization.",
        "content_beginner": """Physical design is turning a chip's logic design into an actual layout that can be manufactured.

**The Challenge:**
- Place millions of standard cells
- Connect them with metal wires
- Meet timing requirements
- Minimize power and area

**Key Steps:**

1. **Floorplanning**
   - Decide where major blocks go
   - Place memory, I/O, big logic blocks
   - Create power/ground network plan

2. **Placement**
   - Position standard cells
   - Optimize for wire length
   - Consider timing-critical paths

3. **Clock Tree Synthesis (CTS)**
   - Build clock distribution network
   - Balance delays (low skew)
   - Buffer insertion for fanout

4. **Routing**
   - Connect all the signals
   - Multiple metal layers
   - Avoid violations (shorts, spacing)

5. **Sign-off**
   - Final timing analysis
   - Design rule checking (DRC)
   - Layout vs schematic (LVS)""",
        "content_advanced": """Physical design requires sophisticated optimization for timing closure at advanced nodes.

**Implementation Challenges by Node:**
| Node | Layers | Cell Height | Key Challenge |
|------|--------|-------------|---------------|
| 7nm | 12-14M | 6-7T | Multi-patterning |
| 5nm | 12-14M | 5-6T | BEOL scaling |
| 3nm | 15-17M | 4-5T | Routability |
| 2nm | 16-18M | 4-5T | BSPD integration |

**Floorplanning Considerations:**
- Macro placement: Memory, analog, I/O
- Power domain partitioning
- Blockage definition
- Pin assignment optimization
- Aspect ratio selection

**Placement Optimization:**
- Global: Quadratic/analytical
- Detailed: Legalization, local opt
- Timing-driven: Slack-based weighting
- Congestion-aware: Routing estimation
- Power-aware: Switching activity

**Clock Tree Synthesis:**
- Target skew: <30ps at advanced nodes
- Useful skew: Intentional delay insertion
- OCV derating: On-chip variation
- Mesh clock: Low skew alternative
- Multi-clock domain handling

**Routing Challenges:**
- Wire resistance: RC delay dominant
- Via resistance: Contact degradation
- Crosstalk: SI effects on timing
- DRC: Thousands of rules
- Antenna: Charge accumulation

**Physical Verification:**
- DRC: Design rule checking
- LVS: Layout vs schematic
- ERC: Electrical rule checking
- DFM: Design for manufacturing
- Fill: Metal density balancing""",
        "diagrams": [],
        "equations": [
            {"latex": "Delay = R \\times C", "description": "Interconnect delay"},
            {"latex": "Skew = T_{max} - T_{min}", "description": "Clock skew definition"}
        ],
        "manufacturing_challenges": ["Routing congestion", "IR drop", "Electromigration", "Metal fill", "Via reliability"],
        "applications": ["ASIC implementation", "SoC design", "Memory design", "IP hardening", "Full-chip assembly"],
        "advantages": ["Automated optimization", "Timing closure", "Design convergence", "Manufacturing readiness"],
        "limitations": ["Long runtime", "Tool expertise needed", "Iteration cycles", "Large data volumes"],
        "related_topics": ["topic_rtl_design", "topic_signoff", "topic_dft"],
        "references": [
            {"title": "Place and Route", "url": "https://www.cadence.com/", "source": "Cadence"},
            {"title": "Physical Design", "url": "https://www.synopsys.com/", "source": "Synopsys"}
        ],
        "difficulty": "advanced",
        "author": "system",
        "views": 0
    },
    {
        "topic_id": "topic_timing_analysis",
        "category_id": "cat_design",
        "title": "Static Timing Analysis (STA)",
        "slug": "static-timing-analysis",
        "overview": "STA verifies that all timing paths in a design meet setup and hold requirements without running simulation. It's essential for sign-off at advanced nodes with complex variation modeling.",
        "content_beginner": """Static Timing Analysis checks if signals arrive at the right time everywhere in a chip, without actually simulating the design.

**Why Timing Matters:**
- Data must be stable when clock arrives
- If too slow = setup violation (wrong data captured)
- If too fast = hold violation (data changes too early)

**Key Concepts:**

**Setup Time:**
- Data must arrive before clock edge
- Enough time for flip-flop to capture

**Hold Time:**
- Data must stay stable after clock
- Prevents capturing wrong value

**Path Analysis:**
- Find all paths from register to register
- Calculate total delay through logic
- Compare to clock period

**Why Static Analysis?**
- Don't need test vectors
- Checks ALL paths (billions)
- Much faster than simulation
- Essential for sign-off""",
        "content_advanced": """Modern STA accounts for process variation, on-chip variation, and signaling effects.

**Timing Path Components:**
| Component | Description | Typical Value |
|-----------|-------------|---------------|
| Clk-to-Q | Register output delay | 20-50ps |
| Logic | Combinational delay | Variable |
| Wire | Interconnect RC | Dominant at 7nm+ |
| Setup | Register requirement | 10-30ps |
| Hold | Register requirement | 5-20ps |

**Analysis Modes:**
- Setup: Worst (slow) corner, max delay
- Hold: Best (fast) corner, min delay
- Multi-mode: Multiple operating conditions
- DMSA: Distributed multi-scenario

**Variation Modeling:**
- PVT corners: Process, voltage, temperature
- OCV: On-chip variation derating
- AOCV: Advanced OCV (path-based)
- POCV: Parametric OCV (statistical)
- LVF: Liberty variation format

**Advanced STA Concepts:**
- Crosstalk analysis: SI timing impact
- Power analysis: IR drop on timing
- Multi-cycle paths: Intentional multi-clock
- False paths: Logically invalid timing paths
- Clock gating: Enable timing checks

**Sign-off Requirements:**
- Multi-corner multi-mode (MCMM)
- PT/Tempus correlation: <3% to silicon
- ECO guidance: Fix recommendations
- Noise analysis: SI + power noise
- EM/IR: Reliability constraints

**Timing Closure:**
1. Synthesis: Initial timing opt
2. Place: Placement optimization
3. CTS: Clock tree balancing
4. Route: Post-route timing
5. ECO: Final fixes
6. Sign-off: Golden STA""",
        "diagrams": [],
        "equations": [
            {"latex": "T_{clk} \\geq T_{cq} + T_{comb} + T_{setup} - T_{skew}", "description": "Setup timing constraint"},
            {"latex": "T_{hold} \\leq T_{cq} + T_{comb} - T_{skew}", "description": "Hold timing constraint"}
        ],
        "manufacturing_challenges": ["Variation modeling accuracy", "Library characterization", "Corner definition", "Power grid impact", "SI effects"],
        "applications": ["Design sign-off", "Timing closure", "ECO guidance", "Silicon correlation", "Yield optimization"],
        "advantages": ["Exhaustive coverage", "Fast runtime", "No vectors needed", "Variation awareness"],
        "limitations": ["False path handling", "Model accuracy", "Memory usage", "Runtime for large designs"],
        "related_topics": ["topic_physical_design", "topic_signoff", "topic_variation"],
        "references": [
            {"title": "PrimeTime", "url": "https://www.synopsys.com/", "source": "Synopsys"},
            {"title": "Tempus", "url": "https://www.cadence.com/", "source": "Cadence"}
        ],
        "difficulty": "advanced",
        "author": "system",
        "views": 0
    },
    # ==================== ADDITIONAL MANUFACTURING ====================
    {
        "topic_id": "topic_cmp",
        "category_id": "cat_manufacturing",
        "title": "Chemical Mechanical Planarization (CMP)",
        "slug": "chemical-mechanical-planarization",
        "overview": "CMP combines chemical etching and mechanical polishing to create atomically flat surfaces essential for multi-layer metallization and advanced lithography at nanometer feature sizes.",
        "content_beginner": """CMP is like super-precise polishing that makes wafers perfectly flat. It's essential for building many layers on a chip.

**Why Flatness Matters:**
- Lithography needs flat surfaces to focus
- Metal layers must be level
- Stacking requires planarity
- Defects from bumps cause failures

**How CMP Works:**
1. Wafer pressed against rotating pad
2. Chemical slurry attacks material
3. Mechanical abrasion removes debris
4. Result: atomically smooth surface

**Where CMP is Used:**
- After metal deposition (damascene)
- Between oxide layers (ILD CMP)
- For STI (shallow trench isolation)
- In advanced packaging

**Key Challenge:**
- Remove material evenly everywhere
- Different areas polish at different rates
- Must not scratch or damage features""",
        "content_advanced": """CMP is critical for both front-end and back-end-of-line processing with stringent uniformity requirements.

**CMP Process Parameters:**
| Parameter | Typical Range | Impact |
|-----------|---------------|--------|
| Down force | 1-4 psi | Removal rate |
| Platen speed | 30-100 rpm | Uniformity |
| Slurry flow | 100-300 ml/min | Chemistry |
| Pad temp | 25-50°C | Rate stability |

**Slurry Chemistry:**
- Oxide CMP: Colloidal silica, pH 10-11
- Cu CMP: Alumina + oxidizer + inhibitor
- W CMP: Alumina + Fe(NO3)3 oxidizer
- Barrier: Selective to Cu vs Ta/TaN

**Damascene Process:**
1. Etch trenches/vias in dielectric
2. Deposit barrier (Ta/TaN)
3. Deposit copper (seed + ECD)
4. CMP remove overburden
5. Result: Inlaid metal

**Uniformity Challenges:**
- Within-die (WID): Pattern density
- Within-wafer (WIW): Edge effects
- Dishing: Metal recessed in wide lines
- Erosion: Dielectric loss in dense areas
- Scratch/defect control

**Advanced CMP:**
- Multi-step: Bulk + finish polish
- Endpoint detection: Optical, eddy current
- Pad conditioning: In-situ groove refresh
- Slurry monitoring: Particle size, pH
- Process control: Run-to-run adjustment""",
        "diagrams": [],
        "equations": [
            {"latex": "RR = K \\times P \\times V", "description": "Preston equation for removal rate"},
            {"latex": "Nu = \\frac{Max - Min}{2 \\times Mean} \\times 100\\%", "description": "Non-uniformity calculation"}
        ],
        "manufacturing_challenges": ["Pattern density effects", "Defect control", "Endpoint accuracy", "Consumable cost", "Within-die uniformity"],
        "applications": ["Copper interconnects", "STI formation", "ILD planarization", "TSV reveal", "Advanced packaging"],
        "advantages": ["Global planarization", "Multiple material capability", "Mature process", "High throughput"],
        "limitations": ["Consumable cost", "Defect sensitivity", "Pattern dependency", "Dishing/erosion"],
        "related_topics": ["topic_deposition", "topic_damascene", "topic_interconnects"],
        "references": [
            {"title": "CMP Technology", "url": "https://www.appliedmaterials.com/", "source": "Applied Materials"},
            {"title": "Planarization", "url": "https://www.cabot-corp.com/", "source": "Cabot Microelectronics"}
        ],
        "difficulty": "intermediate",
        "author": "system",
        "views": 0
    },
    {
        "topic_id": "topic_ion_implantation",
        "category_id": "cat_manufacturing",
        "title": "Ion Implantation",
        "slug": "ion-implantation",
        "overview": "Ion implantation precisely dopes semiconductors by accelerating dopant ions into the substrate. It controls transistor threshold voltage, source/drain formation, and well structures.",
        "content_beginner": """Ion implantation is how we add dopants (special atoms) to silicon to control its electrical properties.

**Why Doping Matters:**
- Pure silicon is a poor conductor
- Adding dopant atoms changes conductivity
- N-type (extra electrons): Phosphorus, Arsenic
- P-type (missing electrons): Boron

**How It Works:**
1. Create ions from dopant gas
2. Accelerate ions with electric field
3. Ions penetrate silicon surface
4. Heat treatment activates dopants

**Key Controls:**
- **Dose**: How many atoms per area
- **Energy**: How deep atoms penetrate
- **Tilt/Rotation**: Angle of implant

**Applications:**
- Transistor threshold voltage (Vth)
- Source/drain formation
- Well implants (N-well, P-well)
- Lightly doped drain (LDD)""",
        "content_advanced": """Ion implantation enables precise doping control essential for advanced transistor engineering.

**Implanter Types:**
| Type | Energy Range | Application |
|------|-------------|-------------|
| Low energy | 0.2-10 keV | USJ, extension |
| Medium current | 10-200 keV | Well, S/D |
| High current | 10-200 keV | High dose S/D |
| High energy | 200keV-3MeV | Deep well |

**Implant Parameters:**
- Dose: 10^11 - 10^16 atoms/cm²
- Energy: 0.2 keV - 3 MeV
- Beam current: µA to mA
- Uniformity: <1% across wafer
- Angle control: 0-60° tilt

**Distribution Profile:**
- Range (Rp): Peak depth
- Straggle (ΔRp): Distribution width
- Channeling: Crystallographic effects
- LSS theory: Projected range calculation

**Advanced Implant Techniques:**
- Plasma doping (PLAD): Conformal doping
- Cluster implant: B18H22+ for USJ
- Cold implant: Reduced damage
- Molecular implants: Dose control

**Damage and Activation:**
- Lattice damage: Amorphization threshold
- Spike anneal: 1050°C, ms timescale
- Laser anneal: Surface activation
- Transient enhanced diffusion (TED)
- Dopant activation: >90% target

**Process Integration:**
- Halo/pocket: Short channel control
- Extension: LDD formation
- S/D: High dose, deep junction
- Well: Deep implant, retrograde""",
        "diagrams": [],
        "equations": [
            {"latex": "R_p = \\frac{M_1}{M_1 + M_2} \\times Range", "description": "Projected range"},
            {"latex": "N(x) = \\frac{\\Phi}{\\sqrt{2\\pi}\\Delta R_p} e^{-\\frac{(x-R_p)^2}{2\\Delta R_p^2}}", "description": "Gaussian profile"}
        ],
        "manufacturing_challenges": ["Ultra-shallow junctions", "Dose uniformity", "Channeling control", "Damage minimization", "Activation efficiency"],
        "applications": ["CMOS transistors", "Source/drain", "Well formation", "Threshold adjust", "Power devices"],
        "advantages": ["Precise dose control", "Profile engineering", "Reproducibility", "Low temperature"],
        "limitations": ["Lattice damage", "Channeling", "Throughput (high dose)", "Equipment cost"],
        "related_topics": ["topic_finfet", "topic_gaafet", "topic_annealing"],
        "references": [
            {"title": "Ion Implantation", "url": "https://www.appliedmaterials.com/", "source": "Applied Materials"},
            {"title": "Implant Technology", "url": "https://www.axcelis.com/", "source": "Axcelis"}
        ],
        "difficulty": "intermediate",
        "author": "system",
        "views": 0
    },
    # ==================== ADVANCED NODES ====================
    {
        "topic_id": "topic_intel_18a",
        "category_id": "cat_nodes",
        "title": "Intel 18A Process",
        "slug": "intel-18a-process",
        "overview": "Intel 18A (1.8nm-class) is Intel's most advanced node combining RibbonFET (GAAFET) transistors with PowerVia backside power delivery, targeting 2024-2025 production.",
        "content_beginner": """Intel 18A is one of the most advanced chip manufacturing processes, using cutting-edge technology.

**Key Technologies:**

**RibbonFET:**
- Intel's version of gate-all-around
- Gate wraps completely around channel
- Better control than FinFET
- Multiple stacked ribbons

**PowerVia (Backside Power):**
- Power delivered from back of chip
- Frees up space on front for signals
- Better power delivery
- First production backside power

**Why It Matters:**
- Competes with TSMC's 2nm
- Shows Intel's manufacturing comeback
- Enables faster, more efficient chips
- First to combine GAA + backside power

**Timeline:**
- 2024-2025: Production ramp
- Key customers: Internal + foundry""",
        "content_advanced": """Intel 18A represents a significant technology transition combining multiple innovations.

**RibbonFET Architecture:**
| Parameter | Intel 18A | N3 (TSMC) | Notes |
|-----------|-----------|-----------|-------|
| Transistor | GAA/RibbonFET | FinFET | Architecture |
| Nanosheet width | ~Variable | N/A | Width modulation |
| Gate pitch | ~48nm (est) | 48nm | Scaling metric |
| Metal pitch | ~21nm (est) | 21nm | BEOL density |

**PowerVia Benefits:**
- >90% VDD utilization (vs ~80% frontside)
- 30-50% IR drop reduction
- Signal routing density improvement
- Thermal path enhancement

**Process Flow (Simplified):**
1. Front-side transistors, local interconnect
2. Intermediate metal layers
3. Wafer bonding to carrier
4. Wafer thinning (<50µm)
5. Nano-TSV formation
6. Backside metal (power rails)
7. Integration completion

**Competitive Position:**
- Direct competition: TSMC N2, Samsung SF2
- First GAA + BSPD combination
- Key differentiator for foundry business
- Arrow Lake, Panther Lake internal chips

**Manufacturing Challenges:**
- Yield ramp with dual innovations
- Thin wafer handling
- Front-to-back alignment
- Cost structure
- Equipment availability""",
        "diagrams": [],
        "equations": [
            {"latex": "P_{density} \\propto \\frac{1}{GP \\times MP}", "description": "Power density scaling"},
            {"latex": "IR_{drop} = I \\times R_{PDN}", "description": "IR drop in power delivery"}
        ],
        "manufacturing_challenges": ["Dual technology introduction", "Yield learning", "Cost management", "Equipment ecosystem", "Design enablement"],
        "applications": ["High-performance computing", "Data center", "Client processors", "AI accelerators", "Foundry customers"],
        "advantages": ["Leadership density", "Power efficiency", "Performance", "Foundry differentiation"],
        "limitations": ["Manufacturing risk", "Cost premium", "Ecosystem readiness", "Ramp timeline"],
        "related_topics": ["topic_gaafet", "topic_bspd", "topic_2nm"],
        "references": [
            {"title": "Intel Process Roadmap", "url": "https://www.intel.com/", "source": "Intel"},
            {"title": "Intel 18A Details", "url": "https://semianalysis.com/", "source": "SemiAnalysis"}
        ],
        "difficulty": "advanced",
        "author": "system",
        "views": 0
    },
    {
        "topic_id": "topic_samsung_sf2",
        "category_id": "cat_nodes",
        "title": "Samsung SF2 Process",
        "slug": "samsung-sf2-process",
        "overview": "Samsung SF2 is Samsung's 2nm-class process using second-generation GAA (MBCFET) transistors with enhanced performance and power efficiency for 2025+ production.",
        "content_beginner": """Samsung SF2 is Samsung's next-generation chip manufacturing process, competing with TSMC and Intel.

**Key Features:**

**Second-Gen GAA (MBCFET):**
- Multi-Bridge Channel FET
- Samsung pioneered GAA in production
- SF2 is the improved version
- Better performance than first-gen

**Improvements over SF3:**
- Smaller transistors
- Lower power consumption
- Higher performance
- Better efficiency

**Samsung's Position:**
- First to produce GAA chips (3nm)
- Learning from early GAA experience
- Targeting foundry customers
- Competition with TSMC N2

**Applications:**
- Mobile processors
- Automotive chips
- AI accelerators
- High-performance computing""",
        "content_advanced": """Samsung SF2 builds on Samsung's GAA experience with improved device and BEOL characteristics.

**SF2 vs SF3 Comparison:**
| Metric | SF3 (3GAE) | SF2 (2nm) | Improvement |
|--------|------------|-----------|-------------|
| Logic density | ~1.6x N5 | ~2x N5 | ~25% |
| Performance | +10% vs SF4 | +12% vs SF3 | Incremental |
| Power | -25% vs SF4 | -25% vs SF3 | Continued |
| SRAM density | Similar | Improved | Scaling |

**MBCFET Architecture:**
- Nanosheet stacking: 3-4 sheets
- Sheet width: Variable (performance tuning)
- Gate length: <12nm (estimated)
- Channel material: Strained Si

**BEOL Characteristics:**
- Metal layers: 15-17
- Min metal pitch: ~21nm
- Via pitch: Aggressive scaling
- Low-k dielectric: k<2.5

**Manufacturing Status:**
- SF3: Production 2022
- SF4: Production 2024
- SF2: Target 2025-2026
- Key customers: Qualcomm, Google potential

**Challenges:**
- Yield improvement from early GAA
- Customer acquisition vs TSMC
- Design ecosystem development
- Cost competitiveness""",
        "diagrams": [],
        "equations": [
            {"latex": "I_{drive} \\propto W_{eff} \\times N_{sheets}", "description": "Drive current with nanosheet count"},
            {"latex": "C_{gate} = \\epsilon \\times A / t_{ox}", "description": "Gate capacitance"}
        ],
        "manufacturing_challenges": ["Nanosheet formation", "Inner spacer control", "Work function metal fill", "Variability management", "Yield scaling"],
        "applications": ["Mobile SoCs", "Automotive", "HPC", "AI chips", "Foundry services"],
        "advantages": ["GAA experience", "Technology leadership", "Capacity availability", "Cost competition"],
        "limitations": ["Yield maturity", "Ecosystem breadth", "Customer confidence", "Design support"],
        "related_topics": ["topic_gaafet", "topic_2nm", "topic_tsmc"],
        "references": [
            {"title": "Samsung Foundry", "url": "https://semiconductor.samsung.com/foundry/", "source": "Samsung"},
            {"title": "MBCFET Technology", "url": "https://news.samsung.com/", "source": "Samsung Newsroom"}
        ],
        "difficulty": "advanced",
        "author": "system",
        "views": 0
    },
    # ==================== FOUNDRIES ====================
    {
        "topic_id": "topic_intel_foundry",
        "category_id": "cat_foundries",
        "title": "Intel Foundry Services",
        "slug": "intel-foundry-services",
        "overview": "Intel Foundry Services (IFS) is Intel's foundry business offering leading-edge and specialty processes to external customers, leveraging Intel's manufacturing and packaging technologies.",
        "content_beginner": """Intel Foundry Services (IFS) is Intel's business making chips for other companies.

**What is a Foundry?**
- A company that manufactures chips for others
- Customers design chips, foundry makes them
- Like a factory for hire
- TSMC is the biggest foundry

**Why Intel Started IFS:**
- Intel traditionally made only its own chips
- Now offering capacity to others
- Competing with TSMC, Samsung
- Part of Intel's turnaround plan

**What IFS Offers:**
- Leading-edge processes (Intel 18A, 20A)
- Advanced packaging (Foveros, EMIB)
- Specialty processes
- Capacity in US and Europe

**Key Customers:**
- US government (secure supply)
- Automotive companies
- AI chip designers
- Potential: MediaTek, Qualcomm""",
        "content_advanced": """Intel Foundry Services represents Intel's strategic pivot to compete in the foundry market.

**Process Portfolio:**
| Node | Status | Key Feature | Target |
|------|--------|-------------|--------|
| Intel 3 | Production | Enhanced FinFET | Volume |
| Intel 20A | 2024 | RibbonFET | Early |
| Intel 18A | 2024-25 | RibbonFET + PowerVia | Lead |
| Intel 14A | 2026+ | High-NA EUV | Future |

**Packaging Technologies:**
- **EMIB**: Embedded multi-die interconnect bridge
- **Foveros**: 3D die stacking
- **Foveros Direct**: Cu-Cu hybrid bonding
- **Co-EMIB**: Combined 2.5D + 3D

**Business Model:**
- External foundry customers
- Internal BU (product groups)
- Separate P&L tracking
- Capacity sharing model

**Strategic Initiatives:**
- CHIPS Act funding ($8.5B)
- Ohio mega-fab construction
- European expansion (Germany)
- US government contracts

**Competitive Analysis:**
- vs TSMC: Technology catch-up, geopolitical
- vs Samsung: Similar position, yield focus
- vs GlobalFoundries: Advanced node differentiation

**Challenges:**
- Customer trust building
- Design ecosystem development
- Yield competitiveness
- Cost structure optimization""",
        "diagrams": [],
        "equations": [
            {"latex": "Revenue = Volume \\times ASP", "description": "Foundry revenue model"},
            {"latex": "Margin = (ASP - Cost) / ASP", "description": "Gross margin"}
        ],
        "manufacturing_challenges": ["Yield parity with competitors", "Customer PDK development", "Capacity ramp", "Ecosystem building", "Cost competitiveness"],
        "applications": ["Government/defense", "AI accelerators", "Automotive", "HPC", "Consumer electronics"],
        "advantages": ["US/EU manufacturing", "Advanced packaging", "Technology roadmap", "Government support"],
        "limitations": ["Limited track record", "Ecosystem maturity", "Customer relationships", "Yield history"],
        "related_topics": ["topic_tsmc", "topic_intel_18a", "topic_packaging"],
        "references": [
            {"title": "Intel Foundry", "url": "https://www.intel.com/foundry/", "source": "Intel"},
            {"title": "IFS Strategy", "url": "https://semianalysis.com/", "source": "SemiAnalysis"}
        ],
        "difficulty": "intermediate",
        "author": "system",
        "views": 0
    },
    {
        "topic_id": "topic_globalfoundries",
        "category_id": "cat_foundries",
        "title": "GlobalFoundries",
        "slug": "globalfoundries",
        "overview": "GlobalFoundries is the third-largest foundry specializing in mature and specialty nodes (12nm-180nm), serving automotive, IoT, RF, and analog applications without competing at leading edge.",
        "content_beginner": """GlobalFoundries is a major chip foundry focused on specialty and mature technology nodes.

**Company Background:**
- Spun off from AMD in 2009
- Owned by Mubadala (Abu Dhabi)
- Went public (IPO) in 2021
- Third largest foundry globally

**Focus Areas:**
- NOT leading edge (stopped 7nm in 2018)
- Specialty technologies
- Mature nodes (22nm, 12nm and older)
- Differentiated features

**Key Markets:**
- **Automotive**: Long product lifecycles
- **IoT**: Low power devices
- **RF/5G**: Communications chips
- **Industrial**: Reliable, mature processes

**Why Choose GF:**
- Feature-rich mature nodes
- Automotive qualification
- US + Europe + Singapore capacity
- Supply chain resilience""",
        "content_advanced": """GlobalFoundries serves markets where specialized features matter more than density.

**Technology Portfolio:**
| Platform | Node | Features | Market |
|----------|------|----------|--------|
| 22FDX | 22nm | FD-SOI, RF | Mobile, IoT |
| 12LP | 12nm | FinFET | HPC, comm |
| 45RFSOI | 45nm | RF-SOI | 5G, RF |
| 55LPe | 55nm | BCD | Automotive, power |

**Key Differentiators:**
- FD-SOI (22FDX): Body biasing, low power
- RF-SOI: 5G mmWave, front-end modules
- BCD: Integrated power management
- Automotive: AEC-Q100 qualified

**Manufacturing Footprint:**
- Malta, NY (Fab 8): 300mm, 12nm
- Dresden, Germany: 300mm, 22nm
- Singapore: 200/300mm, mature
- Burlington, VT: 200mm, specialty

**Business Model:**
- Long-term agreements (LTAs)
- Capacity reservation fees
- Automotive qualification premium
- Feature licensing

**Strategic Position:**
- Immune to leading-edge cost escalation
- Sticky customer relationships
- Automotive/industrial focus
- Supply chain diversification value

**Challenges:**
- Limited growth at mature nodes
- Pricing pressure from China
- Capacity utilization cycles
- Technology differentiation sustain""",
        "diagrams": [],
        "equations": [
            {"latex": "ASP_{specialty} > ASP_{commodity}", "description": "Specialty pricing premium"},
            {"latex": "Utilization = Wafer\\_Starts / Capacity", "description": "Fab utilization"}
        ],
        "manufacturing_challenges": ["Feature differentiation", "Yield for automotive", "Cost competition", "Capacity planning", "Technology sustaining"],
        "applications": ["Automotive MCUs", "RF front-ends", "IoT controllers", "Power management", "Industrial"],
        "advantages": ["Specialty focus", "Multi-geography", "Automotive expertise", "Supply security"],
        "limitations": ["No leading edge", "Limited growth ceiling", "China competition", "Customer concentration"],
        "related_topics": ["topic_tsmc", "topic_automotive_chips", "topic_rf_devices"],
        "references": [
            {"title": "GlobalFoundries", "url": "https://www.globalfoundries.com/", "source": "GlobalFoundries"},
            {"title": "GF Technology", "url": "https://semiengineering.com/", "source": "Semiconductor Engineering"}
        ],
        "difficulty": "intermediate",
        "author": "system",
        "views": 0
    },
    # ==================== APPLICATIONS ====================
    {
        "topic_id": "topic_ai_chips",
        "category_id": "cat_applications",
        "title": "AI Accelerator Chips",
        "slug": "ai-accelerator-chips",
        "overview": "AI accelerators are specialized processors optimized for machine learning workloads, featuring massive parallelism, high memory bandwidth, and specialized compute units for matrix operations.",
        "content_beginner": """AI accelerator chips are specialized processors designed to run artificial intelligence workloads much faster than regular CPUs.

**Why Special Chips for AI?**
- AI needs lots of matrix math
- CPUs are general-purpose, not optimized
- GPUs helped, but custom chips are better
- Training large AI models requires huge compute

**Types of AI Accelerators:**

**GPUs (Graphics Processing Units):**
- Originally for graphics
- NVIDIA dominates (A100, H100)
- Good at parallel operations
- Most mature AI platform

**TPUs (Tensor Processing Units):**
- Google's custom AI chip
- Optimized for TensorFlow
- Used in Google's data centers

**Custom ASICs:**
- Purpose-built for specific AI tasks
- Examples: Tesla Dojo, AWS Trainium
- Most efficient but least flexible

**Key Features:**
- High memory bandwidth (HBM)
- Many parallel compute units
- Fast interconnects
- High power consumption""",
        "content_advanced": """AI accelerators are defined by their architecture, memory system, and interconnect design.

**Leading AI Accelerators:**
| Chip | Process | Compute | Memory | Power |
|------|---------|---------|--------|-------|
| H100 | TSMC 4N | 989 TFLOPS FP16 | 80GB HBM3 | 700W |
| MI300X | TSMC 5nm | 1307 TFLOPS | 192GB HBM3 | 750W |
| TPU v5p | TSMC 4nm | 459 TFLOPS | HBM2e | ~500W |
| Gaudi 3 | TSMC 5nm | 1835 TFLOPS | 128GB HBM2e | 900W |

**Architecture Components:**
- Tensor cores/units: Matrix multiply
- Vector units: Activation, normalization
- Memory hierarchy: L1/L2/HBM
- Interconnect: NVLink, Infinity Fabric

**Memory Bandwidth Challenge:**
- Transformer models are memory-bound
- H100: 3.35 TB/s HBM bandwidth
- Batch size vs latency trade-off
- KV-cache optimization critical

**Scaling Architectures:**
- Multi-chip modules (MCM)
- Chiplet designs
- Wafer-scale: Cerebras
- Optical interconnects emerging

**Workload Considerations:**
- Training: High precision (FP32/FP16)
- Inference: Lower precision (INT8/FP8)
- LLMs: Memory bandwidth critical
- Vision: Compute-bound

**Interconnect Technologies:**
- NVLink: 900 GB/s (H100)
- Infinity Fabric: AMD chiplet
- Scale-out: InfiniBand, Ethernet
- In-rack: NVSwitch, proprietary""",
        "diagrams": [],
        "equations": [
            {"latex": "FLOPS = Cores \\times Freq \\times OPS/cycle", "description": "Compute throughput"},
            {"latex": "AI\\_Efficiency = FLOPS / Watt", "description": "AI performance efficiency"}
        ],
        "manufacturing_challenges": ["HBM integration", "Power delivery", "Thermal management", "Yield (large die)", "Packaging complexity"],
        "applications": ["LLM training", "LLM inference", "Computer vision", "Recommendation systems", "Scientific computing"],
        "advantages": ["Massive parallelism", "High efficiency for AI", "Memory bandwidth", "Ecosystem support"],
        "limitations": ["High power consumption", "Cost", "Limited programmability", "Workload specificity"],
        "related_topics": ["topic_hbm", "topic_cowos", "topic_chiplet"],
        "references": [
            {"title": "NVIDIA H100", "url": "https://www.nvidia.com/", "source": "NVIDIA"},
            {"title": "AI Hardware", "url": "https://semianalysis.com/", "source": "SemiAnalysis"}
        ],
        "difficulty": "intermediate",
        "author": "system",
        "views": 0
    },
    {
        "topic_id": "topic_automotive_chips",
        "category_id": "cat_applications",
        "title": "Automotive Semiconductors",
        "slug": "automotive-semiconductors",
        "overview": "Automotive semiconductors must meet stringent reliability, temperature, and safety requirements (AEC-Q100). Modern vehicles contain 1,000-3,000 chips for powertrain, ADAS, infotainment, and electrification.",
        "content_beginner": """Automotive chips are specially designed to work reliably in cars, which have harsh conditions.

**Why Cars Need Special Chips:**
- Temperature extremes (-40°C to +150°C)
- Vibration and shock
- Long lifetime (15+ years)
- Safety critical (lives at stake)

**Chip Categories in Cars:**

**Microcontrollers (MCUs):**
- Brains of car systems
- Engine control, body electronics
- Many per vehicle (dozens)

**Power Semiconductors:**
- Control electric motors
- Manage batteries in EVs
- SiC and IGBT devices

**Sensors:**
- Cameras, radar, lidar (ADAS)
- Pressure, temperature sensors
- Position sensors

**ADAS & Autonomous Driving:**
- AI processors for vision
- Sensor fusion computing
- Safety-critical real-time

**Qualification:**
- AEC-Q100 for ICs
- AEC-Q101 for discretes
- ISO 26262 functional safety""",
        "content_advanced": """Automotive semiconductors require specialized qualification and long-term supply commitments.

**Qualification Requirements:**
| Grade | Temp Range | Applications |
|-------|------------|--------------|
| Grade 0 | -40 to +150°C | Under-hood |
| Grade 1 | -40 to +125°C | General auto |
| Grade 2 | -40 to +105°C | Interior |
| Grade 3 | -40 to +85°C | Consumer-like |

**AEC-Q100 Key Tests:**
- HTOL: High temperature operating life
- TC: Temperature cycling (1000+ cycles)
- THB: Temp/humidity/bias
- ESD: >2kV HBM, >500V CDM
- Latch-up: >100mA at +125°C

**Functional Safety (ISO 26262):**
- ASIL levels: A, B, C, D (highest)
- ASIL-D: Self-driving critical
- Fault detection, redundancy
- SEU (single event upset) immunity

**Automotive vs Consumer:**
| Aspect | Automotive | Consumer |
|--------|------------|----------|
| Lifetime | 15+ years | 2-3 years |
| Defect rate | <1 DPPM | 100s DPPM |
| Temp range | -40 to +175°C | 0 to +70°C |
| Qualification | 6-24 months | Weeks |
| Price premium | 2-10x | Baseline |

**EV Semiconductor Content:**
- ICE vehicle: ~$500 semis/car
- BEV vehicle: ~$1,500 semis/car
- Autonomous L4/5: +$1,000+/car
- Power semis (SiC): $500-1,000/car

**Supply Chain Considerations:**
- Long product lifecycles (10+ years)
- Dual sourcing requirements
- Change notification requirements
- Supply chain traceability""",
        "diagrams": [],
        "equations": [
            {"latex": "DPPM = \\frac{Defects}{10^6\\_units}", "description": "Defective parts per million"},
            {"latex": "FIT = \\frac{Failures}{10^9\\_hours}", "description": "Failure in time rate"}
        ],
        "manufacturing_challenges": ["Quality requirements", "Long qualification", "Temperature extremes", "Zero-defect targets", "Supply continuity"],
        "applications": ["Powertrain control", "ADAS/autonomous", "EV power electronics", "Infotainment", "Body electronics"],
        "advantages": ["High reliability", "Long lifecycle revenue", "Growing content per vehicle", "EV transition growth"],
        "limitations": ["Slow qualification", "High development cost", "Capacity planning", "Liability concerns"],
        "related_topics": ["topic_sic", "topic_mcu", "topic_safety"],
        "references": [
            {"title": "Automotive Qualification", "url": "https://www.aecouncil.com/", "source": "AEC"},
            {"title": "Auto Semiconductors", "url": "https://www.infineon.com/", "source": "Infineon"}
        ],
        "difficulty": "intermediate",
        "author": "system",
        "views": 0
    }
]


def get_additional_topics():
    """Return additional topics for encyclopedia expansion"""
    return ADDITIONAL_TOPICS
