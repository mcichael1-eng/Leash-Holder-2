# Reader test: chapters 13, 14, 16 and 17

Tested by reading chapters 13, 14, 16 and 17 in order, in full, as the intended reader: almost no computer-science background, a daily chatbot user for a year, who has read the earlier chapters. Chapters 12 and 15 were tested in the first pass (see reader-test.md). Before treating a term as undefined I checked GLOSSARY.md and the earlier chapters. I also worked through every entry for these chapters in acronyms-by-chapter.json.

Every worked number in the four chapters was recomputed: the momentum table, the cosine and WSD schedule values, layer and RMS normalization, the Xavier and He spreads, the parameter counts of both PyTorch scripts and both Keras models, the RNN fade, the LSTM gate, both attention softmaxes, cosine similarity, the diffusion pixel forward and back, the guidance, latent and video token counts, the MoE routing, the KV-cache table, the GNN rounds, QK-norm and DyT, and every exercise and check-your-understanding answer. I found no arithmetic errors. I also ran the Chapter 17 MoE router code (Exercise 8). Its output matches the text exactly: first load [0 4 5 3 4 6 2 8] with 4 dropped, then 3 to 5 per expert and none dropped after balancing.

After editing, every edited file passed `validate.py` (30/30 diagrams valid) and `check.py` (chapters 13, 14, 16 and 17 all `[OK]`).

## Findings and fixes

