# Reader test: chapters 52, 53, 54 and 61

I read chapters 52 (AI for Science and Medicine), 53 (AI Across Industries and at the Edge), 54 (Other Paths to Intelligence) and 61 (The AI Industry Map) in order, in full, as the intended reader. That reader has almost no computer-science background, has used chatbots daily for a year, and has read the earlier chapters. Before treating a term as undefined, I checked GLOSSARY.md and the earlier chapters. I worked through every entry for these chapters in acronyms-by-chapter.json. An organization or product used in three or more chapters got a definition callout in the first of these chapters that uses it, and was added to that chapter's Key terms list. Every other entry got a gloss at its first use, or I record below why none was needed. I re-checked every worked calculation and every exercise answer.

After editing, all four files pass `validate.py` (35/35 mermaid diagrams valid) and `check.py` (52, 53, 54 and 61 all `[OK]`).

## Findings and fixes

| Chapter | Where | Problem a beginner would hit | Fix applied |
|---|---|---|---|
| 52 | Evo 2 paragraph | NVIDIA (used in 43 chapters) had no definition callout anywhere | New definition callout: NVIDIA (added to Key terms) |
| 52 | Physics, astronomy and fusion | NASA (used in 4 chapters) had no definition callout | New definition callout: NASA (National Aeronautics and Space Administration) (added to Key terms) |
| 52 | AlphaFold 2: how it works | "CASP14" did not say what the 14 means | Added "(the competition's 14th round)" |
| 52 | Figure 52.3 caption | "K (positive) ... E (negative)" means electric charge, which is never said | Caption now says K and E have opposite charges that attract |
| 52 | Figure 52.4 and step 2 | "Residues" appears in the diagram and is never explained | Added that biologists call each amino acid in a chain a residue |
| 52 | AlphaFold Database | EMBL-EBI was not explained | Glossed as part of the European Molecular Biology Laboratory, an intergovernmental research organization |
| 52 | AlphaFold 3 | RNA and "ions" were used with no explanation | Glossed both in the sentence |
| 52 | Protein design Watch out | "DNA-synthesis companies" was not explained | Glossed as firms that manufacture custom DNA to order |
| 52 | Evo 2 | Arc Institute was not introduced | Glossed as a nonprofit biomedical research institute in California |
| 52 | AlphaGenome | "Expressed" and "spliced" were unexplained biology jargon | Glossed both ("switched on"; "cut and rejoined before use") |
| 52 | Rentosertib case | "Phase IIa" was not covered by the Phase I/II/III definition | Glossed as the small, early part of Phase II |
| 52 | Figure 52.6 caption | "Phase IV monitoring" appears in the diagram and is never explained | Caption now explains Phase IV |
| 52 | Weather table, WeatherNext 2 | "Pixel forecasts" clashes with the glossary's "pixel" (an image dot) | Changed to "Google's Pixel phones" |
| 52 | Weather table and Try it | AIFS and IFS were never expanded | Expanded both (Artificial Intelligence Forecasting System; Integrated Forecasting System, ECMWF's physics model) |
| 52 | Lean paragraph | "Conjecture" was undefined | Glossed in the sentence |
| 52 | AlphaEvolve bullet | "The exponent of matrix multiplication" means nothing to this reader | Added that the exponent measures how fast the work grows with n, and that the schoolbook method (Chapter 5) has exponent 3 |
| 52 | AI co-scientist | Drug repurposing, acute myeloid leukemia, liver fibrosis and Sakana AI were unexplained | Glossed each in place |
| 52 | Fusion, particle physics, astronomy | Plasma, the Large Hadron Collider and exoplanets were unexplained | Glossed each in place |
| 52 | FDA device list | "Head CT" was unexplained | Glossed computed tomography |
| 52 | Imaging and pathology | MASAI was not expanded | Expanded (Mammography Screening with Artificial Intelligence) |
| 52 | IDx-DR | Retina and diabetic retinopathy were unexplained | Glossed both |
| 52 | Sepsis | Epic, "electronic health record" and JAMA were unexplained | Glossed each |
| 52 | Sepsis, TREWS | The acronym was not expanded | Expanded (Targeted Real-time Early Warning System) |
| 52 | Ambient scribes | "Best in KLAS" was meaningless to an outsider | Glossed KLAS Research and its award |
| 52 | Patients Try it | LDL was unexplained | Glossed as the so-called "bad" cholesterol |
| 52 | Medicine frontier box and Areas of opportunity | "Coding" here means medical billing codes. A reader who has just learned "coding" means programming would be misled | Glossed prior authorization and medical coding; changed "coding assistants" to "medical-coding assistants" |
| 52 | Exercise 3, step 4 | "Plume" was never defined | Glossed as a chart of every ensemble member's forecast |
| 52 | Exercise 6, step 4 | The hardest step had no hint and no target answer, unlike steps 2 and 3 | Added the 70 cases and 180 alerts, plus the expected answers (about 23 caught, 157 false, PPV about 13%) |
| 52 | Exercise 9, step 2 | "Tactics" was unexplained | Glossed, and noted that the game introduces each one |
| 53 | Big Sleep paragraph | DARPA (5 chapters) had no definition callout | New definition callout: DARPA (added to Key terms) |
| 53 | NPU paragraph | AMD (22 chapters) had no definition callout | New definition callout: AMD (Advanced Micro Devices) (added to Key terms) |
| 53 | Quantization Analogy | JPEG (5 chapters) had no definition callout | New definition callout: JPEG (added to Key terms) |
| 53 | Algorithmic trading definition | "Securities" was undefined | Glossed in the definition |
| 53 | Finance, Data | "Credit-bureau files" was unexplained | Glossed |
| 53 | Finance, Risks | "Dow Jones index" was unexplained | Glossed |
| 53 | Finance, Opportunities | SR 11-7 and the Federal Reserve were unexplained | Glossed both |
| 53 | Law | "Privileged", "statutes" and "briefs" are legal jargon | Glossed each at first use |
| 53 | Law, Opportunities | "Vertical" AI is not defined until Chapter 61, and Harvey was not introduced | Glossed "vertical", and Harvey through it |
| 53 | Education | "2 sigma" did not say that sigma is the standard deviation | Added the gloss |
| 53 | Figure 53.4 caption | "Edge device" is used about 200 lines before edge AI is defined | Caption now explains the term and points ahead |
| 53 | UPS example | ORION, GXO and "totes" were unexplained | Expanded ORION; glossed GXO and totes |
| 53 | Agriculture | Near-infrared light, combines, herbicide and right-to-repair were unexplained | Glossed each |
| 53 | Defense policy | Project Maven was unexplained | Glossed as a Pentagon drone-video AI program |
| 53 | Cybersecurity example | "Memory-safety flaw" and DEF CON were unexplained | Glossed both |
| 53 | Other industries table | Underwriting, virtual staging, HR, "royal commission" and FIFA were unexplained | Glossed each in its table cell |
| 53 | Quantization worked example | "Magnitude", and the table's "back to" and "error" columns, were never explained | Glossed magnitude; added a sentence on multiplying back by the scale |
| 53 | On-device runtimes | ONNX was not expanded | Expanded (Open Neural Network Exchange) |
| 53 | TinyML energy | CR2032 was unexplained, and the step from milliamp-hours to watt-hours was skipped | Glossed the battery; added that amp-hours × volts = watt-hours |
| 53 | Wearables | ECG and atrial fibrillation were unexplained | Glossed both |
| 53 | Exercise 5 | "Build the worked example" and "find the break-even point" gave no cells or formula, so a non-programmer could not do it | Gave cells B1 to B6, the total-cost formula, a check value (354000) and the expected break-even (about 56%) |
| 53 | Exercise 6 | A 5 × 5 grid of cells cannot each hold two numbers, so the exercise was impossible as written | Uses two grids now (NIR and red), with the NDVI formula, the copy instruction and the conditional-formatting menu path |
| 53 | Going deeper | NBER was unexplained | Expanded and glossed |
| 54 | MYCIN/XCON paragraph | MYCIN and XCON (3 chapters each) had no definition callouts | New definition callouts: MYCIN and XCON, worded to agree with Chapter 7 (added to Key terms) |
| 54 | Same paragraph | Digital Equipment Corporation was unexplained | Glossed as a leading computer maker of the time |
| 54 | Backward chaining | "E. coli" was unexplained | Glossed as a common bacterium |
| 54 | Logic worked example | Why "IF alarm THEN locked" means "NOT alarm OR locked" was skipped | Added "either the alarm is off, or the door is locked" |
| 54 | Semantic Web | RDF was not expanded | Expanded (Resource Description Framework) |
| 54 | Wikidata | The Wikimedia Foundation and "infoboxes" were unexplained | Glossed both |
| 54 | SPARQL query | SPARQL was unexplained, and the `?` and `#` in the code were not explained | Glossed SPARQL; explained `?` blanks and `#` comments |
| 54 | Bayes' rule | The formula's symbols (P( ), "given", A, B) were never spelled out | Added a sentence explaining each symbol with the disease-test example |
| 54 | Compression paragraph | The "− 1" in 2^3 − 1 = 7 was unexplained | Added that the 8 probabilities must sum to 1 |
| 54 | Era 1 of language AI | IBM (8 chapters) and ALPAC (3 chapters) had no definition callouts | New definition callouts: IBM (International Business Machines) and ALPAC (Automatic Language Processing Advisory Committee) (added to Key terms) |
| 54 | Era 4 | NLLB was not expanded | Expanded (No Language Left Behind) |
| 54 | BLEU worked example | "Geometric mean" and √ were unexplained | Added "multiply, then take the square root" |
| 54 | Brains to AI | "Dopamine" was unexplained | Glossed |
| 54 | BCI table | "Stent", "Utah arrays" and BrainGate were unexplained | Glossed in the table cells |
| 54 | What has been achieved | UC (5 chapters) had no definition callout; UCSF and ALS were unexplained | New definition callout: UC (University of California) (added to Key terms); expanded UCSF; glossed ALS |
| 54 | Exercise 3, step 2 | The exercise did not say how to get a conditional probability from the table | Added which rows to add and divide |
| 54 | Exercise 4 | "Use MAX and MIN formulas" gave a non-programmer no way to build a ramp | Gave the warm, hot, fan-speed and thermostat formulas with cells, plus a check value (26°C gives about 67%) |
| 61 | OpenAI run-rate paragraph | FT (3 chapters) had no definition callout | New definition callout: FT (Financial Times) (added to Key terms) |
| 61 | Gross versus net Watch out | "Top line" is finance shorthand | Glossed |
| 61 | IPO wave | SEC (7 chapters) and EDGAR (3 chapters) had no definition callouts | New definition callouts: SEC (Securities and Exchange Commission) and EDGAR (added to Key terms) |
| 61 | Table 61.1 | Stargate appears 250 lines before it is explained | Glossed in the table cell |
| 61 | Layer 0 | Epoch AI and "shell and core" were unexplained; JLL (9 chapters) had no callout | Glossed Epoch AI and shell and core; new definition callout: JLL (Jones Lang LaSalle), with the label matched to Chapters 38 and 43 |
| 61 | Layer 1 | "Fiscal quarter" was unexplained; TSMC (14 chapters), SK hynix (8) and ASML (5) had no callouts in this chapter | Glossed fiscal quarter; new definition callouts: TSMC, SK hynix and ASML (added to Key terms) |
| 61 | Layer 2 | AWS (22 chapters) had no callout; "earnings calls" and FactSet were unexplained | New definition callout: AWS (Amazon Web Services) (added to Key terms); glossed both |
| 61 | Layer 6 | Palantir was unexplained; HAI (6 chapters) had no callout; MIT NANDA was unexplained here | Glossed Palantir; new definition callout: HAI (added to Key terms); glossed MIT NANDA with a pointer to Chapter 28, which defines it |
| 61 | Follow one dollar | Cushman & Wakefield and "substrates" were unexplained | Glossed both |
| 61 | Figure 61.7 caption | "PMs" was never expanded | Added "PMs are product managers" |
| 61 | Figure 61.9 caption | "SaaS" is never defined anywhere in the book | Glossed in the caption |
| 61 | Legal-AI worked example | The step from 100,000 tokens to "0.1 ×" a per-million price was skipped | Added that 100,000 tokens is 0.1 million and 5,000 is 0.005 million |
| 61 | Capex-revenue gap | "BBB-" and "1990s fiber" were unexplained | Glossed both, pointing to Chapter 43 for credit ratings |
| 61 | Exercise 2 | No starting cells, no first value and no instruction to fill column C | Gave A2:A13, B2 = 100, the fill instructions and check values (about 5,580 against about 2,900) |
| 61 | Exercise 4 | Step 4 asks the reader to change utilization, but the model in step 1 had no utilization and no cost-per-GPU-hour line, so the change did nothing | Added utilization, the yearly-cost and cost-per-GPU-hour formulas, and check values ($15,200; $2.48) |
| 61 | Exercise 5 | "Monthly" had no month length | Specified 30 days |

### Fixes per chapter, by type

| Chapter | New definition callouts | Glosses for undefined terms | Beginner-jump bridges | Exercise fixes | Errors corrected | Total |
|---|---|---|---|---|---|---|
| 52 | 2 | 24 | 4 | 3 | 0 | 33 |
| 53 | 3 | 25 | 5 | 2 | 0 | 35 |
| 54 | 5 | 10 | 4 | 2 | 0 | 21 |
| 61 | 9 | 13 | 1 | 3 | 0 | 26 |

That is 115 fixes in all, including 19 new definition callouts. Every new callout was added to its chapter's Key terms list.

I found no arithmetic errors, contradictions or wrong cross-references. I re-checked every worked example and every stated answer: Levinthal's numbers, clinical attrition and the drug timelines, the GraphCast grid, the screening trees and PPV figures, the fraud, service-desk and maintenance arithmetic, NDVI, quantization, the federated average, the certainty-factor chain, the Bayesian network, the umbrella filter, the fuzzy fan, the genetic-algorithm generation, Simpson's table, BLEU, the run-rate and valuation sums, the per-GPU cost, the job-board bars and the revenue multiples. I also confirmed that the Colab backpack optimum really is 30 by brute force. Cross-references to Chapters 5, 6, 10, 11, 28, 48, 54, 59 and 60 point to content that is really there.

## Acronym entries handled without a new callout

- **Already glossed by context or expanded in the text:** ECMWF, ERA5, ESM3, GFP (esmGFP), ISM001, MVKLAGTSEF (a sample sequence), TNIK, DAX (named as a product), CASP14 (now glossed), FERPA, NIR, CNET ("the tech site"), DEF CON, OWL, MCMC, DAG, GNMT, VP (in the caption), SHRDLU and SYSTRAN (program names explained in context).
- **Not acronyms:** IF, THEN, IS and HAS in Chapter 54 are logic keywords shown in examples, and MIN is a spreadsheet function, now explained in Exercise 4.
- **Already covered by an earlier chapter:** NP (NP-hard) is glossed in the sentence through Chapter 48's NP-complete. MIT NANDA is already defined in Chapters 28 and 31, so Chapter 61 gets a gloss and a pointer rather than a third callout.
- **Left as an everyday word:** COVID.

## Noticed but not changed

- **2026 claims for whoever owns sources.** Chapter 61 says SpaceX absorbed xAI (February 2026), listed on June 12, 2026 near a $2.1 trillion value, and agreed to buy Cursor's maker for about $60 billion. These claims also shape Tables 61.3 and 61.5. They are sourced 2026 facts, so I left them alone. They are unusual enough to deserve a fact-check, as the earlier reader test also said about Chapter 44's "SpaceXSI (formerly xAI)".
- **Other sourced numbers left as written:** the AlphaEvolve bound of 2.371177 (August 2026 preprint) in Chapters 52 and 54, and the AI Impacts range of 10^12 to 10^28 operations per second for brain compute in Chapter 54.
- **Duplicate organization callouts.** Several organization callouts now appear in many chapters, because each reader adds one in their first chapter. For example, NASA is also defined in Chapter 48, and DARPA and UC in Chapter 49. I matched existing labels so the glossary merges them. Chapter 7 labels IBM as plain "IBM", while Chapters 8, 54 and 59 use "IBM (International Business Machines)", so the glossary will show two IBM entries. That is a one-word fix in Chapter 7.
- **"SaaS" has no definition callout anywhere in the book.** I added only a caption gloss in Chapter 61. If it is used elsewhere, one callout in its first chapter would help.

## Verdicts

**Chapter 52 (AI for Science and Medicine).** The difficulty ramp works. The chapter assumes no biology and builds proteins, DNA, drug trials and screening statistics from zero, with 79 definitions and worked numbers that all check out. The steepest stretch is the mathematics section, which is now bridged by the conjecture and exponent glosses. The friction was vocabulary dropped in passing: RNA, plasma, retina, spliced, CT, Phase IIa and Phase IV, and institutional names. One real trap was "coding" meaning medical billing, which a reader who has just learned "coding" means programming would misread. With the fixes, every term is defined or glossed where it is first used.

**Chapter 53 (AI Across Industries and at the Edge).** The ramp is gentle and well judged. The five-part template repeats for each industry, every industry gets a worked number, and the edge-AI half rebuilds NPUs, TOPS and memory bandwidth from earlier chapters before the quantization example. The friction was domain jargon from finance, law and insurance (securities, privileged, briefs, underwriting), two quantization-table columns that were never explained, and two spreadsheet exercises that could not be built as written. After the fixes, every term is defined or glossed and every exercise can be done.

**Chapter 54 (Other Paths to Intelligence).** This is the most demanding of the four, because it tours seven fields. The ramp still works, because every section opens with a small example worked by hand: the car rules, the wet grass, the umbrella, the fan, the backpack and Smart Summaries. A beginner would have stalled in two places: the probability notation P(A given B), and the logic rewrite behind resolution. Both now have bridging sentences. Historic systems and organizations (MYCIN, XCON, IBM, ALPAC, UC) now have callouts, and the two spreadsheet exercises give their formulas. Every term is now defined or glossed.

**Chapter 61 (The AI Industry Map).** The vocabulary-first design is excellent. Every money term is defined before it is used, with worked numbers, and all the arithmetic checks out. The gaps were names and shorthand the chapter treated as known: TSMC, ASML, SK hynix, JLL, the SEC and EDGAR, the FT and HAI, plus "top line", "fiscal quarter", "BBB-", "earnings calls" and "SaaS". There was also one exercise that asked the reader to change utilization in a model that had no utilization in it. With the fixes, every term is defined or glossed. The reliance on dated, reported 2026 figures is clearly signposted throughout.
