# Reader test: chapters 19, 20, 21, 22 and 24

I read chapters 19, 20, 21, 22 and 24 in order, in full, as the intended reader. That reader is smart and curious and has used chatbots daily for a year. They know no programming, no math beyond school arithmetic, and nothing about hardware or the AI industry. They have read chapters 1 to 18. Chapter 23 was tested in the earlier pass.

Before calling a term undefined, I checked the glossary and grepped the earlier chapters. A term that an earlier chapter defines or glosses was not counted as a problem. Every entry for these chapters in `acronyms-by-chapter.json` was handled:

- NVIDIA (43 chapters), GB200 (17) and DALL·E (5) had no definition anywhere in the book, so each got a definition callout in the first of my chapters that uses it.
- Stanford HAI (6 chapters, first used in Chapter 24) also got a definition callout.
- Every other acronym got a gloss at its first use in the chapter.

I re-checked every worked number by hand or with a script. This included:

- the Chinchilla loss table;
- the 16-round RLHF toy table in Chapter 20;
- the majority-vote and GRPO numbers in Chapter 21;
- the image and video token arithmetic in Chapter 22;
- all cost tables in Chapter 24.

All other arithmetic in these chapters is correct. The two rounding slips I found in Chapter 20 are fixed below. The token-calculator code in Exercise 10 of Chapter 22 was run, and its output matches the chapter. New Python code was checked for syntax.

After editing, every edited file passed `validate.py` (36 of 36 mermaid diagrams valid) and `check.py` (all five chapters `[OK]`).

## Findings and fixes

