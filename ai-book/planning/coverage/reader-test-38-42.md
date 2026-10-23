# Reader test: chapters 38, 40, 41 and 42

Tested by reading chapters 38, 40, 41 and 42 in order, in full, as the intended reader: almost no computer-science background, a daily chatbot user for a year, who has read the earlier chapters. (Chapter 39 was tested in the first pass; see reader-test.md.) Every place that reader would get lost was fixed with a small edit: a definition callout, a plain gloss, a bridging sentence, or a clearer exercise instruction. Nothing was rewritten for style and no content was cut. Before each fix I checked GLOSSARY.md and the earlier chapters for an existing definition; a term defined earlier was not counted as a problem.

Every entry for these chapters in acronyms-by-chapter.json was worked through. An organization or product used in three or more chapters got a definition callout in the first of these chapters that uses it (and was added to that chapter's Key terms list); every other entry got a gloss at its first use, or was already glossed in context (noted at the end).

After editing, every edited file passed `validate.py` (all mermaid diagrams valid) and `check.py` (chapters 38, 40, 41 and 42 all `[OK]`).

## Findings and fixes

| Chapter | Where | Problem a beginner would hit | Fix applied |
|---|---|---|---|
| 38 | "Your chatbot lives in a building", H100 paragraph | NVIDIA, and its generation names Hopper, Blackwell and Rubin, are used throughout the book with no definition anywhere | New definition callout: NVIDIA, including the generation names and their chips |
| 38 | Same section, capacity paragraph | JLL (used in 9 chapters) never defined | New definition callout: JLL (Jones Lang LaSalle) |
| 38 | Stop 8, loading dock | "Tonne" may be unfamiliar to US readers, and racks are weighed in tonnes for the rest of the chapter | Added "(1,000 kilograms)" |
| 38 | Floors, weight | "2.4 kN/m²" and "live load" unexplained | Glossed live load and kilonewtons per square meter |
| 38 | Table 38.1 | "GTC 2026" unexplained (used in 4 chapters) | New definition callout: GTC (GPU Technology Conference) |
| 38 | Frontier box after the rack comparison | AMD (22 chapters) and MI455X (9 chapters) never defined | New definition callouts: AMD (Advanced Micro Devices) and MI455X |
| 38 | Figure 38.8 caption | "Tensor and expert parallel traffic" in the diagram has no pointer back to where it is taught | Added "(tensor and expert parallelism, Chapter 37)" |
| 38 | Try it, outage cost | The 30 minutes in the check came from nowhere (20 minutes since the checkpoint plus 10 minutes of outage) | Spelled out the addition |
| 38 | Fire example | OVHcloud unexplained | Glossed as a French cloud provider |
| 38 | Hyperscaler definition | AWS (22 chapters) never defined | New definition callout: AWS (Amazon Web Services) |
| 38 | Converted crypto mines | IREN (3 chapters) only implied to be a miner | New definition callout: IREN |
| 38 | The players | GE (5 chapters, as GE Vernova here and GE Hitachi's BWRX-300 later) never defined | New definition callout: GE (General Electric) |
| 38 | Frontier campus list | "GB200 GPUs" (17 chapters) never defined | New definition callout: GB200 and GB300 |
| 38 | Exercise 2 | No cell locations; a beginner typing 99.9 without % gets nonsense from `=(1-A2)*8760`; no minutes formula | Said where to type the values, to include the % sign, and gave `=B2*60` |
| 38 | Exercise 6 | "EO Browser" unexplained; "historical imagery slider" does not say where it is | Glossed EO (Earth observation); said to use the clock icon in Google Earth Pro or the date in EO Browser |
| 38 | Exercise 9 | Asked for "the cost of an outage" with no outage length, so it cannot be computed | Fixed the outage to the Try it box's numbers and said a rough estimate in words is fine for the other two users |
| 40 | "Every watt becomes heat" | "LEDs" unexplained | Glossed |
| 40 | Two-phase cooling, latent heat | "kJ" used right after joules with no conversion | Added "(kilojoules, thousands of joules)" |
| 40 | Two-phase cooling, drawbacks | PFAS not expanded; why "forever chemicals" not said | Expanded PFAS and glossed "forever" |
| 40 | Idle power, textbook quotation | "WSC" inside the quotation (defined in Chapter 34) | Added "(a warehouse-scale computer, ... Chapter 34)" |
| 40 | CUE worked example | First use of "CO₂" | Added "(carbon dioxide)" |
| 40 | Per-prompt water estimates | "UC Riverside" unexplained | Glossed as the University of California's Riverside campus |
| 40 | Totals and location | Lawrence Berkeley National Laboratory (LBNL, 3 chapters) never defined | New definition callout: LBNL (Lawrence Berkeley National Laboratory) |
| 40 | California veto | "AB 93" unexplained | Added "Assembly Bill 93" |
| 40 | Areas of opportunity | "HVAC" unexplained | Expanded |
| 40 | Exercise 4 | No formulas for airflow, CFM or liters per minute; the cube-law step for fan power not shown | Gave each formula and the 3.25 × 3.25 × 3.25 step |
| 40 | Exercise 7, step 3 | "500 mL per 10 to 50 responses" not turned into a per-response figure | Showed 10 to 50 mL per response, low and high |
| 41 | Data center electricity, hot spots | "EPRI" unexplained | Glossed (Electric Power Research Institute, a utility-funded research group) |
| 41 | Same list | IEA (5 chapters) only spelled out | New definition callout: IEA (International Energy Agency) |
| 41 | Table 41.1 | ERCOT, MISO, SPP, CAISO, NYISO, ISO-NE and TVA are bare acronyms | Added each full name in the table |
| 41 | After Table 41.1 | PJM (5 chapters), the case study of the chapter, is never expanded or defined | New definition callout: PJM (PJM Interconnection), including where the letters come from |
| 41 | Try it, grid mix | EIA (5 chapters) used later only as "the EIA" | New definition callout: EIA (US Energy Information Administration) |
| 41 | Five dimensions, Carbon | First use of CO₂ in the chapter | Added "(carbon dioxide)" |
| 41 | Lifecycle emissions definition, Table 41.3 | "CO₂-equivalent" and "g CO₂e" never explained | Added one sentence to the definition |
| 41 | Natural gas, xAI bullet | NAACP, the two law groups and the Clean Air Act unexplained | Glossed all three |
| 41 | Nuclear restarts | "TMI-1" in Table 41.3 not tied to Three Mile Island Unit 1 | Added "(TMI-1)" at first use |
| 41 | New reactors | NRC (3 chapters) and BWRX-300 (5 chapters) never defined | New definition callouts: NRC (Nuclear Regulatory Commission) and BWRX-300 |
| 41 | Fuel cells | "AEP" unexplained | Added "(American Electric Power)" |
| 41 | Big comparison table intro | "Lazard" unexplained; "IPCC" in the table caption not tied to the full name | Glossed Lazard as an investment bank; added "(IPCC, the United Nations body that assesses climate science)" |
| 41 | 100% solar worked example | "GHG Protocol" not expanded | Added "GHG standing for greenhouse gas" |
| 41 | Flexible loads | "Texas SB 6" unexplained | Added "Senate Bill 6 of the Texas legislature" |
| 41 | Flexible loads worked example | Text says "less than 1%"; the example silently uses 0.5% | Added "Take half that limit" |
| 41 | Forecasts worked example | "1.85× in five years, about 13% growth per year" skips compound growth | Showed 1.13 multiplied by itself five times ≈ 1.84 (and 1.27⁵ ≈ 3.3) |
| 41 | Exercise 4 | "Cumulative capacity" and "marginal plant" not operationalized; adding 300 MW to 1,250 and 1,350 MW exceeds the 1,400 MW total, a case the exercise never mentions | Gave the running total, the rule for finding the marginal plant, and what to write when demand exceeds supply |
| 41 | Exercise 6 | No formula for "the smaller of load and solar"; the battery step is too hard to model hour by hour for a beginner | Gave `=MIN(B2,C2)` and walked through the 800 MWh of battery energy |
| 42 | Choosing a site, JLARC paragraph | "Fiscal 2023" unexplained | Added "(the state's budget year)" |
| 42 | People | "Per diems" unexplained | Glossed |
| 42 | Chips and their parts | SK hynix (8 chapters) and TSMC (14 chapters) never defined | New definition callouts: SK hynix and TSMC (Taiwan Semiconductor Manufacturing Company) |
| 42 | Stargate announcement | SoftBank and SB Energy unexplained; MGX (3 chapters) only glossed | Glossed SoftBank and SB Energy; new definition callout: MGX |
| 42 | Other Stargate sites | "DTE grid" unexplained | Glossed as DTE Energy, the Detroit-area utility |
| 42 | Overseas | "UAE" and "G42" unexplained at first use | Expanded UAE; glossed G42 |
| 42 | Hyperion | "Blue Owl" unexplained | Glossed as an investment firm |
| 42 | Table 42.4 | State postal abbreviations (TX, WI, OH, MS, MI and others) | Listed them in the caption |
| 42 | Grid-aware training | "SB 6" unexplained in this chapter | Added "(Senate Bill 6; see Chapter 41)" |
| 42 | Data centers in space, radiator worked example | "330 kelvin" and the Stefan–Boltzmann law (which Exercise 9 then uses as T^4) unexplained | Glossed kelvin (°C + 273) and what the law says |
| 42 | Areas of opportunity | "GIS mapping" unexplained | Expanded |
| 42 | Exercise 3 | `=SUMPRODUCT(weights, scores)/5` uses placeholders a beginner would type literally; "WRI" unexplained | Gave a version with cell ranges and said what SUMPRODUCT does; glossed WRI |
| 42 | Exercise 4 | Same EO Browser and slider gaps as Chapter 38's Exercise 6 | Same fix |
| 42 | Exercise 6 | Figure 42.4 shows grid power at 60 months, but step 4 says to change it "from 24 to 60"; "power commitment" not mapped to the figure's "new grid power" bar; end-month formula used placeholders | Said to start the grid-power bar at month 0 for 24 months, mapped step 2 to the bar, gave `=B2+C2` |
| 42 | Exercise 9 | Radiator formula's symbols (2, 0.9, 5.67e-8, T^4) unexplained; no spreadsheet form | Explained each symbol, gave the spreadsheet formula and a check value (about 830 m² for 1 MW) |
| 42 | Exercise 10, step 1 | Told to look up the driving distance, then to multiply the straight-line distance by 1.5, which contradict each other | Now measures the straight-line distance with Google Maps and says why fiber is longer |

Fixes per chapter: 38: 17 (9 definition callouts, 3 glosses, 2 bridging steps, 3 exercises), 40: 11 (1 callout, 8 glosses, 2 exercises), 41: 24 (5 callouts, 15 glosses, 2 bridging steps, 2 exercises), 42: 20 (3 callouts, 11 glosses, 1 bridging step, 5 exercises). 72 in total. Eighteen new definitions were added, each to its chapter's Key terms list: NVIDIA, JLL (Jones Lang LaSalle), GTC (GPU Technology Conference), AMD (Advanced Micro Devices), MI455X, AWS (Amazon Web Services), IREN, GE (General Electric), GB200 and GB300 (Chapter 38); LBNL (Lawrence Berkeley National Laboratory) (Chapter 40); IEA (International Energy Agency), PJM (PJM Interconnection), EIA (US Energy Information Administration), NRC (Nuclear Regulatory Commission), BWRX-300 (Chapter 41); SK hynix, TSMC (Taiwan Semiconductor Manufacturing Company), MGX (Chapter 42). No arithmetic error was found: every worked example, table and answer in the four chapters was recomputed and checks out.

## Noticed but not changed

- **Acronyms already glossed in context.** QTS and ABB (Chapters 38 and 42) appear only inside lists headed "colocation developers and landlords" and "power and cooling gear", which tell the reader what they are. SBG2 is called a building, JLARC is "Virginia's legislative watchdog", PORTS is "the decommissioned Portsmouth uranium enrichment plant", and NERC and CFM are spelled out at first use. "MS" in Chapter 42 is also a mermaid node ID that the reader never sees.
- **Possible duplicate definitions.** NVIDIA, AMD, AWS, TSMC and similar companies first appear well before Chapter 38. If the readers of earlier chapters also add callouts for them, the glossary will merge the entries but the wording may differ; whoever builds the glossary may want to keep one wording.
- **Fact-check, Chapter 42 "Corporate changes".** The xAI rebranding to "SpaceXAI (July 2026) and then SpaceXSI (October 2026)" was already flagged for Chapter 44 in the first reader test. It is worth one source check.
- **Small inconsistency.** Figure 38.8 says tensor and *expert* parallel traffic must stay inside each site; Chapter 42's speed-of-light worked example says tensor and *pipeline* parallelism. Both are defensible, but the owner of Part VII may want one phrasing.
- **Chapter 42, Exercise 10.** With its 1.5 × straight-line assumption, the fiber comes out at about 1,600 km (about 8 ms one way), while the chapter's worked example uses about 1,200 km (6 ms). That assumption was left as written; a curious reader may notice the difference.
- **Optional frontier boxes** still name a few things in passing (Open Rack Wide, Trillium, Pathways, VoltaGrid, Starcloud). The sentence around each one says what it is, which is enough for an aside.

## Verdicts

**Chapter 38 (Inside a Data Center).** The ramp works well. The walking-tour structure (site plan, then building, then rack, then networks, then people and money) moves from what you can see to what you have to imagine, and each stop's numbers are small enough to check by hand (the shrinking white space, floor loading, the speed-of-light table, the Tier downtime table). Every technical term had a callout already. The gaps were all names: the chapter leans on NVIDIA, AMD, AWS, JLL and NVIDIA's chip generations as if the reader already knows them, and they had no definition anywhere in the book. With nine company and product callouts and the three exercise fixes, every term is now defined or glossed.

**Chapter 40 (Cooling).** The best-built chapter of the four for this reader. The heat-path staircase, the master equation and the air-versus-water worked example give the reader one idea to hang everything on, and the water section's four distinctions are a model of fair explanation. Every engineering term was already defined. The fixes were stray abbreviations (LED, PFAS, WSC, AB 93, HVAC, kJ) and two exercises that asked for calculations without giving the formula. The ramp works and every term is now defined.

**Chapter 41 (Energy for AI).** The densest chapter for acronyms: the US grid is described through a dozen organizations (PJM, ERCOT, MISO, SPP, CAISO, NYISO, ISO-NE, TVA, EIA, EPRI, NRC, NERC, IEA), most of them never expanded. The reasoning itself ramps well: the merit-order toy, the capacity-price-to-household-bill conversion and the "100% solar" hourly-matching day are exactly the right size for a beginner. Compound growth was the one real arithmetic jump. With five callouts and fifteen glosses, every term is defined, and the merit-order and matching exercises can now be done by someone who has never built a spreadsheet model.

**Chapter 42 (The Great Buildout).** A synthesis chapter, and it reads as one: it re-defines the Part VII terms it needs (gigawatt, IT power, PPA, SMR, interconnection) so it can be read on its own. Its difficulty lies in the volume of company and place names rather than in the concepts. Most were already glossed; SK hynix, TSMC and MGX needed callouts, and a handful of names and abbreviations needed a few words. The exercises had the most mechanical problems of the four chapters (placeholders, a contradictory distance instruction, a Gantt exercise whose numbers clashed with its own figure, a physics formula with unexplained symbols). All five are fixed. The ramp works, and every term is now defined.
