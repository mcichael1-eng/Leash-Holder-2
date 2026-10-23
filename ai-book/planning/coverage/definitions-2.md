# Repeated definitions, keys d to l (reconciliation round 2)

Date: October 23, 2026. Input: `defgroups.py` run on the whole book (3,318 distinct glossary keys, 723 defined more than once). This report covers only keys starting with d to l: **217 groups, 636 callouts**.

Merge rule used by the glossary build: the label with any text in parentheses removed and lowercased is the key. The body from the first chapter in book order wins.

## Counts

| Class | Groups | What was done |
|---|---|---|
| HOMONYM | 10 | The odd meaning got a new label that differs outside the parentheses. That chapter's Key terms list was updated too. |
| CONTRADICTION | 5 | Brought into line with the best-supported version (a number, a name, a date or the scope). |
| OK | 202 | Same meaning, compatible wording. In 12 of these groups (organizations, products and one unit) the core sentence was rewritten to match across chapters, so the glossary entry reads well. The other 190 were left as they are. |
| Total | 217 | 37 definition lines and 11 Key terms entries edited, in 28 chapters |

After the edits, a second `defgroups.py` run finds no d to l homonyms. Seven keys no longer repeat: exposure, feature, frontier safety framework, gate, inference engine, intervention and ipo. One new shared key appeared: "learned feature" (Ch 12 and Ch 57), which both use in the same sense. One relabel joined an existing a-key group: Ch 60's "AI exposure" now merges with Ch 63 and Ch 66, which already used that label in the same sense. Round 1 classed that group as OK. The other new labels are each used once. `validate.py` and `check.py` are clean on all 28 edited chapters.

## HOMONYM changes

| Key | Chapter, line | Old label | New label | Why | Key terms updated |
|---|---|---|---|---|---|
| exposure | Ch 60:74 | Exposure (to AI) | AI exposure | Ch 60 means the share of a job's tasks that AI could do or assist with. Ch 56 means contact with a hazard in risk analysis. The new label matches Ch 63:576 and Ch 66:377, which use "AI exposure" in the same sense. | Yes |
| feature | Ch 12:775 | Feature (learned) | Learned feature | A pattern a network has learned to detect, versus Ch 8's input feature (a column of the data table). Ch 8 keeps the plain "Feature" label, the classic machine-learning sense used in Chapters 8 to 11. | Yes |
| feature | Ch 57:99 | Feature | Learned feature (in interpretability) | The same learned-feature sense as Ch 12, seen as a direction in activation space. It now merges with Ch 12. | Yes |
| function | Ch 5:69 | Function | Mathematical function | A rule mapping each input to one output, versus the programming function in Ch 3 (the glossary winner) and Ch 28 | Yes |
| framework | Ch 29:54 | Framework | Software framework | Ready-made app structure such as React or Django, versus the deep-learning framework (PyTorch, JAX) in Ch 13 and Ch 35 | Yes |
| gate | Ch 36:184 | Gate (of a transistor) | Transistor gate | A transistor's control terminal, versus Ch 14's learned 0-to-1 valve in a neural network | Yes |
| goodput | Ch 23:535 | Goodput | Serving goodput | The share of inference requests served within speed targets, versus the share of cluster time spent on useful training progress (Ch 19, 37, 44) | Yes |
| inference engine | Ch 54:77 | Inference engine | Expert-system inference engine | The rule-applying part of an expert system, versus the software that runs a model's weights (Ch 30) | Yes |
| intervention | Ch 59:589 | Intervention (in a lawsuit) | Legal intervention (in a lawsuit) | A party joining a court case, versus Ch 54's causal intervention (setting a variable to see what it causes) | Yes |
| ipo | Ch 20:422 | IPO (Identity Preference Optimization) | Identity Preference Optimization (IPO) | A DPO variant. Ch 61 uses IPO for initial public offering, the meaning most readers expect. Ch 20 came first in book order, so before this fix the glossary's "IPO" entry described the preference-tuning method. | Yes |
| frontier safety framework | Ch 56:573 | Frontier Safety Framework (FSF) | FSF (Frontier Safety Framework) | Google DeepMind's named policy, versus the generic term defined at Ch 56:541. The new label follows the pattern of the chapter's other named frameworks (RSP, Preparedness Framework). | Yes |