| Chapter | Where | Problem a beginner would hit | Fix applied |
|---|---|---|---|
| 19 | Measuring surprise, perplexity | "e raised to the loss" with no reminder of e and no way to compute e^0.44 | Named Euler's number (Chapter 6) and gave `=EXP(0.44)` |
| 19 | The sources, Common Crawl bullet | "360 TiB" is a unit never defined in the book | New definition callout: TiB (tebibyte), added to Key terms |
| 19 | The sources, licensed data | "News Corp" unexplained | Glossed as the publisher of The Wall Street Journal |
| 19 | Asking permission | "EU AI Act" never introduced before Chapter 59 | Glossed as the European Union's main AI law, with a pointer to Chapter 59 |
| 19 | Choosing the recipe, curriculum | "the Allen Institute's OLMo 2" with no gloss | Glossed the Allen Institute for AI as a nonprofit research lab |
| 19 | The machine (Llama 3, GPT-6 Astra) | NVIDIA (43 chapters) and GB200 (17 chapters) are never defined anywhere | New definition callouts: NVIDIA and GB200, added to Key terms |
| 19 | Fewer bits, more speed | "Hopper chips", "H800" and "quantization-aware training" (defined only in Chapter 23) all unexplained | Glossed each: the H100 generation; an H100 with slower links made for China under US export rules; training while simulating 4-bit rounding |
| 19 | Chinchilla worked example | N^0.34 is a fractional power the reader has never met | Explained it as close to a cube root, with a concrete 1,000-times example |
| 19 | Same | "type 280e9^0.34 into any spreadsheet" has no `=`, so a beginner gets text | Gave the full formula `=406.4/280e9^0.34` and explained 280e9 |
| 19 | Sizing a compute-optimal model | Step from C = 120 × N² to N = √(C ÷ 120) needs algebra the reader has never done | Spelled out: divide by 120, then take the square root, which undoes squaring |
| 19 | Compute trends | "H100-equivalents" has no gloss here (it is defined only in Chapter 34) | Glossed in the sentence |
| 19 | When does the wall bite? | "5^2.9 ≈ 100" appears with no derivation | Showed 5 × 5 = 25 after two years and 125 after three |
| 19 | Exercise 4, step 2 | DeepSeek row had no GPU count, so the days column breaks | Said to keep the step 1 settings and try a round GPU count, because the real count is not public |
| 19 | Exercise 5 | No starting cell; SQRT unexplained; step 4 compares with a 70B row that does not exist | Gave the layout from A2, glossed SQRT, and gave rows 10 and 11 with expected losses (1.949 and 1.937) |
| 19 | Exercise 6 | "List 0.50 to 0.99 in steps of 0.01" with no method | Gave the fill-down formula |
| 19 | Exercise 7 | Layout of years and compute unclear; over-training formula only half given | Gave cell layout and the full `=200*SQRT(A2/1200)` with its derivation |
| 19 | Exercise 9, step 3 | Parameter-count code not runnable as written (no print), and no expected values | Gave the print line and the expected values: about 818,000 parameters, 6.1 million tokens and 3 × 10^13 FLOPs |
| 19 | Areas of opportunity | "Petabyte scale" | Glossed as 1,000 terabytes |
| 20 | Reward model worked example | −ln(0.18) is 1.71, not 1.70 | Corrected to ≈ 1.71 |
| 20 | KL leash, round 1 | ln(0.53 ÷ 0.50) is 0.06, but the text showed 0.05 | Corrected to 0.06 (result unchanged) |
| 20 | DPO, the shortcut | "Turn the equation around" hides a log step the reader has never done | Added the steps: divide, take the natural log (which undoes e^), multiply by β; the rescaling becomes the constant |
| 20 | KTO definition | "Kahneman–Tversky" names unexplained | Named the two psychologists behind prospect theory |
| 20 | Anthropic's constitution | "CC0" acronym | Expanded to Creative Commons Zero and explained it as public domain |
| 20 | Deliberative alignment | "Apollo Research" never introduced (Chapter 57 covers it) | Glossed as an independent AI-safety group that tests for deceptive behavior |
| 20 | Safeguards | "Bug bounty" undefined until Chapter 56 | Glossed in the sentence |
| 20 | Illicit distillation | "MiniMax" unexplained | Glossed DeepSeek, Moonshot and MiniMax as three Chinese AI labs |
| 20 | LoRA worked example | "Rank 8" undefined, and no explanation of how two thin matrices make a full update | Explained rank as the thin side, and that the product is a full 4,096 × 4,096 table of changes |
| 20 | Model merging | "TIES-merging" acronym | Expanded: trim, elect sign and merge |
| 20 | Exercise 4 | No label cells, no formula for normalizing, no check value | Gave cell layout, `=D2/SUM($D$2:$D$4)`, a note on $ signs, and the expected 0.53/0.43/0.05 |
| 20 | Exercise 9, step 4 | Reusing Exercise 7's code would fail: the model is on the GPU but the inputs are not, and there is no untrained copy to compare | Added a complete, commented second code block that compares trained and untrained models |
| 21 | Self-consistency worked example | The coefficients 3, 10 and 5 come from nowhere | Explained them as the number of ways to place the wrong attempts |
| 21 | GRPO step 2 | √(mean × (1 − mean)) is given with no link to what a standard deviation is | Gave the general recipe and showed it gives 0.234 for this group |
| 21 | DAPO | "ByteDance Seed" unexplained | Glossed as the AI research team of ByteDance, TikTok's Chinese parent |
| 21 | R1-Zero | "AIME" used with no gloss (Chapter 24 explains it later) | Expanded and glossed: a US high-school contest, 30 problems a year, whole-number answers |
| 21 | Exercise 2, step 3 | No spreadsheet form and no answer to check | Gave the formula and the expected 0.837 |
| 21 | Exercise 10, step 3 | "Adapter-harness" never named in this chapter | Linked it to the "different harness" described in the text |
| 22 | Late fusion, compressing image vectors | "Salesforce's BLIP-2" with neither name explained | Expanded BLIP and glossed Salesforce |
| 22 | Worked example, token cost | "Qwen2-VL" acronym | Glossed VL as vision-language |
| 22 | Neural audio codecs | "24 kHz" and "Kyutai" unexplained | Glossed as 24,000 samples per second, and Kyutai as a nonprofit AI lab in Paris |
| 22 | Figure 22.5 | "ms" appears in the diagram before milliseconds are mentioned | Spelled out "milliseconds" in the diagram note |
| 22 | Models that draw | DALL·E (5 chapters) is never defined anywhere | New definition callout: DALL·E, added to Key terms |
| 22 | Video generation | "Google I/O" unexplained | Glossed as Google's yearly developer conference |
| 22 | Not every chatbot draws | "HTML and SVG": HTML is not defined until Chapter 29, and SVG never is | Glossed both in the sentence |
| 22 | Cost of seeing (computer use) | "Stateless" pointed only to Chapter 25; the sum 1 + 2 + ... + 50 = 1,275 had no explanation | Glossed stateless and pointed to Chapter 18; showed the pairing shortcut 50 × 51 ÷ 2 |
| 22 | World models | "720p", "SIMA" and "Robotics-ER" unexplained | Glossed 720p as 1,280 × 720 pixels, expanded SIMA, and marked ER as embodied reasoning |
| 22 | Areas of opportunity | "QA" acronym | Glossed as quality assurance |
| 22 | Exercise 1 | No formula for cost or photos per dollar; the cap rule did not catch large images under 2,576 px whose estimate exceeds the cap | Gave both formulas with an example; applied the 4,800-token cap to any estimate above it |
| 22 | Exercise 6, step 6 | Scaling a 1–3 minute clip to 10 minutes not explained | Gave the scaling and cost formula |
| 22 | Exercise 7, step 3 | A beginner may paste a web-page link, not an image link | Explained "Copy image address" and keeping the quotation marks |
| 24 | Error bars Try it | SQRT unexplained | Glossed as the spreadsheet's square-root function |
| 24 | Death by saturation | "Center for AI Safety" unexplained | Glossed as a US nonprofit research group (and Scale AI as a data company) |
| 24 | Table 24.1 | Vals Index, DeepSWE, FrontierSWE, Terminal-Bench and GraphWalks (with "256K–1M" and F1) appear before the benchmark zoo explains any of them | Added one bridging note after the table |
| 24 | HLE table | Xiaomi unexplained | Glossed as a Chinese phone and electronics maker |
| 24 | FrontierMath | "Erdős problems" | Glossed as named after Paul Erdős, who left hundreds of open problems |
| 24 | SWE-bench definition | "SWE" (4 chapters) never expanded | Added "SWE stands for software engineering" |
| 24 | GDPval definition | "GDPval-AA" and "AA Intelligence Index" leave AA implicit | Added "AA for Artificial Analysis" |
| 24 | Open-versus-closed debate | "Cursor's Composer 2.5" assumes the reader knows Cursor | Glossed Cursor as a popular AI code editor |
| 24 | How big is the gap? | "Z.ai" unexplained | Glossed as a Chinese lab, formerly Zhipu AI |
| 24 | How labs are organized | "TBD Lab" and "FAIR" unexplained | Glossed TBD ("to be determined") and FAIR (Fundamental AI Research) |
| 24 | Going deeper | Stanford HAI (6 chapters) is never defined anywhere | New definition callout: Stanford HAI, added to Key terms |
| 24 | Exercise 2 | Formula uses row 2, but the Try it used row 1; "write down both intervals" not explained | Said to put headings in row 1, and that an interval is the score minus and plus column C |
| 24 | Exercise 4, step 4 | No formula for cost per conversation | Gave it |
| 24 | Exercise 8, step 2 | No formula for cost per attempt | Gave it, with the Opus 5.5 check value ($0.30) |
| 24 | Exercise 9 | No `5E15` entry form; no ÷ 86,400 or ÷ 3,600 steps; DeepSeek check has no GPU count | Spelled out each, with the 9.7 × 10^24 check value and a placeholder GPU count |

