# External-standard coverage audit: deep learning

Audited October 21, 2026 against `ai-book/chapters/` and `ai-book/appendices/`. Each topic was located by searching the whole book for its key terms (a scripted term count per chapter, then reading the passages). Statuses: COVERED (explained at beginner level), THIN (mentioned but not explained), MISSING, OUT OF SCOPE (too specialized or mathematical for this reader; the reason is given, and the book names it in one line where the reader is likely to hear the term).

Standards:

1. Goodfellow, Bengio and Courville, *Deep Learning* (MIT Press, 2016), all three parts.
2. *Dive into Deep Learning* (d2l.ai), its chapter list.
3. Stanford course syllabi: CS229 (machine learning), CS231n (CNNs for visual recognition), CS224n (NLP with deep learning) and CS336 (language modeling from scratch).

All structures come from memory; web search was unavailable. Topics are grouped by chapter or unit. The words in the Topic column describe content and are not quoted section titles.

- **Goodfellow:** confident about the 20-chapter structure. The section topics within each chapter are grouped.
- **d2l:** follows the 1.0 edition's chapter order (Preliminaries through the Tools appendix). Sections are grouped, and their exact titles may differ.
- **CS229, CS231n and CS224n:** syllabi change every year. These rows list the units these courses are known to cover across their 2017–2025 offerings: CS229's main lecture notes; CS231n's lectures from classification to 3D, robot learning and human-centered AI; CS224n's lectures from word vectors to post-training, agents and reasoning.
- **CS336:** taught by Percy Liang and Tatsunori Hashimoto (offered in 2024 and 2025). The rows list the lecture and assignment topics as best known. The exact lecture order is uncertain.

Some gaps were filled while this audit was running by parallel external audits working on the same chapters. They are marked "parallel audit" below and are counted as THIN or MISSING before and COVERED after, with no action by this audit.

## 1. Goodfellow, Bengio and Courville, *Deep Learning* (2016)

