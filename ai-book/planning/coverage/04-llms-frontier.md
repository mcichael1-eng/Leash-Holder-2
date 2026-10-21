# Coverage report: 04-llms-frontier.md (topic map, section 1)

Audited October 21, 2026 against `ai-book/chapters/`. Each item was located by searching for its key terms (and every named sub-item), then reading the passage. "COVERED" means explained at beginner level, not just mentioned.

| Item | Status before | Where covered (chapter and section) | Action taken |
|---|---|---|---|
| A1. App vs. model vs. API | COVERED | Ch 18 "The app, the model and the API" (Figure 18.1); Ch 25; Ch 26 | None |
| A2. Next-token prediction | COVERED | Ch 18 "The one trick: predicting the next token"; Ch 15 Step 10 | None |
| A3. Tokens and tokenizers (BPE, vocab size, non-English and code cost, letter counting, priced in tokens, tokenizer changes) | THIN | Ch 18 "Tokens: the pieces a model reads" (BPE by hand, vocab sizes, letter counting, other languages, prices, Opus 4.7 tokenizer 555K words); Ch 15 Step 1. The "code can cost more tokens" sub-item was not explained | Added a "Code can cost more, too" paragraph to Ch 18 "What tokens explain about your chatbot" (hedged: depends on the tokenizer) |
| A4. Probabilities and sampling (logits, softmax, greedy, temperature, top-k/top-p/min-p, temperature 0) | COVERED | Ch 18 "From scores to words: logits, softmax and sampling" incl. "Why temperature 0 is still not perfectly repeatable"; Ch 6 | None |
| A5. Context window (1M frontier, output limit, cost, lost in the middle) | COVERED | Ch 18 "The context window: the model's desk" (128K output limit, worked cost example, lost in the middle); Ch 15 "Stretching the context window" | None |
| A6. Chat templates, roles, system prompts, instruction hierarchy, prompt injection | COVERED | Ch 18 "Chat templates, roles and system prompts"; Ch 31 and Ch 58 for injection depth | None |
| A7. Parameters and weights (memory, total vs active) | COVERED | Ch 18 "Parameters: what a 70B model means" (memory math, compute per token, dense vs MoE) | None |
| B8. Neural networks in one page | COVERED | Ch 12 (full treatment) and Ch 6; Ch 18 "Before you start" points there | None |
| B9. Embeddings | COVERED | Ch 14 "Embeddings"; Ch 15 Step 2; Ch 18 "Inside the box in one page" | None |
| B10. The Transformer (Transformer Explainer, LLM Visualization) | COVERED | Ch 15 (whole chapter); Ch 18 "Inside the box in one page" (Figure 18.8) and exercises | None |
| B11. Attention, intuitively; causal masking | COVERED | Ch 15 Step 4 and Step 8; Ch 18 recap | None |
| B12. Position information (RoPE, YaRN) | COVERED | Ch 15 Step 3 (RoPE worked, YaRN context extension); Ch 23 "Long context" | None |
| C13. Where pretraining data comes from (sources; 15.6T, about 33T) | COVERED | Ch 19 "Where the data comes from" ("The sources", "How much?", opt-outs); Ch 11 | None |
| C14. Curation pipeline | COVERED | Ch 19 "Cleaning the firehose: the curation pipeline" (extraction, language ID, exact and MinHash dedup, heuristic and model-based filters, PII/toxicity, decontamination) | None |
| C15. Data mixtures (proxy models, curriculum, annealing) | THIN | Ch 19 "Choosing the recipe: data mixtures" (Llama 3 mix, upsampling, proxy models, ablations); annealing in "Mid-training and annealing". "Curriculum" was never named or explained | Added a curriculum paragraph, a "Curriculum (training curriculum)" definition and a Key terms entry to Ch 19 "Choosing the recipe" |
| C16. The pretraining run (scale, batch size, LR schedule, checkpoints, spikes, parallelism, MFU, low precision) | COVERED | Ch 19 "The pretraining run" (The machine, The settings, Watching the loss, Things break, Fewer bits); Ch 37 | None |
| C17. What a base model is like | COVERED | Ch 19 "What comes out: meet the base model"; Ch 20 "What a base model actually does" | None |
| D18. Scaling laws (Kaplan 2020) | COVERED | Ch 19 "Kaplan 2020: loss falls on a straight line" | None |
| D19. Chinchilla (about 20 tokens per parameter) | COVERED | Ch 19 "Chinchilla 2022: feed the model more data" | None |
| D20. Over-training and inference-aware scaling | COVERED | Ch 19 "Over-training: why labs train small models far past optimal" (Llama 3 8B about 1,900 tokens/parameter) | None |
| D21. The 6ND rule | COVERED | Ch 19 "The 6ND rule and what a training run costs" (with dollars); Ch 24 worked example; Ch 37 | None |
| D22. Emergent-abilities debate | COVERED | Ch 19 "Emergent abilities" (Wei et al., Schaeffer et al., today's view) | None |
| D23. Compute and cost trends; data wall | COVERED | Ch 19 "Compute and cost trends" (Epoch 5×/yr, 3.5×/yr) and "The data wall and how labs climb it" | None |
| E24. Mid-training | COVERED | Ch 19 "Mid-training and annealing" (OLMo 2) | None |
| F25. SFT / instruction tuning | COVERED | Ch 20 "Stage 1: Supervised fine-tuning" (worked one-token SFT step) | None |
| F26. Preference data | COVERED | Ch 20 "Stage 2: Preference data" | None |
| F27. Reward models | COVERED | Ch 20 "Reward models: teaching a judge to score" (worked) | None |
| F28. RLHF with PPO and the KL leash | COVERED | Ch 20 "Stage 3: RLHF" (toy example, KL leash, PPO, InstructGPT) | None |
| F29. DPO and variants (IPO, KTO, ORPO, SimPO) | COVERED | Ch 20 "DPO and its cousins" (worked DPO pair) | None |
| F30. RLAIF, Constitutional AI, model specs and constitutions | COVERED | Ch 20 "RLAIF and Constitutional AI", "Model specs and constitutions"; Ch 56 | None |
| F31. Safety training (refusal calibration, deliberative alignment, classifiers) | COVERED | Ch 20 "Safety training"; Ch 56 | None |
| F32. Failure modes (sycophancy and GPT-4o rollback, reward hacking, verbosity, over-refusal) | COVERED | Ch 20 "When feedback training goes wrong"; Ch 18; Ch 55 | None |
| G33. Chain-of-thought prompting and self-consistency | COVERED | Ch 21 "Step 1: Chain-of-thought prompting" and "Self-consistency" | None |
| G34. Test-time compute (log-linear) | COVERED | Ch 21 "Test-time compute: a second scaling law" (log-linear definition, worked cost) | None |
| G35. RL with verifiable rewards | COVERED | Ch 21 "Reinforcement learning with verifiable rewards" (worked reward function and how to break it) | None |
| G36. GRPO and variants (DAPO, Dr. GRPO, GSPO) | COVERED | Ch 21 "GRPO: grading on a curve" (group-of-eight worked example, family) | None |
| G37. The DeepSeek-R1 story | COVERED | Ch 21 "The DeepSeek-R1 story" (R1-Zero, aha moment, cold start, distillation) | None |
| G38. Process vs outcome rewards | COVERED | Ch 21 "Process versus outcome rewards" | None |
| G39. RL environments, industry, rubrics and LLM-as-judge | COVERED | Ch 21 "Beyond math and code: RL environments" (gym, industry, rubrics and AI judges) | None |
| G40. Product forms of reasoning across labs | COVERED | Ch 21 "How reasoning shows up in the products you use" (history, lab by lab, effort settings) | None |
| G41. Parallel thinking, agents, compaction | COVERED | Ch 21 "Thinking wider" (best-of-N worked, parallel modes, agent swarms, GPT-6 Pro hedged) and "Thinking longer: compaction" | None |
| G42. CoT faithfulness and monitorability (recurrent depth report) | COVERED | Ch 21 "Can we trust the thinking?" (unconfirmed report hedged); Ch 57 | None |
| H43. Distillation (on-policy, illicit API distillation, countermeasures) | COVERED | Ch 20 "Distillation: big teachers, small students" and "Illicit distillation and countermeasures"; Ch 24 | None |
| H44. Synthetic data and self-play (STaR, rejection sampling, model collapse) | COVERED | Ch 20 "Synthetic data and self-improvement"; Ch 19 data wall; Ch 11 model collapse | None |
| H45. Fine-tuning for everyone (full vs LoRA/QLoRA, APIs) | COVERED | Ch 20 "Fine-tuning for everyone"; Ch 30 (LoRA/QLoRA, hosted fine-tuning services) | None |
| H46. Model merging (soups, task arithmetic, TIES) | COVERED | Ch 20 "Model merging" (worked averaging example) | None |
| H47. Quantization (FP8 → INT4 → FP4, PTQ vs QAT, Gemma 4, Kimi K3) | COVERED | Ch 23 "Quantization: fewer bits per number" (worked 4-bit rounding); Ch 30; Ch 32 | None |
| I48. Mixture of experts (V4-Pro, Kimi K3, Qwen3.8) | COVERED | Ch 17 "Mixture of experts"; Ch 18 "Dense versus mixture of experts"; Ch 24 open-weight table | None |
| I49. Long-context techniques and evals (NIAH, RULER, GraphWalks) | COVERED | Ch 23 "Long context: making a million tokens affordable"; Ch 15; Ch 17; Ch 24 zoo | None |
| I50. Multi-token prediction and other tweaks (mHC) | COVERED | Ch 15 Step 10; Ch 17 "Recursion, memory and small models" and "Keeping giants stable"; Ch 23 speculative decoding | None |
| I51. Multimodality (vision encoders, audio tokenizers, native omni, image/video generation) | COVERED | Ch 22 (patches, vision encoder, projector, hearing, cascade vs omni, "Models that draw") | None |
| J52. Prefill vs decode | COVERED | Ch 23 "Two different jobs: prefill and decode" (two worked examples) | None |
| J53. KV cache and prompt caching | COVERED | Ch 23 "The KV cache" (memory worked by hand, prompt caching) | None |
| J54. Batching, continuous batching, PagedAttention | COVERED | Ch 23 "Serving many people at once: batching" | None |
| J55. Speculative decoding | COVERED | Ch 23 "Speculative decoding: guess ahead, check in one pass" | None |
| J56. Quantized serving, disaggregation, routing, fast modes, batch APIs and prices | COVERED | Ch 23 "Splitting the work" and "How it all shows up in your bill" (Table 23.5, fast mode 2×, batch discounts) | None |
| J57. Latency vs throughput vs cost | COVERED | Ch 23 "Measuring speed: latency, throughput and cost" | None |
| K58. Hallucination (Kalai et al. 2025, mitigations) | COVERED | Ch 18 "Hallucination: fluent, confident and false" (three causes, worked scoring example, grounding, citations, calibration, abstention) | None |
| K59. Sycophancy, over-refusal, prompt injection, jailbreaks | COVERED | Ch 18 "When it goes wrong" and "System prompts and the instruction hierarchy"; Ch 31; Ch 58 | None |
| L60. Why benchmarks exist and how they die (ARC-AGI-3 harness) | COVERED | Ch 24 "How benchmarks die" (saturation, contamination, Goodhart, ARC-AGI-3 62.7% vs 99.9%) | None |
| L61. The benchmark zoo | COVERED | Ch 24 "The benchmark zoo" (all named benchmarks and indices) | None |
| L62. Model cards and system cards | COVERED | Ch 24 "How to read a model card or system card" (worked reading of Opus 5.5) | None |
| M63. Open-weight vs closed, licenses, the gap | COVERED | Ch 24 "Open weights, closed weights and licenses" (revenue-threshold license, gap, debate); Ch 30 | None |
| M64. Who's who in late 2026 | COVERED | Ch 24 "Who's who in late 2026" (each lab plus "Decoding model names") | None |
| M65. Tiered and trusted access | COVERED | Ch 24 "Tiered and trusted access" (Mythos, cyber variants, fallback arithmetic); Ch 56 | None |
| M66. How labs are organized | COVERED | Ch 24 "How frontier labs are organized" (Figure 24.8); Ch 61 | None |
| M67. Training cost estimates | COVERED | Ch 24 "What a frontier model costs to train" (Epoch table, three worked examples, trend) | None |
| N68. Features and superposition | COVERED | Ch 57 "Neurons, activations and features", "Superposition: more ideas than neurons" | None |
| N69. Sparse autoencoders and transcoders (Golden Gate Claude) | COVERED | Ch 57 "Sparse autoencoders: unpacking the suitcase" | None |
| N70. Circuits and attribution graphs | COVERED | Ch 57 "Circuits and attribution graphs: tracing a thought" (rhyme planning, multi-step reasoning) | None |
| N71. Steering, introspection, auditing, natural-language autoencoders | COVERED | Ch 57 "Steering: turning the dials", "Auditing, introspection and new tools" | None |
| O72. World models (Genie 3, JEPA, do LLMs have world models, ARC-AGI-3 interactive) | COVERED | Ch 22 "Toward world models and embodied AI" (both sides of the debate, Othello example); Ch 16; Ch 47; Ch 24 ARC-AGI-3 and "Open frontiers"; Ch 66 | None |
| O73. Open frontiers (continual learning, reliability, AI-accelerated research, safety cases) | COVERED | Ch 24 "Open frontiers" (METR, about 1.5× Anthropic estimate, safety cases); Ch 66 | None |

**Summary.** Of the 73 topic-map items in research file 04, 71 were already COVERED at beginner level, 2 were THIN and none were MISSING. Part IV (Chapters 18–24) maps closely onto this file, with interpretability (Part N) taught in Chapter 57 and world models across Chapters 16, 22 and 24. The two gaps were named sub-items: item 3 listed "code can cost more tokens" alongside non-English text, but Chapter 18 explained only the language case, so a short hedged paragraph on code was added to "What tokens explain about your chatbot"; item 15 listed "curriculum", which the book never named, so Chapter 19's data-mixture section now explains curriculum (ordering and changing the mix over a run, with saving the best data for the end as the documented case, tied to annealing and OLMo 2) with a definition callout and a Key terms entry. Both edited chapters pass validate.py (14/14 diagrams) and check.py (OK).
