# Coverage report: 03-deep-learning.md (topic map, section 1)

Audited October 21, 2026 against `ai-book/chapters/`. Each item was located by searching for its key terms (and every named sub-item), then reading the passage. "COVERED" means explained at beginner level, not just mentioned.

| Item | Status before | Where covered (chapter and section) | Action taken |
|---|---|---|---|
| A1. From rules to learning | COVERED | Ch 12 "From rules to learning" (spam rule vs learned rule, network as adjustable function, knobs); Ch 1, Ch 8 | None |
| A2. Everything becomes numbers (vector, matrix, tensor) | COVERED | Ch 12 "Everything becomes numbers" (definitions incl. tensor); Ch 5 vectors and matrices with spreadsheet exercises | None |
| A3. The artificial neuron (beach example, McCulloch–Pitts, perceptron, XOR, Minsky & Papert) | COVERED | Ch 12 "The artificial neuron": "Should I go to the beach?", "A little history: from logic units to the perceptron", "What one neuron can and cannot do"; Ch 7 history | None |
| A4. Activation functions (step, sigmoid, tanh, ReLU, Leaky ReLU, GELU, SiLU/Swish, softmax) | COVERED | Ch 12 "Activation functions": "Solving XOR with two bent neurons", "The activation function gallery", "Softmax" | None |
| A5. Layers, width and depth; counting parameters | COVERED | Ch 12 "Layers, width and depth" and "Counting parameters" (3 → 4 → 2 = 26 worked in a table, up to "70B") | None |
| A6. The forward pass as matrix multiplication | COVERED | Ch 12 "The forward pass: a layer is one matrix multiplication" incl. "Why this matters for chips" | None |
| A7. Loss (MSE, cross-entropy as surprise, chatbot pretraining loss) | COVERED | Ch 12 "Loss: one number for how wrong" (squared error, cross-entropy, "exactly how chatbots are pre-trained"); Ch 6 "Loss functions"; Ch 19 | None |
| A8. Gradient descent (fog, learning rate, 1-D parabola, 2-D map) | COVERED | Ch 12 "Gradient descent: walking downhill in fog" (one-knob parabola table and ASCII figure); Ch 6 "Gradients" (two-knob worked step, loss landscape, hiking-map analogy) and "Valleys, plateaus and smarter walkers"; Ch 13 ravines. No literal contour drawing, but the 2-D case is taught with numbers | None |
| A9. Backpropagation and the chain rule (gears, autograd, 1986) | COVERED | Ch 12 "Backpropagation" (chain rule as gears, full worked forward/backward pass, gradient checking, history); Ch 6 "The chain rule" | None |
| A10. The training loop (batch, step, epoch, splits) | COVERED | Ch 12 "The training loop: batches, steps and epochs" incl. "Keeping score honestly" (train/validation/test) | None |
| A11. Optimizers (SGD → momentum → Adam/AdamW → Lion, Shampoo/SOAP → Muon) | COVERED | Ch 13 "Optimizers: smarter ways to walk downhill" (all named optimizers, Muon in depth) | None |
| A12. Learning rate and schedules (warmup, cosine, WSD, NaN, loss spikes) | COVERED | Ch 13 "The learning rate" incl. "Schedules", "Batch size and the learning rate", "Loss spikes"; NaN defined | None |
| A13. Initialization (symmetry, Xavier/Glorot, He) | COVERED | Ch 13 "Initialization: where the walk begins" | None |
| A14. Generalization vs memorization (regularization, double descent) | COVERED | Ch 13 "Generalization versus memorization", "The regularization toolkit", "Double descent and other surprises"; Ch 9 | None |
| A15. Normalization (batch, layer, RMSNorm, pre/post-norm, DyT) | COVERED | Ch 13 "Normalization" (layer norm worked by hand, "The family of normalizations"); Ch 17 DyT | None |
| A16. Vanishing/exploding gradients, residuals, hyper-connections, mHC | COVERED | Ch 13 "Vanishing and exploding gradients", "Residual connections: the express elevator"; Ch 17 "Keeping giants stable" | None |
| A17. Theory (universal approximation, depth, inductive bias, Bitter Lesson) | COVERED | Ch 13 "Why depth works" (all four sub-sections); Ch 7 Bitter Lesson | None |
| A18. Numbers on hardware (FP32 → FP4, mixed precision, quantization) | COVERED | Ch 13 "Numbers on hardware: precision in brief"; Ch 5 precision and memory math; Ch 32 | None |
| B19. MLP and its weakness on images | COVERED | Ch 14 "Why a plain network struggles with pictures" (MNIST 784 → 128 → 10, two problems); Ch 12 dense layers and ice-cream network (tabular inputs); Ch 10 tabular data | None |
| B20. CNNs (filters, stride, padding, channels, pooling, receptive field, LeNet → U-Net, transfer learning) | COVERED | Ch 14 "Convolution" (worked by hand, stride and padding, channels, pooling, receptive fields), "The deep learning boom" (LeNet, ImageNet, AlexNet, VGG, ResNet, U-Net), "Transfer learning" | None |
| B21. RNNs, BPTT, LSTM/GRU, no parallelism | COVERED | Ch 14 "Recurrent neural networks", "Backpropagation through time", "LSTM and GRU: memory with valves" | None |
| B22. Seq2seq and the birth of attention (Bahdanau 2014) | COVERED | Ch 14 "Sequence to sequence: translation and its bottleneck", "The birth of attention" | None |
| B23. Embeddings (one-hot, word2vec, GloVe, king − man + woman, contextual, sentence) | COVERED | Ch 14 "Embeddings: putting words on a map of meaning" (all sub-sections); Ch 5; Ch 27 | None |
| C24. Why Transformers won (2017) | COVERED | Ch 15 "Why the Transformer won" | None |
| C25. Tokens and tokenization (BPE, vocab size, strawberry) | COVERED | Ch 15 "Step 1" (BPE worked by hand); Ch 18 "Tokens" with tokenizer playground Try-it | None |
| C26. Token embeddings (embedding matrix) | COVERED | Ch 15 "Step 2: Token embeddings" (table size worked for GPT-2 and a 4,096-wide model) | None |
| C27. Position (sinusoidal, learned, RoPE, ALiBi, NoPE/iRoPE, YaRN) | COVERED | Ch 15 "Step 3" (RoPE worked with angles, ALiBi, iRoPE, "Stretching the context window", Table 15.2) | None |
| C28. Self-attention Q/K/V (library analogy, 3-token example, quadratic cost) | COVERED | Ch 15 "Step 4: Self-attention, worked by hand" (Steps A–E, mask, quadratic cost) | None |
| C29. Multi-head attention, MQA/GQA/MLA | COVERED | Ch 15 "Step 5: Many heads, and how to save their memory" incl. KV-cache memory bill | None |
| C30. Feed-forward block (SwiGLU, facts, two-thirds of params) | COVERED | Ch 15 "Step 6: The feed-forward block" (two-thirds worked for GPT-2, SwiGLU worked) | None |
| C31. Transformer block and residual stream | COVERED | Ch 15 "Step 7: The residual stream and one full block" (block counts for GPT-2/GPT-3/Llama 3/Kimi K3) | None |
| C32. Encoder vs decoder, causal mask | COVERED | Ch 15 "Step 8: Encoders, decoders and the causal mask" (BERT, GPT, T5, Whisper) | None |
| C33. Unembedding, logits, sampling, autoregressive loop, KV cache | COVERED | Ch 15 "Step 9: From vectors back to words"; Ch 18 sampling; Ch 23 KV cache | None |
| C34. Training objective (next token, teacher forcing, MLM, MTP) | COVERED | Ch 15 "Step 10: How a Transformer learns" | None |
| C35. Cheaper attention (FlashAttention, sliding/sparse/compressed, sinks, gated attention) | COVERED | Ch 15 "Making attention cheaper" (Table 15.6, DeepSeek V4 CSA/HCA numbers) | None |
| C36. Transformers beyond text (ViT, audio, video, proteins) | COVERED | Ch 15 "Transformers beyond text" (224 × 224 → 196 patches worked) | None |
| C37. Mixture of experts at architecture level | COVERED | Ch 17 "Mixture of experts" (routing worked example, total vs active, shared experts, load balancing, why MoE won); Ch 15 Step 6 | None |
| D38. Self-supervised learning | COVERED | Ch 16 "Self-supervised learning"; Ch 8 | None |
| D39. Contrastive learning and CLIP (zero-shot, SigLIP) | COVERED | Ch 16 "Contrastive learning and CLIP"; Ch 22 | None |
| D40. Multimodal LLMs (late/early fusion, any-to-any, Gemini Omni) | COVERED | Ch 16 "Beyond single media"; Ch 22 "Late fusion and early fusion", "Models that draw" | None |
| D41. Predictive and world models (JEPA, V-JEPA 2, Genie 3) | COVERED | Ch 16 "Beyond single media: multimodal models and world models"; Ch 22 "Toward world models and embodied AI"; Ch 47; Ch 49 | None |
| E42. What "generative" means (distribution, latent space) | COVERED | Ch 16 "What generative really means" (learning a distribution, latent space) | None |
| E43. Autoencoders | COVERED | Ch 16 "The autoencoder" (compression, denoising, anomaly detection) | None |
| E44. VAEs (mean and spread, reparameterization trick, inside Stable Diffusion) | COVERED | Ch 16 "The variational autoencoder (VAE)" with worked smile example | None |
| E45. GANs (StyleGAN, mode collapse, displaced by diffusion) | COVERED | Ch 16 "GANs: the forger and the detective" | None |
| E46. Autoregressive image generation (GPT-4o, gpt-image-2) | COVERED | Ch 16 "Autoregressive image generation: painting by tokens" (gpt-image-2 "thinking" hedged as reported) | None |
| E47. Diffusion (DDPM, schedulers, CFG, negative prompts, seeds, latent diffusion, cross-attention, DiT) | COVERED | Ch 16 "Diffusion, step by step", "Samplers and step counts", "Steering diffusion with words", "Latent diffusion and the Diffusion Transformer" | None |
| E48. Flow matching / rectified flow; distillation to 1–4 steps | COVERED | Ch 16 "Flow matching and the race to fewer steps" | None |
| E49. Control and customization (inpainting, img2img, ControlNet, LoRA, instruction editing) | COVERED | Ch 16 "Control and customization" (LoRA size worked) | None |
| E50. Video generation (3D VAE, spacetime patches, Veo 3, Sora closure) | COVERED | Ch 16 "Video generation" (token count worked); Ch 47 products | None |
| E51. Diffusion language models (LLaDA, Gemini Diffusion, Mercury) | COVERED | Ch 16 "Diffusion language models" | None |
| F52. Graph neural networks | COVERED | Ch 17 "Graph neural networks: when data is a web, not a line"; Ch 52 GraphCast | None |
| F53. State-space models and linear attention (S4 → Mamba-3, DeltaNet, RWKV, xLSTM) | COVERED | Ch 17 "State-space models and linear attention" (From S4 to Mamba-3; linear attention and the delta rule; the catch) | None |
| F54. Hybrid architectures and the counter-trend | COVERED | Ch 17 "Hybrid architectures" and "The counter-trend: going back to full attention" | None |
| F55. Residual-stream and stability innovations (mHC, QK-norm/clip, DyT) | COVERED | Ch 17 "Keeping giants stable"; Ch 13 | None |
| F56. Recursion, memory and small models (TRM, Titans, MTP) | COVERED | Ch 17 "Recursion, memory and small models" (framed as live research) | None |
| G57. Frameworks (PyTorch, TF/Keras 3, JAX, ecosystem) | COVERED | Ch 13 "Frameworks: PyTorch, JAX and TensorFlow/Keras" | None |
| G58. Anatomy of a training script | COVERED | Ch 13 "Anatomy of a training script" and "A complete training script for Google Colab" | None |
| H59. Synthesis: why it works and what we don't know | COVERED | Ch 17 "The 2026 convergence" and "Open questions"; Ch 13 "The 2026 recipe at a glance", "The Bitter Lesson"; Ch 57 superposition | None |

**Summary.** All 59 topic-map items in research file 03 (and every named sub-item) were already taught at beginner level before this audit: 59 COVERED, 0 THIN, 0 MISSING. Part III of the book (Chapters 12–17) follows this research file almost item for item, with worked numeric examples for nearly every mechanism (parameter counting, one-knob gradient descent, backpropagation, layer norm, RoPE, three-token attention, SwiGLU, VAE sampling, video token counts, MoE routing). The only sub-item delivered differently from the research suggestion is A8's "2-D contour map": the two-dimensional case is taught through a worked two-knob gradient step, the loss-landscape definition and a hiking-map analogy (Chapter 6) and through ravines (Chapter 13), rather than a drawn contour plot; this was judged adequate, so no edits were made for this file.
