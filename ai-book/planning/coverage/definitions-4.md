# Repeated definitions, keys s to z and digits (reconciliation round 4)

Date: October 23, 2026. Input: `defgroups.py` run on the whole book (3,340 distinct glossary keys, 711 defined more than once). This report covers only keys starting with s to z, a digit or a symbol: **161 groups, 414 callouts**. Only two keys start with a digit ("6nd rule" and "800 v dc distribution"). No key starts with a symbol, because quotation marks are stripped from the key (so "The model eats your feature" and "Up to" deal are t and u keys).

Merge rule used by the glossary build: the label with any text in parentheses removed and lowercased is the key. The body from the first chapter in book order wins.

## Counts

| Class | Groups | What was done |
|---|---|---|
| HOMONYM | 11 | The odd meaning got a new label that differs outside the parentheses. That chapter's Key terms list was updated too (Appendix F has no Key terms list). |
| CONTRADICTION | 2 | Brought into line with the best-supported version (a date and a fact). |
| OK | 148 | Same meaning, compatible wording. In 7 of these groups (organizations and products) the core sentence was rewritten to match across chapters, so the glossary entry reads well. The other 141 were left as they are. |
| Total | 161 | 33 definition lines and 11 Key terms entries edited, in 19 chapters and Appendix F |

After the edits, a second `defgroups.py` run (3,349 keys, 706 repeated) finds no s to z homonyms. Six keys no longer repeat: state, tiling, trace, utility, variance and workflow. Two relabels joined existing groups with the same meaning:
- Ch 5's "MFU (model FLOPs utilization)" now merges with Ch 19, 32, 37 and 44. This is an m key, which belongs to round 3. Because Ch 5 is first in book order, its body is now the glossary entry, so it was tightened to say "on the model's necessary math", in line with the other four.
- Ch 26's "Tokens per second (output speed)" now merges with Ch 4, 30 and 33, which define the same per-request writing speed.

"Electrical transformer" is shared by Ch 38 and Ch 39 in the same sense. The other new labels are each used once. `validate.py` and `check.py` are clean on all 19 edited chapters, and `validate.py` is clean on Appendix F.

## HOMONYM changes

| Key | Chapter, line | Old label | New label | Why | Key terms updated |
|---|---|---|---|---|---|
| state | Ch 17:324 | State (memory state) | Memory state | The fixed-size memory a state-space or recurrent layer carries from token to token, versus Ch 48's reinforcement-learning state (a description of the situation at one moment) | Yes |
| throughput | Ch 26:518 | Throughput (tokens per second) | Tokens per second (output speed) | Ch 26 means how fast one reply is written. Ch 23, 32, 37 and 43 mean total work across all users, and Ch 23 says the two "pull in opposite directions". Ch 26's own text uses only "tokens per second", and the new label merges with that existing key. | Yes |
| tiling | Ch 22:189 | Tiling (dynamic resolution) | Image tiling (dynamic resolution) | Cutting a large photo into tiles for a vision encoder, versus Ch 33's tiling of a matrix calculation into blocks that fit in on-chip memory | Yes |
| trace | App F:459 | Trace (of a matrix) | Trace of a matrix | The sum of a matrix's diagonal, versus Ch 37's profiler timeline (the first in book order, closer to the software "trace" readers meet in Ch 31) | No list in App F |
| transformer | Ch 38:111, Ch 39:197 | Transformer | Electrical transformer | The voltage-changing device, versus the neural-network architecture in Ch 1, 7, 15 and 18. Ch 42's "Large power transformer" is a separate key and is unchanged. | Yes, both |
| utility | Ch 41:118 | Utility | Electric utility | A company that delivers electricity, versus Ch 48's utility (how desirable an outcome is, in decision theory) | Yes |
| utilization | Ch 5:852 | Utilization (MFU) | MFU (model FLOPs utilization) | The share of a chip's peak speed used for the model's math, versus Ch 43 and Ch 44's share of time hardware does paid or useful work | Yes |
| variable | Ch 5:71 | Variable | Mathematical variable | A letter standing for a number, as in f(x), versus the programming variable (a named box holding a value) in Ch 3 and Ch 26. This follows round 2's "Mathematical function" relabel in the same chapter. | Yes |
| variance | Ch 9:250 | Variance (statistical) | Model variance | How much a model's predictions change with a different training sample (the bias–variance sense), versus Ch 6's variance as a measure of spread. It pairs with round 1's "Statistical bias" in the same section. | Yes |
| vulnerability | Ch 56:84 | Vulnerability | Vulnerability to harm (in risk analysis) | The third factor in risk ≈ hazard × exposure × vulnerability, versus the software security flaw in Ch 53 and Ch 58 | Yes |
| workflow | Ch 29:556 | Workflow | Automation workflow | A Zapier-style chain of a trigger and actions, versus Ch 28's LLM workflow (steps fixed in code, as opposed to an agent). This follows round 1's "Automation action" relabel two lines above it. | Yes |

