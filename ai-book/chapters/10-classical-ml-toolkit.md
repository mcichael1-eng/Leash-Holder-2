# Chapter 10: The Classical Machine Learning Toolkit

*This chapter hands you the dozen classic algorithms that still make most of the world's everyday predictions, shows how each one "thinks" with small worked examples, and teaches you how to choose, test and run one yourself.*

## What you'll learn

- How the main supervised algorithms work, each with a worked example: k-nearest neighbors, linear and logistic regression, naive Bayes, decision trees, random forests, gradient boosting and SVMs.
- How unsupervised tools find structure without answers: clustering, PCA, t-SNE, UMAP and anomaly detection.
- The basics of recommendations (and the story of the Netflix Prize) and of time-series forecasting.
- Why boosted trees still rule spreadsheet-style data, and how 2025–26 "foundation models" for tables and time series are challenging them.
- How the humble perceptron connects all of this to the neural network behind your chatbot.
- How to pick an algorithm, run a project from question to monitoring, and use the standard free tools.
- How a model lives in production: batch versus real-time serving, staged rollouts, drift monitoring, retraining and the platform tools that support them.
- Where classical machine learning fits in a world of large language models.

## Before you start

Chapter 8 (Learning From Examples) explained models, parameters, features, labels, training and inference. Chapter 9 (Is the Model Any Good?) explained train/test splits, overfitting, cross-validation and metrics such as precision and recall. Chapters 5 and 6 supply the math: distances, dot products, probability, Bayes' rule, the sigmoid curve and gradient descent. Chapter 3 introduced Python and Google Colab, used in the exercises.

## Why a toolkit, and why it still matters

Every time you press Enter in ChatGPT, Claude or Gemini, a giant neural network does the work, so it is natural to assume all AI is now neural networks. It is not. When your bank texts "Was this you?" about a payment, or a supermarket decides how much milk to order for Tuesday, the model is very often one of the "classical" algorithms in this chapter: older, smaller, cheaper, and on the right problem still the best tool.

> **Definition — Classical machine learning:** The family of machine-learning methods developed mostly before the deep-learning boom of the 2010s, such as regression, decision trees and clustering. They usually have from a handful to a few million parameters and run comfortably on an ordinary laptop.

Each algorithm carries a different idea about what patterns look like. One assumes "things that are close together behave alike." Another assumes "the answer is a weighted sum of the inputs." Another assumes "the answer can be found with a short series of yes/no questions." Choosing an algorithm is mostly choosing which assumption fits your problem.

> **Definition — Inductive bias:** The built-in assumption an algorithm makes about what kind of pattern it is looking for, such as "nearby examples share a label" or "the answer is a straight-line combination of the inputs." No algorithm can learn anything without one.

> **Definition — Tabular data:** Data arranged like a spreadsheet: each row is one example (a customer, a loan, a day) and each column is one feature. Most business data is tabular.

> **Analogy:** A hammer, a saw and a screwdriver are all tools for wood, but you would not drive a screw with a hammer. Each algorithm in this chapter is excellent at one shape of problem and clumsy at others, and a good practitioner knows which to reach for first.

```mermaid
mindmap
  root((Classical ML toolkit))
    Supervised
      k-nearest neighbors
      Linear and logistic regression
      Naive Bayes
      Decision trees
      Random forests
      Gradient boosting
      Support vector machines
    Unsupervised
      k-means and clustering
      PCA and t-SNE and UMAP
      Anomaly detection
    Special problems
      Recommenders
      Time-series forecasting
    Bridge
      Perceptron to neural networks
```

*Figure 10.1: The classical toolkit at a glance. Supervised tools learn from labeled answers; unsupervised tools find structure without them.*

```mermaid
timeline
    title When the classic tools arrived
    1901 : PCA first described by Karl Pearson
    1958 : Rosenblatt's perceptron
    1967 : k-nearest neighbors analyzed and k-means named
    1984 : CART decision trees
    1995 : Support vector machines in modern form
    2001 : Random forests
    2006 to 2009 : The Netflix Prize
    2014 : XGBoost released
    2025 : TabPFN-2.5 and Chronos-2 foundation models
```

*Figure 10.2: A rough timeline of the toolkit (CART stands for classification and regression trees). Many of these ideas are decades old and still in daily use.*

## A running example: will this subscriber cancel?

Imagine you work at a company selling a monthly chatbot subscription, much like a paid ChatGPT, Claude or Gemini plan. If you could predict who is about to cancel, you could offer help or a discount first. This is churn prediction, one of the most common machine-learning jobs in business.

> **Definition — Churn:** Customers leaving a service, for example by cancelling a subscription. "Churn prediction" means estimating which customers are likely to leave soon.

Here is a tiny training set with two features and one label. Real projects have thousands of rows, but ten let us do every calculation by hand.

| Customer | Hours of use per week | Months subscribed | Cancelled? |
|---|---|---|---|
| A | 1 | 2 | Yes |
| B | 2 | 1 | Yes |
| C | 2 | 4 | Yes |
| D | 3 | 2 | Yes |
| E | 8 | 3 | No |
| F | 6 | 9 | No |
| G | 9 | 10 | No |
| H | 7 | 6 | No |
| I | 2 | 11 | No |
| J | 5 | 2 | Yes |

A new subscriber, Q, uses the product 6 hours a week and has been subscribed for 4 months. Will Q cancel? We will ask several algorithms.

```
months
 12 |
 11 |       oI
 10 |                                   oG
  9 |                       oF
  8 |
  7 |
  6 |                           oH
  5 |
  4 |       xC              ?Q
  3 |                               oE
  2 |   xA      xD      xJ
  1 |       xB
  0 +---+---+---+---+---+---+---+---+---+---+
    0   1   2   3   4   5   6   7   8   9   10  hours/week
```

*Figure 10.3: The ten subscribers. x = cancelled, o = stayed, ? = the new customer Q.*

## k-nearest neighbors: you are like your neighbors

The simplest learning algorithm needs no training at all. To predict for a new example, it finds the k most similar examples it has already seen and lets them vote.

> **Definition — k-nearest neighbors (kNN):** An algorithm that predicts by finding the k most similar labeled examples and taking a vote (for categories) or an average (for numbers). k is a number the user chooses, such as 3 or 5.

> **Definition — Euclidean distance:** The straight-line distance between two points: subtract each pair of coordinates, square the differences, add them up and take the square root. It is what a ruler would measure on a graph.

Q is at (6 hours, 4 months) and E is at (8, 3). The differences are 2 and −1; squared, 4 and 1; added, 5; square root, about 2.24. Doing the same for everyone and sorting:

| Customer | Calculation | Distance | Cancelled? |
|---|---|---|---|
| E | (8−6)² + (3−4)² = 4 + 1 = 5 | 2.24 | No |
| H | (7−6)² + (6−4)² = 1 + 4 = 5 | 2.24 | No |
| J | (5−6)² + (2−4)² = 1 + 4 = 5 | 2.24 | Yes |
| D | (3−6)² + (2−4)² = 9 + 4 = 13 | 3.61 | Yes |
| C | (2−6)² + (4−4)² = 16 + 0 = 16 | 4.00 | Yes |

With k = 3, the neighbors are E, H and J: two stayed, one cancelled, so Q stays. With k = 5, D and C join, both cancelled, and the vote becomes three to two: Q cancels.

