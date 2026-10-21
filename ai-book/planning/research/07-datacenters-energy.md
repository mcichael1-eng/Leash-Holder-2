# 07 — Data Centers, Energy, and the Economics of AI Infrastructure

Research notes for *Everything About AI: From Zero to the Frontier*. Status as of **October 21, 2026**.

**How to read the confidence tags in this file**

- **[V]**: verified in this research session by fetching the source page (company blog, SEC filing, official statistics, earnings transcript, or a dated tracker).
- **[R]**: reported by secondary coverage, trackers, or Wikipedia, which cite news reports. It's probably right, but re-check it before printing.
- **[M]**: a figure from a well-known published report (IEA, LBNL, EPRI, PJM, Uptime) that I didn't re-fetch this session because the site blocked automated access. These are long-standing, widely cited numbers, but re-verify the exact wording.

The web-search budget for this session ran out partway through. Later checks used direct fetches of known URLs. Anything not tagged is general engineering knowledge and doesn't change from year to year: how transformers work, what PUE means, and so on.

---

## 1. Topic map (teaching order: simplest to most advanced)

### Part A — Foundations: electricity, heat and "compute" as physical things

1. **AI runs on physical machines.** Start from the reader's experience: a chatbot answer is produced by chips in a building somewhere, and those chips draw electricity and make heat. One image anchors this: your phone sends text to a building the size of several football fields.
2. **Power vs. energy.** Watts measure a *rate*, like speed. Watt-hours measure an *amount*, like distance. Use a 10 W LED bulb left on for 10 hours (= 100 Wh) before introducing kW, MW, GW and kWh, MWh, GWh, TWh.
3. **The ladder of scale.** Phone charger (~20 W) → hair dryer (~1.5 kW) → US home average draw (~1.2 kW) → one AI GPU with its share of the building (~1–2 kW) → one AI rack (~130 kW) → a large data hall (~30–50 MW) → an AI campus (1–5 GW) → a mid-size country. Have the reader place each item on a log scale.
4. **Capacity vs. consumption.** A "1 GW data center" is a nameplate *maximum*. Actual energy used depends on how hard it runs (utilization). For example, 1 GW × 8,760 h = 8.76 TWh per year if it ran flat out.
5. **Electricity basics.** Voltage is pressure, current is flow, resistance is friction. Power = voltage × current. Cover AC vs DC, why the grid uses high voltage (lower current means less loss), what a transformer does, and three-phase power at the intuition level only.
6. **Heat basics.** Essentially 100% of the electricity a chip uses becomes heat. Explain why water carries heat far better than air (~3,500× more heat per unit volume), what "a ton of cooling" is, and why temperature *differences* move heat.
7. **What "compute" means physically.** GPUs/TPUs/accelerators, servers, and memory. Link back to the chips chapter (06). A GPU's power rating (700 W for an H100, ~1,000 W+ for Blackwell-class) is the starting point for every data center calculation.

### Part B — Anatomy of a data center (walk the reader through the building)

8. **The campus and the building shell.** Fence, guard house, substation yard, generator yard, cooling yard (chillers, dry coolers, towers), and the buildings themselves: often windowless, single- or two-story "big boxes." Use a satellite-image tour.
9. **White space vs. gray space.** White space is where IT equipment lives. Gray space holds the support gear: electrical rooms, UPS rooms, battery rooms, mechanical rooms. Explain the ratio and why AI shifts more space toward mechanical and electrical equipment.
10. **Floors: raised floor vs. slab.** The old design pushed cold air under removable floor tiles. Modern designs put heavy AI racks on a concrete slab and run power and cooling overhead or in trenches. AI racks can weigh 1.5–3 tonnes, and that drives the shift.
11. **Racks, rows, aisles.** A rack is a standard 19-inch-wide metal frame measured in "U" (1.75 in). Racks stand in rows. Fronts face a cold aisle and backs face a hot aisle. Containment (doors and roofs on aisles) stops hot and cold air from mixing.
12. **Cable management and pathways.** Overhead cable trays and ladder racks carry power and fiber. Busways are overhead power rails that racks plug into. Structured cabling and patch panels round this out.
13. **Meet-me rooms (MMRs) and carrier connectivity.** This is the room where outside network carriers hand off fiber to tenants through "cross-connects." It ties the building to the internet.
14. **Inside the rack.** Servers (compute trays), switches, power shelves, PDUs, manifolds for liquid cooling. Contrast a 2015 enterprise rack (~5–10 kW) with a 2026 NVIDIA GB200/GB300 NVL72 rack (~120–140 kW) and Nvidia's 2027+ roadmap toward ~600 kW–1 MW.
15. **The power chain, step by step.** Utility transmission line → substation (high-voltage to medium-voltage transformer) → medium-voltage switchgear → unit substations/transformers (MV→LV) → low-voltage switchgear → UPS (+ batteries) → PDUs/RPPs or busway → rack power shelves (AC→48/54 V DC) → voltage regulators on the board → chip (~1 V or less). Generators and automatic transfer switches sit alongside for outages. Teach it as a river splitting into streams and then droplets.
16. **Backup power.** Diesel (sometimes gas) generators, fuel storage (often 24–48 h on site), and the automatic transfer switch. The UPS bridges the 10–30 seconds before generators take over. Batteries: lead-acid has given way to lithium-ion. Explain that air permits often limit how many hours generators may run.
17. **New power architectures.** Nvidia and partners are moving to 800 V DC distribution. Explain why: less copper, fewer conversion steps, and 1 MW racks. Also cover solid-state transformers and in-row battery or supercapacitor storage that smooths GPU power spikes.
18. **The cooling chain, step by step.** Chip → heat spreader/cold plate → coolant loop → coolant distribution unit (CDU) → facility water loop → chiller and/or dry cooler/cooling tower → atmosphere. In parallel there's the air path: server fans → hot aisle → CRAH/CRAC coil → back to cold aisle.
19. **Cooling technologies, from simplest to most advanced.** Room air conditioning, then hot/cold aisle containment, in-row coolers, rear-door heat exchangers, direct-to-chip (cold plate) liquid cooling (single-phase and two-phase), and immersion (single- and two-phase). Free cooling and economizers use cold outside air or water. Evaporative cooling uses water to save electricity.
20. **Efficiency metrics.** PUE = total facility energy ÷ IT energy. Then WUE (liters per kWh), CUE (carbon), ERE (credit for heat reuse). Cover typical values and what the metrics *don't* measure.
21. **Networking inside the data center.** NICs, top-of-rack switches, leaf and spine layers, fat-tree/Clos topologies. Distinguish "scale-up" (NVLink inside a rack), "scale-out" (InfiniBand/Ethernet across racks), and "front-end" (user traffic and storage) networks. Optical transceivers, fiber types and co-packaged optics come next. Then why AI training needs a "non-blocking" network.
22. **Networking between data centers.** Dark fiber, wavelengths, data center interconnect (DCI), carrier hotels, internet exchange points, and subsea cables. Then latency and the speed of light: roughly 5 µs per km in fiber. Finally, "AI WANs" that join campuses hundreds of miles apart into one training system, such as Microsoft's Fairwater sites.
23. **Reliability and redundancy.** N, N+1, 2N, 2N+1. Concurrent maintainability vs. fault tolerance. Uptime Institute Tiers I–IV and the "nines." Explain why AI *training* halls often accept less redundancy than a bank's data center, while inference and serving need more.
24. **Operations.** Building management systems (BMS), DCIM software, NOC/SOC, monitoring, maintenance windows, spares, and "remote hands." Cover the people who run a site and the failures they handle.
25. **Physical security.** Layered perimeters, mantraps, biometrics, cameras, and why addresses are often not publicized.

### Part C — Types of data centers and who builds them

26. **Types.** Enterprise (on-premises), retail colocation, wholesale colocation, hyperscale cloud, AI training campuses ("AI factories"), inference data centers, edge sites, modular/containerized units, and converted crypto-mining sites.
27. **The players.** Hyperscalers (AWS, Microsoft Azure, Google Cloud, Meta, Oracle). Neoclouds (CoreWeave, Nebius, Lambda, Crusoe, Together AI, Nscale, Fluidstack, IREN, and others). Colocation developers and landlords (Equinix, Digital Realty, QTS, Vantage, Aligned, STACK, CyrusOne, Related Digital, and others). Equipment makers (Nvidia, AMD, Broadcom; Vertiv, Schneider Electric, Eaton, ABB, Siemens, GE Vernova, Hitachi Energy). Utilities and grid operators. Finance (private equity, infrastructure funds, private credit, sovereign funds).
28. **Business models.** Self-build vs. lease. Powered land, powered shell, build-to-suit and turnkey. GPU-as-a-service (hourly on-demand vs. multi-year reserved). Take-or-pay contracts. Who carries which risk.

### Part D — Electricity grids, energy sources and the power problem

29. **How the grid works.** Generation → transmission → distribution → customer. Balancing supply and demand every second. Regional operators: ISOs/RTOs such as PJM, ERCOT, MISO, SPP, CAISO, NYISO and ISO-NE. Vertically integrated utilities. Regulators: FERC federally, public utility commissions in each state.
30. **Getting connected.** Large-load interconnection requests, load studies, network upgrades, the generator interconnection queue, and why waits now run multiple years. Cover "speed to power" as the industry's top priority.
31. **Who pays.** Rate cases, large-load tariffs, minimum-take contracts, collateral requirements, and capacity markets. Use PJM's price spike as the case study. Then the cost-allocation debate over whether households subsidize data centers.
32. **Energy sources, one at a time.** Natural gas (combined-cycle, simple-cycle turbines, reciprocating engines, aeroderivatives). Nuclear (existing plants, uprates, restarts, SMRs, advanced reactors, fusion PPAs). Solar + batteries, wind, geothermal (including enhanced geothermal), hydro, fuel cells, and coal (delayed retirements). For each, give the cost, speed to build, carbon, firmness and land use.
33. **Front-of-meter vs. behind-the-meter.** On-site generation, "bridge power," microgrids, co-location at power plants, and the regulatory fights over it.
34. **Clean-energy accounting.** PPAs, virtual PPAs, RECs, annual matching vs. 24/7 carbon-free energy, and additionality.
35. **Flexibility.** Data centers as flexible loads: curtailment and demand response. Texas SB6's emergency curtailment provisions. Using batteries and shifting training jobs.
36. **Forecasts.** IEA, LBNL, EPRI and EIA forecasts, and why they disagree. Then the "phantom load" problem: duplicate requests counted across many utilities.
37. **Effects on prices, reliability and emissions.** Household bills, capacity prices, delayed coal and gas retirements, local air pollution from on-site turbines and generators.

### Part E — Building one: site selection, process, bottlenecks

38. **Site selection.** Power (amount, timing, price, carbon), land (acreage, flatness, flood risk), fiber routes, water, climate, latency to users, tax incentives, permitting speed, community attitudes, labor availability and natural hazards.
39. **The development lifecycle.** Land control → power commitment → zoning/entitlements → environmental and air permits → design (basis of design, single-line diagrams) → procurement of long-lead gear → construction (site work, foundations, steel, roof, MEP fit-out) → commissioning (Levels 1–5, integrated systems testing) → IT installation ("rack and stack") → operations. Typical timelines run from 18–36 months for the building to 3–7+ years if new power is needed.
40. **Bottlenecks.** Large power transformers, switchgear, gas turbines, generators, chillers/CDUs, high-voltage breakers, skilled electricians and pipefitters, HBM memory and advanced packaging for chips, optical transceivers, and transmission lines.

### Part F — The money

41. **Capex vs. opex.** Capex is building and buying. Opex is power, staff, maintenance and leases.
42. **Cost per MW.** Building and electromechanical systems run ~$10–18M/MW. AI fit-out can add more. IT equipment (GPUs, networking) costs several times the building. "All-in" cost per GW is in the tens of billions.
43. **Unit economics.** GPU-hour prices, utilization, depreciation schedules, total cost of ownership, and cost per million tokens. Who earns what along the chain: chipmaker → server maker → cloud/neocloud → AI lab → app → user.
44. **Financing.** Corporate cash flow, bonds, equity raises, finance vs. operating leases, joint ventures and SPVs, private credit, GPU-backed loans, vendor financing and "circular" deals, and sovereign wealth funds.
45. **The bubble debate.** Bull and bear cases, depreciation arguments, concentration risk, and historical parallels (railroads, 1990s telecom fiber).

