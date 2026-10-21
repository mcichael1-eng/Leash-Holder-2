# Reader test: the beginner's walk-through

Tested by reading chapters 1, 2, 5, 12, 15, 18, 23, 33, 39 and 44 in order, in full, as the intended reader: almost no computer-science background, a daily chatbot user for a year. Every place that reader would get lost was fixed with a small edit: a definition callout, a bridging sentence, a missing arithmetic step, or a clearer exercise instruction. Nothing was rewritten for style and no content was cut. Before each fix I checked earlier chapters for an existing definition; a term defined in an earlier chapter was not counted as a problem.

After editing, every edited file passed `validate.py` (all mermaid diagrams valid) and `check.py` (all ten chapters `[OK]`).

## Findings and fixes

| Chapter | Where | Problem a beginner would hit | Fix applied |
|---|---|---|---|
| 1 | "How much math is in one answer?" | "2 operations for every parameter the model uses" did not say what the 2 operations are, or why it says "uses" | Added "(one multiplication and one addition)" and one sentence saying some large models switch on only part of their parameters (Chapter 17) |
| 1 | Same section, 500-token bullet | First use of 10^14 notation, with no explanation | Added "(a 1 followed by 14 zeros; Chapter 2 explains this notation)" |
| 1 | Same section, "3.2 million years" | The step from seconds to years was skipped | Added that a year has about 31.5 million seconds, so 10^14 ÷ 31.5 million ≈ 3.2 million |
| 1 | "Way 1: Rules" | "Expert systems" used with no definition; Chapter 7 defines it later | New definition callout: Expert system (added to Key terms) |
| 1 | Figure 1.4 and the symbolic-AI Watch out | "Knowledge graphs" used and never defined anywhere before Part VIII | New definition callout: Knowledge graph (added to Key terms) |
| 1 | AI stack, gigawatt worked example | Gigawatts, gigawatt-hours and terawatt-hours mixed with no explanation of power versus energy | Added a bridging sentence: watts are like speed, watt-hours like distance; 1 TWh = 1,000 GWh |
| 1 | Figure 1.7 (sequence diagram) | "Encrypted", "packets" and "provider gateway" in the diagram are not defined until Chapter 4 | Added one paragraph after the caption explaining all three in plain words |
| 1 | Exercise 4, step 4 | "Retrain" did not say you must first remove the old images, so the sabotage would not work | Step now says to delete the images (or start a new project), re-record, and click Train again |
| 1 | Exercise 7, step 3 | Did not say how to combine tokens, 2 operations and 100 billion parameters | Added "(multiply your token count by 2 × 100 billion)" |
| 2 | Scientific notation, Llama 3.1 405B | "405B" not explained at first use | Added "the 405B means 405 billion parameters" |
| 2 | Logic gates | "CMOS" named with no explanation | Added a one-clause gloss (two opposite kinds of transistor; current flows almost only while switching) |
| 2 | Cores, CPU speed estimate | "Vector units" never defined | Glossed as circuits that apply one instruction to several numbers at once |
| 2 | Memory hierarchy table | HBM appears in the table about 60 lines before it is defined | Added a sentence: HBM is a fast form of DRAM for AI chips, explained later in the chapter |
| 2 | "Moving data costs more than math" | "32-bit floating-point multiplication" appears 100 lines before floating point is defined | Added a short gloss and a pointer to where floating point is explained |
| 2 | Same section | "Price-performance" not explained | Glossed as "how much calculation a dollar of chip buys" |
| 2 | Why your chatbot types at the speed it does | The step from 10^13 versus 10^15 to "99% idle" was skipped | Added "and 10^13 is only 1% of 10^15" |
| 2 | Power and heat, frontier box | "H100-equivalents" undefined | Glossed as total compute expressed as a number of H100 chips |
| 2 | FLOP/s comparison table | "TOP500 list" unexplained | Glossed as a twice-yearly ranking of the fastest supercomputers |
| 2 | Moore's law frontier box | "TSMC" never introduced | Glossed as the contract factory that makes most advanced AI chips |
| 2 | Exercise 8 (Colab) | Did not say where to change `n`; the `@` symbol in the code was not explained | Pointed to the line `n = 4000` and explained `@` |
| 2 | Exercise 9 (spreadsheet) | A non-programmer would type "70 × 10^9" literally | Added: type 70E9 and use * for × |
| 2 | Exercise 10 (spreadsheet) | `=LOG(count/2300, 2)` uses a placeholder a beginner would type literally | Said to replace count with the cell reference, with an example `=LOG(B3/2300, 2)` |
| 5 | "Your chatbot is one enormous function" | "A probability of 0.92" comes before probability is taught (Chapter 6) | Added "(a 92% chance; Chapter 6 covers probability properly)" |
| 5 | Cosine similarity, normalizing | "[3, 4] becomes [0.6, 0.8]" skipped the divide-by-length step | Showed [3 ÷ 5, 4 ÷ 5] |
| 5 | Cosine similarity frontier box | "Grows with the square" not made concrete; "contexts" not defined until Chapter 7 | Added "double the length, four times the comparisons" and a one-line gloss of context, with chapter pointers |
| 5 | Matrix multiplication frontier box | "Matrices of complex numbers" unexplained | Added a one-clause gloss |
| 5 | Tensor table | "Learning rate" used before Chapter 6 defines it | Added "(a training setting, Chapter 6)" |
| 5 | FP8 definition | "NVIDIA's Hopper chips" unexplained | Added "(the H100 generation)" |
| 5 | "Why AI tolerates rough numbers" | "The optimizer's memory" used before optimizers exist in the book | Glossed, with a pointer to Chapter 6 |
| 5 | Exercise 2, step 1 | "Put the genre names in a row above" is impossible: the data starts in row 1 | Labels now go in row 8, so the later formulas still line up |
| 5 | Exercise 3, step 3 | The "Superfan" checks gave no formulas; a beginner could not compute them | Gave the exact cells and formulas for both checks |
| 5 | Exercise 6, step 3 | `result_range` and `word_range` placeholders would be typed literally | Explained them with example ranges |
| 5 | Exercise 7, step 5 | "A second layer" had no cell locations or formula | Gave cells and the `MMULT` formula |
| 5 | Exercise 9, step 4 | The number 86,400 was unexplained | Added "(the number of seconds in a day)" |
| 12 | The artificial neuron, sigmoid | e is used with no reminder of what it is, and there was no way to compute 2.718^(−0.3) | Named Euler's number (Chapter 6) and gave the spreadsheet formula |
| 12 | Activation gallery table | "RNNs" used before Chapter 14 defines them | Changed to "recurrent networks (RNNs, Chapter 14)" |
| 12 | Cross-entropy | −ln given with no way to compute it | Added the calculator ln key and `=-LN(0.9)` |
| 12 | Gradient descent, one knob | The slope "2 × (w − 3)" was stated with no justification | Added a nudge check showing the slope is about −6 at w = 0 |
| 12 | Backpropagation rules table | The slope of ½(ŷ − y)² was not connected to anything | Added that the ½ cancels the 2 from squaring, as in the one-knob example |
| 12 | Exercise 6 | "dL/ds" notation never introduced | Added how to read it |
| 12 | Exercise 7, step 3 | Did not say to reset the previous nudge, so later slopes would be wrong | Added "put the previous one back first" |
| 15 | RoPE toy example | cos and sin used with no explanation for someone who never took trigonometry | Added a sentence on what they give, and a spreadsheet formula |
| 15 | Scaled dot-product attention definition | "K-transposed" undefined | Glossed "transposed" inside the definition |
| 15 | Frontier box after GQA | "Sliding-window" and "linear-attention" used before their section | Added a pointer to "Making attention cheaper" |
| 15 | Residual stream, parameter count | "d²" notation, and what d stands for, not stated | Added "d is the model dimension and d² means d × d" |
| 15 | FlashAttention | "Compute-bound workloads" not defined until Chapter 23 | Added a one-clause gloss |
| 15 | Sparse attention definition | "Top-k" not defined until Chapters 17 and 18 | Glossed as the k highest-scoring |
| 18 | Hallucination worked example | "Expected score" used with no reminder of what it means | Added a sentence linking it to Chapter 6's expected value |
| 18 | Exercise 3, step 3 | "Until no pairs are left" is ambiguous | Now says "until every word in the corpus has become a single token" |
| 18 | Exercise 4, step 5 | The top-p column had no formulas; it is the hardest spreadsheet step in the chapter | Gave the three formulas and the cells (checked: reproduces the chapter's 66.5/24.5/9.0) |
| 18 | Exercise 11, step 2 | The cost calculation had no formula | Gave the input and output cost formulas |
| 23 | KV-cache pricing example | "$0.10/$0.50" did not say which number is input and which is output | Added "(input/output)" |
| 23 | Speculative decoding worked example | The formula (1 − 0.8^5) ÷ (1 − 0.8) came out of nowhere | Added the term-by-term sum it stands for (1 + 0.8 + 0.64 + 0.512 + 0.41 ≈ 3.36) |
| 23 | Energy per token | The step from kilowatts to joules per token, and from joules to watt-hours, was skipped | Added both steps |
| 23 | Exercise 4 | No formulas for the cost with and without caching | Spelled out both cost rules |
| 33 | Tiling worked example | 8,192³ notation | Added "8,192 × 8,192 × 8,192" |
| 33 | Arithmetic intensity, job 4 | 2n³ ÷ 6n² = n ÷ 3 needs algebra the reader has never done | Added the cancel step in words |
| 33 | Newer chips | "A batch of about 456 users" with no division shown | Showed 1,823 ÷ 4 and why |
| 33 | Exercise 6 | A formula written with × and ÷ would fail in a spreadsheet | Added a spreadsheet version with * and / and cell references |
| 39 | Figure 39.4 caption | "About 83 kWh" not derived from PUE 1.2 | Showed 100 ÷ 1.2 ≈ 83 |
| 39 | Bill, capacity charges | "$329 per megawatt-day" is an unexplained unit (capacity markets are only defined in Chapter 41) | Glossed how a capacity price is charged |
| 39 | Try it (50 MW site) | The switch from 6 cents per kWh to $60 per MWh was silent | Showed the conversion |
| 44 | Data, 6ND puzzle | How D follows from N × D was skipped | Added "divide 1.7 × 10^26 by each N to get D" |
| 44 | Figure 44.6 | "A third of every day" did not say the day has 1,440 minutes | Rewrote the line as 470 of the day's 1,440 minutes |
| 44 | Fleet size | 86,400 unexplained | Added "seconds in a day" |

Fixes per chapter: 1: 9, 2: 13, 5: 12, 12: 7, 15: 6, 18: 4, 23: 4, 33: 4, 39: 3, 44: 3 (65 in total). Two new definitions were added (Expert system and Knowledge graph, both in Chapter 1). Both were added to that chapter's Key terms list.

## Noticed but not changed

These are outside a surgical reader-test fix:

- Optional "At the frontier" boxes often use names that are never introduced, such as Kyber racks, Groq LPX and "shared experts". They are optional asides, so they were left alone, but this is where a beginner will most often feel briefly lost.
- Table 44.5 lists "SpaceXSI (formerly xAI)" among the training players. The name is worth a fact-check by whoever owns Chapter 44.
- Another agent edited Chapter 18 during this pass. My edits were applied to the current text, and the chapter still validates and checks clean.

## Verdict: does the difficulty ramp work?

Yes, with a gentle slope at the start and a steep but survivable climb in Parts III and VI. Chapter 1 is a true on-ramp. Chapters 2 and 5 carry the load well: every operation is done by hand with small numbers, so by Chapter 12 the reader can follow a full forward and backward pass with a pencil. Chapter 15 (the Transformer) is the steepest step in the book. RoPE's trigonometry, transposed matrices and KV-cache arithmetic all arrive at once. The worked three-token attention example carries the reader through, and the small glosses added here remove the trigonometry and notation traps. Chapters 18, 23, 33, 39 and 44 are dense with numbers and acronyms, but they re-define what they need and cross-reference reliably. A reader who did Part I can follow them, although Chapter 33 really does depend on Chapter 32's SM and warp.

The friction this pass found fell into four kinds:

1. **Forward references inside Part I.** Terms were used one to six chapters before they are taught: units and expert systems in Chapter 1, floating point and HBM in Chapter 2, learning rate, optimizer and context in Chapter 5.
2. **Spreadsheet mechanics in exercises.** Placeholders, the × symbol and missing cell references are the biggest barrier for a non-programmer, and the most common fix in this pass.
3. **Compressed algebra.** Steps like n³ ÷ n² or the speculative-decoding series were skipped.
4. **Exponent and superscript notation** used before the reader is fluent in it.

None of these was structural. With the fixes in place, the ramp works for the intended reader.