## CONTRADICTION changes

| Key | Chapter, line | Disagreement | Change | Source |
|---|---|---|---|---|
| gigawatt | Ch 7:607 | Number. Ch 7 said 1 GW is "about as much power as a million US homes". Ch 39:640, Ch 42:33 and Ch 66:315 say roughly 800,000 homes. | Now "roughly 800,000 average US homes". | EIA: the average US residential customer used 10,791 kWh in 2022 (https://www.eia.gov/tools/faqs/faq.php?id=97&t=3). 8.76 TWh ÷ 10,791 kWh ≈ 812,000 homes. Ch 42 uses 1.2 kW per home (≈ 833,000). |
| frontier lab | Ch 1:516, Ch 63:48 | Name. Ch 1 (the glossary winner) and Ch 63 listed "xAI" as a current lab. Ch 61:218 says "SpaceX's AI unit (formerly xAI)", and Ch 24 and Ch 42 tell the February 2026 acquisition. | Both now say "xAI (now part of SpaceX)", the wording already used in Ch 63's body text (line 42). | Ch 24:542 and Ch 42:465, both confirmed in freshness-part4 (row 132) and freshness-part7 via https://en.wikipedia.org/wiki/XAI_(company) |
| expert system | Ch 54:73 | Date. Ch 54 said expert systems were "the commercial face of AI in the 1970s and 1980s". Ch 1 says "the main commercial AI of the 1980s". The 1970s systems (MYCIN, DENDRAL) were research projects. | Now "First built in research labs in the 1970s, expert systems became the commercial face of AI in the 1980s." | https://en.wikipedia.org/wiki/Expert_system ("created in the 1970s and then proliferated in the 1980s") |
| knowledge cutoff | Ch 25:153, Ch 27:26 | Scope. These said a model "saw no training data" after the cutoff. Ch 18 and Ch 24 say "little or no", and Anthropic separates the reliable knowledge cutoff from the broader training data cutoff. | Both now say "saw little or no training data". The June 2026 dates are unchanged and still correct. | https://platform.claude.com/docs/en/about-claude/models/overview (Fable 5.1, Opus 5.5, Sonnet 5.5 and Haiku 5.5: reliable knowledge cutoff and training data cutoff both June 2026, with the footnote explaining the difference) |
| interpretability | Ch 10:169 | Scope. Ch 10 (the glossary winner) defines interpretability as a property: how easily a person can see why a model made a prediction. Ch 24, 57, 62, 65 and 66 define it as the research field that looks inside neural networks. | Ch 10 keeps its definition and adds: "The same word names the research field that studies what happens inside neural networks (Chapter 57)." The glossary entry now covers both senses. | The book's own Ch 57:24 |

## OK groups that got consistency edits

| Key | Chapters edited | Shared core sentence now used | What each chapter kept |
|---|---|---|---|
| darpa | Ch 7:327, Ch 49:637 | "The US Department of Defense's agency for funding ambitious, high-risk research." (Ch 53's wording) | Ch 7: ARPA and the ARPANET. Ch 49: the 2004 to 2007 Grand Challenge and Urban Challenge races. |
| dalle | Ch 7:484, Ch 22:420 | "OpenAI's family of text-to-image models: DALL·E (January 2021), DALL·E 2 (2022) and DALL·E 3 (2023). The name blends the painter Salvador Dalí and the Pixar robot WALL·E." (Ch 16's wording) | Ch 7: "which draw pictures from text descriptions". Ch 22: ChatGPT integration (2023) and the 2025 switch to GPT-4o image generation. |
| edgar | Ch 61:103 | "The SEC's free online database of company filings (sec.gov/edgar), where you can search any US public company's reports..." (Ch 43's wording) | "from quarterly results to IPO prospectuses", plus the primary-source sentence. This also removes the overclaim "every filing". |
| far.ai | Ch 63:427 | "A nonprofit research organization working on AI safety problems, such as..." (Ch 55's opening) | Robustness and attacks on safeguards, and the policymaker workshops |
| gb200 and gb300 | Ch 38:734, Ch 43:92 | "NVIDIA's "Grace Blackwell" superchips, each pairing one Grace CPU with two Blackwell GPUs (the original B200 in the GB200, the upgraded B300 in the GB300)." (Ch 34's wording) | Ch 38: what news reports of "GB200 GPUs" mean. Ch 43: adds "or Blackwell Ultra" (the chapter uses that name) and "36 of them, so 72 GPUs". |
| github | Ch 3:630, Ch 29:118 | "The largest website for storing Git repositories online and collaborating on them, owned by Microsoft." | Ch 3: issues, reviews, pull requests, and open-source AI code. Ch 29: GitLab and Bitbucket as alternatives. Ch 29's "most popular" became "largest", the description the source supports. |
| google colab | Ch 26:110 | "A free Google website (colab.research.google.com) where you can write and run Python code in your browser, with nothing to install." (Ch 8's wording) | The code runs on Google's computers, and the "Word document that can run code" analogy |
| iapp | Ch 62:387 | "The largest professional association for people who work in privacy and, increasingly, AI governance." (Ch 59's wording) | The AIGP certification |
| ibm | Ch 8:59, Ch 54:685, Ch 59:412 | "A large American computer company, founded in 1911, that dominated business computing for much of the 20th century." (Ch 7's wording) | Ch 8: Deep Blue (1997) and Watson (2011). Ch 54: the 1954 translation demo. Ch 59: today's software, cloud and consulting businesses and the Granite models. |
| iea | Ch 64:569 | "A Paris-based organization, set up by governments in 1974, that publishes widely used data and forecasts on world energy" (Ch 41's wording) | Supply and demand for member countries, and the widely cited data-center estimates |
| jll | Ch 38:50 | "A global commercial real-estate services firm" (Ch 43 and Ch 61's wording, replacing "a large global commercial property firm") | Its data-center research team's estimates |
| frequency | Ch 39:180 | Now opens with the general meaning: "How many times per second something repeats, measured in hertz." This matches Ch 46's sound-wave definition. | The alternating-current detail (60 Hz and 50 Hz, generators in step). Ch 41's separate "Grid frequency" entry is unchanged. |

Sources for the organization edits:
- IBM: https://en.wikipedia.org/wiki/IBM (founded in 1911 as the Computing-Tabulating-Recording Company and renamed in 1924). ibm.com/history did not state the year.
- IEA: https://en.wikipedia.org/wiki/International_Energy_Agency ("a Paris-based autonomous intergovernmental organization, established in 1974"). iea.org returned HTTP 403.
- GitHub: https://en.wikipedia.org/wiki/GitHub ("the world's largest source code host", a Microsoft subsidiary since 2018).
- IAPP: https://iapp.org/about/ ("the largest association of our kind in the world", "the professional home for privacy, AI governance and digital responsibility", Artificial Intelligence Governance Professional certification).
- GB300: https://www.nvidia.com/en-us/data-center/gb300-nvl72/ (72 Blackwell Ultra GPUs and 36 Grace CPUs per rack).

## OK groups, no change (190)

dangerous-capability evaluation, dark fiber, data augmentation, data center, data curation, data exfiltration, data flywheel, data pipeline, data poisoning, data residency, data retention, data wall, database, dataset, decision boundary, decode, decoder, decontamination, deduplication, deep learning, deepfake, deliberative alignment, demand response, dennard scaling, dense model, deprecation, depreciation, derivative, die, diffusion model, dimension, dimensionality reduction, direct and indirect prompt injection, disaggregated serving, distillation, distillation attack, distribution shift, dot product, double descent, doubling time, dpo, dropout, dual-use, dyt, early fusion, early stopping, elo rating, embedding, embedding table, encoder, endpoint, environment, epoch, error analysis, euclidean distance, euv lithography, eval, eval set, evals, evaluation, evaluation awareness, expert parallelism, exploding gradient, exploit, exponent, export controls, fair use, false positive, fast mode, fde, federated learning, feedback loop, fellowship, fine-tuning, first-party data, flashattention, floating point, floating-point number, flop, flop/s, flow matching, forecast, formal proof, forward pass, foundry, fp16, fp32, fp4, fp8, free cash flow, frontier model, ft, game theory, gan, gated attention, gaussian splatting, generalization, generative engine optimization, go-to-market, golden dataset, goodharts law, gpu, gpu kernel, gpu-hour, grader, gradient, gradient descent, gradual disempowerment, greedy decoding, gross margin, grounding, gtc, guidance scale, h100-equivalent, hai, hallucination, hard constraint, harness, hbm, hertz, hidden markov model, horizontal ai, http, human data, human-in-the-loop, hype cycle, hyperparameter, hyperscaler, imitation learning, imu, in-context learning, indirect prompt injection, induction head, inductive bias, inference, instruction set architecture, instruction-based editing, instrumental convergence, interconnection, interconnection queue, internet exchange point, interposer, inverse reinforcement learning, inverted index, it load, jagged frontier, jailbreak, jepa, jevons paradox, jpeg, json, json schema, kernel, kilowatt-hour, kl divergence, knowledge graph, kv cache, label, language model, large language model, late fusion, latency, latent space, layer, leaderboard, learning rate, learning-rate schedule, least privilege, lethal trifecta, letter of intent, liars dividend, library, license, linear function, linear regression, llm-as-judge, load balancer, local minimum, logarithmic scale, logic gate, logistic regression, logit, long tail, lora, loss function, loss landscape, loss spike, lost in the middle, lpu, lpx.

Notes on groups that were borderline but left as they are:
- **gpu-hour**: the prices differ but do not conflict. Ch 24 gives $7-9 for a B300, Ch 44 gives $6-9 for Blackwell-generation GPUs, and Ch 61 gives $6.69-6.99 for a Lambda B200. These match RunPod's B300 ($6.94-8.99) and Lambda's B200 list prices confirmed in freshness-part7 (https://lambda.ai/pricing, https://www.runpod.io/pricing).
- **hallucination** and **language model**: Ch 46's "(in speech recognition)" versions are the same concept applied to speech, so the merge is right.
- **hyperscaler**: Ch 4 (the glossary winner) names AWS, Azure and Google Cloud with "such as". Other chapters add Meta and Oracle. These are compatible.
- **dimension**: Ch 5 means the count of numbers in a vector. Ch 27 means one position in it and also gives the count reading. These are the two everyday uses of one word.
- **learning rate**: Ch 48's "(alpha)" is the tabular reinforcement-learning step size, the same idea as the gradient-descent step size.
- **data wall**: Ch 19 says "the point at which" supply runs out. Ch 11, 44 and 66 call it "the idea that" progress could stall. These are compatible.
- **dual-use**: Ch 53 adds the civilian-versus-military sense. The others use beneficial versus harmful. These are compatible.
- **frontier model**: Ch 24 includes Fable 5.1 in its list and Ch 44 omits it. Both match Anthropic's current model page.
- **fast mode**: Ch 26's $8 / $40 per MTok is twice Opus 5.5's $4 / $20 list price on the Anthropic models page. Ch 23 says "twice the standard rate". These agree.
- **kernel** (5 chapters) and **gpu kernel** (Ch 62, 65) mean the same thing but are separate keys, so they make two glossary entries. Merging them is outside the merge-key rule and was not done.

## Left as is or unresolved

- Ch 4:276 body text (not a definition) says 1 GW is "roughly enough electricity for 800,000 to a million US homes". It is hedged and compatible with the definitions, so it was left alone. Only definitions were changed in this round.
- The Ch 57 body text keeps saying "feature" and "features". Only the definition label changed, so that the glossary keeps Ch 8's input-feature sense under "Feature".
- `defgroups.py` reported 3,318 keys before this round and 3,327 after, because other agents are adding definitions in parallel. The after-run shows no new d to l groups except "learned feature".
