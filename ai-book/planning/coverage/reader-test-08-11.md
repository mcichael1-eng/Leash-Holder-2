# Reader test: chapters 8 to 11

Tested by reading chapters 8, 9, 10 and 11 in order, in full, as the intended reader: no programming, school arithmetic only, a daily chatbot user who has read chapters 1 to 7. Before treating a term as undefined I checked GLOSSARY.md and the earlier chapters. Every entry for these chapters in `acronyms-by-chapter.json` was worked through. Organizations used in three or more chapters (IBM, NVIDIA, ACM) got a definition callout, which was also added to Key terms. Other names got a plain gloss at first use. NY and SELECT/WHERE/BY needed nothing: NY is already explained in context, and the SQL words are defined in the chapter.

Every worked number and every printed code result in the four chapters was recomputed in Python (numpy 2.5, scikit-learn 1.9, pandas 3.0). All of them reproduce. That covers:

- Tables 8.6 and 8.8, Cell 1 and Cell 2 of Chapter 8, and Exercise 6's row-1001 values
- Table 9.2, the Wisconsin cancer confusion matrices, AUC and fold scores, the ten-seed range, and the Exercise 8 leakage numbers
- the kNN, logistic, Gini, naive Bayes, crowd-vote, GMM and PSI arithmetic in Chapter 10, plus its Exercises 6, 8 and 9
- the Common Crawl rate, the SQL answers, kappa and the model-collapse output in Chapter 11

No arithmetic errors were found. Every edited file passed `validate.py` (8/8, 8/8, 10/10 and 7/7 diagrams) and `check.py` (all four chapters `[OK]`).

## Findings and fixes

