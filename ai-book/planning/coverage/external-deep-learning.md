# External-standard coverage audit: deep learning

Audited October 21, 2026 against `ai-book/chapters/` and `ai-book/appendices/`. Each topic was located by searching the whole book for its key terms (a scripted term count per chapter, then reading the passages). Statuses: COVERED (explained at beginner level), THIN (mentioned but not explained), MISSING, OUT OF SCOPE (too specialized or mathematical for this reader; the reason is given, and the book names it in one line where the reader is likely to hear the term).

Standards:

1. Goodfellow, Bengio and Courville, *Deep Learning* (MIT Press, 2016), all three parts.
2. *Dive into Deep Learning* (d2l.ai), its chapter list.
3. Stanford course syllabi: CS229 (machine learning), CS231n (CNNs for visual recognition), CS224n (NLP with deep learning) and CS336 (language modeling from scratch).

All structures were first reconstructed from memory, because web search was unavailable during the original audit, and were then verified online on October 21, 2026 against the published contents and the latest syllabi (see "Verified online (October 21, 2026)" at the end, which lists the corrections and the new rows). Topics are grouped by chapter or unit. The words in the Topic column describe content and are not quoted section titles.

- **Goodfellow:** confident about the 20-chapter structure. The section topics within each chapter are grouped.
- **d2l:** follows the 1.0 edition's chapter order (Preliminaries through the Tools appendix). Sections are grouped, and their exact titles may differ.
- **CS229, CS231n and CS224n:** syllabi change every year. These rows list the units these courses are known to cover across their 2017–2025 offerings: CS229's main lecture notes; CS231n's lectures from classification to 3D, robot learning and human-centered AI; CS224n's lectures from word vectors to post-training, agents and reasoning. *[Verified Oct 21, 2026: rows that are not in the latest offering are marked in the tables below.]*
- **CS336:** taught by Percy Liang and Tatsunori Hashimoto (offered in 2024 and 2025; *[corrected Oct 21, 2026: also offered in Spring 2026, the offering verified at the end]*). The rows list the lecture and assignment topics as best known. The exact lecture order is uncertain.

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
| Ch 20: autoregressive networks *[corrected Oct 21, 2026: the book's sections are linear and neural auto-regressive networks and NADE; PixelCNN and WaveNet do not appear in it]* | COVERED | Ch 16; Ch 46 | None |
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
| Learning theory: sample complexity, VC dimension *[corrected Oct 21, 2026: not a Fall 2025 lecture title; not verified this round]* | MISSING | None | Added statistical learning theory, VC dimension and PAC learning (Ch 9) |
| Regularization, model selection, cross-validation | COVERED | Ch 9; Ch 13 | None |
| Bayesian statistics and regularization | COVERED | Ch 6; Ch 54 | None |
| Decision trees, bagging, boosting | COVERED | Ch 10 | None |
| k-means | COVERED | Ch 10 (worked by hand) | None |
| Mixture of Gaussians and the EM algorithm | MISSING | None | Added Ch 10 GMM (worked 67% / 33% membership) and EM |
| Factor analysis *[corrected Oct 21, 2026: not a Fall 2025 lecture title; not verified this round]* | OUT OF SCOPE | None | Statistical machinery |
| PCA | COVERED | Ch 10 | Added eigenvectors and SVD |
| ICA *[corrected Oct 21, 2026: not a Fall 2025 lecture title; not verified this round]* | OUT OF SCOPE | None | Named in one line (Ch 10) |
| Self-supervised learning, foundation models, in-context learning *[corrected Oct 21, 2026: 2026 notes chapters 15 to 17; Fall 2025 lectures 17 and 18 cover LLMs]* | COVERED | Ch 8; Ch 16; Ch 18; Ch 19 | None |
| MDPs, value and policy iteration | THIN | Ch 48 Bellman equation and Q-learning; MDP and value iteration (parallel audit) | None (parallel audit) |
| Continuous-state MDPs, fitted value iteration | COVERED | Ch 48 DQN (value function approximation) | None |
| LQR, DDP, LQG *[corrected Oct 21, 2026: LQR is in the 2026 lecture notes; not a Fall 2025 lecture title]* | OUT OF SCOPE | Ch 49 and Ch 50 cover control at product level | Control theory |
| Policy gradient (REINFORCE) *[corrected Oct 21, 2026: a chapter of the August 2026 notes; not a Fall 2025 lecture title]* | COVERED | Ch 48; Ch 20–21 | None |
| ML advice: debugging, error analysis, ablative analysis | THIN | Ch 62 and Ch 65 mention error analysis; Ch 19 ablation | Added Ch 13 debugging checklist |
| Evaluation metrics | COVERED | Ch 9 | None |

**Counts (26 topics).** Before: 15 COVERED, 2 THIN, 4 MISSING, 5 OUT OF SCOPE. After: 21 COVERED, 5 OUT OF SCOPE.

## 3b. Stanford CS231n (CNNs for Visual Recognition) *[corrected Oct 21, 2026: the course is now titled "Deep Learning for Computer Vision"]*

| Topic | Status before | Where in the book | Action |
|---|---|---|---|
| Image classification, kNN, train/val/test | COVERED | Ch 10; Ch 9; Ch 45 | None |
| Linear classifiers, SVM and softmax losses | COVERED | Ch 8 and Ch 10; Ch 6 cross-entropy (hinge loss is out of scope) | None |
| Regularization and optimization | COVERED | Ch 9; Ch 13 | None |
| Backpropagation and computational graphs | THIN | Ch 12 (graph unnamed) | Added computational graph (Ch 12) |
| Neural networks, activation functions | COVERED | Ch 12 | None |
| Convolutional layers, pooling, receptive fields | COVERED | Ch 14 | None |
| Data preprocessing, initialization, batch normalization *[corrected Oct 21, 2026: batch norm is in Spring 2026 lecture 6; preprocessing and initialization come from the Spring 2019 "Training Neural Networks" lectures]* | COVERED | Ch 11 feature scaling; Ch 13 | None |
| Babysitting training, hyperparameter search *[corrected Oct 21, 2026: from the earlier "Training Neural Networks" lectures (Spring 2019); not in Spring 2026]* | THIN | Ch 9 search; Ch 13 curves | Added Ch 13 debugging checklist |
| Transfer learning, augmentation, dropout | COVERED | Ch 13; Ch 14 | None |
| CNN architectures: AlexNet, VGG, GoogLeNet, ResNet | COVERED | Ch 14 | None |
| Efficient architectures (MobileNet, EfficientNet, DenseNet) *[corrected Oct 21, 2026: not a lecture title in the 2019, 2024, 2025 or 2026 syllabi; at most a sub-topic of "CNN Architectures"]* | MISSING | None | Added Ch 14 "After ResNet: smaller, faster CNNs" |
| Hardware and software (GPUs, PyTorch, TensorFlow) *[corrected Oct 21, 2026: a Spring 2019 lecture; Spring 2026 has a PyTorch review session instead]* | COVERED | Ch 13; Ch 32 | None |
| RNNs, LSTM, image captioning | COVERED | Ch 14; Ch 22 vision-language models | None |
| Attention and Transformers | COVERED | Ch 14; Ch 15 | None |
| Detection and segmentation (R-CNN, YOLO, semantic and instance) | COVERED | Ch 45 | None |
| Visualizing and understanding (feature visualization, saliency, DeepDream, style transfer) | THIN | One sentence in Ch 14 plus a Going deeper link | Added Ch 14 "Looking inside a trained CNN" (four definitions) |
| Adversarial examples | COVERED | Ch 45 | None |
| Self-supervised learning (contrastive, masked autoencoders, DINO) | COVERED | Ch 16; Ch 45 | None |
| Generative models (PixelCNN, VAE, GAN, diffusion) | COVERED | Ch 16 | Added grading generators and other families (Ch 16) |
| Video understanding, 3D vision | COVERED | Ch 45 | None |
| Vision and language, CLIP | COVERED | Ch 16; Ch 22 | None |
| Robot learning *[corrected Oct 21, 2026: Spring 2024 and 2025 only; Spring 2026 replaced it with "World Modeling"]* | COVERED | Ch 49 | None |
| Large-scale distributed training | COVERED | Ch 37 | None |
| Human-centered AI, fairness | COVERED | Ch 58 | None |

**Counts (24 topics).** Before: 20 COVERED, 3 THIN, 1 MISSING. After: 24 COVERED.

## 3c. Stanford CS224n (NLP with Deep Learning)

| Topic | Status before | Where in the book | Action |
|---|---|---|---|
| Word vectors (word2vec, GloVe, analogies) | COVERED | Ch 14; Ch 5 | None |
| Neural classifiers, backpropagation | COVERED | Ch 12 | None |
| Syntactic structure and dependency parsing *[corrected Oct 21, 2026: a lecture through Winter 2025; not in Winter 2026]* | MISSING | Ch 54 "Grammar, parsing and ambiguity" (parallel audit) | None (parallel audit) |
| Language modeling: n-grams, perplexity | COVERED | Ch 6 | None |
| RNNs, vanishing gradients, LSTMs | COVERED | Ch 14 | None |
| Bidirectional and multi-layer RNNs *[corrected Oct 21, 2026: earlier offerings (Winter 2021 "Vanishing Gradients, Fancy RNNs, Seq2Seq"); not a Winter 2026 lecture]* | MISSING | None | Added (Ch 14) |
| Machine translation, seq2seq, attention *[corrected Oct 21, 2026: lectures in Winter 2021, 2024 and 2025; no separate lecture in Winter 2026]* | COVERED | Ch 14; Ch 54 | None |
| BLEU *[corrected Oct 21, 2026: a sub-topic of the earlier machine-translation lectures]* | COVERED | Ch 54 | None |
| Beam search *[corrected Oct 21, 2026: a sub-topic of the earlier translation and generation lectures]* | MISSING | None | Added (Ch 18) |
| Self-attention and Transformers | COVERED | Ch 15 | None |
| Subword models (BPE) *[corrected Oct 21, 2026: Winter 2021 lecture; Winter 2026 guest lecture on tokenization]* | COVERED | Ch 15; Ch 18 | None |
| Pretraining: ELMo, BERT, GPT, T5 | COVERED | Ch 14; Ch 15 | None |
| NLG decoding (greedy, sampling, top-k, top-p) *[corrected Oct 21, 2026: Winter 2021 "Natural Language Generation" lecture]* | COVERED | Ch 18 | Added beam search |
| Post-training: instruction tuning, RLHF, DPO | COVERED | Ch 20 | None |
| Prompting, in-context learning, chain of thought | COVERED | Ch 18; Ch 21; Ch 25 | None |
| Question answering *[corrected Oct 21, 2026: lectures in Winter 2021, 2024 and 2025; not in Winter 2026]* | COVERED | Ch 54; Ch 27 | None |
| Coreference resolution *[corrected Oct 21, 2026: Winter 2021 lecture; not in later offerings checked]* | MISSING | None | Added row and definition (Ch 54) |
| Natural language inference *[corrected Oct 21, 2026: not a lecture title in the offerings checked; a sub-topic]* | MISSING | None | Added row and definition (Ch 54) |
| POS tagging, named entity recognition *[corrected Oct 21, 2026: not lecture titles in the offerings checked; sub-topics]* | THIN | NER in Ch 54; POS tagging (parallel audit) | None (parallel audit) |
| Parameter-efficient fine-tuning (adapters, prefix and prompt tuning) | THIN | Ch 30 LoRA; prompt tuning (parallel audit) | None (parallel audit) |
| Benchmarks and evaluation | COVERED | Ch 24; Ch 31 | None |
| Interpretability and probing | COVERED | Ch 57 | None |
| Multimodal models | COVERED | Ch 22 | None |
| Code generation *[corrected Oct 21, 2026: Winter 2024 guest lecture]* | COVERED | Ch 29 | None |
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

## Verified online (October 21, 2026)

The reconstructed topic lists above were checked against the published tables of contents and the most recent syllabus page of each course. For each standard this section gives the pages fetched, what differed, and the topics the reconstruction missed. Each missed topic was audited the same way as before: a search of `chapters/` and `appendices/` for its key terms, then a reading of the passages found. THIN and MISSING in-scope topics were filled in the chapter that owns them in OUTLINE.md. Rows above that were misnamed, or that come only from older offerings, are marked "corrected Oct 21, 2026" in place. Nothing above was deleted.

### Goodfellow, Bengio and Courville, *Deep Learning*

**Fetched:** https://www.deeplearningbook.org/ (contents menu), https://www.deeplearningbook.org/contents/TOC.html (full table of contents, down to sections), https://www.deeplearningbook.org/contents/convnets.html (section 9.7) and https://www.deeplearningbook.org/contents/generative_models.html (chapter 20 subsections).

**What differed:**

- The 20 chapters, their titles and their order match the reconstruction. The website menu calls Part II "Modern Practical Deep Networks", while the book's table of contents calls it "Deep Networks: Modern Practices". The audit table does not use part titles.
- **Misnamed row:** the Ch 20 autoregressive row cited PixelCNN and WaveNet. Sections 20.10.7 to 20.10.10 cover linear auto-regressive networks, neural auto-regressive networks and NADE, and the chapter text does not mention PixelCNN or WaveNet. The row is corrected in place; its status does not change.
- **Merged into existing rows, with no new row needed:**
  - 2.4 (linear dependence and span) and 2.6 (special kinds of matrices), into the out-of-scope matrix row
  - 4.2 (poor conditioning) and 4.5 (linear least squares), into the optimization row and Ch 8's least squares
  - 6.2 (cost functions and output units), into the feedforward row
  - 8.7 (continuation methods and designing models to aid optimization), into the curriculum and residual-connection rows
  - 18.3 (pseudolikelihood), into the out-of-scope partition-function row
  - 20.9 (back-propagation through random operations), into the reparameterization row
- **Missed entirely:** Chapter 1 and 23 sections, listed below.

| Topic (book section) | Status before | Where in the book | Action |
|---|---|---|---|
| Ch 1: who should read the book; historical trends (many names, growing datasets, growing models, rising accuracy) | COVERED | Ch 7 (eras; hardware and data jumps); Ch 19 (scale trends) | None |
| 3.2 and 3.4: random variables, marginal probability | MISSING | None | Added Ch 6 "Random variables, joint tables and marginals", worked spam-and-"free" table (P(spam) = 0.30, P("free") = 0.25, P(spam given "free") = 0.8). Random variable, joint probability and marginal probability are defined |
| 3.12: continuous variables and densities | MISSING | Ch 6 bell curve, without densities | Added Ch 6 "Smooth quantities: densities and areas" (probability density and integral defined; tied to Figure 6.5 and AUC). Change of variables and measure theory are out of scope |
| 5.10: building a machine learning algorithm (data, cost, optimizer, model) | COVERED | Ch 8 Key idea "Data, a model with knobs, a loss and gradient descent" | None |
| 5.11.2: local constancy and smoothness | COVERED | Ch 13 "Inductive biases: built-in assumptions"; Ch 10 kNN | None |
| 7.2 and 7.3: norm penalties as constrained optimization; under-constrained problems | OUT OF SCOPE | None | Optimization math |
| 8.1: how learning differs from pure optimization (empirical risk, surrogate loss, minibatches) | THIN | Minibatches in Ch 6, 12 and 13; test sets in Ch 6 and 9; surrogate loss and empirical risk absent | Added Ch 6 "Why not train on accuracy directly?". Worked case: a spam email moves from 0.48 to 0.49, accuracy stays flat, and the loss falls from 0.734 to 0.713. Surrogate loss and empirical risk are defined |
| 9.4: convolution and pooling as an infinitely strong prior | COVERED | Ch 13 inductive biases (the CNN's assumptions) | None |
| 9.7: data types (1-D, 2-D, 3-D and variable-size inputs) | MISSING | Ch 14 covered only flat images | Added Ch 14 "Beyond flat pictures: convolution in one and three dimensions". 1-D and 3-D convolution are defined, with variable-length inputs, Kim's 2014 text CNN, the C3D video network and CT stacks |
| 9.9: random or unsupervised features | OUT OF SCOPE | None | Historical |
| 10.2.1: teacher forcing | COVERED | Ch 15 (defined) | None |
| 11.6: worked example, multi-digit number recognition | OUT OF SCOPE | Ch 13 debugging checklist carries the method | A single case study |
| 14.4, 14.8 and 14.9: stochastic encoders, predictive sparse decomposition, uses of autoencoders | OUT OF SCOPE | Ch 16 autoencoders | Specialized |
| 15.2: zero-shot and one-shot learning | COVERED | Ch 8; Ch 16; Ch 25 | None |
| 15.3 and 15.6: disentangling the causal factors | THIN | Ch 16's latent-space "sliders" analogy, without the name | Added disentangled representation (Ch 16, "Latent space") |
| 16.5: latent variables | COVERED | Ch 16 latent space; Ch 10 GMM's hidden cluster membership | None |
| 16.2 and 16.3: d-separation, factor graphs, ancestral sampling | OUT OF SCOPE | Ch 54 Bayesian networks | Graphical-model machinery |
| 17.2: importance sampling | OUT OF SCOPE | None | Sampling math |
| 18.5: denoising score matching | COVERED | Ch 16 "Score-based models: diffusion's twin" (predicting the score and predicting the noise are the same thing) | None |
| 19.1 and 19.3: inference as optimization (ELBO), MAP inference | OUT OF SCOPE | Ch 16 VAE | Math |
| 20.4 to 20.8: deep Boltzmann machines and other Boltzmann variants | OUT OF SCOPE | Ch 16 Boltzmann machines and RBMs | Historical |
| 20.10.1 and 20.10.10: sigmoid belief networks, NADE | OUT OF SCOPE | Ch 16 autoregressive generation | Historical model names |
| 20.11: drawing samples from autoencoders | OUT OF SCOPE | None | Specialized |
| 20.13: other generation schemes: diffusion inversion (Sohl-Dickstein et al., 2015) | COVERED | Ch 16 (diffusion "proposed in 2015") | None |

New rows: 24. Before: 9 COVERED, 2 THIN, 3 MISSING, 10 OUT OF SCOPE. After: 14 COVERED, 10 OUT OF SCOPE.

### *Dive into Deep Learning* (d2l.ai)

**Fetched:** https://d2l.ai/ (the full navigation tree, version 1.0.3) and https://d2l.ai/chapter_linear-classification/image-classification-dataset.html.

**What differed:**

- The 23 numbered chapters (21 chapters and two appendices) are in the order the reconstruction assumed.
- Numbering details:
  - Batch normalization is section 8.5, inside "Modern Convolutional Neural Networks".
  - ResNeXt shares section 8.6 with ResNet.
  - The design-spaces row is 8.8, "Designing Convolution Network Architectures".
  - Section 4.2 uses Fashion-MNIST and presents MNIST as history, so that row stands.
- The 14.13 and 14.14 Kaggle image projects and the 23.2, 23.3 and 23.5 cloud and GPU sections fall under the existing Kaggle and Tools rows.
- No row was invented or misnamed.
- **Missed entirely:**

| Topic (d2l section) | Status before | Where in the book | Action |
|---|---|---|---|
| 2.7, 3.2 and 6.4: documentation, object-oriented design, lazy initialization | OUT OF SCOPE | Ch 13 frameworks | Library and coding details |
| 4.6: generalization in classification (reusing the test set) | COVERED | Ch 6 and Ch 9 (the test set is used once; leakage); Ch 9 VC dimension | None |
| 9.1: working with sequences (autoregressive and Markov models) | COVERED | Ch 6 n-gram model; Ch 16 autoregressive generation; Ch 46 and Ch 54 Markov models | None |
| 16.3: sentiment analysis with CNNs (text CNN) | MISSING | None | Added to Ch 14 (1-D convolution over word vectors; Kim 2014 beat the previous best on 4 of 7 sentence tasks) |
| 19.3 and 19.5: asynchronous random search, asynchronous successive halving | OUT OF SCOPE | Ch 9 successive halving and Hyperband | Scheduling detail |
| 21.8: feature-rich recommenders (click-through prediction) | COVERED | Ch 51 CTR prediction | None |
| 22.5: integral calculus | MISSING | Ch 9 AUC only | Added integral (Ch 6, densities subsection) |
| 22.6: random variables (discrete and continuous) | MISSING | None | Added random variable, marginal probability and probability density (Ch 6) |
| 22.10: statistics (estimators, hypothesis tests, confidence intervals) | THIN | Margin of error in Ch 9 and Ch 31; confidence intervals in Ch 24 and Ch 50; "p-value" and "statistical significance" absent | Added a Ch 9 significance-test paragraph, with p-value and statistical significance defined. Worked case: 91.0% vs 91.8% on 1,500 emails, where a gap of about 2 points is needed |

New rows: 9. Before: 3 COVERED, 1 THIN, 3 MISSING, 2 OUT OF SCOPE. After: 7 COVERED, 2 OUT OF SCOPE.

### Stanford CS229 (Machine Learning)

**Fetched:** https://cs229.stanford.edu/ could not be read from this session. The site's certificate chain ends at an emSign root that the session's proxy does not trust, and WebFetch returned HTTP 503. TLS verification was not bypassed. Instead, the search engine's index of the site was used for:

- https://cs229.stanford.edu/index.html-fall25 (the Fall 2025 page with its tentative schedule, September 22 to December 10, 2025)
- https://cs229.stanford.edu/index.html-spr26 (the Spring 2026 page, whose schedule was not visible)
- https://cs229.stanford.edu/main_notes.pdf (Ma and Ng lecture notes, dated August 23, 2026)
- https://cs229.stanford.edu/notes2026spring/main_notes.pdf (dated May 19, 2026)

**Term used:** Fall 2025, the most recent complete lecture-by-lecture schedule that could be seen.

**What differed:**

- **Fall 2025 lectures:**
  - Supervised learning setup and LMS
  - Weighted least squares, logistic regression and Newton's method
  - Exponential families and GLMs
  - Bias–variance and regularization
  - GDA, naive Bayes and Laplace smoothing
  - Kernels and SVMs
  - k-means, GMM and EM
  - Decision trees
  - Boosting
  - Neural networks and backpropagation (two lectures)
  - ML advice
  - RL basics, value and policy iteration
  - Model-based RL and value-function approximation
  - PCA
  - Large language models (lecture 17: language modeling, embeddings, Transformers; lecture 18: RAG, fine-tuning, prompt optimization, safety)
  - Fairness, algorithmic bias, explainability and privacy (lectures 19 and 20)
- **Lecture notes:** the 2026 notes add chapters on foundation models, representation learning (including RAG) and large language models. They keep a reinforcement learning and control part that includes LQR, and the August version lists a policy gradient chapter.
- **Not seen in the Fall 2025 lecture titles:** learning theory, factor analysis, ICA, LQR and policy gradient. These are marked in the table above. They were not removed, because they belong to the notes or to earlier offerings.
- **Missed entirely:**

| Topic (Fall 2025 lecture) | Status before | Where in the book | Action |
|---|---|---|---|
| Large language models: language modeling, embeddings, Transformers, RAG, fine-tuning, prompt optimization, safety (lectures 17 and 18) | COVERED | Ch 15, 18, 25 (prompt optimization), 27, 30, 56 | None |
| Fairness, algorithmic bias, explainability, privacy (lectures 19 and 20) | COVERED | Ch 58 (fairness, privacy); Ch 57 explainable AI; Ch 10 feature importance; Ch 48 Shapley value and SHAP; Ch 11 differential privacy | None |
| Model-based RL (lecture 15) | COVERED | Ch 48 (model-based agents, MuZero) | None |

New rows: 3, all COVERED.

### Stanford CS231n (Deep Learning for Computer Vision)

**Fetched:** https://cs231n.stanford.edu/ and https://cs231n.stanford.edu/schedule.html. To see where older rows came from, also https://cs231n.stanford.edu/2025/schedule.html, https://cs231n.stanford.edu/2024/schedule.html and https://cs231n.stanford.edu/2019/syllabus.html.

**Term used:** Spring 2026 (Fei-Fei Li, Ehsan Adeli, Justin Johnson, Zane Durante, Tiange Xiang). The course's title is now "Deep Learning for Computer Vision".

**What differed:**

- **The 18 Spring 2026 lectures:**
  1. Introduction
  2. Image classification with linear classifiers
  3. Regularization and optimization
  4. Neural networks and backpropagation
  5. Image classification with CNNs
  6. CNN architectures (batch norm, transfer learning)
  7. RNNs
  8. Attention and Transformers
  9. Detection, segmentation, visualizing and understanding (including DETR, panoptic segmentation, adversarial examples, DeepDream and style transfer)
  10. Video understanding (3D CNNs, two-stream networks)
  11. Large-scale distributed training (including activation checkpointing)
  12. Self-supervised learning (pretext tasks, contrastive learning)
  13. Generative models: VAEs, GANs, autoregressive models
  14. Generative models: diffusion
  15. 3D vision (neural implicit representations)
  16. Vision and language
  17. World modeling
  18. Human-centered AI
- **Changes to existing rows:**
  - "Robot learning" was a lecture in 2024 and 2025 and is replaced by "World Modeling" in 2026.
  - "Hardware and software" and "Training Neural Networks" (babysitting training, preprocessing, initialization) are 2019-era lectures.
  - "Efficient architectures" was never a lecture title.
  - All four rows are marked in place. None was invented.
- **Missed entirely:**

| Topic (Spring 2026 lecture) | Status before | Where in the book | Action |
|---|---|---|---|
| Video: 3D CNNs and two-stream networks (lecture 10) | THIN | Ch 45 said only "networks that look across several frames" | Added to Ch 45: 3-D CNN (C3D, 3 × 3 × 3 cubes), two-stream network (Simonyan and Zisserman, 2014) and video Transformers (ViViT and TimeSformer, 2021), with two definitions. Also Ch 14's 3-D convolution |
| Self-supervised pretext tasks (lecture 12) | THIN | Ch 16 had masking examples but not the term | Added pretext task to Ch 16, with jigsaw puzzles (2016) and rotation prediction (2018) |
| World modeling (lecture 17) | COVERED | Ch 16; Ch 22; Ch 47; Ch 49 | None |
| Detection extras: DETR, panoptic segmentation (lecture 9) | COVERED | Ch 45 | None |

New rows: 4. Before: 2 COVERED, 2 THIN. After: 4 COVERED.

### Stanford CS224n (NLP with Deep Learning)

**Fetched:** https://web.stanford.edu/class/cs224n/. To see where older rows came from, also the archived Winter 2025 (https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1254/), Winter 2024 (.../cs224n.1244/) and Winter 2021 (.../cs224n.1214/) schedules.

**Term used:** Winter 2026 (Diyi Yang, Yejin Choi).

**What differed:**

- **The Winter 2026 lectures:**
  1. History of NLP
  2. Word vectors
  3. Backpropagation and neural network basics
  4. Language models and RNNs
  5. Transformers
  6. Final projects and practical tips
  7. Pretraining (scaling, systems, data)
  8. Post-training (RLHF, SFT, DPO)
  9. Efficient adaptation (prompting and PEFT)
  10. Agents, tool use and RAG
  11. Benchmarking and evaluation
  12. Reasoning 1 (chain of thought, self-consistency, DeepSeek-R1, DAPO)
  13. Reasoning 2 (step-level verification, speculative decoding, test-time compute)
  14. Guest lecture: tokenization and multilinguality
  15. Guest lecture: interpretability (Been Kim)
  16. Social and broader impacts of NLP
  17. Guest lecture: multimodality (Luke Zettlemoyer)
  18. Guest lecture: "Tinker and LoRA Without Regret" (John Schulman)
  19. Open questions in NLP 2026
- **Older rows:** dependency parsing, machine translation, coreference, question answering, natural language generation and code generation are lectures from earlier offerings (Winter 2021, 2024 or 2025). NLI and POS tagging were never lecture titles in the offerings checked. These rows are marked in place. None was invented.
- **Missed entirely:**

| Topic (Winter 2026 lecture) | Status before | Where in the book | Action |
|---|---|---|---|
| History of NLP (lecture 1) | COVERED | Ch 54 four eras of language AI; Ch 7 | None |
| Reasoning: chain of thought, self-consistency, RL with verifiable rewards (DeepSeek-R1, DAPO), step-level verification, test-time compute (lectures 12 and 13) | COVERED | Ch 21; Ch 23 speculative decoding | None |
| Tokenization and multilinguality (lecture 14) | COVERED | Ch 18 "Other languages cost more"; Ch 15; Ch 19 multilingual data | None |
| LoRA compared with full fine-tuning ("LoRA Without Regret") and the Tinker fine-tuning service (lecture 18) | THIN | Ch 30 covered LoRA in depth but not how close it gets to full fine-tuning; Tinker appeared only in Appendix D | Added Ch 30 "Does LoRA give up quality?" (all layers, a learning rate about 10 times higher, rank 1 enough for RL, limits). Added a Tinker paragraph to "Where to fine-tune" |
| Open questions in NLP 2026 (lecture 19) | COVERED | Ch 66 | None |

New rows: 5. Before: 4 COVERED, 1 THIN. After: 5 COVERED.

### Stanford CS336 (Language Modeling from Scratch)

**Fetched:** https://stanford-cs336.github.io/ (redirects to http://cs336.stanford.edu/) and https://cs336.stanford.edu/.

**Term used:** Spring 2026 (Tatsunori Hashimoto, Percy Liang), with 19 lectures and five assignments. Earlier offerings were Spring 2024 and Spring 2025.

**What differed:**

- **The lecture order is now known:**
  1. Overview and tokenization
  2. PyTorch (einops) and resource accounting (FLOPs, memory, arithmetic intensity)
  3. Architectures and hyperparameters
  4. Attention alternatives and mixture of experts
  5. GPUs and TPUs
  6. Kernels and Triton
  7–8. Parallelism (two lectures)
  9. Scaling laws
  10. Inference
  11. Scaling laws
  12. Evaluation
  13. Data (sources, datasets)
  14. Data (filtering, deduplication, mixing, synthetic data)
  15. Mid- and post-training (SFT and RLHF)
  16. Post-training with RLVR
  17. Alignment and multimodality
  18–19. Guest lectures
- **Assignments:**
  1. Basics: tokenizer, model, optimizer
  2. Systems: profiling, a Triton FlashAttention2, distributed training
  3. Scaling: fitting a scaling law through a training API
  4. Data: Common Crawl filtering and deduplication
  5. Alignment and reasoning RL: SFT and RL for math, with optional DPO
- Every reconstructed row appears. "Stability tricks" and "Mixed-precision training" are sub-topics, not lecture titles.
- **Missed entirely:**

| Topic (Spring 2026 lecture) | Status before | Where in the book | Action |
|---|---|---|---|
| Attention alternatives (lecture 4) | COVERED | Ch 17 (state-space models, linear attention, hybrids) | None |
| TPUs (lecture 5) | COVERED | Ch 32; Ch 35 | None |
| Data mixing and synthetic data (lecture 14) | COVERED | Ch 19 (data mixtures, synthetic data) | None |
| Mid-training (lecture 15) | COVERED | Ch 19 | None |
| Multimodal alignment (lecture 17) | COVERED | Ch 22 (LLaVA visual instruction tuning, fusion) | None |

New rows: 5, all COVERED.

### Sources for the book additions

- Kim, "Convolutional Neural Networks for Sentence Classification" (EMNLP 2014): https://arxiv.org/abs/1408.5882
- Simonyan and Zisserman, "Two-Stream Convolutional Networks for Action Recognition in Videos" (2014): https://arxiv.org/abs/1406.2199
- Tran et al., C3D (December 2014; 3 × 3 × 3 kernels): https://arxiv.org/abs/1412.0767
- TimeSformer (2021): https://arxiv.org/abs/2102.05095
- ViViT (2021): https://arxiv.org/abs/2103.15691
- Rotation prediction (2018): https://arxiv.org/abs/1803.07728
- Jigsaw puzzles (2016): https://arxiv.org/abs/1603.09246
- Thinking Machines Lab, "LoRA Without Regret" (September 29, 2025): https://thinkingmachines.ai/blog/lora/
- Tinker announcement (October 1, 2025): https://thinkingmachines.ai/blog/announcing-tinker/
- Tinker page: https://thinkingmachines.ai/tinker/ (per-token pricing)
- Goodfellow section 9.7 (table of data types, including CT volumes) and section 20.13 (diffusion inversion), from the deeplearningbook.org pages listed above

The significance, density and surrogate-loss passages are standard definitions with worked arithmetic. They state no new facts that would need a source.

### Updated counts

| Standard | Rows (original + new) | Before: COVERED / THIN / MISSING / OUT OF SCOPE | After: COVERED / OUT OF SCOPE | Share of in-scope topics covered after |
|---|---|---|---|---|
| Goodfellow et al. | 96 (72 + 24) | 53 / 11 / 10 / 22 | 74 / 22 | 100% (74 of 74) |
| d2l.ai | 61 (52 + 9) | 39 / 7 / 11 / 4 | 57 / 4 | 100% (57 of 57) |
| CS229 (Fall 2025) | 29 (26 + 3) | 18 / 2 / 4 / 5 | 24 / 5 | 100% (24 of 24) |
| CS231n (Spring 2026) | 28 (24 + 4) | 22 / 5 / 1 / 0 | 28 / 0 | 100% (28 of 28) |
| CS224n (Winter 2026) | 32 (27 + 5) | 24 / 3 / 5 / 0 | 32 / 0 | 100% (32 of 32) |
| CS336 (Spring 2026) | 22 (17 + 5) | 20 / 0 / 1 / 1 | 21 / 1 | 100% (21 of 21) |
| **All** | **268 (218 + 50)** | **176 / 28 / 32 / 32** | **236 / 32** | **100% of in-scope (88% of all rows)** |

Before both rounds, 176 of the 236 in-scope topics (75%) were covered. The 50 new rows break down as 26 COVERED, 6 THIN, 6 MISSING and 12 OUT OF SCOPE.

### What this round added to the book

Every addition has its definitions in STYLE.md format, and each new term is in its chapter's Key terms list. No figures were added, so figure numbering is unchanged.

- **Ch 6:**
  - "Random variables, joint tables and marginals": random variable, joint probability, marginal probability
  - "Smooth quantities: densities and areas": probability density, integral
  - "Why not train on accuracy directly?": surrogate loss, empirical risk
  - One sentence now points to "the Softmax and Sampling sections below" instead of "the next two sections".
- **Ch 9:** a significance-test paragraph defining p-value and statistical significance.
- **Ch 14:** "Beyond flat pictures: convolution in one and three dimensions", defining 1-D convolution and 3-D convolution.
- **Ch 16:** disentangled representation (in "Latent space") and pretext task (in "Self-supervised learning").
- **Ch 30:**
  - "Does LoRA give up quality?"
  - a paragraph on Tinker in "Where to fine-tune"
- **Ch 45:** video recognition by 3-D CNN, two-stream network and video Transformer, with two definitions.

### Checks

`validate.py` reports every diagram valid in chapters 6, 9, 14, 16, 30 and 45. `check.py` reports [OK] for the same chapters.

### Unresolved

- **CS229:** its rows were verified only indirectly, through search-index entries, because the course site could not be fetched from this session. Rows marked "not verified this round" stand as reconstructed. If the site becomes reachable, re-check them against the Spring 2026 or Autumn 2026 syllabus page.
- **Tinker:** whether it is generally available as of October 2026 was not confirmed (the web-search budget for this session ran out). The book makes no availability claim.
