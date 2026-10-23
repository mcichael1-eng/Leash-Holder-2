# Repeated definitions, keys a to c (reconciliation round 1)

Date: October 23, 2026. Input: `defgroups.py` run on the whole book (3,311 distinct glossary keys, 727 defined more than once). This report covers only keys starting with a, b or c: **156 groups, 411 callouts**.

Merge rule used by the glossary build: the label with any text in parentheses removed and lowercased is the key. The body from the first chapter in book order wins.

## Counts

| Class | Groups | What was done |
|---|---|---|
| HOMONYM | 7 | The odd meaning got a new label that differs outside the parentheses. That chapter's Key terms list was updated too. |
| CONTRADICTION | 6 | Brought into line with the best-supported version (scope, name, date or a technical detail). |
| OK | 143 | Same meaning, compatible wording. For AMD (8 callouts) and AWS (8) the first sentence was rewritten to match across chapters, so the glossary entry reads well. |
| Total | 156 | 59 definition lines and 8 Key terms entries edited, in 28 chapters |

After the edits, `defgroups.py` finds no a to c homonyms. The new labels create no new collisions: "Reinforcement learning agent" is shared only by Chapters 8 and 48, which use it in the same sense. The other six new labels are each used once. `validate.py` and `check.py` are clean on all 28 edited chapters.

## HOMONYM changes

| Key | Chapter, line | Old label | New label | Why | Key terms updated |
|---|---|---|---|---|---|
| action | Ch 29:554 | Action | Automation action | Ch 29 means a step in a Zapier-style automation. Ch 48 means a choice an agent can make in reinforcement learning (RL). | Yes ("automation action") |
| agent | Ch 8:327 | Agent | Reinforcement learning agent | The RL learner and decision-maker, versus the AI agent (a tool-using system) in Ch 1, 21, 25, 28, 55 and 62 | Yes |
| agent | Ch 48:471 | Agent | Reinforcement learning agent | Same as above. The body already says the AI agent is a broader idea. | Yes |
| backbone | Ch 45:121 | Backbone | Model backbone | The feature-extracting part of a vision model, versus the internet's long-distance fiber links (Ch 4) | Yes |
| bias | Ch 9:248 | Bias (statistical) | Statistical bias | Systematic prediction error. Ch 5, 8 and 12 mean the bias parameter added in a neuron. | Yes |
| bottleneck | Ch 14:533 | Bottleneck (information bottleneck) | Information bottleneck | Information squeezed through a fixed-size vector, versus the slowest step in a process (Ch 44) | Yes |
| cold start | Ch 21:366 | Cold start (cold-start data) | Cold-start data | Supervised fine-tuning (SFT) data used before RL. App F means the start-up delay of a serverless function. | Yes |
| complement | Ch 60:84 | Complement (economics) | Economic complement | A technology that makes workers more valuable, versus the probability complement in Ch 6 | Yes |

## CONTRADICTION changes

| Key | Chapter, line | Disagreement | Change | Source |
|---|---|---|---|---|
| agent mode | Ch 25:759 | Scope. The glossary-winning body said "A chat-app feature". Ch 29 defines it as a setting in coding tools. | Now "A setting in a chat app or coding tool...". "Running commands" was added to the examples. | Ch 29 text (agent mode in IDEs) |
| corpus | Ch 19:27 | Scope. Ch 19 said "used for training". Ch 27 uses it for the documents a retrieval system searches. | Now "A large collection of text or documents, such as the text gathered to train a model." | Standard usage. Both chapters now fit. |
| ai governance | Ch 62:385, Ch 63:392, Ch 65:638 | Scope. Ch 59 (the glossary winner) says "the whole set of rules, institutions and processes", including laws and courts. Ch 62, 63 and 65 said only "the policies... an organization uses". | Each now opens with "The rules, institutions and processes that shape how AI is built and used. Inside an organization, it means..." The rest of each chapter's text is kept. | Ch 59 definition. The Ch 62 and 63 sections themselves cover both government and companies. |
| ces | Ch 34:350 (and Ch 7:696 to match) | Name. Ch 34 called it "The Consumer Electronics Show". Ch 49 says "originally the Consumer Electronics Show". | Ch 7 and Ch 34 now use Ch 49's core: "The large consumer-technology trade show held every January in Las Vegas (originally the Consumer Electronics Show)". Each keeps its own second clause. | https://en.wikipedia.org/wiki/CES_(trade_show) ("formerly an acronym for Consumer Electronics Show") |
| cuda | Ch 32:382, Ch 35:221 (plus Ch 7:339 and Ch 65:606 to match) | Date. Ch 2 and Ch 7 said "released in 2007". Ch 32 and Ch 35 said "available since 2006–07". | All five definitions now open with Ch 2's core: "NVIDIA's software platform, released in 2007, that lets programmers run general calculations on its GPUs." Before this, Ch 65 had no date. | https://en.wikipedia.org/wiki/CUDA (first SDK public February 15, 2007). The timelines in Ch 2, 7 and 32 already say 2007. |
| cowos | Ch 33:333, Ch 44:555 (plus Ch 34:151 and Ch 36:469 to match) | Technical detail. Ch 33 said "a silicon interposer" and Ch 44 said "a thin silicon slab". Ch 34 and Ch 36 explain that CoWoS-L (used for Blackwell and Rubin) uses an organic interposer with small silicon bridges. Ch 33's own Interposer definition says the same. | All four definitions now share one core: "TSMC's family of advanced packaging technologies that place GPU [Ch 36: processor] dies and HBM stacks side by side on an interposer, a thin slab with dense wiring." Ch 36 keeps "(2.5D)" and Ch 44 keeps "brake", because Bottleneck is defined only later in Ch 44. | The book's own Ch 36:465-467 and Ch 34:153. TSMC's 3DFabric page returned HTTP 403. |