| Chapter | Where | Problem a beginner would hit | Fix applied |
|---|---|---|---|
| 8 | "Two ways to make a computer do something", Arthur Samuel | IBM is used in 8 chapters and is never defined | New definition callout: IBM (International Business Machines), added to Key terms |
| 8 | Logistic regression, threshold 0.8 | "Above about 5.4 hours" came out of nowhere | Pointed to Table 8.9: the probability passes 0.8 between 5 hours (0.73) and 6 hours (0.88) |
| 8 | Decision boundaries, spam example | The step from z = 0 to "links + exclamation marks = 8" was skipped | Added "because 0.5 × 8 = 4, which cancels the −4" |
| 8 | Cross-entropy | "The logarithm" was ambiguous: a calculator's log key gives different numbers from Table 8.10 | Said it is the natural log (the ln key), with `=-LN(0.9)` giving 0.11 |
| 8 | Areas of opportunity | "pandas" is not defined until Chapter 10 | Glossed as a Python library for working with tables, with a pointer to Chapter 10 |
| 8 | Exercise 8, step 4 | The question "where does the boundary move?" does not match its example: the boundary only goes from 4.47 to 4.49 | Said the boundary barely moves but the weight rises from 0.9 to 1.2, and added a second list that moves it to about 6.5 hours (both checked in scikit-learn) |
| 8 | Exercise 9, step 4 | `=AVERAGEIFS` was given with no arguments or column layout | Gave the column layout and all three bucket formulas, and explained #DIV/0! |
| 9 | Significance test paragraph | Two margins of 1.5 points need a 2-point gap, not 3, and the text did not say why | Added a bridge: the margins combine to about 1.4 times one margin |
| 9 | Duplicate leakage | "CIFAR" was unexplained | Glossed: two sets of 60,000 tiny photos, named after the Canadian Institute for Advanced Research |
| 9 | Shortcut learning | "COVID-19 X-ray models" had no context | Glossed the 2020 pandemic and what the models looked for |
| 9 | L1 and L2 definition | "Sum of absolute weights" assumes the reader knows absolute value | Added "each weight with its minus sign dropped, so −3 counts as 3" |
| 9 | Regression metrics, Watch out | "RSQ function" was unexplained | Glossed as short for "R squared" |
| 9 | Benchmarks section | "Top-5 error rate" is not defined until Chapter 14 | Glossed inline |
| 9 | Benchmarks in the chatbot era | "ARC-AGI-3" and "ARC Prize" are not defined until Chapter 24 | Glossed both: what the puzzles test, and the foundation that runs them |
| 9 | Exercise 3, steps 3, 4 and 7 | `=TP/(TP+FP)` and `=1*FN+10*FP` are placeholders a beginner would type literally | Put the counts in E2:E5 and gave real cell formulas for precision, recall, false positive rate and both cost rules |
| 9 | Exercise 5, step 3 | "Compute the same five metrics" for column C did not say the formulas must change | Said to change B2:B6 to C2:C6, and gave the expected MAE (100) and R² (0) |
| 9 | Exercise 7, step 3 | Asked for an expected margin of error with no pointer to how | Pointed to the rule of thumb, with the accuracy and test size to use |
| 9 | Exercise 9, step 3 | `p` in `=1.96*SQRT(p*(1-p)/30)` would be typed literally | Gave the cell layout and real formulas |
| 9 | Exercise 10, step 2 | "Model card" is not defined until Chapter 24 | Glossed inline |
| 10 | Figure 10.2 (timeline) | "CART" is unexplained | Expanded in the caption |
| 10 | Logistic regression revisited | "Rearranges to months = 9 − 1.2 × hours" skipped the algebra | Added the doubling step |
| 10 | Random forests, arithmetic of crowds | The 10 and the 5 in front of 0.7³ × 0.3² were unexplained | Explained them as the number of ways to pick which trees are right |
| 10 | Feature importance, explaining one prediction | SHAP was not expanded; "Shapley values" and "model-agnostic" were unexplained | Expanded SHAP, glossed Shapley values as fair sharing of a team's winnings, and glossed model-agnostic |
| 10 | Gradient boosting libraries | Yandex is unknown to most readers | Glossed as Russia's largest search-engine company |
| 10 | Tabular foundation models | SAP was unexplained | Glossed as the German business-software maker |
| 10 | Kernel trick | Why ±1.58 was not shown | Added "the two numbers whose square is 2.5" |
| 10 | Gaussian processes | "Grows with the cube" was not made concrete | Added "double the examples, eight times the work" |
| 10 | Gaussian mixture model | The bell-curve formula e^(−d² ÷ (2 × spread²)) appeared unexplained | Added one clause giving the formula and pointing to Chapter 6's normal distribution |
| 10 | PCA, t-SNE and UMAP | t-SNE and UMAP were never expanded | Expanded both at first prose use |
| 10 | ARIMA definition | Not expanded | Added the full name to the definition |
| 10 | Forecasting frontier box | BigQuery, "data warehouse" (Chapter 11), Salesforce and GIFT-Eval were unexplained | Glossed all four |
| 10 | Platform tools | "DVC" was not expanded | Added "Data Version Control" |
| 10 | Testing an ML system | "Unit tests" are not defined until Chapter 21 | Glossed inline |
| 10 | Exercise 5 (forecasting bake-off) | Did not say what "one cycle" is for weekly Trends data, how to start exponential smoothing, or how to compute MAE in a sheet | Said one cycle is 52 rows, gave the smoothing start rule and fill-down rule, and gave the `=ABS` and `=AVERAGE` steps |
| 11 | C4 entry | "T5 model" was unexplained | Glossed as a 2019 language model |
| 11 | The Pile entry | EleutherAI was unexplained | Glossed as a nonprofit open-source AI research group |
| 11 | LAION-5B entry | LAION was unexplained | Glossed as a German nonprofit that builds open datasets |
| 11 | Common Pile entry | "Public-domain" was undefined (it is used again later) | Glossed inline |
| 11 | Collecting data from the web | Perplexity the company could be confused with the perplexity metric | Glossed as an AI search company |
| 11 | Cleaning example | "CA" and "Calif." were not explained | Added "both short for California" |
| 11 | Documentation is becoming law | "AB 2013" was unexplained | Glossed as Assembly Bill 2013, a state law |
| 11 | Bias in data | ProPublica was unexplained | Glossed as an investigative news organization |
| 11 | Privacy | AOL was unexplained | Glossed as America Online |
| 11 | Coin-flip survey | Where "0.5 × p + 0.25" comes from was skipped | Added the two-halves explanation |
| 11 | Synthetic data | NVIDIA is used in 43 chapters and is never defined | New definition callout: NVIDIA, added to Key terms |
| 11 | Copyright table | Suno and Udio were unexplained | Glossed as AI song generators |
| 11 | The data wall | NeurIPS was unexplained | Glossed as a large yearly AI research meeting |
| 11 | Going deeper | ACM is used in 3 chapters, all in reading lists, and is never defined | New definition callout: ACM (Association for Computing Machinery), placed after the bullet that uses it and added to Key terms |
| 11 | Exercise 4 (Titanic) | Survival by sex and class cannot be read from Kaggle's per-column previews | Download train.csv and use a pivot table with AVERAGE of Survived; noted the Join Competition step |
| 11 | Exercise 7 (bias audit) | "Hire rate" pivot from yes/no text needs steps the reader has not seen | Asked the chatbot for 1/0, and gave the Insert, Pivot table, AVERAGE steps |
| 11 | Exercise 8 (coin flip) | "Press Delete in an empty cell" may not trigger a recalculation; "try only 100 rows" did not say how | Said to type into an empty cell and press Enter, or F9 in Excel, and to change 1001 to 101 |

