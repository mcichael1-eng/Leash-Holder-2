# Repeated definitions, keys m to r (reconciliation round 3)

Date: October 23, 2026. Input: `defgroups.py` run on the whole book (3,318 distinct glossary keys, 723 defined more than once). This report covers only keys starting with m, n, o, p, q or r: **195 groups, 536 callouts**.

Merge rule used by the glossary build: the label with any text in parentheses removed and lowercased is the key. The body from the first chapter in book order wins. One more detail of `build.py` matters here: the glossary shows the **longest label** in a group next to that first body. So a group such as "Router" (Ch 4, network device) + "Router (model router)" (Ch 21) displayed the label "Router (model router)" over the home-router definition. The relabels below remove every such mismatch in m to r.

## Counts

| Class | Groups | What was done |
|---|---|---|
| HOMONYM | 11 | The odd meaning(s) got a new label that differs outside the parentheses (15 definition lines). Each chapter's Key terms list was updated too. |
| CONTRADICTION | 2 | Brought into line with the best-supported version (a number range and a scope). |
| OK | 182 | Same meaning, compatible wording. For 9 organizations and products (NVIDIA, MCP, Python, MTIA, MGX, NASA, PyTorch, MIRI, MIT NANDA) the core sentence was made identical across chapters (30 lines). One OK group (parallelism) got a label tidy so the glossary label matches the body. |
| Total | 195 | 48 definition lines and 16 Key terms entries edited, in 34 chapters |