### Part G — The frontier megaprojects (2024–2026)

46. **Case studies.** OpenAI Stargate (Abilene and the other US sites; UAE; Norway), xAI/SpaceX Colossus 1 & 2 (Memphis/Southaven), Meta Prometheus (Ohio) and Hyperion (Louisiana), Microsoft Fairwater (Wisconsin, Atlanta), Amazon Project Rainier (Indiana), Google (Oklahoma, Ohio, Texas, India), and Anthropic's multi-vendor compute portfolio. Teach them as stories: who, where, how much power, where the power comes from, and what went wrong.

### Part H — Geopolitics and sovereign AI

47. **Sovereign AI and export controls.** Countries building national compute (Gulf states, EU "AI gigafactories," UK AI Growth Zones, India, Japan, Norway). Export controls on advanced chips. Data residency laws.

### Part I — Environment and communities

48. **Local impacts.** Water (withdrawal vs. consumption, direct vs. indirect), carbon (operational vs. embodied), air pollution from turbines and diesel, noise, land, jobs (construction vs. permanent), taxes and incentives, moratoriums, and the fight over cost allocation.

### Part J — Frontier ideas and open problems

49. **What's next.** 1 MW racks, 800 V DC, solid-state transformers, two-phase cooling, heat reuse into district heating, on-site nuclear, flexible "grid-aware" AI training, multi-site training over long-distance fiber, orbital data centers (Google's Project Suncatcher, Starcloud, SpaceX), and underwater/offshore data centers.

---

## 2. Glossary candidates (plain-English definitions)

### Units and quantities
1. **Watt (W)**: A rate of energy use, like speed for a car. A phone charger uses about 20 W while charging.
2. **Kilowatt (kW)**: 1,000 watts. A microwave uses about 1 kW. An average US home draws about 1.2 kW averaged over a year.
3. **Megawatt (MW)**: 1,000 kW, or a million watts. Enough for very roughly 800 average US homes. A small enterprise data center might be 1–5 MW.
4. **Gigawatt (GW)**: 1,000 MW. About the output of one large nuclear reactor. The frontier AI campuses of 2026 are measured in GW.
5. **Watt-hour (Wh)**: An *amount* of energy: one watt for one hour. One chatbot answer is often estimated at roughly 0.2–0.3 Wh.
6. **Kilowatt-hour (kWh)**: 1,000 Wh. The unit on your electric bill. US households paid about 17–18 cents per kWh in 2025–26.
7. **Megawatt-hour (MWh)**: 1,000 kWh. Wholesale power is priced per MWh.
8. **Gigawatt-hour (GWh) / Terawatt-hour (TWh)**: A million kWh and a billion kWh. National and global data center consumption is reported in TWh per year.
9. **Nameplate capacity**: The maximum power a power plant can produce or a facility can draw. It's not what it uses on average.
10. **Capacity factor / utilization**: Actual output or use divided by the maximum. A data center running at 70% of its capacity on average has a 70% "load factor."
11. **Load**: Anything that consumes electricity. Data centers are "large loads."
12. **Peak demand**: The highest power draw over a period. Grids must be built for the peak, not the average.
13. **BTU / ton of cooling**: Heat units. One "ton" of cooling removes 12,000 BTU per hour, about 3.5 kW of heat, named after the cooling from melting a ton of ice in a day.
14. **IT load**: The power used by the computing equipment itself (servers, storage, network), as opposed to cooling and other overhead.
15. **Critical IT capacity**: The amount of IT load a facility is designed to support with full backup. Data center sizes are often quoted this way, e.g. "100 MW critical."

### Electricity basics
16. **Voltage (V)**: Electrical "pressure" that pushes current. Homes use 120/240 V. Transmission lines use 69,000–765,000 V.
17. **Current (A, amps)**: The flow of electric charge. More current needs thicker copper and wastes more energy as heat.
18. **Alternating current (AC)**: Electricity that flips direction many times a second (60 Hz in the US, 50 Hz in Europe). The grid uses AC because transformers can easily change its voltage.
19. **Direct current (DC)**: Electricity that flows one way. Chips, batteries and solar panels are DC.
20. **Three-phase power**: Three AC waves offset in timing, used for large equipment because it delivers power smoothly and efficiently.
21. **Transformer**: A device with no moving parts that steps voltage up or down using magnetic coils. A key bottleneck in the AI build-out.
22. **Rectifier / inverter / power supply unit (PSU)**: A rectifier turns AC into DC and an inverter does the reverse. A PSU in a server or rack power shelf converts building power into the low-voltage DC that electronics use.
23. **Voltage regulator (VRM)**: Small circuits next to a chip that convert ~48–54 V DC down to the ~1 V the chip needs.
24. **Power factor / harmonics**: Measures of how "clean" and efficiently a load draws AC power. Big banks of power electronics can distort the grid's waveform.
25. **Power quality / load oscillation**: When thousands of GPUs speed up and slow down together, the whole site's power draw can swing by tens of MW within seconds. This can stress the grid, and engineers smooth it with batteries, capacitors or software.

### The power chain inside a data center
26. **Utility interconnection**: The physical and contractual connection between a site and the grid.
27. **Substation**: A fenced yard of transformers and breakers that steps transmission voltage (e.g. 345 kV) down to medium voltage (e.g. 34.5 kV). Big campuses build their own.
28. **High / medium / low voltage (HV/MV/LV)**: Rough bands. HV is above ~69 kV (transmission). MV is ~1–35 kV (campus distribution). LV is below 1 kV (inside the building, e.g. 415/480 V).
29. **Switchgear**: Cabinets of breakers and switches that route power and cut it off safely during faults. They come in MV and LV versions and are a long-lead item.
30. **Circuit breaker**: An automatic switch that opens when current is dangerously high.
31. **Single-line diagram (one-line)**: The engineering map of how power flows through a site, drawn with one line per circuit.
32. **UPS (uninterruptible power supply)**: Equipment with batteries (or flywheels) that keeps IT running for seconds to minutes when grid power fails, until generators start.
33. **Battery energy storage system (BESS)**: Large battery banks, usually lithium-ion, used for backup, to smooth spikes, or to shift energy in time.
34. **Backup generator**: An engine-generator, usually diesel and sometimes natural gas, that powers a site during an outage. Typical units are 2–3+ MW each, and big sites have dozens to hundreds.
35. **Automatic transfer switch (ATS)**: Switches a load from the utility feed to generators and back, automatically.
36. **PDU (power distribution unit)**: Distributes power to racks. It can be a large floor unit with a transformer or a rack-mounted power strip.
37. **RPP (remote power panel)**: A breaker panel near the racks fed by a PDU.
38. **Busway (busbar trunking)**: Overhead rigid copper or aluminum rails carrying power along a row. Racks plug in with tap-off boxes. Faster to install and change than cables.
39. **Rack power shelf**: A tray of PSUs in an AI rack that converts AC to ~50 V DC for the servers.
40. **800 V DC (HVDC) distribution**: Nvidia's announced architecture for 2027-era racks. It sends high-voltage DC to the rack to cut copper and conversion losses, so racks can reach ~1 MW. [V]
41. **Solid-state transformer (SST)**: A power-electronics replacement for the classic copper-and-iron transformer. Nvidia and partners are evaluating it for AI data centers. [V]
42. **Rack density**: Power per rack, in kW. Classic enterprise is ~5–10 kW. GB200/GB300-class AI racks are ~120–140 kW. Roadmaps point toward ~600 kW and beyond.
43. **Stranded capacity**: Power or cooling that was built but can't be used, e.g. because space or another constraint runs out first.

### Cooling
44. **Heat rejection**: Getting heat out of the building to the outdoors, the final step of cooling.
45. **CRAC (computer room air conditioner)**: A room AC unit with its own refrigeration compressor.
46. **CRAH (computer room air handler)**: A fan-and-coil unit that blows air across coils filled with chilled water from a central plant.
47. **Fan wall**: A wall of large fans and coils at the edge of a data hall that moves huge volumes of air.
48. **Chiller**: A machine that uses a refrigeration cycle to make cold water for the building. Chillers are major electricity users.
49. **Cooling tower**: An outdoor structure that cools water by evaporating part of it. Very energy-efficient but consumes water.
50. **Dry cooler**: A radiator with fans that cools liquid with outside air without evaporating water. Saves water but works less well on hot days.
51. **Adiabatic / evaporative cooling**: Spraying or wicking water into incoming air so that evaporation cools it. Cheap on electricity, but uses water.
52. **Economizer / free cooling**: Using cold outside air or water to cool directly whenever the weather allows, skipping chillers.
53. **Hot aisle / cold aisle**: A layout where racks face each other. Cold air enters the fronts in one aisle and hot air leaves the backs into the next.
54. **Containment**: Doors and ceilings that enclose a hot or cold aisle so the two air streams don't mix.
55. **Rear-door heat exchanger (RDHx)**: A water-cooled radiator mounted on the back door of a rack. It absorbs heat as hot air leaves.
56. **In-row cooler**: A cooling unit placed between racks in a row, close to the heat source.
57. **Direct-to-chip (DTC) liquid cooling**: Coolant pumped through metal "cold plates" sitting directly on GPUs and CPUs. It's standard for Blackwell-class AI racks.
58. **Cold plate**: A metal block with tiny internal channels that coolant flows through, touching the chip.
59. **CDU (coolant distribution unit)**: A pump-and-heat-exchanger unit that separates the clean "technology cooling loop" running through servers from the facility water loop. It also controls flow, pressure and temperature.
60. **Facility water system (FWS) / technology cooling system (TCS)**: The building's main water loop and the separate, cleaner loop that runs to the IT equipment.
61. **Manifold / quick disconnect**: Pipes in the rack that distribute coolant to each server, with dripless connectors so servers can be removed.
62. **Single-phase vs. two-phase cooling**: In single-phase, the coolant stays liquid. In two-phase, a special fluid boils on the chip and absorbs extra heat as it turns to vapor.
63. **Immersion cooling**: Submerging whole servers in a tank of non-conductive fluid.
64. **Closed-loop cooling**: Coolant circulates in sealed pipes and is reused, so little water is consumed on site. Microsoft says its Fairwater design fills the loop once. [V]
65. **Warm-water cooling**: Liquid cooling designed to work with relatively warm supply water (e.g. 30–45 °C). This lets dry coolers replace chillers much of the year.
66. **Heat reuse**: Piping data center waste heat into district heating networks, greenhouses or industry. Common in the Nordics.

### Building and layout
67. **Campus**: A site with multiple data center buildings sharing a substation and other infrastructure.
68. **Building shell**: The structure itself: foundations, walls, roof.
69. **Powered shell**: A building delivered with utility power and basic structure, but without the tenant's IT fit-out.
70. **White space**: The floor area where IT racks sit.
71. **Gray space**: Rooms for electrical and mechanical support equipment.
72. **Data hall**: One large room of white space, often 5–30+ MW in AI designs.
73. **Raised floor**: A floor of removable tiles on pedestals, historically used to blow cold air up through perforated tiles.
74. **Slab-on-grade**: Racks sitting directly on a concrete floor, with services overhead. Common for heavy AI racks.
75. **Rack**: A standard metal cabinet, 19 inches wide inside and about 42–52U tall, that holds servers and network gear.
76. **Rack unit (U)**: 1.75 inches of vertical rack space.
77. **Row / pod / cluster**: A row is a line of racks. A pod is a repeatable block of rows with its own network and cooling. A cluster is a set of pods networked together for one job.
78. **Cable tray / ladder rack**: Overhead channels that carry cables.
79. **Meet-me room (MMR)**: The secure room where telecom carriers' fiber meets the building's tenants.
80. **Cross-connect**: A physical cable in the MMR linking a tenant to a carrier or another tenant.
81. **NOC (network operations center)**: The room or team monitoring systems around the clock.
82. **BMS / DCIM**: Building management system (controls HVAC, power, alarms) and data center infrastructure management software (tracks assets, capacity and power).
83. **Commissioning (Cx)**: Systematic testing that every system works as designed before go-live. It runs from Level 1 (factory tests) to Level 5 (integrated systems test, e.g. pulling the utility feed with load banks running).
84. **Load bank**: A big resistor box that simulates IT load to test power and cooling systems.