### Fixes by type

| Chapter | Undefined terms | Beginner jumps | Exercises | Plainly wrong | Total |
|---|---|---|---|---|---|
| 19 | 12 (3 new definitions: TiB, NVIDIA, GB200) | 5 | 5 | 0 | 22 |
| 20 | 6 | 2 | 2 | 2 | 12 |
| 21 | 2 | 2 | 2 | 0 | 6 |
| 22 | 12 (1 new definition: DALL·E) | 2 | 4 | 0 | 18 |
| 24 | 12 (1 new definition: Stanford HAI) | 0 | 4 | 0 | 16 |

There are 74 fixes in total. Five new definition callouts were added, and each was added to its chapter's Key terms list.

## Noticed but not changed

- **Chapter 24, SpaceXSI.** "SpaceXSI (formerly xAI)" and its timeline are sourced 2026 facts: acquired February 2, 2026, renamed SpaceXAI in July and SpaceXSI in October. The earlier pass flagged the same name in Chapter 44. Whoever owns these facts should check them.
- **Chapter 22, the Claude image-size limit.** The chapter says current Claude models take images "up to 2,576 pixels on the long side, at most 4,784 tokens". A 2,576 × 2,576 image at 28 × 28 pixels per token would be 8,464 tokens, so the token cap must be a separate limit. This is worth checking against Anthropic's documentation. I only made the exercise apply the cap consistently.
- **Chapter 24, Exercise 10.** The Ollama tag `gemma4:e2b` is unverified.
- **Untested code.** The Colab code in Chapter 19 (Exercises 8 and 9), Chapter 20 (Exercises 7 and 9) and Chapter 21 (Exercise 8) was not run here, because there is no GPU or model download. It was checked for syntax only. The parameter count I added to Chapter 19's Exercise 9 was computed from the code's layer sizes.
- **Unintroduced 2026 names.** As in the earlier pass, the optional "At the frontier" boxes and the 2026 product names (Fable, Mythos, Fairwind, Muse Wonder, GPT-6 Sol and Luna) are used without introduction in Chapters 20 and 21. Chapter 24 introduces them properly, so this is a forward-reference cost, not a gap.
- **Concurrent edits.** Another agent edited Chapters 20 and 24 during this pass. My edits were applied to the current text, and I confirmed afterward that all of them are still present.

