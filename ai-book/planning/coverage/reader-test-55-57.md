# Reader test: chapters 55 to 57

I read chapters 55, 56 and 57 in order, in full, as the intended reader. That reader is smart, has used chatbots daily for a year, has read chapters 1 to 54, and has no computer-science background. Before treating a term as undefined, I checked GLOSSARY.md and the earlier chapters. I worked through every entry for these chapters in `acronyms-by-chapter.json`. Every fix is a small, surgical edit. Nothing was rewritten for style and no content was cut.

After editing, `validate.py` passes on all three files (26/26 diagrams valid). `check.py` reports `[OK]` for chapters 55, 56 and 57. A script check confirmed that every definition callout in each chapter appears in that chapter's Key terms list, and that every Key terms entry has a definition.

## Findings and fixes

| Chapter | Where | Problem a beginner would hit | Fix applied |
|---|---|---|---|
| 55 | Sleeper agents, data poisoning paragraph | "Alan Turing Institute" named with no explanation | Glossed as the UK's national institute for data science and AI |
| 55 | Alignment faking (December 2024) | "Redwood Research" named with no explanation (first use in the book) | Glossed as a nonprofit AI safety research lab |
| 55 | In-context scheming | "Apollo Research" named with no explanation | Glossed as a London organization that tests AI models for deception |
| 55 | Power-seeking, the evidence so far | "Palisade Research" named with no explanation | Glossed as a nonprofit that studies dangerous AI behaviors |
| 55 | Figure 55.6 (quadrant chart) | The chart plots "Shutdown script edits" and "Emergent misalignment" before the text has explained either | Added a sentence before the chart saying both are described later in the chapter |
| 55 | Areas of opportunity, technical alignment research | MATS, ARENA and FAR.AI are each used in 3 or more chapters, never defined, and first appear here | New definition callouts for MATS, ARENA and FAR.AI, added to Key terms |
| 55 | Exercise 4, step 2 | `=$A2^B$1` and "fill it across and down" assume the reader knows spreadsheets: what ^ and $ do, and how to fill | Explained ^ and $, and how to drag-fill to G2 and down to row 5 |
| 55 | Exercise 4, steps 3 and 4 | The table's columns (5, 10, 20, 50 steps and so on) cannot answer "how many steps can a 98% agent manage". The answer lies between 20 and 50, and no method was given | Step 3 now says "in your table". Step 4 now says where to type the 0.98 row and how to pin down the answer with trial formulas, and gives the answer (34 steps, with 0.98^34 ≈ 50.3% and 0.98^35 ≈ 49.3%) |
| 55 | Check your understanding, Q5 | "Hint: 0.98^30" gives no way to compute a power | Added the spreadsheet formula `=0.98^30` |
| 56 | Worked example: how layers multiply | The factors 0.10 × 0.20 × 0.25 × 0.5 appear with no link to the catch rates just listed (90%, 80%, 75%, half) | Added: each layer lets through 1 minus its catch rate (catching 80% lets 0.20 through), and the shares multiply |
| 56 | Normal accidents, Flash Crash | "Dow Jones index" assumed | Glossed as a leading measure of US stock prices |
| 56 | Anthropic's constitution bullet | "CC0 public-domain license" leaves the reader to guess what that allows (acronym list) | Glossed: anyone may copy, change and reuse it without asking permission |
| 56 | Adding up across people, prioritarian rule | Square roots appear with no reminder of what they are, and no reason why adding square roots favors the worse-off | Added that the square root of 9 is 3 (3 × 3 = 9) and of 5 is about 2.24, plus a sentence on why square roots weight gains to the worse-off more |
| 56 | Filtering the training data | "A third of its above-chance knowledge" skips the arithmetic from 33.7%, 30.8% and 25% | Showed it: above chance, the score fell from 8.7 to 5.8 points, and the 2.9-point drop is a third of 8.7 |
| 56 | Same paragraph | "EleutherAI" named with no explanation (also unglossed in Chapter 11) | Glossed as a nonprofit research group that builds open AI models and datasets |
| 56 | Agent foundations | MIRI is used in 3 or more chapters, never defined, and first appears here | New definition callout for MIRI (Machine Intelligence Research Institute), added to Key terms |
| 56 | OpenAI Preparedness Framework | First use of "SB 53" (acronym list) and "the EU code of practice", about 190 lines before Table 56.3 explains SB 53 | Glossed both at first use, with a pointer to the table |
| 56 | After Table 56.3 | SB 53 (13 chapters) and the RAISE Act (6 chapters, first used here) have no definition anywhere, though this chapter's table and Exercise 10 depend on them | New definition callouts for SB 53 and the RAISE Act (including "SB stands for Senate Bill"), added to Key terms |
| 56 | Securing the weights | "RAND Corporation" named with no explanation | Glossed as a US nonprofit that researches policy and national security |
| 56 | Worked example: why bandwidth is a defense | The bytes-to-bits step, why gigabits mean dividing by 10^9, and the conversion of seconds to hours and days were all silent | Added "(8 bits per byte)", that network speeds are quoted in bits per second (a gigabit is 10^9, a megabit 10^6), and divide by 3,600 or 86,400 |
| 56 | Monitoring and enforcement | "Claude Code" used with no gloss | Glossed as Anthropic's coding agent |
| 56 | Exercise 4, step 4 | "Making each layer stronger" gave no numbers, so a beginner could not compute it. As written, any reasonable reading also fails to show the stated lesson (diverse layers beat stronger copies) | Rewritten as two concrete upgrades: A halves the pass-through of layers 2 and 3, B adds a fifth 0.5 layer. Both are computed in each scenario, and expected results are given (A wins when independent, 0.6 vs 1.25 per 1,000; only B helps when correlated, 15 vs 30 per 1,000) |
| 56 | Areas of opportunity, governance | "Big Four firms" assumed | Changed to "the Big Four accounting and consulting firms" |
| 57 | Interpretability frontier box | "MRI for AI" (acronym list) | Glossed MRI as the hospital scanner that shows the inside of the body |
| 57 | Table 57.3, cyber row | "Capture-the-flag challenges" appears about 150 lines before the text explains it | Added "(hacking contests, explained later in this chapter)" |
| 57 | Uplift study | The formula √(20²/20 + 20²/20) appears unexplained. Chapter 9 only covers margins of error for a single percentage. "Four times as many participants to halve the range" was unexplained | Walked through the formula piece by piece and the "± 2 ×" step. Added that the group size sits under a square root and √4 = 2 |
| 57 | Outside testing has real limits | SB 53 and RAISE Act unglossed (acronym list). The sentence also said both laws require publication "as of October 2026", which contradicts Chapter 56: the RAISE Act takes effect January 1, 2027 | Glossed as two US state laws with their dates from Chapter 56 (in force since January 2026; from January 2027), and pointed to Chapter 56 |
| 57 | Time horizons, doubling check | "2 to the power 7.5 is about 181" is a fractional power a beginner cannot check | Added that seven doublings give 128 and eight give 256, so 180 lies between them |
| 57 | Exercise 5, step 5 | No cells given for the penalty and total loss, and no expected value to check against | Gave H13 and H14 with formulas, and the expected 0.06 + 0.04 = 0.10 (checked) |
| 57 | Exercise 9, step 5 | "Predict pass@3 from your first pass@1" is ambiguous: the measured pass@3 builds on step 3, not step 2. No worked use of the formula | Set k = 3 and p = the step 3 pass@1, and added a worked example (p = 0.4 gives ≈ 0.78) |
| 57 | Check your understanding, Q3 answer | Arithmetic error: the answer said both totals are 0.08 and tie, but 0.01 + 0.09 = 0.10. The question asks which is lower | Corrected: the first code wins, 0.08 against 0.10, with the reason |
| 57 | Areas of opportunity, interpretability researcher | "Linear algebra" assumed | Glossed as the math of vectors and matrices (Chapter 5) |