### Networking
85. **Fiber optic cable**: Glass strands that carry data as light. Single-mode fiber goes long distances. Multimode is for short links.
86. **Optical transceiver**: A plug-in module that converts electrical signals to light and back, e.g. 800G and 1.6T modules.
87. **Co-packaged optics (CPO)**: Placing the optical parts right next to the switch chip to save power.
88. **NIC (network interface card)**: The server's network adapter.
89. **Top-of-rack (ToR) switch**: A network switch in each rack that connects its servers.
90. **Leaf-spine (Clos) network**: A two- or three-layer design where every "leaf" switch connects to every "spine" switch. Any two servers are then only a few hops apart.
91. **Fat tree / non-blocking**: A network where upper layers have enough capacity that all servers can talk at full speed at once. AI training needs this.
92. **Scale-up network**: Ultra-fast links connecting GPUs inside one rack or domain so they act like one giant GPU, e.g. NVLink.
93. **Scale-out network**: The network connecting many racks, using InfiniBand or high-speed Ethernet.
94. **Scale-across**: Linking multiple data center campuses so they can train one model, e.g. Microsoft's "AI WAN." [V]
95. **InfiniBand / RoCE Ethernet**: High-performance networking technologies used for AI clusters.
96. **Bandwidth vs. latency**: Bandwidth is how much data per second moves (the width of the pipe). Latency is how long one message takes to arrive (the length of the pipe).
97. **Dark fiber**: Unused fiber leased so the customer can "light" it with its own equipment.
98. **DCI (data center interconnect)**: High-capacity links between data centers.
99. **Internet exchange point (IXP) / carrier hotel**: Buildings where many networks meet and swap traffic. One Wilshire in LA and 60 Hudson Street in NYC are classic examples.
100. **Subsea cable**: Fiber cables on the ocean floor that carry nearly all intercontinental internet traffic.

### Reliability
101. **Redundancy**: Having spare equipment so one failure doesn't cause an outage.
102. **N**: The amount of equipment needed to carry the full load with no spare.
103. **N+1**: The needed amount plus one spare unit, e.g. 5 chillers needed, 6 installed.
104. **2N**: Two complete, independent systems, each able to carry the full load.
105. **2N+1 / distributed redundancy**: Variations with even more spare capacity, or with spare capacity shared across blocks.
106. **Concurrently maintainable**: Any component can be taken out for maintenance without shutting down IT.
107. **Fault tolerant**: The site survives any single unplanned failure without IT impact.
108. **Uptime Institute Tier I–IV**: A widely used rating system. Tier I is basic, Tier II adds redundant components, Tier III is concurrently maintainable, and Tier IV is fault tolerant. Common rule-of-thumb availabilities are 99.671%, 99.741%, 99.982% and 99.995%.
109. **"Nines" / availability**: 99.9% uptime is about 8.8 hours down per year. 99.99% is about 53 minutes. 99.999% is about 5 minutes.
110. **SLA (service-level agreement)**: A contract promising a level of uptime or performance, with penalties if missed.

### Grid, markets and regulation
111. **Grid**: The interconnected network of power plants, high-voltage lines and local wires.
112. **Transmission vs. distribution**: Transmission is high-voltage, long-distance "highways." Distribution is lower-voltage local "streets."
113. **Utility**: A company that delivers electricity to customers, sometimes also owning power plants.
114. **ISO / RTO**: Independent system operators or regional transmission organizations run wholesale markets and balance a region's grid, e.g. PJM in the Mid-Atlantic/Midwest and ERCOT in most of Texas.
115. **FERC**: The Federal Energy Regulatory Commission, the US regulator of interstate transmission and wholesale power markets.
116. **PUC / PSC**: State public utility (or service) commissions that set retail electricity rates and approve utility investments.
117. **Interconnection queue**: The waiting line of projects (generators, and increasingly large loads) asking to connect to the grid. Each needs engineering studies.
118. **Large-load tariff**: Special utility rules for huge customers, such as long minimum contract terms, minimum payments and collateral, so others aren't stuck with stranded costs.
119. **Capacity market**: A market, like PJM's, that pays power plants years in advance to be available at peak times. Its costs flow into everyone's bills.
120. **Base Residual Auction (BRA)**: PJM's main capacity auction.
121. **Behind-the-meter (BTM)**: Generation located on the customer's side of the utility meter, often on site. The data center makes its own power.
122. **Co-location (power)**: Placing a data center right next to, and directly connected to, a power plant, e.g. next to a nuclear station. This is the subject of FERC rulings. Don't confuse it with "colocation" data centers.
123. **Bridge power**: Temporary on-site generation, often gas turbines or engines, used until a grid connection is ready.
124. **Microgrid**: A self-contained local power system that can run independently of the main grid.
125. **Curtailment / demand response**: Reducing electricity use on request during grid stress, often for payment.
126. **Transmission upgrade / network upgrade**: New lines or substations needed to serve a new load or generator. Who pays is often contested.
127. **Ratepayer**: A customer who pays utility bills. "Ratepayer protection" is a core political issue around data centers.
128. **Phantom (speculative) load**: Data center power requests filed in many places at once by developers shopping for power. They inflate demand forecasts.

### Energy sources
129. **Combined-cycle gas turbine (CCGT)**: A gas turbine whose hot exhaust also makes steam for a second turbine. It's efficient (~60%) and slow to build (~4–6+ years including equipment lead times).
130. **Simple-cycle / peaker turbine**: A gas turbine without the steam stage. Faster to start and build, less efficient.
131. **Aeroderivative turbine**: A gas turbine adapted from jet engines. Compact and quick-starting, and popular for on-site AI power.
132. **Reciprocating engine (recip)**: A large piston engine generator, like a giant car engine. Modular and fast to deploy.
133. **Fuel cell**: A device that turns fuel such as natural gas or hydrogen into electricity chemically, without burning it, e.g. Bloom Energy's solid-oxide cells.
134. **Nuclear restart**: Returning a closed nuclear plant to service, e.g. Three Mile Island Unit 1 becoming the Crane Clean Energy Center for Microsoft.
135. **Uprate**: Increasing an existing power plant's output through equipment upgrades.
136. **SMR (small modular reactor)**: A nuclear reactor of up to ~300 MW designed to be factory-built in modules. First US units are expected around the end of the decade.
137. **Advanced reactor**: A non-traditional reactor design, e.g. sodium-cooled (TerraPower Natrium, Oklo Aurora), molten-salt-cooled (Kairos) or high-temperature gas (X-energy).
138. **Enhanced geothermal (EGS)**: Drilling deep and fracturing hot rock to make geothermal power possible in more places, e.g. Fervo.
139. **PPA (power purchase agreement)**: A long-term contract, often 10–20 years, to buy electricity from a specific generator at an agreed price.
140. **Virtual PPA**: A financial contract for the price difference, paired with renewable energy certificates, without physical delivery of power.
141. **REC (renewable energy certificate)**: A tradeable proof that 1 MWh of renewable power was generated.
142. **24/7 carbon-free energy (CFE)**: Matching consumption with clean power *every hour* in the same grid region, which is stricter than annual matching.
143. **Additionality**: Whether a clean energy purchase caused *new* clean power to be built, rather than claiming existing output.
144. **Firm power / baseload**: Power available whenever needed, regardless of weather, e.g. nuclear, gas or geothermal.
145. **Intermittent / variable**: Power that depends on weather (solar, wind).

### Efficiency and environment
146. **PUE (power usage effectiveness)**: Total facility energy ÷ IT energy. 1.0 would mean zero overhead. The industry average has hovered around 1.5–1.6, and leading hyperscale sites run about 1.1.
147. **WUE (water usage effectiveness)**: Liters of on-site water consumed per kWh of IT energy.
148. **CUE (carbon usage effectiveness)**: Carbon emissions per kWh of IT energy.
149. **Water withdrawal vs. consumption**: Withdrawal is water taken in. Consumption is water not returned, mostly evaporated.
150. **Direct vs. indirect water**: Direct water is used on site for cooling. Indirect water is used by the power plants making the electricity.
151. **Scope 1 / 2 / 3 emissions**: Direct on-site emissions, emissions from purchased electricity, and supply-chain emissions such as making the concrete, steel and chips.
152. **Embodied carbon**: Emissions from manufacturing and constructing the building and equipment.

### Business, finance and economics
153. **Hyperscaler**: A giant cloud and internet company operating data centers at massive scale: Amazon (AWS), Microsoft, Google, Meta and Oracle.
154. **Neocloud**: A newer cloud company specializing in renting AI GPUs, e.g. CoreWeave, Nebius, Lambda, Crusoe.
155. **Colocation (colo)**: Renting space, power and cooling in someone else's data center. Retail colo means a few racks. Wholesale means whole halls or buildings.
156. **Build-to-suit**: A developer builds a data center to a specific tenant's design under a long lease.
157. **Capex / opex**: Capital expenditure (buying long-lived things like buildings and chips) and operating expenditure (ongoing costs like electricity and salaries).
158. **Depreciation / useful life**: Spreading an asset's cost over the years it's expected to be useful. Hyperscalers use ~5–6 years for servers. Microsoft extended data center buildings from 15 to 25 years in July 2026. [V]
159. **TCO (total cost of ownership)**: All the costs of owning and running something over its life.
160. **GPU-hour**: Renting one GPU for one hour, the basic unit of AI cloud pricing.
161. **On-demand vs. reserved**: Pay-as-you-go hourly pricing vs. committing to months or years for a lower rate.
162. **Utilization**: The share of time GPUs are doing paid or useful work. It drives profitability.
163. **Cost per token**: The cost to generate one unit of AI output text. Usually quoted per million tokens.
164. **Take-or-pay contract**: The customer pays for capacity whether or not it uses it. These contracts underpin data center financing.
165. **Backlog / RPO (remaining performance obligations)**: Contracted future revenue not yet recognized, e.g. AWS's backlog or Oracle's RPO.
166. **Finance lease vs. operating lease**: Accounting categories. Finance leases look like owning (they count in capex at some companies). Operating leases look like renting.
167. **SPV (special purpose vehicle)**: A separate company created to own one project and borrow against it, keeping the debt off the sponsor's main balance sheet. Meta's Hyperion JV with Blue Owl is the prime example. [R]
168. **Private credit**: Loans from non-bank investment funds, now a major data center lender.
169. **GPU-backed loan**: A loan that uses GPUs (and the contracts renting them) as collateral. CoreWeave's 2023 deal backed by H100s was the first. [R]
170. **Circular financing / vendor financing**: When a supplier invests in or lends to a customer that then buys the supplier's products. Example: chipmakers investing in AI labs that buy their chips.
171. **Hyperscale campus economics ($/MW)**: Cost to build, quoted per megawatt of IT capacity.
172. **Sovereign AI**: National efforts to own AI compute and models within a country's borders.

---

## 3. Prerequisites and dependencies (what must come before what)

**Core chain (teach in this order):**
1. *Electricity units (W vs Wh)* → needed for everything else.
2. *Heat = electricity used* → needed for cooling, PUE and water.
3. *What a GPU/server is* (from the chips chapter) → needed for rack density.
4. *Rack density* → needed for why AI data centers differ from old ones (liquid cooling, slab floors, busways, 800 V DC).
5. *Power chain* → needed for UPS/generators, redundancy, Tiers and 800 V DC.
6. *Cooling chain* → needed for PUE, WUE, water debates and site climate.
7. *PUE/WUE* → needed for the environment chapter and for comparing operators.
8. *Networking inside DCs* → needed for why AI clusters must be dense and co-located, and for multi-site training.
9. *Grid basics (generation/transmission/distribution, ISOs, utilities)* → needed for interconnection queues, capacity markets, behind-the-meter power and price effects.
10. *Energy sources* → needed for nuclear/gas/renewable deal analysis and carbon accounting.
11. *Capacity vs consumption, utilization* → needed for demand forecasts and unit economics.
12. *Capex/opex, depreciation* → needed for GPU-hour economics, cost per token, financing and the bubble debate.
13. *All of the above* → needed for the megaproject case studies, which tie power, cooling, chips, money and politics together.

**Specific dependencies:**
- "Why does AI need liquid cooling?" requires heat basics, rack density, and air vs. water heat capacity.
- "Why 800 V DC?" requires P = V × I, resistive losses, and the power chain.
- "What does a 1 GW campus mean?" requires GW, capacity vs. energy, PUE, and GPU power per chip.
- "Why are electricity prices rising?" requires grid basics, capacity markets, transmission costs, and large-load tariffs.
- "Why is gas winning near-term?" requires energy source speed and firmness, interconnection queues, and equipment lead times.
- "Is it a bubble?" requires capex, depreciation, utilization, revenue/backlog, financing structures, and historical analogies.
- "Cost per token" requires GPU-hour pricing, throughput (tokens/second, from the inference chapter) and utilization.
- "Space data centers" requires heat rejection (radiators), solar power, launch costs, and networking/latency.
- "Sovereign AI" requires export controls (chips chapter), site selection, and energy availability.

