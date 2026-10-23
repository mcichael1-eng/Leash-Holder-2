# Code tests: every runnable code block in the chapters (October 23, 2026)

Scope: all 104 fenced `python` blocks in `chapters/*.md` (plus the one SPARQL query and the one-line inline snippets readers are told to run). Each block the reader is asked to run was executed exactly as printed, in fresh virtual environments, unless the table says otherwise. Main-text fragments that are only illustrations (for example Ch10's five-line scikit-learn sketch, Ch28's code-agent sketch, Ch29's `split_cost` test) were parse-checked and, where self-contained, run. All 104 blocks parse with Python 3.13 after the fixes.

## Test environment

- Colab's own published package list (googlecolab/backend-info, current main) shows Colab now runs **Python 3.13.16** on Ubuntu 24.04, not 3.12, with numpy 2.1.3, scipy 1.16.3, pandas 2.2.3, scikit-learn 1.6.1, matplotlib 3.10.0, torch 2.11.0, transformers 5.20.2, sentence-transformers 5.7.0, accelerate 1.15.0, peft 0.21.2, datasets 4.8.5, diffusers 0.41.0, tensorflow 2.21.0, keras 3.13.2. gensim, trl, anthropic, bertviz, ultralytics and openai-whisper are not preinstalled. The test venvs pinned exactly these versions (Python 3.13.16; torch CPU build).
- Packages the exercises install themselves were installed the way the exercise does it, which on October 23, 2026 gave: gensim 4.4.0, trl 1.16.0, anthropic 2.1.0 (sends API version 2026-10-21 and the key as `Authorization: Bearer`), openai 3.37.0, bertviz 1.4.1, ultralytics 8.4.184, openai-whisper 20250625.
- No GPU and no API keys here. GPU code was run with CUDA calls redirected to the CPU (logic and API check only; speeds meaningless). Anthropic code was run end to end against a local mock of the Messages API (`/v1/messages`, streaming, `count_tokens`, batches) that records each request, so every SDK call, argument and response field the book uses was exercised with the real SDK; request shapes were checked against Anthropic's current docs. `google.colab` (`files.upload`, `userdata.get`) was replaced by a small local stand-in.
- The sandbox proxy blocks api.github.com, so Ch4's GitHub call was tested against a local mock with GitHub's documented fields. Everything else that downloads (Hugging Face models, GloVe, MNIST, Shakespeare, Gutenberg, Open-Meteo, Wikidata, YOLO weights, Whisper weights) was fetched live.

## Results

| Chapter | Exercise | Ran? | Result | Fix |
|---|---|---|---|---|
| 2 | Ex 8, GPU beats CPU at matrix math | CPU stand-in | Runs; all calls exist in torch 2.11. Note: the CPU side multiplies 64-bit numbers and the GPU side 32-bit, so the speed-up is somewhat flattered (not changed). | None |
| 3 | Main-text snippets (variables, lists, loop, `tip`, `random.choices`) | Yes | Output matches the comments (72, 36, 144/176/190, 12.0) | None |
| 3 | Ex 1 inline `for ch in "José"` | Yes | é gives 233 and bytes [195, 169] | None |
| 3 | Ex 4 first program; `print(2 ** 20)` | Yes | Runs; 1,048,576 matches the binary-search number in the chapter | None |
| 3 | Ex 6 error snippets | Yes | SyntaxError (unterminated string literal), TypeError, NameError with "Did you mean: 'price'?" | None |
| 3 | Ex 8 image array | Yes | Prints (8, 8, 3) and [255 0 0] as the comments say | None |
| 3 | Ex 10 CSV to JSON (`files.upload`) | Yes (stub upload) | Comma inside "Portland, Oregon" handled; JSON printed | None |
| 4 | Ex 9 first API call (GitHub) | Mock (proxy blocks GitHub) | Fields verified in GitHub REST docs. Step 3 (nonexistent repo, 404) and any rate-limit 403/429 crashed with `KeyError: 'stargazers_count'` | Code now prints the fields only on status 200, otherwise GitHub's error message; step 2 now gives the documented limit (60 per hour per address) and what a 403/429 means. Retested on 200 and 404 |
| 5 | Ex 6 optional gensim analogies | Yes | Runs on Colab's stack with gensim 4.4.0: queen, tokyo, 0.77 / 0.21 | Install line now `"gensim>=4.4"` with a comment; result added |
| 5 | Ex 10 cubic cost (CPU) and GPU cell | Yes; GPU cell as CPU stand-in | Runs; roughly eightfold growth per doubling at larger n | None |
| 5 | Ex 11 rounding errors | Yes | FP16 pi 3.140625, FP16 total 256.0, FP32 total 999.9029: matches text | None |
| 6 | Ex 7 sampling and temperature | Yes | Runs; heads near 0.5; temperature behaves as described | None |
| 8 | "Your first model in code" Cells 1 and 2 | Yes | Exact match: loss 4,894 → 83.07 → 1.10 → 1.00; w 4.000, b 47.000; overshoot 16.5; 4/21/62/91/98%; weight 0.9, bias −4.01, boundary 4.47 | None |
| 8 | Try it (learning rates 0.002, 0.026) | Yes | 0.002 unfinished at step 2,000; 0.026 blows up | None |
| 8 | Ex 8 train and break models | Yes | Steps 2 and 4 claims match (clean labels: weight 1.18, boundary 4.49; later pass: 6.51). But step 4 after step 2 crashes: Cell 2 has 10 labels and Cell 1 now 11 students (`ValueError: inconsistent numbers of samples`) | Step 4 now tells the reader to restore the ten students in Cell 1 first, and why |
| 9 | Café overfitting cell; breast-cancer cell | Yes | Exact match with Tables 9.2 and 9.7, AUC 0.996, baseline 0.629, folds 0.982/0.982/0.974/0.974/0.991. Cell 2 uses `np` from Cell 1, as the text's "same notebook" instruction assumes | None |
| 9 | Ex 8 leakage trap | Yes | 0.454 defaults, 0.678 honest, 0.977 leaky: matches | None |
| 10 | Ex 6 two classical models | Yes | Baseline 0.63 with zero recall; LR 0.971 CV / 0.965 test; forest 0.958 / 0.974: matches text | None |
| 10 | Ex 8 PCA and k-means | Yes | 0.285 of variation; 0.792 in own-digit clusters: matches | None |
| 10 | Ex 9 tree depth and forest | Yes | Train 1.000 by depth 7, test 0.89 to 0.91, forest 0.953: matches | None |
| 11 | Ex 6 SQL in SQLite | Yes | coding 19,700; China 7,900: matches | None |
| 11 | Ex 9 model collapse | Yes | 0.016 and 0.867: exact match | None |
| 12 | Ex 10 XOR from scratch and experiments (a) to (c) | Yes | Loss 0.7195 → 0.0015; H = 1 stuck (0.478); no bend gives 0.6931 and all 0.5; lr 50 gives nan: all match | None |
| 13 | 15-line PyTorch script | Yes | Loss 2.2 → 0.06: matches | None |
| 13 | Complete Colab training script | Yes | Parameters 26,122 and every printed epoch line identical to the book's sample output | None |
| 13 | Ex 8 optimizer race (incl. `torch.optim.Muon`) | Yes | SGD 1.895, Momentum 0.139, Adam 0.235, AdamW 0.236, Muon 0.031: matches | None |
| 13 | Ex 9 residual vs plain 30-layer net | Yes | 0.00e+00 first-block gradient, 10% vs 93%: matches; about 4 s single-threaded | None |
| 14 | Ex 8 gensim word arithmetic | Yes, Colab-like venv | No NumPy/SciPy clash today: plain `pip install gensim` now gets gensim 4.4.0 (Oct 2025), which dropped the old `numpy<2` and `scipy<1.14` caps and ships Python 3.13 wheels; it leaves Colab's numpy 2.1.3 and scipy 1.16.3 alone. The clash existed with gensim 4.3.3 (numpy<2, no 3.13 wheel). Output: queen, tokyo, 0.77 / 0.21 | Install line pinned to `"gensim>=4.4"` and the exercise now says why; observed results added |
| 14 | Ex 9 MLP vs CNN (TensorFlow 2.21 / Keras 3.13) | Yes | 101,770 and 34,826 parameters: matches; test 0.975 vs 0.990; shifted 0.52 vs 0.89 | None |
| 15 | Ex 6 bertviz attention heads in GPT-2 | Yes | Runs; 12 layers of attention returned; view renders in a notebook | None |
| 16 | Ex 6 CLIP zero-shot | Yes (COCO cats photo) | "a photo of a cat" 0.74 | None |
| 16 | Ex 8 SDXL-Turbo | No (GPU, about 7 GB) | API smoke test with Hugging Face's tiny SDXL test pipeline on CPU: runs. diffusers 0.41 warns that `torch_dtype` is deprecated | Changed `torch_dtype=` to `dtype=` (tested, no warning) |
| 17 | Ex 8 MoE router | Yes | Loads [0 4 5 3 4 6 2 8], 4 dropped; after balancing 3 to 5 each, 0 dropped: matches | None |
| 18 | Ex 10 next-token probabilities (Qwen3-0.6B) | Yes | Runs; " Paris" 0.992 at T = 0.5. Download is 1.50 GB, not 1 GB | Size changed to "about 1.5 GB" |
| 19 | Ex 8 meet a base model | Yes | Runs. Base model writes more quiz questions; chat model (greedy, thinking off) answers "Osaka" in both bf16 and fp32; few-shot base model answers Tokyo. Downloads are 1.19 and 1.50 GB | Sizes corrected; observed results and a one-line explanation added to steps 1 and 3 |
| 19 | Ex 9 pretrain tiny Shakespeare model | Yes, CPU (6.4 min) | Loss 4.43 → 1.54; samples go from noise to Shakespeare-like lines; parameter count works out to 817,985 (book: about 818,000) | None |
| 20 | Ex 7 base vs chat | Yes | Same outputs as Ch19 Ex 8 (chat model says Osaka) | Observed result and explanation added |
| 20 | Ex 9 DPO (TRL 1.16) | Yes, CPU | Training ran and loss fell from 0.6931, but (1) the "trained" reply was garbage ("var API/API/API...") because the model is left in training mode after `trainer.train()`; `eval()` fixes it; (2) TRL warned that the plain-string pairs are trained without the chat template, while step 4 asks with the template; (3) transformers 5 loads the model in bf16 by default, so with lr 5e-6 almost every update rounded away, contradicting the "plain 32-bit math" comment | Load with `dtype="float32"`; pairs wrapped as chats in one added statement (reader still writes plain pairs); `trainer.model.eval()` added to the second block; prose updated. Retested exactly as printed: no warning, loss 0.69 → ~0, sensible trained reply |
| 21 | Ex 8 GRPO (TRL 1.16) | 2 steps on CPU (80 on a GPU) | API valid; reward logged (0.25, 0.375); model loads in fp32 by TRL default, so the bf16 comment is right. Step 4's `num_generations=16` with batch 8 stops: "generation_batch_size (8) must be divisible by num_generations (16)" | Step 4 now says to raise `per_device_train_batch_size` to 16 with 16 generations |
| 22 | Ex 7 CLIP | Yes | Same as Ch16 Ex 6 | None |
| 22 | Ex 10 image-token calculator | Yes | 1,333 / 765 / 1,296 for 1,000-pixel and 1,008-pixel images: consistent with Table 22.2 | None |
| 23 | Ex 8 speculative decoding table | Yes | α 0.8, k 4 gives 2.40, consistent with the 3.36-token worked example | None |
| 26 | Steps 4 to 6 walkthrough, history, OpenAI cell, streaming, caching, structured output, image, error handling | Mock API (no key) | All calls valid with anthropic 2.1.0: `output_config={"effort": ...}`, JSON-schema `format`, `system` blocks with `cache_control`, `messages.stream(...).text_stream`, `to_json()`, usage fields. No removed parameters (`temperature`, `top_p`, `top_k`) and no prefill anywhere. Prices in code match Anthropic's ($4/$20 Opus 5.5, $2/$10 Sonnet 5.5, $0.10/$0.50 Haiku 5.5). OpenAI cell: `responses.create(model, instructions, input, max_output_tokens)` and `output_text` exist in openai 3.37 (model ID not testable without a key) | None |
| 26 | Ex 4 to 10 (stateless, `count_tokens`, streaming stopwatch with `get_final_message()`, extraction table, caching lab, batches with `Request` / `MessageCreateParamsNonStreaming`, blind test) | Mock API | All run end to end; Gutenberg download works; batch results matched by `custom_id` | None |
| 27 | Ex 8 mini-RAG (cells 2 to 7), no key and with key | Yes (embeddings live; Claude via mock) | 12 chunks, 384-number vectors; compost question retrieves S5/S6; first question needs S1 and S2 as the text says; flood question gets low scores | None |
| 27 | Ex 9 golden set and Experiments A and B | Yes | recall@1 8/8, recall@3 8/8; Experiment A gives 7/8 exactly as the book says; B gives 6/8 | None |
| 28 | Ex 8 agent loop with Open-Meteo | Yes (Claude via mock, weather live) | Tool call, result and loop work; calculator rejects non-arithmetic; unknown place gives the helpful error. Note: "Lisbonn" geocodes to Lisbonne, Belgium rather than failing, a useful surprise for step 4 | None |
| 29 | `split_cost` and its test | Yes | Test passes | None |
| 30 | Ex 8 QLoRA walkthrough (9 cells) and Ex 9 fair test | CPU adaptation (4-bit, fp16 and paged 8-bit Adam need a CUDA GPU) | With Qwen3-0.6B-Base unquantized on CPU the whole pipeline runs: base model emits digit strings as predicted; loss 2.88 → 0.28; cards correct after training; 29/30 fine-tuned vs 18/30 few-shot. `BitsAndBytesConfig` arguments and `paged_adamw_8bit` exist in transformers 5.20; `disable_adapter()` exists in peft 0.21. Book's numbers for Qwen3-1.7B-Base check out by arithmetic from its config: 17,432,576 trainable parameters, 3.44 GB download, about 3.4 GB at 16 bits, about 70 MB adapter | None |
| 30 | Ex 10 Ollama `ask.py` | Mock Ollama server | Runs; response shape and the `gemma4:e2b` tag confirmed in Ollama's docs and library page | None |
| 31 | Ex 10 automated eval | Mock API | Runs end to end, prints pass rates and writes the CSV | None |
| 32 | Ex 1 `nvidia-smi` cells | No (GPU only) | Query fields are standard `nvidia-smi --query-gpu` names | None |
| 32 | Ex 1 step 6 TFLOPS cell; Ex 5 CPU vs GPU, FP32 vs FP16 | CPU stand-in | Logic and calls valid; T4 reference figures (8.1 / 65 TFLOPS) consistent | None |
| 33 | Ex 5 roofline sweep | CPU stand-in | Valid; intensity formula gives about 819 FLOP/byte at batch 1,024, past the 203 ridge the text cites | None |
| 35 | Ex 3 first GPU multiply | CPU stand-in | Valid | None |
| 45 | Ex 9 YOLO11n on bus.jpg | Yes | bus 0.94 and four persons; `conf=0.7` / `0.2` work; boxes image converts | None |
| 46 | Ex 8 Whisper "base" | Yes (Whisper's JFK test clip via stub upload) | Correct transcript and segment times | None |
| 48 | Ex 6 Q-learning grid | Yes | Start value 1.81: matches the hand calculation | None |
| 51 | Ex 9 matrix factorization | Yes | RMSE 3.16 → 0.030; blanks filled as described; Ana about 2.4/0.2 and Alien about 2.1/0.3; seed 1 gives near-identical predictions: matches | None |
| 54 | Ex 2 SPARQL on query.wikidata.org | Yes | Q142 Paris, Q183 Berlin, Q17 Tokyo | None |
| 54 | Ex 6 genetic algorithm backpack | Yes, 20 runs | Optimum 30 confirmed by brute force; found in 17 of 20 runs (28 otherwise), as the "sometimes stalls" text expects | None |

## Fixes made (all re-run after editing)

1. **Ch4 Ex 9:** GitHub code no longer crashes on a 404 or a rate-limit response; step 2 states the 60-per-hour limit and the 403/429 case.
2. **Ch5 Ex 6 and Ch14 Ex 8:** `!pip install -q "gensim>=4.4"`; Ch14 explains why (first version for NumPy 2 and Python 3.13, which Colab now runs); both give the observed answers.
3. **Ch8 Ex 8 step 4:** restore the ten students before changing Cell 2, avoiding the length-mismatch error.
4. **Ch16 Ex 8:** `dtype=` instead of the deprecated `torch_dtype=`.
5. **Ch18 Ex 10 and Ch19 Ex 8:** download sizes corrected (1.5 GB; 1.2 and 1.5 GB).
6. **Ch19 Ex 8 and Ch20 Ex 7:** say what readers will actually see (the small chat model answers "Osaka"; the few-shot base model gets Tokyo) and why.
7. **Ch20 Ex 9 (DPO):** fp32 load, pairs wrapped as chats, `trainer.model.eval()` before generating; prose updated.
8. **Ch21 Ex 8 step 4:** 16 generations need a batch of 16.

Validators: `validate.py` and `check.py` clean on chapters 4, 5, 8, 14, 16, 18, 19, 20 and 21.

## Not run, or only partly

- GPU-only work (Ch2 Ex 8, Ch5 Ex 10 step 3, Ch16 Ex 8, Ch30 Ex 8 and 9 in 4-bit, Ch32, Ch33, Ch35): logic run on CPU, library calls checked; real speeds, T4 memory fit and bitsandbytes 4-bit loading were not tested. The DPO run now loads in fp32: about 10 to 12 GB on a T4 by estimate, within its 15 GB, not measured.
- No live call to Anthropic or OpenAI (no keys): request shapes and SDK calls were tested against a mock and the docs; model IDs `claude-*-5-5` match Anthropic's current list, `gpt-6.1-sol` was not checked here.
- api.github.com could not be reached from this sandbox; Ch4's code was tested against a mock built from GitHub's documented fields.
- Ch21 GRPO ran 2 of its 80 steps on CPU (48 s per step); whether reward clearly rises over 80 steps was not observed.

## Sources

- Colab runtime and package versions: https://github.com/googlecolab/backend-info/blob/main/os-info.txt ; https://raw.githubusercontent.com/googlecolab/backend-info/main/pip-freeze.txt
- gensim requirements and wheels: https://pypi.org/pypi/gensim/4.3.3/json ; https://pypi.org/pypi/gensim/4.4.0/json
- GitHub REST: https://docs.github.com/en/rest/repos/repos#get-a-repository ; https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api
- Anthropic SDK 2.0 and API version 2026-10-21: https://platform.claude.com/docs/en/api/migration-2026-10-21 ; model IDs, effort, structured outputs, caching, batches and prices from Anthropic's current API reference (claude-api reference, cached 2026-10-06) and https://platform.claude.com/docs/en/about-claude/pricing (as confirmed in freshness-part4.md)
- Ollama: https://docs.ollama.com/api/chat ; https://ollama.com/library/gemma4
- Hugging Face model files and configs: https://huggingface.co/api/models/Qwen/Qwen3-0.6B ; https://huggingface.co/api/models/Qwen/Qwen3-0.6B-Base ; https://huggingface.co/api/models/Qwen/Qwen2.5-0.5B-Instruct ; https://huggingface.co/api/models/Qwen/Qwen3-1.7B-Base ; https://huggingface.co/Qwen/Qwen3-1.7B-Base/raw/main/config.json ; https://huggingface.co/api/models/stabilityai/sdxl-turbo ; https://huggingface.co/hf-internal-testing/tiny-stable-diffusion-xl-pipe
- Library versions: https://pypi.org/pypi/{transformers,peft,trl,datasets,diffusers,bitsandbytes,accelerate}/json
- Live data used by exercises: https://query.wikidata.org/sparql ; https://geocoding-api.open-meteo.com/v1/search ; https://api.open-meteo.com/v1/forecast ; https://www.gutenberg.org/cache/epub/1342/pg1342.txt ; https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt ; https://raw.githubusercontent.com/openai/whisper/main/tests/jfk.flac

Test scripts, stand-ins and outputs: `S/codetest2/` (blocks, cpuver, mock, out).