## OK groups that got consistency edits (the organization sentence now matches)

| Key | Chapters edited | Shared core sentence now used | What each chapter kept |
|---|---|---|---|
| amd | Ch 7:605, 13:1080, 30:491, 34:129, 38:371, 43:351, 53:542, 60:281 | "An American company that designs CPUs for PCs and servers and is NVIDIA's main rival in AI GPUs, with its Instinct line of data-center accelerators." | Ch 30: ROCm as its counterpart to CUDA. Ch 34: chips made by TSMC. Ch 38: the MI355X and MI455X. Ch 43: Helios racks. Ch 53 and Ch 60: pointers to Chapter 35. |
| aws | Ch 3:543, 32:734, 34:390, 38:627, 43:177, 58:152, 61:190, 62:319 | "Amazon's cloud-computing business, the world's largest cloud provider, which rents out computing power, storage and AI chips over the internet." | Ch 3: launched in 2006. Ch 32 and 34: Trainium and Inferentia (and Annapurna Labs in Ch 34). Ch 43: biggest of three hyperscalers, by the hour or on contracts. Ch 58: AI services and Trainium. Ch 61: customers and chips. Ch 62: ahead of Azure and Google Cloud, plus certifications. |

Sources for the AWS change: Synergy Research Group, Q3 2025 cloud infrastructure shares (Amazon 29%, Microsoft 20%, Google 13%): https://www.srgresearch.com/articles/cloud-market-share-trends-big-three-together-hold-63-while-oracle-and-the-neoclouds-inch-higher . Two chapters said "one of the three biggest" and the others said "the largest". Both were true, but they now match.

## OK groups, no change (136)

a/b test, ablation, abstention, accelerator, activation checkpointing, activation function, activations, active parameters, adaptive thinking, advantage, age assurance, agent skill, agi, ai agent, ai app builder, ai control, ai engineer, ai exposure, ai rd automation, ai winter, algorithm, alignment, alpac, anomaly detection, api, api gateway, api key, arena, arithmetic intensity, artificial intelligence, artificial neuron, asi, asic, asml, asr, attention, attention sink, augmentation, automatic differentiation, automation, automation bias, autoregressive generation, autoregressive image generation, background agent, backpropagation, backup generator, bandwidth, barge-in, base die, base model, base rate, batch, batch api, batching, battery energy storage system, bayes rule, beam search, behind-the-meter, benchmark, benchmark contamination, benchmark saturation, bf16, bit depth, bpe, bridge power, brittleness, bubble, bug bounty, busbar, c2pa, cache, caisi, calibration, campus, capability threshold, capacity factor, capex, catastrophic forgetting, cbrn, cdu, chain of command, chain of thought, chain rule, chain-of-thought, chain-of-thought monitorability, character training, checkpoint, chiplet, churn, cicero, circular deal, citation, client, clip, clock speed, closed model, cluster, clustering, code execution, cold plate, cold-start problem, collaborative filtering, collective communication, colocation, combined-cycle gas turbine, commissioning, commit, common crawl, compaction, compute, compute-bound, computer use, computer vision, confidence interval, confounder, connector, constitution, constitutional ai, constitutional classifiers, containment, containment rate, content-based filtering, context engineering, context extension, context parallelism, context rot, context window, continual learning, contrastive learning, core, cosine similarity, cost per million tokens, cot faithfulness, cot monitoring, cpu, critical path, cross-attention, cross-entropy, cross-entropy loss, cset, customer concentration.

Notes on groups that were borderline but left as they are:
- **c2pa**: Ch 47 calls it the standards group, and Ch 58 and Ch 59 call it the standard. C2PA is both the coalition and its specification, so these fit. The 2021 founding and the founding members were confirmed in freshness-part8.
- **caisi**: Ch 57 and Ch 59 agree, including the June 2025 rename and the October 2026 name "CAISSI" on its NIST page (verified in freshness-part9).
- **ablation**: Ch 57 gives the interpretability case (zeroing a part of a model). It is the same idea as the general experiment in Ch 19, 62 and 65.
- **activations**: Ch 33 and 37 (training memory) and Ch 57 (interpretability) describe the same quantity.
- **churn**: Ch 10 (customers leaving) and Ch 64 (the share who cancel per period) are the event and its rate.
- **chain of thought / chain-of-thought**: the hyphen makes these two different glossary keys. Within each key the definitions agree.

## Left as is or unresolved

- Ch 32 body text (line 380, "In 2006–07, NVIDIA released a way to program its GPUs directly", and the recap at line 863) still says 2006–07, while its definition now says "released in 2007". This is defensible: CUDA-capable GeForce 8800 hardware shipped in November 2006 and the SDK went public in February 2007. Only definitions were changed in this round.
- Ch 34's CES definition still says "NVIDIA launched Vera Rubin at CES 2026". This was not re-checked here. Ch 49 notes that a CES launch is an announcement.
- TSMC's own CoWoS page (3dfabric.tsmc.com) returned HTTP 403. The interposer fix rests on the book's own Ch 34 and Ch 36 descriptions of CoWoS-S, -L and -R.