**Cross-chapter links:** Chips & compute (06) supplies GPU power figures and the HBM/packaging bottlenecks. Training vs inference (03/05) explains why training clusters need one giant site while inference can be spread out. Careers (10) takes the opportunity section.

---

## 4. Current state and key facts (2025–2026), with sources

### 4.1 How much electricity do data centers use?

- **Global (IEA, *Energy and AI*, April 2025) [M]:** Data centers used about **415 TWh in 2024, ~1.5% of global electricity**. The base case projects **~945 TWh by 2030**, a bit more than Japan's total electricity use today. The US was ~45% of 2024 consumption, China ~25%, Europe ~15%. Electricity use by AI-accelerated servers grows ~30%/yr in the base case. https://www.iea.org/reports/energy-and-ai (the 415 TWh / 945 TWh figures also appear in https://en.wikipedia.org/wiki/Data_center [R]).
- **United States (LBNL, December 2024) [M]:** US data centers used ~**76 TWh in 2018 (~1.9%)** and **176 TWh in 2023 (~4.4% of US electricity)**. The 2028 projection is **325–580 TWh, or 6.7%–12%**. https://eta.lbl.gov/publications/2024-lbnl-data-center-energy-usage-report
- **EPRI (*Powering Intelligence*, May 2024) [M]:** Data centers could reach 4.6%–9.1% of US electricity by 2030. Virginia data centers were already about a quarter of that state's electricity use in 2023.
- **Ireland [V]:** Data centres used **22% of all metered electricity in 2024**, up from 5% in 2015 (CSO, June 2025). https://www.cso.ie/en/releasesandpublications/ep/p-dcmec/datacentresmeteredelectricityconsumption2024/
- **Tracked AI capacity [V]:** Epoch AI's data center hub (data updated **Oct 20, 2026**) tracks **95 large AI data centers with ~14.2 GW of IT power (~18.5 GW including cooling/overhead)** and ~14.8 million H100-equivalents. It estimates this covers ~44% of global AI compute, and notes sites typically consume 60–80% of capacity on average. https://epoch.ai/data/data-centers
- **Global capacity forecast [V]:** JLL (January 2026) expects global data center capacity to roughly **double from ~103 GW to ~200 GW between 2025 and 2030**. AI was about a quarter of workloads in 2025 and could be half by 2030, and inference may overtake training around 2027. https://www.jll.com/en-us/insights/market-outlook/data-center-outlook
- **US prices [V]:** EIA's October 2026 Short-Term Energy Outlook shows average US **residential electricity at 17.3¢/kWh (2025) → 18.2¢ (2026) → 18.7¢ (2027 forecast)**. https://www.eia.gov/outlooks/steo/report/elec_coal_renew.php

### 4.2 Energy of a single chatbot interaction (the reader's own usage)

- **Google [V]:** The median Gemini Apps text prompt (May 2025) used **0.24 Wh, 0.26 mL water, and 0.03 gCO2e**, comparable to watching TV for under 9 seconds. Google reports energy per median prompt fell 33× in 12 months. The figure includes idle machines, host CPUs and PUE overhead, and Google notes it hasn't been verified by an independent third party. https://cloud.google.com/blog/products/infrastructure/measuring-the-environmental-impact-of-ai-inference
- **OpenAI (Sam Altman, June 2025) [V]:** An average ChatGPT query uses "about 0.34 watt-hours" and "about 0.000085 gallons of water." https://blog.samaltman.com/the-gentle-singularity
- **Epoch AI (Feb 2025) [V]:** A typical GPT-4o query is about **0.3 Wh**, 10× below the older 3 Wh estimate. Long inputs cost much more: about 2.5 Wh for 10k input tokens and about 40 Wh for 100k tokens. Reasoning models generate more tokens and use more energy. https://epoch.ai/gradient-updates/how-much-energy-does-chatgpt-use
- **Teaching point:** Per-query energy is small, about the energy of an LED bulb for a couple of minutes. What matters is the *total*: billions of queries, ever-longer contexts, agents that run for hours, video generation, and training runs.

### 4.3 Hyperscaler capital expenditure (capex)

| Company | 2025 capex (approx.) | 2026 guidance (latest, as of Q2 2026 calls in late July 2026) |
|---|---|---|
| Alphabet/Google | ~$91.5B [R] | **$195–205B**, raised July 2026 from $180–190B, which was itself raised from $175–185B [R][V-FactSet for earlier range] |
| Amazon | ~$131–135B (definitions vary) [R] | **~$220B**, raised July 2026 from ~$200B; includes non-AI spending (robotics, satellites). Higher memory prices were cited [R] |
| Meta | ~$72.2B [R] | **$130–145B**, narrowed/raised July 29, 2026 [R] |
| Microsoft | ~$118B (calendar basis unclear) [R] | Calendar-2026 expectation **~$175B** after an accounting change. Q4 FY26 (Apr–Jun 2026) capex was **$41B incl. finance leases**, ~2/3 on short-lived assets (GPUs/CPUs). Q1 FY27 guidance: >$50B [V] |
| Oracle | FY26 financed with ~$43B debt + $5B equity [V-FactSet] | S&P cut Oracle to **BBB-** on July 9, 2026 [V-FactSet] |

Sources:
- FactSet (July 23, 2026) [V]: "close to $800bn for calendar 2026" across the five companies, including finance leases and customer prepayments, and about $820bn of off-balance-sheet lease commitments. https://insight.factset.com/hyperscalers-tap-external-financing-as-ai-capex-outruns-cash-flow
- Microsoft Q4 FY26 call (late July 2026) [V]: $41B capex, the useful life of data centers extended from 15 to 25 years, demand still exceeding supply. Nadella: Microsoft "added another gigawatt of capacity this quarter." https://www.fool.com/earnings/call-transcripts/2026/08/07/microsoft-msft-q4-2026-earnings-call-transcript/ and https://www.cfodive.com/news/microsoft-holds-line-ai-spending-plans/826648/
- Alphabet raise to $195–205B [R]: https://www.outlookbusiness.com/corporate/google-parent-alphabet-doubles-down-on-ai-plans-up-to-205-billion-in-2026-capex
- Amazon $220B and AWS backlog of **$496B** (Q2 2026) [R]: https://letsdatascience.com/news/aws-revenue-growth-outruns-available-ai-capacity-b0361d90
- Meta $130–145B [R]: https://www.storagenewsletter.com/2026/07/30/meta-platforms-fiscal-2q26-financial-results/
- 2025 actuals [R]: https://platformonomics.com/?p=34926
- **Q3 2026 earnings are due the week of Oct 27–30, 2026.** Update this table before printing.

### 4.4 Financing the build-out

- **Alphabet equity raise (June 1, 2026) [V-SEC]:** An **$80B equity program**: $30B of underwritten public offerings, a $40B at-the-market program, and a **$10B private placement to Berkshire Hathaway**. Proceeds are for general purposes including AI infrastructure capex. https://www.sec.gov/Archives/edgar/data/0001652044/000119312526257724/d83560dex991.htm and https://www.sec.gov/Archives/edgar/data/0001652044/000119312526251733/d160205dfwp.htm
- **Amazon [V-FactSet]:** Placed a $25B bond, 2.5× oversubscribed.
- **Oracle [V-FactSet]:** ~$43B debt plus $5B equity in FY26, a plan for ~$40B more in FY27, and a downgrade to BBB- (the lowest investment grade).
- **Meta Hyperion SPV [R]:** An 80/20 joint venture with Blue Owl–managed "Beignet Investors." Meta is the minority partner and tenant, keeping the project off its balance sheet. Construction is funded by bonds repaid from Meta's lease payments, with an initial 4-year lease from 2029 renewable for up to 20 years. https://en.wikipedia.org/wiki/Hyperion_Data_Center
- **CoreWeave [R]:** Total debt was ~**$35.1B at June 30, 2026**. Its 2023 $2.3B facility collateralized by H100 GPUs was the first GPU-backed loan of its kind. In 2026: a $2B Nvidia investment (January), an $8.5B loan sought against Meta contracts (February), and $3.5B of convertible notes (April). https://en.wikipedia.org/wiki/CoreWeave
- **OpenAI round (February 2026) [R]:** A **$110B round** with $50B from Amazon, $30B from Nvidia and $30B from SoftBank. Nvidia's earlier "up to $100B for 10 GW" letter of intent (September 2025) was reported shelved in favor of the $30B equity investment. https://www.business-standard.com/technology/tech-news/nvidia-30bn-openai-investment-after-shelving-100bn-deal-126022000503_1.html
- **"Circular" deals to explain [M/R]:** Nvidia invests in AI labs and neoclouds (OpenAI, CoreWeave, Nebius, Anthropic) that buy Nvidia GPUs. AMD gave OpenAI warrants for up to ~10% of AMD alongside a 6 GW GPU purchase (October 2025). Microsoft and Nvidia committed up to $5B and $10B respectively to Anthropic as Anthropic committed $30B to Azure (November 2025). https://www.constellationr.com/insights/news/anthropic-microsoft-azure-nvidia-ink-30-billion-compute-pact
- **Real estate and debt need [V]:** JLL estimates ~$1.2T of data center real estate value creation and ~$870B of new debt financing through 2030. Tenants may spend $1–2T more on fit-out, for nearly $3T in total. https://www.jll.com/en-us/insights/market-outlook/data-center-outlook

### 4.5 The frontier megaprojects (status as of October 2026)

**OpenAI "Stargate" (with Oracle, SoftBank, MGX, Crusoe, Vantage, SB Energy, Related, STACK)**
- Announced Jan 21, 2025 at the White House: "up to $500B / 10 GW" by 2029. https://en.wikipedia.org/wiki/Stargate_LLC [R]
- **Abilene, TX** (Crusoe builds, Oracle operates for OpenAI): a **1.2 GW** campus with 8 buildings. Epoch's April 2026 estimate was ~0.3 GW of facility power running (~200 MW IT), with completion in Q4 2026. A planned expansion to ~2.1 GW was cancelled, and Microsoft later partnered with Crusoe on an adjacent ~900 MW site [V]. Oracle reportedly said in September 2026 that six of eight buildings (~618 MW) had been delivered [R].
- **Other US sites (Epoch, April 2026) [V]:** Shackelford County TX (Vantage "Frontier," ~1.4 GW IT / 2.0 GW, on-site gas microgrid; VoltaGrid 700 MW behind-the-meter gas) [V/R]; Doña Ana County NM (STACK "Project Jupiter," 2.2 GW initial, two gas microgrids); Milam County TX (SB Energy, 1.2 GW, with co-located solar); Port Washington WI (Vantage "Lighthouse," ~1.3 GW grid draw); Saline Township MI (Related Digital "The Barn," ~1.4 GW, DTE grid plus batteries); Lordstown OH (<0.3 GW). Epoch projects **"over 9 GW"** across sites by ~2029, with most new capacity in 2027–2028. https://epoch.ai/publications/openai-stargate-where-the-us-sites-stand and https://measuredai.substack.com/p/stargate-site-by-site-status
- **New Ohio site [R]:** "PORTS-Pike" (the former DOE Portsmouth site), announced Aug 17, 2026, with the first 800 MW expected in 2028. Re-verify.
- **International:** Stargate UAE is a 1 GW cluster inside a planned 5 GW UAE–US AI campus in Abu Dhabi (with G42, Oracle, Nvidia, Cisco, SoftBank). The first 200 MW was targeted for 2026 [M; announced May 2025]. Stargate Norway (Narvik, with Nscale and Aker) was announced July 2025 with ~230 MW initial capacity [M]. Stargate Argentina had made no progress beyond a letter of intent as of May 2026 [R]. OpenAI reportedly paused Stargate UK in April 2026, citing energy costs [R].
- **OpenAI chip/compute commitments [R]:** Broadcom 10 GW of custom accelerators, AMD 6 GW (first 1 GW from H2 2026), Cerebras 750 MW plus an option on 1.25 GW (deployed 2026–2028), Oracle (~$300B, 4.5 GW), Microsoft Azure ($250B), AWS ($38B), CoreWeave. https://www.cnbc.com/2026/01/16/openai-chip-deal-with-cerebras-adds-to-roster-of-nvidia-amd-broadcom.html

