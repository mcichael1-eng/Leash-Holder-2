# Research Brief 03: Neural Networks, Deep Learning and Model Architectures (incl. Generative Models)

For: *Everything About AI: From Zero to the Frontier*. Reader: almost no computer-science background, daily chatbot user. Research date: 21 October 2026.

Verification note: facts tagged with a URL in Section 4 were checked against the web in October 2026. Established history (paper years, classic results) comes from well-known literature and is not cited one by one. Secondary sources are flagged as such. The session's web-search budget ran out before every 2026 detail could be cross-checked, so items marked "(secondary)" should be checked against the vendor's own page before printing.

---

## 1. Topic map (teaching order, simplest to most advanced)

### Part A. What a neural network is

1. **From rules to learning.** Contrast a hand-written rule ("if the email contains 'lottery', mark it spam") with a system that *learns* the rule from examples. Introduce the core idea: a neural network is a big adjustable function that maps inputs to outputs, and "training" means turning its knobs until the outputs are right.
2. **Everything becomes numbers.** Pixels become brightness values, words become token IDs and then lists of numbers, and sound becomes wave samples. Introduce *vector* (a list of numbers), *matrix* (a grid) and *tensor* (a stack of grids) using spreadsheets as the mental model. Use no math notation beyond multiplication and addition.
3. **The artificial neuron.** Multiply each input by a weight, add them up, add a bias, then pass the total through an activation function. Work a numeric example on paper ("should I go to the beach?" with inputs for sun, temperature and work). Give the history: McCulloch–Pitts (1943) and Rosenblatt's perceptron (1958). Briefly explain why one neuron can't learn XOR (Minsky & Papert, 1969).
4. **Activation functions.** Explain why a network without them collapses into one big linear function: "stacking straight lines only gives you a straight line." Show plots of step, sigmoid, tanh, ReLU, Leaky ReLU, GELU and SiLU/Swish. Then cover softmax as the "turn scores into percentages" function used at the output.
5. **Layers, width and depth.** Cover input, hidden and output layers; "fully connected" (dense) layers; counting parameters (a 3→4→2 network has 3×4+4 + 4×2+2 = 26 parameters); and what "a 70-billion-parameter model" means in these terms.
6. **The forward pass.** Data flows left to right through the layers. In practice each layer is one matrix multiplication plus an activation, which is why GPUs (matrix-multiplication machines) matter. Link to the compute chapter.
7. **Loss: measuring wrongness.** Cover mean squared error for numbers and cross-entropy for categories, described as "how surprised was the model by the right answer?" Show that a chatbot's pre-training loss is exactly this surprise, measured at every next token.
8. **Gradient descent.** Use the analogy of walking downhill in fog. The gradient is the slope in every knob direction at once, and the learning rate is the step size. Draw a 1-D example (a parabola) by hand, then a 2-D contour map.
9. **Backpropagation and the chain rule.** Present it as an efficient way of assigning blame backward through the network: if the output was wrong, how much did each weight contribute? Explain the chain rule with gears, where the speed of the last gear is the product of the gear ratios. Mention autograd, meaning frameworks do this automatically. Give the history: popularized by Rumelhart, Hinton and Williams (1986).
10. **The training loop.** Cover batch, mini-batch, iteration/step, epoch, and train/validation/test splits. Pseudo-code: *repeat: grab a batch → forward → loss → backward → update*.
11. **Optimizers.** Explain them as progressively smarter hikers: SGD → momentum (a rolling ball) → RMSProp/Adam (per-knob adaptive step sizes) → AdamW (decoupled weight decay) → Lion, Shampoo/SOAP (curvature-aware) → **Muon** (orthogonalized momentum for weight matrices, used at frontier scale in 2025–26).
12. **Learning rate and schedules.** Cover warmup, cosine decay, and warmup-stable-decay (WSD). Explain why too high a rate diverges ("loss = NaN") and too low a rate crawls, and what a loss spike is.
13. **Initialization.** Explain why you can't start with all zeros (symmetry: every neuron would learn the same thing) and why random values must be well-scaled (Xavier/Glorot 2010, He 2015).
14. **Generalization vs. memorization.** Cover overfitting and underfitting, train/validation curves, regularization (weight decay, dropout, data augmentation, early stopping), and briefly mention "double descent" and why huge models can still generalize.
15. **Normalization.** Explain why keeping numbers in a sane range helps training. Cover batch norm (2015), layer norm (2016), RMSNorm (2019, standard in modern LLMs), pre-norm vs. post-norm, and "Transformers without normalization" (DyT, 2025).
16. **Vanishing and exploding gradients.** Use the "telephone game" through many layers: signals shrink to zero or blow up. Fixes include ReLU, careful initialization, normalization, gradient clipping and, above all, **residual (skip) connections**, framed as "add the input back so the layer only has to learn a correction." Cover the 2025–26 extensions: hyper-connections and DeepSeek's mHC.
17. **Theory in plain words.** Universal approximation (one wide hidden layer can approximate any reasonable function, but says nothing about how to find the weights or how many neurons you need). Why depth helps: features are built from features (edges → shapes → objects), and composition is exponentially more efficient. Inductive biases: assumptions built into an architecture. Sutton's **Bitter Lesson** (2019): general methods that scale with compute beat hand-built knowledge.
18. **Numbers on hardware.** Cover precision (FP32, BF16, FP8, FP4) and why lower precision is faster. Mixed precision, quantization as "rounding the weights", and a pointer to the compute and data-center chapter.

### Part B. Classic architectures

19. **MLP (multilayer perceptron).** This is the plain stacked-dense-layer network. Show it on tabular data and on MNIST digits. Explain its weakness on images: it ignores the fact that nearby pixels are related, and it has too many weights.
20. **Convolutional neural networks (CNNs).** A small filter slides across the image looking for one pattern, such as a vertical edge. Cover feature maps, stride, padding, channels, pooling, the receptive field, and the hierarchy of features. Then the milestones: LeNet, ImageNet (2009), AlexNet (2012, the "big bang" of deep learning on GPUs), VGG, ResNet (2015, 152 layers thanks to skip connections), and U-Net (2015, later the backbone of diffusion models). Finish with transfer learning: reuse a pretrained CNN.
21. **Recurrent neural networks (RNNs).** Reading word by word while carrying a "memory" (hidden state). Cover backpropagation through time, why RNNs forget long-range information, the LSTM (1997, with forget/input/output gates as valves) and the GRU (a simpler cousin). Explain the core limitation: they can't be parallelized across time steps.
22. **Sequence-to-sequence (2014).** An encoder RNN compresses a sentence into one vector, and a decoder RNN unrolls it into a translation. The bottleneck problem leads to **attention** (Bahdanau et al., 2014): let the decoder look back at all encoder states.
23. **Embeddings and vector spaces.** Start with one-hot vectors and move to learned dense vectors. Cover word2vec (2013), GloVe, "king − man + woman ≈ queen", cosine similarity, and clustering. Then contextual embeddings (the same word gets different vectors in different sentences) and sentence/document embeddings for semantic search and RAG (link to the applications chapter).

### Part C. The Transformer, in depth

