"""
Final Encyclopedia Topics - Part 5
Final 10 topics to reach 100+ total
"""

FINAL_TOPICS = [
    {
        "topic_id": "topic_mems",
        "category_id": "cat_devices",
        "title": "MEMS Devices",
        "slug": "mems-devices",
        "overview": "Micro-Electro-Mechanical Systems combine electronic and mechanical elements at microscale. MEMS sensors and actuators enable smartphones, automotive, medical, and industrial applications.",
        "content_beginner": """MEMS are tiny machines on chips - mechanical parts smaller than a hair!

**What MEMS Do:**
- Accelerometers detect motion
- Gyroscopes sense rotation
- Pressure sensors measure pressure
- Microphones capture sound

**Where You Find MEMS:**
- Smartphones (orientation, motion)
- Cars (airbag sensors, tire pressure)
- Game controllers (motion control)
- Medical devices
- Industrial equipment""",
        "content_advanced": """MEMS fabrication combines semiconductor and mechanical processes.

**MEMS Technologies:**
- Surface micromachining
- Bulk micromachining
- LIGA (X-ray lithography)
- Wafer bonding

**Common MEMS:**
- Inertial: Accelerometer, gyro
- Pressure: Automotive, medical
- Optical: DMD, MEMS mirrors
- RF: Switches, resonators
- Bio: Lab-on-chip, DNA sequencing""",
        "diagrams": [],
        "equations": [
            {"latex": "F = ma", "description": "Accelerometer principle"},
            {"latex": "\\omega = \\frac{2\\Omega v}{a}", "description": "Coriolis effect in gyroscope"}
        ],
        "manufacturing_challenges": ["Release etch", "Stiction", "Packaging", "Hermeticity"],
        "applications": ["Mobile", "Automotive", "Medical", "Industrial", "Consumer"],
        "advantages": ["Small size", "Low cost at volume", "Low power", "High reliability"],
        "limitations": ["Sensitive to environment", "Packaging cost", "Testing complexity"],
        "related_topics": ["topic_iot_chips", "topic_automotive_chips", "topic_sensors"],
        "references": [],
        "difficulty": "intermediate",
        "author": "system",
        "views": 0
    },
    {
        "topic_id": "topic_gan_power",
        "category_id": "cat_devices",
        "title": "GaN Power Devices",
        "slug": "gan-power-devices",
        "overview": "Gallium Nitride enables high-frequency, high-efficiency power conversion. GaN-on-Si HEMTs are transforming chargers, data centers, EVs, and RF applications with 10x switching speed versus silicon.",
        "content_beginner": """GaN power devices switch faster and waste less energy than silicon.

**Why GaN?**
- Very fast switching (MHz vs kHz)
- Lower losses (higher efficiency)
- Smaller components possible
- Works at higher temperatures

**Where GaN is Used:**
- Fast phone chargers (GaN chargers)
- Server power supplies
- Electric vehicle chargers
- Solar inverters
- 5G base stations""",
        "content_advanced": """GaN-on-Si technology enables cost-effective power electronics.

**GaN vs Si Comparison:**
| Property | Si | GaN |
|----------|-----|-----|
| Band gap | 1.1 eV | 3.4 eV |
| Breakdown | 0.3 MV/cm | 3.3 MV/cm |
| Mobility | 1400 | 2000 |
| Saturation velocity | 1×10^7 | 2.5×10^7 |

**GaN Device Types:**
- Enhancement-mode HEMT (normally-off)
- Depletion-mode (normally-on, needs cascode)
- Integrated GaN ICs (driver + power stage)""",
        "diagrams": [],
        "equations": [
            {"latex": "P_{loss} = I^2 R_{on} + \\frac{1}{2}CV^2 f", "description": "Switching losses"},
            {"latex": "FOM = R_{on} \\times Q_{g}", "description": "Figure of merit"}
        ],
        "manufacturing_challenges": ["GaN-on-Si defects", "Thermal management", "Reliability", "Cost"],
        "applications": ["Fast chargers", "Data center power", "EV", "5G", "Solar"],
        "advantages": ["High frequency", "High efficiency", "Small size", "Integration"],
        "limitations": ["Higher cost than Si", "Thermal management", "Limited voltage range"],
        "related_topics": ["topic_sic", "topic_iii_v", "topic_power_mosfet"],
        "references": [],
        "difficulty": "intermediate",
        "author": "system",
        "views": 0
    },
    {
        "topic_id": "topic_asic",
        "category_id": "cat_applications",
        "title": "Application-Specific ICs (ASICs)",
        "slug": "asic-design",
        "overview": "ASICs are custom chips designed for specific applications, offering optimal performance, power, and cost at volume. They range from simple gate arrays to complex SoCs for AI and crypto mining.",
        "content_beginner": """ASICs are custom-designed chips for specific tasks.

**ASIC vs Other Options:**
- **ASIC:** Custom design, best performance, high NRE
- **FPGA:** Reprogrammable, faster time-to-market
- **CPU:** General purpose, most flexible

**When to Use ASIC:**
- High volume production
- Performance critical
- Power efficiency matters
- Cost per chip matters at scale

**Examples:**
- Bitcoin mining chips
- AI inference accelerators
- Network processors
- Video encoders""",
        "content_advanced": """ASIC development involves significant upfront investment for volume benefits.

**ASIC Economics:**
| Factor | ASIC | FPGA |
|--------|------|------|
| NRE | $1-100M | ~$0 |
| Unit cost | $1-100 | $10-10K |
| Break-even | 10K-1M units | N/A |
| Performance | Best | 3-10x slower |
| Power | Best | 3-5x higher |

**Design Flow:**
1. Specification
2. RTL design
3. Verification
4. Synthesis
5. Physical design
6. Signoff
7. Tapeout
8. Manufacturing""",
        "diagrams": [],
        "equations": [
            {"latex": "TCO = NRE + N \\times Unit\\_Cost", "description": "Total cost of ownership"},
            {"latex": "Break\\_even = \\frac{NRE}{Cost_{FPGA} - Cost_{ASIC}}", "description": "Volume for ASIC benefit"}
        ],
        "manufacturing_challenges": ["High NRE", "Long design cycle", "Mask costs", "Risk of bugs"],
        "applications": ["AI accelerators", "Cryptocurrency", "Networking", "Consumer electronics"],
        "advantages": ["Best performance", "Lowest power", "Lowest unit cost at volume"],
        "limitations": ["High NRE", "Long development", "No changes after fabrication"],
        "related_topics": ["topic_fpga", "topic_rtl_design", "topic_physical_design"],
        "references": [],
        "difficulty": "intermediate",
        "author": "system",
        "views": 0
    },
    {
        "topic_id": "topic_wafer_fab",
        "category_id": "cat_manufacturing",
        "title": "Wafer Fabrication Facility",
        "slug": "wafer-fabrication-facility",
        "overview": "A fab is an ultra-clean manufacturing facility for semiconductor wafers. Modern fabs cost $10-20B, require Class 1 cleanrooms, and run 24/7 with thousands of process steps per wafer.",
        "content_beginner": """A fab is the factory where chips are made on silicon wafers.

**What Makes Fabs Special:**
- Ultra-clean rooms (cleaner than hospital OR)
- Incredibly precise equipment
- Temperature/humidity controlled
- Vibration isolated

**Cleanroom Classes:**
- Class 1: <1 particle per cubic foot
- Your bedroom: ~1,000,000 particles!
- Workers wear full bunny suits

**Cost and Scale:**
- Modern fab: $10-20 billion
- 3-4 years to build
- Runs 24/7/365
- Thousands of employees""",
        "content_advanced": """Leading-edge fabs represent massive capital investments and operational complexity.

**Fab Economics:**
| Node | Fab Cost | Equipment | Tools |
|------|----------|-----------|-------|
| 28nm | $5-7B | $2-4B | ~500 |
| 7nm | $10-15B | $5-8B | ~800 |
| 3nm | $15-20B | $10-12B | ~1000 |

**Key Systems:**
- Process tools: Litho, etch, dep, etc.
- Automation: AMHS, wafer handling
- Facilities: Cleanroom, utilities
- IT: MES, APC, yield systems

**Operating Metrics:**
- Cycle time: 60-90 days
- Wafer starts: 50-100K/month
- Yield: 80-95% (mature)
- Uptime: >95% per tool""",
        "diagrams": [],
        "equations": [
            {"latex": "Cost/die = \\frac{Wafer\\_cost}{Good\\_dies}", "description": "Die cost"},
            {"latex": "Cycle\\_time = \\sum Steps \\times (Process + Queue)", "description": "Manufacturing cycle time"}
        ],
        "manufacturing_challenges": ["Capital investment", "Yield ramp", "Talent", "Supply chain"],
        "applications": ["Logic", "Memory", "Analog", "Power", "MEMS"],
        "advantages": ["High volume capability", "Process control", "Quality"],
        "limitations": ["Massive investment", "Long construction", "Technology risk"],
        "related_topics": ["topic_tsmc", "topic_yield_management", "topic_wafer_inspection"],
        "references": [],
        "difficulty": "beginner",
        "author": "system",
        "views": 0
    },
    {
        "topic_id": "topic_soi",
        "category_id": "cat_materials",
        "title": "Silicon-on-Insulator (SOI)",
        "slug": "silicon-on-insulator",
        "overview": "SOI wafers have a thin silicon layer on buried oxide, reducing parasitic capacitance and enabling fully-depleted transistors. FD-SOI provides an alternative scaling path to FinFET for low-power applications.",
        "content_beginner": """SOI wafers have an insulating layer that improves transistor performance.

**SOI Structure:**
- Thin silicon on top (device layer)
- Buried oxide (BOX) insulator
- Silicon handle wafer below

**Benefits:**
- Lower capacitance (faster)
- Less leakage (lower power)
- Better isolation
- Radiation hardness

**Where SOI is Used:**
- Low-power mobile chips
- RF circuits
- Automotive
- Aerospace/military""",
        "content_advanced": """FD-SOI offers unique features for low-power, RF, and automotive applications.

**SOI Technologies:**
| Type | Silicon | BOX | Application |
|------|---------|-----|-------------|
| PD-SOI | Thick | 100-200nm | Legacy |
| FD-SOI | 5-12nm | 20-25nm | Current |
| RF-SOI | Variable | Thick | RF switches |
| Photonics | 220nm | 2µm | Optical |

**FD-SOI Advantages:**
- Body biasing for Vth control
- Excellent analog/RF performance
- Low power
- Simplified process vs FinFET

**Manufacturing:**
- Smart Cut process
- SIMOX (legacy)
- Wafer bonding""",
        "diagrams": [],
        "equations": [
            {"latex": "V_{th} = V_{th0} - \\gamma V_{BB}", "description": "Body bias effect"},
            {"latex": "C_{BOX} = \\frac{\\epsilon_{ox}}{t_{BOX}}", "description": "BOX capacitance"}
        ],
        "manufacturing_challenges": ["Wafer cost", "Thickness control", "Limited suppliers"],
        "applications": ["Low-power IoT", "Automotive", "RF", "Aerospace"],
        "advantages": ["Low power", "Body biasing", "Good analog", "Radiation hard"],
        "limitations": ["Wafer cost", "Limited ecosystem", "Self-heating"],
        "related_topics": ["topic_silicon", "topic_finfet", "topic_iot_chips"],
        "references": [],
        "difficulty": "intermediate",
        "author": "system",
        "views": 0
    },
    {
        "topic_id": "topic_hbm",
        "category_id": "cat_memory",
        "title": "High Bandwidth Memory (HBM)",
        "slug": "high-bandwidth-memory",
        "overview": "HBM stacks multiple DRAM dies with TSVs for ultra-high bandwidth. HBM3 provides 819 GB/s per stack, essential for AI accelerators, GPUs, and high-performance computing.",
        "content_beginner": """HBM is memory stacked in 3D for massive bandwidth.

**Why HBM?**
- AI needs huge memory bandwidth
- Regular memory can't keep up
- Stack DRAM dies vertically
- Connect with tiny through-silicon vias

**HBM Structure:**
- 4-12 DRAM dies stacked
- Base logic die on bottom
- TSVs connect all layers
- Very wide interface (1024 bits)

**Where HBM is Used:**
- AI accelerators (NVIDIA H100)
- High-end GPUs
- High-performance computing
- Network processors""",
        "content_advanced": """HBM evolution provides increasing bandwidth for AI workloads.

**HBM Generations:**
| Gen | BW/stack | Stack | Year |
|-----|----------|-------|------|
| HBM | 128 GB/s | 4-hi | 2015 |
| HBM2 | 307 GB/s | 8-hi | 2018 |
| HBM2E | 461 GB/s | 8-hi | 2020 |
| HBM3 | 819 GB/s | 12-hi | 2022 |
| HBM3E | 1.2 TB/s | 12-hi | 2024 |

**Key Specifications:**
- Interface: 1024 bits wide
- Channels: 8-16 per stack
- TSV pitch: 36-40µm
- Micro-bumps: 55µm pitch
- Power: ~2.5W per stack

**Integration:**
- CoWoS (TSMC)
- Foveros (Intel)
- I-Cube (Samsung)""",
        "diagrams": [],
        "equations": [
            {"latex": "BW = Width \\times Rate", "description": "Memory bandwidth"},
            {"latex": "BW_{total} = N_{stacks} \\times BW_{stack}", "description": "Total system bandwidth"}
        ],
        "manufacturing_challenges": ["TSV yield", "Thermal management", "Known good die", "Cost"],
        "applications": ["AI accelerators", "GPUs", "HPC", "Networking"],
        "advantages": ["Extreme bandwidth", "Low power per bit", "Small footprint"],
        "limitations": ["High cost", "Limited capacity", "Thermal constraints"],
        "related_topics": ["topic_dram", "topic_tsv", "topic_ai_chips"],
        "references": [],
        "difficulty": "intermediate",
        "author": "system",
        "views": 0
    },
    {
        "topic_id": "topic_bspd",
        "category_id": "cat_packaging",
        "title": "Backside Power Delivery",
        "slug": "backside-power-delivery",
        "overview": "Backside power delivery routes power from the back of the die, freeing front-side metal for signals. Intel PowerVia and TSMC backside power demonstrate 10-30% IR drop improvement and routing density gains.",
        "content_beginner": """Backside power delivery brings power to chips from behind instead of above.

**Traditional vs Backside:**
- Traditional: Power and signals share front metal layers
- Backside: Power from back, signals on front
- More room for both!

**Benefits:**
- Better power delivery (lower voltage drop)
- More signal routing space
- Smaller cell sizes possible
- Better performance

**Who's Doing It:**
- Intel PowerVia (Intel 20A, 18A)
- TSMC backside power (N2P)
- Samsung exploring""",
        "content_advanced": """BSPD requires wafer thinning and backside processing.

**BSPD Process:**
1. Front-side transistors + local interconnect
2. Some metal layers
3. Bond to carrier
4. Thin wafer (<50µm)
5. Form nano-TSVs
6. Backside metal (power rails)
7. Complete integration

**Benefits Quantified:**
- IR drop: 30-50% reduction
- Cell utilization: >90% power rail
- Signal routing: 10-15% more
- Performance: 5-10% improvement

**Challenges:**
- Wafer handling (thin)
- Alignment front-to-back
- Thermal path changes
- Cost increase""",
        "diagrams": [],
        "equations": [
            {"latex": "IR_{drop} = I \\times R_{PDN}", "description": "Power delivery voltage drop"},
            {"latex": "R \\propto \\frac{\\rho L}{A}", "description": "Resistance of power path"}
        ],
        "manufacturing_challenges": ["Thin wafer handling", "Alignment", "TSV formation", "Cost"],
        "applications": ["High-performance logic", "Leading-edge nodes", "Server CPUs"],
        "advantages": ["Better power delivery", "More routing", "Performance gain"],
        "limitations": ["Process complexity", "Cost", "Thermal management changes"],
        "related_topics": ["topic_intel_18a", "topic_tsv", "topic_2nm"],
        "references": [],
        "difficulty": "advanced",
        "author": "system",
        "views": 0
    },
    {
        "topic_id": "topic_umc",
        "category_id": "cat_foundries",
        "title": "UMC",
        "slug": "umc",
        "overview": "United Microelectronics Corporation is Taiwan's second foundry, focusing on mature nodes (28nm and above). UMC serves automotive, IoT, and industrial markets with reliable, cost-effective manufacturing.",
        "content_beginner": """UMC is Taiwan's second-largest chip manufacturer after TSMC.

**Key Facts:**
- Founded 1980 in Taiwan
- Focus on mature nodes (28nm+)
- Strong in specialty technologies
- Not competing at leading edge

**Technology Focus:**
- 28nm (most advanced)
- 40nm, 55nm, 90nm
- Embedded flash, BCD
- RF-SOI, HV processes

**Markets Served:**
- Automotive
- Industrial
- Consumer
- IoT
- Communication""",
        "content_advanced": """UMC differentiates through specialty processes and mature node focus.

**UMC Technology:**
| Node | Status | Features |
|------|--------|----------|
| 28nm | HVM | HPC, HPL, HPC+ |
| 40nm | HVM | LP, ULP |
| 55nm | HVM | eFlash, BCD |
| 90nm+ | HVM | Various |

**Specialty Platforms:**
- Embedded flash (eNVM)
- BCD (bipolar-CMOS-DMOS)
- RF-SOI
- High voltage
- SiGe BiCMOS

**Market Position:**
- ~7% foundry market
- Strong in automotive
- Cost-effective partner
- Taiwan + China + Singapore fabs""",
        "diagrams": [],
        "equations": [],
        "manufacturing_challenges": ["Cost competition", "Technology differentiation", "Capacity utilization"],
        "applications": ["Automotive MCU", "Display drivers", "Power management", "Industrial"],
        "advantages": ["Mature process expertise", "Cost competitive", "Specialty focus", "Reliability"],
        "limitations": ["No leading edge", "Limited growth ceiling", "Technology gap"],
        "related_topics": ["topic_tsmc", "topic_globalfoundries", "topic_automotive_chips"],
        "references": [],
        "difficulty": "beginner",
        "author": "system",
        "views": 0
    },
    {
        "topic_id": "topic_pmic",
        "category_id": "cat_applications",
        "title": "Power Management ICs",
        "slug": "power-management-ics",
        "overview": "PMICs regulate, distribute, and monitor power in electronic systems. They include DC-DC converters, LDOs, battery chargers, and power sequencers essential for mobile, automotive, and IoT applications.",
        "content_beginner": """PMICs manage all the power needs inside electronic devices.

**What PMICs Do:**
- Convert voltages (5V to 1V, etc.)
- Regulate voltage precisely
- Charge batteries
- Protect from faults
- Monitor power consumption

**Key Components:**
- **DC-DC Converter:** Efficient voltage conversion
- **LDO:** Low-noise linear regulator
- **Battery Charger:** Safely charges batteries
- **Load Switch:** Turns power on/off

**Why PMICs Matter:**
- Extend battery life
- Protect expensive chips
- Enable proper operation
- Required in every device""",
        "content_advanced": """PMIC design balances efficiency, accuracy, size, and cost.

**PMIC Architectures:**
| Type | Efficiency | Noise | Size |
|------|------------|-------|------|
| Buck DC-DC | 85-95% | Higher | Medium |
| Boost DC-DC | 80-90% | Higher | Medium |
| LDO | 60-90% | Lowest | Small |
| Charge pump | 80-95% | Medium | Small |

**Key Specifications:**
- Efficiency vs load current
- Output ripple/noise
- Line/load regulation
- Transient response
- Quiescent current

**Integration Trends:**
- Multiple rails in one IC
- Integrated FETs
- Digital control
- Adaptive voltage scaling
- PMICs in SoC/SiP""",
        "diagrams": [],
        "equations": [
            {"latex": "\\eta = \\frac{P_{out}}{P_{in}} \\times 100\\%", "description": "Power efficiency"},
            {"latex": "V_{out} = V_{in} \\times D", "description": "Buck converter (ideal)"}
        ],
        "manufacturing_challenges": ["Efficiency optimization", "EMI control", "Thermal management"],
        "applications": ["Mobile devices", "Automotive", "IoT", "Servers", "Wearables"],
        "advantages": ["Power efficiency", "Integration", "Protection features", "Flexibility"],
        "limitations": ["Heat generation", "Complexity", "EMI", "Cost of advanced features"],
        "related_topics": ["topic_power_mosfet", "topic_automotive_chips", "topic_iot_chips"],
        "references": [],
        "difficulty": "intermediate",
        "author": "system",
        "views": 0
    },
    {
        "topic_id": "topic_chiplet",
        "category_id": "cat_packaging",
        "title": "Chiplet Architecture",
        "slug": "chiplet-architecture",
        "overview": "Chiplets decompose large SoCs into smaller dies connected through advanced packaging. This improves yield, enables heterogeneous integration, and allows mixing different process nodes in one product.",
        "content_beginner": """Chiplets are small chip pieces that connect together to make bigger systems.

**Why Chiplets?**
- Big chips have low yield (expensive!)
- Smaller chips yield better
- Can mix different technologies
- Reuse chiplets across products

**How They Connect:**
- Silicon interposer (2.5D)
- Direct die-to-die bonding (3D)
- Organic substrate
- Standards like UCIe

**Examples:**
- AMD EPYC (CPU chiplets + I/O die)
- Apple M1 Ultra (2 dies connected)
- Intel Ponte Vecchio (47 tiles!)""",
        "content_advanced": """Chiplet architectures enable disaggregated SoC design.

**Chiplet Benefits:**
| Aspect | Monolithic | Chiplet |
|--------|------------|---------|
| Yield | Lower (large die) | Higher |
| Cost | High | Can be lower |
| Flexibility | Fixed | Configurable |
| Node mixing | No | Yes |
| Time to market | Longer | Shorter |

**Interconnect Options:**
- UCIe: Universal Chiplet Interconnect Express
- EMIB: Intel embedded bridge
- CoWoS: TSMC interposer
- Foveros: Intel 3D

**Design Challenges:**
- Partition strategy
- Interface standardization
- Known good die (KGD)
- Thermal management
- Test strategy""",
        "diagrams": [],
        "equations": [
            {"latex": "Yield_{system} = \\prod Yield_{chiplet}", "description": "System yield"},
            {"latex": "Cost = \\sum(Chiplet + Packaging)", "description": "Total cost"}
        ],
        "manufacturing_challenges": ["KGD testing", "Interconnect density", "Thermal", "Standards"],
        "applications": ["HPC", "Data center", "AI", "Consumer", "Automotive"],
        "advantages": ["Better yield economics", "Heterogeneous integration", "Design reuse", "Flexibility"],
        "limitations": ["Packaging complexity", "Interconnect overhead", "Testing", "Standards immaturity"],
        "related_topics": ["topic_cowos", "topic_hybrid_bonding", "topic_ai_chips"],
        "references": [],
        "difficulty": "intermediate",
        "author": "system",
        "views": 0
    }
]


def get_final_topics():
    """Return final topics to reach 100+ total"""
    return FINAL_TOPICS