**xAI / SpaceX "Colossus" (Memphis, TN and Southaven, MS)**
- **Colossus 1:** A former Electrolux plant built in **122 days** in 2024 with ~100,000 H100s. Initial grid power was ~8 MW, upgraded toward ~150 MW, with temporary gas turbines and Tesla Megapacks filling the gap [R]. https://en.wikipedia.org/wiki/Colossus_(data_center)
- **Colossus 2:** The first ~110,000 GB200 cluster (~210 MW) came online around January 2026. Reports in late September 2026 counted ~440,000 GB300s in use [R]. Epoch lists Colossus 2 at **~946 MW IT power, the largest site by compute (~1.1M H100e)** [V]. https://epoch.ai/data/data-centers
- **Power controversy:** Dozens of gas turbines ran without permanent permits. Mississippi approved a permanent **~1.2 GW, 41-turbine plant in Southaven (March 2026)**. The NAACP (represented by SELC and Earthjustice) sued in April 2026 under the Clean Air Act [R]. https://www.selc.org/news/xai-built-an-illegal-power-plant-to-power-its-data-center/
- **Corporate:** **SpaceX acquired xAI on Feb 2, 2026** (all-stock; xAI valued at $250B), and the AI unit was later rebranded SpaceXAI. Reports in May–June 2026 said Anthropic would rent Colossus capacity and Google would pay SpaceX ~$920M per month for compute [R: Wikipedia citing Yahoo Finance/CNBC; verify]. https://en.wikipedia.org/wiki/XAI_(company)

**Meta**
- **Prometheus (New Albany, Ohio):** ~1 GW targeted for 2026. Epoch lists ~471 MW IT running in October 2026 [V]. On-site gas plants supplement the grid [R]. Meta's January 2026 nuclear deals are explicitly meant to support grids serving Prometheus [V].
- **Hyperion (Richland Parish, Louisiana):** A 2,250-acre site. On **July 13, 2026**, Meta said it will scale to **5 GW, with investment above $50B**. The first phase of ~2 GW is due by 2030 and full build-out around 2032. Entergy is building gas plants (combined-cycle) and has proposed 1.5 GW of new solar and hybrid solar-storage on top of 3 GW previously approved; Meta funds the new transmission [V/R]. https://www.datacenterknowledge.com/data-center-construction/meta-s-5-gw-hyperion-campus-signals-ai-s-shift-into-utility-territory and https://en.wikipedia.org/wiki/Hyperion_Data_Center
- **Nuclear (Jan 9, 2026) [V]:** Up to **6.6 GW** by 2035. Vistra: 2.1 GW+ from Perry and Davis-Besse, plus 433 MW of uprates. TerraPower: 2 Natrium units (690 MW) as early as 2032, with rights to 6 more. Oklo: up to 1.2 GW in Pike County, Ohio, as early as 2030. This adds to a 2025 deal for Constellation's Clinton plant. https://about.fb.com/news/2026/01/meta-nuclear-energy-projects-power-american-ai-leadership/

