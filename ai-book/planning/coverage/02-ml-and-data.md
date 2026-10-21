# Coverage report: 02-ml-and-data.md (topic map, section 1)

Audited October 21, 2026 against `ai-book/chapters/`. Each of the 64 items was located by searching for its key terms and every named sub-item, then reading the passage. "COVERED" means explained at beginner level, not just mentioned.

| Item | Status before | Where covered (chapter and section) | Action taken |
|---|---|---|---|
| A1. Programs as recipes (rules-based programming) | COVERED | Ch 8 "Two ways to make a computer do something" (thermostat, recipe, rules-based system); Ch 1 "Way 1: Rules" | None |
| A2. Where rules break | COVERED | Ch 8 same section (writing "is this a cat?" rules, messy handwriting, voice, sarcastic review) | None |
| A3. Learning from examples | COVERED | Ch 8 same section (labeled examples, child learning "dog", Figure 8.1, Samuel and Mitchell) | None |
| A4. What a model is (file of numbers plus recipe, not a database or a mind) | COVERED | Ch 8 "What a model really is" (box with knobs, Figure 8.2, "not a database") | None |
| A5. Parameters and weights, with scale | COVERED | Ch 8 same section (weight and bias definitions, Table 8.1 "From 2 knobs to trillions") | None |
| A6. Hyperparameters | COVERED | Ch 8 "Hyperparameters: the settings about learning" (Table 8.2) | None |
| A7. Features and labels | COVERED | Ch 8 "Features, labels and the anatomy of a dataset" (house-price table, doctor's-chart analogy) | None |
| A8. Training vs inference (chatting is inference; the model is not learning from you) | COVERED | Ch 8 "Training versus inference" | None |
| A9. Generalization | COVERED | Ch 8 "Generalization: the whole point"; Ch 9 throughout | None |
| B10. Supervised learning (regression, classification) | COVERED | Ch 8 "Supervised learning: flashcards with answers on the back" | None |
| B11. Unsupervised learning (clustering, dimensionality reduction, anomaly detection) | COVERED | Ch 8 "Unsupervised learning: sorting a box of buttons"; algorithms in Ch 10 | None |
| B12. Semi-supervised learning and pseudo-labeling | COVERED | Ch 8 "Semi-supervised learning: a few labels go a long way" (X-ray pseudo-labeling worked) | None |
| B13. Self-supervised learning, the bridge to chatbots | COVERED | Ch 8 "Self-supervised learning: the bridge to your chatbot" (Figure 8.5, next token, hidden image patches and audio slices) | None |
| B14. Reinforcement learning overview (AlphaGo, robots, RLHF, verifiable rewards) | COVERED | Ch 8 "Reinforcement learning: learning from rewards" | None |
| B15. Other setups (transfer, fine-tuning, few-shot, active, online) | COVERED | Ch 8 "Other ways to learn" (definitions, in-context learning, Table 8.5) | None |
| C16. Loss functions (MSE, log loss / cross-entropy) | COVERED | Ch 8 "Measuring wrongness: the loss function"; "Cross-entropy: the loss for categories" | None |
| C17. Gradient descent intuition (learning rate, epoch, batch, SGD, local minima) | COVERED | Ch 8 "Walking downhill in fog: gradient descent"; "Batches, epochs and noisy steps" | None |
| C18. Linear regression worked example | COVERED | Ch 8 "Worked example: fitting a line in a spreadsheet" (study hours vs score) | None |
| C19. Logistic regression and decision boundaries | COVERED | Ch 8 "Predicting categories: logistic regression"; "Decision boundaries" | None |
| C20. Probabilities, confidence and calibration | COVERED | Ch 8 "Calibration: what '80% sure' should mean" | None |
| D21. Train / validation / test split | COVERED | Ch 9 "Splitting the data: train, validation and test" (70/15/15, "Keeping the mix fair") | None |
| D22. Data leakage | COVERED | Ch 9 "Data leakage: how models cheat by accident" (treatment column, shortcut learning) | None |
| D23. Overfitting and underfitting | COVERED | Ch 9 "Overfitting and underfitting" (iced-drinks worked example) | None |
| D24. Bias–variance tradeoff, double descent teaser | COVERED | Ch 9 "Bias and variance: the dartboard"; "A twist: double descent" | None |
| D25. Regularization | COVERED | Ch 9 "Regularization: keeping models simple on purpose" (L1/L2 worked, early stopping, dropout, augmentation, more data, Occam's razor) | None |
| D26. Cross-validation (k-fold, stratified, walk-forward) | COVERED | Ch 9 "Cross-validation: don't trust one lucky split"; "Time series: never train on the future" | None |
| D27. Classification metrics and the confusion matrix | COVERED | Ch 9 "The confusion matrix" (worked medical test, "Precision or recall: which matters more?" incl. airport bag scans, 99.9% fraud trap) | None |
| D28. Thresholds, ROC, AUC, precision–recall curves | COVERED | Ch 9 "Thresholds, ROC curves and AUC" | None |
| D29. Regression metrics (MSE, RMSE, MAE, R², MAPE) | COVERED | Ch 9 "Measuring models that predict numbers" | None |
| D30. Baselines and hyperparameter tuning (grid, random, Bayesian optimization) | COVERED | Ch 9 "Baselines: is it better than doing something dumb?"; "Tuning hyperparameters without cheating" | None |
| D31. Benchmarks and Goodhart's law | COVERED | Ch 9 "Benchmarks and Goodhart's law" and "Benchmarks in the chatbot era" (pointers to Ch 24 and Ch 57) | None |
| E32. k-nearest neighbors | COVERED | Ch 10 "k-nearest neighbors: you are like your neighbors" | None |
| E33. Linear and logistic regression revisited | COVERED | Ch 10 "Linear and logistic regression, revisited" | None |
| E34. Naive Bayes | COVERED | Ch 10 "Naive Bayes: adding up the clues" | None |
| E35. Decision trees (impurity, information gain) | COVERED | Ch 10 "Decision trees: Twenty Questions learned from data" | None |
| E36. Random forests (bagging) | COVERED | Ch 10 "Random forests: a crowd of trees" (crowd arithmetic, bootstrap rows, random features) | None |
| E37. Gradient boosting and tabular foundation models | COVERED | Ch 10 "Gradient boosting: a relay of tutors"; "The 2025–26 twist: foundation models for spreadsheets" (TabPFN) | None |
| E38. Support vector machines and the kernel trick | COVERED | Ch 10 "Support vector machines: the widest street" | None |
| E39. k-means and other clustering (elbow, hierarchical, DBSCAN) | COVERED | Ch 10 "Clustering: finding groups without answers" (k-means by hand) | None |
| E40. Dimensionality reduction (PCA, t-SNE, UMAP) | COVERED | Ch 10 "Shrinking many columns into a few: PCA, t-SNE and UMAP" (camera-angle analogy, bridge to embeddings) | None |
| E41. Anomaly detection (z-scores, isolation forests) | COVERED | Ch 10 "Anomaly detection: spotting the odd one out" | None |
| E42. Recommender systems and the Netflix Prize | COVERED | Ch 10 "Recommenders and the Netflix Prize" (content-based, collaborative, matrix factorization worked, cold start, implicit signals); explicit vs implicit feedback and filter bubbles in Ch 51 | None |
| E43. Time-series forecasting | COVERED | Ch 10 "Forecasting time series" (trend, seasonality, naive and moving-average baselines, exponential smoothing, ARIMA, Prophet, lags, backtesting, Chronos-2, TimesFM 2.5) | None |
| E44. The bridge to neural networks (perceptron) | COVERED | Ch 10 "The perceptron: the bridge to neural networks" | None |
| E45. Choosing an algorithm | COVERED | Ch 10 "Choosing an algorithm: a cheat sheet" (decision flowchart, "start simple") | None |
| F46. What data is (structured, semi-structured, unstructured; types; formats) | COVERED | Ch 11 "What data is" (Figure 11.1, CSV/JSON/Parquet, MNIST as numbers) | None |
| F47. Where data comes from (data exhaust) | COVERED | Ch 11 "Where data comes from" | None |
| F48. Famous datasets as a history of AI | COVERED | Ch 11 "A history of AI told through datasets" (Iris to Common Pile, timeline and scale chart) | None |
| F49. Data collection and web scraping (robots.txt, ToS, paywalls, Pay Per Crawl, RSL) | COVERED | Ch 11 "Collecting data from the web" | None |
| F50. Labeling and annotation (task types, quality control, industry, human side) | COVERED | Ch 11 "Labeling: teaching by example" (Cohen's kappa worked) and "The labeling industry" | None |
| F51. Data cleaning (incl. web-scale cleaning, "garbage in", the 80% folk saying) | COVERED | Ch 11 "Cleaning data"; the 80% saying framed as folklore in Ch 10 "The machine-learning project lifecycle" | None |
| F52. Feature engineering (one-hot, scaling, dates, ratios, TF-IDF, binning, feature selection) | THIN | Ch 11 "Feature engineering" covered all moves except binning and feature selection, which appeared nowhere in the book in this sense (L1 removing features was mentioned only in passing in Ch 9) | Added two paragraphs to Ch 11 "Feature engineering": bucketing/binning with a worked driver-age example and its trade-offs, and feature selection (duplicates, empty and noisy columns, feature importance, L1, select on training data only); definitions "Bucketing (binning)" and "Feature selection" (named to avoid clashing with chip "Binning" in Ch 36) and key terms |
| F53. Databases and SQL basics (four moves; relational vs NoSQL vs vector) | COVERED | Ch 11 "Databases and SQL: the four everyday moves" | None |
| F54. Pipelines, warehouses, lakes, lakehouses (ETL/ELT, batch vs streaming, scheduled jobs and orchestration) | THIN | Ch 11 "Pipelines, warehouses, lakes and lakehouses" defined ETL/ELT and the storage types, but batch vs streaming got one clause and orchestration was absent | Added two paragraphs after the ETL/ELT definition: when to use batch vs streaming (nightly sales totals vs card-fraud checks) and orchestration of dependent steps (failure at 3 a.m., retries, alerts, the chatbot-data chain); definitions "Batch and streaming processing" and "Orchestration" and key terms |
| F55. Data quality and documentation | COVERED | Ch 11 "Data quality and documentation" (six dimensions table, lineage, versioning, datasheets, data and model cards) | None |
| F56. Bias in data | COVERED | Ch 11 "Bias in data" (bias types, worked hiring example, Amazon, COMPAS, Gender Shades, conflicting fairness definitions); depth in Ch 58 | None |
| F57. Privacy | COVERED | Ch 11 "Privacy" (re-identification incl. Netflix and AOL, GDPR/CCPA, minimization, differential privacy worked with a coin, federated learning, memorization) | None |
| F58. Synthetic data and model collapse | COVERED | Ch 11 "Synthetic data and model collapse" | None |
| F59. Data licensing, copyright and lawsuits | COVERED | Ch 11 "Who owns the data? Copyright, licensing and lawsuits in brief" (cases table, deals, open questions); depth in Ch 58–59 | None |
| F60. The data-wall debate | COVERED | Ch 11 "The data wall: are we running out?" (Epoch estimate, both sides, escape routes, Figure 11.10); also Ch 19 | None |
| G61. The project lifecycle | COVERED | Ch 10 "The machine-learning project lifecycle" (Figure 10.11, churn walk-through, EDA) | None |
| G62. The toolbox | COVERED | Ch 10 "The toolbox" (tool table incl. Kaggle, Hugging Face, AutoML and no-code tools; scikit-learn code); matplotlib introduced in Ch 3 and used in the Colab exercises | None |
| G63. MLOps basics (drift, retraining, experiment tracking, reproducibility) | COVERED | Ch 10 "MLOps: keeping a model alive" (data vs concept drift, 2020 example, Figure 10.12, experiment tracking and fixed seeds) | None |
| G64. Classical ML in the LLM era | COVERED | Ch 10 "Classical machine learning in the age of LLMs" (LLMs as labelers, feature makers, coders, analysts; cost worked example; agents doing data science) | None |

**Summary.** Of the 64 topic-map items, 62 were already COVERED, 2 were THIN and none were MISSING. Part II (Chapters 8–11) maps onto this research file section by section, with worked numbers and definitions for nearly every sub-item; recommender side effects (explicit vs implicit feedback, filter bubbles) are taught in Chapter 51 as the outline intends. The two gaps were both in Chapter 11: feature engineering lacked binning and feature selection, and the pipelines section mentioned batch vs streaming only in passing and never explained orchestration. Each gap was filled with short, worked, plain-English paragraphs inserted where they fit the chapter's flow, four new definition callouts in the exact STYLE.md format, and matching additions to the Key terms list. Chapter 11 passes validate.py (all diagrams valid) and check.py.
