# Reader test: chapters 43, 45, 46 and 47

Tested by reading chapters 43, 45, 46 and 47 in order, in full, as the intended reader: almost no computer-science background, a daily chatbot user for a year, and someone who has read the earlier chapters. Chapter 44 was tested in the first pass (see reader-test.md). Before treating a term as undefined I checked GLOSSARY.md and grepped the earlier chapters for a definition or a plain gloss. Every entry for these chapters in acronyms-by-chapter.json was worked through. I recomputed every worked example (all the arithmetic in Chapter 43's payback, IRR, 100 MW and token-cost examples, Chapter 45's IoU, precision/recall, OCR compounding and bottling-line figures, Chapter 46's CD bitrate, WER, WaveNet and bioacoustics figures, and Chapter 47's pixel counts, probability and detector figures). All of them check out. No sourced 2025–2026 fact was changed.

After editing, all four files pass `validate.py` (31/31 mermaid diagrams valid) and `check.py` (ch43, ch45, ch46 and ch47 all `[OK]`).

## Findings and fixes

| Chapter | Where | Problem a beginner would hit | Fix applied |
|---|---|---|---|
| 43 | Building costs, JLL bullet | JLL (used in 9 chapters) has no definition in this chapter. Cushman & Wakefield is not introduced | New definition callout: JLL (Jones Lang LaSalle). Glossed Cushman & Wakefield as a real-estate firm |
| 43 | Same list | "Greenfield cost" is jargon | Glossed (built from scratch on an empty site) |
| 43 | IT equipment paragraph | NVIDIA, GB200 and GB300 are central to the chapter but not defined here | New definition callouts: NVIDIA, and GB200 and GB300 |
| 43 | All-in cost per gigawatt | "Fluidstack" not introduced | Glossed as a GPU cloud company |
| 43 | Running costs, per-GPU power | The power price jumps from $70 per MWh to $0.08 per kWh, and the 2 kW figure appears from nowhere | Added the conversion ($70 per MWh = $0.07 per kWh, rounded up) and the 2.2 kW × 80% × PUE 1.2 ≈ 2.1 kW step |
| 43 | Same section | "45,000 GPU slots" not derived | Added "(100 MW × 450 slots per MW)" |
| 43 | Neoclouds versus hyperscalers | AWS (used in 22 chapters) is not defined here | New definition callout: AWS (Amazon Web Services) |
| 43 | Depreciation, what companies do | "2027 fiscal year" is unexplained | Glossed fiscal year (and that Microsoft's starts in July) |
| 43 | TCO, custom chips | Broadcom, Maia 200 and Helios are named with no explanation. MTIA and AMD are not defined here | Glossed Broadcom, Maia 200 and Helios. New definition callouts: MTIA and AMD |
| 43 | Fairwater worked example | The heading names Fairwater but the text never says what it is | Added "For its Fairwater AI data centers (Chapter 34)" |
| 43 | Layer 1: chips | "GAAP" and "guided to" are finance jargon. TSMC and SK hynix are not defined here | Glossed both terms. New definition callouts: TSMC and SK hynix |
| 43 | Layer 4: AI labs | "Recognized" revenue, "stock-based compensation" and booking "gross" versus "net" would lose a non-accountant | Glossed all three in plain words |
| 43 | Layer 4, then the bear case | "FT" is used as an abbreviation with no expansion | New definition callout: FT (Financial Times) |
| 43 | Layer 6 | "Per seat" | Glossed (per user) |
| 43 | The spending, intro | "Earnings calls" not explained, and "finance leases" appears about 40 lines before its definition | Glossed earnings calls. Added a short gloss of finance leases with a pointer to the later definition |
| 43 | Table 43.8 | Blue Owl and GIC are named without explanation | Glossed (an investment firm; Singapore) |
| 43 | Credit rating definition | AAA, BBB, the minus sign and "junk" (used later) are not explained. S&P is not defined | Definition now gives the letter scale and "junk". New definition callout: S&P (S&P Global Ratings) |
| 43 | Alphabet equity program | "Underwritten offerings", "mandatory convertible preferred shares" and "private placement" are dense finance jargon | Added a three-sentence parenthetical explaining each |
| 43 | Same paragraph and Going deeper | SEC (used in 7 chapters) and EDGAR are not defined | New definition callouts: SEC (Securities and Exchange Commission), with 10-K and 10-Q, and EDGAR |
| 43 | NVIDIA and OpenAI bullet | "Post-money valuation" is used before its definition. "IPO" is not expanded anywhere before Chapter 61. Reuters is not introduced | Glossed post-money with a "defined below" pointer. Expanded and explained IPO. Glossed Reuters |
| 43 | After the circular-deal examples | SB Energy (in 4 chapters) is not defined | New definition callout: SB Energy (glosses SoftBank too) |
| 43 | Sovereign funds | "Series G" is not defined until Chapter 61. MGX is not defined here | Glossed Series G. New definition callout: MGX |
| 43 | Exercise 3 | Steps 5 to 7 use the placeholders `total`, `power`, `rent` and `net`, which a beginner would type literally | Gave the exact cells (B9 to B15) and complete formulas. Checked: they reproduce $1.79, $2.56 and 3.9 years |
| 43 | Exercise 7 | No cell layout for `=IRR()`. In Case C (35% a year) later-year cash is negative and no IRR exists, so the spreadsheet shows #NUM! and the beginner thinks they made a mistake | Gave the column layout and `=IRR(B1:B6)`. Added a note that #NUM! is the answer in Case C. Verified: the 20% case gives −16% |
| 43 | Exercise 8 | "10-Q filings" is unexplained | Glossed, with a pointer to EDGAR |
| 43 | Key terms | The 14 new definitions were missing from the list | Added, in order of appearance |
| 45 | Vision foundation models | DINO is named but not described | Glossed as Meta's self-supervised vision models |
| 45 | Detection history | DETR is not expanded | Expanded (DEtection TRansformer) |
| 45 | Open-vocabulary detection | COCO is not expanded | Expanded (Common Objects in Context) |
| 45 | Segment Anything | "SA-1B" is not explained | Expanded (Segment Anything 1 Billion) |
| 45 | OCR worked example | 0.99^20: the reader is not told how to compute a power | Added what ^ means, the x^y key and `=0.99^20` |
| 45 | EU law bullet | CCTV is not expanded | Glossed (security-camera footage) |
| 45 | Liveness frontier box | "Deepfake" and "provenance" are first defined in Chapter 47 | Added a one-clause gloss of each with a pointer to Chapter 47 |
| 45 | SLAM definition | "AR headsets": AR is never expanded before this point | Expanded and glossed augmented reality |
| 45 | Industry table | "FDA-authorized": the FDA is not defined until Chapter 52 | Glossed the FDA as the US agency that approves medical devices |
| 45 | Industry table | Be My Eyes is not introduced | Glossed |
| 45 | Exercise 6 | No cells, and nothing says to copy the formula down to the other rows | Gave A1 to A4, B1 and C1, and told the reader to copy down. Explained ^ |
| 45 | Exercise 7 | "Gallery size ÷ 100,000" has no spreadsheet form | Gave cells and `=A1/100000` |
| 45 | Exercise 9 (Colab) | Step 4 tells the reader to type `model(url, conf=0.7)`, but `url` is never defined in the code, so it crashes with a NameError. `conf` is unexplained | Replaced with the full working line using the image address. Explained `conf` as the score threshold |
| 45 | Exercise 9 code comment | "Flip BGR colors to RGB": BGR is unexplained | Comment now explains the blue-green-red order |
| 45 | Going deeper | FRVT is not expanded | Expanded (Face Recognition Vendor Test) |
| 46 | Fairness section | PNAS is not explained | Glossed (a leading US science journal) |
| 46 | Same section | ALS is not explained | Glossed (amyotrophic lateral sclerosis) |
| 46 | Careless Whisper | "Aphasia" is a medical term | Glossed |
| 46 | Performers' livelihoods | "ELVIS Act" is a name with no expansion | Expanded (the Ensuring Likeness Voice and Image Security Act) |
| 46 | Labels and settlements | "Fair use" has no reminder (it is defined in Chapter 11). BMG is not introduced | Added a one-clause gloss with a pointer to Chapter 11. Glossed BMG as a music company |
| 46 | Bioacoustics | Project CETI is not expanded | Expanded (Cetacean Translation Initiative) and glossed |
| 46 | Areas of opportunity | QA, NGOs and HVAC are not expanded anywhere before this point (HVAC is first defined in Chapter 62) | Glossed all three |
| 46 | Exercise 3 | "Compute the WER" did not say what the reference is or what N is | Added: your written paragraph is the reference, N = 60 |
| 47 | Seeds and iteration | 1 − 0.8^4 appears without the reasoning (each try misses with probability 0.8, so all four miss with 0.8^4) | Added the bridging step |
| 47 | Figure 47.4 | The diagram's last box uses "Content Credentials", which is defined about 230 lines later | Caption now says what they are and where they are explained |
| 47 | Table 47.2 | "4K" and ByteDance are not explained | Glossed both |
| 47 | 3D, route 2 | Tencent is not introduced | Glossed |
| 47 | Why labs care | SIMA is not expanded | Expanded (Scalable Instructable Multiworld Agent) |
| 47 | C2PA definition | BBC is not expanded | Glossed |
| 47 | Exercise 1, step 3 | Tells the reader to change "wide shot" to "close-up", but the given prompt contains no "wide shot", so the step cannot be done | The step now says to add "wide shot", then change it to "close-up" |
| 47 | Exercise 3, step 4 | "Per-image rate ... raise it to the 10th power" gave no method | Added how to compute the rate (sum ÷ 5) and `=0.6^10` |
| 47 | Exercise 6 | Formulas were written in words with ×; there were no cells, and percentages had no input format | Gave cells B1 to B7, decimal inputs and the three formulas. Checked: they give 0.49 |

Fixes by type:

| Chapter | New definition callouts | Glosses of undefined terms or names | Reasoning or diagram bridges | Exercise fixes |
|---|---|---|---|---|
| 43 | 14 (all added to Key terms) | About 26 | 2 | 2 |
| 45 | 0 | 11 | 1 | 4 |
| 46 | 0 | 10 | 0 | 1 |
| 47 | 0 | 5 | 2 | 3 |

No fixes of the "plainly wrong" kind were needed.

## Noticed but not changed

- Parallel reader-test passes added definition callouts for NVIDIA, AWS, AMD, TSMC, GB200 and GB300, JLL, SK hynix and MGX to earlier chapters (3, 19, 30, 34, 38, 42) while this pass was running. The Chapter 43 callouts for these are therefore re-definitions. That is harmless: the glossary keeps the first definition and adds Chapter 43 as a reference, and STYLE.md allows a re-definition when the term is central. Whoever owns the glossary may still want to dedupe. JPEG (Chapter 3), MP3 (Chapter 3), IBM (Chapter 8) and DALL·E (Chapters 16 and 22) were already defined earlier, so Chapters 45, 46 and 47 needed nothing for them.
- No arithmetic errors, contradictions or wrong chapter cross-references were found. All the IRRs in Chapter 43 (8.5%, about −16%, 13.5%, 3.5%, $2.93 for 8%) and Table 43.6 reproduce exactly.
- Chapter 43's "Is it a bubble?" and financing sections remain the densest part of these four chapters for this reader. They lean on 2026 figures that are all marked as reported, so they should be refreshed after the late-October 2026 earnings.

## Verdict per chapter

**Chapter 43 (Economics of AI Compute).** The ramp is excellent in the first half. It goes from one cent per answer, to capex versus opex, to the $1.14-per-hour GPU, the payback and IRR of one slot, and a full 100 MW model with a sensitivity table, and every number is worked and correct. The friction was almost entirely vocabulary in the second half. Credit-rating letters, share-offering jargon, SEC, IPO, Series G, GAAP, "guided", gross versus net booking, and a dozen company and fund names arrived with no explanation. The definitions and glosses added here now cover every term. Two exercises had spreadsheet placeholders or an IRR that cannot exist, and both are fixed. Not every term was defined before this pass; after it, every term is.

**Chapter 45 (Computer Vision).** The ramp works well. It goes from pixels as a spreadsheet, up the task ladder, to pencil-and-paper IoU, precision/recall and the face-search base-rate example, and each rung is defined before use (62 definitions). The gaps were names: datasets and models (COCO, DETR, DINO, SA-1B, FRVT), and three terms the book defines only later (FDA, deepfake, provenance). The Colab exercise contained a real bug that would have crashed for every reader. Every term is now defined or glossed.

**Chapter 46 (Speech, Audio and Music).** This is the cleanest of the four. Sampling, then spectrograms, then ASR, then WER is a model ramp, and every worked example checks out. The definitions cover all the technical vocabulary. What was missing were glosses for medical terms (ALS, aphasia), a journal (PNAS), a law's name (ELVIS Act), CETI, BMG, and the stray QA, NGO and HVAC in the opportunities list. All are now glossed.

**Chapter 47 (Generative Media).** The ramp works: a one-section recap of the machinery, then products, then craft, then video, 3D, world models and provenance. The probability examples (seeds, consistency, detector base rates) are good teaching but slightly compressed; one bridging step was added. Every technical term already had a definition callout (57). Only company and project names (ByteDance, Tencent, SIMA, BBC, 4K) needed glosses. Three exercises needed fixing: one was impossible as written, and two had no spreadsheet mechanics.