**Microsoft "Fairwater" AI superfactories**
- **Mount Pleasant, Wisconsin [V]:** 315 acres, 3 buildings, ~1.2M sq ft, "hundreds of thousands" of NVIDIA GB200 GPUs, and a two-story rack layout. It uses a **closed-loop liquid cooling** system (>90% of capacity) filled once, plus the "second-largest water-cooled chiller plant on the planet" and 172 20-ft fans. Each 72-GPU rack is quoted at **865,000 tokens/second**. Construction used 46.6 miles of deep foundation piles, 26.5M lbs of structural steel, 120 miles of medium-voltage underground cable and 72.6 miles of mechanical piping. https://blogs.microsoft.com/blog/2025/09/18/inside-the-worlds-most-powerful-ai-datacenter/
- **Atlanta (Fayetteville, GA):** The second Fairwater site, operating since October 2025 and linked to Wisconsin over an "AI WAN" so the two act as one system. Racks are ~140 kW [R] (https://w.media/?p=186700). Epoch lists ~636 MW IT [V].
- **Three Mile Island Unit 1 → Crane Clean Energy Center [R]:** A 20-year PPA covering the plant's output (~835 MW per Constellation; Wikipedia lists 819 MW net). Restart was targeted for 2027 (originally 2028), backed by a $1B DOE loan (November 2025). https://en.wikipedia.org/wiki/Three_Mile_Island_Nuclear_Generating_Station

**Amazon / Anthropic "Project Rainier"**
- The Indiana site (St. Joseph County / New Carlisle) came online in under a year with ~500,000 Trainium2 chips at launch (October 2025). Anthropic was to use >1 million Trainium2 chips. AWS water efficiency is quoted at 0.15 L/kWh vs a 0.375 industry average [V]. https://www.aboutamazon.com/news/aws/aws-project-rainier-ai-trainium-chips-compute-cluster
- Epoch lists "Anthropic-Amazon New Carlisle" at **~1,037 MW IT, the largest tracked site by power** (October 2026) [V].
- **Anthropic–Amazon (Apr 20, 2026) [V/R]:** Up to **5 GW**, with nearly 1 GW of Trainium2/3 online by end of 2026. Reported terms: >$100B committed to AWS over 10 years. https://www.anthropic.com/news/anthropic-amazon-compute

**Anthropic's other compute**
- **Google TPUs:** In October 2025, up to 1 million TPUs ("well over a gigawatt" in 2026). On **Apr 6, 2026**, a new Google+Broadcom agreement for "multiple gigawatts" of next-generation TPUs from 2027; a Broadcom filing implies ~3.5 GW. Anthropic's run-rate revenue then exceeded $30B, up from ~$9B at end-2025 [V/R]. https://www.anthropic.com/news/google-broadcom-partnership-compute and https://techcrunch.com/2026/04/07/anthropic-compute-deal-google-broadcom-tpus/
- **Fluidstack:** $50B of US data centers (Texas, New York) announced in November 2025 [M].
- **Microsoft/Nvidia (November 2025):** $30B of Azure compute and up to 1 GW of Grace Blackwell/Vera Rubin systems [R].
- **CoreWeave:** A multi-year Nvidia GPU deal announced April 2026 [R].

**Google**
- Huge self-builds in Oklahoma (Pryor, ranked #4 by compute in Epoch's tracker), Ohio, Texas ($40B through 2027), Arkansas, Indiana, and a ~1 GW Visakhapatnam (India) hub of ~$15B [R]. https://en.wikipedia.org/wiki/Google_data_centers
- Energy deals: Kairos SMRs (500 MW, 2030–35), the Duane Arnold (Iowa) nuclear restart by 2029, and a reported record 12 GW of clean-energy contracts in 2025 [R].
- Efficiency: fleet PUE ~1.09 vs an industry average ~1.56 [R].

**Neoclouds (snapshot)**
- **CoreWeave [R]:** 2025 revenue $5.13B, Q1 2026 revenue $2.08B, backlog near $100B, ~51 AI data centers (2026), and Microsoft as ~2/3 of 2025 revenue. A $21B Meta expansion was announced April 2026.
- **Nebius [R/M]:** Microsoft contract of $17.4B (up to $19.4B, September 2025) and a Meta contract (~$3B, November 2025). Sites in Finland, New Jersey (Vineland, 300 MW) and Kansas City, with Birmingham, AL announced February 2026. Nvidia invested $2B in March 2026. https://en.wikipedia.org/wiki/Nebius_Group
- Others to profile: Lambda, Crusoe (Abilene builder; also building for Microsoft), Together AI, Nscale (Stargate Norway/UK), Fluidstack (TPU data centers for Google/Anthropic), and bitcoin-miner conversions (IREN, Cipher, TeraWulf, Core Scientific).

### 4.6 Rack power, chips and new power architecture

- Hopper→Blackwell raised rack density ~3.4×, "from tens of kilowatts to well over 100." Nvidia is designing for **>1 MW per rack**, with **800 V DC** distribution in production alongside Kyber racks in **2027**. 800 VDC carries 85% more power through the same conductor than 415 VAC, cuts copper ~45%, and improves end-to-end efficiency by up to 5%. A 1 MW rack at 54 V could need ~200 kg of copper busbar [V]. https://developer.nvidia.com/blog/nvidia-800-v-hvdc-architecture-will-power-the-next-generation-of-ai-factories/ and https://developer.nvidia.com/blog/building-the-800-vdc-ecosystem-for-efficient-scalable-ai-factories/
- Energy storage is placed at two levels. Capacitors near racks absorb millisecond spikes, and facility batteries handle seconds-to-minutes swings and generator ride-through [V].
- Microsoft Fairwater Atlanta racks are ~140 kW (GB200 NVL72) [R]. Rule of thumb: an H100 is 700 W chip TDP, about 1.2–1.5 kW all-in with server, network and cooling overhead. Epoch's energy estimate uses ~1,500 W per H100 including overhead [V].

### 4.7 Costs and prices

- **Build cost per MW [V]:** JLL puts global average shell-and-core at **$10.7M/MW in 2025 and $11.3M/MW forecast for 2026** (up from $7.7M in 2020). AI tenant fit-out can reach **~$25M/MW**. Cushman & Wakefield's 2026 guide puts the average greenfield cost of the most modern facilities at **$17.6M/MW**, up 21% from its previous report. https://www.jll.com/en-us/insights/market-outlook/data-center-outlook and https://www.cushmanwakefield.com/en/united-states/insights/data-center-development-cost-guide
- **All-in cost per GW including chips:** Industry statements put it at tens of billions of dollars. Nvidia's CEO has cited ~$50–60B per GW, and Forbes described Anthropic's $50B Fluidstack commitment as roughly the cost of one gigawatt [M/R]. Teach the split: the building and power gear are roughly 20–30%, and IT equipment (GPUs, networking, storage) is the large majority.
- **GPU rental prices (list prices, October 2026) [V]:**
  - **Lambda on-demand:** H100 SXM $3.99–4.29/GPU-hr; B200 $6.69–6.99; A100 80GB $2.79. 1-Click Clusters: H100 $5.54–6.16 and B200 $8.87–9.86. https://lambda.ai/pricing
  - **RunPod:** H100 SXM $3.99 (secure) / ~$2.69 (community); H200 $5.29; B200 $7.99; B300 $8.99; A100 $1.79. https://www.runpod.io/pricing
  - Teaching note: in 2025, H100s were widely available at roughly $2–3/hr on-demand from many providers. October 2026 list prices are higher at several providers, consistent with reports of tight supply and higher memory costs [M]. Reserved multi-year contracts for big customers are much cheaper per hour than these on-demand list prices and aren't public.
- **Depreciation [V/M]:** Microsoft extended data center building life from 15 to 25 years effective FY27 [V]. Server/GPU lives at hyperscalers are ~5–6 years. Amazon shortened some servers from 6 to 5 years in early 2025 [M]. Critics argue AI GPUs become economically obsolete faster than that.

### 4.8 Grid, interconnection and community pushback

- **Wait times [V]:** JLL says the average wait for a grid connection in primary markets exceeds **four years**, pushing operators to behind-the-meter power, batteries and gas. Ireland and Texas have "bring your own power" style requirements.
- **PJM capacity market [M]:** Capacity prices jumped from ~$29/MW-day (2024/25) to **$269.92 (2025/26)**, then hit the cap at **~$329 (2026/27)** and **~$333 (2027/28)**. The 2027/28 auction fell short of PJM's reliability target for the first time, at a total cost of ~$16B+. Data center load growth is the main driver of forecast demand. Re-verify the exact numbers at https://www.pjm.com (Base Residual Auction reports). See also https://en.wikipedia.org/wiki/PJM_Interconnection [R].
- **FERC (December 2025) [R]:** A unanimous order on letting data centers connect directly to (co-locate with) power plants in PJM. https://en.wikipedia.org/wiki/Data_center
- **Texas SB 6 (2025) [M]:** Large loads (≥75 MW) must disclose backup generation, share interconnection costs, and can be curtailed or required to switch to backup power in grid emergencies.
- **Local opposition [V]:** Data Center Watch counted **$64B** of US projects blocked ($18B) or delayed ($46B) between May 2024 and March 2025, with 142 activist groups in 24+ states. Opposition is bipartisan. https://www.datacenterwatch.org/report
- **2026 political trend [R]:** Wikipedia reports that in 2026 hundreds of local jurisdictions enacted moratoriums and that Virginia's Senate voted to phase out the state's data center sales-tax exemption. https://en.wikipedia.org/wiki/Data_center (verify specifics).
- **Lordstown, OH [V]:** A ban on future data centers was reported by Epoch, and the Saline Township, MI site faced local opposition.

### 4.9 Energy sources: who is betting on what

- **Natural gas dominates the near term.** Behind-the-meter gas runs at Colossus (turbines), Stargate Shackelford (700 MW of VoltaGrid reciprocating engines) and Stargate New Mexico (gas microgrids). Utilities are building new combined-cycle plants for Hyperion (Entergy) [V/R]. Turbine makers (GE Vernova, Siemens Energy, Mitsubishi Power) report multi-year backlogs. Lead times for large turbines ordered in 2025–26 are often reported around 2029–2030 [M; verify against GE Vernova's Q3 2026 results on Oct 28, 2026].
- **Nuclear:**
  - Existing plants: Talen–Amazon at Susquehanna (~1.9 GW) [M], Constellation–Meta at Clinton [V], Vistra–Meta at Perry and Davis-Besse [V].
  - Restarts: Crane/TMI-1 for Microsoft [R], Duane Arnold for Google [R], Palisades (Holtec) [M].
  - SMRs and advanced reactors: Google–Kairos [R], Amazon–X-energy [M], Meta–Oklo and TerraPower [V].
  - **The NRC issued the first US construction permit for a BWRX-300 SMR, at TVA's Clinch River site, on Sept 28, 2026** [V headline: https://www.gevernova.com/news/press-releases].
  - As of 2026, only China and Russia operate SMRs [R]. https://en.wikipedia.org/wiki/Small_modular_reactor
- **Solar + storage and wind:** Still the largest source of new US capacity. EIA expects US solar capacity to go from 152 GW (2025) to 182 GW (2026) to 223 GW (2027) [V]. Developers pair solar and batteries with data centers (Milam County Stargate, Port Washington's claimed 70% renewables) [V].
- **Geothermal and fuel cells:** Enhanced geothermal deals (e.g. Google–Fervo) and Bloom Energy fuel cells for fast on-site power (AEP, Oracle, Brookfield deals) [M].

### 4.10 Water and environment

- **US data centers' direct water use was ~17 billion gallons per year** (LBNL), with much more used *indirectly* by power plants [M/R]. Virginia data centers used ~2.1 billion gallons in 2023, about a third of it reclaimed water [R]. https://en.wikipedia.org/wiki/Data_center
- **Google [R]:** Water consumption rose to 10.9 billion gallons in 2025, with ~78% of freshwater replenished. It uses air-cooled designs at water-scarce sites (Mesa, AZ; Canelones, Uruguay). https://en.wikipedia.org/wiki/Google_data_centers
- **Global data center CO₂ [R]:** ~220 Mt in 2024, projected to reach 300–320 Mt by 2035 (IEA via Wikipedia).
- **Air quality:** Unpermitted turbines at xAI and diesel generator fleets in Northern Virginia are the flagship local-pollution stories [R].

### 4.11 Space and offshore data centers

- **Google Project Suncatcher (Nov 4, 2025) [V]:** Solar-powered TPU satellites in a dawn–dusk sun-synchronous orbit linked by free-space optics. A bench demo reached 1.6 Tbps. A Trillium TPU survived radiation testing well beyond the expected 5-year dose. The economics roughly work if launch costs fall below ~$200/kg in the mid-2030s. Two prototype satellites with Planet are due by early 2027. Thermal management and ground links remain unsolved. https://research.google/blog/exploring-a-space-based-scalable-ai-infrastructure-system-design/
- **Starcloud** (Nvidia-backed startup) flew an H100 in orbit in November 2025 [M]. SpaceX (which now owns xAI) has publicly promoted orbital AI compute [M/R].
- **Underwater/offshore:** Microsoft's Project Natick (2015–2020 trials, then ended) and China's commercial underwater modules off Hainan [M]. Teach the trade-offs: free ocean cooling vs. maintenance, corrosion and permitting.

### 4.12 Sovereign AI

- Gulf: UAE (Stargate UAE / 5 GW campus) and Saudi Arabia's **Humain** (PIF-owned, founded May 2025, plans "several gigawatts"; Nvidia/AMD/Qualcomm partnerships) [R]. https://en.wikipedia.org/wiki/Humain
- Europe: EU "AI gigafactories" under InvestAI [M]; Stargate Norway [M]; Google's ~€13B Finland commitment (September 2026) [R].
- Asia: India (Google Visakhapatnam ~$15B; national GPU programs) [R]; Malaysia's Johor cluster (DayOne Nusajaya ~473 MW IT, among Epoch's top 5 worldwide) [V].
- The drivers are data residency, national security, energy availability (the Gulf and Nordics have cheap power) and access to chips under US export rules.


---

## 5. Diagram ideas (26)

1. **"Where your chat goes."** A phone on the left, then arrows through a cell tower → fiber → internet exchange → a data center campus → a single rack → a single GPU. The answer travels back. Label approximate distances and times (milliseconds) and the ~0.3 Wh energy per answer.
2. **Ladder of power (log scale).** A vertical log axis from 1 W to 10 GW with icons: LED bulb (10 W), laptop (60 W), hair dryer (1.5 kW), average US home (1.2 kW average), H100 GPU (0.7 kW chip / ~1.4 kW all-in), 2015 server rack (8 kW), GB200 rack (~130 kW), Kyber-era rack (~600 kW–1 MW), Colossus 1 (~150 MW), Abilene (1.2 GW), Hyperion target (5 GW), Ireland's average demand (~3–4 GW).
3. **Power vs energy.** A speedometer labeled "kW = rate" beside an odometer labeled "kWh = amount," with a worked example: 1 GW for 1 year = 8.76 TWh.
4. **Campus aerial cutaway.** A site plan with the high-voltage line arriving at the substation yard, generator yard, cooling yard (dry coolers/towers), two data halls, admin/NOC, security gate, fiber entrances (two diverse paths) and water tanks. Callouts give typical acreage.
5. **The power path from grid to GPU.** A horizontal chain of boxes with the voltage under each: transmission line (345 kV AC) → substation transformer → MV switchgear (34.5 kV) → MV/LV transformer → LV switchgear (480/415 V) → UPS with battery string → busway/PDU → rack power shelf (AC→54 V DC) → board VRMs (~1 V) → GPU. Side branch: generators + ATS. Show losses (% heat) at each conversion.
6. **The same path with 800 V DC.** Stack it above diagram 5 to show the steps that disappear: rectification moves to the row/facility level and 800 V DC goes to the rack, with less copper and fewer conversions. Label "2027+ (Nvidia Kyber)."
7. **Outage timeline.** A time axis from 0 to 60 seconds after a grid failure. UPS batteries carry the load instantly. Generators start (~10 s), sync and take load (~15–30 s). The ATS transfers. Then the grid returns and power transfers back. Show what fails in a site without each layer.
8. **Redundancy patterns.** Four mini-diagrams of N, N+1, 2N and 2N+1 using icons (e.g. chillers or UPS modules) with "what happens if one fails" annotations. Add an inset of the Tier I–IV ladder with annual downtime.
9. **The heat path from GPU to atmosphere (liquid-cooled).** GPU die → cold plate → rack manifold → CDU (heat exchanger) → facility water loop → chiller *or* dry cooler/cooling tower → outside air. Label temperatures at each step (e.g. chip ~80 °C, supply water ~30–40 °C). Parallel thin arrows show the residual air-cooled heat (fans → CRAH).
10. **Air-cooled hall cross-section.** Raised floor plenum, perforated tiles, cold aisle, racks, hot aisle with containment, return plenum and CRAH units. Blue and red arrows show airflow, and a callout explains why it tops out around 30–50 kW per rack.
11. **Cooling technology spectrum.** A horizontal bar from "room AC" to "two-phase immersion," with max rack density, typical PUE, water use, and cost/complexity under each option.
12. **Evaporative vs dry vs chiller trade-off triangle.** Corners labeled water use, electricity use and climate suitability, with each cooling method plotted inside. It teaches that saving water usually costs electricity and vice versa.
13. **PUE pie charts.** Three pies: an old enterprise room (PUE 2.0: half overhead), the industry average (~1.55), and a hyperscale AI site (~1.1). Slices for IT, cooling, power losses and lighting.
14. **Rack anatomy.** A front-and-side exploded view of an NVL72-style rack: compute trays, NVLink switch trays, power shelves, liquid manifolds, busbar, top-of-rack network, weight (~1.5 t) and power (~130 kW). Compare it with a 2015 rack drawn beside it.
15. **Spine-leaf network.** Servers at the bottom, leaf switches above, spine switches on top, every leaf linked to every spine. Highlight one path between two servers (2–4 hops). An inset shows the "scale-up" NVLink domain inside a rack as one big box.
16. **Three networks of an AI cluster.** Color-coded overlay: the scale-up network (NVLink, inside the rack), the back-end scale-out network (InfiniBand/Ethernet linking GPUs across racks), and the front-end network (users, storage, internet). Optical transceivers are shown as small light-bulb icons.
17. **Multi-campus "AI WAN."** A US map with Fairwater Wisconsin and Atlanta (~700 miles apart) linked by thick fiber lines. Label the latency (~5 µs/km → ~6 ms one-way over ~1,200 km of fiber) and explain what can and can't be split across sites.
18. **The US grid map of data center regions.** Shade the ISOs (PJM, ERCOT, MISO, SPP, etc.) and overlay megaprojects: Abilene, Shackelford, Milam, Doña Ana, Port Washington, Saline, Memphis/Southaven, New Albany, Richland Parish, New Carlisle, Mount Pleasant, Atlanta, Pryor. Size the bubbles by GW.
19. **Interconnection queue funnel.** A wide top ("thousands of requests / ~2,000+ GW") narrows through feasibility study → system impact study → facilities study → interconnection agreement → construction → operation (only a minority complete). Add a timeline of ~4–5+ years.
20. **Who pays for a new data center's power (money-flow diagram).** Data center ↔ utility (tariff, minimum take, collateral). Utility ↔ regulator (rate case). Utility → all ratepayers (shared transmission and capacity costs). PJM capacity market → bills. Mark where "cost shifting" can occur.
21. **Energy-source comparison matrix.** Rows: gas CCGT, gas recip/aero, solar+storage, wind, existing nuclear, nuclear restart, SMR, geothermal, fuel cell. Columns: years to first power, firmness, carbon, cost ($/MWh band), land, water, and main bottleneck.
22. **Front-of-meter vs behind-the-meter vs co-location.** Three panels. (a) Grid-connected DC. (b) DC with its own on-site turbines and no grid. (c) DC fenced next to a nuclear plant with a direct feed. Pros and cons are listed under each.
23. **Development timeline Gantt chart.** Bars for land acquisition, power application, zoning/permits, design, long-lead procurement (transformers 2–4 yrs, turbines ~3–5 yrs), construction (12–24 months), commissioning (L1–L5), and rack-and-stack. Show the critical path running through power, not the building.
24. **Stack of an AI dollar.** Stacked bars for a hypothetical 1 GW campus: land and shell, electrical, mechanical, power generation (if BTM), network, GPUs/servers. The GPU share dominates. A second bar shows annual opex: power, staff, maintenance, depreciation.
25. **Financing structure of an SPV deal (Hyperion-style).** Investors/bondholders → SPV (owns the data center) ← construction. The SPV leases to the tech company, and lease payments flow to bondholders. The tech company holds a minority stake plus a residual value guarantee. Dashed lines show what stays off the tech company's balance sheet.
26. **Circular deal web.** Nodes for Nvidia, AMD, OpenAI, Anthropic, Microsoft, Amazon, Google, Oracle, CoreWeave and Nebius. Arrows labeled "invests $," "buys chips," "rents compute" and "commits $X over Y years." This shows money flowing in loops.
27. **Space data center concept.** A satellite with a solar array, a large radiator panel, TPUs inside, and optical laser links to neighbors in tight formation. Ground station downlinks are labeled with the challenges (heat only leaves by radiation, launch cost, repair).

---

## 6. Practical exercises (sorted easy → hard)

1. **Unit warm-up (5 min).** Find the wattage label on three devices at home (phone charger, microwave, TV). Compute the energy each uses in a day in Wh and kWh, then price it at your electricity rate. *Learn:* power vs energy.
2. **How many homes is a gigawatt?** Look up your own annual household electricity use on a bill (or use the US average of ~10,500 kWh/yr). Divide by 8,760 hours to get average kW. Then compute how many homes 1 GW would supply (~800,000+ for the US average). Repeat for Hyperion's 5 GW. *Learn:* scale, and that "GW" is a rate.
3. **The energy of your chats.** Estimate how many chatbot messages you send per day. Multiply by 0.3 Wh (Epoch/OpenAI estimates) and by 3 Wh (the old pessimistic estimate). Compare the total with boiling a kettle (~0.1 kWh) or a 10-mile drive in an EV (~3 kWh). Then try a long-document query (~40 Wh for 100k tokens). *Learn:* individual footprint is small, context length matters, and scale is what counts.
4. **Find data centers near you.** Use Google Maps satellite view, plus a public map such as datacentermap.com or Baxtel. Search your county name + "data center." Identify the substation, generator yard and cooling equipment from above. *Learn:* to recognize the physical anatomy.
5. **Read a GPU price list.** Open two or three GPU cloud price pages (e.g. Lambda, RunPod, AWS/Azure/GCP GPU instances). Make a table of $/GPU-hour for H100, H200, B200 and A100. Compute the cost of renting 8 H100s for one week, and 1,000 H100s for one month. *Learn:* on-demand pricing, cluster premiums, and the scale of AI budgets.
6. **PUE calculator.** In a spreadsheet: IT load = 100 MW. Compute the facility load at PUE 2.0, 1.5, 1.2 and 1.1. Then compute the annual electricity cost at $0.07/kWh. *Learn:* why operators fight over decimal points. The 1.5 vs 1.1 difference is ~350 GWh/yr, about $25M/yr.
7. **Racks to megawatts.** A hall has 200 racks at 132 kW each. What is the IT load? With PUE 1.25, what does the utility need to supply? How many 2.5 MW generators are needed for N+1? *Learn:* how designers size infrastructure.
8. **GPUs per gigawatt.** Assume ~1.4 kW per H100 all-in, then ~2.2 kW per Blackwell GPU all-in. How many GPUs fit in 1 GW of facility power? Compare with Epoch's figures (e.g. Abilene 1.2 GW ≈ 1M H100-equivalents). *Learn:* the link between chips and power.
9. **Water math.** A 100 MW IT site uses evaporative cooling at a WUE of 1.8 L/kWh, vs a closed loop at 0.1 L/kWh, vs AWS's quoted 0.15 L/kWh. Compute annual liters and Olympic pools (2.5 million L each). Then add indirect water from power generation, assuming ~2 L/kWh for a thermal-heavy grid. *Learn:* direct vs indirect water, and the water–electricity trade-off.
10. **Read your utility bill like an analyst.** Find the line items: energy charge, delivery/distribution, transmission, capacity or riders. Check your utility's regulatory filings or news for "large load tariff" or "data center tariff." *Learn:* where data center costs could show up in household bills.
11. **Explore a capacity market.** Find PJM's Base Residual Auction results (pjm.com). Chart the clearing price ($/MW-day) from 2022/23 to 2027/28. Convert $/MW-day into $/kW-year and estimate the effect on a home with a 5 kW peak. *Learn:* how a market three years ahead turns data center growth into today's bills.
12. **Read an interconnection queue.** Download your ISO's public queue (e.g. ERCOT's large-load reports, PJM's or MISO's generation queues). Filter by county, fuel type and status. Count gigawatts of solar, storage, gas and wind, and how many are "withdrawn." *Learn:* what grid bottlenecks look like in data.
13. **Satellite time-lapse of a megaproject.** Use Google Earth Pro's historical imagery (free) or Sentinel Hub EO Browser. Track Abilene, TX or Richland Parish, LA from 2023 to now. Count buildings, cooling units and turbines. Compare with Epoch's published estimates. *Learn:* open-source intelligence (OSINT), and how analysts like Epoch estimate capacity.
14. **Cost-to-build spreadsheet.** For a 100 MW (IT) facility, use $11–18M/MW for the building and electromechanical systems (JLL/Cushman), plus ~$25M/MW for AI fit-out where relevant. Estimate GPU cost per MW: e.g. ~450 Blackwell-class GPUs per MW at ~$50k each all-in with server and network, or about $22M/MW. *Learn:* why chips dominate, and why "$50B per GW" is plausible.
15. **GPU-hour break-even.** Assume a GPU's all-in cost (server share + network) is $50,000, depreciated over 5 years. Add power at 2 kW × $0.08/kWh and a facility lease of $180/kW-month. Compute the cost per GPU-hour at 100%, 70% and 50% utilization, and compare with market rental prices. *Learn:* unit economics, and why utilization and depreciation life are everything.
16. **Cost per million tokens.** Microsoft says one GB200 NVL72 rack can do ~865,000 tokens/second. Assume $4/GPU-hr × 72 GPUs. Compute the cost per million tokens at 100%, 50% and 25% effective throughput (≈$0.09, $0.19 and $0.37). Compare with published API prices of several models. *Learn:* the gap between raw compute cost and price (model size, margins, peak vs average load, R&D recovery).
17. **Build a capex tracker.** Make a sheet with Alphabet, Amazon, Meta, Microsoft and Oracle quarterly capex from earnings releases or 10-Qs (investor relations sites). Add revenue and operating cash flow, and compute capex as a % of operating cash flow. *Learn:* to read primary financial disclosures, and how close capex is to cash generation (Amazon's capex reportedly exceeded its operating cash flow in Q2 2026).
18. **Site selection scorecard.** Pick three candidate counties (e.g. one in Texas, one in Virginia, one in Wyoming). Score each 1–5 on power availability and price (EIA state data), fiber, water stress (WRI Aqueduct), climate (cooling degree days), tax incentives (state economic development pages), and community sentiment (local news). Weight the scores and pick a winner. *Learn:* the multi-factor trade-off that real site selectors make.
19. **Energy-source decision memo.** You need 500 MW firm by 2028. Compare gas turbines (on-site), a grid connection, solar + 4-hour batteries + gas backup, and waiting for SMRs. Cover time-to-power, $/MWh, carbon and risk. Write a one-page recommendation. *Learn:* why gas wins near-term despite climate goals, and what would change that.
20. **Bubble debate worksheet.** List the bull arguments (backlogs like AWS's $496B, demand exceeding supply per Microsoft/Amazon) and the bear arguments (debt, SPVs, circular deals, depreciation, Oracle's downgrade). Find one historical analogy (1990s fiber glut, 1840s railway mania), note how it ended, and decide what would convince you either way. *Learn:* critical thinking about finance.
21. **Design a 50 MW AI hall (capstone).** Specify rack count and density, power chain (with redundancy level), cooling method, PUE target, backup duration, network layout and water plan. Draw your own versions of diagrams 5 and 9. *Learn:* how it all fits together.

---

## 7. Areas of opportunity

### Careers (from fastest entry to longer training)
- **Skilled trades (high demand, short training):** electricians (inside wiremen, the biggest constraint at many sites), linemen/high-voltage lineworkers, pipefitters and HVAC technicians (liquid cooling is plumbing), controls technicians, welders, ironworkers, low-voltage/fiber technicians (splicing, testing), heavy-equipment operators. The US median electrician wage was about $62k in 2024 (BLS), but data center megaprojects often pay large premiums, per diem and overtime [M].
- **Data center operations:** critical facilities technician/engineer, data center technician ("remote hands," rack-and-stack, GPU replacement), NOC operator, commissioning agent/technician, EHS (safety) specialist, security.
- **Engineering:** electrical engineers (power systems, protection, MV/HV design), mechanical engineers (thermal and liquid cooling), controls/BMS engineers, structural/civil engineers, fire protection engineers, network/optical engineers, power electronics engineers (800 V DC, solid-state transformers), reliability engineers.
- **Energy and grid:** interconnection specialists, transmission planners, utility large-load account managers, energy developers (solar, storage, gas, nuclear), power traders and PPA originators, rate analysts and regulatory attorneys, nuclear operators and engineers (restarts and SMRs need people), grid-modeling software specialists.
- **Real estate and development:** site selectors, land acquisition and entitlement specialists, permitting and environmental consultants, community relations/public affairs, construction project managers and schedulers, procurement/supply-chain managers for long-lead gear.
- **Finance and strategy:** project finance, infrastructure private equity, private credit underwriting of data centers and GPU loans, equity research on AI infrastructure, FinOps/GPU capacity planning, compute brokers and marketplaces.
- **Policy and public interest:** state energy offices, PUC staff, local planning boards, environmental justice advocates, water resource planners, journalists and OSINT analysts tracking build-outs (Epoch-style).

### Businesses and niches
- **Speed-to-power:** bridge power (mobile turbines, recip engines, fuel cells), battery systems for load smoothing, microgrid developers, "powered land" developers who secure interconnection and resell sites.
- **Cooling:** CDUs, cold plates, quick-disconnects, leak detection, dry coolers, two-phase fluids, immersion, rear-door heat exchangers, water treatment, and heat-reuse projects (district heating, greenhouses, aquaculture).
- **Electrical gear:** transformers (domestic manufacturing is scarce), switchgear, busway, 800 V DC power shelves, solid-state transformers, supercapacitors.
- **Software:** DCIM, digital twins for thermal and power design, GPU scheduling for utilization, grid-aware workload shifting (demand response), carbon/water accounting, interconnection-queue analytics, permitting automation.
- **Services:** commissioning firms, specialized staffing/training (electrician bootcamps), GPU maintenance/RMA logistics, decommissioning and resale of used GPUs (a secondary market), insurance for GPU fleets.
- **Local:** suppliers, catering/lodging for construction crews, community benefit programs, and community colleges' data center technician programs.

### Skills in demand
High-voltage safety and NFPA 70E; liquid-cooling installation and maintenance; fiber splicing and testing; power-system modeling (ETAP, PSS/E); thermal/CFD modeling; project scheduling (Primavera P6); utility regulation literacy; reading single-line diagrams; spreadsheet financial modeling (capex/opex/IRR); data analysis of public datasets (EIA, ISO queues); clear communication with communities.

### Open problems (good for "frontier" chapter boxes)
1. **Interconnection speed:** how to connect gigawatts in 2 years instead of 5–7 without shifting costs onto households.
2. **Flexible AI load:** can training jobs throttle on grid stress days so data centers become grid assets? This lets more load connect without new peak capacity.
3. **Power swings:** synchronized GPU loads swing tens of MW in seconds. They need standards and storage so grids stay stable.
4. **1 MW racks:** cooling, power delivery (800 V DC safety), floor loading, and serviceability at that density.
5. **Firm clean power at speed:** SMR cost and timeline (first US units ~2030), enhanced geothermal scale-up, long-duration storage, and gas with carbon capture.
6. **Supply chains:** transformers, turbines, switchgear, HBM memory and optics, plus domestic manufacturing capacity.
7. **Measurement transparency:** standard, audited per-query/per-token energy and water disclosure. Today's numbers are company self-reported.
8. **Heat reuse economics:** AI heat is low-grade (30–60 °C), and finding nearby users is hard.
9. **Water in drylands:** zero-water cooling without big electricity penalties.
10. **Economic durability:** GPU useful life, residual values, utilization over a full cycle, and debt risk if demand slows.
11. **Distributed training:** training one model across multiple campuses hundreds of miles apart. This sidesteps single-site power limits.
12. **Fair siting:** community benefits, tax policy, and environmental justice (Memphis is the case study).
13. **Space and offshore compute:** radiators, maintenance, launch cost, radiation, latency.
14. **Embodied carbon:** concrete, steel and chips. Data center construction's footprint grows with every short-lived GPU generation.

---

## 8. Common misconceptions to correct

1. **"The cloud is in the sky / weightless."** It is concrete, steel, copper, water pipes and gas turbines in specific towns.
2. **"A 1 GW data center uses 1 GW all the time."** GW is a capacity rate. Real use depends on utilization, often 60–80% of capacity on average (Epoch). Energy per year is GW × hours × load factor.
3. **"Each chatbot answer uses a bottle of water / huge energy."** Current company and independent estimates are ~0.24–0.34 Wh and well under 1 mL of on-site water per typical text query. Long contexts, agents, reasoning, images and video cost much more, and totals across billions of queries are what matter.
4. **"AI already uses more electricity than most countries."** All data centers (not just AI) were ~1.5% of global electricity in 2024 (IEA). The concern is local concentration (Ireland 22%, Virginia ~25%) and growth rates.
5. **"Data centers are all AI now."** AI was about a quarter of data center workloads in 2025 (JLL). Email, video streaming, banking and enterprise IT still fill much of the world's capacity.
6. **"PUE 1.1 means the data center is 'efficient' at AI."** PUE measures only building overhead. It says nothing about whether the chips do useful work efficiently, or about water and carbon.
7. **"Closed-loop cooling means zero water."** On-site evaporation can be near zero, but the power plants generating the electricity use (often more) water. Dry cooling also uses more electricity on hot days.
8. **"100% renewable = runs on renewables every hour."** Most claims are annual matching with certificates. Hourly (24/7) matching in the same grid is much harder and rarer.
9. **"Nuclear will power AI soon."** Restarts and uprates help this decade. New SMRs mostly arrive in the 2030s (first US construction permit for a BWRX-300 came only in September 2026), and gas is filling the near-term gap.
10. **"Data centers bring lots of permanent jobs."** Construction employs thousands. A finished hyperscale campus may employ only hundreds. The local benefit is mainly property taxes, which incentives sometimes reduce.
11. **"Electricity price increases are all because of data centers."** Data centers are a big driver in some markets (PJM capacity prices), but so are fuel prices, transmission and wildfire costs, aging plants and retirements.
12. **"GPUs are a 10-year asset like the building."** Buildings last 15–25+ years (Microsoft now uses 25). GPUs are depreciated over ~5–6 years and may lose economic value faster as new generations arrive yearly.
13. **"Training uses most AI energy."** Training is spiky and visible, but inference (serving users) is growing into the majority of AI compute. JLL expects inference to overtake training around 2027.
14. **"Space is cold, so space data centers cool easily."** Vacuum is an insulator. Heat leaves only by radiation, which needs large radiators. Launch cost and repair are the other big hurdles.
15. **"Backup generators can just run the data center when the grid is short."** Air permits limit generator hours. Diesel fleets are for emergencies, though some regions now encourage using them during grid emergencies to relieve the grid.
16. **"Bigger GPU cluster = linearly smarter AI."** Power and chips are necessary but not sufficient. Algorithms, data and utilization matter (link to the scaling-laws chapter).
17. **"70% of the world's internet traffic flows through Northern Virginia."** This is a popular but unsupported claim. Virginia is the world's largest data center market, but the statistic is not well sourced.
18. **"Colocation" and "co-location" are the same.** Colocation is renting data center space. Co-location (in power) is siting a data center at a power plant. They are different debates.
19. **"Hyperscalers pay for everything with cash."** In 2026, capex at several firms rivals or exceeds operating cash flow, and they are raising debt and equity and using SPVs and leases (FactSet, Alphabet's $80B equity program, Oracle's debt).

---

## 9. Analogies that work for beginners

- **Electricity as water in pipes:** voltage = water pressure, current = flow rate, wire thickness = pipe width, resistance = friction, power = pressure × flow.
- **Watts vs watt-hours:** speed (mph) vs distance (miles). "1 GW for a year" is like driving at a set speed for a set time.
- **Transformer:** a gearbox for electricity. It trades voltage for current, like a bicycle trades pedal speed for force.
- **The power chain:** a river delta. A mighty river (transmission line) splits into canals (MV), streets (LV) and garden hoses (rack power), down to a drip line (each chip).
- **UPS and generators:** a car's battery starts the engine; the UPS keeps the lights on for the seconds it takes the generator "engine" to start.
- **N+1 vs 2N:** N+1 is carrying a spare tire. 2N is owning two complete cars. Tier IV is two cars with two drivers, each able to finish the trip alone.
- **Data center as a restaurant kitchen:** the stoves (GPUs) do the cooking. Ventilation hoods and AC (cooling) and the gas line and electrical panel (power) are the infrastructure. PUE is how much energy goes to everything except cooking.
- **Air vs liquid cooling:** a fan blowing on you vs jumping into a pool. Water carries heat away thousands of times better per volume.
- **Cold plate + CDU:** a car's radiator system. Coolant flows past the hot engine (chip) and to the radiator (heat exchanger), and a fan blows the heat outdoors.
- **Hot/cold aisles:** keeping the fridge door closed. Don't let warm and cold air mix.
- **Rack density growth:** fitting a whole suburban street's electricity use (~130 kW ≈ 100 homes) into a refrigerator-sized cabinet.
- **Spine-leaf network:** a highway system where every local road (leaf) has an on-ramp to every highway (spine), so any trip takes at most a couple of interchanges.
- **Scale-up vs scale-out:** scale-up is a team in one room shouting to each other (NVLink). Scale-out is teams in different buildings on phone calls (InfiniBand/Ethernet). Scale-across is offices in different cities on video calls.
- **Interconnection queue:** a waiting list at a popular restaurant where each party must also pay to have the kitchen expanded before being seated.
- **Capacity market:** paying a reservation fee years ahead so a power plant promises to be available on the hottest day.
- **PPA:** a long-term fixed-price phone plan, or a farmer selling next decade's harvest in advance so the farm can get a loan.
- **Behind-the-meter power:** digging your own well instead of using city water, which is faster but you maintain it and answer for its pollution.
- **Hyperscaler vs neocloud vs colocation:** a hyperscaler is a city that owns its buildings. A neocloud is a hotel chain renting rooms (GPUs) by the night or year. Colocation is self-storage: you rent the unit and bring your own stuff.
- **Utilization:** hotel occupancy. Empty rooms still cost money.
- **GPU depreciation:** a new car losing value when a newer model comes out every year.
- **SPV financing:** a separate "holding box" company that owns the building and borrows money. The tech giant rents from it, so the debt doesn't sit on the giant's own balance sheet. It's like a parent co-signing a lease for a child's apartment rather than buying it.
- **Circular deals:** a store lending you money to buy its own products, which boosts its sales figures. Fine if you can repay, risky if you can't.
- **Gigawatt campus:** a city's worth of electricity, roughly 800,000 average US homes, delivered to one fenced site.
- **Space data center:** a solar-powered satellite is a laptop in a thermos. It gets plenty of power but has a hard time shedding heat.
- **Interconnecting campuses with fiber:** even light needs ~5 milliseconds to cross 1,000 km of fiber, an eternity for GPUs that sync thousands of times a second.

---

## Source list (primary URLs used in this file)

- Epoch AI data center hub (Oct 20, 2026 data): https://epoch.ai/data/data-centers
- Epoch AI, Stargate sites (April 2026): https://epoch.ai/publications/openai-stargate-where-the-us-sites-stand
- Measured AI, Stargate site-by-site (March 31, 2026): https://measuredai.substack.com/p/stargate-site-by-site-status
- Epoch AI, ChatGPT energy (Feb 2025): https://epoch.ai/gradient-updates/how-much-energy-does-chatgpt-use
- Google, AI inference footprint (Aug 21, 2025): https://cloud.google.com/blog/products/infrastructure/measuring-the-environmental-impact-of-ai-inference
- Sam Altman, "The Gentle Singularity": https://blog.samaltman.com/the-gentle-singularity
- FactSet, hyperscaler financing (July 23, 2026): https://insight.factset.com/hyperscalers-tap-external-financing-as-ai-capex-outruns-cash-flow
- Microsoft Q4 FY26 call transcript: https://www.fool.com/earnings/call-transcripts/2026/08/07/microsoft-msft-q4-2026-earnings-call-transcript/
- CFO Dive, Microsoft capex (July 30, 2026): https://www.cfodive.com/news/microsoft-holds-line-ai-spending-plans/826648/
- Alphabet SEC filings (June 2026 equity raise): https://www.sec.gov/Archives/edgar/data/0001652044/000119312526257724/d83560dex991.htm and https://www.sec.gov/Archives/edgar/data/0001652044/000119312526251733/d160205dfwp.htm
- Alphabet capex raise (July 2026): https://www.outlookbusiness.com/corporate/google-parent-alphabet-doubles-down-on-ai-plans-up-to-205-billion-in-2026-capex
- Amazon capex/AWS backlog (July 2026): https://letsdatascience.com/news/aws-revenue-growth-outruns-available-ai-capacity-b0361d90
- Meta Q2 2026: https://www.storagenewsletter.com/2026/07/30/meta-platforms-fiscal-2q26-financial-results/
- 2025 capex retrospective: https://platformonomics.com/?p=34926
- Microsoft Fairwater: https://blogs.microsoft.com/blog/2025/09/18/inside-the-worlds-most-powerful-ai-datacenter/ ; Atlanta: https://w.media/?p=186700
- Meta nuclear (Jan 2026): https://about.fb.com/news/2026/01/meta-nuclear-energy-projects-power-american-ai-leadership/
- Meta Hyperion: https://www.datacenterknowledge.com/data-center-construction/meta-s-5-gw-hyperion-campus-signals-ai-s-shift-into-utility-territory ; https://en.wikipedia.org/wiki/Hyperion_Data_Center
- xAI/Colossus: https://en.wikipedia.org/wiki/Colossus_(data_center) ; https://en.wikipedia.org/wiki/XAI_(company) ; https://www.selc.org/news/xai-built-an-illegal-power-plant-to-power-its-data-center/ ; further reading: https://newsletter.semianalysis.com/p/xais-colossus-2-first-gigawatt-datacenter
- Anthropic compute: https://www.anthropic.com/news/google-broadcom-partnership-compute ; https://www.anthropic.com/news/anthropic-amazon-compute ; https://techcrunch.com/2026/04/07/anthropic-compute-deal-google-broadcom-tpus/ ; https://www.constellationr.com/insights/news/anthropic-microsoft-azure-nvidia-ink-30-billion-compute-pact
- Amazon Project Rainier: https://www.aboutamazon.com/news/aws/aws-project-rainier-ai-trainium-chips-compute-cluster
- OpenAI deals: https://www.cnbc.com/2026/01/16/openai-chip-deal-with-cerebras-adds-to-roster-of-nvidia-amd-broadcom.html ; https://www.business-standard.com/technology/tech-news/nvidia-30bn-openai-investment-after-shelving-100bn-deal-126022000503_1.html ; https://en.wikipedia.org/wiki/Stargate_LLC
- Nvidia 800 V DC: https://developer.nvidia.com/blog/nvidia-800-v-hvdc-architecture-will-power-the-next-generation-of-ai-factories/ ; https://developer.nvidia.com/blog/building-the-800-vdc-ecosystem-for-efficient-scalable-ai-factories/
- Google Project Suncatcher: https://research.google/blog/exploring-a-space-based-scalable-ai-infrastructure-system-design/
- GPU prices: https://lambda.ai/pricing ; https://www.runpod.io/pricing
- Build costs and market: https://www.jll.com/en-us/insights/market-outlook/data-center-outlook ; https://www.cushmanwakefield.com/en/united-states/insights/data-center-development-cost-guide
- EIA STEO (Oct 2026): https://www.eia.gov/outlooks/steo/report/elec_coal_renew.php
- Ireland CSO: https://www.cso.ie/en/releasesandpublications/ep/p-dcmec/datacentresmeteredelectricityconsumption2024/
- Data Center Watch: https://www.datacenterwatch.org/report
- IEA Energy and AI: https://www.iea.org/reports/energy-and-ai ; LBNL: https://eta.lbl.gov/publications/2024-lbnl-data-center-energy-usage-report ; LBNL Queued Up: https://emp.lbl.gov/queues (not re-fetched; blocked)
- Neoclouds: https://en.wikipedia.org/wiki/CoreWeave ; https://en.wikipedia.org/wiki/Nebius_Group
- Background: https://en.wikipedia.org/wiki/Data_center ; https://en.wikipedia.org/wiki/Google_data_centers ; https://en.wikipedia.org/wiki/Three_Mile_Island_Nuclear_Generating_Station ; https://en.wikipedia.org/wiki/Small_modular_reactor ; https://en.wikipedia.org/wiki/Humain ; https://en.wikipedia.org/wiki/PJM_Interconnection ; https://www.gevernova.com/news/press-releases

**Items to re-verify before publication:** the Q3 2026 earnings (late October 2026) for capex; PJM auction figures; the status of Stargate UAE's first 200 MW; the Anthropic/Google leasing of SpaceX Colossus capacity; the Crane restart date; the PORTS-Pike Stargate site; the Stargate UK pause; gas-turbine backlog figures (GE Vernova Q3, Oct 28, 2026).