24. **Why Transformers won.** "Attention Is All You Need" (June 2017). Every token looks at every other token in parallel, with no recurrence, so the whole sentence is processed at once on GPUs. This is the architecture behind GPT, Claude, Gemini, Llama, DeepSeek and Qwen.
25. **Tokens and tokenization.** Cover subword pieces, byte-pair encoding (BPE), vocabulary size, and why the model can struggle to count letters in "strawberry". Hands-on: a tokenizer website.
26. **Token embeddings.** Each token ID is looked up in a giant table (the embedding matrix) to get a vector of, say, 4,096 numbers.
27. **Position information.** Attention by itself is order-blind ("dog bites man" = "man bites dog"). Cover sinusoidal and learned position embeddings, **RoPE** (rotary: rotate each vector by an angle proportional to its position, so relative distance shows up in dot products), ALiBi, NoPE layers (Llama 4's interleaved "iRoPE"), and context-length extension (YaRN-style RoPE scaling).
28. **Self-attention: queries, keys, values.** Use the library/search analogy. Each token makes a query ("what am I looking for?"), a key ("what do I contain?") and a value ("what I'll hand over"). Score = query · key, scaled, then softmax into weights, then a weighted sum of values. Work a pencil example with 3 tokens. Cover the attention matrix and why cost grows with the square of the sequence length.
29. **Multi-head attention.** Several attention "spotlights" in parallel, each free to specialize (one tracks pronouns, another syntax). Then the memory-saving variants: MQA, GQA (most open models) and MLA (DeepSeek, Kimi, GLM).
30. **Feed-forward (MLP) block.** After tokens "talk" in attention, each token "thinks" alone in a two-layer MLP, usually SwiGLU today. This is where much factual association appears to be stored. It is roughly two-thirds of the parameters in dense models.
31. **The Transformer block and residual stream.** One block is: norm → attention → add back; norm → MLP → add back. Stack 30–120 blocks. The "residual stream" is a shared notepad that each layer reads from and writes to.
32. **Encoder vs. decoder.** Encoder-only (BERT, 2018) sees the whole text both ways and is good for classification and embeddings. Decoder-only (GPT family, essentially all chatbots) uses a **causal mask** so a token can't see the future. Encoder-decoder (original Transformer, T5, Whisper) suits translation and speech.
33. **From vectors back to words.** Cover the unembedding, logits, softmax over the vocabulary, sampling (temperature, top-k, top-p), the autoregressive loop (generate one token, append, repeat), and the KV cache (why long chats use memory). Link to the inference chapter.
34. **Training objective.** Cover next-token prediction, teacher forcing, masked language modeling (BERT), and multi-token prediction (DeepSeek-V3, Nemotron 3 Super).
35. **Making attention cheaper.** FlashAttention (exact attention, computed in GPU-friendly tiles), sliding-window/local attention, sparse attention (DeepSeek Sparse Attention), compressed attention (DeepSeek V4's CSA/HCA), attention sinks, and gated attention (NeurIPS 2025 best paper).
36. **Transformers beyond text.** Vision Transformer (ViT, 2020): cut the image into 16×16 patches and treat each patch as a token. Audio: spectrogram patches (Whisper). Video: spacetime patches. Proteins and molecules: AlphaFold-style attention.
37. **Mixture-of-experts (MoE) at the architecture level.** Replace the single MLP with many expert MLPs plus a router that sends each token to the top-k experts. Cover total vs. active parameters (DeepSeek V4-Pro: 1.6T total, 49B active), shared experts, load balancing, and why MoE won for frontier efficiency. Leave scaling economics to the compute chapter.

### Part D. Representation learning and multimodality

38. **Self-supervised learning.** Training signals made from the data itself (predict the next word, fill in masked patches). This is why the internet could be used as a textbook without human labels.
39. **Contrastive learning and CLIP (2021).** Pull matching image–caption pairs together and push mismatched pairs apart in one shared space. This enables zero-shot classification, image search, and text conditioning for image generators. Mention SigLIP.
40. **Multimodal LLMs.** Late fusion: vision encoder → projector → LLM. Early fusion: image and text tokens trained together from the start (Llama 4). Then "any-to-any" models: Gemini Omni (May 2026) takes text, image, audio and video in and produces video out.
41. **Predictive and world models.** JEPA (predict in embedding space, not pixels; V-JEPA 2) and interactive world models (Genie 3, 2025). Connect them to robotics (link to the robotics chapter).

### Part E. Generative models

42. **What "generative" means.** Learning the *distribution* of data well enough to sample new examples. Introduce latent space as a "map of possibilities".
43. **Autoencoders.** Squeeze → bottleneck → rebuild. Used for compression, denoising and anomaly detection.
44. **VAEs (2013).** The encoder outputs a fuzzy region (mean and spread) instead of a point, so the latent space becomes smooth and you can sample from it. Cover the reparameterization trick in one sentence. VAEs remain inside Stable Diffusion as the image ↔ latent compressor.
45. **GANs (2014).** A forger (generator) and a detective (discriminator) improve each other. Cover StyleGAN faces (thispersondoesnotexist), mode collapse and training instability, and why diffusion displaced GANs for most image generation.
46. **Autoregressive image generation.** Images as sequences of tokens. GPT-4o's native image generation (March 2025) was autoregressive, and gpt-image-2 (April 2026) adds "thinking" before drawing.
47. **Diffusion models.** The forward process adds noise step by step until the image is static. A network (U-Net or Transformer) learns to predict the noise, and the reverse process denoises from pure static guided by text. Cover DDPM (2020), sampling steps, schedulers (DDIM etc.), classifier-free guidance (the "guidance scale" slider), negative prompts, seeds, **latent diffusion** (Stable Diffusion, Aug 2022: denoise in a compressed VAE latent, not pixels), text conditioning via cross-attention to CLIP/T5 text embeddings, and the Diffusion Transformer (DiT, 2022).
48. **Flow matching / rectified flow (2022).** Learn a velocity field that carries noise to data along (nearly) straight paths, which allows fewer steps. Used in Stable Diffusion 3 (2024) and FLUX. Cover distillation down to 1–4 steps (SDXL-Turbo, consistency models).
49. **Control and customization.** Cover inpainting/outpainting, img2img, ControlNet (2023: poses, edges, depth), LoRA fine-tunes for styles and characters, and instruction-based editing (Nano Banana, FLUX Kontext).
50. **Video generation.** A 3D (spacetime) VAE compresses video, and a diffusion Transformer denoises spacetime patches. Cover temporal consistency, physics failures, native audio (Veo 3, 2025), product churn (Sora app closed April 2026; Veo 3.1, Kling, Seedance, Runway), and the link to world models.
51. **Diffusion language models.** Start from a fully "masked" answer and unmask many tokens in parallel over a few refinement steps. Examples: LLaDA (2025), LLaDA2.0 (100B MoE), Gemini Diffusion, Inception's Mercury/Mercury 2 (about 1,000 tokens/s). Trade-offs vs. autoregressive models.

### Part F. Other and frontier architectures

52. **Graph neural networks.** Data as nodes and edges (molecules, social networks, road maps). Message passing: each node updates itself from its neighbors. Examples: GCN (2016), GraphCast weather forecasting (2023), drug discovery. Note that Transformers are GNNs on a fully connected graph.
53. **State-space models and linear attention.** S4 → Mamba (Dec 2023: a selective state that decides what to remember) → Mamba-2 → Mamba-3 (2026). Linear attention, DeltaNet / Gated DeltaNet, Kimi Delta Attention, RWKV, xLSTM. The key property is a fixed-size memory, which gives constant cost per new token instead of a growing KV cache.
54. **Hybrid architectures.** Most layers are cheap recurrent or linear layers, with a few full-attention layers for exact recall. Examples: Jamba (2024), Qwen3-Next/Qwen3.5 (3:1 Gated DeltaNet : gated attention), Kimi Linear (3:1 KDA : MLA), and Nemotron 3 (mostly Mamba-2 + MoE + a few attention layers). Cover the counter-trend: MiniMax M2 went back to full attention (Oct 2025).
55. **Residual-stream and stability innovations.** Hyper-connections and mHC (DeepSeek, Dec 2025; used in V4), gated attention, QK-norm and QK-clip (Kimi K2's MuonClip), and DyT.
56. **Recursion, memory and small models.** Looped/recursive models (Tiny Recursive Model, Oct 2025), test-time memory (Titans), and multi-token prediction. Frame these as live research, not settled practice.

### Part G. Frameworks and tools

57. **What a framework does.** Tensors on GPUs, automatic differentiation, ready-made layers and optimizers, and data loaders. PyTorch (dominant in research and most frontier open models), TensorFlow + Keras (large installed base; Keras 3 runs on JAX/PyTorch/TF), and JAX (Google DeepMind, TPUs, functional style). The ecosystem: Hugging Face Transformers/Diffusers, vLLM, Triton kernels.
58. **Anatomy of a training script.** Annotate 15 lines of PyTorch line by line (model, loss, optimizer, loop).

### Part H. Big-picture synthesis

59. **Why it all works and what we still don't know.** Scaling, the Bitter Lesson revisited, why inductive biases still matter at small scale, open questions (generalization theory, interpretability, superposition), and the convergence of 2026 frontier designs (MoE + efficient attention + low precision + Muon-style optimizers).

---

## 2. Glossary candidates (plain-English definitions)

**Foundations**
1. **Artificial intelligence (AI):** Computer systems that perform tasks we associate with intelligence, such as recognizing images, understanding language or making decisions.
2. **Machine learning (ML):** A branch of AI where the computer learns patterns from examples instead of following hand-written rules.
3. **Deep learning:** Machine learning using neural networks with many layers ("deep" means many layers stacked).
4. **Neural network:** A function made of many simple connected units (neurons) whose adjustable numbers (weights) are tuned on data so the function produces useful outputs.
5. **Artificial neuron:** The basic unit. It multiplies each input by a weight, adds them up with a bias, and passes the result through an activation function.
6. **Perceptron:** The earliest trainable artificial neuron (Rosenblatt, 1958). It outputs 1 or 0 depending on whether its weighted sum passes a threshold.
7. **Weight:** A number that sets how strongly one input influences a neuron. Learning means adjusting weights.
8. **Bias (in a neuron):** An extra adjustable number added to the weighted sum. It shifts the neuron's threshold up or down. (Not the same as social bias.)
9. **Parameter:** Any number the model learns during training (weights and biases). "A 70B model" has about 70 billion of them.
10. **Hyperparameter:** A setting chosen by humans before training, such as learning rate, batch size or number of layers, rather than learned.
11. **Activation function:** The non-linear "squish" applied after the weighted sum. Without it, any stack of layers would behave like a single straight-line function.
12. **Linear / non-linear:** Linear means "output changes proportionally with input" (a straight line). Non-linear means curves, thresholds and bends, which neural networks need to model the real world.
13. **Step function:** An activation that outputs 0 below a threshold and 1 above it. It was used in early perceptrons but can't be trained with gradients.
14. **Sigmoid:** An S-shaped activation that squeezes any number into the range 0 to 1. Useful for probabilities, but it causes vanishing gradients in deep networks.
15. **Tanh:** Like sigmoid but ranges from −1 to 1, centered on zero.
16. **ReLU (Rectified Linear Unit):** Outputs the input if positive, otherwise 0. Simple and fast, and it made deep networks much easier to train.
17. **Leaky ReLU:** A ReLU variant that lets a small negative slope through, so neurons don't "die" permanently at zero.
18. **GELU (Gaussian Error Linear Unit):** A smooth, curved version of ReLU used in GPT-2, BERT and many Transformers.
19. **SiLU / Swish:** Another smooth ReLU-like activation (input × sigmoid(input)), common in modern models.
20. **SwiGLU:** A "gated" feed-forward design where one branch, passed through Swish, multiplies another branch element by element. It is the standard MLP in most current LLMs.
21. **Softmax:** Turns a list of arbitrary scores into positive numbers that add to 1, i.e. a probability distribution. Used for next-token probabilities and attention weights.
22. **Logit:** A raw score before softmax. Higher logit means the model favors that option more.
23. **Layer:** A group of neurons that process inputs in parallel. Networks stack layers so each builds on the previous one.
24. **Input layer / hidden layer / output layer:** Where data enters, the internal processing stages, and where answers come out.
25. **Dense (fully connected) layer:** A layer where every input connects to every neuron. Mathematically, a matrix multiplication plus bias.
26. **Depth / width:** Depth is the number of layers; width is the number of neurons per layer.
27. **Vector:** An ordered list of numbers, e.g. [0.2, −1.3, 4.0]. Can be pictured as an arrow or a point in space.
28. **Matrix:** A rectangular grid of numbers. A layer's weights form a matrix.
29. **Tensor:** The general term for arrays of numbers with any number of dimensions (a vector is 1-D, a matrix is 2-D, a color image batch is 4-D).
30. **Matrix multiplication (matmul):** The core arithmetic operation of neural networks: many multiply-and-add operations done at once. GPUs are built to do it fast.
31. **Dot product:** Multiply two vectors element by element and add up the results. A measure of how aligned they are, used heavily in attention.
32. **Forward pass:** Running inputs through the network, layer by layer, to get an output.

**Training**
33. **Training:** The process of adjusting parameters so the model's outputs match the desired outputs on example data.
34. **Inference:** Using a trained model to produce outputs (what happens when you chat with a bot).
35. **Dataset / training set / validation set / test set:** The examples used to learn, to tune choices during development, and to give a final honest score on unseen data.
36. **Label:** The correct answer attached to a training example (e.g., "cat").
37. **Loss (loss function / cost / objective):** A single number measuring how wrong the model is. Training tries to make it small.
38. **Mean squared error (MSE):** Loss for predicting numbers: the average of squared differences between predictions and truth.
39. **Cross-entropy loss:** Loss for predicting categories or next tokens. It measures how surprised the model is by the correct answer.
40. **Perplexity:** A language-model score derived from cross-entropy: roughly "how many equally likely choices the model feels it's picking between." Lower is better.
41. **Gradient:** For every parameter, the direction and steepness in which the loss would increase. Training steps the opposite way.
42. **Derivative:** The slope of a function at a point: how much the output changes when the input nudges slightly.
43. **Gradient descent:** Repeatedly nudging all parameters a small step downhill on the loss, using the gradient.
44. **Stochastic gradient descent (SGD):** Gradient descent using a random small batch of examples per step instead of the whole dataset. Noisier but much faster.
45. **Backpropagation (backprop):** The algorithm that efficiently computes the gradient for every parameter by passing error signals backward through the network.
46. **Chain rule:** The calculus rule that the rate of change through a chain of steps is the product of each step's rate of change. Backprop is the chain rule applied systematically.
47. **Automatic differentiation (autograd):** Software that records the forward computation and computes gradients automatically, so programmers never derive them by hand.
48. **Learning rate:** How big a step the optimizer takes each update. The single most important hyperparameter.
49. **Learning-rate schedule:** A plan for changing the learning rate over training, e.g. warm up from tiny, then decay.
50. **Warmup:** Starting training with a very small learning rate and ramping up, to avoid early instability.
51. **Cosine decay / WSD (warmup–stable–decay):** Common schedules. Cosine decay smoothly lowers the rate along a cosine curve. WSD holds it flat, then drops it quickly near the end.
52. **Batch / mini-batch / batch size:** A group of examples processed together in one step, and how many are in it.
53. **Step (iteration):** One parameter update.
54. **Epoch:** One complete pass through the training dataset. Frontier LLMs often see most data roughly once.
55. **Optimizer:** The algorithm that turns gradients into parameter updates (SGD, Adam, AdamW, Muon...).
56. **Momentum:** An optimizer trick that keeps a running average of past gradients, like a ball rolling downhill that keeps its speed through small bumps.
57. **Adam:** An optimizer (2014) that combines momentum with per-parameter adaptive step sizes. The default for most deep learning for a decade.
58. **AdamW:** Adam with weight decay applied separately ("decoupled"), the standard for training Transformers.
59. **Muon:** An optimizer (Keller Jordan, Dec 2024) that takes the momentum update for each weight matrix and "orthogonalizes" it (via Newton–Schulz iterations) so no single direction dominates. Used at trillion-parameter scale by Kimi K2 and DeepSeek V4.
60. **Lion / Shampoo / SOAP:** Other optimizers. Lion uses only the sign of the update. Shampoo and SOAP use richer curvature information ("second-order-ish").
61. **Weight decay:** Gently shrinking weights toward zero every step, discouraging overly complex solutions.
62. **Initialization:** How weights are set before training. They must be random (to break symmetry) and correctly scaled (Xavier/Glorot, He initialization).
63. **Overfitting:** Memorizing the training examples (including noise) so performance on new data is worse.
64. **Underfitting:** The model is too simple or undertrained to capture the pattern even on training data.
65. **Generalization:** Performing well on new, unseen data, which is the actual goal of learning.
66. **Regularization:** Any technique that reduces overfitting (weight decay, dropout, data augmentation, early stopping).
67. **Dropout:** Randomly switching off a fraction of neurons during training so the network can't rely on any single one. Turned off at inference.
68. **Data augmentation:** Creating extra training examples by flipping, cropping or recoloring images, paraphrasing text, etc.
69. **Early stopping:** Stopping training when validation performance stops improving.
70. **Normalization layer:** A layer that rescales activations to a standard range so training stays stable.
71. **Batch normalization:** Normalizes each feature using statistics from the current batch. Key for CNNs.
72. **Layer normalization:** Normalizes across the features of each single example. Standard in Transformers.
73. **RMSNorm:** A simpler, cheaper layer norm that only rescales by the root-mean-square (no mean subtraction). Used in Llama, Qwen, DeepSeek, etc.
74. **Pre-norm / post-norm:** Whether normalization is applied before or after each sub-layer. Pre-norm trains more stably in deep Transformers.
75. **Vanishing gradient:** Error signals shrink as they travel back through many layers, so early layers stop learning.
76. **Exploding gradient:** Error signals grow uncontrollably, making training blow up.
77. **Gradient clipping:** Capping the size of gradients to prevent explosions.
78. **Residual connection (skip connection):** Adding a layer's input back to its output (output = input + layer(input)), giving signals and gradients a highway around each layer. This made 100+-layer networks trainable.
79. **Residual stream:** In a Transformer, the running vector each token carries through all layers, which every layer reads and adds to.
80. **Hyper-connections / mHC:** 2024–25 generalizations of residual connections with several parallel streams that mix. DeepSeek's mHC constrains the mixing to keep training stable.
81. **Loss spike:** A sudden jump in training loss, often a sign of instability. Expensive at frontier scale.
82. **Mixed precision / BF16 / FP8 / FP4:** Storing and computing numbers with fewer bits to go faster and use less memory, while keeping key quantities in higher precision.
83. **Quantization:** Converting a trained model's numbers to lower precision (e.g., 4-bit) to shrink and speed it up.

**Theory**
84. **Universal approximation theorem:** A result (Cybenko 1989; Hornik 1991) that a network with one wide enough hidden layer can approximate any reasonable function. It guarantees existence, not that training will find it.
85. **Inductive bias:** Assumptions baked into a model's design that make some solutions easier to learn, e.g. CNNs assume nearby pixels matter together.
86. **The Bitter Lesson:** Rich Sutton's 2019 essay arguing that, over decades, general methods that scale with computation beat approaches built on human-crafted knowledge.
87. **Scaling laws:** Empirical rules showing loss falls predictably as model size, data and compute grow (detailed in the scaling chapter).
88. **Feature (learned):** A pattern a network has learned to detect internally, such as an edge, a texture, or the concept "legal language".
89. **Superposition:** The phenomenon of networks packing more features than they have neurons by overlapping them, which makes interpretability hard.
90. **Double descent:** The surprising observation that test error can fall, rise, then fall again as models grow past the point of fitting training data exactly.

**Architectures**
91. **MLP (multilayer perceptron):** A network of stacked dense layers. Also the name for the feed-forward block in Transformers.
92. **CNN (convolutional neural network):** A network that slides small learned filters across images (or audio) to detect local patterns, reusing the same weights everywhere.
93. **Convolution:** Sliding a small grid of weights over the input and computing a weighted sum at each position.
94. **Filter / kernel:** The small grid of learned weights used in a convolution, e.g. 3×3.
95. **Feature map:** The output grid of a convolution, showing where the filter's pattern was found.
96. **Stride / padding:** How far the filter jumps each move, and the border added so the filter can cover edges.
97. **Channel:** One "layer" of an image or feature map (red, green and blue are 3 channels; deep layers may have hundreds).
98. **Pooling (max/average):** Shrinking a feature map by keeping the max or average of each small region, making detection robust to small shifts.
99. **Receptive field:** The region of the original input that a given neuron can "see". It grows with depth.
100. **ResNet:** A 2015 CNN family that introduced residual connections and trained 152-layer networks.
101. **U-Net:** An encoder–decoder CNN with skip connections between matching resolutions. The classic denoiser in diffusion models.
102. **Transfer learning:** Reusing a model trained on one task as the starting point for another.
103. **Fine-tuning:** Continuing training of a pretrained model on new, usually smaller, data.
104. **RNN (recurrent neural network):** A network that processes sequences one step at a time, carrying a hidden state forward as memory.
105. **Hidden state:** The internal memory vector an RNN (or SSM) carries from step to step.
106. **LSTM (long short-term memory):** An RNN (1997) with gates that decide what to forget, store and output, so it can remember over longer spans.
107. **GRU (gated recurrent unit):** A simpler gated RNN with two gates instead of three.
108. **Gate:** A learned 0-to-1 multiplier that controls how much information flows, like a valve.
109. **Sequence-to-sequence (seq2seq):** An encoder reads an input sequence and a decoder writes an output sequence (e.g., translation).
110. **Encoder / decoder:** The part that turns input into an internal representation / the part that turns a representation into output.
111. **Embedding:** A learned vector representing a token, word, image or anything else, placed so similar things are near each other.
112. **Vector space / embedding space:** The "map" where embeddings live. Directions and distances carry meaning.
113. **One-hot encoding:** Representing item #k out of N as a vector of N zeros with a single 1. No notion of similarity.
114. **word2vec:** A 2013 method that learns word embeddings by predicting nearby words. It famously supports analogies like king − man + woman ≈ queen.
115. **Cosine similarity:** A measure of how similar two vectors' directions are (1 = same direction, 0 = unrelated).
116. **Transformer:** The 2017 architecture built on self-attention and feed-forward blocks. The foundation of modern LLMs and many image, audio and video models.
117. **Token:** A chunk of text (word, part of a word, punctuation) or a patch of image/audio that the model processes as one unit.
118. **Tokenizer / BPE:** The program that splits text into tokens. Byte-pair encoding builds a vocabulary by repeatedly merging frequent character pairs.
119. **Vocabulary:** The fixed list of all tokens a model knows (often 100k–250k).
120. **Context window:** The maximum number of tokens the model can consider at once (now up to ~1M for several models).
121. **Positional encoding:** Information added so the model knows the order of tokens.
122. **RoPE (rotary position embedding):** Encodes position by rotating query and key vectors by position-dependent angles, so attention naturally depends on relative distance.
123. **Attention:** A mechanism letting each element compute a weighted mix of other elements, with weights based on relevance.
124. **Self-attention:** Attention where a sequence attends to itself (each token looks at the other tokens of the same text).
125. **Cross-attention:** Attention where one sequence looks at another (e.g., image denoiser attending to text-prompt embeddings).
126. **Query / key / value (Q, K, V):** Three vectors each token produces: what it's looking for, what it offers as a label, and the content it hands over if selected.
127. **Attention weights / attention matrix:** The softmaxed scores saying how much each token attends to each other token.
128. **Multi-head attention:** Running several attention operations in parallel with different learned projections, each capturing different relationships.
129. **MQA / GQA / MLA:** Ways to shrink attention memory. Several query heads share keys/values (multi-query, grouped-query), or keys/values are compressed into a small latent (multi-head latent attention).
130. **Causal mask:** Blocks each token from attending to future tokens, so the model learns to predict the next token honestly.
131. **Encoder-only / decoder-only / encoder–decoder:** Transformer layouts. BERT-style (understanding), GPT-style (generating; all major chatbots), T5/Whisper-style (input→output transformation).
132. **Feed-forward network (FFN):** The per-token MLP inside each Transformer block.
133. **KV cache:** Stored keys and values from earlier tokens so generation doesn't recompute them. It grows with conversation length.
134. **Autoregressive:** Generating one piece at a time, each conditioned on everything generated so far.
135. **Temperature / top-p:** Sampling settings. Temperature flattens or sharpens the probability distribution. Top-p samples only from the smallest set of tokens covering p% probability.
136. **FlashAttention:** A GPU-efficient way to compute exact attention in tiles without storing the full attention matrix.
137. **Sliding-window attention:** Each token attends only to the last N tokens, which caps cost.
138. **Sparse attention:** Each token attends to a selected subset of earlier tokens (e.g., DeepSeek Sparse Attention picks the top-k relevant ones).
139. **Attention sink:** The tendency of models to dump excess attention on the first token. Some designs add an explicit learnable sink, others remove the need via gating.
140. **Vision Transformer (ViT):** A Transformer that splits an image into patches and treats each patch as a token.
141. **Patch:** A small square of an image (or a small spacetime block of video) used as one token.
142. **Mixture of experts (MoE):** A layer containing many expert sub-networks plus a router that activates only a few per token, giving huge total capacity at modest compute.
143. **Router (gating network):** The small network in an MoE that scores experts and picks which ones process each token.
144. **Total vs. active parameters:** All parameters stored vs. those actually used for one token (e.g., 1.6T total, 49B active).
145. **Graph neural network (GNN):** A network that operates on nodes and edges, updating each node from its neighbors ("message passing").
146. **State-space model (SSM):** A sequence model that keeps a fixed-size internal state updated each step (like an RNN) but is designed for fast parallel training.
147. **Mamba:** A 2023 selective state-space model whose state update depends on the input, letting it choose what to remember. Successors are Mamba-2 (2024) and Mamba-3 (2026).
148. **Linear attention / DeltaNet / Gated DeltaNet / KDA:** Attention variants that replace the growing token-by-token comparison with a fixed-size memory updated per token. Gates and the "delta rule" control what is overwritten.
149. **Hybrid architecture:** A model mixing layer types, typically mostly linear/SSM layers plus some full-attention layers.

**Representation and generative**
150. **Self-supervised learning:** Learning from labels the data provides itself (next word, masked patch), with no human annotation.
151. **Contrastive learning:** Training embeddings by pulling matching pairs together and pushing non-matching pairs apart.
152. **CLIP:** OpenAI's 2021 model that learned a shared space for images and text from about 400 million image–caption pairs.
153. **Zero-shot:** Performing a task without any task-specific training examples.
154. **Multimodal model:** A model that handles more than one data type (text, images, audio, video).
155. **Early fusion / late fusion:** Combining modalities from the very first layer vs. bolting a separate encoder onto a language model.
156. **Generative model:** A model that learns the distribution of data so it can produce new samples (text, images, sound).
157. **Latent space:** The compressed internal space of representations. Moving through it smoothly changes the generated output.
158. **Autoencoder:** A network trained to compress input to a small code and reconstruct it.
159. **VAE (variational autoencoder):** An autoencoder whose code is a probability region, making its latent space smooth and sample-able.
160. **GAN (generative adversarial network):** A generator and a discriminator trained against each other until the fakes are convincing.
161. **Mode collapse:** A GAN failure where the generator produces only a few kinds of outputs.
162. **Diffusion model:** A generator trained to reverse a gradual noising process. It creates data by denoising random static step by step.
163. **Denoising / noise schedule:** Removing predicted noise / the plan for how much noise is present at each step.
164. **Sampler / scheduler / steps:** The algorithm and number of steps used to go from noise to image. Fewer steps is faster but sometimes worse.
165. **Classifier-free guidance (CFG):** Making outputs follow the prompt more strongly by contrasting the model's prediction with and without the prompt (the "guidance scale").
166. **Negative prompt:** Text describing what you *don't* want, used in place of the empty prompt during guidance.
167. **Seed:** The number that fixes the starting random noise, so the same seed and settings reproduce the same image.
168. **Latent diffusion:** Running diffusion in a VAE's compressed latent space instead of on full-resolution pixels, the key efficiency trick behind Stable Diffusion.
169. **Diffusion Transformer (DiT):** A diffusion model whose denoiser is a Transformer over latent patches rather than a U-Net. Standard for modern image and video generators.
170. **Flow matching / rectified flow:** A training method where the model learns a velocity field that moves noise to data along straight-ish paths, enabling efficient, few-step generation.
171. **Distillation (step distillation):** Training a faster "student" model to mimic a slower "teacher", e.g. generating an image in 1–4 steps instead of 50.
172. **ControlNet:** An add-on that steers a diffusion model with structure such as poses, edges or depth maps.
173. **LoRA (low-rank adaptation):** A cheap fine-tuning method that trains small add-on matrices instead of all weights. Widely used for custom image styles.
174. **Inpainting / outpainting:** Regenerating a masked region inside an image / extending an image beyond its borders.
175. **Diffusion language model (dLLM):** A text generator that refines many masked tokens in parallel over several steps instead of writing strictly left to right.
176. **World model:** A model that predicts how an environment evolves, especially in response to actions, sometimes rendering it interactively.
177. **JEPA (joint-embedding predictive architecture):** Yann LeCun's approach of predicting missing parts in embedding space rather than pixel by pixel.

**Frameworks**
178. **PyTorch:** The most widely used deep-learning library (Meta-originated, now under the PyTorch Foundation). Python-first and flexible.
179. **TensorFlow:** Google's deep-learning library (2015). Large production install base, less used in new research.
180. **Keras:** A high-level, beginner-friendly API for building networks. Keras 3 runs on TensorFlow, JAX or PyTorch.
181. **JAX:** Google's library for fast numerical computing with automatic differentiation and compilation, widely used on TPUs at Google DeepMind.
182. **GPU / TPU:** Chips specialized for parallel arithmetic (graphics processing unit; Google's tensor processing unit).
183. **CUDA / Triton / kernel:** NVIDIA's GPU programming platform / a Python-like language for writing GPU code / a single optimized GPU routine.
184. **Hugging Face:** The main hub for sharing open models and datasets, plus popular libraries (Transformers, Diffusers).
185. **Checkpoint / weights file:** The saved parameters of a model (e.g., `.safetensors`), which is what "open weights" means.

---

## 3. Prerequisites and dependencies

Read "A → B" as "teach A before B".

- **Numbers-as-data (vectors/matrices)** → neuron → everything else.
- **Weighted sum + bias** → activation functions → "why non-linearity" → layers/MLP.
- **Layers** → forward pass → loss → gradient (slope intuition) → gradient descent → backpropagation/chain rule → training loop (batches, epochs).
- **Gradient descent** → learning rate → optimizers (SGD → momentum → Adam → AdamW → Muon). Muon also needs "a layer's weights form a matrix".
- **Training loop** → overfitting/generalization → regularization (dropout, weight decay, augmentation).
- **Backprop through many layers** → vanishing/exploding gradients → initialization, normalization, residual connections.
- **MLP + "MLPs ignore spatial structure"** → convolution → CNNs → ResNet (needs residuals) → U-Net (needs encoder/decoder + skip connections).
- **MLP + "sequences"** → RNN → LSTM/GRU (needs gates) → seq2seq (needs encoder/decoder) → attention.
- **Vectors + dot product + cosine similarity** → embeddings (word2vec) → token embeddings.
- **Tokens + embeddings + softmax + dot product** → self-attention (Q/K/V) → multi-head → Transformer block (needs residuals + layer norm + MLP) → causal masking → decoder-only LLM → KV cache → efficient attention variants (GQA/MLA/sparse/FlashAttention).
- **Positional encoding** requires understanding that attention is order-blind. RoPE requires a simple picture of rotating arrows.
- **Transformer + patches** → ViT → multimodal models; ViT + contrastive loss → CLIP.
- **Router + MLP block** → mixture of experts.
- **RNN hidden state + attention cost** → SSMs/Mamba/linear attention → hybrid architectures.
- **Autoencoder** → VAE → latent space → latent diffusion. Separately: **noise + denoising** → diffusion → classifier-free guidance (needs CLIP/text embeddings + cross-attention) → DiT (needs ViT) → flow matching → video diffusion → world models.
- **GANs** need only MLP/CNN + loss + "two players". They can be taught before or after diffusion; teaching them before diffusion gives a nice "why diffusion won" story.
- **Diffusion + masked language modeling (BERT)** → diffusion language models.
- **Message passing** needs only the "weighted sum of neighbors" idea → GNNs. Pointing out that attention is message passing on a complete graph is a good bridge.
- **Frameworks** come after the reader understands tensors, autograd and the training loop. Introduce Colab before the first code exercise.
- **Bitter Lesson / inductive bias** works best after CNN vs. ViT and RNN vs. Transformer have both been seen.

Cross-chapter links: GPUs/precision → compute chapter; scaling laws, pre-/post-training, RLHF → LLM training chapter; KV cache, quantization, speculative decoding → inference chapter; interpretability (features, superposition) → safety/interpretability chapter; embeddings for search → RAG/applications chapter.

---

## 4. Current state and key facts (2025–2026)

### Optimizers
- **Muon** was introduced in Keller Jordan's blog post of **8 Dec 2024**: "MomentUm Orthogonalized by Newton-Schulz". It applies to 2-D hidden-layer weight matrices, with AdamW recommended for embeddings, the output head, and scalar/vector parameters. It set NanoGPT speedrun and CIFAR-10 speed records (CIFAR-10 to 94%: 3.3 → 2.6 A100-seconds). https://kellerjordan.github.io/posts/muon/
- **Moonshot "Muon is Scalable for LLM Training"** (Feb 2025) showed that adding weight decay and per-parameter update-scale adjustments makes Muon work at scale. https://arxiv.org/abs/2502.16982
- **Kimi K2** (July 2025): a 1T-total / 32B-active MoE, pre-trained on 15.5T tokens with **MuonClip** (Muon + "QK-clip" to stop attention logits from exploding) and reported "zero loss spike". https://arxiv.org/abs/2507.20534
- **DeepSeek V4** (2026) states it uses Muon "for faster convergence and greater training stability". https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro
- **PyTorch ships `torch.optim.Muon`.** It is documented from PyTorch 2.9 onward, and the docs' example pairs Muon for 2-D params with AdamW for the rest. https://docs.pytorch.org/docs/2.11/generated/torch.optim.Muon.html
- Research continues in 2026 (e.g., Muon+ arXiv 2602.21545; Newton-Muon arXiv 2604.01472). Teaching point: the optimizer field, frozen on Adam/AdamW for about 10 years, is moving again.

### Attention, normalization and residual innovations
- **Gated attention** (Qwen team) won a **NeurIPS 2025 Best Paper**. A head-specific sigmoid gate after attention improves performance and stability and removes "attention sinks". It was adopted in Qwen3-Next. https://blog.neurips.cc/?p=1443 ; https://github.com/qiuzh20/gated_attention
- The other NeurIPS 2025 best papers relevant to this chapter: "1000 Layer Networks for Self-Supervised RL" (depth scaling to 1,024 layers) and "Why Diffusion Models Don't Memorize" (two training timescales, where generalization comes before memorization). https://blog.neurips.cc/?p=1443
- **DyT, "Transformers without Normalization"** (Zhu, Chen, He, LeCun, Liu; CVPR 2025): replacing LayerNorm with `tanh(αx)` matches normalized Transformers in many settings. https://arxiv.org/abs/2503.10622
- **mHC: Manifold-Constrained Hyper-Connections** (DeepSeek, arXiv 2512.24880, end of Dec 2025). Constraining the multi-stream residual mixing matrices restores identity-like stability. Used in DeepSeek V4. https://arxiv.org/abs/2512.24880
- **Attention landscape (2026).** Raschka's LLM Architecture Gallery counts 111 recent models (categories overlap): GQA-family ~65%, sliding-window/global patterns ~31%, MLA-family ~23%, DeltaNet/Lightning/KDA hybrids ~14%, Mamba/mLSTM layers ~7%, DeepSeek Sparse Attention ~6%, and classic full MHA only ~4%. Good for a "nobody agrees on attention anymore" chart. https://www.sebastianraschka.com/llm-architecture-gallery/attention-mechanism-distribution/

### Flagship architectures (open models, where details are public)
- **DeepSeek V4** (technical report dated late April 2026; arXiv 2606.19348). **V4-Pro: 1.6T total / 49B active. V4-Flash: 284B / 13B.** 1M-token context. Hybrid **Compressed Sparse Attention (CSA) + Heavily Compressed Attention (HCA)**: at 1M context, Pro needs 27% of V3.2's per-token FLOPs and 10% of its KV cache. Also mHC residuals, Muon, FP4 experts + FP8 elsewhere, >32T training tokens, MIT license. https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro ; https://arxiv.org/html/2606.19348v1
- **Qwen3-Next** (Sept 2025): 80B total / 3B active. 48 layers arranged as 12 × (3 Gated DeltaNet + 1 Gated Attention). https://sebastianraschka.com/llm-architecture-gallery/hybrid-attention/
- **Qwen3.5** (flagship 397B-A17B, ~16–17 Feb 2026, Apache 2.0): 60 layers = 15 × [3 × (Gated DeltaNet → MoE) + 1 × (Gated Attention → MoE)]. Small dense variants (0.8B–9B) use the same 3:1 pattern. https://build.nvidia.com/qwen/qwen3.5-397b-a17b/modelcard
- **Kimi Linear** (Oct 2025, arXiv 2510.26692): 48B-A3B with Kimi Delta Attention (channel-wise gated DeltaNet) : MLA at about 3:1. Up to 75% less KV cache and up to 6× faster decoding at 1M context (company-reported; critics note small training budget and baselines). https://arxiv.org/abs/2510.26692 ; https://kaitchup.substack.com/p/minimax-m2-and-kimi-linear-why-full
- **The counter-trend:** **MiniMax M2** (Oct 2025) returned to plain full attention after earlier hybrid "lightning attention" models. Its stated reasons: hybrids looked fine on benchmarks but degraded on multi-hop reasoning at scale, and full attention has far more mature kernels and inference tooling. https://kaitchup.substack.com/p/minimax-m2-and-kimi-linear-why-full
- **NVIDIA Nemotron 3** (white paper Dec 2025): a hybrid **Mamba-2 + MoE + few attention layers** family with up to 1M context. Nano 30B-A3B has 52 layers (23 Mamba-2, 23 MoE, 6 attention). **Super 120B-A12B** (report 11 Mar 2026) is the first in the family pre-trained in **NVFP4** (4-bit), with **LatentMoE** and multi-token prediction, and NVIDIA claims up to 2.2× the throughput of gpt-oss-120b. Ultra is listed in the gallery as 550B-A55B. https://arxiv.org/abs/2512.20856 ; https://arxiv.org/pdf/2604.12374 ; https://sebastianraschka.com/llm-architecture-gallery/hybrid-attention/
- **Mamba-3** (arXiv 2603.15569, ICLR 2026 oral; Lahoti, …, Dao, Gu). Adds a more expressive recurrence, complex-valued state updates and a MIMO formulation. At 1.5B parameters it beats Gated DeltaNet on average downstream accuracy and matches Mamba-2 perplexity with half the state. https://arxiv.org/abs/2603.15569 ; https://tridao.me/blog/2026/mamba3-part1/
- **TransMamba** (AAAI 2026): a research hybrid that switches between attention and Mamba with shared parameters. https://arxiv.org/abs/2503.24067
- **gpt-oss** (OpenAI, Aug 2025): **116.8B total / 5.1B active**, 36 layers, MoE weights in **MXFP4 (~4.25 bits)** so it fits on one 80 GB GPU. Alternating full and 128-token sliding-window attention, plus learned attention sinks (secondary sources for the last two). https://arxiv.org/abs/2508.10925
- **Llama 4** (Meta, April 2025): MoE throughout. Scout is 17B active / 109B total / 16 experts with a 10M-token context claim. Maverick is 17B active / 400B total / 128 routed experts + 1 shared. Early-fusion multimodality and **iRoPE** (some attention layers have no positional embedding). https://ai.meta.com/blog/llama-4-multimodal-intelligence/

### Diffusion language models
- **Inception Mercury 2** (24 Feb 2026), billed as the first *reasoning* diffusion LLM: ~1,009 tokens/s on Blackwell GPUs and 128K context (company-reported). https://the-decoder.com/inception-launches-mercury-2-the-first-diffusion-based-language-reasoning-model/
- **LLaDA2.0** (Dec 2025): scales diffusion LMs to 100B (MoE) by converting autoregressive models. LLaDA2.0-mini (16B) and -flash (100B) are open-sourced. https://arxiv.org/abs/2512.15745
- **Gemini Diffusion** was demoed at Google I/O (May 2025) and is reported to roughly match Gemini 2.0 Flash-Lite. It was still described as experimental in 2026 (secondary sources).

### Image generation
- **gpt-image-2 / ChatGPT Images 2.0** (OpenAI, **21 Apr 2026**) is an image model that can "think" (plan the composition) before drawing, with much-improved text rendering and up to 2K output (secondary coverage). https://www.techwyse.com/news/ai-search/openai-gpt-image-2-api-codex-launch
- The 2025 lineage: GPT-4o native image generation (March 2025, autoregressive), Google "Nano Banana" (Gemini 2.5 Flash Image, Aug 2025), Nano Banana Pro (Gemini 3 Pro Image, Nov 2025), Black Forest Labs **FLUX.2** (Nov 2025; open-weight "dev" tier ~32B), and Midjourney V7 (2025) → V8.x (2026, secondary). Teaching point: top image systems are now a mix of diffusion/flow-matching Transformers and LLM-integrated autoregressive generators, often combined.

### Video and world models
- **Veo 3** (May 2025) generated native synchronized audio. **Veo 3.1** (15 Oct 2025) is still listed by DeepMind as its leading video model, with native audio and 1080p/4K output. https://deepmind.google/models/veo/
- **Sora 2** launched 30 Sept 2025 with a social app. **OpenAI discontinued the Sora web/app on 26 Apr 2026, with the API ending 24 Sept 2026.** Sora continues as a world-model research project; reporting ties this to redirecting compute to coding and enterprise. https://the-decoder.com/openai-sets-two-stage-sora-shutdown-with-app-closing-april-2026-and-api-following-in-september/ ; https://help.openai.com/en/articles/20001152-what-to-know-about-the-sora-app-discontinuation
- **Gemini Omni** (Google I/O, 19 May 2026) is a multimodal family combining Gemini with Veo, Nano Banana and Genie: any input in, video out, with conversational editing. The first model was "Gemini Omni Flash". https://www.businesstoday.in/technology/artificial-intelligence/story/google-io-2026-google-unveils-gemini-omni-ai-video-editing-model-532350-2026-05-19
- **Genie 3** (DeepMind, Aug 2025) is a real-time interactive world model: text → explorable world at 720p/24 fps, consistent for a few minutes. https://techcrunch.com/2025/08/05/deepmind-reveals-genie-3-a-world-model-that-could-be-the-key-to-reaching-agi
- **Other leading video models in 2026** (secondary sources): Kling 3.0, ByteDance Seedance 2.0, Runway Gen-4.5, Alibaba Wan (open weights). https://provimedia.de/en/blog/ai-video-tools-2026

### Frameworks
- **PyTorch 2.11** (23 Mar 2026): 2,723 commits from 432 contributors. FlexAttention gained a FlashAttention-4 backend (1.2–3.2× faster on compute-bound workloads). **The release cadence increased to every 2 months in 2026.** https://pytorch.org/blog/pytorch-2-11-release-blog/
- **TensorFlow** retains a large enterprise base. One 2026 source claims Google moved it toward maintenance mode with 2.21 (March 2026) and steers new generative-AI work to Keras 3/JAX/PyTorch. This is **unverified** against Google's own notes and must be checked before printing. **JAX** is Google DeepMind's main research stack. **Keras 3** is multi-backend. https://tech-insider.org/pytorch-vs-tensorflow-2026/

### Education tools (useful for exercises)
- **Transformer Explainer** (Georgia Tech Polo Club) runs live GPT-2 in the browser (AAAI 2025; CHI 2026). https://poloclub.github.io/transformer-explainer/ . **Diffusion Explainer** does the same for Stable Diffusion. https://poloclub.github.io/diffusion-explainer/

### Big-picture 2026 convergence (synthesis for the chapter's ending)
Frontier open designs in 2026 tend to combine: (1) sparse MoE with hundreds of experts and ~3–5% of parameters active; (2) attention that is cheaper than full softmax attention (GQA/MLA, sliding windows, sparse/compressed attention, or linear/SSM hybrids at ~3:1); (3) 1M-token contexts; (4) 4–8-bit training and inference formats (FP8, MXFP4, NVFP4); (5) stability tricks (QK-norm/clip, gated attention, mHC); (6) Muon-family optimizers; and (7) multi-token prediction. Closed labs (OpenAI, Anthropic, Google) disclose little, so the book should say plainly that their architectures are not public.

---

## 5. Diagram ideas (22)

1. **"The neuron as a recipe card."** Three input circles (x1 = sunny 1, x2 = temp 0.8, x3 = workday 1) with arrows labeled by weights (w1 = 2, w2 = 1, w3 = −3) into a Σ box (+ bias b = 0.5). Then an arrow into an activation box (sigmoid curve icon) and the output "0.6 → go to the beach?". Show the arithmetic under each arrow.
2. **Activation function gallery.** Six small plots in a 2×3 grid: step, sigmoid, tanh, ReLU, GELU, SiLU. Each has the x-axis from −4 to 4, a one-line caption ("squashes to 0–1", "zero for negatives") and a red note on sigmoid's flat tails: "gradient ≈ 0 here → vanishing".
3. **Why non-linearity matters.** Left: two stacked linear layers collapse into one line (equation boxes merging). Right: the same data (a spiral or two moons) separated by a curved boundary only after adding ReLU.
4. **A small network, labeled.** A 3-4-4-2 network with layers labeled "input / hidden 1 / hidden 2 / output", one highlighted path, and a parameter-count tally box ("3×4+4 = 16, 4×4+4 = 20, 4×2+2 = 10 → 46 parameters"). Callout: "GPT-scale: same idea, ×1,000,000,000".
5. **Loss landscape hike.** A 3-D bumpy surface with a hiker (a dot) taking steps downhill, a "learning rate = step length" ruler, and three inset trajectories: too small (tiny steps, not done), just right, too large (zig-zag and overshoot off the chart).
6. **Backprop as blame flowing backward.** The network from Diagram 4 with green forward arrows (activations) on top and red backward arrows (gradients) underneath, a loss box at the right edge, and chain-rule gears ("∂loss/∂w = gear1 × gear2 × gear3") along the bottom.
7. **The training loop wheel.** A circular cycle: "Get batch" → "Forward pass" → "Compute loss" → "Backward pass" → "Optimizer update" → back to the start. Side counters show "step", "epoch" and "loss ↓" over time as a mini chart.
8. **Optimizer race.** A 2-D contour map (elongated valley) with four colored paths from the same start: SGD (zig-zag), momentum (smooth, overshoots), Adam (direct), and a Muon caption ("rescales the whole update matrix so all directions move evenly"). A legend says which is which.
9. **Overfitting curves.** Training loss steadily falling, validation loss falling then rising, a vertical dashed line at "early stopping point", and shaded regions labeled "underfitting / good fit / overfitting". Inset: three curve fits through dots (too straight, just right, wiggly).
10. **Residual connection highway.** A stack of 6 blocks with a straight vertical "highway" arrow bypassing each, with "+" junctions. Annotation: "output = input + f(input)". A side panel shows the gradient signal fading without skips (gray to white) vs. staying strong with skips.
11. **Convolution step by step.** A 6×6 grid of pixel numbers (a vertical edge), a 3×3 filter [[1,0,−1]…], the filter highlighted at one position with the multiply-add written out, and the resulting 4×4 feature map with the edge column lit up. Then a pooling 2×2 → max arrow.
12. **CNN feature hierarchy.** Image of a cat → layer 1 thumbnails (edges, color blobs) → layer 3 (textures, eyes) → layer 5 (faces, ears) → "cat 97%". The receptive-field cone widens with depth.
13. **RNN unrolled vs. Transformer.** Top: a chain of RNN boxes for "The cat sat on the mat", each passing a hidden-state arrow to the next, with a "must go one at a time" clock icon. Bottom: the same six tokens with every token connected to every other in one layer, labeled "all at once (parallel)".
14. **Embedding map.** A 2-D scatter of words: royal cluster (king, queen, prince), food cluster, countries/capitals with parallel arrows (France→Paris, Japan→Tokyo), and a vector-arithmetic parallelogram man→woman, king→queen. Caption: "real spaces have thousands of dimensions; this is a flattened shadow".
15. **Self-attention as a spotlight table.** The sentence "The animal didn't cross the street because it was tired". Above it: Q, K, V boxes per token. A heat-map matrix (rows = queries, columns = keys) with "it" → "animal" brightest. Bottom: a weighted-sum arrow producing the new vector for "it".
16. **Q/K/V library analogy panel.** Query = "a book about baking"; keys = spine labels; values = the books' contents. Match scores → softmax percentages (70%, 20%, 10%) → "blend of contents handed back".
17. **The Transformer block (decoder-only), full stack.** Bottom to top: token IDs → embedding lookup → (+RoPE applied to Q,K) → [RMSNorm → masked multi-head attention → +] → [RMSNorm → MLP or MoE → +] × N → final norm → unembedding → logits → softmax → "next token: 'Paris' 91%". A side callout zooms into the causal mask triangle.
18. **Mixture of experts router.** A token vector enters a router box that shows scores for 8 experts, two highlighted (top-2). Only those two light up, and their outputs are weighted and summed. A side label reads "Total params: all 8 experts; active params: 2". A bar comparing DeepSeek V4-Pro 1.6T total vs. 49B active.
19. **Attention vs. SSM vs. hybrid memory.** Three columns. Full attention: a growing pile of KV-cache "index cards", one per token. SSM/linear: a fixed-size notebook that gets overwritten. Hybrid: mostly notebooks, with every 4th layer keeping index cards (Qwen3.5 / Kimi Linear 3:1). Memory-vs-length mini-graph: a linear rising line vs. a flat line.
20. **Diffusion forward and reverse.** Top row: a photo of a dog → progressively noisier → pure static (t = 0 … T) with arrow "add noise (fixed, easy)". Bottom row reversed: static → … → dog, with a U-Net/DiT icon at each arrow, labeled "predict & remove noise (learned)". A text prompt box feeds in via a "cross-attention" arrow. A slider icon labels "guidance scale".
21. **Latent diffusion pipeline (Stable Diffusion).** Prompt → text encoder (CLIP/T5) → embeddings. Random latent (64×64×4) → denoiser loop × N steps (with text via cross-attention) → VAE decoder → 512×512 image. Size annotations show "48× smaller than pixels".
22. **Generative-model family tree.** A timeline from 2013 to 2026: Autoencoder → VAE (2013) → GAN (2014) → PixelRNN/autoregressive → DDPM (2020) → latent diffusion/SD (2022) → DiT (2022) → flow matching (2022–24, SD3/FLUX) → video DiTs (Sora 2024, Veo 3 2025) → diffusion LLMs (2025–26) / world models (Genie 3). Each node has a thumbnail.
23. **CLIP contrastive grid.** A 4×4 matrix with images down the side and captions across the top. The diagonal is bright ("match → pull together") and off-diagonals are dark ("mismatch → push apart"). Below: a zero-shot classifier using the same space.
24. **The 2026 frontier recipe card.** A labeled cutaway of a modern open LLM layer stack: MoE MLP (hundreds of experts), mixed attention (linear 3 : 1 full, or sparse/compressed), RMSNorm/QK-norm, mHC residual streams, RoPE, FP8/FP4 tags, optimizer badge "Muon". Footer: "Closed frontier labs don't publish theirs."

---

## 6. Practical exercises (easy → hard)

**1. Tokenize your own sentences (5 min, browser).** Go to https://tiktokenizer.vercel.app or OpenAI's tokenizer page. Paste "strawberry", "Strawberry", " strawberry", a sentence in your native language, a URL and a number like 123456789. Count the tokens and note the splits. *Learn:* models read chunks, not letters. This explains odd spelling and counting mistakes, and why non-English text can cost more tokens.

**2. Be a neuron with pencil and paper (15 min).** Use Diagram 1's beach decision with your own weights. Compute weighted sum + bias, then apply ReLU and a step function. Change one weight and see the decision flip. *Learn:* a neuron is just multiply-add-squish, and "learning" means changing those numbers.

**3. Teachable Machine (20 min, webcam).** At https://teachablemachine.withgoogle.com, make an image project with three classes (e.g., thumbs up, thumbs down, nothing). Record about 50 images each, train, and test. Then sabotage it: train with only 5 images, or with one class always under different lighting. *Learn:* data quantity and quality and shortcut learning (the model may learn the lighting, not the gesture), plus transfer learning (it reuses a pretrained network).

**4. Chatbot as tutor: explain-back (20 min).** Ask your chatbot: "Explain backpropagation to me using a bakery analogy, then quiz me with 5 questions and grade my answers." Then: "What's one thing about your own architecture that's publicly known, and one that isn't?" *Learn:* active recall, plus the habit of separating disclosed facts from speculation.

**5. TensorFlow Playground: the power of non-linearity (30 min).** At https://playground.tensorflow.org, (a) choose the "circle" dataset, no hidden layers, linear activation, and press play: it fails. (b) Add one hidden layer with 4 neurons and ReLU: it succeeds. (c) Try the spiral dataset, then add layers and neurons until it works. (d) Set learning rate to 3 or 10 and watch it explode. (e) Add noise and set the train/test ratio to 10%, and look for overfitting. *Learn:* activation functions, depth vs. width, learning rate, overfitting, and the meaning of the loss chart.

**6. Spreadsheet gradient descent (45 min, Google Sheets/Excel).** Fit y = w·x to data (x = 1,2,3,4; y = 2,4,6,8). Column A holds step number and B holds w (start 0). C computes loss = average of (w·x − y)². D computes gradient = average of 2·x·(w·x − y). Row n+1 sets w = w − lr × gradient. Try lr = 0.01, 0.05 and 0.2, and chart w and loss. *Learn:* gradient descent is literally "move against the slope", and learning rate controls convergence or divergence.

**7. One-neuron backprop by hand (45 min, paper).** Use input x = 2, weight w = 0.5, bias b = 0, sigmoid output, target 1, squared-error loss. Compute the forward pass, then dLoss/dOutput, dOutput/dSum (sigmoid' = s(1−s)) and dSum/dw = x. Multiply them (chain rule), update w with lr = 1, and recompute: the loss went down. *Learn:* the chain rule as multiplying local slopes, which is all backprop is.

**8. Convolution by hand (30 min, graph paper).** Draw a 6×6 grid with a dark left half (values 9) and a light right half (0). Apply a 3×3 vertical-edge filter [[1,0,−1],[1,0,−1],[1,0,−1]] at every position to produce a 4×4 map. Then apply 2×2 max pooling. Next, try a horizontal-edge filter. *Learn:* filters detect patterns, feature maps show where they are, and pooling summarizes.

**9. CNN Explainer (30 min).** At https://poloclub.github.io/cnn-explainer/, click through each layer of TinyVGG classifying an image. Hover over a neuron to see its convolution animated, then upload your own image. *Learn:* how channels, ReLU, pooling and softmax produce class probabilities, and how the feature hierarchy looks in practice.

**10. Embedding Projector (30 min).** At https://projector.tensorflow.org (Word2Vec 10K preloaded), search "king", "paris" and "happy" and inspect the nearest neighbors. Switch between PCA, t-SNE and UMAP. Isolate 100 points around "doctor" and look for social bias in the neighbors. *Learn:* meaning as geometry, dimension reduction, and how embeddings absorb societal biases.

**11. Attention on paper (45 min).** Take three tokens with 2-D vectors (set Q = K = V for simplicity): "cat" [1,0], "sat" [0,1], "it" [0.9,0.1]. For "it", compute dot products with each token (0.9, 0.1, 0.82). Divide by √2, take softmax (use e^x ≈ a calculator), and compute the weighted sum of values. *Learn:* attention is just similarity → percentages → blend, and "it" ends up mostly "cat".

**12. Transformer Explainer (45 min).** At https://poloclub.github.io/transformer-explainer/, type "Data visualization empowers users to". Expand the embedding, Q/K/V, attention heat map, MLP and output probabilities. Move the temperature slider from 0.2 to 2 and sample several times. *Learn:* the full decoder-only pipeline on real GPT-2, the causal mask (upper triangle blank), and how temperature reshapes probabilities.

**13. LLM Visualization in 3-D (30 min).** At https://bbycroft.net/llm, step through the nano-GPT walkthrough and compare it visually with GPT-2 and GPT-3 sizes. *Learn:* the actual matrix shapes and the sheer scale difference between toy and real models.

**14. GAN Lab (30 min).** At https://poloclub.github.io/ganlab/, pick the ring distribution and train. Watch the generator's points chase the real distribution while the discriminator's background colors shift. Try a high generator learning rate and look for mode collapse. *Learn:* adversarial training and why it's unstable.

**15. Diffusion Explainer (30 min).** At https://poloclub.github.io/diffusion-explainer/, step through the timesteps for a prompt. Change the guidance scale (low → bland/off-prompt, high → oversaturated), change the seed, and edit one word of the prompt. *Learn:* denoising in latent space, classifier-free guidance, and the role of seeds.

**16. Chatbot image-model experiment (30 min, any image-capable chatbot).** Generate the same scene with 3 prompt variants: plain, with style words, and with exact text on a sign. Then ask for an edit ("make it night, keep everything else"). Record what stays consistent. *Learn:* text conditioning, editing vs. regenerating, and current limits (text rendering, counting, hands, consistency).

**17. Colab: train your first network on handwritten digits (45 min).** Open https://colab.research.google.com, choose New notebook, paste the code below, and press Run:
```python
import tensorflow as tf
(x_tr, y_tr), (x_te, y_te) = tf.keras.datasets.mnist.load_data()
x_tr, x_te = x_tr/255.0, x_te/255.0
model = tf.keras.Sequential([tf.keras.Input(shape=(28,28)),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation="relu"),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10, activation="softmax")])
model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])
model.fit(x_tr, y_tr, epochs=5, validation_split=0.1)
model.evaluate(x_te, y_te)
```
Then change one thing at a time: 128 → 8 neurons, epochs 5 → 1, add a second Dense layer, remove Dropout. *Learn:* the training loop, epochs, validation accuracy, and capacity. Expect about 97–98% test accuracy.

**18. Colab: king − man + woman (20 min).**
```python
!pip install -q gensim
import gensim.downloader as api
wv = api.load("glove-wiki-gigaword-100")
print(wv.most_similar(positive=["king","woman"], negative=["man"], topn=5))
print(wv.most_similar(positive=["paris","japan"], negative=["france"], topn=3))
print(wv.similarity("coffee","tea"), wv.similarity("coffee","airplane"))
```
Invent your own analogies and record which fail. *Learn:* vector arithmetic on meaning, its limits, and the fact that the library quietly excludes input words from the answers.

**19. Colab: see attention heads in GPT-2 (30 min).**
```python
!pip install -q bertviz transformers
from bertviz import head_view
from transformers import AutoTokenizer, AutoModel
tok = AutoTokenizer.from_pretrained("gpt2")
model = AutoModel.from_pretrained("gpt2", output_attentions=True)
inp = tok("The animal didn't cross the street because it was too tired", return_tensors="pt")
head_view(model(**inp).attentions, tok.convert_ids_to_tokens(inp["input_ids"][0]))
```
Click through layers and heads to find a head linking "it" to "animal". Change "tired" to "wide" and check whether "it" shifts toward "street". *Learn:* multi-head specialization, the causal pattern, and attention sinks (many heads stare at the first token).

**20. Colab: zero-shot image classification with CLIP (20 min).**
```python
!pip install -q transformers pillow
from transformers import pipeline
clf = pipeline("zero-shot-image-classification", model="openai/clip-vit-base-patch32")
url = "PASTE_ANY_IMAGE_URL_HERE"
print(clf(url, candidate_labels=["a photo of a dog","a photo of a cat","a painting","a diagram"]))
```
*Learn:* a shared image–text embedding space, classifying with labels the model was never trained on, and prompt wording effects ("a photo of…").

**21. Colab: generate images and turn the knobs (40 min; Runtime → change runtime type → GPU).**
```python
!pip install -q diffusers transformers accelerate
import torch
from diffusers import AutoPipelineForText2Image
pipe = AutoPipelineForText2Image.from_pretrained("stabilityai/sdxl-turbo",
        torch_dtype=torch.float16, variant="fp16").to("cuda")
g = torch.Generator("cuda").manual_seed(42)
pipe("a watercolor fox reading a book", num_inference_steps=1, guidance_scale=0.0, generator=g).images[0]
```
Try steps = 1, 2, 4 and seeds 42, 43, 44. *Learn:* seeds, step count, and that this "turbo" model is *distilled* to work in 1–4 steps. The model license is non-commercial, and a free Hugging Face account/token may be needed.

**22. Colab: optimizer race (40 min).** Ask a chatbot to "write a minimal PyTorch script that trains the same small MLP on a synthetic classification dataset with SGD, SGD+momentum, Adam, AdamW and torch.optim.Muon (Muon for 2-D weight matrices, AdamW for biases), and plots loss curves". Run it, then vary learning rates 10× up and down. *Learn:* optimizers differ in speed and stability, learning rate interacts with optimizer choice, and how to use an AI assistant as a coding partner.

**23. Colab: build a tiny GPT on Shakespeare (2–3 hours).** Follow Andrej Karpathy's "Let's build GPT: from scratch, in code, spelled out" video alongside its Colab notebook (linked from the video description), or the `nanoGPT` repo's shakespeare_char example. Change the number of layers/heads and the context length, and compare sample quality. *Learn:* every Transformer component in ~200 lines (embeddings, causal self-attention, MLP, residuals, layer norm, the training loop) and that "it's just next-character prediction."

**24. Capstone: architecture detective (1–2 hours, no code).** Pick two open models (e.g., Qwen3.5-397B-A17B and DeepSeek-V4-Flash). Read their Hugging Face model cards and `config.json` files, plus Raschka's LLM Architecture Gallery entries. Fill a table: layers, hidden size, attention type, experts (total/active), context length, precision, license. *Learn:* reading real architecture specs, and how this chapter's vocabulary maps onto actual frontier systems.

---

## 7. Areas of opportunity

**Careers and roles**
- **ML/AI engineer (applied):** fine-tunes, evaluates and deploys models (PyTorch, Hugging Face, vLLM). It is the largest-volume role, and understanding architectures sets candidates apart from people who only call APIs.
- **Research engineer / research scientist:** new architectures, optimizers and training recipes. Strong math plus large-scale engineering. Very competitive, with very high pay at frontier labs.
- **ML performance / kernel engineer:** writes GPU kernels (CUDA, Triton), works on attention implementations (FlashAttention-style) and low-precision (FP8/FP4) training. Chronically scarce, because every new architecture (DeltaNet, compressed attention, MoE) needs new kernels.
- **Inference optimization engineer:** quantization, KV-cache management, MoE serving, speculative decoding. Directly tied to cost savings.
- **Generative media specialist / AI artist / technical director:** diffusion pipelines, LoRA training, ControlNet workflows (ComfyUI), and video generation for advertising, film previsualization and games.
- **Evaluation and interpretability researcher:** diagnosing what models actually learned. It needs a deep understanding of the residual stream, attention and features.
- **Domain-specialist ML (science, medicine, climate):** GNNs for molecules and materials, diffusion for protein design, weather models. Domain knowledge plus DL basics is a rare combination.
- **AI educator / technical writer / developer advocate:** strong demand for people who can explain these systems accurately to non-experts (exactly this book's skill).

**Businesses**
- Vertical fine-tuned models (legal, medical, manufacturing vision) built on open weights (Qwen, DeepSeek, Llama, Nemotron, gpt-oss licenses permit commercial use, with conditions).
- Generative media studios and tools: product photography, ad variants, localization (video dubbing), and game assets. Watch platform churn (Sora's closure shows the risk of depending on a single vendor).
- Edge/on-device AI: small efficient models (SSM/hybrid, quantized) for phones, cars and factories, plus privacy-sensitive deployments.
- Synthetic data generation for training other models (images for vision QA, simulated scenarios via world models for robotics).
- Embedding-based products: semantic search, recommendation, deduplication and anomaly detection. These use mature, cheap technology and are underused by small and medium businesses.
- Training/inference infrastructure services: kernel optimization consulting, model compression, MoE serving.

**Skills in demand (2026)**
- Python + PyTorch fundamentals; reading model cards and configs.
- Understanding attention variants, MoE, KV-cache economics and quantization formats.
- Diffusion/flow-matching workflows; LoRA fine-tuning; evaluation design.
- GPU programming (Triton/CUDA); distributed training basics.
- Data curation: quality filtering and dataset construction, often valued more than architecture tweaks.
- Using AI coding assistants to prototype quickly, while being able to verify their output.

**Open research problems**
- **Efficient long context without losing recall:** whether hybrids (3:1 linear:full) truly match full attention on multi-hop reasoning at scale. The MiniMax M2 vs. Kimi Linear disagreement is unresolved.
- **Why optimizers like Muon work, and what comes next:** theory is behind practice (e.g., Newton-Muon 2026 tries to explain it).
- **Training stability at trillion-parameter scale:** loss spikes, attention-logit growth, residual-stream design (mHC), and 4-bit pretraining (NVFP4).
- **Diffusion language models:** can parallel denoising match autoregressive quality on reasoning, and how do they combine with RL and tool use?
- **World models and physical consistency in video:** long-horizon coherence and controllability (Genie 3 holds consistency for minutes, not hours).
- **Generalization theory:** why overparameterized networks generalize (double descent, implicit regularization, diffusion memorization timescales).
- **Interpretability:** superposition, feature circuits, how knowledge is stored in MLPs.
- **Continual learning / memory:** updating models without catastrophic forgetting, and test-time memory (Titans-style).
- **Small recursive models:** whether looping a small network many times (TRM-style) can substitute for scale on reasoning tasks.
- **Data efficiency:** learning from far fewer tokens, as humans do. JEPA-style predictive objectives are one bet.

---

## 8. Common misconceptions to correct

1. **"Neural networks work like the brain."** They are loosely *inspired* by neurons. Artificial neurons are simple multiply-add-squish units, and backpropagation is not how biological brains are known to learn.
2. **"The model looks things up in a database of its training data."** A plain LLM stores no documents. Its knowledge is spread across billions of weights as statistical associations. (Retrieval systems are a separate add-on.)
3. **"More layers/parameters is always better."** Only with enough data, compute and good training. Small, well-trained models routinely beat larger, poorly trained ones, and MoE "total parameters" overstate the compute used per token.
4. **"A 1-trillion-parameter MoE uses 1 trillion parameters per word."** Only the active parameters (e.g., 32B for Kimi K2, 49B for DeepSeek V4-Pro) compute each token, though all must be stored in memory.
5. **"Attention means the model is paying attention like a human."** It is a learned weighted average based on vector similarity, a routing mechanism. High attention weight doesn't necessarily explain the model's decision.
6. **"Each neuron represents one concept."** Usually not. Concepts are spread across many neurons, and neurons respond to many concepts (superposition).
7. **"Training is the model reading and understanding text like a student."** Pre-training is billions of tiny weight nudges to reduce next-token prediction error. Any "understanding" emerges from that process.
8. **"The chatbot learns from my conversation as we talk."** Weights are frozen during use. The model only "remembers" what is in its context window (or a separate memory feature), unless the provider later trains on data under its policies.
9. **"Diffusion models collage or copy pieces of training images."** They learn to denoise toward the data distribution and generate new pixels. They *can* memorize and regurgitate heavily duplicated images, which is a real legal and research issue, but this isn't how typical outputs are made.
10. **"Image generators 'see' the prompt and draw it."** Text is converted to embeddings that steer denoising via cross-attention. That's why exact counts, spatial relations and text on signs were historically weak (much improved by 2026's reasoning-based image models).
11. **"Universal approximation means neural networks can learn anything."** It only says suitable weights *exist*. It doesn't say how many neurons are needed, whether training finds them, or whether the result generalizes.
12. **"Backpropagation is the learning algorithm."** Backprop only *computes gradients*. The optimizer (SGD, Adam, Muon) decides how to change the weights.
13. **"Transformers replaced everything; CNNs and RNNs are dead."** CNNs still dominate many vision and edge uses. RNN ideas returned as SSMs, linear attention and the hybrids at the heart of Qwen3.5 and Nemotron 3.
14. **"Hybrid/linear attention is strictly better because it's cheaper."** It trades exact recall for efficiency, and some labs (MiniMax M2) went back to full attention after seeing reasoning regressions.
15. **"king − man + woman = queen exactly."** The nearest neighbor is queen only when the input words are excluded, and many analogies fail. The structure is approximate and also encodes biases.
16. **"Temperature makes the model more creative/intelligent."** It only changes how randomly it samples from the same probability distribution: higher means more varied and more error-prone.
17. **"Dropout/normalization/residuals are minor implementation details."** These "plumbing" choices are what made deep networks trainable at all. Frontier labs still innovate here (mHC, gated attention, DyT).
18. **"A model's architecture is its intelligence."** At the frontier, data quality, training compute, post-training (RL) and inference-time reasoning matter as much as or more than architectural details, which have largely converged.
19. **"Closed models like GPT-5 or Claude use architecture X."** Their architectures are not publicly disclosed. Claims about them are speculation unless the company has published them.
20. **"Video generators simulate physics."** They learn visual regularities from data. They often violate physics (objects merging, inconsistent counts), though world-model research aims to improve this.
21. **"You need a PhD in math to understand deep learning."** The core ideas are multiplication, addition, slopes and averages. The math formalizes what can be explained visually.

---

## 9. Analogies that work for beginners

- **Neural network = a giant mixing console.** Billions of sliders (weights). Training is an automated sound engineer nudging every slider slightly after each song until the mix sounds right.
- **Neuron = a voting committee member.** Each input "argues" with a strength (weight), the bias is the member's prior mood, and the activation decides whether the member speaks up.
- **Activation function = a dimmer with a floor (ReLU).** Below zero the light is off, above zero it gets brighter. Without dimmers, all you can build are straight lines.
- **Depth = an assembly line.** Each station adds one refinement: edges → shapes → parts → objects. Features are built from features.
- **Loss = a golf score.** One number for how far off you are. Lower is better.
- **Gradient descent = walking downhill in fog with a slope-meter.** You can't see the valley, but you can feel which way is down under your feet. The learning rate is the length of your stride.
- **Backpropagation = tracing blame in a kitchen.** The soup is too salty. How much is the head chef at fault, how much the sous-chef who seasoned the stock, how much the supplier? Blame flows backward in proportion to each person's influence.
- **Chain rule = gears.** Turn the first gear, and the last gear's speed is the product of all the gear ratios in between.
- **Momentum = a bowling ball vs. a ping-pong ball.** The heavy ball rolls through small bumps and keeps its direction.
- **Adam = a hiker with adjustable shoes.** Bigger strides on smooth terrain, careful steps on rocky terrain, decided separately for each direction.
- **Muon = balancing a team's workload.** Instead of letting one direction of change dominate, it evens out the update so every "direction" of the weight matrix moves at a similar pace.
- **Overfitting = memorizing the answer key.** Perfect on practice tests, lost on the real exam.
- **Dropout = randomly benching players in practice.** The team can't rely on one star, so everyone learns to contribute.
- **Normalization = re-leveling the audio between songs.** It keeps the volume in a sane range so nothing clips or fades out.
- **Residual connection = an express elevator plus optional stairs.** The signal can always take the express route, and each layer just adds a small correction.
- **Vanishing gradients = the telephone game.** After 50 people, the message whispered down the line is gone.
- **Convolution = a flashlight with a stencil.** Slide a small "vertical edge" stencil across a dark picture and it lights up wherever the pattern matches.
- **Pooling = making a thumbnail.** Keep the strongest signal in each little square, losing detail but keeping the gist.
- **RNN = reading a book while taking one Post-it note of notes.** You must keep rewriting the same small note, so early chapters fade.
- **Embeddings = coordinates on a map of meaning.** Similar words live in the same neighborhood. Directions can mean things, such as "male→female" or "country→capital".
- **Tokens = Scrabble tiles.** Text is broken into reusable pieces, sometimes whole words and sometimes fragments.
- **Self-attention = a cocktail party.** Each guest (token) scans the room, asks "who's relevant to me?", and blends in what the relevant people are saying.
- **Q/K/V = a library search.** Query = what you're looking for, key = the label on each book's spine, value = the book's contents. You borrow a blend of the best-matching books.
- **Multi-head attention = a panel of specialists.** One editor checks grammar, another tracks who "she" refers to, another follows the timeline, all reading the same page at once.
- **Positional encoding (RoPE) = clock hands.** Each position rotates the vector like a clock hand, and two tokens compare how far apart their hands point to know their distance.
- **Causal mask = a mystery novel read without peeking ahead.** You can only use pages you've already read to guess the next word.
- **Residual stream = a shared whiteboard.** Each layer reads the board, adds a note, and passes it on. Nobody erases.
- **KV cache = sticky notes about earlier parts of the conversation.** The longer the chat, the bigger the stack.
- **Mixture of experts = a hospital triage desk.** The receptionist (router) sends each patient (token) to two relevant specialists instead of making every doctor see everyone.
- **SSM / Mamba = a running summary notebook.** Fixed size, constantly updated, cheap to carry, but details get overwritten. Full attention = a filing cabinet of every page (perfect recall, grows forever). Hybrid = mostly notebooks, with a filing cabinet every few floors.
- **GNN = gossip in a village.** Each house updates its opinion based on its neighbors. After a few rounds, news has spread across the graph.
- **Autoencoder = packing a suitcase.** Compress everything into a small bag (latent), then unpack it at the destination. What survives shows what mattered.
- **VAE = describing a face with sliders instead of a photo.** Any slider setting gives a plausible face, so you can explore between them.
- **GAN = art forger vs. detective.** Each gets better because the other does.
- **Diffusion = a sculptor removing marble, or restoring a photo from static.** Learn to clean up a little noise at a time, then start from pure static and clean, step by step, toward what the prompt describes.
- **Classifier-free guidance = turning up the "follow the brief" knob.** Too low and the artist ignores you, too high and it overdoes everything.
- **Latent diffusion = sketching on a thumbnail, then upscaling.** Do the hard creative work in a small compressed space, then decode to full size.
- **Flow matching = straightening a winding mountain road into a highway.** It takes the same start (noise) to the same destination (image) in far fewer turns (steps).
- **CLIP = a bilingual dictionary between pictures and words.** Both are placed on one shared map so "photo of a dog" lands next to dog photos.
- **Diffusion LLM = filling in a crossword all at once.** Instead of writing left to right, it pencils in many squares in parallel and refines over a few passes.
- **Bitter Lesson = teaching to fish vs. handing out fish.** Methods that learn from more data and compute ultimately beat carefully hand-crafted rules.
- **Inductive bias = training wheels.** Helpful when data is scarce (CNNs on small image sets), unnecessary or limiting once you have huge data (ViTs at scale).
- **Frameworks (PyTorch/JAX/TensorFlow) = kitchen appliances.** You could cook over a fire (raw math), but these give you an oven with a thermostat (autograd, GPU support, ready-made layers).

---

### Key sources (consolidated)
- Muon (Keller Jordan): https://kellerjordan.github.io/posts/muon/
- Muon is Scalable: https://arxiv.org/abs/2502.16982
- Kimi K2 tech report: https://arxiv.org/abs/2507.20534
- PyTorch Muon docs: https://docs.pytorch.org/docs/2.11/generated/torch.optim.Muon.html
- PyTorch 2.11 release: https://pytorch.org/blog/pytorch-2-11-release-blog/
- NeurIPS 2025 best papers: https://blog.neurips.cc/?p=1443
- DyT: https://arxiv.org/abs/2503.10622
- mHC: https://arxiv.org/abs/2512.24880
- DeepSeek V4-Pro model card: https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro ; report https://arxiv.org/html/2606.19348v1
- Qwen3.5 model card (NVIDIA): https://build.nvidia.com/qwen/qwen3.5-397b-a17b/modelcard
- Raschka LLM Architecture Gallery (hybrid attention / attention distribution): https://sebastianraschka.com/llm-architecture-gallery/hybrid-attention/ ; https://www.sebastianraschka.com/llm-architecture-gallery/attention-mechanism-distribution/
- Kimi Linear: https://arxiv.org/abs/2510.26692
- MiniMax M2 full-attention discussion: https://kaitchup.substack.com/p/minimax-m2-and-kimi-linear-why-full
- Nemotron 3 white paper: https://arxiv.org/abs/2512.20856 ; Nemotron 3 Super report: https://arxiv.org/pdf/2604.12374
- Mamba-3: https://arxiv.org/abs/2603.15569 ; https://tridao.me/blog/2026/mamba3-part1/
- gpt-oss model card: https://arxiv.org/abs/2508.10925
- Llama 4: https://ai.meta.com/blog/llama-4-multimodal-intelligence/
- Mercury 2: https://the-decoder.com/inception-launches-mercury-2-the-first-diffusion-based-language-reasoning-model/
- LLaDA2.0: https://arxiv.org/abs/2512.15745
- gpt-image-2 (secondary): https://www.techwyse.com/news/ai-search/openai-gpt-image-2-api-codex-launch
- Veo: https://deepmind.google/models/veo/
- Sora shutdown: https://the-decoder.com/openai-sets-two-stage-sora-shutdown-with-app-closing-april-2026-and-api-following-in-september/
- Gemini Omni: https://www.businesstoday.in/technology/artificial-intelligence/story/google-io-2026-google-unveils-gemini-omni-ai-video-editing-model-532350-2026-05-19
- Genie 3: https://techcrunch.com/2025/08/05/deepmind-reveals-genie-3-a-world-model-that-could-be-the-key-to-reaching-agi
- Transformer Explainer / Diffusion Explainer: https://poloclub.github.io/transformer-explainer/ ; https://poloclub.github.io/diffusion-explainer/