## Verdicts

**Chapter 19 (Pretraining).** The ramp works. The chapter starts from "every token is a free quiz" and builds to the training loop, curation, 6ND and dollar costs. Every number is worked, and all of them check out. The steepest steps were the Chinchilla formula, with its fractional exponents, and the square-root inversion for compute-optimal size. Both are now bridged. Undefined chip and company names were the main gaps: NVIDIA, GB200, Hopper, H800 and TiB. With the new callouts and glosses, every term is defined or glossed. The spreadsheet exercises were good in substance but left out cell layouts. They now give exact cells and expected values.

**Chapter 20 (Post-training).** This is the most beginner-friendly of the five chapters. The toy RLHF example (three replies, flawed judge, the KL leash) is fully computed, and I reproduced all 16 rounds exactly. The DPO section's "turn the equation around" was the only real jump, because it assumes the reader can take logs of both sides. It is now spelled out. Two small rounding slips were corrected. Terms are thoroughly defined. The missing pieces were organization and acronym names (CC0, Apollo Research, MiniMax, TIES, bug bounty). Exercise 9's final step was not doable as written, and it now has complete code.

**Chapter 21 (Reasoning models).** The ramp works well: from the bat-and-ball puzzle, to chain of thought, to test-time compute, to GRPO with a worked group of eight, to products. The chapter assumed two pieces of school-plus math, the binomial counts in majority voting and how to compute a standard deviation. Both are now explained in one or two sentences. Definitions are thorough; only AIME and ByteDance were missing. The exercises were already well specified, apart from one missing check value and one undefined term.

**Chapter 22 (Multimodal models).** The ramp works. It goes from pixels to patches to the encoder, the projector and visual tokens, and each token cost is worked by hand from the architecture. The voice section builds the cascade before the omni model, which is the right order. Most problems were unexplained names and abbreviations that a beginner cannot look past: BLIP-2, VL, kHz, Kyutai, SIMA, ER, SVG and DALL·E, which had no definition anywhere in the book. After the fixes, every term is defined or glossed. The exercises are mostly chatbot-based and doable; three needed cost formulas or a clearer instruction.

**Chapter 24 (Model landscape and benchmarks).** The ramp works. Error bars by hand come first, then how benchmarks die, the benchmark zoo, cards, licenses, the who's who, and a cost-per-task method. The main stumble was Table 24.1, which listed five benchmarks the reader had not met yet. A one-sentence bridge now names them before the zoo. The chapter is dense with company and lab names. The well-known ones are introduced in earlier chapters, and the rest are now glossed (Xiaomi, Z.ai, Cursor, Center for AI Safety, Vals AI, TBD Lab, FAIR). Stanford HAI received the definition it lacked book-wide. Four exercises were missing the formulas a non-programmer needs, and they now have them.
