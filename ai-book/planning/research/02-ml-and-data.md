# 02 — What Machine Learning Is, Classical Machine Learning, and Data

Research notes for *Everything About AI: From Zero to the Frontier*. Compiled October 21, 2026.

**Research note:** time-sensitive facts below were checked with web searches and fetches of primary or near-primary pages on October 21, 2026. The shared web-search budget ran out partway through, so a few items are marked **[verify before print]**. Facts from before 2025 (MNIST, ImageNet, the Netflix Prize and so on) come from well-established history; check them against the cited canonical sources during copy-edit.

---

## 1. Topic map (teaching order, simplest to most advanced)

### Part A — Why machine learning exists

1. **Programs as recipes (rules-based programming).** Explain that a normal program is a list of exact instructions a human writes ("if the email contains 'lottery', mark it spam"). Use a cooking recipe and a thermostat as examples. The reader already uses software every day, so start from that.
2. **Where rules break.** Show tasks that are easy for people but nearly impossible to write rules for: recognizing a cat, reading messy handwriting, judging whether a review is sarcastic. Have the reader try to write rules for "is this a cat?" and watch the list blow up.
3. **Learning from examples.** The core idea is to show the computer thousands of labeled examples and let it adjust itself until its guesses match. Compare it to how a child learns "dog" from examples rather than from a definition.
4. **What a "model" is.** A model is a mathematical function, which you can picture as a box with many adjustable knobs. Data goes in and a prediction comes out. Stress that a model is a *file of numbers plus a recipe for using them*, not a database of memorized answers and not a mind.
5. **Parameters and weights.** The knobs are called parameters (in neural networks, mostly "weights"). Training means turning the knobs. Give a sense of scale: a line has 2 knobs, a spam filter might have thousands, and frontier chatbots have hundreds of billions to trillions.
6. **Hyperparameters.** These are settings a human picks *before* training: how fast to turn the knobs, how many rounds, how deep a tree can grow. They are settings *about* learning, not things learned.
7. **Features and labels.** Use a spreadsheet picture. Each row is an example, each column is a feature (an input fact), and one special column is the label (the answer to predict). House-price and email-spam tables make good worked examples.
8. **Training vs inference.** Training is the expensive, one-time (or occasional) learning phase. Inference is using the finished model to answer new questions. Tie it to the reader's experience: when you chat with Claude or ChatGPT, that is inference, and the model is not learning from you in that moment.
9. **Generalization: the whole point.** A model is only useful if it works on examples it has never seen. Memorizing the practice exam is not learning. This idea sets up everything in Part D.

### Part B — The kinds of machine learning

10. **Supervised learning.** Learning from input→answer pairs. It has two flavors: **regression** (predict a number, such as price or temperature) and **classification** (predict a category, such as spam/not-spam or which digit). Give many everyday examples of each.
11. **Unsupervised learning.** Finding structure without answers: grouping customers (clustering), compressing many columns into a few (dimensionality reduction), spotting weird items (anomaly detection). The analogy is sorting a pile of unlabeled photos into piles that "go together."
12. **Semi-supervised learning.** A few labeled examples plus many unlabeled ones. Explain why this matters: labels are expensive, raw data is cheap. Cover pseudo-labeling (the model labels easy cases for itself).
13. **Self-supervised learning.** The data supplies its own labels. Hide part of the input and predict it, for example the next word in a sentence or a masked-out patch of an image. This is the **bridge to chatbots**: large language models are pretrained by predicting the next token across trillions of words. Make this explicit, because it is the "aha" link between this chapter and the reader's daily experience.
14. **Reinforcement learning (overview).** An agent takes actions in an environment and gets rewards or penalties, like training a dog with treats or learning a video game by trial and error. Mention AlphaGo, robotics, and that chatbots are refined with RL from human feedback (RLHF) and, increasingly, RL on verifiable tasks such as math and code. Leave the details for later chapters.
15. **Other learning setups (brief).** Transfer learning (reuse a model trained on one task), fine-tuning, few-shot learning, active learning (the model asks for labels on the examples it is most unsure about), and online learning (updating continuously as data streams in).

### Part C — How learning actually happens

16. **Loss functions: measuring wrongness.** A loss is one number that says how bad the model's guesses are. For numbers, use squared error (MSE). For categories, use log loss / cross-entropy, which punishes confident wrong answers hard. Training means "make the loss small."
17. **Gradient descent intuition.** Picture being blindfolded on a hilly landscape and feeling which way is downhill, then taking a small step, over and over. The **gradient** is the slope; the **learning rate** is the step size. Show what happens when the step is too big (bouncing around) or too small (taking forever). Cover the terms *epoch*, *batch*, *stochastic gradient descent*, and *local minima*. No calculus needed; a single worked example of nudging one knob is enough.
18. **Linear regression as the worked example.** Fit a line to points (study hours vs. test score). Show slope and intercept as the two knobs, the error as vertical distances, and the line moving until total squared error is smallest. The reader can do this in a spreadsheet (Exercise 6).
19. **Logistic regression and decision boundaries.** Turn a score into a probability (0 to 1) with an S-shaped curve. A threshold (often 0.5) turns the probability into a yes/no. Explain the decision boundary as a line on a 2-D plot separating two colors of dots.
20. **Probabilities, confidence and calibration.** A model's "80% sure" is only meaningful if, across many such cases, it is right about 80% of the time. Link this to chatbot overconfidence.

### Part D — Is the model any good? Generalization and evaluation

21. **Train / validation / test split.** Split the data into a study set, a practice-quiz set (for tuning choices), and a sealed final exam you look at only once. Use a 70/15/15 example.
22. **Data leakage.** This is how models cheat by accident: information from the answer sneaks into the inputs (for example, a "treatment given" column when predicting disease), or test data leaks into training. Tell real cautionary tales.
23. **Overfitting and underfitting.** Underfitting is too simple (a straight line through a curve). Overfitting is too complex (a squiggle through every point, including the noise). Show the classic three-panel diagram.
24. **Bias–variance tradeoff.** Bias is systematic error from being too simple. Variance is jumpiness from being too sensitive to the particular training sample. Use the dartboard analogy. Mention that very large neural networks complicate the classic picture ("double descent") as a teaser.
25. **Regularization.** These are techniques that discourage over-complicated models: penalties on big weights (L2/ridge, L1/lasso), limiting tree depth, early stopping, dropout (later chapter), and getting more data. The analogy is "Occam's razor, enforced by math."
26. **Cross-validation.** Rotate which slice of data is held out (k-fold) and average the scores, so one lucky split doesn't fool you. Use stratified splits for imbalanced classes. For time series, never train on the future (walk-forward validation).
27. **Classification metrics.** Start from the **confusion matrix** (true positives, false positives, false negatives, true negatives). Then derive accuracy, precision, recall, specificity, and F1. Explain why accuracy misleads with rare events: a "model" that always says "no fraud" is 99.9% accurate and useless. Use medical testing and airport security as examples of when you care more about recall vs. precision.
28. **Thresholds, ROC curves and AUC.** Moving the threshold trades false alarms for misses. The ROC curve plots this trade, and AUC summarizes it (0.5 = coin flip, 1.0 = perfect). Mention precision–recall curves for rare-event problems.
29. **Regression metrics.** MSE, RMSE (error in original units), MAE (average absolute miss), R² (share of variation explained), and MAPE (percentage error). Show when each is most interpretable.
30. **Baselines and hyperparameter tuning.** Always compare to a dumb baseline (predict the average; predict the most common class). Tune with grid search, random search, or Bayesian optimization, using validation data only.
31. **Benchmarks and Goodhart's law.** Shared test sets (MNIST, ImageNet, later LLM benchmarks) drive progress but can be "overfit" by a whole field. "When a measure becomes a target, it ceases to be a good measure." This sets up later chapters on LLM evals and benchmark contamination.

### Part E — The classical algorithm zoo