After the edits, `defgroups.py` (re-run, output in the scratchpad as `defgroups-3-after.json`) finds no m to r homonyms. Two new labels join an existing key on purpose, in the same sense: "Model router" (Ch 21 now merges with Ch 23's "Model router") and "Software regression" (Ch 29 and Ch 31 share it). "Numerical precision" is shared by Ch 5 and Ch 32. The other new labels are each used once. `validate.py` (268/268 diagrams) and `check.py` are clean on all 34 edited chapters: 3, 5, 7, 11, 13, 17, 19, 21, 25, 26, 27, 28, 29, 30, 31, 32, 34, 35, 36, 38, 42, 43, 44, 45, 48, 50, 51, 52, 54, 56, 58, 62, 64, 65.

## HOMONYM changes

| Key | Chapter, line | Old label | New label | Why | Key terms updated |
|---|---|---|---|---|---|
| memory | Ch 25:671 | Memory (in chat apps) | Chat memory | Saved notes a chat app re-inserts into the context, versus computer RAM (Ch 2, the glossary winner). The glossary was showing "Memory (in chat apps)" over the RAM body. | Yes |
| p | Ch 19:285 | μP (maximal update parametrization) | Maximal update parametrization (μP) | The key builder strips "μ" and the parentheses, so μP and P(doom) (Ch 60) both became "p". The glossary showed the μP label over the μP body and dropped P(doom) entirely. | Yes |
| parsing | Ch 27:388 | Parsing | Document parsing | Extracting text and structure from PDFs and other files, versus grammatical parsing of a sentence (Ch 54), the classic meaning, which keeps the bare word. | Yes |
| patch | Ch 58:136 | Patch | Security patch | A software update that fixes a vulnerability, versus an image patch treated as a token (Ch 15, Ch 22). | Yes |
| position bias | Ch 51:352 | Position bias | Position bias in rankings | People clicking top-ranked items more, versus an AI judge favoring the first or last answer (Ch 31, first in book order). | Yes ("position bias in rankings") |
| precision | Ch 5:874 and Ch 32:550 | Precision | Numerical precision | How finely a number format resolves values, versus the classification metric TP ÷ (TP + FP) in Ch 9. Ch 9 keeps the bare word because it sits next to Recall, Specificity and F1 score, and "precision" alone means the metric in ML usage. | Yes, both chapters |
| prediction | Ch 50:198 | Prediction (motion forecasting) | Motion prediction (motion forecasting) | Forecasting other road users' paths, versus the general idea of a model's prediction (Ch 1). The glossary was showing the longer motion-forecasting label over Ch 1's body. | Yes |
| re-identification | Ch 45:377 | Re-identification (re-ID) | Visual re-identification (re-ID) | Matching a person or vehicle across cameras by appearance, versus de-anonymizing a dataset by linking it with other data (Ch 11). Same label-over-wrong-body problem. | Yes |
| regression | Ch 29:157 and Ch 31:296 | Regression | Software regression | A change that breaks something that used to work, versus the supervised task of predicting a number (Ch 8, first in book order). Ch 29 and Ch 31 mean the same thing and now merge under the new label. | Yes, both chapters |
| resolution | Ch 36:254 | Resolution (lithography) | Lithography resolution | The smallest feature a lithography tool can print, versus an image's pixel count (Ch 3, Ch 45). | Yes |
| resolution | Ch 54:172 | Resolution | Resolution rule | The logic inference rule behind automated theorem proving, a third, unrelated meaning. | Yes |
| router | Ch 17:61 | Router (gating network) | MoE router (gating network) | The small network inside a mixture-of-experts layer that picks experts, versus the network device that forwards internet traffic (Ch 4). | Yes |
| router | Ch 21:507 | Router (model router) | Model router | A component that sends each request to a fast or a reasoning model. Now merges with Ch 23's identical-sense "Model router". The glossary was showing "Router (model router)" over Ch 4's home-router body. | Yes |

## CONTRADICTION changes

| Key | Chapter, line | Disagreement | Change | Source |
|---|---|---|---|---|
| mfu | Ch 44:396 | Number. Ch 19 (the glossary winner), Ch 32 and Ch 37 say large runs typically reach 35 to 50%. Ch 44 said "about 25 to 50%". Its 25% comes from Epoch AI's assumption for an FP8 run (Ch 44 Table 44.3, Ch 37:600). | Now: "Large training runs typically reach about 35 to 50% of their 16-bit peak, and less of the faster 8-bit peak: Epoch AI assumes about 25% (Chapter 37)." The acronyms BF16 and FP8 were avoided because Ch 44 does not define them. | Llama 3.1 405B at 38 to 43% MFU on 16,384 H100s (already cited in Ch 19:337, Ch 32:280 and Ch 37:105 and 444); Ch 37:600 for the lower MFU against an FP8 peak. |
| payback period | Ch 64:362 | Scope. Ch 43 (the glossary winner) gives the general meaning (cash from an investment repaying its cost). Ch 64 defined it only as customer-acquisition payback. | Now opens with Ch 43's general sentence, then "For a new customer, it is how long their profit takes to repay the cost of acquiring them." The customer meaning used in Ch 64's unit-economics example is kept. | Ch 43 definition, standard usage. |

## OK groups that got consistency edits (the core sentence now matches)

| Key | Chapters edited | Shared core sentence now used | What each chapter kept |
|---|---|---|---|
| nvidia | Ch 3:370, 11:495, 19:258, 30:489, 34:28, 38:42, 43:90, 52:246, 58:150, 62:333 (10) | "An American chip company that designs most of the GPUs used to train and run AI models, along with the networking gear that links them and CUDA, the software for programming them." Ch 52 and Ch 58 keep their in-place spelling-out of GPU. | Ch 3: founded in 1993 to make video-game graphics chips, then H100 and B200. Ch 11: among the most valuable companies, Part VI. Ch 19: graphics origins and dominance of accelerator sales. Ch 30: gaming cards to H100, contract factories. Ch 34: rack designs, TSMC makes the chips. Ch 38: rack designs and the Hopper, Blackwell, Rubin generations. Ch 43: TSMC and its GPU generations. Ch 52, 58, 62: pointers to Chapter 35. Before this, the sentences varied between "the US company", "the American company" and "an American chip company", and only some mentioned CUDA. |
| mcp | Ch 7:593, 25:745, 28:502, 62:203, 65:315 (5) | "An open standard for connecting AI applications to outside tools and data sources, introduced by Anthropic in November 2024 and governed since December 2025 by the Agentic AI Foundation, part of the nonprofit Linux Foundation." | Ch 7: the USB-port analogy. Ch 25: one common "plug", most connectors are built on it. Ch 28 and Ch 62: build one MCP server, any compatible app can use it. Ch 65: email, calendars, drives and databases, the "USB-C port for AI" phrase. Before this, Ch 7, 62 and 65 had no governance line and Ch 25 said only "under the Linux Foundation". |
| python | Ch 3:380, 26:106, 62:217, 65:394 (4) | "The most widely used programming language for AI work, popular for its readable code and its huge collection of ready-made libraries for math, data and neural networks." | Ch 26: reads almost like English. Ch 62: (see Chapter 3). Ch 65: almost every AI course, tool and codebase uses it. |
| mtia | Ch 32:700, 35:363, 43:349 (3) | "Meta's own family of custom AI chips, built first to run the recommendation and ranking models behind Facebook and Instagram feeds." (Ch 32 keeps "(ASICs)" after "chips".) | Ch 32: Meta's effort to rely less on bought GPUs. Ch 35: based on RISC-V, designed with Broadcom. Ch 43: designed with Broadcom. Ch 43 previously said "used mainly" (present tense, single chip); "built first" matches Ch 32 and 35. |
| mgx | Ch 42:434, 43:624 (2) | "An Abu Dhabi investment firm backed by the government of the United Arab Emirates, founded in 2024 to invest in AI and AI infrastructure. It is a partner in OpenAI's Stargate project." | Both definitions are now identical (Ch 42 only gained the word "project"). |
| nasa | Ch 48:305, 52:506 (2) | "The United States government's space agency, which runs space missions, satellites, space telescopes and robotic probes such as the Mars rovers." | Ch 48: funds research on spacecraft autonomy. Ch 52: makes much of its data freely available. |
| pytorch | Ch 13:655, 62:307 (2) | "The most widely used deep-learning framework, a software library for building and training neural networks, originally developed at Meta and now governed by the PyTorch Foundation." | Ch 13: Python-first, dominates research and open models. Ch 62: JAX is the main alternative (see Chapter 13). |
| miri | Ch 56:506 (to match Ch 63:425) | "One of the oldest AI-risk organizations, a Berkeley nonprofit co-founded by Eliezer Yudkowsky in 2000." | Ch 56 gained "Berkeley" and "in 2000"; its second sentence is unchanged. |
| mit nanda | Ch 31:902 (to match Ch 28:494) | "A research initiative at MIT's Media Lab (MIT is the Massachusetts Institute of Technology) that studies networks of AI agents and how organizations adopt AI." | Ch 31 keeps its own sentence on the July 2025 "GenAI Divide" report. |

Label tidy in an OK group:

| Key | Chapter, line | Old label | New label | Why | Key terms updated |
|---|---|---|---|---|---|
| parallelism | Ch 19:266 | Parallelism (distributed training) | Training parallelism (distributed training) | Same idea as Ch 2 and Ch 32 (doing many operations at once), but Ch 19's body is the specific case of splitting one training run across chips. Because the glossary shows the longest label, readers saw "Parallelism (distributed training)" over Ch 2's general body. The two now have separate entries. | Yes |

Sources used for the consistency edits:
- MIRI founded in 2000 by Eliezer Yudkowsky, Brian Atkins and Sabine Atkins; nonprofit based in Berkeley, California: https://intelligence.org/about/
- MGX launched in March 2024 by Mubadala and G42, Abu Dhabi, government-owned: https://en.wikipedia.org/wiki/MGX_(company) (mgx.ae was too large to fetch). MGX as one of the four initial Stargate equity partners: https://en.wikipedia.org/wiki/Stargate_LLC (openai.com returned HTTP 403).
- MCP donated to the Agentic AI Foundation on December 9, 2025: already confirmed in freshness-part1-3 and freshness-part5 (https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation ; https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation). Ch 28:506 and Ch 28:691 say the same.
- MIT NANDA as a Media Lab group: https://nanda.media.mit.edu/ redirects to https://www.media.mit.edu/groups/nanda/overview/ (the target page itself returned HTTP 503).
- NVIDIA founding year (1993), CUDA, and the GPU generations were already in the book. No new facts were added beyond rearranging them.

## OK groups, no change (172)

machine code, machine learning, margin of error, matrix, matrix factorization, matrix multiplication, mats, mean squared error, megawatt and gigawatt, memorization, memory bandwidth, memory hierarchy, memory wall, memory-bound, metadata, metr time horizon, microgrid, mid-training, misuse, mixed precision, mixture of experts, ml engineer, mla, mlops, mlp, moat, model, model card, model cascade, model collapse, model snapshot, model spec, model tier, model welfare, monte carlo tree search, moore's law, moratorium, moravec's paradox, multi-armed bandit, multi-token prediction, multimodal, multimodal model, multiply-accumulate, mycin, nameplate capacity, narrow ai, nash equilibrium, natural language processing, ncii, negative prompt, neocloud, neural network, neuro-symbolic ai, neuromorphic chip, next-token prediction, nic, nist ai rmf, noise, non-blocking network, notebook, npu, nuclear restart, oauth, object tracking, observability, ocr, one-hot encoding, open problem, open-source ai, open-weight model, operating margin, optical transceiver, optimizer, optimizer state, osworld, outcome-based pricing, over-refusal, over-the-air update, overfitting, package hallucination, parameter, pass@k, pdu, peak demand, peer review, perceptron, permissive license, perplexity, personal data, phishing, pii, pilot, pixel, planning, point cloud, policy, portfolio, post-training, power law, power user, powered land, ppo, pre-deployment testing, preemption, preference data, prefill, pretraining, primary source, prisoner's dilemma, probability distribution, production, program, progressive disclosure, prompt, prompt caching, prompt chaining, prompt engineering, prompt injection, proof assistant, proof of concept, proxy variable, pruning, public benefit corporation, pue, pull request, quantization, quantization-aware training, rack, rack and stack, rack power shelf, rag, randomized controlled trial, rate limit, rational agent, reasoning effort, reasoning model, reciprocating engine, recognized revenue, recommender system, recursive self-improvement, red-teaming, register, regularization, reinforcement fine-tuning, reinforcement learning, reinforcement learning agent, relu, remote assistance, replication, repository, research engineer, research taste, residual, residual connection, residual stream, resnet, reticle limit, reward, reward hacking, reward model, rgb, risc-v, rl environment, rlaif, rlhf, rlvr, rmsnorm, robots.txt, round-trip time, routing, rubric, run-rate.

Notes on groups that were borderline but left as they are:
- **narrow ai**: Ch 1 says "Nearly all AI deployed in the world is narrow"; Ch 60 says "Nearly all deployed AI before chatbots was narrow". Ch 60 is more cautious, but both hold if you count deployed systems (spam filters, recommenders, face unlock far outnumber general chatbots).
- **perceptron**: Ch 7 says 1957–58, Ch 12 says 1958. Rosenblatt's first report was dated 1957 and his best-known paper was published in 1958, so both fit.
- **metr time horizon**: Ch 7's "doubled roughly every four to seven months" matches Ch 57:600 (about 4.2 months since 2023, about 7 months in the 2019-onward study) and Ch 24:320.
- **optimizer state**: Ch 13 "several times the size of the model", Ch 33 and 37 "often larger than the model". Adam's two FP32 averages are 8 bytes per parameter against 2 for BF16 weights, so both are true.
- **pue**: Ch 39 "industry average around 1.5 to 1.6" and Ch 44 "around 1.5" are compatible.
- **model tier**: Ch 24's "OpenAI's Luna, Sol and Astra" are the GPT-6 tiers confirmed in freshness-part1-3 and freshness-appendices; no change.
- **moratorium**: Ch 42 (a local ban on approving data centers) and Ch 59 (a proposed pause on state AI laws) are the same word in two policy settings; both bodies open with "A temporary ban".
- **planning, policy, parameter, residual, routing, pilot**: each group uses one meaning, sometimes with a narrower context in parentheses that matches the first body.

## Left as is or unresolved

- Ch 19's μP definition says "A 2022 recipe". The parametrization itself first appeared in Yang and Hu's Tensor Programs IV paper (2020); the 2022 Tensor Programs V paper introduced the hyperparameter-transfer recipe the chapter describes. This was not changed, because it is a single definition, not a repeat, and was not re-sourced here.
- Ch 66's preemption definition says only Congress or the courts can preempt state law. Federal agency rules can also preempt when Congress authorizes them. Ch 59 does not conflict, so this was left for a law-and-policy check.
- MTIA "designed with Broadcom" still rests on wide reporting (see adversarial-review). It was kept where it already appeared (Ch 35, Ch 43) and not added to Ch 32.
- Only definition lines and Key terms lists were changed in this round. Body text using the old bare words ("parsing", "patch", "regression", "router") reads correctly in context.