| Topic | Status before | Where in the book | Action |
|---|---|---|---|
| Ch 2: scalars, vectors, matrices, tensors, matrix multiplication | COVERED | Ch 5 (dot product and matrix multiplication worked by hand, tensors) | None |
| Ch 2: norms and vector length | COVERED | Ch 5 cosine similarity; Ch 9 L1 and L2; Ch 13 gradient norm | None |
| Ch 2: eigendecomposition and SVD | MISSING | PCA in Ch 10 without the names; "singular values" used undefined in a Ch 13 Try-it | Added to Ch 10 (PCA section): eigenvector and SVD definitions, linked to LoRA and Muon |
| Ch 2: identity, inverse, span, pseudoinverse, trace, determinant | OUT OF SCOPE | None | Matrix machinery a reader never meets by name outside a math course |
| Ch 2: PCA as an application | COVERED | Ch 10 "Shrinking many columns into a few" | None |
| Ch 3: probability, distributions, conditional probability, chain rule, independence | COVERED | Ch 6 (probability, distributions, conditional probability, chaining sentence probabilities) | None |
| Ch 3: expectation, variance, covariance | COVERED | Ch 6 expected value, variance, correlation (covariance as a formula is out of scope) | None |
| Ch 3: common distributions and functions (Gaussian, sigmoid, softplus) | COVERED | Ch 6 normal distribution; Ch 12 activation gallery | None |
| Ch 3: Bayes' rule | COVERED | Ch 6 (natural frequencies); Ch 54 | None |
| Ch 3: information theory (entropy, KL divergence, cross-entropy) | THIN | Cross-entropy in Ch 6; KL only inside RLHF (Ch 20); entropy never defined | Added Ch 6 "Maximum likelihood, entropy and KL divergence" with a worked coin example (cross-entropy 1.204, entropy 0.693, KL 0.511) |
| Ch 3: structured probabilistic models | THIN | Ch 54 Bayesian network worked by hand; no umbrella term, no undirected models | Added to Ch 54: probabilistic graphical model, Markov random field |
| Ch 4: overflow, underflow, stable softmax | COVERED | Ch 18 subtract-the-largest-logit trick; Ch 13 NaN; Ch 5 and Ch 32 precision | None |
| Ch 4: gradient-based optimization, curvature | COVERED | Ch 6 gradients; Ch 13 curvature and second-order methods (Jacobians, Hessians and conditioning are out of scope) | None |
| Ch 4: constrained optimization (Lagrange, KKT) | OUT OF SCOPE | None | Pure math machinery |
| Ch 5: learning algorithms, capacity, overfitting and underfitting | COVERED | Ch 8, Ch 9 | None |
| Ch 5: hyperparameters and validation sets | COVERED | Ch 8, Ch 9 | None |
| Ch 5: estimators, bias and variance | COVERED | Ch 9 dartboard | None |
| Ch 5: maximum likelihood estimation | MISSING | Cross-entropy taught but never tied to MLE | Added MLE definition and explanation (Ch 6) |
| Ch 5: Bayesian statistics | COVERED | Ch 6 prior and posterior; Ch 54 | None |
| Ch 5: classic supervised and unsupervised algorithms | COVERED | Ch 10 | None |
| Ch 5: stochastic gradient descent | COVERED | Ch 6, Ch 12, Ch 13 | None |
| Ch 5: curse of dimensionality | COVERED | Ch 10 kNN (one-line explanation) | None |
| Ch 5: manifold learning (manifold hypothesis) | THIN | Ch 16 describes real images as a "tiny island" but does not use the name | Added term and definition (Ch 16, "Learning a distribution") |
| Ch 6: feedforward networks, XOR, hidden units, architecture design | COVERED | Ch 12; Ch 13 universal approximation | None |
| Ch 6: back-propagation and computational graphs | THIN | Ch 12 backprop worked by hand; "computational graph" never named | Added computational graph paragraph and definition (Ch 12) |
| Ch 7: norm penalties (L1, L2, weight decay) | COVERED | Ch 9; Ch 13 AdamW | None |
| Ch 7: dataset augmentation, early stopping, dropout | COVERED | Ch 13 regularization toolkit; Ch 9 | None |
| Ch 7: noise robustness and label smoothing | THIN | Only dropout and augmentation | Added label smoothing with a worked target, 0.91 and nine of 0.01 (Ch 13) |
| Ch 7: semi-supervised learning | COVERED | Ch 8 | None |
| Ch 7: multitask learning | COVERED | Ch 51 (defined) | Added a pointer to it as a regularizer (Ch 13) |
| Ch 7: parameter tying and sharing | COVERED | Ch 14 weight sharing | None |
| Ch 7: bagging and ensembles | COVERED | Ch 10 random forests | None |
| Ch 7: adversarial examples and training | COVERED | Ch 45 "How vision systems fail" (panda, stop sign, robust training); Ch 14 Watch out | None |
| Ch 7: sparse representations, tangent prop, manifold tangent classifier | OUT OF SCOPE | Sparse autoencoders in Ch 57 cover the live use | Obsolete or too specialized |
| Ch 8: local minima, saddle points, plateaus, cliffs, exploding gradients | COVERED | Ch 6 "Valleys, plateaus"; Ch 13 saddle point, gradient clipping | Added convexity (Ch 6) |
| Ch 8: SGD and momentum | COVERED | Ch 13 (the Nesterov variant is out of scope) | None |
| Ch 8: parameter initialization | COVERED | Ch 13 | None |
| Ch 8: adaptive learning rates (AdaGrad, RMSProp, Adam) | THIN | Ch 13 covers RMSProp and Adam; AdaGrad absent | Added AdaGrad sentence (Ch 13) |
| Ch 8: approximate second-order methods | COVERED | Ch 13 Shampoo, SOAP, curvature (Newton's method and BFGS are out of scope by name) | None |
| Ch 8: batch normalization | COVERED | Ch 13 | None |
| Ch 8: Polyak averaging, coordinate descent | OUT OF SCOPE | Weight averaging appears as model soups (Ch 20) | Too specialized |
| Ch 8: supervised pretraining, curriculum learning | COVERED | Ch 14 transfer learning; Ch 19 curriculum (defined) | None |
| Ch 9: convolution, sparse interactions, parameter sharing, equivariance, pooling | COVERED | Ch 14 (worked convolution; "its features move with it") | None |
| Ch 9: stride, padding, structured outputs | COVERED | Ch 14 stride and padding, U-Net; Ch 45 segmentation | None |
| Ch 9: efficient convolution, neuroscientific basis | COVERED | Ch 14 Hubel and Wiesel (FFT and Winograd algorithms are out of scope) | Added efficient CNN designs (Ch 14) |
| Ch 10: unfolding, RNNs, BPTT | COVERED | Ch 14 | None |
| Ch 10: bidirectional RNNs | MISSING | The word "bidirectional" appeared nowhere in the book | Added Ch 14 "Stacking layers and reading both ways" (Teddy example) |
| Ch 10: encoder–decoder (seq2seq) | COVERED | Ch 14 | None |
| Ch 10: deep recurrent networks | MISSING | Only "stacks of LSTM layers" in passing | Added stacked RNN definition, with GNMT's 8 + 8 layers (Ch 14) |
| Ch 10: recursive nets, echo state networks, leaky units | OUT OF SCOPE | None | Niche or historical; the reader is unlikely to meet them |
| Ch 10: long-term dependencies, LSTM and GRU, gradient clipping | COVERED | Ch 14; Ch 13 | None |
| Ch 10: explicit memory (neural Turing machines) | MISSING | None | Added memory-augmented networks: NTM, Memory Networks, DNC (Ch 17) |
| Ch 11: metrics, default baselines | COVERED | Ch 9 | None |
| Ch 11: whether to gather more data, debugging strategies | THIN | Ch 9 "more data" fix; Ch 13 reading loss curves | Added Ch 13 debugging checklist (starting loss ln 10 = 2.30, overfit one batch; learning curve and error analysis defined) |
| Ch 11: hyperparameter selection (manual, grid, random, model-based) | COVERED | Ch 9 | Added successive halving and Hyperband (Ch 9) |
| Ch 12: large-scale deep learning (GPUs, distributed, compression, dynamic structure, hardware) | COVERED | Ch 32–37; Ch 23 quantization; Ch 53 pruning and distillation; Ch 17 MoE | None |
| Ch 12: applications (vision, speech, n-grams, neural language models, NMT, recommenders, knowledge, QA) | COVERED | Ch 45, 46, 6, 14, 18, 51, 54, 27 | None |
| Ch 13: probabilistic PCA, factor analysis | OUT OF SCOPE | Ch 10 PCA | Statistical machinery |
| Ch 13: independent component analysis | OUT OF SCOPE | None | Now named in one line (Ch 10, cocktail-party use) |
| Ch 13: slow feature analysis, sparse coding | OUT OF SCOPE | The sparse dictionary idea lives on in Ch 57 SAEs | None |
| Ch 14: autoencoders (undercomplete, denoising, sparse) | COVERED | Ch 16; Ch 57 sparse autoencoders (contractive ones are out of scope) | None |
| Ch 15: greedy layer-wise unsupervised pretraining | THIN | Ch 7 said only "a way to train networks with many layers" | Added definition (Ch 16); clarified the Ch 7 history line |
| Ch 15: transfer learning, domain adaptation, distributed representations, gains from depth | COVERED | Ch 14; Ch 9 and Ch 45 distribution shift; Ch 13 "Why depth beats width" | None |
| Ch 16: directed and undirected graphical models, RBMs | THIN | Ch 54 Bayesian networks only | Added PGM and MRF (Ch 54); Boltzmann machine and RBM (Ch 16) |
| Ch 17: Monte Carlo methods, MCMC, Gibbs sampling | OUT OF SCOPE | Ch 54 Monte Carlo inference and MCMC (parallel audit) | Named; Gibbs sampling is out of scope |
| Ch 18: partition function, contrastive divergence, score matching, NCE | OUT OF SCOPE | None | Named the partition function and score-based models in one line each (Ch 16); CD and NCE are too technical |
| Ch 19: approximate inference (variational inference, EM, wake–sleep) | OUT OF SCOPE | Ch 16 VAE | Named variational inference (Ch 54); EM fully explained for CS229 (Ch 10) |
| Ch 20: Boltzmann machines, RBMs, deep belief networks | MISSING | Appendix C timeline and one Ch 7 line only | Added Ch 16 "Energy-based models and Boltzmann machines" (Nobel link, the 2006 DBN) |
| Ch 20: VAEs, GANs, reparameterization | COVERED | Ch 16 | None |
| Ch 20: autoregressive networks (PixelCNN, WaveNet) | COVERED | Ch 16; Ch 46 | None |
| Ch 20: evaluating generative models | MISSING | None | Added Ch 16 "How do you grade a generator?" (likelihood, FID, CLIP score, human preference) |
| Ch 20: generative stochastic networks, moment matching | OUT OF SCOPE | None | Obsolete |

**Counts (72 topics).** Before: 44 COVERED, 9 THIN, 7 MISSING, 12 OUT OF SCOPE. After: 60 COVERED, 12 OUT OF SCOPE.

## 2. Dive into Deep Learning (d2l.ai)

| Topic | Status before | Where in the book | Action |
|---|---|---|---|
| Introduction: kinds of ML problems, roots, successes | COVERED | Ch 1, Ch 7, Ch 8 | None |
| Preliminaries: data manipulation and preprocessing | COVERED | Ch 3; Ch 11 | None |
| Preliminaries: linear algebra, calculus, autograd, probability | COVERED | Ch 5, Ch 6, Ch 12 | None |
| Linear regression; generalization | COVERED | Ch 8 (spreadsheet); Ch 9 | None |
| Weight decay | COVERED | Ch 9; Ch 13 | None |
| Softmax regression | THIN | Ch 6 softmax; logistic regression in Ch 8 and Ch 10, without the name | Added softmax regression and GLM definitions (Ch 10) |
| Image classification datasets (MNIST, Fashion-MNIST) | COVERED | Ch 11; Ch 14 | None |
| Environment and distribution shift | COVERED | Ch 9; Ch 45; Ch 10 drift | None |
| MLPs; forward and backward propagation, computational graphs | THIN | Ch 12 (the graph is not named) | Added computational graph (Ch 12) |
| Numerical stability and initialization | COVERED | Ch 13 | None |
| Generalization in deep learning; dropout | COVERED | Ch 13 | None |
| Kaggle house-price project | COVERED | Ch 10 toolbox and exercises | None |
| Builder's guide: modules, parameters, custom layers, file I/O, GPUs | COVERED | Ch 13 frameworks and annotated script; Ch 19 checkpoints | None |
| CNNs: convolution, padding, stride, channels, pooling, LeNet | COVERED | Ch 14 | None |
| Modern CNNs: AlexNet, VGG, GoogLeNet, ResNet | COVERED | Ch 14 hall of fame | None |
| NiN and 1 × 1 convolutions | MISSING | None | Added 1 × 1 convolution (Ch 14 "After ResNet") |
| Batch normalization | COVERED | Ch 13 | None |
| DenseNet, ResNeXt, design spaces | MISSING | Only ConvNeXt mentioned | Added DenseNet, MobileNet and EfficientNet, with a depthwise-separable worked count of 589,824 vs 67,840 weights (Ch 14); ResNeXt and RegNet are out of scope by name |
| Sequences, text to tokens, language models, perplexity | COVERED | Ch 14; Ch 15 and Ch 18 tokenization; Ch 6 n-gram model and perplexity | None |
| RNNs, BPTT | COVERED | Ch 14 | None |
| LSTM, GRU | COVERED | Ch 14 | None |
| Deep and bidirectional RNNs | MISSING | None | Added (Ch 14) |
| Machine translation, encoder–decoder, seq2seq | COVERED | Ch 14; Ch 54 | None |
| Beam search | MISSING | Not mentioned anywhere in the book | Added Ch 18 "Beam search: looking a few steps ahead" (worked mat 0.12 vs sofa 0.28; beam search and beam width defined) |
| Queries, keys, values; attention pooling; scoring functions; Bahdanau | COVERED | Ch 14; Ch 15 Step 4 | None |
| Multi-head attention, self-attention, positional encoding, Transformer | COVERED | Ch 15 | None |
| Vision Transformers; large-scale pretraining | COVERED | Ch 15; Ch 19 | None |
| Optimization and deep learning; convexity | THIN | Ch 6 landscapes; "convex" absent | Added convex function (Ch 6) |
| GD, SGD, minibatch SGD, momentum | COVERED | Ch 6, Ch 12, Ch 13 | None |
| Adagrad, RMSProp, Adadelta, Adam | THIN | Ch 13 RMSProp and Adam only | Added AdaGrad (Ch 13); Adadelta is out of scope by name |
| Learning-rate scheduling | COVERED | Ch 13 | None |
| Compilers and interpreters, asynchronous computation, automatic parallelism | COVERED | Ch 3 compilers vs interpreters; Ch 13 eager vs compiled frameworks (asynchronous execution details are out of scope) | None |
| Hardware, multi-GPU training, parameter servers | COVERED | Ch 32–34; Ch 37 data parallelism and all-reduce (parameter servers are superseded) | None |
| Image augmentation, fine-tuning | COVERED | Ch 13; Ch 14 | None |
| Object detection: boxes, anchors, SSD, R-CNN | COVERED | Ch 45 (YOLO, NMS, R-CNN named; anchor boxes are out of scope) | None |
| Semantic segmentation, transposed convolution, FCN | COVERED | Ch 45; Ch 14 U-Net up path | None |
| Neural style transfer | MISSING | None | Added (Ch 14 "Looking inside a trained CNN") |
| word2vec, GloVe, subword embeddings, word similarity and analogy | COVERED | Ch 14; Ch 5; Ch 15 and Ch 18 BPE | None |
| Negative sampling, hierarchical softmax | OUT OF SCOPE | None | word2vec training shortcuts the reader will not meet |
| BERT and its pretraining | COVERED | Ch 15 Step 8; Ch 16 | None |
| Sentiment analysis | COVERED | Ch 54 classic NLP tasks | None |
| Natural language inference | MISSING | None | Added NLI row and definition (Ch 54) |
| Fine-tuning BERT for sequence and token tasks | COVERED | Ch 14 transfer learning; Ch 15 encoder-only uses | None |
| Reinforcement learning: MDPs, value iteration, Q-learning | THIN | Ch 48 Q-learning worked by hand; MDP and value iteration (parallel audit) | None (parallel audit) |
| Gaussian processes | MISSING | None | Added definition and paragraph after the kernel trick (Ch 10) |
| Hyperparameter optimization, random search | COVERED | Ch 9 | None |
| Multi-fidelity HPO (successive halving, Hyperband) | MISSING | None | Added with a worked example, 108 vs 729 epochs (Ch 9) |
| GANs, DCGAN | COVERED | Ch 16 (GAN Lab exercise) | None |
| Recommenders: matrix factorization, ranking, sequence-aware | COVERED | Ch 10; Ch 51 | None |
| AutoRec, NeuMF, factorization machines, DeepFM | OUT OF SCOPE | Ch 51 two-tower and multi-task ranking carry the modern ideas | Specific model names |
| Math appendix (eigendecomposition, MLE, information theory) | THIN | Appendix B; Ch 5–6 | Added eigenvectors and SVD (Ch 10); MLE, entropy and KL (Ch 6) |
| Tools: Jupyter, Colab, cloud GPUs | COVERED | Ch 3; Ch 26; Ch 43 | None |

**Counts (52 topics).** Before: 36 COVERED, 6 THIN, 8 MISSING, 2 OUT OF SCOPE. After: 50 COVERED, 2 OUT OF SCOPE.

## 3a. Stanford CS229 (Machine Learning)

| Topic | Status before | Where in the book | Action |
|---|---|---|---|
| Linear regression, LMS and gradient descent | COVERED | Ch 8; Ch 6 | None |
| Normal equations, locally weighted regression | OUT OF SCOPE | Ch 8 least squares | Closed-form algebra and a niche method |
| Probabilistic interpretation (least squares as maximum likelihood) | MISSING | None | Added MLE (Ch 6) |
| Logistic regression, perceptron | COVERED | Ch 8, Ch 10, Ch 12 | None |
| Newton's method | OUT OF SCOPE | Ch 13 covers curvature and second-order ideas | None |
| Generalized linear models, softmax regression | MISSING | None | Added GLM (incl. Poisson regression) and softmax regression (Ch 10); exponential-family math is out of scope |
| Generative learning: GDA, naive Bayes, Laplace smoothing | COVERED | Ch 10 naive Bayes with smoothing; Ch 16 generative vs discriminative (GDA itself is out of scope) | None |
| SVMs, margins, kernels | COVERED | Ch 10 (duality and SMO are out of scope) | None |
| Neural networks and backpropagation | COVERED | Ch 12 | None |
| Bias–variance tradeoff, double descent | COVERED | Ch 9; Ch 13 | None |
| Learning theory: sample complexity, VC dimension | MISSING | None | Added statistical learning theory, VC dimension and PAC learning (Ch 9) |
| Regularization, model selection, cross-validation | COVERED | Ch 9; Ch 13 | None |
| Bayesian statistics and regularization | COVERED | Ch 6; Ch 54 | None |
| Decision trees, bagging, boosting | COVERED | Ch 10 | None |
| k-means | COVERED | Ch 10 (worked by hand) | None |
| Mixture of Gaussians and the EM algorithm | MISSING | None | Added Ch 10 GMM (worked 67% / 33% membership) and EM |
| Factor analysis | OUT OF SCOPE | None | Statistical machinery |
| PCA | COVERED | Ch 10 | Added eigenvectors and SVD |
| ICA | OUT OF SCOPE | None | Named in one line (Ch 10) |
| Self-supervised learning, foundation models, in-context learning | COVERED | Ch 8; Ch 16; Ch 18; Ch 19 | None |
| MDPs, value and policy iteration | THIN | Ch 48 Bellman equation and Q-learning; MDP and value iteration (parallel audit) | None (parallel audit) |
| Continuous-state MDPs, fitted value iteration | COVERED | Ch 48 DQN (value function approximation) | None |
| LQR, DDP, LQG | OUT OF SCOPE | Ch 49 and Ch 50 cover control at product level | Control theory |
| Policy gradient (REINFORCE) | COVERED | Ch 48; Ch 20–21 | None |
| ML advice: debugging, error analysis, ablative analysis | THIN | Ch 62 and Ch 65 mention error analysis; Ch 19 ablation | Added Ch 13 debugging checklist |
| Evaluation metrics | COVERED | Ch 9 | None |

**Counts (26 topics).** Before: 15 COVERED, 2 THIN, 4 MISSING, 5 OUT OF SCOPE. After: 21 COVERED, 5 OUT OF SCOPE.

## 3b. Stanford CS231n (CNNs for Visual Recognition)

| Topic | Status before | Where in the book | Action |
|---|---|---|---|
| Image classification, kNN, train/val/test | COVERED | Ch 10; Ch 9; Ch 45 | None |
| Linear classifiers, SVM and softmax losses | COVERED | Ch 8 and Ch 10; Ch 6 cross-entropy (hinge loss is out of scope) | None |
| Regularization and optimization | COVERED | Ch 9; Ch 13 | None |
| Backpropagation and computational graphs | THIN | Ch 12 (graph unnamed) | Added computational graph (Ch 12) |
| Neural networks, activation functions | COVERED | Ch 12 | None |
| Convolutional layers, pooling, receptive fields | COVERED | Ch 14 | None |
| Data preprocessing, initialization, batch normalization | COVERED | Ch 11 feature scaling; Ch 13 | None |
| Babysitting training, hyperparameter search | THIN | Ch 9 search; Ch 13 curves | Added Ch 13 debugging checklist |
| Transfer learning, augmentation, dropout | COVERED | Ch 13; Ch 14 | None |
| CNN architectures: AlexNet, VGG, GoogLeNet, ResNet | COVERED | Ch 14 | None |
| Efficient architectures (MobileNet, EfficientNet, DenseNet) | MISSING | None | Added Ch 14 "After ResNet: smaller, faster CNNs" |
| Hardware and software (GPUs, PyTorch, TensorFlow) | COVERED | Ch 13; Ch 32 | None |
| RNNs, LSTM, image captioning | COVERED | Ch 14; Ch 22 vision-language models | None |
| Attention and Transformers | COVERED | Ch 14; Ch 15 | None |
| Detection and segmentation (R-CNN, YOLO, semantic and instance) | COVERED | Ch 45 | None |
| Visualizing and understanding (feature visualization, saliency, DeepDream, style transfer) | THIN | One sentence in Ch 14 plus a Going deeper link | Added Ch 14 "Looking inside a trained CNN" (four definitions) |
| Adversarial examples | COVERED | Ch 45 | None |
| Self-supervised learning (contrastive, masked autoencoders, DINO) | COVERED | Ch 16; Ch 45 | None |
| Generative models (PixelCNN, VAE, GAN, diffusion) | COVERED | Ch 16 | Added grading generators and other families (Ch 16) |
| Video understanding, 3D vision | COVERED | Ch 45 | None |
| Vision and language, CLIP | COVERED | Ch 16; Ch 22 | None |
| Robot learning | COVERED | Ch 49 | None |
| Large-scale distributed training | COVERED | Ch 37 | None |
| Human-centered AI, fairness | COVERED | Ch 58 | None |

**Counts (24 topics).** Before: 20 COVERED, 3 THIN, 1 MISSING. After: 24 COVERED.

## 3c. Stanford CS224n (NLP with Deep Learning)

| Topic | Status before | Where in the book | Action |
|---|---|---|---|
| Word vectors (word2vec, GloVe, analogies) | COVERED | Ch 14; Ch 5 | None |
| Neural classifiers, backpropagation | COVERED | Ch 12 | None |
| Syntactic structure and dependency parsing | MISSING | Ch 54 "Grammar, parsing and ambiguity" (parallel audit) | None (parallel audit) |
| Language modeling: n-grams, perplexity | COVERED | Ch 6 | None |
| RNNs, vanishing gradients, LSTMs | COVERED | Ch 14 | None |
| Bidirectional and multi-layer RNNs | MISSING | None | Added (Ch 14) |
| Machine translation, seq2seq, attention | COVERED | Ch 14; Ch 54 | None |
| BLEU | COVERED | Ch 54 | None |
| Beam search | MISSING | None | Added (Ch 18) |
| Self-attention and Transformers | COVERED | Ch 15 | None |
| Subword models (BPE) | COVERED | Ch 15; Ch 18 | None |
| Pretraining: ELMo, BERT, GPT, T5 | COVERED | Ch 14; Ch 15 | None |
| NLG decoding (greedy, sampling, top-k, top-p) | COVERED | Ch 18 | Added beam search |
| Post-training: instruction tuning, RLHF, DPO | COVERED | Ch 20 | None |
| Prompting, in-context learning, chain of thought | COVERED | Ch 18; Ch 21; Ch 25 | None |
| Question answering | COVERED | Ch 54; Ch 27 | None |
| Coreference resolution | MISSING | None | Added row and definition (Ch 54) |
| Natural language inference | MISSING | None | Added row and definition (Ch 54) |
| POS tagging, named entity recognition | THIN | NER in Ch 54; POS tagging (parallel audit) | None (parallel audit) |
| Parameter-efficient fine-tuning (adapters, prefix and prompt tuning) | THIN | Ch 30 LoRA; prompt tuning (parallel audit) | None (parallel audit) |
| Benchmarks and evaluation | COVERED | Ch 24; Ch 31 | None |
| Interpretability and probing | COVERED | Ch 57 | None |
| Multimodal models | COVERED | Ch 22 | None |
| Code generation | COVERED | Ch 29 | None |
| Retrieval augmentation and agents | COVERED | Ch 27; Ch 28 | None |
| Ethics, bias, social impact | COVERED | Ch 58 | None |
| Word senses, polysemy | COVERED | Ch 14 ("bank"); Ch 57 | None |

**Counts (27 topics).** Before: 20 COVERED, 2 THIN, 5 MISSING. After: 27 COVERED.

## 3d. Stanford CS336 (Language Modeling from Scratch)

| Topic | Status before | Where in the book | Action |
|---|---|---|---|
| Tokenization (BPE) | COVERED | Ch 15 (worked by hand); Ch 18 | None |
| PyTorch and resource accounting (FLOPs, memory) | COVERED | Ch 5 (2N, 6ND, memory math); Ch 12; Ch 33; Ch 37 | None |
| Architecture variants (pre-norm, RMSNorm, SwiGLU, RoPE, weight tying, QK-norm) | COVERED | Ch 13; Ch 15; Ch 17 | None |
| Stability tricks (z-loss, logit soft-capping) | OUT OF SCOPE | Ch 17 "Keeping giants stable" covers the idea | Individual tricks are too specialized |
| Hyperparameters across scale (μP, hyperparameter scaling laws) | MISSING | None | Added μP and hyperparameter transfer (40M to 6.7B), plus hyperparameter scaling laws (Ch 19) |
| Mixture of experts | COVERED | Ch 17 | None |
| GPUs, memory hierarchy, roofline | COVERED | Ch 32; Ch 33 | None |
| Kernels, Triton, fusion | COVERED | Ch 13; Ch 33; Ch 35 | None |
| FlashAttention | COVERED | Ch 15; Ch 23 | None |
| Parallelism (data, FSDP/ZeRO, tensor, pipeline, sequence, expert) | COVERED | Ch 37 | None |
| Scaling laws | COVERED | Ch 19 | None |
| Inference (KV cache, batching, speculative decoding, quantization) | COVERED | Ch 23 | None |
| Evaluation (perplexity, benchmarks, contamination) | COVERED | Ch 6; Ch 19; Ch 24 | None |
| Data (Common Crawl, filtering, quality classifiers, MinHash dedup) | COVERED | Ch 19; Ch 11 | None |
| Alignment (SFT, RLHF, DPO) | COVERED | Ch 20 | None |
| RL for reasoning (verifiable rewards, GRPO, expert iteration) | COVERED | Ch 21; Ch 20 | None |
| Mixed- and low-precision training | COVERED | Ch 13; Ch 32; Ch 37 | None |

**Counts (17 topics).** Before: 15 COVERED, 1 MISSING, 1 OUT OF SCOPE. After: 16 COVERED, 1 OUT OF SCOPE.

## Summary

| Standard | Topics | Before: COVERED / THIN / MISSING / OUT OF SCOPE | After: COVERED / OUT OF SCOPE | Share of in-scope topics covered after |
|---|---|---|---|---|
| Goodfellow et al. | 72 | 44 / 9 / 7 / 12 | 60 / 12 | 100% (60 of 60) |
| d2l.ai | 52 | 36 / 6 / 8 / 2 | 50 / 2 | 100% (50 of 50) |
| CS229 | 26 | 15 / 2 / 4 / 5 | 21 / 5 | 100% (21 of 21) |
| CS231n | 24 | 20 / 3 / 1 / 0 | 24 / 0 | 100% (24 of 24) |
| CS224n | 27 | 20 / 2 / 5 / 0 | 27 / 0 | 100% (27 of 27) |
| CS336 | 17 | 15 / 0 / 1 / 1 | 16 / 1 | 100% (16 of 16) |
| **All** | **218** | **150 / 22 / 26 / 20** | **198 / 20** | **100% of in-scope (91% of all rows)** |

Before this audit, 150 of 198 in-scope topics (76%) were covered.

**Gaps filled by parallel audits, with no action from this audit:**

- MDPs and value iteration (Ch 48)
- Parsing and POS tagging (Ch 54)
- Prompt tuning (Ch 30)
- Monte Carlo inference and MCMC (Ch 54)

### What this audit added

Every addition carries definitions in STYLE.md format and is listed in that chapter's Key terms. No figures were added, so figure numbering is unchanged.

- **Ch 6:** convex function; a new subsection "Maximum likelihood, entropy and KL divergence" with a worked coin example.
- **Ch 7:** one clause explaining how the 2006 deep belief nets were trained.
- **Ch 9:**
  - statistical learning theory, VC dimension and PAC learning
  - successive halving and Hyperband, with the worked example of 108 vs 729 epochs
- **Ch 10:**
  - GLM and softmax regression
  - Gaussian process
  - Gaussian mixture model and EM, with the worked example of 67% / 33% membership
  - eigenvector, SVD and ICA
- **Ch 12:** computational graph.
- **Ch 13:**
  - label smoothing, with a worked target
  - a sentence on AdaGrad
  - a debugging checklist: starting loss ln 10 = 2.30, overfit one batch; learning curve and error analysis defined
- **Ch 14:**
  - "Looking inside a trained CNN": feature visualization, saliency maps and Grad-CAM, DeepDream, neural style transfer
  - "After ResNet": 1 × 1 and depthwise separable convolutions, with a worked weight count; MobileNet, DenseNet and EfficientNet
  - "Stacking layers and reading both ways": stacked and bidirectional RNNs
- **Ch 16:**
  - manifold hypothesis
  - a new section "Other families you will hear about, and how generators are graded": energy-based models, partition function, Boltzmann machines and RBMs, deep belief networks, greedy layer-wise pretraining, normalizing flows, score-based models, FID, CLIP score
- **Ch 17:** memory-augmented networks (Neural Turing Machine, Memory Networks, DNC).
- **Ch 18:** "Beam search: looking a few steps ahead", with a worked example; beam search and beam width defined.
- **Ch 19:** μP and hyperparameter transfer.
- **Ch 54:**
  - variational inference, probabilistic graphical model, Markov random field
  - coreference resolution and NLI added to the classic-tasks table, which now has eight rows (the text was updated to match)

### Judged OUT OF SCOPE

These are mostly mathematical machinery or obsolete methods. Where a reader might hear the name, the book now names it in one line: ICA, Monte Carlo and MCMC, the partition function, score matching and variational inference.

The rest are not named, because a reader of this book is unlikely to meet them outside a math or specialist course:

- matrix inverses, determinants and the pseudoinverse
- Lagrange multipliers
- tangent propagation
- echo state networks and recursive nets
- Polyak averaging
- factor analysis and slow feature analysis
- contrastive divergence and NCE
- generative stochastic networks
- negative sampling
- the specific recommender models AutoRec, NeuMF and DeepFM
- normal equations and locally weighted regression
- Newton's method by name
- LQR, DDP and LQG control
- z-loss and other single stability tricks

### Checks

`validate.py` reports every diagram valid in all edited chapters. `check.py` reports [OK] for chapters 6, 7, 9, 10, 12, 13, 14, 16, 17, 18, 19 and 54.