Fixes per chapter: 8: 7, 9: 12, 10: 15, 11: 17 (51 in total). By type:

| Chapter | Undefined terms | Beginner jumps | Exercises | Plainly wrong |
|---|---|---|---|---|
| 8 | 2 | 3 | 2 | 0 |
| 9 | 6 | 2 | 4 | 0 |
| 10 | 9 | 5 | 1 | 0 |
| 11 | 13 | 1 | 3 | 0 |

Three new definitions were added (IBM in Chapter 8; NVIDIA and ACM in Chapter 11), and each was added to its chapter's Key terms.

## Noticed but not changed

- The ACM definition sits in Going deeper, because a reading-list citation is the only place Chapter 11 (and the other two chapters that use it) mentions ACM. It splits that bullet list in two when rendered.
- The VC-dimension definition in Chapter 9 says "the largest number of points it can classify correctly under every possible labeling". Strictly, it is the largest number of points that can be arranged so that every labeling is achievable. It is a common simplification, so I left it.
- Chapter 9, Exercise 8 asks for "the right baseline accuracy" without stating it. It is about 55%: always predict "no default", since 45% defaulted. The reader can derive it from the chapter, so I added nothing.
- Optional frontier boxes still drop a few names with only a functional gloss (TabArena, Moirai, Full Stack Deep Learning, Great Expectations). They are understandable from context.
- No sourced 2025–2026 facts were changed. None looked inconsistent with earlier chapters. Kimi K3's 2.8 trillion parameters matches Chapter 7.

## Verdicts

**Chapter 8 (Learning From Examples).** An excellent on-ramp to Part II. Every idea starts at the simplest level, and the study-hours example carries the whole chapter: the 2-knob model, hand-computed MSE, gradient descent at three learning rates, spreadsheet SLOPE/INTERCEPT, then the same loop in Colab. All its numbers reproduce exactly. The difficulty ramp works. The steepest moment is logistic regression with e and cross-entropy, and it is now bridged to the ln key and to Table 8.9. Every term is defined in the chapter or earlier. IBM was the only defined-nowhere name. The two weak exercises (calibration buckets and the "clean data" boundary) are now doable and their answers match.

**Chapter 9 (Evaluation and Metrics).** Dense but well paced. The café overfitting table and the 1,000-person screening test are reproducible and do real teaching, and the Colab cell matches the text exactly. The ramp works up to the significance-test paragraph, which was the one real conceptual jump (now bridged). The benchmarks section was the main source of undefined names (CIFAR, top-5, ARC-AGI-3, RSQ), because their definitions live in Chapters 14 and 24. The spreadsheet exercises were the biggest barrier, with placeholders like TP, FN and p that a non-programmer would type literally. With real cell references, every term is now defined or glossed and every exercise can be done as written.

**Chapter 10 (The Classical ML Toolkit).** The most demanding chapter of the four. It covers about twenty algorithms plus a long MLOps section, and it uses more mathematics than Chapters 8 and 9: binomial counting, the normal-curve formula, eigenvectors and SVD. The running churn example with ten customers holds it together, and every hand calculation checks out. The ramp works for the supervised half. The unsupervised half (GMM/EM, PCA/SVD/ICA) is the steepest stretch of Part II; the added bridges make the arithmetic followable, though the eigenvector/SVD paragraph remains conceptual rather than worked. Names and acronyms were the main gap (SHAP, t-SNE/UMAP, ARIMA, DVC, SAP, Yandex, BigQuery, CART), and all are now expanded or glossed. The MLOps half is long but plain, with every term defined.

**Chapter 11 (Data: The Fuel of AI).** The easiest read of the four, and a good change of pace after Chapter 10. It is narrative, with little new math: kappa, TF-IDF, the coin-flip survey and the data-wall arithmetic, all correct. The SQL section is concrete and its answers match the Colab code. The ramp is gentle throughout. The friction was almost entirely unintroduced organizations and products in the dataset history, the industry section and the legal section (EleutherAI, LAION, T5, AOL, ProPublica, Perplexity, NeurIPS, NVIDIA), which are now glossed or defined. The exercises that relied on pivot tables or recalculation tricks now give the steps.