32. **k-Nearest Neighbors (kNN).** "You are like your closest neighbors." To classify a new point, find the k most similar labeled points and take a vote. It needs no training and is slow at prediction. It introduces **distance** and **similarity**, which come back later as embeddings and vector search.
33. **Linear and logistic regression (revisited).** These are the workhorses of science, economics and medicine because they are interpretable: each weight says how much a feature pushes the answer.
34. **Naive Bayes.** Count how often words appear in spam vs. normal email and combine the evidence using probability (Bayes' rule). It is "naive" because it assumes the clues are independent. This was the classic early spam filter.
35. **Decision trees.** A flowchart of yes/no questions ("Income > $50k? → Has prior default?") learned from data. Easy to read, but prone to overfitting. Introduce impurity/information gain informally: pick the question that best separates the classes.
36. **Random forests (bagging).** Many trees, each trained on a random sample of rows and features, then voting. This is "wisdom of crowds" and reduces variance.
37. **Gradient boosting (XGBoost, LightGBM, CatBoost).** Trees built in sequence, each one fixing the previous ones' mistakes. For spreadsheet-style (tabular) data, boosted trees have been the default winner of Kaggle competitions and industry systems for a decade. Then add the 2025–2026 twist: **tabular foundation models** such as TabPFN now rival or beat tuned boosted trees on many small-to-medium benchmarks (see Section 4).
38. **Support Vector Machines (SVMs).** Find the widest "street" separating two classes. The kernel trick separates curvy data by implicitly lifting it into higher dimensions. SVMs dominated the 2000s before deep learning.
39. **k-means and other clustering.** Choose k centers, assign points to the nearest one, move each center to the middle of its group, and repeat. Discuss choosing k (the elbow method) and alternatives such as hierarchical clustering and DBSCAN (density-based, finds odd shapes and noise).
40. **Dimensionality reduction (PCA, t-SNE, UMAP).** PCA finds the directions along which the data varies most, like finding the best camera angle to photograph a 3-D object in 2-D. t-SNE and UMAP make 2-D "maps" of high-dimensional data for visualization. This is the bridge to embeddings.
41. **Anomaly detection.** Flag the unusual: z-scores (how many standard deviations from normal), isolation forests (anomalies are easy to isolate with few random cuts), and autoencoders (later). Applications include credit-card fraud, machine failure and network intrusion.
42. **Recommender systems.** Content-based ("you liked sci-fi, here is more sci-fi"), collaborative filtering ("people like you also liked..."), matrix factorization (hidden "taste dimensions"), the cold-start problem, implicit vs. explicit feedback, and filter bubbles. Use the Netflix Prize (2006–2009, $1M, ~100M ratings) as the story.
43. **Time-series forecasting.** Trend, seasonality, noise, and lags. Methods run from naive forecasts ("tomorrow = today") and moving averages through exponential smoothing and ARIMA to gradient boosting with lag features and Prophet. In 2024–2026 came pretrained **time-series foundation models** (Amazon Chronos-2, Google TimesFM 2.5). Emphasize backtesting and never peeking at the future.
44. **The bridge to neural networks.** The perceptron is just logistic regression with a different name. Stack many and you get a neural network. Explain why deep learning won on images, audio and text (it learns its own features from raw pixels and characters), while classical ML still dominates many business tables.
45. **Choosing an algorithm.** Give a decision cheat-sheet: what kind of data, how much, whether you need explanations, and how fast predictions must be. Close with "start simple, add complexity only if it pays."

### Part F — Data: the fuel

46. **What data is.** Structured (tables), semi-structured (JSON, logs), and unstructured (text, images, audio, video). Data types (numeric, categorical, ordinal, text, date/time). File formats (CSV, JSON, Parquet). How a photo becomes numbers (pixels) and how text becomes numbers (tokens; a preview of the LLM chapter).
47. **Where data comes from.** App and website logs, transactions, sensors and IoT, surveys, government open data, scientific instruments, user-generated content, the public web, licensed archives, paid human labeling, and synthetic generation. Also "data exhaust": every click and swipe becomes data.
48. **Famous datasets as a history of AI.** Iris (1936) → MNIST (1998) → Netflix Prize (2006) → ImageNet (2009) and AlexNet (2012) → COCO → Common Crawl → C4 → The Pile (2020) → LAION-5B (2022) → RedPajama/Dolma/FineWeb (2023–24) → Common Pile (2025). Show how dataset size grew from thousands of rows to tens of trillions of tokens, and how each dataset unlocked an era.
49. **Data collection and web scraping.** Crawlers, HTML parsing, APIs, rate limits, robots.txt (a polite "please don't" sign, not a lock), terms of service, paywalls. The 2025–26 shift is toward blocking AI crawlers by default and charging for access (Cloudflare Pay Per Crawl, the RSL licensing standard).
50. **Labeling and annotation.** Task types: image tags, bounding boxes, segmentation masks, transcription, sentiment, named entities, and, for chatbots, writing ideal answers, ranking two responses (preference data), red-teaming, and grading reasoning. Quality control: gold-standard questions, consensus, inter-annotator agreement, audits. The **industry** runs from Mechanical Turk crowdwork to expert data vendors (Scale AI, Surge AI, Mercor, Handshake, micro1, Turing, Invisible) paying doctors, lawyers and PhDs. Cover the human side too: low-wage offshore labelers, psychologically hard content-moderation work, and gig instability.
51. **Data cleaning.** Missing values (drop vs. fill), duplicates, typos and inconsistent categories ("NY", "New York", "new york"), unit mix-ups, impossible values, outliers, time-zone errors. At web scale: deduplication, language identification, quality classifiers, removing boilerplate, toxic content and personal information. "Garbage in, garbage out" and the folk statistic that data work takes most of a data scientist's time (frame it as a common saying, not a measured figure).
52. **Feature engineering.** Turning raw data into useful inputs: one-hot encoding categories, scaling numbers, extracting day-of-week from dates, ratios ("debt ÷ income"), text to word counts / TF-IDF, binning, feature selection. Explain that deep learning automated much of this for images and text, but it still matters enormously for tables.
53. **Databases and SQL basics.** Tables, rows, columns, primary keys, relationships; the four everyday SQL moves (SELECT columns, WHERE filter, GROUP BY summarize, JOIN combine tables). Relational vs. NoSQL vs. **vector databases** (a preview of retrieval-augmented generation).
54. **Data pipelines, warehouses, lakes and lakehouses.** ETL/ELT (extract, transform, load), batch vs. streaming, scheduled jobs and orchestration. A warehouse is a tidy library of clean tables; a lake is a big storage room of raw files; a lakehouse combines the two. Name the major platforms (Snowflake, Google BigQuery, Databricks, Amazon Redshift) without endorsing any.
55. **Data quality and documentation.** Dimensions: accuracy, completeness, consistency, timeliness, validity, uniqueness. Lineage (where did this number come from?), versioning, datasheets for datasets, data cards / model cards.
56. **Bias in data.** Sampling bias, historical bias, measurement bias, label bias, representation gaps, feedback loops. Cases: Amazon's scrapped recruiting model (reported 2018), the COMPAS recidivism debate (2016), Gender Shades face-analysis error gaps (2018). Fairness metrics give a short introduction to the idea that different definitions of "fair" can mathematically conflict.
57. **Privacy.** Personal information, anonymization and how it fails (re-identification in the Netflix Prize and AOL search-log releases), GDPR/CCPA basics, consent, data minimization, differential privacy (adding calibrated noise), federated learning (training where the data lives), and models memorizing and regurgitating training data.
58. **Synthetic data.** Data produced by simulations or by models: game-engine images for self-driving cars, fake-but-realistic patient records, LLM-written textbooks and Q&A, "distillation" from a stronger model, reasoning traces checked by a verifier. Benefits: privacy, rare cases, scale. Risks: inheriting the generator's errors and biases, and "model collapse" when models train recursively on their own outputs without fresh human data.
59. **Data licensing, copyright and lawsuits.** Copyright basics, fair use (US), text-and-data-mining exceptions (EU/UK/Japan), opt-outs, licensing deals vs. lawsuits. Walk through the key cases and deals as of October 2026 (Section 4) and the open questions: Is training fair use? Does it matter if the data was pirated? Are model outputs infringing? What do transparency laws require?
60. **The "data wall" debate.** Will we run out of high-quality human text? Cover Epoch AI's estimate (~300 trillion tokens of usable public text, fully used sometime 2026–2032) and Ilya Sutskever's "we have but one internet" (NeurIPS, December 2024). Then the escape routes: synthetic data, multimodal data (video, audio), RL environments and verifiable tasks, private/proprietary data, expert-written data, better data efficiency, and repeating data. Present this as a live debate, not a settled fact.

### Part G — The data science / ML workflow and tools

61. **The project lifecycle.** Frame the business question → get data → explore (EDA) → clean → engineer features → baseline → train models → evaluate → deploy → monitor → retrain. Stress that framing the right question and getting the right data matter more than the algorithm.
62. **The toolbox.** Spreadsheets (still valid), Python (the lingua franca), Jupyter notebooks and Google Colab (code + text + charts in one page), pandas (tables in code), NumPy, matplotlib/seaborn (charts), scikit-learn (classical ML), XGBoost/LightGBM, SQL, Kaggle (datasets and competitions), Hugging Face (models and datasets), AutoML and no-code tools (Teachable Machine, Orange, BigQuery ML). AI coding assistants now write much of this code.
63. **MLOps basics.** Deploying a model behind an app, monitoring for **data drift** (the world changes; for example, consumer behavior shifted sharply in 2020), retraining, experiment tracking, reproducibility.
64. **Classical ML in the LLM era.** LLMs as labelers, feature extractors (embeddings) and coding assistants; when a simple logistic regression beats an expensive LLM call (cost, speed, explainability, regulated settings); tabular and time-series foundation models; "AI agents doing data science." Close by pointing forward to neural networks and transformers.

---

## 2. Glossary candidates (plain-English definitions)

**Core concepts**

1. **Algorithm** — A step-by-step procedure for solving a problem. In ML, it usually means the procedure that learns a model from data (for example, "the decision-tree algorithm").
2. **Artificial intelligence (AI)** — The broad goal of making computers do things that seem to require intelligence. Machine learning is today's dominant way of achieving it.
3. **Machine learning (ML)** — Getting computers to perform a task by learning patterns from examples instead of following hand-written rules.
4. **Rules-based system** — A program whose behavior is entirely spelled out by human-written if-then rules. Also called an "expert system" in older AI.
5. **Model** — The learned thing: a mathematical function with adjustable numbers inside that turns inputs into predictions. Physically, it is a file of numbers plus code that uses them.
6. **Parameter** — One adjustable number inside a model that is set by training. Models range from 2 parameters (a line) to trillions (frontier LLMs).
7. **Weight** — A parameter that says how strongly one input influences the output. "Weights" is often used loosely to mean all of a model's learned numbers.
8. **Bias (term)** — A parameter that shifts the output up or down regardless of input (the intercept of a line). It is unrelated to unfairness.
9. **Hyperparameter** — A setting chosen by a human before training, such as learning rate, tree depth, or number of clusters. It controls how learning happens but is not itself learned.
10. **Feature** — One measurable input property of an example, such as square footage, word count, or pixel brightness. A column in a data table.
11. **Label (target)** — The correct answer the model should learn to predict for an example, such as "spam" or "$410,000."
12. **Example (instance, sample, row)** — One record in a dataset: one email, one house, one image.
13. **Dataset** — A collection of examples used to train or test models.
14. **Training** — The process of adjusting a model's parameters so its predictions on example data get better.
15. **Inference** — Using a trained model to make predictions on new inputs. Every chatbot reply is inference.
16. **Prediction** — The model's output for an input. It can be a number, a category, a probability, or generated text.
17. **Generalization** — How well a model performs on new data it never saw during training. This is the true goal of ML.
18. **Pattern** — A regularity in data, such as "emails with many exclamation marks are often spam," that a model can exploit.

**Types of learning**

19. **Supervised learning** — Learning from examples that come with correct answers (labels).
20. **Unsupervised learning** — Finding structure, such as groups or simpler representations, in data that has no labels.
21. **Semi-supervised learning** — Learning from a small labeled set plus a large unlabeled set.
22. **Self-supervised learning** — Learning where the labels are created automatically from the data itself, for example by hiding the next word and asking the model to predict it. This is how LLMs are pretrained.
23. **Reinforcement learning (RL)** — Learning by trial and error: an agent takes actions, receives rewards or penalties, and improves its strategy.
24. **Agent (RL)** — The learner/decision-maker in reinforcement learning.
25. **Environment** — The world, game or simulation an RL agent acts in.
26. **Reward** — The numeric score an RL agent receives that tells it how good an outcome was.
27. **Policy** — An RL agent's strategy: the rule for choosing actions in each situation.
28. **RLHF (reinforcement learning from human feedback)** — Fine-tuning a model using human judgments (often rankings of two responses) as the reward signal. It is key to how chatbots are made helpful.
29. **Transfer learning** — Reusing knowledge from a model trained on one task to help with a different task.
30. **Fine-tuning** — Further training an already-trained model on a smaller, specific dataset.
31. **Pretraining** — The large first stage of training on broad data, before task-specific fine-tuning.
32. **Few-shot / zero-shot learning** — Doing a task from just a few examples, or none, usually by leveraging a large pretrained model.
33. **Active learning** — A strategy where the model picks which unlabeled examples it would most benefit from having humans label.
34. **Online learning** — Updating a model continuously as new data arrives, rather than training once.

**Task types**

35. **Regression** — Predicting a number (price, temperature, demand).
36. **Classification** — Predicting a category (spam/not spam; cat/dog/bird).
37. **Binary classification** — Classification with exactly two categories.
38. **Multiclass classification** — Classification with three or more mutually exclusive categories.
39. **Multilabel classification** — Each example can have several labels at once (a photo tagged "beach" and "dog").
40. **Clustering** — Grouping similar examples together without predefined labels.
41. **Dimensionality reduction** — Compressing many features into fewer while keeping the important information.
42. **Anomaly (outlier) detection** — Identifying examples that are unusually different from the rest.
43. **Recommender system** — A system that predicts what items (movies, products, posts) a person will like.
44. **Time series** — Data recorded over time in order (daily sales, hourly temperature).
45. **Forecasting** — Predicting future values of a time series.
46. **Ranking** — Ordering items by predicted relevance, as search engines and feeds do.

**How training works**

47. **Loss function (cost function)** — A formula that turns the model's mistakes into a single number. Training tries to make it as small as possible.
48. **Mean squared error (MSE)** — The average of squared differences between predictions and true numbers. It punishes big misses heavily.
49. **Mean absolute error (MAE)** — The average size of the misses, ignoring direction.
50. **Cross-entropy / log loss** — The standard loss for classification. It heavily penalizes being confidently wrong.
51. **Optimization** — The process of searching for parameter values that minimize the loss.
52. **Gradient** — The direction and steepness of the loss's slope with respect to each parameter. It tells you which way to nudge each knob.
53. **Gradient descent** — Repeatedly nudging parameters a small step "downhill" against the gradient to reduce loss.
54. **Learning rate** — The size of each gradient-descent step. Too large overshoots; too small crawls.
55. **Stochastic gradient descent (SGD)** — Gradient descent using small random subsets of data (batches) each step, which is faster and noisier.
56. **Batch (mini-batch)** — The group of examples used for one update step.
57. **Epoch** — One full pass through the entire training dataset.
58. **Iteration / step** — One parameter update.
59. **Local minimum** — A valley in the loss landscape that is lower than its surroundings but not the lowest overall.
60. **Convergence** — When training settles and the loss stops improving meaningfully.
61. **Decision boundary** — The dividing line (or surface) where a classifier switches from predicting one class to another.
62. **Probability score** — A model's estimated chance (0–1) that an example belongs to a class.
63. **Threshold** — The cutoff that turns a probability into a yes/no decision (often 0.5, but adjustable).
64. **Calibration** — Whether a model's stated confidence matches reality (things it calls "70% likely" happen about 70% of the time).

**Generalization and evaluation**

65. **Training set** — The data the model learns from.
66. **Validation set** — Held-out data used to compare models and tune hyperparameters during development.
67. **Test set** — Data locked away until the very end to give an honest final score.
68. **Holdout** — Any data deliberately kept out of training for evaluation.
69. **Overfitting** — When a model memorizes quirks and noise in its training data and so does worse on new data.
70. **Underfitting** — When a model is too simple to capture the real pattern, so it does poorly even on training data.
71. **Bias (statistical)** — Systematic error from overly simple assumptions: consistently missing in the same direction.
72. **Variance (statistical)** — How much a model's predictions would change if trained on a different sample. High variance means jumpy and overfit.
73. **Bias–variance tradeoff** — Making a model more flexible lowers bias but raises variance; good models balance the two.
74. **Regularization** — Any technique that discourages unnecessary complexity to reduce overfitting.
75. **L1 / L2 regularization (lasso / ridge)** — Adding a penalty for large weights. L1 can push some weights to exactly zero (feature selection); L2 shrinks them all.
76. **Early stopping** — Halting training when validation performance stops improving.
77. **Cross-validation (k-fold)** — Splitting data into k parts, training k times with a different part held out each time, and averaging the scores.
78. **Stratified sampling** — Splitting data so each part keeps the same mix of classes as the whole.
79. **Data leakage** — When information that wouldn't be available at prediction time sneaks into training, producing falsely good scores.
80. **Baseline** — A simple reference model (such as "always predict the average") that any real model must beat.
81. **Hyperparameter tuning** — Systematically trying hyperparameter settings (grid search, random search, Bayesian optimization) to find the best one on validation data.
82. **Benchmark** — A standard dataset and metric used to compare models across research groups.
83. **Goodhart's law** — "When a measure becomes a target, it ceases to be a good measure."

**Metrics**

84. **Confusion matrix** — A 2×2 (or larger) table counting correct and incorrect predictions by type.
85. **True positive (TP)** — The model said "yes" and the answer was yes.
86. **False positive (FP)** — The model said "yes" but the answer was no (a false alarm; a "Type I error").
87. **False negative (FN)** — The model said "no" but the answer was yes (a miss; a "Type II error").
88. **True negative (TN)** — The model said "no" and the answer was no.
89. **Accuracy** — The share of all predictions that were correct. It is misleading when one class is rare.
90. **Precision** — Of everything the model flagged as positive, the share that truly was. "When it cries wolf, how often is there a wolf?"
91. **Recall (sensitivity, true positive rate)** — Of all real positives, the share the model caught. "How many wolves did it spot?"
92. **Specificity** — Of all real negatives, the share correctly left alone.
93. **F1 score** — A single number combining precision and recall (their harmonic mean). It is high only when both are high.
94. **ROC curve** — A graph of true-positive rate vs. false-positive rate as the threshold slides from strict to lenient.
95. **AUC (area under the ROC curve)** — A single 0.5–1.0 score summarizing the ROC curve: the chance the model ranks a random positive above a random negative.
96. **Precision–recall curve** — A graph of precision vs. recall across thresholds. It is more informative than ROC when positives are rare.
97. **Class imbalance** — When one category vastly outnumbers another (fraud vs. normal transactions).
98. **RMSE** — The square root of MSE, which puts error back into the original units (dollars, degrees).
99. **R² (coefficient of determination)** — The share of the variation in the target that the model explains (1 = perfect, 0 = no better than the average).
100. **MAPE** — Mean absolute percentage error: the average miss as a percentage of the true value.

**Classical algorithms**

101. **Linear regression** — Fits a straight line (or flat plane) through data to predict a number.
102. **Logistic regression** — Despite the name, a classification method. It squashes a weighted sum into a 0–1 probability with an S-shaped (sigmoid) curve.
103. **Sigmoid function** — The S-shaped curve that maps any number to a value between 0 and 1.
104. **k-nearest neighbors (kNN)** — Predicts by looking at the k most similar known examples and taking a vote or average.
105. **Distance / similarity metric** — A way to measure how alike two examples are (for example, straight-line Euclidean distance or cosine similarity).
106. **Naive Bayes** — A probabilistic classifier that combines evidence from each feature, assuming (naively) that features are independent.
107. **Bayes' rule** — A formula for updating a probability when you get new evidence.
108. **Decision tree** — A flowchart of yes/no questions learned from data, ending in predictions at the leaves.
109. **Node / leaf / depth** — In a tree: a question point / a final answer / how many questions deep the tree goes.
110. **Ensemble** — Combining many models so their errors partly cancel out.
111. **Bagging** — Training many models on random resamples of the data and averaging their votes.
112. **Random forest** — A bagged ensemble of decision trees, each also seeing a random subset of features.
113. **Boosting** — Building models in sequence, each focusing on the errors of the ones before.
114. **Gradient boosting** — Boosting where each new tree is fit to the remaining errors using gradient descent ideas.
115. **XGBoost / LightGBM / CatBoost** — Popular, fast open-source gradient-boosting libraries that dominate tabular-data competitions.
116. **Support vector machine (SVM)** — A classifier that finds the boundary with the widest margin between classes.
117. **Kernel trick** — A mathematical shortcut that lets linear methods like SVMs draw curved boundaries.
118. **k-means** — A clustering algorithm that repeatedly assigns points to the nearest of k centers and moves each center to its group's average.
119. **Centroid** — The center point (average) of a cluster.
120. **Hierarchical clustering** — Building a tree of nested clusters by repeatedly merging the closest groups.
121. **DBSCAN** — A density-based clustering method that finds arbitrarily shaped clusters and labels sparse points as noise.
122. **Principal component analysis (PCA)** — Finds a few new combined axes that capture most of the variation in many features.
123. **t-SNE / UMAP** — Techniques for squashing high-dimensional data into a 2-D map that keeps similar items near each other, mainly for visualization.
124. **Embedding** — A list of numbers representing an item (word, image, product) so that similar items get similar lists.
125. **Isolation forest** — An anomaly detector based on the idea that odd points can be isolated with fewer random splits.
126. **Z-score** — How many standard deviations a value is from the average. It is a simple anomaly flag.
127. **Collaborative filtering** — Recommending items based on the preferences of similar users or similar items.
128. **Content-based filtering** — Recommending items similar in their attributes to ones the user liked.
129. **Matrix factorization** — Breaking a big user × item ratings table into hidden "taste" factors to fill in missing ratings.
130. **Cold-start problem** — Difficulty recommending for new users or new items with no history.
131. **Trend / seasonality** — In time series: a long-run upward or downward drift / a repeating cycle (weekly, yearly).
132. **Lag feature** — A past value used as an input, for example "sales 7 days ago."
133. **ARIMA** — A classic statistical forecasting model built from past values and past errors.
134. **Exponential smoothing** — Forecasting with a weighted average that favors recent observations.
135. **Backtesting (walk-forward validation)** — Testing a forecasting method by repeatedly training on the past and predicting the next period.
136. **Perceptron** — The simplest artificial neuron: a weighted sum followed by a threshold. It is the ancestor of neural networks.
137. **Neural network** — A model built from many layers of simple connected units. It is the basis of deep learning and covered in the next chapter.
138. **Tabular foundation model** — A model pretrained (often on synthetic tables) to make predictions on new spreadsheet-style datasets with little or no training. TabPFN is the best-known example.
139. **Interpretability / explainability** — How easily a human can understand why a model made a prediction.
140. **Feature importance** — A measure of how much each feature contributed to a model's predictions.

**Data**

141. **Data** — Recorded facts or measurements: numbers, text, images, sounds, clicks.
142. **Structured data** — Data organized in rows and columns with a fixed format (spreadsheets, database tables).
143. **Unstructured data** — Data without a predefined table format: free text, images, audio, video.
144. **Semi-structured data** — Data with some organization but no rigid table, such as JSON or log files.
145. **Categorical feature** — A feature with a fixed set of categories (color, country).
146. **Numerical feature** — A feature that is a measured quantity (age, price).
147. **CSV** — "Comma-separated values": a plain-text spreadsheet format.
148. **JSON** — A text format for nested, labeled data, widely used by web apps and APIs.
149. **Parquet** — A compressed, column-based file format used for large analytical datasets.
150. **Token** — A chunk of text (a word or word-piece) that language models read. Dataset sizes for LLMs are measured in tokens.
151. **Corpus** — A large collection of text used for training or study.
152. **Web scraping / crawling** — Automatically downloading and extracting content from websites. A crawler follows links from page to page.
153. **robots.txt** — A file on a website telling automated crawlers which parts they may visit. It is a request, not an enforcement mechanism.
154. **API** — An "application programming interface": a structured way for programs to request data or services from another system.
155. **Annotation / labeling** — Humans (or models) adding labels to raw data: tagging images, transcribing audio, rating answers.
156. **Bounding box / segmentation mask** — Image labels: a rectangle around an object / a pixel-precise outline of it.
157. **Preference data** — Human judgments comparing two or more model outputs ("A is better than B"), used to train chatbots.
158. **Gold standard (ground truth)** — The trusted correct labels against which predictions or annotators are checked.
159. **Inter-annotator agreement** — How often different human labelers give the same label. Low agreement signals an ambiguous task.
160. **Crowdsourcing** — Splitting labeling work into small tasks done by many online workers (for example, Amazon Mechanical Turk).
161. **Data cleaning** — Fixing or removing incorrect, duplicate, missing or inconsistent data.
162. **Missing value / imputation** — An empty cell / filling it with a reasonable estimate (such as the column's median).
163. **Deduplication** — Removing repeated or near-identical examples, which is critical for web-scale text.
164. **Outlier** — A value far from the rest. It may be an error or a genuinely rare event.
165. **Feature engineering** — Creating more useful input features from raw data using domain knowledge.
166. **One-hot encoding** — Turning a category into several yes/no columns (red → [1,0,0]).
167. **Normalization / standardization (scaling)** — Rescaling numeric features to comparable ranges so no feature dominates just by its units.
168. **TF-IDF / bag-of-words** — Classic ways to turn text into numbers by counting words, weighting rare informative words more.
169. **Database** — An organized system for storing and retrieving data.
170. **Relational database** — A database storing data in linked tables, queried with SQL.
171. **SQL** — "Structured Query Language", the standard language for asking questions of relational databases.
172. **Primary key / join** — A column that uniquely identifies each row / combining two tables on a shared key.
173. **NoSQL database** — Databases that don't use the classic table model (document, key-value, graph stores).
174. **Vector database** — A database optimized to find items whose embeddings are most similar to a query. It is used in AI search and RAG.
175. **Data pipeline** — An automated series of steps that moves and transforms data from sources to where it's used.
176. **ETL / ELT** — Extract–Transform–Load (clean before storing) vs. Extract–Load–Transform (store raw, clean later).
177. **Data warehouse** — A central store of cleaned, structured data organized for analysis and reports.
178. **Data lake** — A large, cheap store of raw data in many formats, cleaned only when needed.
179. **Lakehouse** — An architecture combining a lake's cheap flexible storage with a warehouse's structure and querying.
180. **Data quality** — How fit data is for its purpose: accurate, complete, consistent, timely, valid, unique.
181. **Data lineage** — The record of where data came from and every transformation it went through.
182. **Datasheet / data card / model card** — Standard documentation describing a dataset's (or model's) origin, contents, intended uses and limitations.
183. **Data drift / concept drift** — When incoming data (or the relationship between inputs and answers) changes over time, so a once-good model degrades.
184. **Sampling bias** — When the collected data doesn't represent the population the model will serve.
185. **Historical bias** — When data faithfully records a past that was unfair, so a model learns to repeat it.
186. **Proxy variable** — A feature that indirectly stands in for a sensitive attribute (zip code standing in for race).
187. **Feedback loop** — When a model's predictions shape the future data it is trained on (predictive policing sends more patrols, which record more incidents).
188. **Algorithmic fairness** — The study of whether models treat groups equitably. It includes several competing mathematical definitions.
189. **Personally identifiable information (PII)** — Data that can identify a person (name, email, ID numbers, face).
190. **Anonymization / re-identification** — Removing identifying details / figuring out who someone is anyway by linking data.
191. **Differential privacy** — A mathematical guarantee, achieved by adding calibrated noise, that results barely change whether or not any one person's data is included.
192. **Federated learning** — Training a shared model across many devices or institutions without centralizing their raw data.
193. **Memorization (training-data extraction)** — When a model can reproduce exact pieces of its training data, a privacy and copyright concern.
194. **GDPR / CCPA** — The EU's and California's main personal-data protection laws.
195. **Synthetic data** — Artificially generated data (by simulation or by AI models) used in place of, or alongside, real data.
196. **Distillation** — Training a smaller "student" model on outputs produced by a larger "teacher" model.
197. **Model collapse** — Degradation that can occur when models are trained repeatedly on model-generated data, losing rare patterns and diversity.
198. **Data augmentation** — Creating extra training examples by modifying existing ones (flipping, cropping or rotating images; paraphrasing text).
199. **Copyright** — Legal rights an author has over original creative works, including control over copying.
200. **Fair use** — A US legal doctrine allowing some unlicensed uses of copyrighted works, judged case by case on four factors.
201. **Text and data mining (TDM) exception** — Laws (EU, UK, Japan, others) allowing automated analysis of content under certain conditions, sometimes with opt-outs.
202. **Data licensing** — Paying, or otherwise getting permission, to use data, often through a contract with a publisher or platform.
203. **Data wall** — The idea that AI progress could stall because the supply of high-quality human-generated training data is running out.
204. **RL environment** — A simulated task (a software sandbox, a website clone, a math checker) where a model can practice and get automatically scored. It is increasingly treated as "the new training data."
205. **Exploratory data analysis (EDA)** — Looking at data through summaries and charts before modeling, to understand it and spot problems.
206. **Notebook (Jupyter / Colab)** — An interactive document mixing runnable code, results, charts and notes.
207. **Python** — The programming language most widely used for data science and AI.
208. **pandas** — A Python library for working with tables of data ("DataFrames").
209. **scikit-learn** — The standard Python library for classical machine learning.
210. **Kaggle** — A Google-owned website hosting data science competitions, free datasets and notebooks.
211. **Hugging Face** — A platform hosting millions of shared AI models and hundreds of thousands of datasets.
212. **AutoML** — Tools that automatically try many algorithms and settings to find a good model.
213. **MLOps** — The practices and tools for deploying, monitoring and maintaining ML models in production.

---

## 3. Prerequisites and dependencies

Read "A → B" as "A must be taught before B."

**Spine (must go in this order)**

- Programs as recipes → where rules break → learning from examples → what a model is → parameters → features & labels → training vs. inference → generalization.
- Features & labels → supervised learning → regression vs. classification.
- Generalization → train/validation/test split → overfitting/underfitting → bias–variance → regularization → cross-validation.
- What a model is + parameters → loss function → gradient descent → linear regression worked example → logistic regression → probability/threshold → calibration.
- Classification + threshold → confusion matrix → accuracy → precision/recall → F1 → ROC/AUC (ROC needs both threshold and confusion matrix).
- Regression → MSE/MAE/RMSE/R².

**Algorithm dependencies**

- Distance/similarity → kNN → k-means → (later) embeddings and vector search.
- Decision tree → overfitting (trees are the perfect demo) → bagging → random forest → boosting → gradient boosting (needs a loose idea of gradient descent) → XGBoost.
- Logistic regression → perceptron → neural networks (next chapter).
- Linear regression + regularization → ridge/lasso.
- Basic probability → Bayes' rule → naive Bayes.
- Decision boundary → SVM → kernel trick (optional sidebar).
- Features as columns → dimensionality reduction → PCA → t-SNE/UMAP → embeddings.
- Clustering + the idea of "normal" → anomaly detection.
- Similarity + matrix (table) intuition → collaborative filtering → matrix factorization → (later) neural recommenders.
- Train/test split + leakage → time-series cross-validation → forecasting.

**Learning-paradigm dependencies**

- Supervised → unsupervised (contrast) → semi-supervised (blend) → self-supervised (labels from data) → next-token prediction (LLM chapter).
- Reward/agent/environment basics → RL overview → RLHF and RL environments (alignment and post-training chapters).

**Data dependencies**

- What data is → where data comes from → famous datasets → scraping/collection → labeling → cleaning → feature engineering.
- Tables (rows/columns) → SQL → warehouses/lakes → pipelines.
- Sampling and generalization → bias in data → fairness.
- PII basics → anonymization → re-identification → differential privacy / federated learning.
- Self-supervised learning + famous web datasets + tokens → the data wall → synthetic data / RL environments.
- Scraping + copyright basics → fair use → lawsuits and licensing deals.

**Cross-chapter dependencies**

- This chapter must precede: neural networks/deep learning, transformers/LLMs, training & post-training, evaluation/benchmarks, AI ethics/fairness, compute (training vs. inference cost depends on understanding the two phases).
- It depends on: a gentle intro to "what a computer/program is" and basic number sense (averages, percentages, reading a chart). No calculus, statistics or programming is assumed; introduce averages, standard deviation and probability in sidebars.

---

## 4. Current state / key facts (2025–2026)

### Training-data scale and the data wall

- **Public web scale.** Common Crawl's August 2026 crawl (CC-MAIN-2026-34) captured **2.14 billion web pages, 360 TiB uncompressed**, crawled August 7–20, 2026. Monthly crawls have been running about 2.1–2.2 billion pages in 2026. https://commoncrawl.org/blog/august-2026-crawl-archive-now-available
- **Pretraining token counts.** Meta said Llama 4 was pretrained on "more than 30 trillion tokens" (April 5, 2025): https://ai.meta.com/blog/llama-4-multimodal-intelligence/ . Alibaba said Qwen3 was pretrained on ~36 trillion tokens across 119 languages, using Qwen2.5-Math/Coder to generate synthetic textbooks and Q&A and Qwen2.5-VL to extract text from PDFs (April 29, 2025): https://qwenlm.github.io/blog/qwen3/ . For comparison, MNIST is 70,000 tiny images.
- **Epoch AI's data-wall estimate.** About **300 trillion tokens** of effective high-quality public human text (90% CI 100T–1,000T), expected to be fully used **between 2026 and 2032**. Compute-optimal scaling would hit it around 2028; heavier "overtraining" earlier. Escape routes named: synthetic data, other modalities, data efficiency. Published June 6, 2024; no newer headline estimate was found in October 2026. https://epoch.ai/blog/will-we-run-out-of-data-limits-of-llm-scaling-based-on-human-generated-data
- **Ilya Sutskever (NeurIPS, December 2024)** argued pretraining "as we know it will end" because "we have but one internet," calling data the "fossil fuel of AI." Widely reported; cite the talk video in the book.
- **Shift to RL environments and verifiable tasks.** 2025–26 industry commentary describes simulated environments as "the new training data" (Mayfield, https://www.mayfield.com/reinforcement-learning-rl-environments-issue-36/). DeepSeek-V3.2's technical report (December 2025) describes large-scale synthetic agentic task generation for RL (https://arxiv.org/abs/2512.02556). Mercor agreed to buy Deeptune, which builds simulated software environments for training agents (reported July 2026, https://dealroom.co/news/137121-mercor-doubles-to-2b-gross-revenue-run-rate-as-ai-labs-buy-expert-data/).
- **Model collapse** (training recursively on generated data without fresh human data degrades models): Shumailov et al., *Nature*, July 2024. https://www.nature.com/articles/s41586-024-07566-y

### Open datasets

- **FineWeb** (Hugging Face): **15 trillion tokens** from 96 Common Crawl snapshots; FineWeb-Edu subsets of 1.3T and 5.4T tokens; ODC-By license; NeurIPS 2024. https://arxiv.org/abs/2406.17557 . A multilingual FineWeb2 also exists. [verify size before print]
- **Common Pile v0.1** (EleutherAI with University of Toronto, Hugging Face, Ai2 and others, June 2025): an **8 TB** corpus of public-domain and openly licensed text from 30 sources. The 7B "Comma" models trained on it were competitive with Llama 1/2 7B, showing licensed-only training is viable at moderate scale. https://www.eleuther.ai/papers-blog/the-common-pile-v01-an-8tb-dataset-of-public-domain-and-openly-licensed-text
- **The Pile** (EleutherAI, released December 2020): 825 GiB from 22 sources, including the Books3 subset later at the center of copyright suits. https://arxiv.org/abs/2101.00027
- **Hugging Face Hub**: third-party counts in mid-2026 put it above 2 million public models (one API-based tally: ~3.0M on August 22, 2026) and roughly 0.7–1 million public datasets. Sources disagree; check https://huggingface.co/datasets live before print.
- **Kaggle**: 23.29 million accounts as of April 2025 (no 2026 figure found). https://en.wikipedia.org/wiki/Kaggle

### The data-labeling and expert-data industry

- **Scale AI / Meta.** In June 2025 Meta invested about **$14.3B for ~49%** of Scale AI (valuing it at ~$29B). Founder Alexandr Wang left to lead Meta's superintelligence effort, and Jason Droege became interim CEO. Several labs (reportedly including OpenAI and Google) pulled back work afterward. https://www.cdomagazine.tech/aiml/meta-takes-49-stake-in-scale-ai-ceo-alexandr-wang-joins-to-boost-ai-push . On **July 30, 2026** Scale named former Google Cloud COO (and ex-Illumina CEO) **Francis deSouza** as CEO, effective August 10, 2026, and said its enterprise/government applications business is on track to overtake its data business within ~18 months. https://axios.com/2026/07/30/scale-ai-google-cloud-coo-francis-desouza ; https://scale.com/blog/scale-appoints-new-ceo
- **Surge AI** (Edwin Chen): bootstrapped and profitable, with estimated >$1B revenue in 2024 (Sacra estimate ~$1.2B). In July 2025 Reuters reported it sought its first outside raise (up to $1B at ~$15B valuation). Later reports cite a target above $25B; no closed round was confirmed. https://sacra.com/c/surge-ai ; https://www.tipranks.com/news/the-fly/scale-ais-bigger-rival-surge-ai-seeks-up-to-1b-capital-raise-reuters-says-thefly
- **Mercor** (expert marketplace: doctors, lawyers, bankers, PhDs producing training data): $350M Series C at **$10B** valuation (October 2025). Bloomberg reported talks at **~$20B** (July 2026). The CEO claimed >$2B gross revenue run-rate in June 2026; this is self-reported gross, before contractor payouts. https://dealroom.co/news/137121-mercor-doubles-to-2b-gross-revenue-run-rate-as-ai-labs-buy-expert-data/ . In **March 2026** Mercor was hit by a supply-chain attack via poisoned versions of the open-source LiteLLM library, followed by multiple contractor class actions (from April 2026). https://www.pymnts.com/legal/2026/ai-startup-mercor-faces-lawsuit-over-data-breach/ ; https://www.staffingindustry.com/news/global-daily-news/ai-staffing-firm-mercor-faces-lawsuits-over-data-breach
- **Handshake** (the campus-jobs platform turned AI-data vendor): Sacra estimates ~$1.1B annualized gross revenue in April 2026, mostly from AI labeling with PhD/graduate experts; micro1 ~ $300M annualized. Estimates, not company-reported. https://sacra.com/research/handshake-indeed-for-data-labelers/
- **The structural trend**: work is moving from cheap generalist crowdwork (image boxes, simple tags) to **expert data** (STEM PhDs, physicians, lawyers, coders writing and grading hard problems, building RL tasks), with expert pay reported above $100/hour in some programs. Quality auditing and rater verification are becoming selling points.

### Copyright, lawsuits and licensing (status as of October 2026)

- **Bartz v. Anthropic** (N.D. Cal.). On June 23, 2025, Judge Alsup ruled that training on lawfully acquired books was fair use but that building a library from pirated copies (LibGen, Pirate Library Mirror) was not. The case settled for **$1.5 billion**, the largest copyright settlement in US history. Final approval came **July 2026** (Judge Araceli Martínez-Olguín), covering ~482,460 works at roughly **$3,100 per work**, split between authors and publishers, with 91%+ of works claimed. Payments are in tranches into 2027, and some appeals were filed in August 2026. https://news.bloomberglaw.com/ip-law/anthropic-authors-1-5-billion-deal-receives-final-approval ; https://writerbeware.blog/2026/07/23/anthropic-settlement-update-final-settlement-approved/
- **Kadrey v. Meta** (N.D. Cal.). On June 25, 2025, Judge Chhabria granted Meta summary judgment that training was fair use on the record these 13 authors presented, explicitly noting the ruling was narrow. Torrent-"seeding" distribution claims continued into 2026. https://www.nortonrosefulbright.com/en/knowledge/publications/ce8eaa5f/ai-in-litigation-series-an-update-on-ai-copyright-cases-in-2026
- **Thomson Reuters v. Ross Intelligence.** On **September 29, 2026**, the **Third Circuit affirmed** that Ross's copying of Westlaw headnotes to train a competing (non-generative) legal-search AI was **not fair use**. This is the first federal appellate ruling on fair use in AI training, and it does not decide the generative-AI question. https://www.musicbusinessworldwide.com/us-appeals-court-rejects-fair-use-defense-over-ai-training-as-thomson-reuters-wins-copyright-case-backed-by-riaa-and-nmpa/
- **NYT and other news orgs v. OpenAI/Microsoft** (consolidated MDL, S.D.N.Y.). Still in discovery in 2026. Courts ordered production of a 20-million-log sample of ChatGPT outputs (January 2026) and further log sets (March 2026). No trial date or settlement was found. https://www.nortonrosefulbright.com/en/knowledge/publications/ce8eaa5f/ai-in-litigation-series-an-update-on-ai-copyright-cases-in-2026
- **Getty Images v. Stability AI (UK High Court, November 4, 2025)**: Getty largely lost. Model weights that never stored copies of images were held not to be "infringing copies." Getty had dropped its training claim because training happened outside the UK. It won only narrow trademark points about reproduced watermarks. An appeal on the secondary-infringement point was permitted (December 2025, per case trackers). https://www.aippi.org/news/getty-images-v-stability-ai-uk-high-court-finds-no-secondary-copyright-infringement-in-landmark-genai-ruling/
- **Music.** Universal Music settled with Udio and agreed to build a licensed AI music platform (October 2025). Warner Music settled with Suno and Udio and partnered on licensed models (November 2025). Suno committed to replace its models with licensed ones in 2026. https://www.musicbusinessworldwide.com/universal-music-settles-udio-lawsuit-strikes-deal-for-licensed-ai-music-platform ; https://www.musicbusinessworldwide.com/warner-music-group-settles-with-suno-strikes-first-of-its-kind-deal-with-ai-song-generator/
- **Disney v. Midjourney** is pending (C.D. Cal.). Separately, **Disney and OpenAI** signed a three-year deal letting Sora generate short videos with 200+ Disney characters, alongside a **$1B Disney investment in OpenAI** (announced December 2025). Norton Rose overview above.
- **Reddit's scraping suits.** Reddit v. Anthropic (filed June 2025) was sent back to California state court as a contract/trespass/privacy case, not a copyright case. In October 2025 Reddit sued Perplexity, SerpApi, Oxylabs and AWMProxy for allegedly scraping Reddit content via Google results. https://news.bloomberglaw.com/litigation/reddit-gets-anthropic-ai-scraping-suit-sent-back-to-state-court
- **Licensing deals (examples):** Reddit–Google (~$60M/year, reported February 2024); OpenAI–News Corp (>$250M over 5 years, reported May 2024); Amazon–New York Times (~$20–25M/year, May 2025); **Meta–News Corp** (WSJ and other News Corp brands, up to **$50M/year for 3 years**, March 3, 2026, https://engadget.com/ai/meta-signs-a-multimillion-dollar-ai-licensing-deal-with-news-corp-234157902.html). OpenAI has the most publisher deals (two dozen or so by mid-2026). Timeline: https://digiday.com/media/a-timeline-of-the-major-deals-between-publishers-and-ai-tech-companies-in-2025/
- **Thaler v. Perlmutter**: the US Supreme Court declined review (March 2, 2026), leaving human authorship as a requirement for copyright in AI outputs (Norton Rose overview above).
- **US Copyright Office**, *Copyright and AI* Part 3 "Generative AI Training," pre-publication version released May 9, 2025. https://www.copyright.gov/ai/

### Crawling, consent and regulation

- **Cloudflare** began blocking known AI crawlers **by default** for new domains on July 1, 2025 and launched "Pay Per Crawl" (reviving HTTP 402 "Payment Required"). https://searchengineland.com/cloudflare-to-block-ai-crawlers-by-default-with-new-pay-per-crawl-initiative-457708
- **RSL (Really Simple Licensing)**, launched September 2025 by the RSL Collective and backed by Reddit, Yahoo, Medium, Quora and others, is a machine-readable standard for sites to state AI licensing and payment terms. https://shellypalmer.com/2025/09/rsl-a-new-ai-licensing-standard/
- **EU AI Act**: general-purpose AI obligations applied from **August 2, 2025**, including a public "sufficiently detailed summary" of training content using the Commission's template (published July 24, 2025) and a copyright policy. The voluntary GPAI Code of Practice was published July 10, 2025. The AI Office's enforcement and fining powers for GPAI start **August 2, 2026**. https://www.mayerbrown.com/en/insights/publications/2025/08/eu-ai-act-news-rules-on-general-purpose-ai-start-applying-guidelines-and-template-for-summary-of-training-data-finalized
- **California AB 2013** (signed 2024) requires generative-AI developers to post high-level documentation of their training data from January 1, 2026. [verify compliance status before print]

### Classical ML and tools

- **Tabular foundation models.** TabPFN-2.5 (Prior Labs, November 2025) reported leading the TabArena benchmark ahead of tuned tree ensembles on small-to-medium tables (https://arxiv.org/abs/2511.08667). **SAP agreed to acquire Prior Labs** (announced May 2026; >€1B commitment to a European structured-data AI lab; reported closed July 2026). https://tech.eu/2026/07/17/sap-acquires-prior-labs-just-18-months-after-launch-in-eur1b-deal/ . The lesson for readers: gradient boosting is still the practical default for tables, but "pretrained models for spreadsheets" are a fast-moving frontier.
- **Time-series foundation models.** Amazon's **Chronos-2** (October 2025) handles multivariate series and covariates; Google's **TimesFM 2.5** is available in BigQuery's AI.FORECAST; Salesforce Moirai and others compete on the GIFT-Eval benchmark. https://www.amazon.science/blog/introducing-chronos-2-from-univariate-to-universal-forecasting
- **pandas 3.0** released **January 21, 2026** (new default string dtype, Copy-on-Write by default). https://pandas.pydata.org/docs/whatsnew/v3.0.0.html . Older tutorials may show warnings or behave differently.
- **scikit-learn 1.8** released December 2025 (experimental GPU support via the Array API; Python 3.11–3.14). https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_8_0.html
- **Synthetic-data consolidation.** Gretel (synthetic tabular/text data) was acquired by NVIDIA in 2025; gretel.ai now redirects to an NVIDIA synthetic-data page (observed October 2026). https://www.nvidia.com/en-us/use-cases/synthetic-data-generation-for-agentic-ai/

### Historic anchor facts (pre-2025, for the narrative)

- **MNIST** (LeCun, Cortes, Burges, 1998): 70,000 28×28 grayscale handwritten digits (60k train / 10k test).
- **ImageNet** (Fei-Fei Li et al., 2009): ~14 million images in ~22,000 categories, labeled via Amazon Mechanical Turk. The ILSVRC challenge subset had ~1.28M training images in 1,000 classes. In **2012, AlexNet** cut top-5 error to ~15.3% vs. ~26% for the runner-up, which launched the deep-learning era. https://image-net.org
- **Netflix Prize** (2006–2009): $1M for a 10% improvement over Netflix's recommender, about 100M ratings, won by "BellKor's Pragmatic Chaos." Researchers showed the "anonymized" data could be partly re-identified, and a planned sequel was cancelled after a privacy lawsuit.
- **Gender Shades** (Buolamwini & Gebru, 2018): commercial face-analysis systems had far higher error rates for darker-skinned women than lighter-skinned men. http://gendershades.org
- **Amazon recruiting model** (reported by Reuters, 2018): scrapped after it learned to downgrade résumés containing "women's."

---

## 5. Diagram ideas

1. **"Two ways to make a computer do something."** Two side-by-side flows. Left, "Traditional programming": [Rules (written by human)] + [Data] → [Computer] → [Answers]. Right, "Machine learning": [Data] + [Answers (examples)] → [Computer/training] → [Rules (the model)]. Use matching colors for "Rules" in both so the reader sees the swap.
2. **"A model is a box with knobs."** A box labeled "Model" with an input arrow ("house: 3 bedrooms, 1,800 sq ft, zip 30301") and an output arrow ("$412,000"). Several dials on the box face labeled w₁, w₂, w₃, b. Caption: "Training = turning the knobs. Inference = using the box."
3. **"Anatomy of a dataset."** A spreadsheet with 6 rows of houses. Header row; columns bracketed in blue as "Features" and the last column bracketed in orange as "Label." One row highlighted as "One example." A side callout: "Training set (rows 1–4) / Test set (rows 5–6)."
4. **"Training vs. inference timeline."** A horizontal timeline. Left segment, "Training: weeks–months, huge computers, data in, knobs adjusted" (with a loop arrow). A frozen-snowflake icon at "Model saved." Right segment, many small arrows: "Inference: milliseconds, millions of times, knobs fixed." Annotate "Your chat with Claude happens here."
5. **"The family tree of machine learning."** A tree: Machine Learning → Supervised (Regression, Classification), Unsupervised (Clustering, Dimensionality reduction, Anomaly detection), Semi-supervised, Self-supervised (→ "LLM pretraining: predict next word"), Reinforcement learning (→ "Games, robots, RLHF"). Each leaf has a one-line everyday example.
6. **"Regression vs. classification."** Two panels. Left: a scatter of hours studied vs. score, with a fitted line, labeled "predict a number." Right: a scatter of red and blue dots with a dividing line, labeled "predict a category."
7. **"Loss as distance."** Data points with a candidate line. Vertical dashed lines from each point to the line, labeled "error." A tally box: "square each, average them = MSE = 41.3." A second, better line beside it with shorter dashes and "MSE = 9.8."
8. **"Hiking down the loss mountain (gradient descent)."** A 3-D-looking valley surface with a hiker icon. Footprints show steps descending, each labeled with step number. Inset: three mini-paths: "learning rate too small" (tiny steps, still high), "just right" (reaches bottom), "too large" (zigzags across the valley). Mark a small side-dip as "local minimum."
9. **"Underfit / just right / overfit."** Three panels, the same noisy curved data. Panel 1: a straight line ("underfit, high bias"). Panel 2: a smooth curve ("good fit"). Panel 3: a wild squiggle through every point ("overfit, high variance"). Beneath each: training error and test error bars.
10. **"The training/validation curve."** X-axis: model complexity (or training epochs). Y-axis: error. The training-error line goes steadily down; the validation-error line goes down then up (U-shape). A vertical dashed line at the minimum labeled "sweet spot / stop here (early stopping)." Shade the left "underfitting" and right "overfitting" zones.
11. **"Bias–variance dartboard."** A 2×2 grid of dartboards: low bias/low variance (tight cluster on bullseye), low bias/high variance (scattered around bullseye), high bias/low variance (tight cluster off-center), high bias/high variance (scattered, off-center).
12. **"Data splits and k-fold cross-validation."** Top: one bar split 70/15/15 into Train / Validation / Test (test has a padlock icon). Bottom: 5 stacked bars each cut into 5 segments, with a different segment shaded "validation" in each row, arrows to "Score 1..5 → average."
13. **"The confusion matrix, illustrated."** A 2×2 grid for a COVID-test example. Rows are "Actually sick / Actually healthy"; columns are "Test says positive / Test says negative." Cells: TP (a sick person correctly flagged), FN ("missed! sent home sick"), FP ("false alarm"), TN. Side formulas with colored highlights showing which cells feed Precision, Recall and Accuracy.
14. **"Threshold slider and ROC curve."** Top: two overlapping bell curves (healthy vs. sick model scores) with a movable vertical threshold line; areas shaded as FP and FN. Bottom: the ROC curve with three dots marking "strict," "balanced" and "lenient" thresholds; the diagonal labeled "coin flip (AUC=0.5)"; the area under the curve shaded "AUC=0.91."
15. **"A decision tree for loan approval."** A flowchart: root "Income > $50k?" → yes: "Debt/Income < 0.4?" → yes: leaf "Approve (92%)" / no: leaf "Review." Root no: "Years employed > 3?" → leaves. Annotate depth, node and leaf.
16. **"From one tree to a forest to boosting."** Three rows. Row 1: one tree → one prediction. Row 2 (Random forest): five different trees in parallel → votes → majority. Row 3 (Boosting): tree 1 → "errors" → tree 2 focuses on red-highlighted mistakes → tree 3 → summed prediction. Arrows show parallel vs. sequential.
17. **"k-nearest neighbors and k-means side by side."** Left (kNN, supervised): colored dots plus a new gray "?" point with a circle around its 5 nearest neighbors (3 blue, 2 red) → "predict blue." Right (k-means, unsupervised): gray dots; three iterations showing centers (stars) moving and dots recoloring until stable.
18. **"PCA as finding the best camera angle."** A 3-D cloud of points shaped like a flattened football. Arrows show PC1 (the long axis) and PC2. A projection onto a 2-D sheet shows the cloud's shape preserved. Caption: "Keep the directions where the data spreads most."
19. **"Collaborative filtering matrix."** A user × movie grid with star ratings and "?" cells. Highlight two users with similar rows ("taste twins"), with an arrow filling a "?" for one from the other's rating. Below: the matrix factored into a tall "user tastes" matrix × a wide "movie traits" matrix (hidden factors labeled "action-ness," "romance-ness").
20. **"Time series decomposed."** Four stacked line charts sharing a time axis: Observed (messy) = Trend (smooth rise) + Seasonality (repeating wave) + Noise (jitter). Then a "walk-forward backtest" strip: train window → forecast window, sliding right in 4 steps.
21. **"The life of training data for a chatbot."** A left-to-right pipeline: [Public web (Common Crawl) | Books & papers | Code | Licensed news | Human-written expert data | Synthetic data] → [Crawl / acquire] → [Clean: dedupe, language ID, quality filter, remove PII/toxicity] → [Tokenize] → [Pretraining mix] → [Model]. A branch for post-training: [Human labelers: write answers, rank responses] + [RL environments / verifiers] → [Fine-tuned chatbot]. Shrinking funnel widths show how much is discarded (illustrative, not exact).
22. **"The labeling industry map."** Concentric rings or a 2×2. X-axis: "generalist crowd ↔ credentialed experts." Y-axis: "tooling/platform ↔ managed workforce." Place Mechanical Turk, Appen, Sama, Labelbox, Scale AI, Surge AI, Mercor, Handshake, micro1, Turing, Invisible. An arrow shows "where the money moved, 2023→2026: toward experts."
23. **"Data warehouse vs. data lake vs. lakehouse."** Three building icons. Lake: a big tank with mixed raw files (logs, images, CSVs). Warehouse: neat labeled shelves of tables. Lakehouse: a tank with a shelf structure on top. ETL/ELT arrows from sources (apps, sensors, sales) into each.
24. **"Sources of bias in the ML pipeline."** The pipeline World → Data collection → Labeling → Features → Model → Deployment → feedback arrow back to World. Red warning tags at each stage: "historical bias," "sampling bias," "label bias," "proxy variables," "evaluation bias," "feedback loops."
25. **"The data wall."** A line chart. X-axis: year (2020–2032). One rising curve, "tokens used to train largest models"; one flat band, "estimated stock of quality public human text (~300T tokens; range 100T–1,000T)"; the intersection shaded "2026–2032." Arrows leading off the wall: "synthetic data," "video/audio," "RL environments," "expert-written data," "private data," "better data efficiency." Label the source (Epoch AI 2024), keep it schematic, and caveat it as an estimate.

---

## 6. Practical exercises (easy → hard)

1. **Write rules for a cat (paper, 15 min).** Write as many if-then rules as you can for "Is this photo a cat?" Then have a friend (or a chatbot) find counter-examples: a hairless cat, a cat in a box, a cartoon cat, a tiger. *Learn:* why rules-based programming fails for perception tasks and why learning from examples is needed.
2. **Be the model: features and labels (paper or spreadsheet, 20 min).** List 10 fruits you know with 3 features each (color, size, smooth/bumpy) and the label (fruit name). Cover the label column and ask a friend to guess from the features. *Learn:* features vs. labels, and that bad features ("color" alone) make a problem impossible.
3. **Train an image classifier in your browser (Teachable Machine, 30 min).** Go to teachablemachine.withgoogle.com → Image Project. Make two classes ("thumbs up," "thumbs down"), record ~50 webcam images each, click Train, test live. Then deliberately record class 1 only in a bright room and class 2 only in a dark room, and test with the lights switched. *Learn:* training vs. inference, how much data matters, and how a model can learn the wrong shortcut (lighting instead of hands).
4. **Spot supervised vs. unsupervised vs. RL (chatbot quiz, 15 min).** Ask a chatbot: "Give me 15 real-world AI applications, one per line, without saying which type of learning they use." Label each yourself as supervised (regression/classification), unsupervised, or RL, then ask the chatbot to check you. *Learn:* the taxonomy, and to catch the chatbot when it's wrong.
5. **Human k-means with coins or sticky notes (tabletop, 20 min).** Scatter 20 coins on a table. Place 3 "center" markers randomly. Assign each coin to the nearest marker, move each marker to the middle of its group, and repeat until nothing changes. Try again with different starting spots. *Learn:* clustering, iteration, convergence, and sensitivity to initialization.
6. **Fit a line in a spreadsheet by hand (Google Sheets, 30 min).** Enter 10 rows of (hours studied, test score). Make a scatter chart. Create two cells, slope and intercept; add a column for predictions and one for squared error; sum the errors. Change slope and intercept by hand to make the sum smaller. Finally add the chart's built-in trendline and compare. *Learn:* parameters, loss, and that "training" is literally knob-turning to reduce error.
7. **Gradient descent by hand (spreadsheet, 30 min).** Use the same sheet: write a formula that nudges the slope by −(learning rate × the change in error when the slope increases by 0.01). Copy it down 30 rows to watch the slope converge. Try learning rates of 0.0001, 0.01 and 1. *Learn:* gradient descent, learning rate, divergence.
8. **Build a confusion matrix from a medical-test story (paper, 20 min).** Scenario: 1,000 people, 10 actually sick. The test catches 9 of them and wrongly flags 50 healthy people. Fill in TP/FP/FN/TN, then compute accuracy, precision, recall and F1. Then compute the accuracy of a "test" that always says healthy. *Learn:* why accuracy misleads with rare events and what precision and recall each mean.
9. **Threshold game (spreadsheet, 30 min).** Make a column of 20 "model scores" (0–1) with true labels. Add a threshold cell; use IF formulas to produce predictions and auto-count TP/FP/FN/TN. Slide the threshold from 0.1 to 0.9 and record precision and recall at each. Plot them. *Learn:* the precision–recall tradeoff and where ROC curves come from.
10. **Overfitting with polynomial trendlines (Google Sheets, 20 min).** Using noisy data (10 points), add a polynomial trendline and increase the degree from 1 to 6. Hide 3 points first and see how badly the high-degree curve predicts them. *Learn:* overfitting, underfitting, and why we hold out test data.
11. **Decision tree on paper: the "play tennis" table (paper, 30 min).** Using a 14-row weather table (Outlook, Temperature, Humidity, Wind → Play?), which a chatbot can generate, try each feature as the first question and count how "pure" the resulting groups are. Build a 2-level tree and use it to classify new days. *Learn:* how trees choose splits; interpretability.
12. **Data detective: clean a messy dataset (spreadsheet + chatbot, 45 min).** Ask a chatbot to "generate a 40-row CSV of customer records with realistic errors: duplicates, missing values, inconsistent state names, impossible ages, mixed date formats, and one outlier." Paste it into Sheets and find and fix every problem, logging each fix. Ask the chatbot to reveal the planted errors and score yourself. *Learn:* data cleaning, data quality dimensions, and how much time this takes.
13. **Bias audit of a toy hiring dataset (spreadsheet, 45 min).** Ask a chatbot for a 100-row fictional past-hiring dataset where historical decisions favored one group. Compute hire rates by group with a pivot table. Discuss: if a model learns from this, what will it do? Identify a "proxy" column (such as a hobby or zip code) that correlates with group. *Learn:* historical bias, proxies, and why "just remove the gender column" isn't enough.
14. **Explore a famous dataset on Kaggle without coding (web, 30 min).** Create a free Kaggle account, open the Titanic dataset, read its data card, and use the column-preview charts to answer: Who survived more, by sex, by class, by age? Then browse 3 public notebooks and read just their text cells. *Learn:* EDA, how real datasets are documented, and the Kaggle ecosystem.
15. **Investigate a web-scale dataset (Hugging Face, 30 min).** On huggingface.co/datasets open FineWeb (HuggingFaceFW/fineweb) and use the dataset viewer to read 20 random rows. Note the quality: ads, spam, boilerplate, non-English text. Then read the dataset card sections on filtering and PII. Compare with a FineWeb-Edu sample. *Learn:* what pretraining data really looks like and why filtering matters.
16. **Check robots.txt and AI crawlers (web, 15 min).** Visit nytimes.com/robots.txt, reddit.com/robots.txt, and a small blog's robots.txt. Find the entries for GPTBot, ClaudeBot, Google-Extended, CCBot. Ask a chatbot what each user-agent belongs to. *Learn:* how sites signal consent, and that robots.txt is a request, not a lock.
17. **Ask SQL questions of a real table (Google BigQuery sandbox or an online SQL playground, 45 min).** Ask a chatbot to explain and write queries, then run them on a public dataset (for example, a public baby-names table): SELECT, WHERE, GROUP BY, ORDER BY, and one JOIN. *Learn:* the four everyday SQL moves and that databases are just organized tables.
18. **Your first scikit-learn model in Colab (copy-paste code, 45 min).** Open colab.research.google.com. Ask a chatbot: "Write a beginner Google Colab notebook that loads the scikit-learn Iris dataset, splits it 80/20, trains a decision tree, prints accuracy and a confusion matrix, and plots the tree. Comment every line for a non-programmer." Run each cell; change `max_depth` from 1 to 10 and record test accuracy. *Learn:* the full train/test workflow in code; hyperparameters; overfitting.
19. **Algorithm bake-off (Colab, 60 min).** Extend Exercise 18: on the scikit-learn breast-cancer dataset, compare logistic regression, kNN, random forest and gradient boosting using 5-fold cross-validation, and report accuracy, precision, recall and ROC-AUC in a table. Ask the chatbot to also add a "dumb baseline" (always predict the majority class). *Learn:* cross-validation, baselines, metric choice, and that the fancy model isn't always best.
20. **Unsupervised exploration: cluster and map (Colab, 60 min).** Using the scikit-learn handwritten-digits dataset (8×8 images), run PCA to 2-D and plot it colored by true digit; then run k-means with k=10 *without* labels and compare clusters to true digits. *Learn:* dimensionality reduction, clustering, and how much structure exists without labels.
21. **Forecast something you care about (Colab or Sheets, 60–90 min).** Download a time series (for example Google Trends for a search term, or your city's daily temperatures). Build: (a) a naive forecast, (b) a seasonal naive forecast, (c) a moving average, (d) with chatbot help, an exponential smoothing or gradient-boosting model with lag features. Backtest each on the last 8 weeks and compare MAE. *Learn:* time-series concepts, backtesting, baselines that are hard to beat.
22. **Mini movie recommender (Colab, 90 min).** Ask a chatbot for code using the public MovieLens 100K dataset to build (a) a "most popular" recommender, (b) item-based collaborative filtering with cosine similarity, and (c) a check of what it recommends for a new user with 3 ratings you enter. *Learn:* collaborative filtering, similarity, cold start.
23. **Leakage trap (Colab, 60 min).** Ask a chatbot to create a synthetic loan dataset including a column "collections_agency_contacted" that is only set *after* default. Train with and without that column and compare the suspiciously high accuracy. Then write one paragraph explaining why the first model would fail in real life. *Learn:* data leakage and skepticism about too-good results.
24. **Synthetic data experiment (chatbot + Colab, 90 min).** Ask a chatbot to generate 200 labeled synthetic product reviews (positive/negative). Train a simple TF-IDF + logistic regression classifier on them, then test on 50 real reviews you copy from a site (or a public sentiment dataset). Compare with training on 200 real reviews. *Learn:* the promise and limits of synthetic data (distribution mismatch, too-clean language).
25. **Datasheet for a dataset (writing, 60 min).** Pick any dataset from Exercises 14–22 and write a one-page datasheet: who made it, why, how it was collected and labeled, what's missing, who might be harmed, license, recommended and non-recommended uses. Compare against the real data card. *Learn:* data documentation, licensing, ethics. It is a good capstone.

---

## 7. Areas of opportunity

**Careers and roles**

- **Data analyst → data scientist → ML engineer ladder.** SQL, spreadsheets, Python/pandas and clear communication remain the entry point. AI coding assistants lower the programming barrier but raise expectations for problem framing, judgment and validation.
- **AI trainer / expert data contributor.** This is the fastest-growing new on-ramp for domain experts: doctors, lawyers, accountants, engineers, scientists, coders and writers grading model outputs, writing hard problems and building evaluation rubrics for labs via Mercor, Surge, Scale, Handshake, micro1, Turing and others. Pros: flexible, well paid for scarce expertise. Cons: gig instability, project volatility, confidentiality burdens, and data-security risk (see the Mercor breach).
- **Data engineer / analytics engineer.** Builds pipelines, warehouses and data quality checks. Consistently in demand because every AI system depends on reliable data plumbing.
- **Data labeling operations / quality lead.** Designs annotation guidelines, measures inter-annotator agreement, audits vendors.
- **RL environment builder.** Creates simulated tasks, verifiers and graders for agent training. This is an emerging 2025–26 niche where software engineering meets ML.
- **Data governance, privacy and AI compliance.** EU AI Act training-data summaries, California AB 2013 disclosures, copyright policies, data provenance audits, licensing negotiation.
- **Data licensing / partnerships.** Publishers, archives and platforms need people who can price, package and negotiate data deals; AI firms need people who can source them.
- **Forecasting and decision science in business.** Demand planning, pricing, churn, fraud. Classical ML still delivers most enterprise value here.

**Businesses**

- **Niche, rights-cleared datasets**: specialized licensed corpora (medical, legal, industrial, regional languages, audio/video with consent) sold to model builders.
- **Expert data marketplaces** for underserved domains or languages.
- **Synthetic data services** for regulated industries (healthcare, finance), rare-event simulation, and testing.
- **Data-quality, deduplication and provenance tooling**, including content credentials and opt-out registries.
- **Vertical ML products for SMBs**: forecasting for restaurants and retailers, churn prediction for subscription businesses, anomaly detection for small manufacturers. Classical ML plus a good UI is often enough.
- **Training and education** for non-programmers using no-code ML and AI-assisted analysis.
- **Monetized crawling/licensing infrastructure**: pay-per-crawl, licensing standards (RSL), attribution and payment rails.

**Skills in demand**

- SQL; spreadsheets at an advanced level; Python + pandas + scikit-learn; data visualization; experimental design and A/B testing; statistics literacy (distributions, sampling, uncertainty); evaluation design (metrics, rubrics, test sets); domain expertise combined with data literacy; prompting LLMs to do data work *and* verifying the results; privacy and compliance basics.

**Open problems (good "frontier" sidebars)**

- How to keep scaling when high-quality human data runs short (the data wall). How much synthetic data helps, and when it causes collapse.
- Measuring data quality: which data actually makes models better ("data attribution," data valuation).
- Fair compensation and consent for creators whose work trains models. Collective licensing models; how the courts will settle generative-AI fair use.
- Evaluation that doesn't get "gamed" (benchmark contamination, Goodhart's law).
- Robustness to distribution shift and drift.
- Fairness definitions that conflict mathematically; auditing models without access to sensitive attributes.
- Privacy: memorization, machine "unlearning" (removing a person's data from a trained model).
- Tabular and time-series foundation models: will pretrained models replace hand-tuned XGBoost for business data?
- Labor conditions and pay transparency in the global annotation workforce.

---

## 8. Common misconceptions to correct

1. **"AI and machine learning are the same thing."** ML is one approach to AI (now the dominant one). Rules-based AI, search and planning also exist.
2. **"The model looks up answers in a database of its training data."** A model stores learned parameters, not a copy of its training set. It can sometimes memorize fragments, which is a known problem, but prediction is computation, not retrieval (unless retrieval is deliberately added, as in RAG).
3. **"The chatbot is learning from my conversation right now."** During inference the weights are frozen. Some products store conversations and may use them in *future* training (depending on settings and policy) or keep "memories" in a separate store, but the model doesn't update mid-chat.
4. **"More data always helps."** More *relevant, clean, representative* data helps. Duplicated, mislabeled, biased or off-distribution data can hurt.
5. **"99% accuracy means the model is great."** Not with rare events: a fraud detector that never flags anything can be 99.9% accurate. Look at precision, recall and the confusion matrix.
6. **"A more complex model is always better."** Complexity invites overfitting; simple baselines often win on small or tabular data; interpretability matters in regulated areas.
7. **"Deep learning made classical ML obsolete."** For spreadsheets and business tables, boosted trees and logistic regression remain workhorses, and are cheaper, faster and more explainable. (The 2025–26 twist is tabular foundation models, which are themselves pretrained neural networks.)
8. **"Algorithms are objective because they're math."** Models learn whatever patterns, including unfair ones, exist in their data and labels. Choices of data, labels and metrics are human choices.
9. **"Removing race/gender columns makes a model fair."** Proxies (zip code, name, school, hobbies) can reconstruct sensitive attributes.
10. **"Anonymized data is safe."** Many "anonymous" datasets have been re-identified by linking them with other data (Netflix Prize, AOL search logs).
11. **"If it's on the public internet, it's free to use for anything."** Public does not mean public domain. Copyright, terms of service, privacy law and contracts still apply, and courts are actively deciding the training question.
12. **"Courts have decided that AI training is legal (or illegal)."** As of October 2026 it is mixed and unsettled. Two US district judges found training fair use on their records (with pirated acquisition treated differently); the only appellate ruling (Thomson Reuters v. Ross, 3rd Cir., September 2026) found *non-generative* training on a competitor's content not fair use; and generative-AI appeals are still pending.
13. **"Synthetic data is fake, so it's useless" / "Synthetic data solves the data problem."** Both are wrong. It works well where outputs can be verified (math, code) or simulated (driving scenes), and is risky where it drifts from reality or recycles a model's own errors.
14. **"Labeling is low-skill busywork that AI has already automated."** Simple labeling is increasingly automated, but frontier labs now pay large sums for expert human judgment. Labeling became *more* specialized, not extinct.
15. **"Training and testing on the same data is fine if you're careful."** A test set the model has seen is no longer a test. Leakage is one of the most common causes of inflated results.
16. **"Correlation the model finds = cause."** Predictive models exploit correlations; they don't establish causation (ice-cream sales predict drownings because both rise in summer).
17. **"The model is 80% confident, so there's an 80% chance it's right."** Only if the model is calibrated. Many models, including chatbots, are overconfident.
18. **"Unsupervised means the computer figures out meaning by itself."** It finds structure (groups, directions of variation); humans still interpret what clusters mean, and clusters can be arbitrary.
19. **"Data scientists spend their time building fancy models."** Most of the work is framing questions, finding, cleaning and understanding data, and communicating results. (Present the oft-quoted "80%" as folklore, not a measured statistic.)
20. **"We're about to literally run out of data and AI will stop."** The data wall is an estimate with wide uncertainty and many workarounds (synthetic data, RL environments, multimodal data, efficiency). It's a real pressure, not a cliff date.
21. **"Bias in ML only means unfairness."** "Bias" has three meanings in this chapter: the intercept parameter, statistical bias (in bias–variance), and social or unfair bias. Teach all three explicitly.

---

## 9. Analogies that work well for beginners

- **Traditional programming vs. ML: a recipe vs. a taste-testing apprentice.** A recipe tells you every step; an apprentice cook tastes thousands of dishes with feedback ("too salty") and develops a feel for it.
- **Model as a sound mixing board.** Hundreds of sliders (parameters); training slowly adjusts every slider until the music (predictions) sounds right; inference is just playing the song with the sliders locked.
- **Training vs. inference: studying vs. taking the exam.** Studying is slow, effortful and done in advance; answering a question on exam day is quick and uses what you already learned. You don't learn new material mid-exam.
- **Generalization and overfitting: memorizing the answer key vs. understanding the subject.** The student who memorized last year's test fails when the questions change.
- **Underfitting: a weather forecaster who always predicts "mild."** Too simple to capture reality.
- **Features and labels: a doctor's chart.** Symptoms and measurements (features) are written at the top; the diagnosis (label) is at the bottom.
- **Supervised learning: flashcards with answers on the back.** **Unsupervised: sorting a box of mixed buttons into piles without being told the categories.** **Reinforcement learning: training a dog with treats** (or learning a video game by dying a lot).
- **Self-supervised learning: a fill-in-the-blank workbook the internet writes for free.** Hide a word, guess it, check, repeat billions of times.
- **Loss function: a golf score.** Lower is better; it adds up how far off every shot was.
- **Gradient descent: walking downhill blindfolded in fog.** Feel the slope under your feet, take a small step downhill, repeat. Learning rate is your stride length: too long and you stumble over the valley, too short and you never arrive.
- **Bias vs. variance: the dartboard.** Consistently off-target (bias) vs. scattered all over (variance).
- **Regularization: a word limit on an essay.** It forces you to keep only what matters instead of padding with noise.
- **Validation vs. test set: practice quizzes vs. the sealed final exam.** Use practice quizzes as often as you like to adjust your study; open the final once.
- **Cross-validation: rotating which friend is the taste-tester** so one person's quirky palate doesn't decide the recipe.
- **Precision vs. recall: a fishing net.** A fine, wide net catches every fish (high recall) but also boots and seaweed (low precision); a small net with a picky fisher keeps only fish (high precision) but misses many (low recall).
- **Smoke alarm for thresholds.** Set it too sensitive and it shrieks at toast (false positives); too lax and it misses a real fire (false negatives).
- **kNN: "tell me who your friends are and I'll tell you who you are."** Or: guessing a house's price from the five most similar houses on the block (it's how real-estate "comps" work).
- **Decision tree: the game Twenty Questions.** **Random forest: asking a crowd of people who each saw part of the evidence and taking a vote.** **Boosting: a relay of tutors, each focusing on the questions the previous tutor's student got wrong.**
- **Naive Bayes: a detective adding up clues** ("mentions lottery: more suspicious; from a known contact: less suspicious"), assuming each clue is independent.
- **SVM: drawing the widest possible road between two neighborhoods** so no house is too close to the border.
- **k-means: placing a few ice-cream trucks in a park** and repeatedly moving each truck to the center of the people who walk to it.
- **PCA: finding the best camera angle** to photograph a 3-D sculpture so the 2-D photo shows as much as possible. Or: summarizing a 20-question personality survey into 2 scores.
- **Anomaly detection: a bank's "this doesn't look like you" text** when your card is used abroad at 3 a.m.
- **Collaborative filtering: the friend with eerily similar taste** whose recommendations you trust. **Cold start: a new restaurant with no reviews.**
- **Time series: a heartbeat on a monitor**: trend (slowly rising), seasonality (the regular beat), noise (jitter).
- **Data as ingredients; the model as the dish.** Even a great chef can't make a good meal from spoiled ingredients ("garbage in, garbage out").
- **Data cleaning: washing and chopping vegetables.** It takes most of the kitchen time, nobody sees it, and it matters most.
- **Feature engineering: a chef prepping ingredients so they cook evenly**: turning a birthdate into "age," a timestamp into "weekend vs. weekday."
- **Database: a library catalog. SQL: asking the librarian precise questions.** **Warehouse: a tidy, labeled library. Lake: a huge storage room of unsorted boxes. Pipeline: the conveyor belt between them.**
- **Data leakage: seeing the answer key slip under the exam paper.** A great score that means nothing.
- **Biased data: learning about the world only from one neighborhood's newspapers.** **Feedback loop: a store that only stocks what sold last week, so nothing new ever gets a chance.**
- **Differential privacy: answering a survey after secretly flipping a coin**, so any one answer is deniable but the overall statistics stay accurate.
- **Synthetic data: flight simulators.** Pilots learn a lot from simulators, but a simulator can't teach what its designers didn't model, and nobody wants a pilot trained *only* in one.
- **Model collapse: photocopying a photocopy.** Each generation loses detail.
- **Data wall: fossil fuel.** (Sutskever's framing.) There's only one internet, we've drilled most of the easy reserves, and now the race is to find new sources and use what we have more efficiently.
- **Labeling industry: the "invisible kitchen staff" of AI.** Diners (users) see the plated dish (the chatbot), not the many people who prepped it, from crowdworkers tagging images to PhDs writing exam-grade problems.
