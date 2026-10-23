# Reader test: chapters 62 to 66

I read chapters 62, 63, 64, 65 and 66 in order, in full, as the intended reader would: almost no computer-science background, a daily chatbot user for a year, and someone who has read chapters 1 to 61. Before treating a term as undefined, I checked the glossary and the earlier chapters. I also worked through every entry for these chapters in `acronyms-by-chapter.json`. Every edit was small and surgical: a definition callout (added to the chapter's Key terms list), a short gloss, a bridging sentence, or a clearer exercise step. Nothing was restyled, restructured or cut.

After editing, `validate.py` passed on all five files: 5/5, 6/6, 7/7, 11/11 and 8/8 diagrams valid. `check.py` reported `[OK]` for chapters 62 to 66. In every chapter, each definition label appears in the Key terms list.

## Findings and fixes

| Chapter | Where | Problem a beginner would hit | Fix applied |
|---|---|---|---|
| 62 | Verification, worked example | 0.95^10 was given with no reason for multiplying and no way to work it out | Added that all ten claims must be right, and that 0.95^10 means 0.95 multiplied by itself ten times |
| 62 | Level 3, Python basics | "CS50P" was unexplained (it is used in 3 chapters) | New definition callout: CS50P |
| 62 | Level 5, data engineering | "AWS" was never expanded (22 chapters) | New definition callout: AWS (Amazon Web Services) |
| 62 | Level 5, kernels | "NVIDIA" first appears inside the CUDA definition with no introduction (43 chapters) | New definition callout: NVIDIA |
| 62 | Level 5, kernels | "Stanford CS336" was used before the chapter said what it is (4 chapters) | New definition callout: CS336 |
| 62 | Level 6, interpretability and alignment | ARENA and MATS were named as on-ramps but never explained (10 and 11 chapters) | New definition callouts: ARENA (Alignment Research Engineer Accelerator) and MATS |
| 62 | Level 6, evaluation research | "Inspect framework" was unexplained | Glossed as free software for building and running evals |
| 62 | Level 6, alignment | "80,000 Hours" was cited with no explanation | Glossed as a career-advice nonprofit |
| 62 | Cross-cutting, policy | IAPP was only half-glossed, and CSET was not explained at all | New definition callouts: IAPP and CSET |
| 62 | Cross-cutting, data-center trades | HVAC, IBEW and NECA were undefined everywhere in the book | New definition callouts: HVAC, IBEW and NECA |
| 62 | Table 62.2 and the certifications paragraph | "CV" and "HR" were unexplained | Glossed as résumé and human resources |
| 62 | Verification definition | The label "Verification" shares a glossary key with Chapter 59's treaty-verification definition, so the glossary would show the wrong meaning | Renamed the label "Verification of AI output" (Key terms updated) |
| 63 | Figure 63.2 | "TC" appears in the figure about 30 lines before it is defined | The caption now says that TC means total compensation, defined below |
| 63 | Research engineer definition and Table 63.3 | "RE/RS" and "MS" were unexplained | Glossed |
| 63 | Table 63.4 | "HPC" was used 15 lines before the SRE definition expands it | Glossed at first use |
| 63 | Tables 63.6, 63.7 and 63.8 | "UX", "Spark" and "Full-stack" were unexplained. Spark is also a different product from the Spark in earlier chapters | Glossed each one (Spark as Apache Spark) |
| 63 | Sales pay, worked example | "Quota" was undefined. "Accelerators above quota" reuses a word the reader has learned as "AI chip" | Glossed quota, and explained the sales meaning of "accelerators" |
| 63 | Who works on AI safety | MIRI, FAR.AI and IAPS were named with no explanation (3 or more chapters each) | New definition callouts: MIRI, FAR.AI and IAPS |
| 63 | Same list | NYU, and "DAIR" (Gebru's institute, which is a different organization from Chapter 25's DAIR.AI) | Glossed each one |
| 63 | Jagged frontier and the evidence list | Stanford HAI and MIT NANDA were unexplained (6 and 5 chapters) | New definition callouts: HAI and NANDA, with "Stanford HAI's" added before the AI Index mention |
| 63 | Credentials, and finding openings | "HR" and "Ask HN" were unexplained | Glossed |
| 63 | Exercise 2 | The formula `=B2/B$6` came with no layout, and the $ was unexplained | Gave the cell layout and explained the $ |
| 63 | Exercise 3 | `=grant/years`, `=base+bonus+equity_per_year` and `=ownership*exit_price` are placeholders a beginner would type literally | Rewrote the steps with exact cells and formulas (checked: Offer C's $100M exit gives $128,000, matching the text) |
| 63 | Exercise 7 | "Midpoint" of a pay range was not explained | Added (bottom + top) ÷ 2 |
| 64 | Figure 64.3 | "FinOps" is in the diagram and nowhere else | Explained in the caption |
| 64 | Table 64.1 | "SEC filing" (7 chapters) and "guided to" were unexplained | New definition callout: SEC (which also explains S-1). Glossed "guided to" |
| 64 | Voice-receptionist example | "Contribution" was used as a term with no explanation | Glossed |
| 64 | Lessons from the winners | "Take rate" was undefined | Glossed |
| 64 | Table 64.7 | IEA (5 chapters) was only expanded inline | New definition callout: IEA |
| 64 | Definitions "Accelerator" and "CAC" | The glossary builder keys terms without their parentheses. "Accelerator" (a startup program) would merge into the AI-chip definition, and "CAC" (customer acquisition cost) into Chapter 59's Cyberspace Administration of China | Renamed the labels "Startup accelerator" and "Customer acquisition cost (CAC)" (Key terms updated) |
| 64 | Exercise 3 | Said "in row 12" for both the total and the percentage, and SUMPRODUCT was unexplained | Put the total in C12 and the percentage in C13, and explained SUMPRODUCT and the $ signs |
| 64 | Exercise 5 | Formulas used placeholders (`calls`, `cost_per_min`, `CAC`) | Gave cells B1 to B12 with exact formulas, and said how to find the break-even volume |
| 65 | Worked time budget | The Machine Learning Specialization example silently switched from 5 to 8 hours a week | Said who studies 8 hours a week, and added the 5-hour result (38 weeks) |
| 65 | A week in Stage 1 | "Only three hours" was actually 195 minutes | Now says "about three hours" and shows the sum |
| 65 | MCP definition, CS50P row, Missing Semester row | "USB-C", "CS50" and "CS" were unexplained | Glossed |
| 65 | nanochat row | "Full-stack harness" was jargon | Glossed |
| 65 | Checklist, point 1 | "FT" (3 chapters) was used as an abbreviation | New definition callout: FT (Financial Times) |
| 65 | Answer 5 | "HR" was unexplained | Glossed |
| 65 | Exercise 6 | The Brier score had no cell layout and no spreadsheet formula for squaring or averaging | Added columns A to D, `=(B2-C2)^2` and `=AVERAGE(D2:D11)` |
| 66 | One-month horizon, step 2 | "2^3.26" is a fractional power the reader cannot compute | Showed that the answer lies between 2^3 and 2^4, and gave `=LOG(9.6,2)` |
| 66 | Robotics, power, chips and money sections | Omdia, JLL, NRC, TSMC, AMD's MI500, FactSet and GB200 were named with no reminder of what they are | Glossed each in place, with chapter pointers (see notes below) |
| 66 | Misuse, rights and wellbeing | "SB" (13 chapters) and "RAISE Act" were unexplained at first use in the chapter | Glossed (Senate Bill 53; a similar state law for frontier developers) |
| 66 | Tables 66.4 to 66.6 | EMA was unexplained. EIA is easily confused with IEA in the same cell. "10-Q" was unexplained | Glossed all three |
| 66 | Bust and backlash | "Down-round" was undefined | Glossed |
| 66 | Areas of opportunity | "HR" was unexplained | Glossed |
| 66 | Worked example 3 | "Off by roughly a thousandfold": 500 mL ÷ 0.26 mL is about 1,900 | Changed to "more than a thousandfold (500 ÷ 0.26 ≈ 1,900)" |
| 66 | Exercise 4 | No cell layout, and `=1044*2^(months/4.2)` uses a placeholder | Gave columns and exact formulas (checked: the thresholds come out near month 14 and month 23, as in the text) |

Fixes per chapter: 62: 17, 63: 20, 64: 10, 65: 9, 66: 16 (72 in total). By type:

- **Undefined terms:** 19 new definition callouts (11 in Chapter 62, 5 in 63, 2 in 64 and 1 in 65) and 37 glosses.
- **Beginner jumps:** 5 bridging fixes.
- **Exercises:** 7 exercise fixes.
- **Plainly wrong:** 4 corrections (3 glossary label collisions and 1 arithmetic statement).

## Notes, and things not changed

- **Parallel edits.** While this pass was running, other agents added definition callouts for many names in my acronym lists in earlier chapters: NVIDIA, AWS, MATS, ARENA, IAPP, CSET, MIRI, FAR.AI, SEC, IEA, AMD, TSMC, GB200, JLL, BWRX-300, LBNL, EIA, NRC, MI500, the RAISE Act and SB 53. My callouts in Chapters 62 to 65 were added when none existed yet. They are consistent with the later ones, and the glossary merges them. By the time I reached Chapter 66, each of its organizations already had a callout in two to seven earlier chapters. So in Chapter 66 I glossed them in place with chapter pointers, following the style guide's rule for terms defined earlier, instead of adding yet another callout.
- **Glossary collision outside my chapters.** Chapter 14's "Alignment" (which input words a translation model attends to) shares a glossary key with the safety meaning used in Chapters 20, 55, 62 and 65. Because Chapter 14 is processed first, the generated glossary would show the translation meaning for all of them. The builder strips parentheses when it keys terms, so the fix is for Chapter 14 to relabel its definition (for example "Word alignment"). I did not change it.
- **Remaining small names.** Chapter 66 still names GR00T and π0 only inside a list of robot foundation models, and Chapter 63 lists several nonprofits by name (Apollo Research, Redwood Research and others) under a heading that describes them. Both are glossed by their context, so I left them.
- **Sourced facts.** No sourced 2025 to 2026 facts were changed.

## Verdict per chapter

**Chapter 62 (The Complete AI Skills Map).** The ramp works. Each level repeats the same four questions (what, why, learn, prove), which gives a beginner a steady rhythm. The self-assessment and the worked example of Maria make the abstract tree personal. The main friction was a run of program and organization names in Levels 5 and 6 and in the cross-cutting branches: CS336, ARENA, MATS, IAPP, CSET, IBEW and NECA, with HVAC undefined anywhere in the book. Each now has a callout. Every term the reader needs is now defined here or in an earlier chapter.

**Chapter 63 (Careers in AI).** This is the densest chapter of the five for jargon, because the job-board tables are written in the industry's own shorthand: TC, RE/RS, HPC, UX, Spark, full-stack, quota and OTE. The pay tutorial (base, bonus, RSU, cliff, dilution) is excellent, and its arithmetic checks out, as does the arithmetic of the task audit. The fixes mostly glossed table shorthand and the names in the safety-ecosystem list. The offer-modeling spreadsheet exercise was the one real barrier, and it is now doable. Every term is now defined or glossed.

**Chapter 64 (Opportunities).** The ramp works well. The three-ingredient definition, the stack map and the worked unit economics (all checked: $6,000 of value, $280 to serve, 2.7-month payback, LTV of about $7,300, a break-even near 1,333 calls) carry a non-business reader through. Business jargon was the gap: FinOps, "guided to", contribution and take rate. Two definition labels would also have produced wrong glossary entries. Both spreadsheet exercises used placeholders and now give exact cells. Every term is now defined.

**Chapter 65 (Your Learning Roadmap).** This is the gentlest chapter of the five. Its time budgets and worked examples are clear and correct (65 hours; 22-week payback; 1.7 cents per question; 183 minutes a week). The only reasoning gap was an unannounced switch from 5 to 8 study hours a week, which matters because a reader is planning real time from it. A handful of abbreviations (USB-C, CS50, CS, FT, HR) were glossed, and the Brier-score exercise now has formulas. Every term is defined, often twice, which suits a chapter the reader may open first.

**Chapter 66 (The Road Ahead).** The synthesis works. Each open problem is recapped in a line with a pointer back. The worked examples (error compounding, the one-month horizon, the 1 GW campus, the 2030 compute trend, the Brier and Bayes examples) all check out numerically, apart from the "thousandfold" water ratio, now corrected. The steepest step was the fractional doubling count (2^3.26), now bridged. Infrastructure names from Parts VI and VII reappear in quick succession, so each now carries a short reminder and a chapter pointer. The letter and the ten ideas close the book well for this reader. With the glosses, every term is defined here or earlier.