**Fixes by type and chapter (32 in total):**

- Chapter 55 (9): 5 undefined-term fixes (4 glosses, plus one row adding 3 new definition callouts), 1 beginner jump, 3 exercise fixes.
- Chapter 56 (14): 9 undefined-term fixes (6 glosses; a first-use gloss for SB 53 and the EU code of practice; a new MIRI definition; new SB 53 and RAISE Act definitions), 4 beginner jumps, 1 exercise fix.
- Chapter 57 (9): 4 undefined terms (one of them also fixes a date contradiction with Chapter 56), 2 beginner jumps, 2 exercise fixes, 1 wrong answer.

Seven new definition callouts in all: MATS, ARENA and FAR.AI in Chapter 55, and MIRI, SB 53 and the RAISE Act in Chapter 56. All are in their chapter's Key terms list.

## Acronym-list entries resolved without a new callout

- **NVIDIA and AWS** (Chapter 56): both are now defined in earlier chapters, such as Chapters 19, 38 and 43. Another definition in Chapter 56 would add nothing, so none was added.
- **SL2, SL3 and SL4** (Chapter 56): already covered by the "RAND security levels (SL1–SL5)" definition and Table 56.2. The acronym tool only recognizes SL1 and SL5 from that label.
- **BSL and WMDP** (Chapter 56) and **CAISSI** (Chapter 57): already spelled out and explained inline at first use.
- **SWE** (Chapter 57): the "SWE" of SWE-bench, which is defined in Chapter 24.
- **FAR** (Chapter 55): FAR.AI, now defined. The tool still lists it because it splits "FAR.AI" at the dot.

