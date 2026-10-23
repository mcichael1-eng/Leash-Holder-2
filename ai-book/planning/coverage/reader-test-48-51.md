# Reader test: chapters 48 to 51

I read chapters 48 (Reinforcement Learning, Games and Planning), 49 (Robotics and Physical AI), 50 (Self-Driving Vehicles) and 51 (Recommenders, Search and Ads) in order, in full, as the intended reader. That reader is smart and curious, uses a chatbot every day, knows school arithmetic and nothing about programming, hardware or the industry, and has read chapters 1 to 47. Before treating a term as undefined, I checked GLOSSARY.md and grepped the current chapter files, since other agents were adding definitions at the same time. I went through every entry for these chapters in acronyms-by-chapter.json.

I recomputed every worked example, table value and exercise answer. I also ran both Colab programs: chapter 48's Q-learning agent prints a start value of 1.81 on every run, and chapter 51's matrix factorization falls to an RMSE of 0.030 with the factors the text describes. The PageRank exercise values (0.38 after adding D to A, and D about 0.07 with spam pages) were checked by script. All edits are small and surgical. After editing, `validate.py` passes on all four files (7/7, 8/8, 7/7 and 8/8 diagrams valid) and `check.py` reports `[OK]` for chapters 48, 49, 50 and 51.

## Findings and fixes