| Chapter | Where | Problem a beginner would hit | Fix applied |
|---|---|---|---|
| 13 | Why deep networks are hard to train, problem 2 | "loss = NaN" appears 200 lines before NaN is defined | Added a gloss: "not a number", the computer's sign that its arithmetic has broken down |
| 13 | Beyond Adam: Lion | "Uses only the *sign*": the mathematical meaning of sign is not obvious | Added "(whether it is positive or negative, ignoring its size)" |
| 13 | Muon results, first bullet | NanoGPT "speedrun", CIFAR-10 and A100 were all unexplained (CIFAR is in the acronym list) | Glossed all three: a public training race, the 60,000-photo ten-class dataset, and NVIDIA's 2020 data-center GPU |
| 13 | Loss spikes | "Google's PaLM paper" was never introduced | Added that it describes a 540-billion-parameter language model |
| 13 | Loss spikes, QK-norm | "Queries and keys inside attention" are Chapter 15 material, and QK is in the acronym list | Added one bridging sentence on what queries and keys are and why big ones make scores explode |
| 13 | Xavier initialization | √(2 ÷ 1,024) appeared with no rule and no explanation of where 1,024 comes from | Stated the rule √(2 ÷ (inputs + outputs)) and the sum 512 + 512 = 1,024 |
| 13 | Double descent, grokking | "NeurIPS" was not explained | Glossed it as the largest yearly AI research conference |
| 13 | RMSNorm | The acronym RMS (used again in Exercise 6) was never tied to "root-mean-square" | Added "or RMS" |
| 13 | Normalization placement | "Sub-layer" was undefined (Transformer blocks are Chapter 15) | Said the sub-layers are the attention and feed-forward parts, pointing to Figure 13.8 |
| 13 | Normalization placement, DyT | CVPR (acronym list) was unexplained, and α was used with no explanation | Glossed CVPR as the leading computer-vision conference, and α as the Greek letter alpha, a learned number |
| 13 | Framework table | "Functional style" and "graph-based" are programmer jargon | Added a short gloss in each cell |
| 13 | Colab script, Part 2 | The `lambda` line was the only code line with no comment | Added the comment "helper: array -> tensor" |
| 13 | 2026 recipe table | SwiGLU appears before Chapter 15 defines it | Added a pointer to Chapter 15 |
| 13 | Areas of opportunity | AMD was used with no definition anywhere in the book (22 chapters use it) | New definition callout: AMD (Advanced Micro Devices), placed after the list as in Chapter 59, and added to Key terms |
| 13 | Exercise 7, step 2 | "Remove both `nn.ReLU()` entries" invites leaving a stray comma, which is a syntax error | The step now says to delete `nn.ReLU(),` together with its comma |
| 13 | Exercise 7, step 3 | "Fix the matching numbers" did not say which three lines change, or to what | Gave the three exact new lines |
| 13 | Exercise 8 | "Multiply and divide each learning rate by 10" did not say where the rates are, and `1e-3` notation was unexplained | Pointed to the `lr=` values in `make_optimizers` and showed 1e-3 → 1e-2 / 1e-4 |
| 14 | 1-D convolution | "Sentiment analysis" was not glossed in this chapter | Glossed it as judging whether a review is positive or negative |
| 14 | 3-D convolution | CT (acronym list) was unexplained | Glossed it as computed tomography, which X-rays the body in thin slices |
| 14 | A whole CNN | "TinyVGG" appears 60 lines before VGG is introduced | Added "a miniature of the VGG design described later in this chapter" |
| 14 | Looking inside a trained CNN | Grad-CAM (CAM is in the acronym list) was not expanded | Expanded it to gradient-weighted class activation mapping |
| 14 | VGG, GoogLeNet | VGG (acronym list) was never explained | Glossed it as Oxford's Visual Geometry Group |
| 14 | Transfer learning, Key idea | "Foundation models" is used here, and no chapter in the book defines the term | New definition callout: Foundation model (added to Key terms) |
| 14 | Exercise 4, step 4 | Typing 1/9 into Sheets or Excel turns it into a date, so the blur filter breaks | The step now says to type `=1/9` and explains why |
| 14 | Exercise 5, step 4 | Changing "0.8 to 0.95" only edits C2 unless the formula is copied down again. With 1.5, tanh caps the memory near 0.86, so the promised "blow up" never appears | Said to edit the formula and copy it down again. Explained what 1.5 actually shows (the forward value is capped; the backward signal explodes) and adjusted the "What you'll learn" line to match |
| 14 | Exercise 6, step 1 | "Compute e to each score" gave no way to do it | Added the calculator e^x key and `=EXP(0.3)` |
| 16 | Self-supervised learning | "Masked autoencoders" appear before autoencoders are explained | Added a pointer to later in the chapter |
| 16 | VAE worked example | "The standard bell curve" was not explained | Glossed it as centered on 0 with a spread of 1, the shape the second loss term pulls toward |
| 16 | Autoregressive image generation | VQ (acronym list) was not expanded | Glossed VQ as "vector quantized", with what that means |
| 16 | Same paragraph | DALL·E (5 chapters, no definition anywhere) | New definition callout: DALL·E (added to Key terms) |
| 16 | Diffusion, opening | DDPM is used 115 lines before it is expanded | Expanded it at first use |
| 16 | Forward process formula | "sqrt" written as a word, not the √ the reader has seen | Added "writing sqrt for 'the square root of'" |
| 16 | Samplers | DPM-Solver (DPM is in the acronym list) was not expanded | Glossed DPM as diffusion probabilistic model |
| 16 | Distillation | SDXL-Turbo (acronym list) and Stability AI were not introduced | Glossed Stability AI as the company behind Stable Diffusion, and SDXL-Turbo as a fast version of Stable Diffusion XL |
| 16 | LoRA | "Rank-8" was unexplained, and so was how two thin matrices become a change to a 4,096 × 4,096 matrix | Said the rank is the thin side, and that multiplying the two (Chapter 5) gives the full grid of changes |
| 16 | World models | "720p" was unexplained | Glossed it as frames 720 pixels tall, standard HD |
| 16 | Exercise 9 | "Simulate generation with 1, 2, 4 and 10 steps" gave a non-programmer no worked first step and no spreadsheet layout | Worked the 2-step curved case (error 1.0) and suggested the column layout |
| 17 | MoE worked example, training compute | The 6 × N × D rule comes from Chapter 19, two chapters later, and "49e9" notation was unexplained | Added why it is 6 (2 forward plus about 4 backward) and what 49e9 means |
| 17 | Auxiliary-loss-free balancing | "E3 about 0.71 and E8 about 0.29" with no reason given | Showed it is a softmax over the original scores 2.0 and 1.1, with both exponentials |
| 17 | Mamba-3 | ICLR (acronym list) was unexplained | Glossed it as a major machine-learning research conference |
| 17 | Linear attention | `value × keyᵀ` and `S × q` assume transposes and outer products | Added one sentence on what ᵀ means and how the grid is built |
| 17 | Hybrid architectures | AI21 Labs (acronym list) was unexplained | Glossed it as an Israeli AI company |
| 17 | Counter-trend | MiniMax was not introduced | Glossed it as a Chinese AI company |
| 17 | Table 17.4 | "mLSTM" was undefined | Glossed it as xLSTM's memory layer |
| 17 | Exercise 2 | No way given to compute e^2.1 | Added the calculator e^x key and `=EXP(2.1)` |
| 17 | Exercise 3 | The second part (add the Ana–Dee edge) had no answer to check against | Added the expected round-1 values (4.5, 6, 4.5, 5) |
| 17 | Exercise 6 | "Add `value × keyᵀ`" with pencil and paper is impossible for someone who has never met an outer product | Gave the 2 × 2 grid rule, an example and the read-out rule (checked: it reproduces both expected answers) |

Fixes per chapter: 13: 17 (11 undefined terms, 3 beginner jumps, 3 exercises); 14: 9 (6 terms, 3 exercises); 16: 11 (7 terms, 3 jumps, 1 exercise); 17: 10 (4 terms, 3 jumps, 3 exercises). That is 47 in total. Three new definition callouts were added, each also added to its chapter's Key terms list: AMD (Chapter 13), Foundation model (Chapter 14) and DALL·E (Chapter 16).

## Acronym list: entries not changed, and why

