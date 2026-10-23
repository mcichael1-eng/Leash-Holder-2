# Reader test: chapters 34 to 37

Tested by reading chapters 34 (servers, racks and networks), 35 (the AI chip industry), 36 (how chips are made) and 37 (training and serving at scale) in order, in full, as the intended reader: almost no computer-science background, a daily chatbot user for a year, who has read chapters 1 to 33. Before treating a term as undefined I checked GLOSSARY.md and grepped every chapter for a definition callout, because other passes were adding definitions at the same time. Every entry for these chapters in acronyms-by-chapter.json was worked through: organizations, products and units used in three or more chapters got a definition callout in the first of these four chapters that uses them (and in that chapter's Key terms list); everything else got a gloss at its first use. Edits are small and surgical; nothing was cut, restructured or rewritten for style.

After editing, all four files pass `validate.py` (34/34 mermaid diagrams valid) and `check.py` (ch34 to ch37 all `[OK ]`).

## Findings and fixes

| Chapter | Where | Problem a beginner would hit | Fix applied |
|---|---|---|---|
| 34 | Why one chip is not enough, Memory | NVIDIA is the subject of the whole chapter and is never defined | New definition callout: NVIDIA |
| 34 | Same section, Time | "Dense BF16" used; "dense" is only taught as a spec-sheet idea in Chapter 32 | One-clause gloss with a pointer to Chapter 32 |
| 34 | Table 34.1 and its lead-in | GB300/GB200 never defined; PF, EF, ZF and PB units used in the first table with no explanation | New callouts: GB200 and GB300; TFLOPS and PFLOPS (PF); EF and ZF (exaFLOPS and zettaFLOPS); PB (petabyte) |
| 34 | Cluster-power bullet | "IT load" is defined only in Chapter 39 | Glossed as the power used by the computing equipment itself |
| 34 | The die and the reticle limit | "TSMC's 4N process": neither TSMC nor "process" (node) is defined before Chapter 36 | Gloss for process; new callout: TSMC |
| 34 | Chiplets | NVL72/NVL144 naming never explained; AMD and the MI300X/MI455X used with no introduction | Added a sentence on what "NVL" and the number mean; new callouts: AMD, and AMD Instinct (MI300X, MI355X, MI455X) |
| 34 | HBM | "AMD's MI400 family" unexplained | Glossed as the family that includes the MI455X |
| 34 | A kilowatt in your palm | "SXM version" used a section before SXM is defined | Pointer to the next section |
| 34 | Same section, and the VRM definition | "DC" (direct current) used; it is defined only in Chapter 39 | Gloss with a pointer to Chapter 39 |
| 34 | Superchips | LPDDR5X used with no definition (3+ chapters) | New callout: LPDDR5X |
| 34 | Scale-up, NVSwitch paragraph | "72 GPUs would need 2,556 links" with no arithmetic | Showed 72 × 71 ÷ 2 and why |
| 34 | After Table 34.3 | "CES 2026" unexplained | New callout: CES |
| 34 | Other ways to scale up | MXFP8 used a chapter before MX formats are defined; AWS never defined | New callouts: MXFP8, AWS (Amazon Web Services) |
| 34 | Table 34.4 | "2H 2026 / 2H 2027" unexplained | Caption now says 2H means the second half of the year |
| 34 | 800 V DC definition; power swings | "415 V AC" and "capacitors" undefined until Chapter 39 | Glossed both |
| 34 | Switches and the fat tree | Broadcom never introduced | One-clause gloss |
| 34 | Fat-tree worked example | "Each doubling of ports multiplies the size by eight" with no reason | Added 2 × 2 × 2 and why |
| 34 | Tori, Virgo fabric | "47 Pb/s" unit unexplained | Glossed petabits per second |
| 34 | Figure 34.10 | The figure uses pipeline, context and data parallelism and FSDP, none yet explained (Chapter 37 does) | Added a one-paragraph bridge giving one line on each |
| 34 | Counting transceivers | Why the top layer needs only 780 switches was skipped | Added the reason (all 128 ports face down) |
| 34 | Optics power | "Huawei" unintroduced; the per-module watts are really a lower bound | Glossed Huawei; "implies at least ... (more if the replacement units draw power)" |
| 34 | Try it (optics) | "OSFP" unexplained | Glossed |
| 34 | Ironwood pod check | 42.5 million TFLOPS = 42.5 EF and 1,770,000 GB = 1.77 PB, conversions skipped | Added both conversions |
| 34 | Frontier box (clusters) | "Ascend chips" unexplained | Glossed as Huawei's AI chips |
| 34 | Failures at scale | "About 43,800 hours" unexplained | Showed 5 × 8,760 |
| 34 | Scale-across definition | "AI WAN" unexplained in this chapter | Glossed wide-area network |
| 34 | Distributed storage | GFS and Amazon S3 unexplained | Glossed both |
| 34 | Areas of opportunity | "FinOps" unexplained | Glossed |
| 34 | Exercise 2 | "NV#, PIX and SYS" codes unexplained | Said what each code means |
| 34 | Exercise 3 | No Tb/s conversion and no formula for transfer time | Added the conversion, the time rule and spreadsheet formulas |
| 34 | Exercise 4 | 1 GW ÷ 130 kW mixes units | Said to write 1 GW as 1,000,000 kW and multiply racks by 72 |
| 34 | Exercise 5 | No method for counting leaf, middle and top switches | Pointed to the worked example's method |
| 34 | Exercise 7 | "Which distances are affordable?" gave no criterion | Added the 1 ms (1,000 µs) budget per exchange |
| 34 | Going deeper | ISCA, SIGCOMM and HVDC unexplained | Glossed all three |
| 35 | Figure 35.1 caption | SK hynix (8 chapters) never defined | New callout: SK hynix |
| 35 | Fabless definition | "Foundry" is defined only in Chapter 36 | Glossed inside the definition |
| 35 | Fabless analogy | ASML (5 chapters) never defined | New callout: ASML |
| 35 | NVIDIA revenue | "Fiscal year 2027" for a 2026 quarter would confuse | Explained NVIDIA's February-to-January year |
| 35 | Same section | GTC (4 chapters) never defined | New callout: GTC (GPU Technology Conference) |
| 35 | Table 35.1 | HBM2, HBM2e and HBM3 never defined (glossary had only HBM3E onward) | Bridge sentence plus new callout: HBM2, HBM2e and HBM3 |
| 35 | Groq deal | "Groq 3 LPU" and "LPX rack" used about 240 lines before LPU is defined | New callout: LPX (Groq 3 LPX rack), which glosses LPU and points ahead |
| 35 | Rubin CPX | CPX (3 chapters) and GDDR7 undefined | New callout: Rubin CPX (glosses GDDR7) |
| 35 | Beyond the data center | GB10 and RTX unexplained | Glossed both |
| 35 | Table 35.3 | MI500 (3 chapters) and CDNA unexplained | New callout: MI500 (glosses CDNA) |
| 35 | ROCm paragraph | "MI450-series" unexplained | Glossed as the family including the MI455X |
| 35 | Meta MTIA | MTIA (4 chapters) undefined; "total cost of ownership" defined only in Chapter 37 | New callout: MTIA; glossed TCO in place |
| 35 | Wafer-scale engine definition | Tables use "WSE-3" but the definition never says WSE | Added "(WSE)" to the definition label and Key terms |
| 35 | Table 35.8 | "DDR" unexplained; "licensable IP" reads as the internet's IP | Glossed both |
| 35 | Table 35.10 | "PORTS-Pike" and SB Energy (13 chapters) unexplained | Glossed the site; new callout: SB Energy |
| 35 | Translating a gigawatt deal | "Add up the gigawatts in Table 35.10 (roughly 35–40 GW)": the table now sums to about 43–45 GW | Corrected to "roughly 43–45 GW"; the conclusion (well over a trillion dollars) is unchanged |
| 35 | Exercise 4 | "Growth" and the ridge point gave no method; PF ÷ TB/s needs a unit step | Said to divide Rubin by H100, convert PF to TFLOPS, with the H100 check value 295 |
| 35 | Exercise 5 | "GB of HBM per dollar-hour" unclear; A100 specs not in the chapter's tables in usable form | Said what to divide; gave A100's 80 GB and 2 TB/s |
| 35 | Exercise 6 | No rule for chips needed | Gave GB ÷ memory per chip, rounded up |
| 35 | Exercise 7 | No formula for slots per gigawatt | Gave the formula |
| 35 | Exercise 8 | Break-even had no formula | Gave the saving formula and the break-even condition |
| 35 | Areas of opportunity | MLIR, RTL and Pallas unexplained | Glossed all three |
| 35 | Going deeper | ACM (3 chapters) unexplained | Glossed in place (see below) |
| 36 | Foundry definition | SMIC (3 chapters) unexplained | New callout: SMIC |
| 36 | Why 300 mm | π × 150 × 150 and "2.25 times" with no reasoning | Added the circle-area rule and 1.5 × 1.5 = 2.25 |
| 36 | First Try it | "Process node" used before its definition | Glossed with a pointer |
| 36 | Fab loop, Figure 36.2 | The figure says "anneal" and "CMP", which the steps never name | Named annealing in step 7 and pointed to CMP in step 8 |
| 36 | Thousand-step table | "0.999^1000" notation unexplained | Explained ^ and gave a spreadsheet check |
| 36 | Transistor shapes | "CFET" unexplained (and FET never expanded) | Glossed both |
| 36 | Table 36.2 | Column header uses λ, never introduced | Said λ is the symbol for wavelength |
| 36 | Yield formula | No way to turn mm² into cm² or to compute e to a power | Added the ÷ 100 step, the e^x key and `=EXP()` |
| 36 | Supply chain, Figure 36.8 | Figure says "Licensed IP"; a reader knows IP only as internet addresses | Glossed IP as intellectual property in the text |
| 36 | Figures 36.8 and 36.9 | "TEL", "JSR" and "TOK" appear only in the diagrams | Named them in the text |
| 36 | Table 36.6 | "Capex" undefined until Chapter 43 | Glossed |
| 36 | January 2026 rule | "Section 232 tariff" used about 75 lines before its definition | Gloss with a pointer |
| 36 | Huawei roadmap | Huawei calls Ascend chips "NPUs", which contradicts Chapter 35's phone-NPU definition | Added a bridging sentence |
| 36 | Exercise 3 | `=B$1^$A2`: the $ signs are unexplained | Explained them and gave the grid range |
| 36 | Exercise 4 | Rearranging the formula for NA is algebra the reader has not done | Gave NA ≈ k1 × wavelength ÷ resolution |
| 36 | Exercise 5 | Formulas used B2 and B3, but step 1 never said which cell holds what, so they would break | Gave an explicit cell layout (B1 to B8) and formulas for good dies and cost |
| 36 | Exercise 7 | PFLOPS must be turned into trillions of operations | Added "multiply PFLOPS by 1,000" |
| 36 | Exercise 10 | 100 exaFLOPS versus PFLOPS per chip | Added 100 EF = 100,000 PFLOPS |
| 36 | Answer 4 | "CO2 laser" unexplained | Glossed carbon dioxide |
| 37 | Llama 3.1 6ND example | 37,908 × 10^21 ≈ 3.8 × 10^25 skipped the exponent arithmetic | Explained adding exponents and moving the decimal |
| 37 | Llama time estimate | "1,630 hours" came from nowhere | Showed seconds ÷ 3,600 |
| 37 | Tensor parallelism | "Megatron-LM" unexplained | Glossed |
| 37 | Expert parallelism | "Kimi K3" and "shared experts" unexplained here | Glossed Moonshot AI and shared experts, with a pointer to Chapter 17 |
| 37 | 3D/4D/5D parallelism | "Product of the degrees": degree never defined | Glossed |
| 37 | Network bottleneck example | "400 × 10^12 ÷ 50 × 10^9" is ambiguous, and why N cancels was skipped | Added parentheses and the 8,000 step |
| 37 | Checkpoint table | "Half an interval + restart" was not explained | Added why a failure loses half an interval on average |
| 37 | Batching example | KV-cache size: the 2 and the step to 0.34 GB per user were skipped | Explained the 2 and showed × 2,048 tokens |
| 37 | Table 37.9 | No column was derived; the cost formula appears only later | Worked the one-user row and pointed to the cost formula |
| 37 | Table 37.10 | "GDDR7" unexplained | Glossed |
| 37 | Energy worked example | LED (8 chapters) never defined | New callout: LED (light-emitting diode) |
| 37 | Exercise 3 | Minimum GPUs needs rounding up | Added `=ROUNDUP()` |
| 37 | Exercise 4, steps 7 and 8 | No usable N and D for 10^27; step 8 did not say to change B4, B5 and B18 or how to get megawatts | Said to type 1e27 in B3, which cells to change and where to read the megawatts |
| 37 | Exercise 5 | Placeholder formula would be typed literally; step 2 had no answer in the grid (128 microbatches gives 10.5 percent) | Gave the cell formula with $ references; said to add larger columns (the answer is 136) |
| 37 | Exercise 6 | No formula for time between failures or goodput; placeholder names in Young's formula | Gave all three formulas with cell references |
| 37 | Exercise 7 | Formulas used placeholder names | Gave a B1 to B8 layout and real formulas |
| 37 | Exercise 9 | No FP8 peak or formula to recompute the FLOP | Gave both |
| 37 | Exercise 10 | No formulas for yearly spending or joules to GWh | Gave both (1 GWh = 3.6 trillion joules) |

Fixes per chapter, by type:

| Chapter | Undefined terms | Beginner jumps | Exercises | Plainly wrong | Total | New definition callouts |
|---|---|---|---|---|---|---|
| 34 | 34 | 6 | 5 | 1 | 46 | 12 |
| 35 | 26 | 0 | 5 | 1 | 32 | 9, plus 1 label fix |
| 36 | 15 | 3 | 5 | 0 | 23 | 1 |
| 37 | 6 | 6 | 7 | 0 | 19 | 1 |

(The undefined-terms column counts individual terms, so one table row can count as several. Ch 36 Exercise 5's broken cell references and Ch 37 Exercise 5's unanswerable step are counted as exercise fixes.)

New definition callouts, each added to its chapter's Key terms list: NVIDIA; GB200 and GB300; TFLOPS and PFLOPS (PF); EF and ZF; PB; TSMC; AMD; AMD Instinct (MI300X, MI355X, MI455X); LPDDR5X; CES; MXFP8; AWS (Ch 34). SK hynix; ASML; GTC; HBM2, HBM2e and HBM3; LPX; Rubin CPX; MI500; MTIA; SB Energy, plus "(WSE)" added to the Wafer-scale engine label (Ch 35). SMIC (Ch 36). LED (Ch 37).

## Noticed but not changed

- **Duplicate organization definitions.** While this pass ran, other passes added NVIDIA, AMD, AWS, GB200 and TSMC callouts to chapters 3, 19, 30, 38, 43 and others. The brief's rule ("in the first of your chapters that uses it") led to short re-definitions in Ch 34 too. They agree in substance with the others, and the style guide allows re-defining a term that is central to a chapter. Whoever builds the glossary may want to keep just one entry per organization.
- **ACM (Ch 35) and CSET (Ch 36)** appear in these chapters only inside the Going deeper reading lists. A definition callout there would break the list, so each was glossed in place instead (ACM spelled out and described; CSET already spelled out). CSET now has callouts in Chapters 59 and 62.
- **Remaining acronyms.py hits.** The script still reports RISC (Ch 35) and CS (Ch 35), but both are false alarms. "RISC" is the first half of RISC-V, which Ch 35 defines; the script's tokenizer splits on the hyphen. "CS" here is Cerebras's CS-4 system, glossed in place. All other remaining hits for chapters 34 to 37 are used in only one or two chapters and are glossed at first use.
- **No sourced 2025–26 facts were changed.** The only number corrected is the Ch 35 gigawatt total, which is arithmetic over that chapter's own Table 35.10. My recount: 8 (the reshaped OpenAI–NVIDIA plan) + 6 + 10 + 1 + 1 + 0.75 + 6 + 3.5 + 5 + 2 ≈ 43 GW, or about 45 GW counting Cerebras's option or the original 10 GW NVIDIA plan.

## Verdict per chapter

**Chapter 34 (servers, racks, networks).** The ramp works. The chapter climbs its eight-rung ladder one rung at a time, checks every headline number with the reader's own arithmetic, and defines its networking vocabulary carefully. Friction came from the industry around the machine rather than the machine itself. NVIDIA, AMD, TSMC, AWS, the GB200/GB300 and MI-series product names, and the PF/EF/PB shorthand were all used from the first page with no definition. Electrical terms from Chapter 39 (DC, AC, capacitors, IT load) also arrived early. Figure 34.10 got ahead of the text by naming four parallelism strategies that only Chapter 37 explains. With the new callouts and the bridging paragraph, every term is now defined at or before first use, or glossed with a pointer. The exercises needed spreadsheet mechanics (formulas, unit conversions, a criterion for "affordable"), and now have them.

**Chapter 35 (the chip industry).** The ramp works, and this is the easiest of the four to read: it is mostly a map of companies with a few worked examples. The SRAM-versus-HBM example is especially clear. The main gaps were product and company names used before their definitions or never defined: SK hynix, ASML, GTC, MTIA, MI500, the older HBM generations, and the LPU/LPX pair (used some 240 lines before LPU is defined). The chapter's one arithmetic error was the gigawatt total, which had not been updated after later deals were added to Table 35.10. Five exercises named a calculation without giving a method; each now gives a formula. Every term is now defined.

**Chapter 36 (how chips are made).** The ramp works well. Sand to wafer to fab loop to lithography to yield to packaging to geopolitics is a natural order, and each step is defined as it arrives. Most of the friction was mathematical notation the reader has not used since school: π r², exponents written with ^, the e^x yield formula with its mm² to cm² step, λ in a table header, and rearranging the Rayleigh formula. A few diagram labels (anneal, CMP, Licensed IP, TEL, JSR, TOK) also never appeared in the text. One genuine contradiction was smoothed over: Huawei's data-center "NPUs" against Chapter 35's phone-sized NPU definition. Exercise 5 would have failed as written, because its formulas referred to cells the setup never assigned; it now has a full cell layout. Every term is now defined.

**Chapter 37 (training and serving at scale).** This is the steepest of the four, and it should be: it is where Part VI's hardware meets Part IV's models. The difficulty is in chained arithmetic rather than vocabulary. Its definitions were already nearly complete; the only undefined names were Megatron-LM, Moonshot, "degree" and LED. The worked examples are correct (I re-checked the 6ND table, every row of the ring all-reduce, the bubble formula, the checkpoint table and every row of the batching table), but several skipped a step a beginner needs: exponent arithmetic, seconds to hours, the KV-cache size, and how Table 37.9's columns are computed. Those steps are now shown. The exercises were the weakest part, because four used placeholder names that a non-programmer would type literally, and Exercise 5 asked for an answer the given grid could not produce. All now use real cell references, and Exercise 5 tells the reader how to find the answer (136 microbatches). With these fixes, a reader who did Chapters 5, 32 and 33 can follow the whole chapter with a spreadsheet.