| Chapter | Where | Problem a beginner would hit | Fix applied |
|---|---|---|---|
| 48 | A* section, Shakey paragraph | "SRI" is used later ("the SRI robot") but the text never connects it to "Stanford Research Institute"; SRI appears in three or more chapters and is not in the glossary | Added "(SRI)" at first use and a definition callout: SRI (SRI International) |
| 48 | Blind search, bidirectional search | The jump from "half the distance" to 2 × 10^3 was skipped | Added that each half-search is 3 steps deep, so about 10^3 states each |
| 48 | Constraint satisfaction, last paragraph | "SAT solver" used with no definition (Chapter 54 defines it later) | Gloss: short for satisfiability, with what the program does |
| 48 | NP-completeness paragraph | "P versus NP": neither letter explained | Gloss explaining P and NP in plain words |
| 48 | Planning with actions | STRIPS not expanded | Added "the Stanford Research Institute Problem Solver" |
| 48 | Classical planners in practice | NASA is used in four chapters, has no definition, and this is its first use | Definition callout: NASA (National Aeronautics and Space Administration) |
| 48 | MCTS, UCB formula | ln given with no pointer to where it was taught or how to compute it | Added "(Chapter 6; the ln key on a calculator)" |
| 48 | CICERO section | CICERO is used in three chapters and is not in the glossary | Definition callout: CICERO |
| 48 | Elo formula | Negative and fractional powers of 10 (10^−0.5) cannot be done by hand | Showed 10^−1 = 0.1 (Chapter 2) and gave the spreadsheet formula |
| 48 | Watch out after Figure 48.10 | "In-distribution" undefined | Glossed in the sentence |
| 48 | Shapley value paragraph | SHAP not expanded | Added "SHapley Additive exPlanations, Chapter 10" |
| 48 | RL applications, fusion | EPFL unexplained. "Tokamak" and "plasma" are never defined before Chapter 52 | Glossed EPFL. Added a definition callout for Tokamak that includes plasma |
| 48 | Planning today, AlphaProof | "Lean proof checker" unexplained | Pointer to the proof assistant definition in Chapter 21, with a plain gloss |
| 48 | Exercise 3 (spreadsheet) | "Put α = 0.5 in B1" invites typing text. The formulas lack "=", the $ signs are unexplained, and there is no instruction for copying down | Labels and numbers in separate cells, formulas written with "=", $ explained, how to copy rows 8 to 36 |
| 48 | Exercise 6, step 3 | The hand check of 1.81 used 0.9^5 with no explanation of why five discounts | Explained the five ordinary steps and the discounted treasure step, and that 0.9^5 ≈ 0.59 |
| 48 | Exercise 8, step 1 | Broken: a six-sided die cannot pick squares 7 or 9, which are among the empty squares | After X's move only two squares remain, so O's reply is now a coin flip and X takes the last square |
| 48 | Exercise 10 | "Set `epsilon = 0`" invites adding a new line, which the existing `alpha, gamma, epsilon = ...` line silently overwrites. The step-reward and treasure edits did not say where to edit | Named the exact line and number to change in each step. Gave an example of a moved treasure (checked by running it) |
| 49 | Proprioception definition | "Encoders in each joint" undefined | Glossed |
| 49 | Coordinate frames | "0.4 m × 0.017": where 0.017 comes from is never said | Added that a one-degree tilt shifts a point about 0.017 m per meter of distance |
| 49 | Configuration space | 100^7 = 10^14 is unexplained | Added "100 multiplied by itself 7 times, once per joint" |
| 49 | Dynamics paragraph | "Torques" undefined | Glossed as twisting forces |
| 49 | Learning to walk, worked example | ETH Zurich unexplained | Glossed. NVIDIA is defined in Chapter 3, so it only gets a descriptor |
| 49 | Frontier box, whole-body control | "Figure says its Helix 02 ... Figure 03's work at BMW": a company called Figure, in a chapter full of numbered figures, never introduced; BMW not glossed | Named Figure AI as a US humanoid start-up and BMW as the German carmaker |
| 49 | Robot data gap | RT-1 and RT-2: RT never expanded | Added "RT stands for Robotics Transformer" |
| 49 | Teleoperation | ALOHA not expanded; VR used later without its abbreviation being introduced | Expanded ALOHA and added "(VR)" at first use |
| 49 | Human video | Physical Intelligence, central to the chapter, is never introduced | Glossed as a San Francisco start-up building general robot models |
| 49 | Fleet learning | "A VLA" is quoted one section before VLA is defined | Added a forward gloss |
| 49 | Fast and slow thinker | "ER" in Gemini Robotics-ER not expanded | Added "ER stands for embodied reasoning" |
| 49 | Lineage bullets | GR00T and Ai2 unexplained. UC is used in five chapters with no definition | Glossed GR00T and Ai2. Definition callout: UC (University of California) |
| 49 | World models | "720p" unexplained (Chapter 45 explained only 1080p) | Glossed as 1,280 × 720 pixels |
| 49 | Table 49.3 | CES is used in seven chapters with no definition. "EV plant" not glossed | Definition callout: CES. Glossed EV |
| 49 | Figure 02 worked example | The 4.33 in 11 × 4.33 × 40 is unexplained | Added "(52 weeks ÷ 12 months)" |
| 49 | Safety standards | ISO/TS: TS not expanded | Glossed as technical specification |
| 49 | What to watch next | DARPA is used in five chapters with no definition. "The DARPA challenges" are not told until Chapter 50 | Short gloss plus a definition callout: DARPA (Defense Advanced Research Projects Agency) |
| 49 | Exercise 4 (spreadsheet) | Cell layout unclear. `=A2^B1` "adjusting the references" fails when copied. The retry formula and the break-even target were not reachable | Exact cells, `=$A2^B$1` with $ explained, the full retry formula, and `=0.9^(1/50)` for the exact break-even |
| 49 | Exercise 7 | "SEC filing" undefined in this chapter | Glossed, with a pointer to the SEC definition in Chapter 43 |
| 49 | Exercise 8 | No formula linking price, years, hours, speed and interventions; no intervention values to try | Gave the three formulas (from the factory worked example) and values to try |
| 49 | Going deeper | "CS 285" unexplained | Glossed as a course number |
| 50 | Worked example, fatal mistakes | Plainly wrong: "goes thousands of lifetimes between fatal crashes". 5,700 years of driving is dozens of lifetimes | Now "thousands of years, many dozens of lifetimes" |
| 50 | Watch out, "94 percent" | NHTSA used about 500 lines before its definition | Glossed with a forward pointer |
| 50 | Table 50.1 | FSD and GM appear before either is introduced | Expanded both in the cell |
| 50 | Stopping distance | "7 meters per second squared" is an unexplained unit | Glossed as losing 7 m/s of speed every second |
| 50 | Rule of three | RAND Corporation unexplained | Glossed |
| 50 | Exercise 3 | "Unprotected left turn" is a US driving term the reader may not know | Glossed |
| 50 | Exercise 4 (spreadsheet) | No cell layout. "speed²" typed literally would fail. Step 6 does not say which reaction time the truck uses | Cells, `=A2*0.447`, `=B2^2/(2*7)`, and a 0.3-second driverless truck (answer falls between 70 and 80 mph) |
| 50 | Exercise 8 | Cost per ride, profit and break-even were asked for with no formulas; remote-assistance hours missing | Gave the formulas, using 16 operating hours a day from the chapter's worked example |
| 50 | Areas of opportunity | "GIS specialists" undefined | Glossed |
| 51 | NDCG worked example | log2 used with no pointer | Added "the base-2 logarithm of Chapter 6" and what it asks |
| 51 | Compulsive use | SAFE for Kids Act not expanded | Expanded |
| 51 | CPM definition | Why "M" means thousand | Added "M is the Roman numeral for a thousand" |
| 51 | Ads inside chatbots | Stripe unexplained | Glossed as an online-payments company |
| 51 | Exercise 4, step 6 | "Compute ... the four updated numbers using the rule in the chapter" gave no cells or formulas, the hardest step in the exercise | Exact cells and all six formulas (checked: reproduces 0.69 and 1.59) |
| 51 | Exercise 7, step 5 | "Rebuild the formulas" for a six-page web gave no guidance | Gave the new starting value, the jump term and the D, E and F formulas (checked: D ≈ 0.07) |
| 51 | Going deeper | IEEE and RecSys unexplained | Glossed both |

