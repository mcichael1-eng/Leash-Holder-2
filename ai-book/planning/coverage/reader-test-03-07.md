# Reader test: chapters 3, 4, 6 and 7

Tested by reading chapters 3, 4, 6 and 7 in order, in full, as the intended reader: almost no computer-science background, a daily chatbot user for a year, who has read the earlier chapters. Every place that reader would get lost was fixed with a small edit: a definition callout, a short gloss, a bridging sentence, a missing arithmetic step, or a clearer exercise instruction. Nothing was rewritten for style and no content was cut. Before treating a term as undefined I checked GLOSSARY.md and the earlier chapters (Chapters 1, 2 and 5). Every entry for these chapters in `acronyms-by-chapter.json` was worked through: organizations and products used in three or more chapters got a definition callout in the first of these chapters that uses them, and every other entry got at least a gloss at its first use.

I recomputed every worked example and exercise answer in the four chapters (UTF-8 byte values, image, audio and video sizes, compression ratios, binary search and sorting counts, packet counts, speed-of-light delays, API prices, energy per message, softmax at three temperatures, the Bayes tables, the standard deviations including the billionaire case, the gradient-descent and training-loop tables, KL divergence, perplexities, the perceptron runs, 6 × N × D for GPT-3, the Moore's law and METR doubling times). All were correct; the only error found was a cross-reference.

After editing, every edited file passed `validate.py` (all mermaid diagrams valid: 7, 7, 6 and 13) and `check.py` (ch03, ch04, ch06 and ch07 all `[OK ]`).

## Findings and fixes

| Chapter | Where | Problem a beginner would hit | Fix applied |
|---|---|---|---|
| 3 | Unicode, code points | "U+0041" is said to be 65 with no way to read hexadecimal | Added how base 16 works: 41 means 4 × 16 + 1 = 65, and A to F stand for 10 to 15 |
| 3 | Audio, "Why 44,100?" | "Frequency" used with no meaning | Added one sentence: waves per second, and higher frequency sounds higher-pitched |
| 3 | Audio worked example | The step from 128 kilobits to 16,000 bytes per second was skipped | Added "(128,000 bits ÷ 8)" |
| 3 | Audio worked example | MP3 used with no definition (3 chapters) | New definition callout: MP3 |
| 3 | Video, streaming | The step from 5 megabits to 0.6 MB per second was skipped | Added "(5 ÷ 8, since a byte is 8 bits)" |
| 3 | Files and formats | JPEG used with no definition (5 chapters) | New definition callout: JPEG |
| 3 | Files and formats | PNG and ZIP used before compression is explained | Short gloss for each in the sentence |
| 3 | Compression table | "12 MP" abbreviation | Added "(megapixel)" |
| 3 | Programs, "Software 2.0" | "Optimizer" used three chapters before it is taught | Glossed, with a pointer to Chapter 6 |
| 3 | Algorithms, merge sort | "log2(n)" used with no explanation | Explained as "how many times you can halve n", about 20 for a million, as in binary search |
| 3 | AlphaEvolve frontier box | Matrices, complex numbers, "scalar multiplications" and "the Strassen-based method" all unexplained | Four short glosses (matrices point to Chapter 5) |
| 3 | Compilers and CUDA | NVIDIA used with no definition anywhere in the book (43 chapters; Chapter 3 is its first use in this range, spelled "Nvidia", which the acronym scan missed) | New definition callout: NVIDIA |
| 3 | Why Python runs AI | TIOBE index, GitHub and "repositories" used before they are explained | Glossed all three |
| 3 | Bugs, Harvard Mark II | "Relay" unexplained | Glossed as an electrically operated switch |
| 3 | Watch out on AI-written code | METR unexplained (defined only in Chapter 57) | Glossed, with a pointer to Chapter 57 |
| 3 | Operating systems | TOP500 (3 chapters) has no glossary entry | New definition callout: TOP500 |
| 3 | Project Glasswing frontier box | "Vulnerabilities", OpenBSD, FFmpeg and the Linux Foundation unexplained | Glossed each |
| 3 | Same box | AWS used with no definition (22 chapters; first use in the book) | New definition callout: AWS (Amazon Web Services), pointing to Chapter 4 |
| 3 | Licenses | GPL abbreviation | Added the full name |
| 3 | Open weights | Mistral unexplained | Glossed as a French AI company |
| 3 | Figure 3.12 | AI2 unexplained | Expanded to the Allen Institute for AI |
| 3 | CSV | "NY" | Glossed |
| 3 | Exercise 2, step 3 | Phones often show file size in KB while step 2 gives MB, so the ratio comes out 1,000 times wrong | Added the unit check |
| 3 | Exercise 3, step 3 | XML never explained | Added a one-clause gloss |
| 3 | Exercise 4, step 4 | The `**` operator is never explained | Explained as "to the power of" |
| 3 | Exercise 8, step 2 | Drawing a letter needs row/column indexing and slices, which only step 3 asks about | Explained `img[row, column]` and `2:6`, with a worked yellow "L" |
| 3 | Exercise 9, step 2 | Windows 11 hides "Send to" | Added "Show more options" |
| 3 | Exercise 11 | README and model card unexplained | Glossed both |
| 3 | Areas of opportunity | QA and NGOs | Glossed both |
| 3 | Going deeper | "CS" in CS50x | Glossed |
| 4 | Networks | International Telecommunication Union unexplained | Glossed as the UN telecom agency |
| 4 | Packets | QUIC "used by HTTP/3" before HTTP is taught | Added a pointer to the HTTP section |
| 4 | Speed of light | 200,000 km per second to 5 microseconds per km skipped | Added "1 ÷ 200,000 of a second" |
| 4 | IP addresses | Why four numbers from 0 to 255 make 32 bits | Added "(four bytes of 8 bits each)" |
| 4 | DNS, Figure 4.4 | The diagram's "registry" and "name server" are not in the text | Named and glossed both in the paragraph |
| 4 | HTTP requests | "Login token" collides with the AI meaning of token from Chapter 3 | Clarified that it is unrelated |
| 4 | Status code table | "API key" and "rate limit" used 140 lines before they are explained | Added a one-sentence forward pointer |
| 4 | Cloudflare frontier box | "AI crawlers" undefined | Glossed |
| 4 | Data centers | "IT power" undefined (defined in Chapter 42) | Glossed |
| 4 | Try it, Epoch data center hub | Dividing megawatts by 1.2 kilowatts without converting units | Added "multiply the megawatts by 1,000" |
| 4 | Regions | "Uplift" | Glossed as surcharge |
| 4 | Renting GPUs | "GPU-hour" and RunPod undefined | Glossed both |
| 4 | Latency worked example | 100 Mbps = 100,000,000 bits per second not stated | Added |
| 4 | Step 10, tools | "Context" undefined until Chapter 7 | Glossed |
| 4 | Arithmetic worked example | "The rule of thumb from Chapter 5": Chapter 5 comes after Chapter 4; the rule was given in Chapter 1 | Corrected to "from Chapter 1 (Chapter 5 shows where it comes from)" |
| 4 | Same | The step from `5.2 × 10^14` seconds to "16 million years" was skipped | Added "a year has about 31.5 million seconds" |
| 4 | Energy | LED | Expanded |
| 4 | Fairwater frontier box | "AI WAN", "pretraining run" and "Stargate" unexplained | Glossed each |
| 4 | Exercise 4, step 3 | No method for either calculation | Gave both conversions, matching the worked example |
| 4 | Areas of opportunity | NGOs | Glossed |
| 4 | Going deeper | MDN | Expanded to Mozilla Developer Network |
| 6 | Exponential growth in AI | "2 multiplied by itself 2.3 times": a fractional power is never explained | Added how to compute `2^2.3` and a sanity check (between 4 and 8) |
| 6 | Exponential decay | 280-fold in two years to "more than ten times per year" skipped | Added 17 × 17 ≈ 290 |
| 6 | Softmax Try it | `$B$1:$B$3` dollar signs unexplained | Glossed |
| 6 | Bayes' rule formula | 0.0891 appears with no source | Showed 0.9 × 0.01 and 0.09 × 0.99 |
| 6 | Densities aside | "ROC curve" unexplained | Glossed, with a pointer to Chapter 9 |
| 6 | Rolling down a parabola | The slope 2 × (x − 3) is not justified; the derivative table only covers x squared | Derived it in one sentence with the chain rule |
| 6 | Training the Chapter 5 line | The four data points are not restated, so the errors and slope sums cannot be checked | Restated hours, scores and the sign of the error |
| 6 | Muon frontier box | Moonshot AI unexplained | Glossed |
| 6 | Exercise 5, step 5 | "Find the prevalence" had no method | Gave cells and formulas (the answer is 5%) |
| 6 | Exercise 8, step 4 | The nudged LN formula was missing, and the x = 0 row errors | Added both |
| 6 | Exercise 8, step 5 | The nudged chain-rule formula was missing and easy to mistype as `(3*A2+0.001)^2` | Gave `=(3*(A2+0.001))^2` |
| 6 | Exercise 9, step 5 | The sheet only had 30 rows, and the cells for the new formulas were not given | Specified cells and filling to row 202 |
| 7 | Era 1 | ENIAC (3 chapters) has no definition | New definition callout: ENIAC |
| 7 | Era 1 | Bell Labs | Glossed |
| 7 | Figure 7.2 | "1958: Lisp" in the timeline, and later "Lisp machines", never explained in the text | Added a 1958 bullet on Lisp, and tied Lisp machines back to it |
| 7 | Era 2 | IBM (8 chapters) and SRI (3 chapters) | New definition callouts: IBM; SRI (Stanford Research Institute) |
| 7 | Perceptron's limits | ALPAC (3 chapters) | New definition callout: ALPAC |
| 7 | Same sentence | It said the committee concluded "that funding dried up" | Reworded: "and funding for it dried up" |
| 7 | Expert systems | MYCIN and XCON (3 chapters each) | New definition callouts: MYCIN, XCON |
| 7 | Same | Digital Equipment Corporation unexplained | Glossed |
| 7 | Backpropagation | *Nature* | Glossed |
| 7 | Web as data | "Hello world" | Glossed |
| 7 | Neural networks survive | Figure 7.6's "Stanley" is not in the text; Waymo unexplained | Added both |
| 7 | Same | DARPA (5 chapters) | New definition callout: DARPA |
| 7 | Table 7.4 | CICERO (3 chapters); the game Diplomacy unexplained | New definition callout: CICERO |
| 7 | Proteins, pictures and code | Figure 7.8's "CLIP" is not in the text | Added one clause on CLIP |
| 7 | Same | DALL·E (5 chapters) | New definition callout: DALL·E |
| 7 | 2023 | Bard | Glossed |
| 7 | MCP definition | USB | Glossed |
| 7 | Compute race | "Letter of intent", Broadcom and Trainium2 unexplained | Glossed each |
| 7 | Same | AMD (22 chapters) | New definition callout: AMD |
| 7 | Agents | "Terminal" | Glossed |
| 7 | GPT-5 section | METR time horizons used 60 lines before their definition | Added a short gloss and pointer |
| 7 | Reality checks | "SB 53" (SB appears in 13 chapters) | Glossed as Senate Bill, and how states number bills |
| 7 | Table 7.5 and Figure 7.11 | Claude Cowork, Anthropic's constitution and Gemini Omni are in the timeline but nowhere in the text | Added a short paragraph with pointers to Chapters 20 and 22 (facts from the research notes and those chapters) |
| 7 | GPT-6 Astra | AGI used about 145 lines before its definition | Added a gloss and pointer |
| 7 | Open weights | Grok | Glossed |
| 7 | Benchmarks | ARC Prize and Artificial Analysis | Glossed both |
| 7 | Chips | CES (7 chapters) | New definition callout: CES |
| 7 | Gigawatt campuses | "Small modular reactor" and Tennessee Valley Authority | Glossed both |
| 7 | Rules in 2026 | "Preempt" | Glossed |
| 7 | Pattern 2, Figure 7.13 | "Common Crawl" in the diagram is not in the text | Added to the data sentence (GPT-3's training text) |
| 7 | Is this time different? | "Capital projects", FactSet and the dot-com crash | Glossed each |
| 7 | Exercise 6, step 2 | Which cell to use, and what `^(1/(A3-A2))` does | Explained both |
| 7 | Exercise 7, steps 1 and 3 | No cell layout; "extend the trend" had no method | Gave the layout, and October 2027 as month 55 with `=2^FORECAST(55, C2:C9, A2:A9)` |
| 7 | Areas of opportunity | "Family offices" | Glossed |

Fixes per chapter, by type:

| Chapter | New definition callouts | Glosses for undefined terms | Beginner jumps (steps, forward references, diagram words) | Exercises and Try-its | Plainly wrong | Total |
|---|---|---|---|---|---|---|
| 3 | 5 | 15 | 4 | 6 | 0 | 30 |
| 4 | 0 | 12 | 6 | 2 | 1 | 21 |
| 6 | 0 | 2 | 5 | 5 | 0 | 12 |
| 7 | 11 | 15 | 7 | 2 | 1 | 36 |
| All | 16 | 44 | 22 | 15 | 2 | 99 |

The 16 new definitions are MP3, JPEG, NVIDIA, TOP500 and AWS (Amazon Web Services) in Chapter 3, and ENIAC, IBM, SRI, ALPAC, MYCIN, XCON, DARPA, CICERO, DALL·E, AMD and CES in Chapter 7. Each was added to its chapter's Key terms list in order of appearance.

Acronym-list entries that needed no new text: UTF (UTF-8 is defined in Chapter 3), HEVC and AV1 (named as video codecs inside the Codec definition), ADD (named as an assembly instruction in context), ARPANET and QUIC (glossed where used), GET and POST (explained inline), and AWS in Chapters 4 and 7 (spelled out in Chapter 4 and defined in Chapter 3).

## Noticed but not changed

- Chapter 3 spells the company "Nvidia" while the rest of the book uses "NVIDIA". I left the spelling alone (style), but the new definition uses "NVIDIA" to match the glossary.
- Another agent was editing Chapters 3 and 7 during this pass. In Chapter 7 it changed the OpenAI row of Table 7.5, the date of the small-reactor permit and the Astra timeline label. My edits went onto the current text, and both chapters still validate and check clean.
- No sourced 2025–2026 facts were changed. Glosses added to 2026 passages only name what something is, such as ARC Prize being a nonprofit or Trainium2 being Amazon's chip.
- Chapter 6, Exercise 1: the linear column starts at 0, which a log-scale axis cannot show. Spreadsheets simply drop the point, so I left it.
- The "At the frontier" boxes still name a few products briefly, such as Kimi K2, Fairwater and Vera Rubin. Each is identified by its owner in the same sentence, so I left them.

## Verdicts

**Chapter 3 (Software, Code and Data).** The ramp works well. The chapter climbs from one byte to text, images, audio, video, files, compression, programs, Python, operating systems, open source, Git and data. Each step has a worked example with real numbers, and every number checks out. The friction was small and local. Hexadecimal and log2 appeared as notation with no explanation. Two unit conversions were silent. Five widely used names (NVIDIA, AWS, JPEG, MP3, TOP500) had no definition anywhere in the book, and this chapter is the right place for them. Exercise 8 asked the reader to draw with array indexing before explaining it. With the fixes, every term is defined or glossed where it first appears, and a non-programmer can do all eleven exercises.

**Chapter 4 (The Internet and the Cloud).** This is the best-paced of the four chapters. The twelve-step journey at the end reuses every idea in the chapter, so the chapter teaches and then consolidates. Its 53 definitions cover the core vocabulary. The problems were forward references inside the chapter: HTTP/3 before HTTP, API keys and rate limits in the status-code table, and "context" before Chapter 7. A few silent unit conversions (megabits, megawatts, seconds to years) needed showing. One cross-reference was wrong: it sent the reader to Chapter 5, which comes later, for a rule taught in Chapter 1. Every term is now defined or glossed.

**Chapter 6 (Probability, Statistics and Learning by Slopes).** This is the steepest chapter in Part I. It is also the most carefully scaffolded: every formula is worked by hand with small numbers before it is named. I recomputed every table, including softmax at three temperatures, both Bayes trees, the standard deviation before and after the billionaire, both gradient-descent tables, the training loop and the KL divergence. All are correct, including Exercise 10's claim that a learning rate of 0.12 fails: the largest stable rate for that data is about 0.1198. The ramp works. The friction was a handful of skipped steps: a fractional power, 280-fold over two years, where 0.0891 comes from, the slope of (x − 3) squared, and Chapter 5's data not being restated. Spreadsheet instructions in three exercises were incomplete, and that remains the biggest barrier for this reader. With the fixes, every term was already defined (79 definitions) and every exercise can be done as written.

**Chapter 7 (A History of AI).** As narrative, the difficulty ramp is gentle. The technical worked examples are the perceptron, XOR, chess branching, 6 × N × D, Moore's law and METR's doubling time. All are correct and all reuse Chapters 5 and 6. The chapter's problem was names. A history chapter names dozens of organizations and products, and eleven that recur across the book had no definition anywhere: ENIAC, IBM, SRI, ALPAC, MYCIN, XCON, DARPA, CICERO, DALL·E, AMD and CES. Five timeline figures named things the text never mentioned: Lisp, Stanley, CLIP, Common Crawl, and the January and May 2026 items. Two terms (time horizon and AGI) were used long before their definitions. All of these are now fixed, and every term in the chapter is defined or glossed. The 2026 section remains dense with model names by design. The chapter itself tells the reader to learn the pattern, not the version numbers.
