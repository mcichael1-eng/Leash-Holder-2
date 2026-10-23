# Reader test: chapters 29 to 32

Tested by reading chapters 29, 30, 31 and 32 in order, in full, as the intended reader: almost no computer-science background, a daily chatbot user for a year, who has read chapters 1 to 28. Before treating a term as undefined I checked every earlier chapter for a definition callout or a plain gloss. Every entry for these chapters in `acronyms-by-chapter.json` was worked through. Organizations and products used in three or more chapters got a definition callout here, in the first of these four chapters that uses them. Units got a definition callout where they are first used. Every other entry got a gloss at its first use, or already had one from context (listed at the end). All worked arithmetic in the four chapters was re-computed. Nothing was rewritten for style and no content was cut.

After editing, `validate.py` passed on all four files (37/37 diagrams valid) and `check.py` reported `[OK]` for chapters 29, 30, 31 and 32.

## Findings and fixes

| Chapter | Where | Problem a beginner would hit | Fix applied |
|---|---|---|---|
| 29 | Frontend definition | "HTML, CSS and JavaScript": HTML and CSS are defined nowhere in the book (JavaScript is covered in Chapter 3) | New definition callout: HTML and CSS (added to Key terms) |
| 29 | Instruction file definition | "It is a README written for agents": README never explained | Glossed README as the welcome-and-instructions file projects keep for human readers |
| 29 | Coding-agent table, Devin row | "SWE-series models" with no expansion | Added "SWE is short for software engineering" |
| 29 | Market paragraph | "Run-rate revenue" is first defined in Chapter 43 | Inline gloss: recent revenue multiplied up to a full year |
| 29 | Vibe coding | "Collins named..." with no hint that Collins is a dictionary | "Collins, the dictionary publisher" |
| 29 | Evidence list | Veracode and CodeRabbit named with no explanation | Glossed each as a security-testing company and an AI code-review company |
| 29 | Evidence list, package hallucination | "USENIX Security Symposium" unexplained | Glossed as a leading security conference run by the association USENIX |
| 29 | App builders, "The last 20%" | "Edge cases" is defined only in Chapter 31 | Inline gloss: rare and unusual situations the app must still handle |
| 29 | Receipt-logger cost | 100,000 and 10,000 tokens appear without the multiplication behind them, and no link from 100,000 to "per million" | Showed 100 × 1,000 and 100 × 100, and that 100,000 is a tenth of a million |
| 29 | Exercise 6 | "the method (GET)" | Glossed GET with a pointer to Chapter 26 |
| 29 | Exercise 8, step 2 | A non-programmer is told to "run the tests" with no way to do it | Added "(or ask the agent to run them)" |
| 29 | Exercise 9 | Asks to compare measured speed with a predicted "% faster" but never says how to compute a percentage from two averages | Added the rule and a worked example (20 vs 16 minutes = 20% faster) |
| 29 | Going deeper, Missing Semester | "CS" unexplained | Added "CS stands for computer science" |
| 30 | Full fine-tuning memory | "Eight times the memory of the free GPU in Google Colab": the 16 GB figure only appears 90 lines later | Added "(16 GB)" |
| 30 | LoRA quality study | Thinking Machines Lab named with no description | "the AI startup Thinking Machines Lab" (matches Chapter 18) |
| 30 | Figure 30.3 | The diagram's formula uses alpha and r; alpha is explained only after the figure | Caption now says the product is scaled by alpha ÷ r, names r as the rank and points to alpha just below |
| 30 | QLoRA frontier box | "Quantization-aware training" used about 250 lines before its definition | Added a short gloss and "defined later in this chapter" |
| 30 | Where to fine-tune table | "Vertex AI" unexplained | "Vertex AI, its cloud AI platform" |
| 30 | Open-weight Watch out vs. memory table | Text says DeepSeek V4-Pro at 4 bits is "about 800 GB"; the table a few lines later says about 960 GB | Added "(nearer 960 GB once the scaling numbers are counted, as the table below shows)" |
| 30 | KV-cache worked example | Typo "A 8,000-token conversation" | "An 8,000-token" |
| 30 | No GPU, small GPU, non-NVIDIA | NVIDIA (43 chapters) and AMD (22 chapters) have no definition anywhere in the book | New definition callouts: NVIDIA, and AMD (Advanced Micro Devices) (both added to Key terms) |
| 30 | Speed rule | The "≤" sign is used without explanation | Added (the sign ≤ means "is at most") |
| 30 | Quantization ruler | "2 ÷ 15" with no reason for 15 | Explained that 16 marks have 15 gaps covering a distance of 2 |
| 30 | Other formats | AWQ and GPTQ unexplained | Glossed as files made by two popular 4-bit quantization methods (AWQ expanded) |
| 30 | JPEG analogy | JPEG named with no gloss in this chapter | "the everyday compressed photo format (Chapter 3)" |
| 30 | Exercise 4 | Formulas written with × and ÷ fail in a spreadsheet; the config.json field names for layers, KV heads and head size are not given | Added the field names (num_hidden_layers, num_key_value_heads, head_dim), a column layout and the four exact spreadsheet formulas, including how $N$1 works |
| 30 | Exercise 9 | "Rerun Cell 7 with num_train_epochs=1" would keep training the already-trained adapter, giving a misleading result; "add a new sentence pattern used only for the held-out set" gave no way to do it | Now says to rerun Cells 3, 5, 6, 7 and 8 so the adapter starts fresh, and gives the exact `templates.append(...)` line and where to put it |
| 30 | Exercise 10 | "curl" unexplained; the Python script has no instruction on how to run it | Glossed curl; added "save it as ask.py and run python3 ask.py (python ask.py on Windows)" |
| 30 | Areas of opportunity | "NGOs" unexplained | "(non-governmental organizations, such as charities)" |
| 31 | Grading two prompts | "(7 + 1) ÷ 128" appears with no explanation of 128 or 7 + 1 | Added two sentences: 7 coin flips give 2^7 = 128 patterns, 8 of which give B six or more wins |
| 31 | Evaluating agents | 0.99^50 used with no reminder of what the notation means or how to compute it | Glossed as 0.99 multiplied by itself 50 times, with `=0.99^50` |
| 31 | CVE definition | "CVSS" not expanded | Added "(Common Vulnerability Scoring System)" |
| 31 | Package hallucination | "USENIX Security Symposium" unexplained in this chapter | Glossed as a leading academic computer-security conference |
| 31 | Red-teaming Try it | "Lakera" unexplained | "from Lakera, an AI-security company" |
| 31 | Table 31.4 | LLM01 to LLM10 codes never explained | Caption now says they are the list's own numbers for the ten risks |
| 31 | NIST AI RMF definition | NIST is first defined in Chapter 59 | Expanded NIST inside the definition |
| 31 | MITRE ATLAS definition | MITRE unexplained | Glossed as a US nonprofit that runs research centers for the government |
| 31 | Frameworks | "ISO/IEC 42001": ISO and IEC unexplained (defined only in Chapter 59) | Glossed ISO and IEC as the two main international standards bodies |
| 31 | Levers, batching | "$3.80", "$1.90" and "$0.19" appear with no token assumptions, so a reader cannot reproduce them | Added the assumptions (650 input, 250 output tokens) and the formula; checked that all three figures follow |
| 31 | Buy or build | MIT NANDA (5 chapters) has no definition anywhere; Chapter 31 dated its report "August 2025" while Chapters 28, 61, 63 and 64 say July 2025 | New definition callout: MIT NANDA (added to Key terms); removed the conflicting month (see below) |
| 31 | Exercise 7, step 5 | No hint how to find the cap that keeps a 70% margin | Added: cost must stay at or below $6, so divide $6 by the cost of one agent task (checked: 14 and 32) |
| 31 | Exercise 8, step 5 | "UX patterns": UX never expanded | "UX (user-experience) patterns" |
| 31 | Going deeper, Amershi et al. | "CHI 2019" unexplained | Added that CHI is the main academic conference on human-computer interaction |
| 32 | RISC-V definition | "RISC" never expanded anywhere in the book | Added pronunciation and "RISC stands for reduced instruction set computer" |
| 32 | CPU section | "EPYC" and "Helios rack" unexplained | Glossed both |
| 32 | Table 32.1 | TFLOPS, PFLOPS and EFLOPS used with no unit definition; "PF" in Table 32.2 never explained | New definition callout: TFLOPS, PFLOPS (PF) and EFLOPS |
| 32 | Table 32.1 | GB300 NVL72 (13 chapters) has no definition before Chapter 34 | New definition callout: GB300 NVL72 (consistent with Chapter 34's) |
| 32 | TPU v1 peak formula | "700 MHz" and "92 TOPS" appear before either is explained (TOPS is defined 30 lines later) | Glossed MHz as millions of ticks per second; said TPU v1 used whole numbers, so its speed is in TOPS (defined below) |
| 32 | Llama 3.1 training time | The step from 5.9 million seconds to 68 days was skipped | Added "a day has 86,400 seconds" and the division |
| 32 | CUDA changes the game | TSMC (14 chapters) is never defined before Chapter 36; "3-nanometer-class process" unclear | New definition callout: TSMC; "process" became "manufacturing process" |
| 32 | Tensor core definition | "MXU" used before it is explained | "(matrix multiply unit, described below)" |
| 32 | Floating point example | "6.5 in binary is 110.1" assumes the reader knows binary fractions | Added that 110 is 6 and the 1 after the binary point means one half |
| 32 | MX formats definition | "Open Compute Project" unexplained | Glossed as an industry group that publishes open data-center hardware designs |
| 32 | MXFP4 example | Why the power-of-two scale is 0.0625 and not 0.03125 was not said | Explained that 1/32 would push 0.30 past FP4's largest mark (9.6 > 6) |
| 32 | Precision frontier box | "H800 GPUs" unexplained | Glossed as a China-market H100 with slower chip-to-chip links |
| 32 | ASIC section | MTIA (4 chapters) has no definition | New definition callout: MTIA (Meta Training and Inference Accelerator) |
| 32 | Inference specialists | "GTC 2026" unexplained; LPX (8 chapters) has no definition | Glossed GTC; new definition callout: LPX |
| 32 | Wafer-scale engine definition | "WSE-3" in the table never linked to the abbreviation; "lithography machine" first defined in Chapter 36 | Label now "Wafer-scale engine (WSE)"; glossed the lithography machine with a pointer to Chapter 36 |
| 32 | Table 32.6 / 32.7 | AWS (22 chapters) has no definition anywhere | New definition callout: AWS (Amazon Web Services) |
| 32 | Table 32.7 | "2H 2025", "SXM", "LPDDR5X" and "CES 2026" unexplained | Caption explains 2H and SXM and glosses CES; table cell glosses LPDDR5X |
| 32 | After Table 32.7 | MI355X (7 chapters) and MI455X (9 chapters) have no definition | New definition callout: MI355X and MI455X (facts taken from the chapter's own table) |
| 32 | Table 32.8 | "28 MiB" next to MB elsewhere | Glossed MiB |
| 32 | Pixel Visual Core | "HDR+" unexplained | Added "(high dynamic range)" |
| 32 | Exercise 7, step 3 | "Convert to time" with no rule for dividing by TFLOPS/PFLOPS | Gave time = operations ÷ operations per second, the three speeds in powers of ten, and the spreadsheet E-notation |
| 32 | Exercise 9 | "per dollar-hour" not explained, and price ranges given with no rule for which value to use | Explained the division, said to use the middle of each range, with a worked H100 example (80 ÷ 3.34 ≈ 24) |

Fixes per chapter by type:

| Chapter | Undefined terms (new definitions + glosses) | Beginner jumps | Exercises | Plainly wrong / contradictions | Total |
|---|---|---|---|---|---|
| 29 | 11 (1 + 10) | 1 | 2 | 0 | 14 |
| 30 | 10 (2 + 8) | 3 | 3 | 2 | 18 |
| 31 | 10 (1 + 9) | 3 | 1 | 1 | 15 |
| 32 | 21 (7 + 14) | 3 | 2 | 0 | 26 |

That is 73 fixes in total. Eleven new definition callouts were added, each also added to its chapter's Key terms list: HTML and CSS (29); NVIDIA, AMD (30); MIT NANDA (31); TFLOPS, PFLOPS (PF) and EFLOPS, GB300 NVL72, TSMC, MTIA, LPX, AWS, MI355X and MI455X (32). One existing label was extended to "Wafer-scale engine (WSE)".

## Acronym-list entries that needed no edit

- **29:** CLAUDE (the CLAUDE.md file name, already explained in the Instruction file definition).
- **30:** WHO / WHAT / WHEN (labels on the example card in the Colab code, self-explanatory in context).
- **31:** FAIL and PINEAPPLE (ordinary words in capitals); SWE (SWE-bench is glossed in place and defined in Chapter 24); ATT&CK (glossed in place as "MITRE's catalog of conventional cyberattacks"); NVIDIA (now defined in Chapter 30).
- **32:** GB200 (defined in Chapter 19); GTX ("gaming cards" in the same sentence); FMA (glossed where used); MXFP8 and MXFP6 (named inside the Microscaling definition); HBM3 (named in the HBM definition); VCU (expanded in place); MLIR, TVM and CUTLASS (described by their sentences as compiler or kernel-writing software).

## Noticed but not changed (for the fact owners)

- **MIT NANDA report date (Chapter 31).** Chapter 31 called it "an influential August 2025 report", while Chapters 28, 61, 63 and 64 date it July 2025 (the report is dated July 2025; press coverage peaked in August). I removed the month from Chapter 31 rather than choose one. Whoever owns the sourcing should confirm the date and, if wanted, restore "July 2025".
- **Chapter 32, the memory-wall puzzle.** It says real chatbots run "such a model" (70B) "on one GPU" at the H100's speed, while Table 32.5 says a 70B model in BF16 does not fit on one 80 GB H100 (only at FP8 or below). It does not change the lesson, but a careful reader may notice.
- **Chapter 31, model tiers.** Table 31.5 puts Claude Fable 5.1 at $10/$50 as the "Large" tier, and a few paragraphs later the fast-mode sentence prices Claude Opus 5.5 at $4/$20 standard. The two do not contradict each other, but the reader is never told where Opus sits among the tiers.
- **Chapter 29** says the "lethal trifecta" is "of Chapter 31". Chapter 28 defines it first, and Chapter 31 covers it in depth, so the pointer is not wrong.

## Verdicts

**Chapter 29 (Coding With AI and Building Without Code).** The ramp works well. The chapter starts from what an app is made of, builds Git, tests and deploys with one running example (the Book Club Picker), and only then brings in agents. A beginner who never wrote code can follow the agent loop because the chapter has already shown what a diff, a test and a pull request look like. Every technical term already had a callout. The gaps were HTML and CSS (used inside a definition and defined nowhere in the book) and the company names used as evidence (Veracode, CodeRabbit, Collins, USENIX). The cost examples recompute exactly. The exercises are realistic for a non-programmer. They needed only a way to run tests without coding and a way to turn two timings into a percentage. Every term is now defined or glossed.

**Chapter 30 (Customizing Models).** This is the hardest of the four for the target reader, because of the Colab walkthrough and the memory arithmetic. The ramp still works. The 3 × 3 LoRA example, the memory table and the ruler picture build intuition before the real numbers arrive. The numbers are right: 42 million LoRA parameters for Llama 3 8B, 17.4 million for Qwen3-1.7B, 0.125 MB per token of KV cache, and the $710 / $330 / $36 cost ladder. The real problems were in the exercises. The spreadsheet formulas were written with × and ÷ and did not name the config.json fields. One instruction ("rerun Cell 7") would quietly have continued training the old adapter and produced a misleading comparison. A Python script came with no word on how to run it. NVIDIA and AMD, used across 40-plus chapters, are now defined here for the first time. Every term is now defined or glossed.

**Chapter 31 (Shipping AI).** The ramp works. The invented Juni shop carries the reader from evals through security, cost and design, so each new idea lands on something concrete. Statistics is the steepest step. The standard-error table is well scaffolded, but the "1 time in 16" paired comparison skipped its counting step, which is now shown. All cost, margin, cascade and reliability arithmetic recomputes, including the exercise check values (14 and 32 agent tasks). The undefined terms were almost all organizations and standards (NIST, MITRE, ISO/IEC, CVSS, Lakera, MIT NANDA) plus UX and CHI. One date conflicted with four other chapters. Every term is now defined or glossed.

**Chapter 32 (CPUs, GPUs, TPUs and FLOPs).** The core teaching is excellent and fully checkable by hand. The worked numbers all reproduce: shift-and-add multiplication, the peak formula on the V100 (125 TFLOPS) and TPU v1 (92 TOPS), the 68-day Llama 3.1 run, the tick-by-tick systolic array, FP4 and MXFP4 block scaling, and the answer to Exercise 4. The chapter is also the densest in the book so far for product names and abbreviations: 31 acronym-list entries, plus spec-table shorthand such as 2H, SXM, PF and MiB. These cluster in the spec tables and frontier boxes, so that is where a beginner felt lost. Seven new definitions now cover the companies and products that recur across many later chapters (TSMC, AWS, GB300 NVL72, MI355X/MI455X, MTIA, LPX) and the speed units. A reader who did Chapters 2 and 5 can follow it, and Chapter 33 depends on it. Every term is now defined or glossed.