Fixes per chapter (55 in total):

- **Chapter 48 (17 fixes):** 10 undefined terms, including 4 new definition callouts (SRI, NASA, CICERO, Tokamak); 3 beginner jumps; 4 exercise fixes, one of them a broken exercise.
- **Chapter 49 (21 fixes):** 16 undefined terms, including 3 new callouts (UC, CES, DARPA); 3 beginner jumps; 2 exercise fixes.
- **Chapter 50 (9 fixes):** 5 undefined terms; 1 beginner jump; 2 exercise fixes; 1 plain error.
- **Chapter 51 (8 fixes):** 5 undefined terms; 1 beginner jump; 2 exercise fixes.

Every new definition was added to its chapter's Key terms list.

## Acronym list: how each entry was handled

- **Chapter 48.**
  - NASA, SRI and CICERO got callouts here.
  - IBM: I added a callout and then removed it, because another agent had meanwhile added "IBM (International Business Machines)" to Chapter 8, which comes earlier.
  - Glossed in the sentence: NP, SHAP, STRIPS and EPFL.
  - Already explained in the text: PEAS (spelled out at first use), OG (described as "the reigning world champion team") and EVE (described as a persistent shared world).
- **Chapter 49.**
  - UC, CES and DARPA got callouts here.
  - Already defined in earlier chapters, so these got a gloss or a pointer instead of a duplicate callout: NVIDIA (Chapter 3 and others) and SEC (Chapter 43).
  - Glossed: CS, ER, RT, BMW, ETH, GR00T, ALOHA, EV, VR and TS.
  - Already glossed in the text: NEO (1X's home robot), GXO ("logistics firm GXO") and MEM ("a memory system called MEM").
- **Chapter 50.** DARPA is now defined in Chapter 49 and is glossed again in Chapter 50's history section. FSD and GM are glossed in Table 50.1, and GIS in Areas of opportunity. NTSB is already spelled out at its first use in the body.
- **Chapter 51.** SAFE and IEEE are glossed.

## Noticed but not changed

- **Duplicate organization definitions across chapters.** Other agents running the same pass are adding the same callouts in parallel. NVIDIA is now defined in eight chapters and NASA in both 48 and 52. Whoever builds the glossary should check that the build merges these sensibly.
- **"At the frontier" boxes in Chapter 49.** They still name things the reader cannot place: Helix 02, Sharpa, Jetson Thor and "Gemini 4 Argon". They are optional asides, so they were left alone. The 2026 facts in them were not changed.
- **Figure 49.5.** The diagram says "diffusion or flow head" but never says what a model "head" is. The following text explains the action expert, so the gap is small.
- **Table 48.9 ordering.** The table uses "tokamak" about ten lines before the new Tokamak definition, which is attached to the prose paragraph that discusses it.
- **No sourced 2025–2026 figures were altered.** These include Waymo's ride and mile counts, the humanoid shipment estimates and Tesla's FSD mileage.

## Verdicts

**Chapter 48.** The ramp works, but this is the longest chapter in the set: about 17,000 words and 121 definitions.
- It climbs in clean steps:
  - a single decision (the umbrella);
  - search, from blind search to A*;
  - local search, constraint satisfaction and planning;
  - games, through minimax by hand, chance nodes and MCTS;
  - reinforcement learning, from a corridor Q-table to policy gradients;
  - the game milestones and game theory.
- Every number I recomputed is right: the A* scores, all three minimax branches, the dice values, UCB, the Q-table through episode 7, the Elo figures, the Shapley split and the Colab value of 1.81.
- The core vocabulary is defined thoroughly. The gaps were organization and acronym names (SRI, NASA, CICERO, STRIPS, SHAP, EPFL) and a few forward borrowings from later chapters (SAT solver, tokamak, Lean). All are now defined or glossed.
- The exercises were the weak point. One was impossible as written: a six-sided die cannot pick squares 7 or 9. Another had a code-editing trap that would silently do nothing. Both are fixed.

**Chapter 49.** The ramp works.
- It moves from Moravec's paradox and the sense–plan–act loop through the classic toolkit to simulation, then the reliability arithmetic, the data problem, VLAs, world models and the industry.
- The classic-toolkit section is the steepest climb, with coordinate frames, configuration space, RRT, PID and MPC in quick succession. It is carried by worked numbers, and the two silent steps in it (the 0.017 tilt factor and 100^7) are now explained.
- Nearly every gap was a company, product or acronym name in the industry and lineage sections. The most confusing was "Figure", a company name in a chapter full of numbered figures.
- All arithmetic checks out. With the glosses and the three new callouts, every term is now defined or glossed.

**Chapter 50.** This is the gentlest chapter of the four for this reader, and the ramp works well.
- It starts from responsibility rather than technology. It walks one scene through the driving stack, then builds to a careful eight-step method for reading safety statistics. The Poisson range, the rule of three and the RoboCab numbers are all correct.
- It had the only plainly wrong statement I found: "thousands of lifetimes" between fatal crashes, where the chapter's own numbers give dozens of lifetimes. It also had a forward use of NHTSA long before its definition.
- The two spreadsheet exercises now give a beginner everything needed to finish them.
- With these fixes, every term is defined.

**Chapter 51.** The ramp works and the chapter needed the fewest fixes.
- Each idea is shown with small numbers the reader can check:
  - cosine similarity on a purchase table;
  - a fully worked matrix factorization, including one gradient step;
  - the two-tower dot products;
  - the ranking-weight example;
  - NDCG, the ad auction and PageRank.
- All of these verify, and the Colab code produces exactly the output the exercise promises.
- The remaining gaps were a few names (SAFE for Kids Act, Stripe, IEEE, RecSys) and two exercise steps that asked for spreadsheet work without giving cells or formulas. Both are now fixed.
- Every term is defined.