Same data, opposite answers, because k is a hyperparameter you choose (Chapter 8). Small k is jumpy: one odd neighbor can flip the answer (high variance, in Chapter 9's language). Large k is sluggish: with k = 10, every new customer gets the same 5-to-5 tie (high bias). In practice you pick k by cross-validation.

> **Key idea:** Q is a borderline customer, so reasonable settings disagree. That disagreement is itself useful: it tells you the model is unsure and a human might want to look.

kNN has two traps. First, units: if tenure were measured in days, a 30-day gap would swamp a 3-hour gap and usage would barely count.

> **Definition — Feature scaling:** Rescaling numeric features so they have comparable ranges, for example so each has an average of 0 and a typical spread of 1. Without it, features measured in big units dominate distance-based algorithms.

Second, dimensions: with 500 features, almost every point is about the same distance from every other, so "nearest" loses meaning (the "curse of dimensionality"). kNN is also slow at prediction time, since it compares each question with every stored example unless clever indexes find approximate neighbors quickly, as vector databases do (Chapter 27).

> **Analogy:** Real-estate agents price a house from "comps," the sale prices of the five most similar houses nearby. That is kNN for regression: average the neighbors instead of voting.

> **Watch out:** kNN looks too simple to matter, but its core idea, that similarity is distance between lists of numbers, is the idea behind embeddings and semantic search (Chapters 14 and 27). When Claude searches your uploaded files for the passage closest in meaning to your question, it is doing a nearest-neighbor lookup.

## Linear and logistic regression, revisited

Chapter 8 built these two step by step. Here they are as tools, the workhorses of medicine, economics and finance.

> **Definition — Linear regression:** A method that predicts a number as a weighted sum of the inputs plus a constant, for example price = 150 × square metres + 20,000. Training finds the weights that make the squared errors smallest.

> **Definition — Logistic regression:** Despite its name, a classification method. It computes a weighted sum of the inputs (a score) and squashes it into a probability between 0 and 1 with the S-shaped sigmoid curve.

Suppose logistic regression, trained on our ten subscribers, settles on:

`score = 4.5 − 0.6 × hours − 0.5 × months`

and turns the score into a probability with `1 ÷ (1 + e^(−score))`, where e is about 2.718 (Chapter 6).

For Q: score = 4.5 − 3.6 − 2.0 = −1.1. Since e^1.1 is about 3.00, the probability is 1 ÷ 4.00 = 0.25. A 25 percent chance of cancelling, so with the usual 0.5 threshold, Q stays. For customer A (1 hour, 2 months): score = 2.9, and the probability is 1 ÷ (1 + 0.055) = 0.95. These weights put all ten customers on the correct side of 0.5.

The real attraction is that you can read the weights. Each extra weekly hour lowers the score by 0.6, which multiplies the odds of cancelling (the chance it happens divided by the chance it does not) by e^−0.6, about 0.55: every extra hour of use roughly halves the odds.

> **Definition — Interpretability:** How easily a person can understand why a model made a particular prediction. A regression with five readable weights is highly interpretable; a forest of 500 trees much less so.

The decision boundary is where the score is zero. Doubling every number in 4.5 − 0.6 × hours − 0.5 × months = 0 gives 9 − 1.2 × hours − months = 0, which rearranges to months = 9 − 1.2 × hours: a straight line on Figure 10.3 from 9 months at zero hours down to zero months at 7.5 hours. Everyone below it is predicted to cancel. That straightness is the strength and the weakness. These models are fast, stable, hard to overfit with a little regularization (Chapter 9), and usually give well-calibrated probabilities. But if the true pattern curves, or depends on combinations ("light users cancel only if they are also new"), a straight line misses it unless a human adds features such as hours × months.

Linear and logistic regression are the best-known members of a family statisticians call generalized linear models: compute a weighted sum of the inputs, then pass it through a fixed function suited to what you are predicting. An amount uses the sum as it is (linear regression). A yes-or-no uses the sigmoid (logistic regression). A count, such as the number of insurance claims a driver files in a year, uses the exponential, which keeps the prediction positive (Poisson regression). For more than two classes, softmax (Chapter 6) replaces the sigmoid, giving softmax regression, which is exactly the calculation in the final layer of most neural-network classifiers.

> **Definition — Generalized linear model (GLM):** A family of models that compute a weighted sum of the inputs and pass it through a fixed function matched to the kind of answer: unchanged for amounts (linear regression), a sigmoid for yes-or-no (logistic regression), an exponential for counts (Poisson regression).

> **Definition — Softmax regression (multinomial logistic regression):** Logistic regression extended to more than two classes: one weighted sum per class, turned into probabilities with softmax. It is the same calculation as the last layer of a typical neural-network classifier.

> **Key idea:** When a bank must explain to a regulator, or a doctor to a patient, why the model said what it said, a regression with a few readable weights is often the right tool even if a more complex model scores slightly higher.

## Naive Bayes: adding up the clues

Naive Bayes is the classic early spam filter. It treats each word as a clue and combines clues with Bayes' rule (Chapter 6): start from the prior (how common spam is overall) and multiply by the likelihood of each clue (how often that word appears in spam compared with normal mail).

> **Definition — Naive Bayes:** A probabilistic classifier that multiplies together the evidence from each feature, assuming (naively) that the features are independent of one another once you know the class.

You have 100 past emails: 30 spam and 70 normal. You count two words:

| Word | Appears in spam | Appears in normal email |
|---|---|---|
| "free" | 15 of 30 (50%) | 7 of 70 (10%) |
| "meeting" | 3 of 30 (10%) | 21 of 70 (30%) |

A new email contains "free." Spam: 0.30 × 0.50 = 0.15. Normal: 0.70 × 0.10 = 0.07. Divide each by their total, 0.22: spam = 0.68, a 68 percent chance.

Another email contains both words. Spam: 0.30 × 0.50 × 0.10 = 0.015. Normal: 0.70 × 0.10 × 0.30 = 0.021. Spam = 0.015 ÷ 0.036 = 0.42. "Meeting" pulled it back toward normal. A real filter does this with thousands of words in a fraction of a millisecond.

Notice what the filter ignores: word order. It treats each email as a bag of words, a pile of word counts, so "dog bites man" and "man bites dog" look identical to it. For spotting spam or sorting articles by topic that is surprisingly harmless; for understanding meaning it is fatal, which is one reason language models read text in order (Chapter 15).

> **Definition — Bag of words:** Representing a piece of text only by which words it contains and how often, ignoring their order. It is the classic input for spam filters and topic classifiers.

The "naive" part is assuming the clues are independent. They are not ("free" and "offer" travel together), but for picking the more likely class the ranking usually survives. One fix is essential: a word never seen in spam would get probability zero and wipe out the whole product, so filters add a small pretend count to every word, a trick called Laplace smoothing.

> **Analogy:** Naive Bayes is a detective adding up clues: "mentions a lottery, more suspicious; sent by a known contact, less suspicious." The detective treats each clue as independent, which is not quite true, but the verdict is usually right.

Naive Bayes is fast, needs little data and remains a strong first baseline for text classification.

## Decision trees: Twenty Questions learned from data

A decision tree is a flowchart of yes/no questions ending in predictions. The clever part is that the algorithm chooses the questions.

> **Definition — Decision tree:** A model shaped like a flowchart of yes/no questions about the features ("Months subscribed 5 or more?"), learned from data, with a prediction stored at each final branch.

> **Definition — Node, leaf and depth:** In a decision tree, a node is a point where a question is asked, a leaf is a final box holding a prediction, and depth is the number of questions from the top to the deepest leaf.

At each step the algorithm tries every feature and many thresholds, and picks the question that splits the examples into the purest groups, as close as possible to all-Yes or all-No.

> **Definition — Gini impurity:** A score from 0 to 0.5 (for two classes) of how mixed a group is: 1 minus the sum of the squared shares of each class. An all-one-class group scores 0; a 50/50 mix scores 0.5.

Our ten subscribers are 5 cancelled and 5 stayed, so Gini = 1 − (0.5² + 0.5²) = 0.5, the most mixed possible. Try two first questions.

**"Hours per week 5 or more?"** Yes side: E, F, G, H, J (four stayed, one cancelled), Gini = 1 − (0.8² + 0.2²) = 0.32. No side: A, B, C, D, I, also 0.32. Weighted average: 0.32.

**"Months subscribed 5 or more?"** Yes side: F, G, H, I, all stayed, Gini = 0. No side: A, B, C, D, E, J (five cancelled, one stayed), Gini = 1 − ((5/6)² + (1/6)²) = 0.28. Weighted: 0.4 × 0 + 0.6 × 0.28 = 0.17.

The months question drops impurity to 0.17, far better than 0.32, so it goes first. On the "under 5 months" side, one more question finishes the job: E uses the product 8 hours a week and stayed, while A, B, C, D and J use it 5 hours or less and cancelled. The algorithm puts the threshold halfway between 5 and 8, at 6.5 hours.

```mermaid
flowchart TD
    R["Months subscribed 5 or more?"] -->|"Yes"| L1["Leaf: STAYS<br/>4 of 4 stayed"]
    R -->|"No"| N2["Hours per week 6.5 or more?"]
    N2 -->|"Yes"| L2["Leaf: STAYS<br/>1 of 1 stayed"]
    N2 -->|"No"| L3["Leaf: CANCELS<br/>5 of 5 cancelled"]
```

*Figure 10.4: The decision tree learned from the ten subscribers. Each leaf shows how many training customers ended there.*

Follow Q down: months 4, "No"; hours 6, less than 6.5, "No." The tree predicts Q cancels, disagreeing with logistic regression. Q sits near a boundary, and different inductive biases draw it in different places.

Trees are easy to read, mix numbers and categories freely, need no scaling and capture combinations naturally. Their weakness is overfitting: allowed to keep asking questions, a tree builds one leaf per training example and memorizes noise. Hyperparameters such as maximum depth and minimum examples per leaf keep it honest. Trees are also unstable: change a few rows and the top question can change.

> **Analogy:** A decision tree plays Twenty Questions. A good player asks the question that splits the remaining possibilities most evenly. A tree that asks forty questions about ten people has stopped playing and started memorizing.

## Random forests: a crowd of trees

That instability turns out to be useful. If trees make different mistakes, a crowd of them voting can cancel many mistakes out.

> **Definition — Ensemble:** A combination of several models whose predictions are merged, by voting or averaging, so that their individual errors partly cancel out.

The arithmetic of crowds: suppose each of five trees is right 70 percent of the time and, unrealistically, their mistakes are independent. The majority is right when at least three are. The 10 and the 5 below count the different ways it can happen: there are 10 ways to choose which three of the five trees are the right ones, and 5 ways to choose which single tree is the wrong one. Exactly three right: 10 × 0.7³ × 0.3² = 0.309. Exactly four: 5 × 0.7⁴ × 0.3 = 0.360. All five: 0.7⁵ = 0.168. Total: about 0.84. Five 70-percent trees make an 84-percent forest; 101 independent ones would be right more than 99.99 percent of the time.

The catch is "independent": trees trained on the same data make the same mistakes. Leo Breiman's random forest (2001) makes trees deliberately different. Each trains on a bootstrap sample, a random draw of rows with replacement (some rows twice, some not at all), and at each question each tree may consider only a random handful of features.

> **Definition — Bagging:** Short for "bootstrap aggregating": training many models on different random resamples of the rows and averaging or voting their predictions. It mainly reduces variance.

> **Definition — Random forest:** A bagged ensemble of decision trees in which each tree also sees only a random subset of features at each split, which makes the trees more different and their vote more reliable.

Random forests are the safe default of tabular machine learning: they need little tuning, rarely overfit badly as you add trees, and report which features mattered.

> **Definition — Feature importance:** A score for each input feature showing how much it contributed to a model's predictions, for example how much the trees' impurity dropped thanks to splits on that feature.

The price is interpretability: you can read one tree, not 500.

Feature importance describes the model as a whole. To explain one particular prediction ("why was this loan refused?"), two model-agnostic tools (ones that work with any kind of model) are standard. SHAP (SHapley Additive exPlanations) splits the prediction among the features using Shapley values from game theory, a method for sharing a team's winnings fairly according to what each player added (Chapter 48). LIME, introduced by Marco Tulio Ribeiro, Sameer Singh and Carlos Guestrin in 2016, takes the case being explained, makes many slightly altered copies of it (change the income a little, drop a word from the email), asks the black-box model for its prediction on each, and fits a small linear model to those nearby answers. The weights of that little model are the explanation: they say which features pushed this one prediction up or down. Both are approximations of the model's behavior, not a view of its insides, and they can disagree.

> **Definition — LIME (local interpretable model-agnostic explanations):** A method that explains one prediction of any model by testing slightly altered versions of the input and fitting a simple linear model to how the predictions change, whose weights show which features mattered for that case.

## Gradient boosting: a relay of tutors

Random forests build trees side by side. Boosting builds them one after another, each new tree focused on the mistakes left by those before it.

> **Definition — Boosting:** Building models in sequence, each trained to fix the errors of the combined models so far, then adding them all together.

> **Definition — Residual:** The leftover error for one example: the true value minus the current prediction.

Here is boosting with three houses that sold for $200,000, $300,000 and $400,000.

1. Start with the average, $300,000, for every house. Residuals: −$100,000, $0, +$100,000.
2. Train a small tree to predict those residuals. Suppose it learns them perfectly. Add only half its answer, a safety brake called the learning rate. Predictions: $250,000, $300,000, $350,000. Residuals: −$50,000, $0, +$50,000.
3. Train a second tree on the new residuals and add half again. Predictions: $225,000, $300,000, $375,000.
4. Each round halves the remaining error. After 10 rounds it is $100,000 × 0.5¹⁰, under $100.

Real data is noisy, so too many rounds start fitting noise; practitioners stop when validation error stops falling (early stopping, Chapter 9). "Gradient" appears because predicting the residuals is exactly a gradient-descent step on squared error (Chapter 6).

> **Definition — Gradient boosting:** Boosting in which each new tree is fitted to the gradient of the loss (for squared error, simply the residuals), so the ensemble walks downhill on its errors one small tree at a time.

> **Definition — XGBoost, LightGBM and CatBoost:** The three most popular open-source gradient-boosting libraries. XGBoost was released in 2014; LightGBM comes from Microsoft and CatBoost from Yandex, Russia's largest search-engine company.

For about a decade, gradient-boosted trees have been the default winner on tabular data, in industry and in Kaggle competitions: fraud scoring, credit risk, ad click prediction, insurance pricing, demand planning. Careful 2022 research comparing them with deep neural networks on typical business tables still found the trees ahead in most cases.

```mermaid
flowchart LR
    subgraph BAG["Random forest: parallel"]
        D1["Data"] --> T1["Tree 1"]
        D1 --> T2["Tree 2"]
        D1 --> T3["Tree 3"]
        T1 --> V["Vote or average"]
        T2 --> V
        T3 --> V
    end
    subgraph BOOST["Gradient boosting: in sequence"]
        S0["Start: the average"] --> B1["Tree 1 fits the errors"]
        B1 --> B2["Tree 2 fits what is left"]
        B2 --> B3["Tree 3 fits what is left"]
        B3 --> SUM["Add them all up"]
    end
```

*Figure 10.5: Bagging builds independent trees and lets them vote; boosting builds trees in sequence, each correcting the last.*

> **Analogy:** Boosting is a relay of tutors. The first teaches the whole syllabus. The second looks only at the questions the student still gets wrong. The third handles whatever is still wrong after that.

A third way to combine models mixes different kinds. In stacking, you train several unlike models, say a random forest, a boosted model and a logistic regression, and then train one more small model whose inputs are their predictions and whose job is to learn how much to trust each one, and when. To keep it honest, the combiner must learn from predictions the first models made on data they were not trained on, or it simply learns to trust whichever model memorized the training set best.

> **Definition — Stacking:** Combining several different models by training a final "combiner" model on their predictions, so it learns how much weight to give each one.

### The 2025–26 twist: foundation models for spreadsheets

Chapter 18 shows how a chatbot learns a task from examples pasted into your prompt, with no retraining. Could a model do the same for tables?

> **Definition — In-context learning:** A model picking up a new task from examples supplied in its input at prediction time, with no change to its parameters, as when you show a chatbot three examples and it follows the pattern.

The best-known answer is TabPFN, from the startup Prior Labs: a neural network pretrained on millions of synthetic, computer-generated tables. You do not train it. You hand it your whole small training table plus the new rows, and it predicts the labels in one pass.

> **Definition — Tabular foundation model:** A model pretrained, often on synthetic tables, to make predictions on new spreadsheet-style datasets with little or no training of its own. TabPFN is the best-known example.

According to its developers, TabPFN-2.5 (November 2025) led the TabArena benchmark ahead of tuned tree ensembles on small-to-medium tables. In May 2026 SAP, the German maker of business software used by many large companies, announced it would acquire Prior Labs, in a deal described as a commitment of more than €1 billion; it was reported closed in July 2026.

> **At the frontier (2026):** Gradient boosting is still the practical default for business tables: cheap, fast, well understood and runnable anywhere. But pretrained "models for spreadsheets" are moving fast, and big enterprise software makers are betting on them. Whether they replace hand-tuned XGBoost for everyday business data is one of 2026's open questions.

## Support vector machines: the widest street

If two classes can be separated by a line at all, many lines do it. A support vector machine picks the one that leaves the widest empty "street" between the classes, because a line hugging one class will misclassify the next example that lands slightly on the wrong side.

> **Definition — Support vector machine (SVM):** A classifier that finds the boundary leaving the widest possible margin between two classes.

> **Definition — Margin and support vectors:** The margin is the width of the empty street between the boundary and the nearest examples of each class. The support vectors are those nearest examples; they alone fix where the boundary goes.

Real data is messy, so SVMs allow some examples inside the street, with a penalty set by a hyperparameter usually called C: large C insists on few mistakes (risking overfitting), small C accepts some in exchange for a wider street.

The famous part is the kernel trick, which lets this straight-line method draw curves. Seven points sit on a number line, red (R) at both ends and blue (B) in the middle. No single cut separates them. Add a second feature, x squared: the reds become 9, 4, 4 and 9, the blues 1, 0 and 1, and a flat cut at 2.5 separates them perfectly. On the original line, that one cut becomes two, at about −1.58 and +1.58 (the two numbers whose square is 2.5).

```
BEFORE: one feature, x. No single cut separates R from B.

        R     R     B     B     B     R     R
      --+-----+-----+-----+-----+-----+-----+---  x
       -3    -2    -1     0     1     2     3

AFTER: add x squared as a second feature. One flat cut works.

 9 |    R                                   R
 4 |          R                       R
2.5| - - - - - - - - - - - - - - - - - - - - -  the cut
 1 |                B           B
 0 |                      B
   +----+-----+-----+-----+-----+-----+-----+---  x
       -3    -2    -1     0     1     2     3
```

*Figure 10.6: The idea behind the kernel trick. Lifting data into an extra dimension can make a curved problem straight.*

> **Definition — Kernel trick:** A mathematical shortcut that lets an SVM behave as if it had added many extra features (even infinitely many) without computing them, so it can draw curved boundaries cheaply.

SVMs dominated the 2000s, in handwriting recognition, text classification and biology, before deep learning took over. They still suit small, high-dimensional data, such as a few hundred patients with thousands of gene measurements, but are slow on very large datasets.

> **Analogy:** An SVM is a town planner drawing the widest possible road between two neighborhoods. The houses right at the roadside are the support vectors; move any other house and the road stays put.

Kernels power another classic method you may hear about. A Gaussian process predicts a number together with an honest error bar. Close to the examples it has seen, it is confident; far from them, its error bar widens. The kernel decides how similar two inputs are, and so how much each known example should sway a guess about a new one. Gaussian processes suit small datasets where knowing your uncertainty matters, such as deciding which experiment to run next, and they are the classic engine inside the Bayesian optimization of hyperparameters (Chapter 9). Their cost grows with the cube of the number of examples (double the examples and the work goes up eight times, because 2 × 2 × 2 = 8), so they struggle beyond tens of thousands of data points.

> **Definition — Gaussian process:** A method that predicts a value together with an uncertainty band, using a kernel to judge how much each known example should influence the prediction at a new point. The uncertainty is small near known examples and grows away from them.

## Clustering: finding groups without answers

So far we had a "Cancelled?" column to learn from. Often you have no labels, just a pile of customers or articles, and want to know whether they fall into natural groups.

> **Definition — Clustering:** Grouping examples so that members of the same group are similar to each other and different from other groups, without being told what the groups should be.

The most famous method is k-means. You choose k, the number of groups. The algorithm places k centers, then repeats two steps until nothing changes: assign every example to its nearest center, then move each center to the average of its examples (the centroid).

> **Definition — k-means:** A clustering algorithm that repeatedly assigns each example to the nearest of k centers and moves each center to the average of its assigned examples, until the groups stop changing.

By hand: six subscribers use the product 1, 2, 3, 10, 11 and 12 hours a week. Ask for k = 2 and start the centers, badly on purpose, at 1 and 4.

1. **Assign.** 1 and 2 go to center 1. 3, 10, 11 and 12 go to center 2.
2. **Move.** Center 1 moves to 1.5. Center 2 moves to 36 ÷ 4 = 9.
3. **Assign.** Hour 3 is now 1.5 from center 1 and 6 from center 2, so it switches. Groups: {1, 2, 3} and {10, 11, 12}.
4. **Move.** Centers go to 2 and 11.
5. **Assign.** Nobody switches. Converged.

You might name the groups "light users" and "heavy users." The algorithm did not name them or know they mattered. You did.

```mermaid
flowchart TD
    A["Choose k and place k starting centers"] --> B["Assign each point to its nearest center"]
    B --> C["Move each center to the average of its points"]
    C --> D{"Did any point change group?"}
    D -->|"Yes"| B
    D -->|"No"| E["Done: k clusters and their centers"]
```

*Figure 10.7: The k-means loop. It always stops, but where it stops depends on where the centers started.*

Bad starts can trap k-means, so software runs it several times and keeps the best. To choose k, the "elbow" trick plots how tight the clusters are for k = 1, 2, 3 and so on and stops where extra clusters stop helping. And k-means assumes round blobs; two other families handle other shapes.

> **Definition — Hierarchical clustering:** Building a tree of nested clusters by repeatedly merging the closest pair of groups, so you can cut the tree at whatever level of detail you like.

> **Definition — DBSCAN:** A density-based clustering method that grows clusters through crowded regions, finds clusters of any shape and labels isolated points as noise.

> **Analogy:** k-means is placing ice-cream trucks in a park. Put three trucks down anywhere, let everyone walk to the nearest one, move each truck to the middle of its crowd, and repeat until no one switches.

A softer cousin of k-means gives every point a probability of belonging to each group instead of an all-or-nothing assignment. In a Gaussian mixture model, each cluster is a bell curve (a normal distribution, Chapter 6) with its own center, spread and share of the data. Take our subscribers, with two bell curves centered at 2 and 11 hours, each with a spread (standard deviation) of 2.5 hours and an equal share. A subscriber who uses the product 6 hours a week sits 4 hours from the first center and 5 from the second. A bell curve's height falls off with distance from its center as e^(−distance² ÷ (2 × spread²)), the formula behind the normal distribution of Chapter 6, so the heights of the two bell curves at that point are proportional to e^(−4² ÷ (2 × 2.5²)) = e^(−1.28) ≈ 0.278 and e^(−5² ÷ (2 × 2.5²)) = e^(−2) ≈ 0.135, so she is 0.278 ÷ (0.278 + 0.135) ≈ 67% "light user" and 33% "heavy user."

The model is fitted with the expectation–maximization (EM) algorithm, which is k-means with soft edges. The E step computes every point's membership probabilities, as we just did. The M step moves each bell curve's center, spread and share to fit its members, each counted in proportion to its membership. Repeat until nothing changes. EM is a general recipe for learning when part of the picture is hidden (here, each point's true group), and it is how the hidden Markov models of classic speech recognition were trained (Chapter 46).

> **Definition — Gaussian mixture model (GMM):** A clustering model in which each cluster is a bell-shaped (normal) distribution with its own center and spread, and each point belongs to every cluster with some probability rather than to exactly one.

> **Definition — Expectation–maximization (EM):** An algorithm for fitting models with hidden information that alternates two steps: estimate the hidden parts using the current model (expectation), then refit the model using those estimates (maximization), until it settles.

> **Watch out:** Clusters are not facts about the world. k-means always returns exactly k groups, even from random noise. Humans decide whether the groups mean anything.

## Shrinking many columns into a few: PCA, t-SNE and UMAP

A dataset can have hundreds of columns, and a chatbot's internal representation of a word has thousands of numbers (Chapter 14). Nobody can picture 500 dimensions.

> **Definition — Dimensionality reduction:** Compressing many features into fewer, for example from 64 columns to 2, while keeping as much of the important information as possible.

Principal component analysis (PCA) looks for the directions along which the data spreads most. People's height and arm span rise together so closely that most variation lies along one diagonal, "overall size." A second direction, "arm span minus height," holds only small differences. Keep the first and drop the second, and two numbers become one with little lost.

> **Definition — Principal component analysis (PCA):** A method that finds new axes, each a weighted mix of the original features, ordered by how much of the data's variation they capture. Keeping only the first few compresses the data.

PCA tells you how much you keep. In the Colab exercise you will squash handwritten-digit images, 64 pixel values each, to just 2 components. Those keep about 28.5 percent of the variation, yet the plot already shows the digits forming recognizable neighborhoods.

> **Analogy:** PCA is finding the best camera angle. Photograph a long, flat sculpture end-on and you see a blob; from the side, its shape is obvious.

Two names travel with PCA. Its directions are the **eigenvectors** of a table recording how every pair of features varies together, and software usually finds them with **singular value decomposition (SVD)**, a standard routine that breaks any matrix into a rotation, a stretch along each axis and another rotation. The stretch factors, called singular values, rank the directions by importance. You will meet the idea again: LoRA (Chapter 30) bets that a fine-tuning change can be captured by a few such directions, and the Muon optimizer (Chapter 13) evens out the singular values of its updates. A cousin of PCA, independent component analysis (ICA), looks for directions that are statistically independent rather than widely spread; its textbook use is unmixing several voices recorded by several microphones in the same room.

> **Definition — Eigenvector:** A direction that a matrix only stretches or shrinks, without turning; the amount of stretch is its eigenvalue. PCA's principal components are the eigenvectors of the table of how the data's features vary together.

> **Definition — Singular value decomposition (SVD):** A standard way to break any matrix into three simple steps: a rotation, a stretch by different amounts along each axis, and another rotation. The stretch amounts (singular values) show which directions matter most.

> **Definition — Independent component analysis (ICA):** A method that unmixes signals by finding directions in the data that are statistically independent, such as separating two voices recorded together by two microphones.

PCA only rotates and squashes in straight lines. For pictures of complex data, t-SNE (2008; short for t-distributed stochastic neighbor embedding) and UMAP (2018; uniform manifold approximation and projection) are more popular: both keep each point's close neighbors close in a 2-D map, producing striking "islands" of similar items.

> **Definition — t-SNE and UMAP:** Methods for squashing high-dimensional data into a 2-D or 3-D map in which similar items end up near each other, used mainly for visualization.

> **Watch out:** In a t-SNE or UMAP map, island sizes and the distances between islands often mean little. Read these maps as who-is-near-whom, not as rulers.

This is the bridge to a central idea of modern AI. The famous "word maps," with "king" near "queen" and "Paris" near "France," are embeddings with hundreds of dimensions squashed to two by these methods.

> **Definition — Embedding:** A list of numbers representing an item (a word, image, product or user) so that similar items get similar lists. Embeddings let computers measure meaning as distance.

## Anomaly detection: spotting the odd one out

Your bank's "this doesn't look like you" message is anomaly detection.

> **Definition — Anomaly detection:** Identifying examples that are unusually different from the rest, such as a fraudulent payment, a failing machine or a network intrusion.

The simplest tool measures distance from normal in units of standard deviation, the typical spread of values around their average (Chapter 6).

> **Definition — Z-score:** How many standard deviations a value is from the average: (value − average) ÷ standard deviation. Values with a z-score beyond about 3 are often flagged as unusual.

Suppose your daily card spending averages $40 with a standard deviation of $15. A $85 day has z = (85 − 40) ÷ 15 = 3: unusual but plausible. A $400 day has z = 24, so the bank texts you. But z-scores look at one number at a time, and "normal" varies by person and season: a $400 day in December may be ordinary.

For many features at once, the isolation forest builds random trees of random cuts. A normal point in a dense crowd needs many cuts before it stands alone; an outlier is cut off quickly. In a crowd of about 1,000 points, halving it with each cut takes around 10 cuts to isolate a typical point (2 multiplied by itself 10 times is 1,024), while a lone outlier may fall away in 2 or 3.

> **Definition — Isolation forest:** An anomaly detector that builds random trees of random cuts and flags points that can be isolated with unusually few cuts.

Anomaly detection lives on Chapter 9's precision–recall trade-off: too eager and customers drown in false alarms, too relaxed and fraud slips through.

## Recommenders and the Netflix Prize

Recommender systems decide what fills your feeds and your streaming home screen. Chapter 51 covers today's giant systems; here are the foundations.

> **Definition — Recommender system:** A system that predicts which items (films, products, posts, songs) a person is likely to want, usually to rank what to show them.

> **Definition — Content-based filtering:** Recommending items whose attributes (genre, author, ingredients) resemble those of items the user already liked.

> **Definition — Collaborative filtering:** Recommending items based on the behavior of similar users ("people like you also liked") or similar items, without needing to know what the items are.

```
            Alien  Die Hard  Titanic  Notebook  Toy Story
  Sam         5       5         1        ?          3
  Priya       5       4         1        1          ?
  Leo         1       ?         5        5          4
  Mei         ?       1         4        5          5
```

*Figure 10.8: A ratings matrix with gaps. Sam and Priya rate almost identically, so Priya's 1 star for Notebook suggests Sam would also dislike it.*

The breakthrough of the 2000s was matrix factorization. Suppose each film has a few hidden traits, such as how much action and romance it contains, and each user has a taste for each trait. A predicted rating is then a dot product (Chapter 5). If Sam's tastes are (action 4, romance 1) and Die Hard's traits are (1.0, 0.1), the prediction is 4 × 1.0 + 1 × 0.1 = 4.1 stars. For The Notebook, (0.1, 0.9), it is 4 × 0.1 + 1 × 0.9 = 1.3 stars. The algorithm learns tastes and traits together from the known ratings, and nobody tells it that "action" exists.

> **Definition — Matrix factorization:** Splitting a big user-by-item ratings table into two smaller tables of hidden "taste" factors, one row per user and one per item, whose dot products fill in the missing ratings.

> **Definition — Cold-start problem:** The difficulty of recommending to a brand-new user, or recommending a brand-new item, when there is no history of behavior to learn from.

Most real signals are also implicit: services rarely get star ratings, but they see what you clicked, finished or skipped.

The most famous episode is the Netflix Prize. From 2006 to 2009 Netflix offered $1 million for a 10 percent improvement in its rating predictions and released about 100 million ratings. Thousands of teams competed, and the prize went in 2009 to the merged team "BellKor's Pragmatic Chaos," whose entry blended many models, an early showcase for ensembles. Two footnotes matter. Netflix later explained it never put the full winning blend into production, because the extra accuracy did not justify the engineering cost as its business shifted to streaming. And researchers showed that the "anonymized" ratings could be partly linked back to real people, which led to a privacy lawsuit and a cancelled second contest (Chapter 11).

> **Key idea:** The Netflix Prize taught three lessons that still hold: ensembles win competitions, a better score on a fixed metric is not automatically a better product, and "anonymous" data is often less anonymous than it looks.

## Forecasting time series

Many business questions concern the future of a number: sales next week, electricity demand tomorrow afternoon.

> **Definition — Time series:** A sequence of measurements recorded in time order, such as daily sales, hourly temperatures or monthly subscribers.

> **Definition — Trend and seasonality:** In a time series, the trend is the long-run upward or downward drift, and seasonality is a pattern that repeats on a fixed cycle, such as busier weekends or a December peak.

```mermaid
flowchart LR
    A["Observed daily sales"] --> B["Trend:<br/>slow growth"]
    A --> C["Seasonality:<br/>weekend peaks"]
    A --> D["Noise:<br/>random jitter"]
    B --> F["Forecast = trend + season,<br/>with a range for noise"]
    C --> F
    D --> F
```

*Figure 10.9: Decomposing a time series. Good forecasts model trend and seasonal cycle and treat the rest as uncertainty.*

A coffee shop sold these cups last week, Monday to Sunday: 120, 130, 125, 135, 160, 210, 190. What about next Monday?

| Method | Rule | Forecast for Monday | Error if Monday is 124 |
|---|---|---|---|
| Naive | Same as the last day (Sunday) | 190 | 66 |
| Seasonal naive | Same as last Monday | 120 | 4 |
| 7-day moving average | 1,070 ÷ 7 | 153 | 29 |

The seasonal naive forecast wins because the shop has a strong weekly cycle. Simple baselines like these are surprisingly hard to beat, and any fancier method must prove it does better.

> **Definition — Naive forecast:** The simplest forecast, "the next value equals the last value" (or, in the seasonal version, "equals the value one cycle ago"). It is the baseline every forecasting model must beat.

One step up, exponential smoothing blends the latest actual with the previous forecast. With a weight of 0.3: forecast 100, actual 120, so the next forecast is 0.3 × 120 + 0.7 × 100 = 106. If the next actual is 90, the forecast after that is 0.3 × 90 + 0.7 × 106 = 101.2. Recent values count most; older ones fade.

> **Definition — Exponential smoothing:** A forecasting method in which each new forecast is a weighted blend of the latest actual value and the previous forecast, so recent data counts most and older data fades.

> **Definition — ARIMA:** Short for autoregressive integrated moving average: a classic statistical forecasting model that predicts the next value from recent past values and recent past forecast errors, after removing trend.

Further up sit Prophet, an open-source forecaster from Meta (2017), and gradient-boosted trees fed lag and calendar features such as day of week and holidays, an approach large retailers use heavily.

> **Definition — Lag feature:** A past value of the series used as an input, such as "sales 7 days ago" or "sales on this date last year."

The golden rule is never peek at the future. A random train/test split lets a model learn from Thursday to predict Wednesday. Instead you backtest (Chapter 9's walk-forward validation).

> **Definition — Backtesting:** Testing a forecasting method by repeatedly training only on data up to a past date, forecasting the period after it, and comparing with what actually happened.

> **At the frontier (2026):** Forecasting has its own foundation models, pretrained on huge collections of time series. Amazon's Chronos-2 (October 2025) handles many related series and outside factors together; Google's TimesFM 2.5 is the default forecaster inside BigQuery, Google's cloud data warehouse (a database built for analysis, Chapter 11), with TimesFM 3.0, which can forecast several related series together, in preview as of October 2026; Moirai, from the business-software company Salesforce, and others compete on the GIFT-Eval benchmark, a public test of forecasters on many real-world time series. Whether they beat a tuned boosted-tree forecaster depends on the data, so backtest both.

> **Definition — Time-series foundation model:** A model pretrained on a large, varied collection of time series that can forecast a new series with little or no task-specific training.

## The perceptron: the bridge to neural networks

In 1958 the psychologist Frank Rosenblatt built the perceptron, a machine that learned to classify simple images. It multiplies each input by a weight, adds a bias, and outputs 1 if the total is above zero, otherwise 0.

> **Definition — Perceptron:** The simplest artificial neuron: a weighted sum of inputs plus a bias, followed by a hard yes/no threshold. It learns by nudging its weights whenever it makes a mistake.

You have seen this before. With our churn weights, Q's weighted sum is 4.5 − 0.6 × 6 − 0.5 × 4 = −1.1. Logistic regression squashes −1.1 smoothly to 0.25; a perceptron just asks "above zero?" and answers 0, "stays." A perceptron is logistic regression with a hard cutoff instead of an S-curve.

A single perceptron can only draw a straight line. In 1969 Marvin Minsky and Seymour Papert showed this rules out even exclusive-or ("true if exactly one input is true"), whose two classes sit on opposite corners of a square where no single line separates them. Their book helped push neural-network research into a long winter (Chapter 7).

The fix echoes the kernel trick. Stack perceptron-like units in layers, and the first layer computes new features ("is exactly one input on?") that make the problem straight for the next. The crucial difference is that a neural network learns those intermediate features from data instead of having a human or a fixed kernel supply them.

> **Definition — Neural network:** A model built from many layers of simple units, each computing a weighted sum followed by a squashing function, so that the layers learn their own intermediate features. Chapter 12 builds one from scratch.

This explains the great division of labor. For raw pixels, sound and text, nobody can hand-design good features, so networks that learn their own win by a mile; that is why your chatbot is a neural network. Business tables already arrive as meaningful features ("months subscribed," "debt to income"), so trees and regressions stay strong, cheap and explainable.

> **Key idea:** A neural network is, at heart, many logistic regressions stacked in layers and trained together so that each layer invents features for the next. Everything in Part III grows from that sentence.

## Choosing an algorithm: a cheat sheet

A famous result nicknamed "no free lunch" says that, averaged over every possible problem, no learner beats another. What matters is fit: what kind of data, how much, whether people must understand the decisions, and how fast predictions must be.

| Your situation | Try first | Also try |
|---|---|---|
| Table, predict a category or a number | Gradient boosting | Random forest, logistic or linear regression, TabPFN for small tables |
| Must explain every decision (credit, medicine) | Logistic or linear regression | A shallow decision tree |
| Images, audio, long text | A pretrained neural network | An LLM or vision model through an API |
| No labels, want groups | k-means | DBSCAN, hierarchical clustering |
| Want to see high-dimensional data | PCA | UMAP, t-SNE |
| Find rare odd cases | Isolation forest | z-scores, autoencoders (Chapter 16) |
| Forecast a series | Seasonal naive baseline | Exponential smoothing, boosting with lags, Chronos or TimesFM |

```mermaid
flowchart TD
    Q1{"Do you have labels?"} -->|"No"| U{"Groups, a map, or oddities?"}
    U -->|"Groups"| KM["k-means or DBSCAN"]
    U -->|"Map"| PC["PCA, then UMAP"]
    U -->|"Oddities"| IF["Isolation forest"]
    Q1 -->|"Yes"| Q2{"Raw images, audio or text?"}
    Q2 -->|"Yes"| NN["Pretrained neural network"]
    Q2 -->|"No, a table"| Q3{"Must every decision be explained?"}
    Q3 -->|"Yes"| LR["Logistic or linear regression,<br/>or a shallow tree"]
    Q3 -->|"No"| GB["Gradient boosting,<br/>check TabPFN if small"]
```

*Figure 10.10: A first-pass decision guide. Whatever you pick, compare it against a dumb baseline.*

> **Key idea:** Start simple and add complexity only when it pays. A logistic regression you understand, compared honestly against a baseline, beats a giant model you cannot debug.

## The machine-learning project lifecycle

Algorithms are the fun part, but in real projects they are a small slice of the work.

```mermaid
flowchart LR
    A["Frame the<br/>question"] --> B["Get the data"]
    B --> C["Explore<br/>EDA"]
    C --> D["Clean and<br/>build features"]
    D --> E["Baseline"]
    E --> F["Train and tune"]
    F --> G["Final test"]
    G --> H["Deploy"]
    H --> I["Monitor"]
    I -->|"Drift or new data"| D
    I -->|"Wrong question"| A
```

*Figure 10.11: The machine-learning project lifecycle. The loop back from monitoring keeps a model useful.*

Walk our churn project through it. **Frame the question:** if the plan is to offer discounts, the real question may be "who will stay only if offered one?", which is harder; and "cancelled" needs a precise definition. **Get the data:** usage logs, billing, support tickets, using only what will exist at prediction time (Chapter 9's leakage traps). **Explore:** charts may reveal that usage is missing for every mobile-app customer.

> **Definition — Exploratory data analysis (EDA):** Examining data with summaries and charts before modeling, to understand it and spot problems such as missing values, odd distributions and errors.

**Clean and build features** such as "change in usage last month" (Chapter 11). **Baseline:** "nobody cancels." **Train and tune** a few algorithms with cross-validation. **Final test:** open the sealed test set once. **Deploy**, perhaps as a nightly scoring job. **Monitor and retrain** as the world changes.

Machine-learning projects are also unusually hard to schedule. In ordinary software, a feature that is half built is roughly half done. In machine learning you often cannot know whether the goal is reachable until you try: the first week might lift accuracy from a 70 percent baseline to 85 percent, and the next two months might add one point, or none, because the information simply is not in the data. Experienced teams therefore plan in stages with a go-or-stop decision after each: a feasibility check against the baseline in days, a prototype in weeks, a pilot with a few real users, and only then full production. They state expected results as ranges rather than promises, and they stop projects early when the data cannot support them, which is cheaper than stopping late.

> **Definition — Proof of concept:** A small, quick experiment to check whether an idea can work at all, such as training a simple model on a sample of the data and comparing it with the baseline, before committing to a full project.

The work also needs several kinds of people: data scientists who explore data and build models, data engineers who build the pipelines (Chapter 11), machine-learning engineers who train and deploy at scale, platform engineers who run the shared tools described later in this chapter, a product manager, and domain experts who know what a prediction means for a customer. Chapter 63 describes each role, and Chapter 31 shows how companies arrange them into teams.

> **Watch out:** Newcomers think the job is choosing clever algorithms. Practitioners say it is mostly framing the question, getting and cleaning the right data, and explaining results. The often-quoted "80 percent of the time goes on data work" is folklore, not a measured statistic, but most practitioners recognize its spirit.

## The toolbox

You do not write these algorithms from scratch. A standard set of free tools covers almost everything here, most of it in Python inside notebooks such as Google Colab (Chapter 3).

> **Definition — pandas:** The standard Python library for working with tables of data, called DataFrames, much like a spreadsheet you control with code.

> **Definition — scikit-learn:** The standard free Python library for classical machine learning, with nearly every algorithm in this chapter behind the same simple commands.

| Tool | What it is for | Note |
|---|---|---|
| Spreadsheets | Small data, charts, simple regressions | Still valid for many jobs |
| Python with Jupyter or Colab notebooks | Code, results and notes on one page | Colab needs only a browser |
| pandas and NumPy | Loading, cleaning and crunching tables and arrays | pandas 3.0 arrived January 21, 2026, so older tutorials may show warnings |
| scikit-learn | Classical algorithms, splitting, metrics | Version 1.8 (December 2025) added experimental GPU support |
| XGBoost, LightGBM, CatBoost | Gradient boosting | The tabular workhorses |
| SQL | Asking questions of databases | Chapter 11 |
| Kaggle (owned by Google) | Competitions, free datasets, shared notebooks | Over 23 million accounts as of April 2025 |
| Hugging Face | Shared models and datasets | Chapters 11 and 30 |
| No-code and AutoML tools | Teachable Machine, Orange, BigQuery ML | Train models with clicks or SQL; AutoML tries many algorithms for you |

The beauty of scikit-learn is that every algorithm speaks the same verbs:

```python
from sklearn.ensemble import RandomForestClassifier  # pick an algorithm
model = RandomForestClassifier(n_estimators=300)     # set its hyperparameters
model.fit(X_train, y_train)                          # training: turn the knobs
predictions = model.predict(X_test)                  # inference: use the model
print(model.score(X_test, y_test))                   # accuracy on the test set
```

Swap the first two lines for any other algorithm and the rest stays the same, so a beginner can compare five algorithms in an afternoon.

> **Try it:** Paste the five lines above into ChatGPT, Claude or Gemini and ask: "Explain what each line does for a non-programmer." Then ask it to switch to k-nearest neighbors with k = 5 and explain what changed.

## MLOps: keeping a model alive

A model is trained once, but the world keeps moving.

> **Definition — MLOps:** The practices and tools for deploying, monitoring, updating and maintaining machine-learning models in real products, borrowed from "DevOps," software engineering's practices for shipping and running ordinary software reliably.

The biggest threat is drift. Data drift means the inputs change: a marketing campaign brings in younger customers who behave differently. Concept drift means the relationship itself changes: a competitor launches a cheaper product, and customers with the same usage now cancel more often. In 2020, when the pandemic changed how people shopped and spent almost overnight, many forecasting and fraud models trained on earlier years went wrong until they were retrained.

> **Definition — Data drift:** A change over time in the inputs a model sees, so they no longer resemble the training data.

> **Definition — Concept drift:** A change over time in the relationship between inputs and the correct answer, so patterns the model learned no longer hold.

```mermaid
sequenceDiagram
    participant App as Subscription app
    participant Model as Churn model service
    participant Mon as Monitoring
    participant Team as Data team
    App->>Model: Features for customer Q
    Model-->>App: 25 percent chance of cancelling
    App->>Mon: Log prediction and later the real outcome
    Mon->>Mon: Compare recent inputs and accuracy with training
    Mon-->>Team: Alert, accuracy falling and inputs drifting
    Team->>Model: Retrain on fresh data and redeploy
```

*Figure 10.12: A deployed model in daily life. Monitoring compares live data and outcomes with the training data and triggers retraining.*

Good MLOps also means experiment tracking: recording which data, code and settings produced each model so results can be reproduced and audited, fixing the random seed so "random" splits repeat exactly, and noting library versions so an upgrade does not silently change results.

> **Analogy:** A deployed model is a printed map. It was accurate the day it was printed, but roads change. MLOps is the surveying team that notices new roads and reprints the map before drivers get lost.

### Serving a model: batch or real time

Before a model can be monitored, it has to be put somewhere useful. There are two basic ways.

> **Definition — Batch prediction:** Running a model over a large set of inputs on a schedule, such as every customer once a night, and storing the results for later use. Also called offline inference.

> **Definition — Online prediction:** Running a model the moment a request arrives and returning the answer within a fraction of a second, as a card-fraud check or a chatbot does. Also called real-time inference.

Our churn model is a natural batch job. At 2 a.m. a script scores all 200,000 subscribers, a few minutes' work for an ordinary server, and writes a "risk" column into the database; the retention team's dashboard reads it at 9 a.m. Nobody is waiting, and if the job fails it is simply rerun. A fraud model cannot work that way: the payment terminal needs an answer in well under a second, so the model runs as a small web service behind an API (Chapter 26), answering one request at a time, around the clock. Online prediction is harder: the service must stay up, stay fast during traffic spikes, and compute its features from fresh data in milliseconds. A good rule is to use batch whenever the answer can be a few hours old, and online only when it cannot.

Engineers usually package a model service in a container, so it runs identically on a laptop, a test server and the cloud, and let a cluster manager such as Kubernetes (Chapter 62) start extra copies when traffic rises.

> **Definition — Container:** A sealed package holding a program together with every library and setting it needs, so it runs the same way on any machine. Docker is the best-known container tool.

One trap deserves its own name. Suppose the training data computed "average spend over the last 30 days" in a data scientist's notebook, and the live service computes it with code an engineer wrote later, which rounds differently and skips refunds. The model now sees slightly different numbers in production than it learned from, and quietly gets worse.

> **Definition — Training-serving skew:** A mismatch between how data is prepared for training and how it is prepared when the deployed model is used, which makes a model perform worse in production than in testing even though nothing in the world has changed.

### Rolling out a new model safely

A retrained model that scores better on the test set is a candidate, not a winner. Live traffic differs from any test set, so teams release new models in stages, exposing more users only when the previous stage looks healthy.

> **Definition — Shadow deployment:** Running a new model alongside the current one on real traffic and logging its predictions without acting on them, so the two can be compared safely before launch.

> **Definition — Canary release:** Sending a small share of real traffic, say 1 to 5 percent, to a new model first and watching for problems before widening the rollout. The name comes from the canaries miners once carried to warn of gas.

> **Definition — Rollback:** Switching production back to the previous version of a model or program when a new one misbehaves. Good teams can do it with one command.

```mermaid
flowchart LR
    A["Offline test:<br/>beats current model"] --> B["Shadow:<br/>logged, not used"]
    B --> C["Canary:<br/>5 percent of traffic"]
    C --> D["A/B test:<br/>half and half"]
    D --> E["Full rollout"]
    B -->|"problems"| R["Roll back<br/>and investigate"]
    C -->|"problems"| R
    D -->|"no real gain"| R
```

*Figure 10.13: A staged rollout. Each stage exposes more users only if the previous one looked healthy, and every stage can roll back.*

The numbers show why each stage exists. Suppose a fraud service checks 1 million payments a day. In shadow mode the new model scores all 1 million, but its verdicts are only logged; perhaps it disagrees with the old model on 3,000 payments, and analysts inspect a sample of those by hand. As a 5 percent canary it decides 50,000 real payments a day, so a serious bug hurts 50,000 customers instead of a million, and alerts fire within hours. Only then does an A/B test (Chapter 31) split traffic evenly to measure whether the new model really catches more fraud and blocks fewer honest customers, the business outcomes an offline test can only estimate. Recommenders often use interleaving instead, mixing two models' suggestions into a single list and counting whose items people choose, which detects differences with far fewer users. And when several versions compete, bandit methods (Chapter 51) shift traffic toward the winner as evidence builds rather than waiting for a fixed test to end.

### Monitoring: what to watch and how to spot drift

Drift comes in three flavors that call for different responses. Picture a model that predicts whether a loan applicant will repay.

> **Definition — Covariate shift:** A change in the mix of inputs a model sees while the relationship between inputs and answers stays the same, such as a lender suddenly receiving far more applications from young people. It is the most common kind of data drift.

> **Definition — Label shift:** A change in how common each answer is, while what each kind of case looks like stays the same, such as the share of loans that default doubling during a recession. Also called prior shift.

Concept drift, defined above, is the third: the same kind of applicant now behaves differently, perhaps because a new law changed how debts are collected. Covariate shift may do no harm if the model already handled young applicants well. Label shift leaves the model's ranking of applicants roughly right but makes its probabilities too optimistic or too pessimistic. Concept drift breaks the model outright and calls for retraining on recent data.

Two more distinctions help in practice. First, drift has a shape in time. It can be sudden (the pandemic changed shopping almost overnight), gradual (tastes shift over months), periodic (holiday shopping every December, or people in different time zones using an app at different hours) or temporary (a one-day promotion, or an attacker probing the model). Periodic drift fools people most often: compare this December with last December, not with November, or every holiday season will look like a crisis. Temporary drift usually needs no retraining at all, only a check that it really has ended. Second, sometimes the world stays put but the definitions move. A feature change happens when an input is added, removed or redefined, such as age suddenly reported in months instead of years. A label schema change happens when the set of possible answers changes: the support team splits the old "billing" category into "refund" and "payment failed", or "cancelled" is redefined to include paused accounts. Retraining on the old labels cannot fix a schema change; the training data has to be relabeled for the new categories first.

> **Definition — Periodic drift (seasonal drift):** A shift in a model's inputs or outcomes that repeats on a cycle, such as holiday shopping each December or weekend traffic each week. It should be judged against the same point in the previous cycle, not against last week.

> **Definition — Label schema change:** A change in the set or meaning of the answers a model must give, such as one category being split in two or "cancelled" being redefined. The old labels no longer match, so training data must be relabeled before retraining.

What to watch, from cheapest to most valuable:

| Layer | Examples | Catches |
|---|---|---|
| System health | Requests per minute, errors, response time | Crashes, outages, slowness |
| Inputs | Missing values, ranges, the mix of each feature | Broken pipelines, covariate shift |
| Predictions | Share predicted "will cancel", average score | Many problems, early and without labels |
| Outcomes | Accuracy once the true answers arrive | What actually matters, but late |

The last row is the hard one, because the true answer often arrives long after the prediction.

> **Definition — Feedback delay:** The time between a model's prediction and the moment the true answer becomes known, from seconds for a clicked recommendation to a month for a cancellation or years for a loan.

So teams treat the earlier rows as early warnings. A common score for "has this column moved?" is the population stability index. Split the feature into buckets, then for each bucket multiply (this week's share − training share) by ln(this week's share ÷ training share), and add up the results. Here is the customer age mix of our subscription app after a campaign aimed at students:

| Age group | Training share | This week | Difference | ln(this week ÷ training) | Product |
|---|---|---|---|---|---|
| Under 30 | 0.30 | 0.45 | +0.15 | ln(1.50) = 0.405 | 0.061 |
| 30 to 49 | 0.50 | 0.40 | −0.10 | ln(0.80) = −0.223 | 0.022 |
| 50 and over | 0.20 | 0.15 | −0.05 | ln(0.75) = −0.288 | 0.014 |

The products add up to about 0.10. A widely used rule of thumb reads under 0.1 as stable, 0.1 to 0.25 as worth a look, and over 0.25 as a major shift, so this campaign sits right at the "take a look" line: check whether the model is as accurate for under-30s as for everyone else.

> **Definition — Population stability index (PSI):** A score for how much the distribution of one feature, or of a model's scores, has moved between two periods, computed by comparing the share of data in each bucket. Values above about 0.25 usually signal a major shift.

Formal statistical tests such as the Kolmogorov–Smirnov test do the same job with a yes-or-no verdict, though on millions of rows they flag even trivial, harmless changes as "significant".

> **Watch out:** Most alarms are not the world changing. When Google engineers reviewed close to a hundred outages of one large machine-learning pipeline, most had ordinary software and data causes rather than anything specific to machine learning. A column renamed, a price switched from dollars to cents, a sensor sending zeros, a join that silently dropped half the rows: check the plumbing before blaming drift. And tune alerts with care, because a monitor that fires every day teaches people to ignore it.

### Retraining: how often, and how

When monitoring shows the model slipping, or simply on a schedule, you retrain. There are two ways to do it.

> **Definition — Stateless retraining:** Training a fresh model from scratch on a recent window of data, such as the last 12 months, every time the model is updated.

> **Definition — Stateful training (incremental training):** Updating the existing model by continuing to train it on only the data that arrived since the last update. It is cheaper and faster, but needs care so the model does not wander or forget older patterns.

Most teams start with a calendar, retraining monthly from scratch, then automate the whole chain (pull the data, train, evaluate, and if the new model wins, start a staged rollout) so it runs without anyone remembering to do it. Mature teams add triggers that retrain when drift or a drop in accuracy is detected, and some move to frequent stateful updates: ad-click and fraud models at large companies may update daily or even hourly, which is the online learning of Chapter 8.

Retraining needs the right data, and that starts with logging. Every live prediction should be stored with the exact inputs the model saw, the model version and, once it is known, the true outcome, so the next training set is built from production as it really was (which also guards against the training-serving skew described earlier). Then comes curation, because labeling everything is usually too expensive. Teams typically label a random sample, to keep an honest picture of overall accuracy; add extra examples from slices that matter or perform badly (Chapter 9); and add the cases where the model was least confident or a person overruled it, the active-learning idea from Chapter 8. Finally they choose the training window, all history or only the last 12 months, so stale patterns age out. The Full Stack Deep Learning course calls this repeating cycle of logging, curating, retraining and testing the continual improvement workflow.

> **Definition — Prediction logging:** Recording every live prediction together with the exact inputs the model saw, the model version and, once known, the true outcome, so performance can be measured and future training data can be drawn from real use.

How often is often enough? Measure it. Train a model on January to June data and test it separately on July, August, September and October. If accuracy goes 0.85, 0.84, 0.82, 0.79, the model loses six points in a quarter and needs at least monthly updates. If it holds steady for a year, monthly retraining is wasted effort. This "value of freshness" experiment turns a guess into a schedule.

> **Key idea:** A model in production is never finished. Serving, rollout, monitoring and retraining form a loop, and the teams that do well automate that loop so a fresh model can ship safely every week rather than every year.

### Testing a machine-learning system

Ordinary software has unit tests, small automatic checks that each piece of code does what it should (Chapter 29). A machine-learning system needs those plus three kinds of check of its own.

- **Data tests** run whenever new data arrives, before training or scoring: ages between 0 and 120, no more than 1 percent of emails missing, every customer ID unique, today's row count within 20 percent of yesterday's. Open-source tools such as Great Expectations let you write these as rules. They catch the broken pipelines from the warning above before a model learns from them.
- **Training tests** check the training code. The most useful is to train on a tiny sample, say 10 examples, and confirm the model can memorize it almost perfectly. A model that cannot even overfit 10 examples has a bug, such as labels shuffled out of line with their rows, a wrong loss or a learning rate of zero, and more data will not fix it.
- **Evaluation gates** run automatically before any release: the candidate must beat the current model on the test set without getting worse on important slices of the data or on behavioral tests (both explained in Chapter 9).

> **Definition — Data validation:** Automatic checks that incoming data matches expectations, such as allowed ranges, types, missing-value rates and row counts, before it is used to train or run a model.

> **Definition — Overfitting a single batch:** A sanity check in which a model is trained on a handful of examples to confirm it can learn them almost perfectly. Failure points to a bug in the code or data rather than a shortage of data.

> **Definition — Evaluation gate:** An automatic rule that blocks a new model from release unless it beats the current model on agreed tests, both overall and on key subgroups.

A handy self-check comes from Google. A 2017 paper by Eric Breck and colleagues, "The ML Test Score", turned lessons from many production systems into a rubric of 28 tests in four areas of seven each: features and data, model development, the infrastructure that trains and serves models, and monitoring. Each test earns half a point if someone runs it by hand and documents the result, and a full point if it runs automatically and repeatedly. The final score is the lowest of the four area totals, not their sum, because a superb set of model tests cannot make up for having no monitoring at all. The authors tried it on 36 teams across Google; on their scale 0 means "more of a research project than a productionized system" and above 5 means exceptional automated testing and monitoring. You do not need Google's scale to use it: reading the 28 questions is a quick way to find the holes in your own project.

> **Definition — ML Test Score:** A rubric of 28 tests for production machine-learning systems, published by Google engineers in 2017, covering data, model development, infrastructure and monitoring, with the final score set by the weakest of the four areas.

### The ML platform: tracking, registries and feature stores

For one model, a few scripts and a careful person suffice. For fifty models, companies build or buy a shared platform so each team does not reinvent the plumbing.

> **Definition — ML platform:** The shared internal tools a company's teams use to train, store, deploy and monitor models, run by a platform team so each product team does not rebuild the same plumbing.

The usual pieces:

- **Experiment tracking.** Every training run logs its code version, data version, settings and scores to a shared dashboard, so "which model was that?" always has an answer. MLflow and Weights & Biases are widely used.
- **Data versioning.** Datasets get version numbers just as code does with Git (Chapter 3), using tools such as DVC (Data Version Control), so any model can be rebuilt from exactly the data that made it.
- **Model registry.** A catalog of trained models with their versions, scores, owners and status (testing, production, retired), and the one place deployment tools fetch models from.
- **Feature store.** A shared library of features, such as "spend in the last 30 days", computed by one piece of code and served both to training jobs and to live models. It is the standard cure for training-serving skew, and it lets ten teams reuse one feature instead of writing it ten slightly different ways. Feast is a popular open-source example.
- **Pipelines and compute.** Orchestrators such as Airflow (Chapter 11) run the steps in order, on clusters scheduled by systems such as Kubernetes.

> **Definition — Experiment tracking:** Automatically recording the code, data, settings and results of every training run, so any model can be compared, reproduced and audited later.

> **Definition — Data versioning:** Recording each version of a dataset, as Git records versions of code, so any model can be traced to, and rebuilt from, the exact data that trained it.

> **Definition — Model registry:** A catalog of trained models that records each version's training data, scores, owner and status, and serves as the single source from which deployment tools pull models.

> **Definition — Feature store:** A shared system that computes, stores and serves model features, so the same feature definitions are used in training and in production and can be reused across teams.

The big clouds sell the whole kit as managed services, such as Amazon SageMaker, Google Vertex AI, Azure Machine Learning and Databricks. The buy-or-build rule from Chapter 31 applies here too: buy the plumbing, and build only what makes your models better than a competitor's.

## Classical machine learning in the age of LLMs

In 2026 LLMs and classical models work together in four ways. **As labelers:** an LLM labels 10,000 support tickets, humans check a sample, and a small, fast classical model trains on the result. **As feature makers:** an embedding model turns each customer message into numbers that capture its meaning, which a boosted tree uses alongside ordinary columns. **As coding assistants:** pandas and scikit-learn code is drafted in seconds; the scarce skill is knowing whether it is right. **As analysts:** chat apps run Python on a spreadsheet you upload and fit models from a plain-English request.

There are equally strong reasons not to send every prediction to an LLM. Cost: a bank scoring 10 million card payments a day would pay $10,000 a day, about $3.65 million a year, at an illustrative tenth of a cent per LLM call, while a boosted tree scores them on a few ordinary servers. Speed: a small model scores a payment in well under a millisecond; an LLM call takes hundreds of milliseconds or more. Explainability and regulation: lenders and insurers must often justify decisions. Stability: a fixed model gives the same answer to the same input, which auditors like.

> **Watch out:** "Deep learning made classical ML obsolete" is a common misconception. For business tables, boosted trees and logistic regression remain the workhorses because they are cheaper, faster and more explainable. Even their 2025–26 challengers, tabular foundation models, are neural networks built specifically to beat trees on the trees' home ground.

> **At the frontier (2026):** The newest twist is AI agents that do data science themselves: load a dataset, explore it, try several algorithms from this chapter, cross-validate and write up results. They are fast and useful, but they inherit every trap in Chapter 9, from leakage to overfitting the validation set. Knowing the toolkit is what lets you check their work.

> **Try it:** Upload a small spreadsheet (even a made-up one with 30 rows) to a chatbot that can run code, and ask: "Train a logistic regression and a random forest to predict the last column, use 5-fold cross-validation, compare them with a majority-class baseline, and explain the results to a beginner." Then ask: "What could make these results misleading?"

## In plain English

Machine learning is a toolbox, and each tool assumes something different about patterns. k-nearest neighbors says "you are like the examples closest to you." Linear and logistic regression say "the answer is a weighted sum of the inputs," which makes them easy to explain. Naive Bayes adds up clues like a detective. Decision trees play Twenty Questions. Random forests let a crowd of differently trained trees vote, and gradient boosting builds trees one after another, each fixing the mistakes left so far; on business tables boosted trees have been champions for a decade, though "foundation models for tables" such as TabPFN now challenge them. Support vector machines draw the widest road between two classes.

Without answers, k-means finds groups, PCA and its cousins squash many columns into a picture, and anomaly detectors flag the odd one out. Recommenders learn from people with similar taste, and forecasters split a series into trend, cycle and noise, tested without peeking at the future.

The perceptron, a weighted sum with a yes/no cutoff, is the seed of the neural network behind your chatbot: stack many and let them learn their own features. In real projects most of the work is framing the question, getting and cleaning data, beating a simple baseline and watching the model as the world drifts. LLMs now help with labels, features and code, but small classical models still win when you need cheap, fast, explainable predictions.

## Key terms

Classical machine learning, inductive bias, tabular data, churn, k-nearest neighbors (kNN), Euclidean distance, feature scaling, linear regression, logistic regression, interpretability, generalized linear model (GLM), softmax regression (multinomial logistic regression), naive Bayes, bag of words, decision tree, node, leaf, depth, Gini impurity, ensemble, bagging, random forest, feature importance, LIME (local interpretable model-agnostic explanations), boosting, residual, gradient boosting, XGBoost, LightGBM, CatBoost, stacking, in-context learning, tabular foundation model, support vector machine (SVM), margin, support vectors, kernel trick, Gaussian process, clustering, k-means, hierarchical clustering, DBSCAN, Gaussian mixture model (GMM), expectation–maximization (EM), dimensionality reduction, principal component analysis (PCA), eigenvector, singular value decomposition (SVD), independent component analysis (ICA), t-SNE, UMAP, embedding, anomaly detection, z-score, isolation forest, recommender system, content-based filtering, collaborative filtering, matrix factorization, cold-start problem, time series, trend, seasonality, naive forecast, exponential smoothing, ARIMA, lag feature, backtesting, time-series foundation model, perceptron, neural network, exploratory data analysis (EDA), proof of concept, pandas, scikit-learn, MLOps, data drift, concept drift, batch prediction, online prediction, container, training-serving skew, shadow deployment, canary release, rollback, covariate shift, label shift, feedback delay, population stability index (PSI), stateless retraining, stateful training (incremental training), data validation, overfitting a single batch, evaluation gate, ML platform, experiment tracking, data versioning, model registry, feature store, periodic drift (seasonal drift), label schema change, prediction logging, ML Test Score.

## Exercises

1. **[Easy] Be the nearest neighbor.** Pencil and paper, 15 minutes.
   1. Copy the ten-subscriber table from this chapter.
   2. A new customer, R, uses the product 3 hours a week and has been subscribed for 9 months. Compute R's Euclidean distance to all ten customers (square the two differences, add, take the square root; a phone calculator is fine).
   3. Sort the distances and predict "cancel" or "stay" with k = 1, k = 3 and k = 5.
   4. Now pretend months were recorded in days (multiply every months value by 30) and redo the k = 3 prediction. Which feature now dominates?

   **What you'll learn:** how kNN really works, why k is a choice, and why feature scaling matters.

2. **[Easy] Human k-means with coins.** Tabletop, 20 minutes.
   1. Scatter about 20 coins on a table in two or three loose clumps.
   2. Place 3 "center" markers (bottle caps) at random spots.
   3. Assign each coin to its nearest marker, then move each marker to the middle of its coins. Repeat until no coin changes marker.
   4. Start again with the markers in different places. Do you get the same groups?

   **What you'll learn:** clustering, iteration, convergence, and how the starting position changes the result.

3. **[Easy] Grow a decision tree on paper.** Chatbot plus paper, 30 minutes.
   1. Ask a chatbot: "Give me the classic 14-row 'play tennis' weather table with columns Outlook, Temperature, Humidity, Wind and Play, as a plain table."
   2. For each of the four columns, split the 14 days by that column's values and count Play = Yes and No in each group.
   3. Compute the Gini impurity of each group (1 minus the sum of squared shares) and the size-weighted average for each column. The lowest average is the best first question.
   4. Build a two-level tree and use it to predict three new days you invent. Ask the chatbot to check your arithmetic.

   **What you'll learn:** how trees choose their questions and why they are easy to explain.

4. **[Medium] A naive Bayes spam filter in a spreadsheet.** Google Sheets or Excel, 40 minutes.
   1. Write 10 short messages, 4 spam ("Win a free prize now") and 6 normal ("Meeting moved to 3pm"), one per row, with a Spam? column.
   2. Pick 5 clue words (for example free, win, meeting, now, lunch). Add a column per word with 1 if the message contains it, 0 if not (or use a formula such as `=IF(ISNUMBER(SEARCH("free",A2)),1,0)`).
   3. For each word, compute the share of spam messages and the share of normal messages that contain it. Add 1 to each count and 2 to each total first (Laplace smoothing) so nothing is zero.
   4. Write a new message. Multiply the prior (4/10 or 6/10) by the shares for the words it contains, for each class, and divide by the total to get the spam probability.

   **What you'll learn:** priors, likelihoods, Laplace smoothing and why naive Bayes is fast.

5. **[Medium] Forecasting bake-off.** Google Sheets plus Google Trends, 60 minutes.
   1. At trends.google.com, search a term with a weekly or yearly rhythm (for example "pizza" or "gym") and download the past 5 years as CSV. Open it in Sheets.
   2. For the last 8 periods, make four forecasts per period using only earlier data: naive (previous value), seasonal naive (same period one cycle ago; five years of Trends data come as one row per week, so for a yearly rhythm that is the value 52 rows earlier), 4-period moving average (the `=AVERAGE` of the 4 rows just before), and exponential smoothing with weight 0.3 (in a new column, set the first forecast equal to the first value of the series; each row below is 0.3 × the previous row's actual value + 0.7 × the previous row's forecast, filled down to the end).
   3. For each method compute the mean absolute error: next to each of the 8 forecasts put its miss with `=ABS(...)`, for example `=ABS(C200-B200)` if the forecast is in C200 and the actual value in B200, then take the `=AVERAGE` of the 8 misses.
   4. Which method won? Ask a chatbot to explain why, given your series' shape.

   **What you'll learn:** trend, seasonality, baselines and honest backtesting.

6. **[Medium] Train and compare two classical models in Google Colab.** Colab, 45 minutes. Open colab.research.google.com, click "New notebook," paste each block below into its own cell and run it with Shift+Enter. The data is scikit-learn's built-in breast-cancer dataset: 569 tumor samples, each with 30 measurements taken from a microscope image, labeled malignant (cancer) or benign.

   ```python
   # ---------- Cell 1: load the tools ----------
   import pandas as pd                                   # tables in code
   from sklearn.datasets import load_breast_cancer       # a built-in medical dataset
   from sklearn.model_selection import train_test_split, cross_val_score
   from sklearn.pipeline import make_pipeline            # chains steps together
   from sklearn.preprocessing import StandardScaler      # puts features on one scale
   from sklearn.linear_model import LogisticRegression   # model 1
   from sklearn.ensemble import RandomForestClassifier   # model 2
   from sklearn.dummy import DummyClassifier             # the "dumb baseline"
   from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix

   # ---------- Cell 2: load the data and look at it ----------
   data = load_breast_cancer(as_frame=True)   # 569 tumor samples, 30 measurements each
   X = data.data                              # the features (inputs)
   y = (data.target == 0).astype(int)         # the label: 1 = malignant (cancer), 0 = benign
   print("Rows and columns:", X.shape)
   print("Cancer cases:", y.sum(), "of", len(y))
   print(X.iloc[:5, :4])                      # peek at 5 rows, 4 columns

   # ---------- Cell 3: split into study set and sealed exam ----------
   X_train, X_test, y_train, y_test = train_test_split(
       X, y, test_size=0.2, random_state=42, stratify=y)   # 80% train, 20% test, same cancer mix
   print("Training rows:", len(X_train), " Test rows:", len(X_test))

   # ---------- Cell 4: define the contestants ----------
   models = {
       "Baseline (always 'benign')": DummyClassifier(strategy="most_frequent"),
       "Logistic regression": make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000)),
       "Random forest (300 trees)": RandomForestClassifier(n_estimators=300, random_state=42),
   }

   # ---------- Cell 5: train, cross-validate and test each one ----------
   rows = []
   for name, model in models.items():
       cv = cross_val_score(model, X_train, y_train, cv=5, scoring="accuracy")  # 5 practice quizzes
       model.fit(X_train, y_train)                 # training = turning the knobs
       pred = model.predict(X_test)                # inference on the sealed exam
       rows.append({
           "model": name,
           "cv accuracy": round(cv.mean(), 3),
           "test accuracy": round(accuracy_score(y_test, pred), 3),
           "precision": round(precision_score(y_test, pred, zero_division=0), 3),
           "recall": round(recall_score(y_test, pred), 3),
       })
       print(name)
       print(confusion_matrix(y_test, pred))       # rows: true benign/cancer, columns: predicted
   print(pd.DataFrame(rows).to_string(index=False))

   # ---------- Cell 6: what did each model pay attention to? ----------
   forest = models["Random forest (300 trees)"]
   importance = pd.Series(forest.feature_importances_, index=X.columns)
   print("Random forest - top 5 features:")
   print(importance.sort_values(ascending=False).head(5).round(3))

   logreg = models["Logistic regression"].named_steps["logisticregression"]
   weights = pd.Series(logreg.coef_[0], index=X.columns)
   print("Logistic regression - 5 biggest weights (positive = pushes toward cancer):")
   print(weights.reindex(weights.abs().sort_values(ascending=False).index).head(5).round(2))
   ```

   What each cell does, in plain words: Cell 1 loads the free libraries. Cell 2 loads the data, flips the label so that 1 means cancer, and prints a peek. Cell 3 locks away 20 percent of the samples as a final exam, keeping the same share of cancer cases in both parts. Cell 4 lists three contestants: a baseline that always says "benign," a logistic regression (with feature scaling first) and a random forest. Cell 5 scores each one with 5-fold cross-validation on the training data, then trains it and tests it once on the sealed exam, printing a confusion matrix and a summary table. Cell 6 shows which measurements each model relied on. When we ran it in late 2026, the baseline scored about 63 percent accuracy with zero recall, while both real models scored around 96–97 percent, with logistic regression slightly ahead in cross-validation and the forest slightly ahead on the test set; your numbers may differ a little with library versions. Then experiment: change `n_estimators=300` to `10`; add a k-nearest-neighbors contestant with `from sklearn.neighbors import KNeighborsClassifier` and `make_pipeline(StandardScaler(), KNeighborsClassifier(n_neighbors=5))`; and decide which model you would trust for cancer screening, where missing a cancer (recall) matters most.

   **What you'll learn:** the full train, cross-validate and test workflow in code, why a baseline matters, and that the fancier model does not always win.

7. **[Medium] Pick the right tool.** Chatbot, 20 minutes.
   1. Ask a chatbot: "List 10 realistic business prediction problems, one per line, without saying which algorithm to use." 
   2. For each, use this chapter's cheat sheet to choose a first algorithm and a baseline, and write one sentence of reasoning.
   3. Paste your answers back and ask the chatbot to critique them. Where you disagree, decide who is right and why.

   **What you'll learn:** matching problem shapes to inductive biases, and checking a chatbot's reasoning rather than trusting it.

8. **[Challenge] Find structure without labels in Colab.** Colab, 45 minutes. Paste these cells into a new notebook.

   ```python
   # ---------- Cell 1: tools and data ----------
   import pandas as pd
   import matplotlib.pyplot as plt
   from sklearn.datasets import load_digits
   from sklearn.decomposition import PCA
   from sklearn.cluster import KMeans

   digits = load_digits()            # 1,797 tiny 8x8 images of handwritten digits
   X = digits.data                   # each image flattened to 64 numbers (pixel darkness 0-16)
   y = digits.target                 # the true digit 0-9 (we hide this from k-means)
   print(X.shape)

   # ---------- Cell 2: PCA squashes 64 columns down to 2 ----------
   pca = PCA(n_components=2)
   X2 = pca.fit_transform(X)
   print("Share of variation kept by 2 components:", round(pca.explained_variance_ratio_.sum(), 3))
   plt.figure(figsize=(7, 6))
   plt.scatter(X2[:, 0], X2[:, 1], c=y, cmap="tab10", s=8)   # color each dot by its true digit
   plt.colorbar(label="true digit")
   plt.title("64-pixel digits squashed onto 2 axes by PCA")
   plt.show()

   # ---------- Cell 3: k-means finds 10 groups WITHOUT seeing the labels ----------
   km = KMeans(n_clusters=10, n_init=10, random_state=0)
   clusters = km.fit_predict(X)                               # a group number for each image
   table = pd.crosstab(clusters, y, rownames=["cluster"], colnames=["true digit"])
   print(table)                                               # which digits landed in which group
   purity = table.max(axis=1).sum() / len(y)
   print("Share of images in a cluster dominated by their own digit:", round(purity, 3))
   ```

   Cell 2 should report that two components keep about 28.5 percent of the variation and draw a map where same-digit dots crowd together. Cell 3 runs k-means without ever seeing the labels, then compares its groups with the true digits; expect roughly 80 percent of images to land in a cluster dominated by their own digit. Look at the table: which digits get confused (often 1, 8 and 9)? Try `n_clusters=5` and `20`.

   **What you'll learn:** dimensionality reduction, clustering, and how much structure exists in data before anyone labels it.

9. **[Challenge] Watch a tree overfit, and a forest fix it.** Colab, 20 minutes.

   ```python
   from sklearn.datasets import load_breast_cancer
   from sklearn.model_selection import train_test_split
   from sklearn.tree import DecisionTreeClassifier
   from sklearn.ensemble import RandomForestClassifier

   X, y = load_breast_cancer(return_X_y=True)
   X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0, stratify=y)

   print("depth  train_accuracy  test_accuracy")
   for depth in [1, 2, 3, 4, 5, 7, 10, 15, None]:            # None = no depth limit at all
       tree = DecisionTreeClassifier(max_depth=depth, random_state=0)
       tree.fit(X_train, y_train)                            # grow one tree
       print(f"{str(depth):>5}  {tree.score(X_train, y_train):14.3f}  {tree.score(X_test, y_test):13.3f}")

   forest = RandomForestClassifier(n_estimators=300, random_state=0).fit(X_train, y_train)
   print("Random forest of 300 unlimited trees:",
         round(forest.score(X_train, y_train), 3), round(forest.score(X_test, y_test), 3))
   ```

   The loop grows one tree at each maximum depth and prints its accuracy on the data it studied and on the sealed test set. Expect training accuracy to climb to a perfect 1.000 by depth 7 while test accuracy stalls around 0.90–0.91: the deeper trees are memorizing. The last line grows 300 unlimited trees as a random forest; expect its test accuracy to jump to about 0.95 even though every tree in it overfits. Write two sentences explaining why.

   **What you'll learn:** overfitting in action, the max-depth hyperparameter, and why ensembles reduce variance.

## Areas of opportunity

- **Tabular data scientist or ML engineer.** Churn, fraud, credit risk, pricing and demand forecasting are still mostly classical ML, and companies pay for people who can frame the question, build a trustworthy boosted-tree model and explain it to managers.
- **Forecasting and decision science.** Retailers, restaurants, utilities and logistics firms need demand forecasts they can act on; people who can backtest honestly and compare classical methods with the new time-series foundation models are in demand.
- **Vertical ML products for small businesses.** A forecasting tool for independent restaurants, churn prediction for subscription boxes or gyms, anomaly alerts for small manufacturers: classical ML plus a good interface is often enough, and these customers cannot hire data scientists.
- **Model validation and explainability in regulated industries.** Banks, insurers and healthcare providers must document and defend their models; specialists in interpretable models, fairness checks and model risk review are steadily needed.
- **MLOps and monitoring.** Many companies have models in production that nobody watches. Drift monitoring, retraining pipelines and experiment tracking are concrete services a consultant or small firm can sell.
- **LLM-plus-classical cost cutting.** Companies that send millions of simple classification calls to LLMs can often save most of that cost by having the LLM label data once and training a small model; helping them do it is a clear value proposition.
- **Tabular and time-series foundation models.** SAP's purchase of Prior Labs shows enterprise appetite. Open problems include scaling to larger tables, handling messy real-world columns, and proving reliability; startups and integrators can build on the open releases.
- **Teaching no-code and AI-assisted analysis.** Managers, analysts and small-business owners want to run these algorithms through chatbots and no-code tools without being misled; practical training in baselines and validation is a sellable skill.
- **Open problems worth working on.** Robustness to drift, calibrated probabilities, fair models when sensitive attributes are unavailable, and whether pretrained models will replace hand-tuned XGBoost for everyday business data.

## Check your understanding

1. For the new customer Q, k-nearest neighbors predicted "stays" with k = 3 and "cancels" with k = 5. Why, and how would you choose k in practice?
2. In the naive Bayes example, why did adding the word "meeting" lower the spam probability from 68 percent to 42 percent, and what exactly is "naive" about naive Bayes?
3. Why does a random forest train each tree on a random sample of rows and let it consider only random subsets of features?
4. How does gradient boosting differ from a random forest, and what stops boosting from overfitting?
5. A bank must predict loan defaults and explain each decision to regulators. Which algorithm would you try first, and why might it accept slightly lower accuracy?
6. Why is a random train/test split wrong for evaluating a sales forecaster, and what should you do instead?
7. How is a perceptron related to logistic regression, and what limitation did Minsky and Papert point out in 1969?
8. Give three reasons a bank might score card payments with a small classical model rather than an LLM call.

<details><summary>Answers</summary>

1. Q is a borderline case. Its three nearest neighbors (E, H and J, all at distance 2.24) include two who stayed, but the next two (D and C) both cancelled, so widening the vote to five flips the majority. k is a hyperparameter: try several values and pick the one that scores best in cross-validation on held-out data.
2. "Meeting" appears in 30 percent of normal emails but only 10 percent of spam, so multiplying it in favors the normal class (0.021 against 0.015). It is "naive" because it assumes each word is independent evidence given the class, which is false (spammy words travel together), though the ranking of classes usually survives.
3. To make the trees different from each other. Trees trained on identical data make the same mistakes, so voting would not help. Random rows (bootstrap samples) and random feature subsets decorrelate the trees, so their errors partly cancel when they vote.
4. A forest builds independent trees in parallel and averages them; boosting builds small trees in sequence, each fitted to the errors (residuals) left by the trees before it, adding only a fraction of each (the learning rate). Too many rounds would fit noise, so practitioners use early stopping on a validation set, plus limits on tree depth.
5. Logistic regression (or a shallow decision tree), because each weight or rule can be read and explained, the probabilities are usually well calibrated, and the model is stable. Regulated decisions often require a justification for each applicant, which matters more than a small gain in accuracy.
6. A random split lets the model learn from later dates to predict earlier ones, which is impossible in real life and makes scores look too good. Use backtesting (walk-forward validation): train only on data before a cut-off date, forecast the next period, then slide forward and repeat.
7. A perceptron computes the same weighted sum as logistic regression but applies a hard yes/no threshold instead of the smooth S-shaped sigmoid. A single perceptron can only draw a straight-line boundary, so it cannot learn exclusive-or (XOR), whose classes sit on opposite corners; stacking units into layers that learn intermediate features solves this, which leads to neural networks.
8. Any three of: cost (millions of calls a day add up quickly), speed (well under a millisecond versus hundreds of milliseconds), explainability for regulators and customers, and stability (the same input always gives the same answer).

</details>

## Going deeper

- **An Introduction to Statistical Learning** (James, Witten, Hastie and Tibshirani), free at statlearning.com, with a Python edition: the clearest serious textbook on everything in this chapter.
- **Hands-On Machine Learning with Scikit-Learn, Keras and TensorFlow** (Aurélien Géron): the most popular practical book, full of runnable notebooks.
- **The scikit-learn User Guide** (scikit-learn.org): excellent plain explanations and examples for every algorithm, plus its "choosing the right estimator" map.
- **StatQuest with Josh Starmer** (YouTube): friendly, visual explanations of decision trees, random forests, gradient boosting, PCA and more.
- **Kaggle Learn** (kaggle.com/learn): free short courses, "Intro to Machine Learning" and "Intermediate Machine Learning," that run in the browser.
- **Machine Learning Specialization** (Andrew Ng, DeepLearning.AI and Coursera): a well-paced video course covering regression, trees, clustering, anomaly detection and recommenders.
- **Forecasting: Principles and Practice** (Hyndman and Athanasopoulos), free at otexts.com/fpp3: the standard friendly guide to time-series forecasting and backtesting.
- **"XGBoost: A Scalable Tree Boosting System"** (Chen and Guestrin, 2016): the paper behind the most famous boosting library.
- **"Why do tree-based models still outperform deep learning on tabular data?"** (Grinsztajn, Oyallon and Varoquaux, 2022): a careful comparison explaining the trees' advantage, useful context for the TabPFN debate.