## Noticed but not changed

- These chapters contain many sourced 2026 facts that I did not verify: Claude Mythos Preview and Project Glasswing, Fable 5 and Mythos 5, Opus 4.8 and 5.5, GPT-6 Astra, Sol and Luna, Gemini 4 Argon and Fairwind, RSP v3.4, the CAISSI rename, and METR's Opus 5.5 assessment. Whoever owns freshness for Part IX should check them.
- Chapter 57, SAE loss example: "Suppose a second candidate code gives the rebuild [2.4, 1.0, 0.1, 1.5] ... (here 2 + 1 + 1 = 4)". Strengths of 2, 1 and 1 on the original features would rebuild the activation exactly, so the example is slightly inconsistent. It is illustrative and does not block the reader, so I left it.
- Chapter 57, Exercise 7: transcript A blames "the wrong rate" and transcript B "the rounding bug" for what is called the same task. This is harmless to the exercise.
- Style only, left alone: Chapter 55 says the reasoning appeared "in a scratchpad the model could be read through" (awkward). Chapter 57's elicitation "Try it" has two consecutive "This ... is why" sentences.

## Verdicts

**Chapter 55 (What Can Go Wrong).** The difficulty ramp works well. The chapter opens with the three families of harm and two pieces of simple arithmetic: base rates times users, and p^n for agent steps, which reaches 100 steps in a table. It then moves through Goodhart's law, specification gaming and outer and inner alignment to the speculative material (deceptive alignment, scheming, power-seeking). It keeps the reader calibrated with explicit "how contrived was this?" tables and the quadrant chart. All of its 53 original terms were defined. The real gaps were unglossed research-organization names, the quadrant chart's forward references and the spreadsheet mechanics of Exercise 4. All are now fixed, and every term is defined.

**Chapter 56 (How Labs Make AI Safer).** This is the longest of the three (about 15,000 words before the exercises, now 98 definitions). The ramp works, but the front is heavy. "What other safety-critical industries learned" and "Which values?" introduce about 35 defined terms (risk factors, normal accidents, wicked problems, four families of moral theory, social welfare functions) before Layer 1's techniques begin. Each one is defined and has a worked example, so it is dense rather than broken. The arithmetic is light and correct. The friction was compressed steps (catch rates turned into pass-through rates, square roots, bits and bytes), plus laws and organizations named without explanation. The access-tiers section is crowded with 2026 product names but readable. After the fixes, every term is defined, and SB 53 and the RAISE Act now enter the glossary from here.

**Chapter 57 (Interpretability and Evaluations).** This is the steepest of the three. It uses vectors, dot products, ReLU, cosine similarity and square roots in high dimensions, and standard errors. It states its dependence on Chapters 5, 12 and 15 honestly in "Before you start". The pencil examples are the chapter's strength, and all of them check out: superposition with three arrows, the SAE decoder, the probe and the steering addition. The biggest beginner jump was the uplift study's statistics, which Chapter 9 does not cover for a difference between two groups. The only factual slip was a wrong answer in Check your understanding Q3. A date contradiction with Chapter 56 on the RAISE Act was also fixed. With the fixes, the ramp works, and every term is defined.