## CONTRADICTION changes

| Key | Chapter, line | Disagreement | Change | Source |
|---|---|---|---|---|
| smr | Ch 42:662 | Date. The Ch 42 definition said the first US units "are expected around the end of the 2020s". Ch 41's text says "first US units around 2030 at the earliest" (Table 41.3) and "New SMRs mostly arrive in the 2030s". Ch 42's own text heads the nuclear timeline "Around 2030 and after". | Now "The first US units are expected around 2030 at the earliest." Ch 41's definition gives no date and is unchanged. | https://www.nrc.gov/about-nrc/news-releases/2026/26-079 (September 29, 2026: a construction permit only; TVA still needs a separate operating license before loading fuel). Ch 41:375-389 and Ch 42:660. |
| sec | Ch 61:101, Ch 64:118 | Fact and scope. In the input, Ch 61 said public companies "file audited financial results with it every quarter". Only the annual 10-K is audited; the three quarterly 10-Qs are generally unaudited. Ch 61 and Ch 64 also said the SEC regulates "stock markets", while Ch 43 says "stock and bond markets". | The "audited" error had already been corrected by another agent, working at the same time, when this round re-read the line. It now says the yearly report is audited and the quarterly reports are only reviewed. This round aligned the first sentence: Ch 61 and Ch 64 now open "The US government agency that regulates stock and bond markets." (Ch 43's wording). | https://en.wikipedia.org/wiki/Form_10-Q ("the financial statements are generally unaudited", three 10-Qs a year). https://www.sec.gov/about/mission (oversight of US capital markets). |

## OK groups that got consistency edits

| Key | Chapters edited | Shared core sentence now used | What each chapter kept |
|---|---|---|---|
| tsmc | Ch 32:388, 34:119, 42:380, 43:452, 61:170 | "The Taiwanese company that is the world's largest contract chipmaker (foundry) and manufactures nearly all advanced AI chips to their designers' blueprints." | Ch 32: customers NVIDIA, AMD, Apple and Google, which design chips but do not make them (Chapter 36). Ch 34: customers, plus the CoWoS packages. Ch 42: the CoWoS packaging lines. Ch 43: customers. Ch 61: a single point the whole AI industry depends on. Ch 42's "most of the world's most advanced chips" became "nearly all advanced AI chips", the wording of the other chapters. |
| sk hynix | Ch 35:67, 42:378, 43:454, 61:176 | "A South Korean memory-chip maker, part of the SK business group, that leads the market for the high-bandwidth memory (HBM) stacked beside AI chips and has been NVIDIA's main HBM supplier since HBM3." | Ch 35, 42 and 61: Samsung and Micron as the other two HBM makers. Ch 42's "SK industrial group" and "the leading supplier of HBM in recent years", and Ch 61's "a leading supplier", now match the others. |
| tpu | Ch 32:687, 35:317 | "Google's family of chips designed specifically for neural-network math, first deployed in Google's data centers in 2015." (the opening of Ch 2, the glossary winner, which is unchanged) | Ch 32: AI ASICs, large systolic arrays, Google's own chip-to-chip network, eighth generation (TPU 8t and TPU 8i) in 2026. Ch 35: systolic arrays, large pods, eighth generation in 2026. |
| 800 v dc distribution | Ch 34:430, 39:501, 42:644 | "NVIDIA's announced power architecture for 2027-era AI racks, which sends 800-volt direct current to the racks instead of alternating current (AC)." | Ch 34: AC glossed as "the kind the grid supplies", full-scale production with Kyber racks (around 600 kW each), NVIDIA's 85% / 45% / 5% figures. Ch 39: the same figures plus racks of around 1 MW. Ch 42: "The higher voltage cuts copper, conversion losses and space." |
| smic | Ch 36:37, 59:876 | "China's largest foundry (contract chipmaker)" | Ch 36: EUV out of reach, 7 nm-class (reportedly 5 nm-class), Ascend chips reportedly. Ch 59: makes chips other companies design, Ascend per teardown reports, US export controls. |
| sb energy | Ch 35:573 | Ch 35 now matches Ch 43's first sentence: "...backed by Japan's SoftBank Group (a technology investment company and a lead partner in OpenAI's Stargate project, Chapter 42)." Before this, the sentence could be read as calling SB Energy itself the Stargate lead partner. | The pointer to Chapter 42 |
| superchip | Ch 32:720 | "one or more GPUs" became "one or two GPUs", matching Ch 34 (GH200 pairs one GPU with the CPU, and GB200, GB300 and Vera Rubin pair two). | Ch 32's examples: Grace plus two Blackwell GPUs (GB200), Vera plus two Rubin GPUs |

Sources for these edits:
- TSMC: https://en.wikipedia.org/wiki/TSMC ("the leading dedicated contract chipmaker", about 70% of the global foundry market) and https://www.tsmc.com/english/aboutTSMC/company_profile ("pioneered the pure-play foundry business model"). The book's Ch 36:35 says TSMC is "by far the largest" foundry.
- SK hynix: the book's own Ch 33:404 and Ch 36:541 ("the market leader and NVIDIA's primary HBM supplier since HBM3", with industry trackers putting it at roughly half or more of shipments). No primary source was fetched (see below).
- 800 V DC: https://developer.nvidia.com/blog/nvidia-800-v-hvdc-architecture-will-power-the-next-generation-of-ai-factories/ ("Full-scale production of 800 VDC data centers will coincide with NVIDIA Kyber rack-scale systems in 2027"; 85% more power through the same conductor than 415 VAC; 45% less copper; up to 5% better end-to-end efficiency).
- TPU: freshness-appendices.md and freshness-part6.md (TPU 8t and 8i, April 2026, confirmed at https://cloud.google.com/blog/products/compute/tpu-8t-and-tpu-8i-technical-deep-dive). Only the wording changed here.

## OK groups, no change (141)

6nd rule, safety case, safety classifier, saliency map, sampling, sampling bias, sampling rate, sandbagging, sandbox, scalable oversight, scale-across, scaling laws, scikit-learn, seat-based pricing, seed, self-play, self-supervised learning, semantic search, semiconductor, server, server-sent events, services-as-software, serving engine, shortcut learning, sigmoid, single-line diagram, softmax, software regression, sparse attention, sparsity, special token, specificity, spectrogram, speed to power, sql, sram, sri, standard deviation, stateless, status code, steelman, stochastic gradient descent, stop reason, streaming, sub-agent, substation, supervised learning, switchgear, switching cost, sycophancy, symbolic ai, synthetic data, system card, system prompt, systolic array, t-shaped skills, take-or-pay contract, tanh, tape-out, task, tco, teleoperation, temperature, temporal consistency, tensor, tensor core, tensor parallelism, test-time compute, text encoder, the model eats your feature, thinking tokens, time horizon, time to first token, tokamak, token, tokenizer, tokens per second, tool call, tool poisoning, top-p sampling, tops, total parameters, training, training compute, training opt-out, transfer learning, transistor, trusted access program, tsv, ttft, tts, u-net, uc, ucie, underfitting, unembedding, unified memory, unit economics, unit test, unsupervised learning, up to deal, uplift, uprate, url, usage-based pricing, validation set, valuation, vanishing gradient, vector, vector database, verbosity bias, verifier, version control, vertical ai, vibe coding, vision transformer, vision-language model, vision-language-action model, visual grounding, vocabulary, voice cloning, von neumann architecture, wafer, wafer-scale engine, wake word, warmup, warrant, watt, watt-hour, web crawler, weight, weighted sum, weights, whistleblower protection, word2vec, workflow automation, world model, wrapper, xcon, xor, zero / fsdp.

("tokens per second" gained Ch 26 through the throughput relabel. Its existing definitions were not edited.)

Notes on groups that were borderline but left as they are:
- **sparsity**: Ch 51 (the share of a ratings table that is empty) and Ch 57 (most values zero, or only a few features active) describe the same idea, applied to data and to representations.
- **wafer-scale engine**: Ch 32 says "an entire silicon wafer" and Ch 35 "nearly an entire" wafer. Cerebras says "One silicon wafer" (https://www.cerebras.ai/chip, 46,225 mm²). Wikipedia says the chip is 215 mm square and takes up an entire wafer (https://en.wikipedia.org/wiki/Cerebras). A 215 mm square is about the largest that fits on a 300 mm wafer, so both readings hold.
- **800 v dc distribution**: Ch 34's Kyber racks of "around 600 kW" and Ch 39's "racks of around 1 MW" do not conflict. NVIDIA describes the architecture as designed for megawatt-class racks, starting with Kyber in 2027.
- **time to first token / ttft**: these are two separate keys because one label starts with the abbreviation. Within each key the definitions agree.
- **synthetic data**: Ch 19 and 20 say "generated by AI models" and Ch 47 and 49 "a model or simulator". Ch 11, the glossary winner, covers both.
- **valuation**: Ch 43 and Ch 65 give the post-money valuation and Ch 61 the general idea. These are compatible.
- **sri**: Ch 7 says Shakey was "the first mobile robot to reason about its own actions" and Ch 48 "one of the first mobile robots". These are compatible. Both give the 1946 founding.
- **symbolic ai**: only Ch 54 gives dates ("from the 1950s to the 1980s"). Ch 1 and Ch 7 give none, so there is no conflict between definitions.
- **streaming**: Ch 26 describes receiving the response and Ch 4 and Ch 44 sending it. These are the two ends of the same thing.

## Left as is or unresolved

- WebSearch quota was exhausted. https://www.investor.gov/... (Form 10-Q glossary) returned HTTP 403 and https://www.sec.gov/files/reada10q.pdf returned 404, so the 10-Q point rests on Wikipedia. It is a stable fact, and another agent had already made the same correction.
- SK hynix's HBM leadership is taken from the book's own hedged text in Ch 33 and Ch 36. No primary market-share source was fetched in this round.
- The "mfu" group (an m key, round 3's range) now has Ch 5 as its first definition. Round 3's input (defgroups-3.json) predates this change.
- `extra-terms.json` still holds a research-file entry labeled "Variance (statistical)". It is not a chapter callout, and build.py adds extra terms only when no chapter defines the key ("variance" is defined in Ch 6), so it has no effect.
- GLOSSARY.md is a build output and still shows the old labels until the next build.
- Body text was not changed. Ch 26's prose never used "throughput", and the electrical "transformer" prose in Ch 38 to 42 reads correctly next to the new labels.