- **NVIDIA** (all four chapters): while this pass was running, another agent added a definition in Chapter 3. That chapter comes before mine, so I did not add a duplicate.
- **AMD**: I defined it in Chapter 13 as the brief requires. Other agents also added AMD definitions in Chapters 30, 34 and 38 during this pass. The glossary merges them, so nothing is lost. The owner of Chapters 2 and 7, where AMD first appears, may want one there too.
- **DJ** (Chapter 13, the volume-leveler analogy): everyday English, so I left it.
- **SNE** (Chapter 14): t-SNE is defined in Chapter 10 and glossed again in Exercise 7.
- **GTX** (Chapter 14): already glossed by its sentence ("two NVIDIA GTX 580 gaming graphics cards").
- **RBM** (Chapter 16): already expanded in the text and covered by the Boltzmann machine definition.
- **UNTIL, PASTE, ANY, HERE** (Chapter 16): false positives. They come from the "OPEN UNTIL 9 PM" sign prompt and the `PASTE_ANY_IMAGE_URL_HERE` placeholder.
- **QK** (Chapter 17): QK-norm has its own definition in Chapter 17, and I also glossed it at its first use in Chapter 13.

## Noticed but not changed

- Chapter 13's optional "At the frontier" boxes use "expert weights", "gated attention" and "multi-token prediction" before Chapter 17 covers them. Mixture of experts is defined back in Chapter 5, and these are asides, so I left them.
- Chapter 14's U-Net definition calls it an "encoder-decoder" CNN about 200 lines before encoder and decoder are defined. The paragraph just before it explains the down path and up path, so I left it.
- Chapter 14, Exercise 8 (gensim in Colab) was not run here. gensim has at times pinned an older NumPy than the one Colab ships, which can force a runtime restart after the install. It is worth one test run by whoever owns the exercises.
- Sourced 2025–2026 facts (model sizes, release dates, Sora's shutdown, best-paper awards and similar) were not checked, as the brief instructs.
- Another agent was editing these chapters at the same time; one edit to Chapter 16 reported that the file had changed on disk. I re-read every target passage before editing, and all edits landed on the current text without duplicates.

## Verdicts

**Chapter 13 (Training Deep Networks).** The ramp works well. The chapter opens from Chapter 12's loop and names five problems, and each trick is then motivated by one of them and worked with real numbers: momentum step by step, Adam's division, the schedule table, normalization by hand, the tent function for depth. The friction came from three places. Some terms belong to Chapter 15 (queries and keys, sub-layers, SwiGLU). Some names were dropped without introduction (CIFAR-10, A100, PaLM, NeurIPS, CVPR). And the Colab exercise edits could break the code of someone who has never programmed. With the fixes, every term is defined in this chapter, defined earlier (NVIDIA in Chapter 3, SGD and autograd in Chapters 6 and 12) or glossed where it is used. The two scripts are fully explained and their parameter counts are correct.

**Chapter 14 (CNNs, RNNs, Embeddings).** This is the gentlest of the four and the ramp is excellent. Convolution, pooling, receptive fields, the RNN's fading memory, the LSTM gate, Bahdanau attention and cosine similarity are all done by hand with small numbers. Then the chapter climbs into history and sets up Chapter 15 cleanly. The problems were architecture acronyms (VGG, CT, Grad-CAM) and spreadsheet traps: 1/9 turning into a date, editing one cell instead of the whole column, and an exercise setting that could not show what its "What you'll learn" line promised. "Foundation model" was used without a definition anywhere in the book, and is now defined here. Every term is now defined.

**Chapter 16 (Generative Models).** The ramp is strong. It moves from "what is a distribution" through latent space, autoencoders, VAEs and GANs to diffusion, and follows one pixel through noising, noise prediction and denoising. Each newer method is presented as fixing the last one's weakness. The steep spots were VAE sampling (an unexplained "standard bell curve"), "sqrt" notation, LoRA's "rank-8" with no account of how two thin matrices make a full-size change, and a cluster of acronyms (DDPM 115 lines before its expansion, VQ, DPM, SDXL, DALL·E). All are now explained, and DALL·E has a definition. The diffusion-language-model and world-model sections are brief previews that point onward correctly (Chapters 22, 47 and 49).

**Chapter 17 (Beyond the Transformer).** This is the densest chapter, and it really does depend on Chapter 15 (KV cache, GQA, MLA, queries and keys). The hand-routed MoE token is one of the best worked examples in the book, and the GNN gossip example and the delta-rule example are clear. The jumps were the 6 × N × D rule borrowed from Chapter 19, "49e9" notation, the transposed key and outer product behind linear attention (worst in Exercise 6, which a beginner could not do as written), and the unexplained gating numbers in the bias-balancing example. Company names (AI21 Labs, MiniMax) are now glossed. The frontier tables are dense but read as reference rather than as required learning. With the fixes, every term is defined or glossed. A reader who finished Chapter 15 can follow the whole chapter with a calculator.
