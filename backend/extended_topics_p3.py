"""
Extended Encyclopedia Topics - Part 3
Final batch to reach 100+ topics
Focus: Filling out all categories to depth
"""

EXTENDED_TOPICS_PART3 = [
    # ==================== MORE DEVICES ====================
    {
        "topic_id": "topic_planar_transistor",
        "category_id": "cat_devices",
        "title": "Planar Transistor",
        "slug": "planar-transistor",
        "overview": "Planar transistors were the dominant architecture from 1960s to 2011, with gate control over a flat channel surface. Short-channel effects limited scaling below 28nm, driving FinFET adoption.",
        "content_beginner": """Planar transistors are the classic flat transistor design used for decades.

**Structure:**
- Source and drain regions in the silicon
- Thin gate oxide on top
- Gate electrode controls channel
- Everything in one plane (flat)

**How It Works:**
- Gate voltage attracts/repels electrons
- Channel forms under the gate
- Current flows source to drain
- Works well for larger sizes

**Why We Moved On:**
- Below 28nm, control became poor
- Leakage current too high
- Needed 3D structure (FinFET)""",
        "content_advanced": """Planar scaling limits drove the transition to FinFET architecture.

**Scaling Challenges:**
| Parameter | 90nm | 45nm | 28nm |
|-----------|------|------|------|
| Lg (nm) | 50 | 25 | 20 |
| tox (nm) | 1.2 | 0.9 | 0.8 |
| Vth roll-off | Low | Medium | High |
| DIBL | <100mV | 100-150mV | >150mV |

**Short-Channel Effects:**
- Vth roll-off
- DIBL (drain-induced barrier lowering)
- Subthreshold swing degradation
- Hot carrier injection

**Final Planar Nodes:**
- Intel: 32nm (2010)
- TSMC: 28nm (2011)
- Samsung: 28nm (2011)""",
        "diagrams": [],
        "equations": [
            {"latex": "DIBL = \\frac{V_{th,low} - V_{th,high}}{V_{DD,high} - V_{DD,low}}", "description": "DIBL measurement"},
            {"latex": "I_{sub} \\propto e^{qV_{gs}/nkT}", "description": "Subthreshold current"}
        ],
        "manufacturing_challenges": ["Short-channel effects", "Leakage control", "Vth variability"],
        "applications": ["Legacy nodes", "Analog circuits", "Power devices", "Educational"],
        "advantages": ["Simple process", "Well understood", "Lower cost"],
        "limitations": ["Limited scaling", "Poor control at small sizes", "High leakage"],
        "related_topics": ["topic_finfet", "topic_mosfet_basics", "topic_gaafet"],
        "references": [],
        "difficulty": "beginner",
        "author": "system",
        "views": 0
    },
    {
        "topic_id": "topic_diode",
        "category_id": "cat_devices",
        "title": "Semiconductor Diodes",
        "slug": "semiconductor-diodes",
        "overview": "Diodes are two-terminal devices that conduct current in one direction. Types include PN junction, Schottky, Zener, and PIN diodes, each optimized for specific applications.",
        "content_beginner": """A diode is like a one-way valve for electricity.

**Basic Operation:**
- Forward bias: Current flows easily
- Reverse bias: Current blocked
- Uses PN junction physics

**Common Diode Types:**
- **PN Junction:** Basic rectification
- **Schottky:** Fast, low forward drop
- **Zener:** Voltage regulation
- **LED:** Light emission

**Uses:**
- Convert AC to DC (rectifiers)
- Protect circuits (clipping)
- Generate light (LEDs)
- Detect signals (RF)""",
        "content_advanced": """Diode characteristics vary significantly by structure and materials.

**Diode Comparison:**
| Type | Forward Drop | Speed | Reverse Recovery |
|------|-------------|-------|------------------|
| PN Si | 0.7V | Medium | 50-200ns |
| Schottky | 0.2-0.4V | Fast | <10ns |
| SiC Schottky | 0.8-1.5V | Very fast | <10ns |
| GaN | 0.5-1.0V | Very fast | <5ns |

**Key Parameters:**
- Forward voltage (Vf)
- Reverse leakage (Ir)
- Breakdown voltage (Vbr)
- Junction capacitance (Cj)
- Recovery time (trr)""",
        "diagrams": [],
        "equations": [
            {"latex": "I = I_s(e^{qV/nkT} - 1)", "description": "Diode equation"},
            {"latex": "C_j = \\frac{C_{j0}}{(1+V_r/V_{bi})^m}", "description": "Junction capacitance"}
        ],
        "manufacturing_challenges": ["Junction uniformity", "Breakdown control", "Leakage minimization"],
        "applications": ["Rectifiers", "ESD protection", "RF detectors", "LEDs", "Solar cells"],
        "advantages": ["Simple", "Reliable", "Low cost", "Wide variety"],
        "limitations": ["Forward drop", "Reverse recovery", "Temperature sensitivity"],
        "related_topics": ["topic_pn_junction", "topic_led", "topic_power_devices"],
        "references": [],
        "difficulty": "beginner",
        "author": "system",
        "views": 0
    },
    {
        "topic_id": "topic_power_mosfet",
        "category_id": "cat_devices",
        "title": "Power MOSFETs",
        "slug": "power-mosfets",
        "overview": "Power MOSFETs handle high voltages and currents for power conversion applications. Vertical structures like VDMOS and superjunction designs optimize the trade-off between on-resistance and breakdown voltage.",
        "content_beginner": """Power MOSFETs are heavy-duty transistors for controlling high power.

**Different from Logic MOSFETs:**
- Handle volts to hundreds of volts
- Carry amps to hundreds of amps
- Built vertically (current flows down)
- Focus on low resistance

**Key Types:**
- **VDMOS:** Standard vertical power
- **Trench:** Lower resistance
- **Superjunction:** High voltage + low Rds

**Applications:**
- Motor drives
- Power supplies
- Electric vehicles
- Solar inverters""",
        "content_advanced": """Power MOSFET architectures optimize the Ron × Area figure of merit.

**Technology Comparison:**
| Type | Voltage | Rsp (mΩ·cm²) | Speed |
|------|---------|--------------|-------|
| Planar VDMOS | 30-200V | 20-50 | Medium |
| Trench | 20-100V | 5-15 | Fast |
| Superjunction | 400-900V | 10-30 | Medium |
| GaN HEMT | 100-650V | 5-10 | Very fast |

**Key Parameters:**
- Rds(on): On-resistance
- BVdss: Breakdown voltage
- Qg: Gate charge
- Coss: Output capacitance

**Superjunction Principle:**
- Alternating n/p columns
- Charge balance for high BV
- Low on-resistance""",
        "diagrams": [],
        "equations": [
            {"latex": "R_{on} \\propto BV^{2.5}", "description": "Silicon limit"},
            {"latex": "FOM = R_{on} \\times Q_g", "description": "Figure of merit"}
        ],
        "manufacturing_challenges": ["Deep trench etch", "Charge balance", "Avalanche ruggedness"],
        "applications": ["Switch-mode power supplies", "Motor control", "EVs", "Solar"],
        "advantages": ["High efficiency", "Easy gate drive", "Fast switching"],
        "limitations": ["Body diode recovery", "Gate charge", "Package parasitics"],
        "related_topics": ["topic_sic", "topic_gan_power", "topic_automotive_chips"],
        "references": [],
        "difficulty": "intermediate",
        "author": "system",
        "views": 0
    },
    # ==================== MORE FOUNDRIES ====================
    {
        "topic_id": "topic_tsmc",
        "category_id": "cat_foundries",
        "title": "TSMC",
        "slug": "tsmc",
        "overview": "Taiwan Semiconductor Manufacturing Company is the world's largest foundry with over 50% market share. TSMC leads in advanced nodes, manufacturing chips for Apple, NVIDIA, AMD, and Qualcomm.",
        "content_beginner": """TSMC is the world's largest chip manufacturer for other companies.

**Key Facts:**
- Founded 1987 in Taiwan
- Invented the foundry business model
- Makes chips for Apple, NVIDIA, AMD, etc.
- Over 50% of global foundry market

**Technology Leadership:**
- First to 7nm, 5nm, 3nm
- Most EUV production capacity
- Industry-leading yields

**Why Companies Choose TSMC:**
- Best-in-class technology
- High yields
- Reliable delivery
- Massive capacity""",
        "content_advanced": """TSMC's technology and capacity leadership drives industry direction.

**Technology Roadmap:**
| Node | Production | Features |
|------|------------|----------|
| N5 | 2020 | Leading edge |
| N4 | 2022 | N5 enhanced |
| N3E | 2023 | FinFET final |
| N2 | 2025 | GAA transition |

**Market Position:**
- 56% foundry market share
- 90%+ advanced (<7nm) market
- Key customers: Apple, NVIDIA, AMD, Qualcomm

**Capacity:**
- ~2M 12-inch wafers/month
- Arizona fab: $40B investment
- Japan fab: Partnership with Sony

**Competitive Advantages:**
- Process technology lead
- Manufacturing excellence
- Customer ecosystem
- R&D investment (~$5B/year)""",
        "diagrams": [],
        "equations": [],
        "manufacturing_challenges": ["Geopolitical risk", "Capacity expansion", "Talent acquisition"],
        "applications": ["Mobile SoCs", "HPC", "AI", "Automotive", "IoT"],
        "advantages": ["Technology leadership", "Scale", "Ecosystem", "Reliability"],
        "limitations": ["Taiwan concentration", "Capacity constraints", "Premium pricing"],
        "related_topics": ["topic_samsung_foundry", "topic_intel_foundry", "topic_3nm"],
        "references": [],
        "difficulty": "beginner",
        "author": "system",
        "views": 0
    },
    {
        "topic_id": "topic_samsung_foundry",
        "category_id": "cat_foundries",
        "title": "Samsung Foundry",
        "slug": "samsung-foundry",
        "overview": "Samsung Foundry is the second-largest pure-play foundry, pioneering GAA transistors at 3nm. Samsung offers a complete semiconductor ecosystem from foundry to memory to packaging.",
        "content_beginner": """Samsung Foundry makes chips for other companies alongside TSMC.

**Key Facts:**
- Part of Samsung Electronics
- Second largest foundry
- First to make GAA transistors (2022)
- Strong memory expertise

**Technology:**
- 3nm GAA in production (2022)
- Compete with TSMC on advanced nodes
- Integrated device manufacturer (IDM)

**Customers:**
- Qualcomm (some products)
- Google Tensor chips
- Own Exynos processors
- Various automotive/IoT""",
        "content_advanced": """Samsung combines foundry with IDM capabilities.

**Technology Nodes:**
| Node | Status | Transistor |
|------|--------|------------|
| 7LPP | Production | FinFET+EUV |
| 5LPE | Production | FinFET |
| 4LPP | Production | FinFET |
| 3GAE | Production | GAA |
| 2nm | Development | GAA |

**Competitive Position:**
- ~15% foundry market share
- First GAA production (3nm)
- Strong packaging capability
- Memory + foundry synergy

**Challenges:**
- Yield ramp vs TSMC
- Customer acquisition
- Technology gap at leading edge

**Differentiators:**
- GAA technology lead
- Memory integration
- Korean government support
- Complete solution provider""",
        "diagrams": [],
        "equations": [],
        "manufacturing_challenges": ["Yield improvement", "Customer diversification", "Technology catch-up"],
        "applications": ["Mobile", "Automotive", "IoT", "HPC"],
        "advantages": ["GAA first", "Integrated ecosystem", "Memory synergy", "Capacity"],
        "limitations": ["Yield concerns", "Market share gap", "Customer trust"],
        "related_topics": ["topic_tsmc", "topic_gaafet", "topic_samsung_sf2"],
        "references": [],
        "difficulty": "beginner",
        "author": "system",
        "views": 0
    },
    # ==================== MORE TESTING ====================
    {
        "topic_id": "topic_failure_analysis",
        "category_id": "cat_testing",
        "title": "Failure Analysis",
        "slug": "failure-analysis",
        "overview": "Failure analysis identifies root causes of semiconductor defects using physical, electrical, and chemical techniques. FA is essential for yield improvement, reliability qualification, and customer returns.",
        "content_beginner": """Failure analysis finds out why chips fail - like detective work for electronics.

**Why FA is Important:**
- Find why chips fail
- Improve manufacturing
- Qualify new processes
- Solve customer problems

**Analysis Techniques:**

**Electrical:**
- Find where defect is located
- Measure what's wrong electrically

**Physical:**
- Look inside the chip
- Use microscopes, X-rays
- Sometimes destroy the sample

**Common Tools:**
- Electron microscope (SEM)
- Focused ion beam (FIB)
- X-ray imaging
- Emission microscopy""",
        "content_advanced": """FA combines multiple techniques for comprehensive defect identification.

**FA Workflow:**
| Stage | Technique | Purpose |
|-------|-----------|---------|
| Fault isolation | OBIRCH, PEM | Locate defect |
| Deprocessing | Chemical, RIE | Access layer |
| Imaging | SEM, TEM | See defect |
| Analysis | EDS, SIMS | Composition |

**Key Techniques:**
- Photon emission microscopy (PEM)
- Laser voltage probing (LVP)
- Electron beam absorbed current (EBAC)
- Atom probe tomography (APT)
- Transmission electron microscopy (TEM)

**Sample Preparation:**
- Mechanical polishing
- FIB cross-section
- Delayering (wet/dry)
- TEM lamella preparation""",
        "diagrams": [],
        "equations": [],
        "manufacturing_challenges": ["Sample preparation", "Non-destructive analysis", "Time pressure", "Smaller features"],
        "applications": ["Yield improvement", "Reliability", "Customer returns", "Process development"],
        "advantages": ["Root cause identification", "Process feedback", "Customer confidence"],
        "limitations": ["Time consuming", "Destructive (often)", "Equipment cost", "Expertise required"],
        "related_topics": ["topic_wafer_inspection", "topic_yield_management", "topic_reliability"],
        "references": [],
        "difficulty": "intermediate",
        "author": "system",
        "views": 0
    },
    {
        "topic_id": "topic_burn_in",
        "category_id": "cat_testing",
        "title": "Burn-In Testing",
        "slug": "burn-in-testing",
        "overview": "Burn-in accelerates early-life failures by stressing devices at elevated temperature and voltage. It screens out infant mortality defects that would fail early in customer applications.",
        "content_beginner": """Burn-in stresses chips to find weak ones before shipping to customers.

**Why Burn-In?**
- Some chips fail early (infant mortality)
- Stress at high temp/voltage accelerates failures
- Weak chips fail during burn-in, not at customer

**How It Works:**
1. Put chips in burn-in oven
2. Apply high voltage and temperature
3. Run for hours to days
4. Test again - failed chips discarded

**Conditions:**
- Temperature: 85-150°C
- Voltage: 10-20% above normal
- Time: 24-168 hours typical""",
        "content_advanced": """Burn-in parameters are optimized for defect acceleration without causing wearout.

**Burn-In Types:**
| Type | Temperature | Voltage | Duration |
|------|-------------|---------|----------|
| Static | 125°C | Vmax | 48-168h |
| Dynamic | 125°C | Vmax+10% | 24-48h |
| HTOL (qual) | 125°C | Vmax | 1000h |

**Acceleration Factors:**
- Arrhenius (temperature)
- Eyring (voltage)
- Combined stress models

**Acceleration Equations:**
- AF_T = exp(Ea/k × (1/T_use - 1/T_stress))
- AF_V = (V_stress/V_use)^n

**Modern Approaches:**
- Statistical burn-in (sample-based)
- Known good die (KGD) for MCM
- In-system burn-in
- Virtual burn-in (data-driven)""",
        "diagrams": [],
        "equations": [
            {"latex": "AF = e^{E_a/k(1/T_{use} - 1/T_{stress})}", "description": "Temperature acceleration"},
            {"latex": "MTTF = t_{BI} \\times AF", "description": "Projected field life"}
        ],
        "manufacturing_challenges": ["Cost vs coverage", "Over-stress risk", "Throughput", "Board design"],
        "applications": ["Automotive qualification", "High-reliability", "Military/aerospace", "Data center"],
        "advantages": ["Screens early failures", "Increases reliability", "Customer confidence"],
        "limitations": ["Cost", "Time", "May cause wearout", "Not all defect types"],
        "related_topics": ["topic_reliability", "topic_ate", "topic_automotive_chips"],
        "references": [],
        "difficulty": "intermediate",
        "author": "system",
        "views": 0
    },
    # ==================== MORE APPLICATIONS ====================
    {
        "topic_id": "topic_iot_chips",
        "category_id": "cat_applications",
        "title": "IoT Semiconductors",
        "slug": "iot-semiconductors",
        "overview": "IoT chips prioritize ultra-low power, wireless connectivity, and sensor integration. They enable billions of connected devices from smart homes to industrial sensors to wearables.",
        "content_beginner": """IoT chips power the Internet of Things - billions of connected devices.

**What Makes IoT Chips Special:**
- Ultra-low power (battery life in years)
- Built-in wireless (WiFi, Bluetooth, etc.)
- Small and cheap
- Sensor integration

**Key Features:**
- **MCU:** Runs the device software
- **Radio:** Connects to network
- **Sensors:** Measures environment
- **Power management:** Extends battery

**Applications:**
- Smart home devices
- Wearables and fitness trackers
- Industrial sensors
- Smart agriculture
- Asset tracking""",
        "content_advanced": """IoT semiconductor architecture balances power, performance, and connectivity.

**IoT SoC Components:**
| Block | Power Budget | Function |
|-------|-------------|----------|
| MCU core | 10-50µW/MHz | Processing |
| Radio | 5-20mA (active) | Connectivity |
| Sensors | 1-100µW | Measurement |
| PMU | 90%+ efficiency | Power |

**Wireless Options:**
- BLE: 1-2mA, 1Mbps, 100m
- WiFi: 100-300mA, 1Gbps, 100m
- LoRa: 20-40mA, 50kbps, 10km
- NB-IoT: 50-100mA, cellular

**Low Power Techniques:**
- Subthreshold operation
- Duty cycling
- Wake-on-event
- Energy harvesting integration""",
        "diagrams": [],
        "equations": [
            {"latex": "Battery\\_Life = \\frac{Capacity}{I_{avg}}", "description": "Battery life estimate"},
            {"latex": "P_{avg} = D \\times P_{active} + (1-D) \\times P_{sleep}", "description": "Average power with duty cycling"}
        ],
        "manufacturing_challenges": ["Cost optimization", "Integration density", "Power optimization"],
        "applications": ["Smart home", "Wearables", "Industrial IoT", "Agriculture", "Healthcare"],
        "advantages": ["Low power", "Low cost", "High integration", "Wireless"],
        "limitations": ["Limited compute", "Security challenges", "Fragmented standards"],
        "related_topics": ["topic_mcu", "topic_wireless", "topic_power_management"],
        "references": [],
        "difficulty": "beginner",
        "author": "system",
        "views": 0
    },
    {
        "topic_id": "topic_rf_chips",
        "category_id": "cat_applications",
        "title": "RF/Wireless Semiconductors",
        "slug": "rf-wireless-semiconductors",
        "overview": "RF semiconductors enable wireless communication from 5G and WiFi to satellite links. They include power amplifiers, low-noise amplifiers, filters, and integrated RF front-ends.",
        "content_beginner": """RF chips enable all wireless communication - phones, WiFi, satellites.

**What RF Chips Do:**
- Amplify weak signals (LNA)
- Boost signals for transmission (PA)
- Filter unwanted frequencies
- Convert between RF and digital

**Key Components:**
- **Power Amplifier (PA):** Boosts transmit signal
- **Low Noise Amplifier (LNA):** Amplifies received signal
- **Filter:** Selects wanted frequencies
- **Mixer:** Changes frequency

**Technologies:**
- GaAs: Traditional RF
- GaN: High power, 5G
- RF-SOI: Switches, tuners
- SiGe: High frequency""",
        "content_advanced": """RF semiconductor selection depends on frequency, power, and efficiency requirements.

**Technology Comparison:**
| Tech | Frequency | Power | Efficiency |
|------|-----------|-------|------------|
| Si CMOS | <6GHz | Low | Medium |
| RF-SOI | <10GHz | Medium | Good |
| SiGe BiCMOS | <100GHz | Medium | Good |
| GaAs pHEMT | <100GHz | High | Best |
| GaN HEMT | <40GHz | Highest | Good |

**Key Specifications:**
- Psat: Saturated output power
- PAE: Power added efficiency
- NF: Noise figure
- IP3: Linearity
- Gain: Signal amplification

**5G Requirements:**
- Sub-6GHz: GaAs/GaN PAs
- mmWave: GaAs/SiGe/CMOS
- Massive MIMO: Integrated solutions
- Beamforming: Phase shifters""",
        "diagrams": [],
        "equations": [
            {"latex": "PAE = \\frac{P_{out} - P_{in}}{P_{DC}}", "description": "Power added efficiency"},
            {"latex": "NF = 10\\log\\frac{SNR_{in}}{SNR_{out}}", "description": "Noise figure"}
        ],
        "manufacturing_challenges": ["Yield at high frequency", "Integration", "Package parasitics"],
        "applications": ["5G", "WiFi", "Satellite", "Radar", "Automotive"],
        "advantages": ["Wireless enabling", "High integration possible", "Performance scaling"],
        "limitations": ["Power consumption", "Heat generation", "Cost of advanced materials"],
        "related_topics": ["topic_iii_v", "topic_gan_power", "topic_packaging"],
        "references": [],
        "difficulty": "intermediate",
        "author": "system",
        "views": 0
    },
    {
        "topic_id": "topic_fpga",
        "category_id": "cat_applications",
        "title": "FPGAs",
        "slug": "fpgas",
        "overview": "Field-Programmable Gate Arrays are reprogrammable logic devices offering hardware flexibility. FPGAs excel in prototyping, low-volume production, and applications requiring hardware adaptability.",
        "content_beginner": """FPGAs are chips you can reprogram to do different things.

**What Makes FPGAs Special:**
- Program hardware behavior with software
- Change function after manufacturing
- Faster than CPUs for parallel tasks
- More flexible than fixed chips (ASICs)

**FPGA Structure:**
- Look-up tables (LUTs): Logic blocks
- Flip-flops: Store data
- Routing: Connect blocks
- I/O blocks: External connections

**Use Cases:**
- Prototyping before ASIC
- Low-volume products
- Hardware acceleration
- Aerospace/defense
- Data centers""",
        "content_advanced": """Modern FPGAs integrate hard IP blocks with programmable fabric.

**FPGA Architecture:**
| Block Type | Function | Example |
|------------|----------|---------|
| CLB/LAB | Logic | 6-input LUT |
| DSP | Math | Multiply-accumulate |
| BRAM | Memory | 18/36Kb blocks |
| Transceiver | I/O | 28Gbps+ SerDes |
| Hard IP | Fixed | PCIe, DDR, CPU |

**Technology Trends:**
- 3D integration with HBM
- AI inference acceleration
- Chiplet architectures
- 7nm and 5nm nodes

**Programming Flow:**
1. RTL design (Verilog/VHDL)
2. Synthesis to FPGA primitives
3. Place and route
4. Bitstream generation
5. Device configuration""",
        "diagrams": [],
        "equations": [
            {"latex": "LUT = 2^n\\ SRAM\\ bits", "description": "LUT size for n inputs"},
            {"latex": "Perf/W_{FPGA} > Perf/W_{CPU}", "description": "Efficiency advantage"}
        ],
        "manufacturing_challenges": ["Utilization optimization", "Timing closure", "Power management"],
        "applications": ["Prototyping", "Data center acceleration", "Aerospace", "Automotive ADAS", "5G"],
        "advantages": ["Reprogrammable", "Time to market", "Parallel processing", "Hardware flexibility"],
        "limitations": ["Higher cost than ASIC at volume", "Lower performance than ASIC", "Power", "Design complexity"],
        "related_topics": ["topic_rtl_design", "topic_ai_chips", "topic_asic"],
        "references": [],
        "difficulty": "intermediate",
        "author": "system",
        "views": 0
    },
    {
        "topic_id": "topic_image_sensors",
        "category_id": "cat_applications",
        "title": "Image Sensors",
        "slug": "image-sensors",
        "overview": "CMOS image sensors convert light to electrical signals for cameras in smartphones, automotive, and security applications. BSI technology and stacked architectures enable high resolution and performance.",
        "content_beginner": """Image sensors are the 'eyes' of digital cameras - they capture light and create images.

**How They Work:**
1. Light hits sensor pixels
2. Photons create electrical charge
3. Charge is read out row by row
4. Signal is digitized to create image

**Key Types:**
- **CCD:** Older technology, still used in specialized applications
- **CMOS:** Dominant technology today

**Important Specs:**
- Resolution: Number of pixels (megapixels)
- Pixel size: Smaller = higher resolution
- Sensitivity: Performance in low light
- Frame rate: Speed of capture

**Applications:**
- Smartphones (main market)
- Automotive (ADAS, backup cameras)
- Security cameras
- Medical imaging""",
        "content_advanced": """CMOS image sensor technology has advanced dramatically with stacking and BSI.

**Technology Evolution:**
| Feature | Early CMOS | Modern CIS |
|---------|------------|------------|
| Illumination | FSI | BSI |
| Pixel size | 5.6µm | 0.56µm |
| Stacking | No | 2-3 layer |
| Architecture | Rolling shutter | Global shutter |

**Key Technologies:**
- BSI (back-side illumination): Higher QE
- Stacked sensors: Pixel + logic + memory
- Deep trench isolation (DTI)
- Color filter array optimization

**Performance Metrics:**
- QE: Quantum efficiency
- SNR: Signal-to-noise ratio
- DR: Dynamic range
- Dark current
- FWC: Full well capacity""",
        "diagrams": [],
        "equations": [
            {"latex": "QE = \\frac{electrons}{photons}", "description": "Quantum efficiency"},
            {"latex": "SNR = \\frac{Signal}{\\sqrt{Signal + Noise^2}}", "description": "Signal to noise ratio"}
        ],
        "manufacturing_challenges": ["BSI processing", "Stacking alignment", "Defect control", "Color filter uniformity"],
        "applications": ["Smartphones", "Automotive", "Security", "Medical", "Industrial"],
        "advantages": ["High integration", "Low power", "High resolution", "Fast readout"],
        "limitations": ["Rolling shutter artifacts", "Low light performance", "Heat sensitivity"],
        "related_topics": ["topic_tsv", "topic_hybrid_bonding", "topic_automotive_chips"],
        "references": [],
        "difficulty": "intermediate",
        "author": "system",
        "views": 0
    },
    # ==================== MORE MANUFACTURING ====================
    {
        "topic_id": "topic_photomask",
        "category_id": "cat_manufacturing",
        "title": "Photomask Technology",
        "slug": "photomask-technology",
        "overview": "Photomasks transfer circuit patterns to wafers during lithography. EUV masks use reflective multilayer structures, while DUV masks use transmission through chrome patterns on quartz.",
        "content_beginner": """Photomasks are like stencils for printing chip patterns onto wafers.

**How Masks Work:**
- Light shines through mask
- Pattern blocks/passes light
- Lens projects pattern onto wafer
- Photoresist captures the image

**Mask Types:**
- **Binary:** Simple on/off pattern
- **Phase shift:** Uses light interference
- **EUV:** Reflective (not transmissive)

**Why Masks are Critical:**
- One mask makes millions of chips
- Must be nearly perfect
- Very expensive to make
- Any defect copies to all chips""",
        "content_advanced": """Advanced masks enable resolution enhancement and defect-free patterning.

**Mask Technologies:**
| Type | Light | Structure | Application |
|------|-------|-----------|-------------|
| Binary | DUV | Cr on quartz | Legacy |
| AttPSM | DUV | MoSi phase shift | Critical layers |
| AltPSM | DUV | Etched quartz | Dense lines |
| EUV | 13.5nm | Mo/Si multilayer | Leading edge |

**EUV Mask Structure:**
- Low thermal expansion substrate
- Mo/Si multilayer (40 pairs)
- Ru capping layer
- TaBN absorber pattern
- Pellicle (membrane protection)

**Key Specifications:**
- CD uniformity: <1nm 3σ
- Registration: <2nm
- Defect density: Zero printable
- Reflectivity: >65% (EUV)""",
        "diagrams": [],
        "equations": [
            {"latex": "Resolution = k_1 \\frac{\\lambda}{NA}", "description": "Optical resolution"},
            {"latex": "MEEF = \\frac{\\Delta CD_{wafer}}{\\Delta CD_{mask} \\times M}", "description": "Mask error enhancement factor"}
        ],
        "manufacturing_challenges": ["Defect-free fabrication", "EUV pellicle", "Repair capability", "Cost"],
        "applications": ["All lithography steps", "Logic/memory manufacturing", "Advanced packaging"],
        "advantages": ["High fidelity", "High throughput production", "Mature technology"],
        "limitations": ["Very expensive", "Long lead time", "No defects allowed"],
        "related_topics": ["topic_euv_lithography", "topic_duv_lithography", "topic_opc"],
        "references": [],
        "difficulty": "intermediate",
        "author": "system",
        "views": 0
    },
    {
        "topic_id": "topic_annealing",
        "category_id": "cat_manufacturing",
        "title": "Thermal Annealing",
        "slug": "thermal-annealing",
        "overview": "Annealing uses high temperatures to activate dopants, repair crystal damage, and densify films. Advanced techniques include spike, millisecond laser, and flash annealing for ultra-shallow junctions.",
        "content_beginner": """Annealing heats wafers to fix damage and activate dopants.

**Why Annealing is Needed:**
- Ion implantation damages crystal
- Dopants need activation to work
- Films need densification
- Stress needs relief

**Types of Annealing:**
- **Furnace:** Slow, uniform (hours)
- **RTP:** Rapid thermal (seconds)
- **Spike:** Very short peak (milliseconds)
- **Laser:** Ultra-fast (microseconds)

**Key Effects:**
- Repair crystal damage
- Activate dopants electrically
- Control dopant diffusion
- Reduce film stress""",
        "content_advanced": """Anneal optimization balances activation, diffusion, and damage repair.

**Anneal Techniques:**
| Type | Time | Temp | Diffusion |
|------|------|------|-----------|
| Furnace | Hours | 900-1100°C | High |
| RTP | 1-60s | 1000-1100°C | Medium |
| Spike | 1-5ms | 1050-1100°C | Low |
| Laser | 0.1-1ms | >1200°C | Minimal |
| Flash | 0.1-1ms | >1200°C | Minimal |

**Key Parameters:**
- Peak temperature
- Time at temperature
- Ramp rate
- Ambient (N2, O2, etc.)

**Advanced Applications:**
- USJ formation
- SiGe strain preservation
- High-K crystallization
- Silicide formation""",
        "diagrams": [],
        "equations": [
            {"latex": "D = D_0 e^{-E_a/kT}", "description": "Diffusion coefficient"},
            {"latex": "x_j = 2\\sqrt{Dt}", "description": "Junction depth from diffusion"}
        ],
        "manufacturing_challenges": ["Activation vs diffusion", "Temperature uniformity", "Slip/warpage", "Pattern effects"],
        "applications": ["Dopant activation", "Damage repair", "Silicidation", "Film densification"],
        "advantages": ["Essential for devices", "Well controlled", "Multiple techniques available"],
        "limitations": ["Diffusion trade-off", "Thermal budget limits", "Equipment cost"],
        "related_topics": ["topic_ion_implantation", "topic_finfet", "topic_gaafet"],
        "references": [],
        "difficulty": "intermediate",
        "author": "system",
        "views": 0
    },
    {
        "topic_id": "topic_defect_inspection",
        "category_id": "cat_manufacturing",
        "title": "Defect Inspection Technology",
        "slug": "defect-inspection-technology",
        "overview": "Inline defect inspection detects particles, pattern defects, and process excursions during manufacturing. Optical brightfield/darkfield and e-beam systems provide complementary capabilities.",
        "content_beginner": """Defect inspection finds tiny problems on wafers during manufacturing.

**Why Inspection Matters:**
- Defects kill chip yield
- Early detection saves money
- Helps fix process problems
- Required for quality control

**Inspection Methods:**

**Optical (Light-based):**
- Fast - can inspect whole wafers
- Finds particles and big defects
- Limited by light wavelength

**E-beam (Electron-based):**
- Can see much smaller defects
- Very slow - samples only
- Finds electrical defects too

**What Gets Inspected:**
- After each major process step
- Critical layers get more inspection
- Statistical sampling for production""",
        "content_advanced": """Advanced inspection combines multiple modalities for comprehensive defect detection.

**Inspection Technologies:**
| Type | Resolution | Throughput | Use |
|------|------------|------------|-----|
| Brightfield | ~30nm | 100 wph | Patterned |
| Darkfield | ~20nm | 50 wph | Particles |
| E-beam (single) | ~5nm | <1 wph | Sampling |
| E-beam (multi) | ~5nm | 5-10 wph | Advanced |

**Defect Classification:**
- DOI: Defect of interest (real)
- Nuisance: Not yield-limiting
- Systematic: Process-related
- Random: Particles, contamination

**Advanced Capabilities:**
- Design-based binning
- Defect source analysis
- Machine learning classification
- Hot lot monitoring""",
        "diagrams": [],
        "equations": [
            {"latex": "Capture\\_Rate = \\frac{DOI\\_found}{DOI\\_total}", "description": "Detection capability"},
            {"latex": "D_0 = \\frac{Defects}{Area}", "description": "Defect density"}
        ],
        "manufacturing_challenges": ["Nuisance suppression", "Throughput vs sensitivity", "3D structure inspection"],
        "applications": ["Yield ramp", "Process monitoring", "Excursion detection", "Failure analysis"],
        "advantages": ["Early defect detection", "Process feedback", "Quality assurance"],
        "limitations": ["Cannot see all defect types", "Throughput limits", "Tool cost"],
        "related_topics": ["topic_wafer_inspection", "topic_yield_management", "topic_metrology"],
        "references": [],
        "difficulty": "intermediate",
        "author": "system",
        "views": 0
    },
    # ==================== MORE RELIABILITY ====================
    {
        "topic_id": "topic_tddb",
        "category_id": "cat_reliability",
        "title": "Time-Dependent Dielectric Breakdown",
        "slug": "tddb",
        "overview": "TDDB describes the gradual degradation and eventual breakdown of gate and interconnect dielectrics under electrical stress. It's a key reliability concern for thin oxides and low-K materials.",
        "content_beginner": """TDDB is when thin insulating layers slowly fail over time.

**What Happens:**
- Electric field stresses the insulator
- Small defects (traps) form over time
- Defects accumulate and connect
- Eventually creates a short circuit

**Where It Matters:**
- Gate oxide in transistors
- Low-K dielectrics between wires
- Capacitor dielectrics

**Why It's Important:**
- Chips must last 10+ years
- Can't directly test that long
- Use accelerated testing
- Models predict field lifetime""",
        "content_advanced": """TDDB models enable lifetime prediction from accelerated stress data.

**TDDB Models:**
| Model | Field Accel. | Application |
|-------|-------------|-------------|
| E-model | exp(-γE) | Thermal SiO2 |
| 1/E-model | exp(G/E) | Thin oxides |
| √E-model | exp(-√E) | High-K |
| Power law | V^(-n) | Low-K |

**Key Parameters:**
- Time to breakdown (t_BD)
- Charge to breakdown (Q_BD)
- Field acceleration factor
- Temperature acceleration (Ea)

**Weibull Analysis:**
- Distribution of failure times
- β (shape): Failure mode
- η (scale): Characteristic life
- t10: 10% failure time

**Testing Conditions:**
- Constant voltage stress (CVS)
- Ramped voltage stress (RVS)
- Temperature: 25-150°C
- Field: 8-15 MV/cm""",
        "diagrams": [],
        "equations": [
            {"latex": "t_{BD} = A e^{-\\gamma E} e^{E_a/kT}", "description": "E-model lifetime"},
            {"latex": "F(t) = 1 - e^{-(t/\\eta)^\\beta}", "description": "Weibull distribution"}
        ],
        "manufacturing_challenges": ["Defect density reduction", "Process control", "Testing time"],
        "applications": ["Gate oxide qualification", "Low-K reliability", "Capacitor lifetime"],
        "advantages": ["Predictive models exist", "Accelerated testing works", "Well understood"],
        "limitations": ["Extrinsic defects", "Model extrapolation", "New materials uncertainty"],
        "related_topics": ["topic_high_k", "topic_low_k", "topic_electromigration"],
        "references": [],
        "difficulty": "advanced",
        "author": "system",
        "views": 0
    },
    {
        "topic_id": "topic_nbti",
        "category_id": "cat_reliability",
        "title": "Bias Temperature Instability",
        "slug": "bias-temperature-instability",
        "overview": "BTI causes threshold voltage shifts in MOSFETs under bias stress, with NBTI affecting PMOS and PBTI affecting NMOS with high-K. It's a major reliability concern for circuit aging.",
        "content_beginner": """BTI makes transistors slowly change their behavior over time.

**What Happens:**
- Transistor under bias and heat
- Chemical reactions at interface
- Threshold voltage shifts
- Transistor becomes slower

**Two Main Types:**
- **NBTI:** Affects PMOS transistors
- **PBTI:** Affects NMOS with high-K

**Why It Matters:**
- Circuits slow down over time
- Can cause timing failures
- Must be accounted in design
- Part of device qualification""",
        "content_advanced": """BTI degradation involves complex physics at the oxide/silicon interface.

**BTI Mechanisms:**
| Effect | Cause | Recovery |
|--------|-------|----------|
| Interface traps | Si-H bond breaking | Partial |
| Oxide charge | Hole trapping | Full |
| Border traps | Near-interface | Partial |

**NBTI vs PBTI:**
- NBTI: Negative gate bias on PMOS
- PBTI: Positive gate bias on NMOS
- High-K makes PBTI significant
- Different recovery behavior

**Modeling Approaches:**
- Reaction-diffusion (R-D)
- Atomistic models
- Compact models for design
- AC vs DC stress factors

**Design Implications:**
- Vth shift budgets
- Aging-aware timing analysis
- Guard-banding
- Reliability circuits""",
        "diagrams": [],
        "equations": [
            {"latex": "\\Delta V_{th} = A t^n e^{E_a/kT}", "description": "Power law degradation"},
            {"latex": "Lifetime = t_0 (\\Delta V_{th,crit}/A)^{1/n}", "description": "BTI lifetime"}
        ],
        "manufacturing_challenges": ["Interface quality", "Process optimization", "Testing correlation"],
        "applications": ["Transistor qualification", "Circuit aging", "Reliability prediction"],
        "advantages": ["Well-characterized", "Models exist", "Can be designed around"],
        "limitations": ["Complex physics", "Recovery complicates testing", "Scaling challenges"],
        "related_topics": ["topic_high_k", "topic_finfet", "topic_reliability"],
        "references": [],
        "difficulty": "advanced",
        "author": "system",
        "views": 0
    },
    # ==================== MORE PACKAGING ====================
    {
        "topic_id": "topic_underfill",
        "category_id": "cat_packaging",
        "title": "Underfill Technology",
        "slug": "underfill-technology",
        "overview": "Underfill is an epoxy material dispensed between flip chip dies and substrates. It redistributes thermal and mechanical stress, dramatically improving solder joint reliability.",
        "content_beginner": """Underfill is the glue that protects the connections under flip chips.

**Why Underfill is Needed:**
- Chip and substrate expand differently with heat
- Without underfill, solder joints crack
- Underfill spreads the stress
- Dramatically improves reliability

**How It Works:**
1. Dispense liquid epoxy at chip edge
2. Capillary action pulls it under chip
3. Heat to cure (harden)
4. Now mechanically protected

**Types:**
- **Capillary:** Flows after chip attach
- **No-flow:** Applied before chip placement
- **Molded:** Wafer-level or mass-produced""",
        "content_advanced": """Underfill material selection balances flow, adhesion, and CTE matching.

**Underfill Properties:**
| Property | Requirement | Impact |
|----------|-------------|--------|
| Viscosity | 5-50 Pa·s | Flow |
| CTE | 20-40 ppm/°C | Stress |
| Tg | >150°C | High temp |
| Filler | 60-70% | CTE match |
| Modulus | 5-10 GPa | Compliance |

**Process Considerations:**
- Dispense pattern (L, U, etc.)
- Flow time vs temperature
- Void formation
- Cure profile

**Reliability Impact:**
- >10x fatigue life improvement
- Thermal cycle performance
- Drop test survival
- Corner/edge stress distribution""",
        "diagrams": [],
        "equations": [
            {"latex": "\\sigma = E \\alpha \\Delta T", "description": "Thermal stress"},
            {"latex": "Life \\propto \\frac{1}{\\Delta \\gamma^n}", "description": "Fatigue life vs strain"}
        ],
        "manufacturing_challenges": ["Void-free fill", "Cure control", "Rework difficulty", "Fine pitch flow"],
        "applications": ["Flip chip", "BGA", "CSP", "Advanced packaging"],
        "advantages": ["Major reliability improvement", "Mature technology", "Cost-effective"],
        "limitations": ["Adds process step", "Rework difficult", "Fine pitch challenges"],
        "related_topics": ["topic_flip_chip", "topic_reliability", "topic_packaging"],
        "references": [],
        "difficulty": "intermediate",
        "author": "system",
        "views": 0
    },
    {
        "topic_id": "topic_lead_frame",
        "category_id": "cat_packaging",
        "title": "Lead Frame Packages",
        "slug": "lead-frame-packages",
        "overview": "Lead frame packages use metal frames for die attachment and wire bonding, then encapsulate in molding compound. Common types include QFP, QFN, SOIC, offering low cost for consumer and automotive applications.",
        "content_beginner": """Lead frame packages are the classic, low-cost way to package chips.

**Package Structure:**
- Metal lead frame (copper alloy)
- Die attached to die pad
- Wire bonds to leads
- Molding compound encapsulation

**Common Types:**
- **QFP:** Quad Flat Pack (leads on all sides)
- **QFN:** Quad Flat No-lead (pads underneath)
- **SOIC:** Small Outline IC (leads on two sides)

**Advantages:**
- Very low cost
- High volume production
- Proven reliability
- Automotive qualified

**Where Used:**
- Consumer electronics
- Automotive
- Industrial
- IoT devices""",
        "content_advanced": """Lead frame evolution includes exposed pad and multi-row designs.

**Package Comparison:**
| Type | Lead Count | Pitch | Thermal |
|------|------------|-------|---------|
| SOIC | 8-28 | 1.27mm | Poor |
| QFP | 44-256 | 0.4-0.65mm | Medium |
| QFN | 8-100 | 0.4-0.5mm | Good |
| DFN | 6-14 | 0.5mm | Good |

**Design Features:**
- Exposed die pad (thermal)
- Half-etched leads
- Multi-row QFN
- Wettable flanks (optical inspection)

**Manufacturing Flow:**
1. Lead frame strip fabrication
2. Die attach (epoxy/solder)
3. Wire bonding
4. Molding
5. Plating
6. Trim and form
7. Singulation""",
        "diagrams": [],
        "equations": [
            {"latex": "R_{\\theta JA} = R_{JC} + R_{CA}", "description": "Thermal resistance"},
            {"latex": "Cost \\propto \\frac{1}{UPH \\times Yield}", "description": "Package cost drivers"}
        ],
        "manufacturing_challenges": ["Lead coplanarity", "Wire bond coverage", "Mold void", "Warpage"],
        "applications": ["Consumer", "Automotive", "Industrial", "IoT", "Power"],
        "advantages": ["Very low cost", "High volume", "Proven reliability", "Multiple options"],
        "limitations": ["Limited I/O", "Higher inductance", "Size constraints"],
        "related_topics": ["topic_wire_bonding", "topic_packaging", "topic_automotive_chips"],
        "references": [],
        "difficulty": "beginner",
        "author": "system",
        "views": 0
    }
]


def get_extended_topics_part3():
    """Return extended topics part 3 for encyclopedia expansion to 100+"""
    return EXTENDED_TOPICS_PART3
