# Chapter 9: Is the Model Any Good? Evaluation, Overfitting and Metrics

*This chapter gives you the tools to tell a genuinely good model from one that only looks good, and to see through impressive-sounding numbers, including the ones in AI headlines.*

## What you'll learn

- Why a model's score on its own training data is nearly meaningless, and how splitting data into training, validation and test sets fixes that.
- How models cheat by accident through data leakage, with real cautionary tales from medicine and research.
- What overfitting and underfitting look like, with a worked example where a fancier model does dozens of times worse on new data.
- The bias–variance tradeoff, explained with a dartboard, plus a first look at the surprising "double descent" of huge models.
- How regularization and cross-validation keep you honest.
- How to build a confusion matrix and compute accuracy, precision, recall, specificity and F1 by hand, using a medical test and a real cancer dataset.
- How thresholds, ROC curves and AUC work, and how to measure models that predict numbers.
- Why you should always beat a dumb baseline, how to tune settings without cheating, and why benchmarks stop working once everyone aims at them (Goodhart's law).

## Before you start

You need Chapter 8 (Learning From Examples), which introduced models, parameters, hyperparameters, training versus inference, generalization, loss functions and thresholds. Chapter 6 (The Math of AI, Part 2) helps with probability, base rates and Bayes' rule, which explain why a positive medical test can still mean you are probably healthy. Chapter 5 introduced graphs and curves. As always, every number here is worked out step by step, and you can redo all of it in a spreadsheet.

## Why "how good is it?" is a hard question

In Chapter 8 you fit a line to ten students and got a mean squared error of 1.0. Was that a good model? You cannot tell from that number alone. A model that simply memorized all ten students would score a perfect 0.0 and be useless for the eleventh.

The same trap shows up in AI headlines every week. A fraud detector is "99.9% accurate." A new chatbot "beats every rival on the leading benchmark." A medical AI "matches expert doctors." Each claim might be true and important, or true and meaningless, or quietly false. This chapter teaches you to tell which.

Evaluation answers three questions:

1. **Does it generalize?** Does the model work on examples it has never seen?
2. **Which mistakes does it make?** Not just how many, but which kind, and what they cost.
3. **Is it actually better than the alternative?** Better than a simple rule, an older model or a human?

> **Definition — Evaluation:** Measuring how well a model performs, in a way that predicts how it will behave on real, new data. Good evaluation is honest about which mistakes the model makes and how sure we can be of the score.

> **Key idea:** A model is only as good as its performance on data it did not learn from. Everything in this chapter is a way of measuring that honestly.

## Splitting the data: train, validation and test

The single most important habit in machine learning is simple: before you train anything, set some data aside and do not let the model see it.

> **Definition — Training set:** The portion of the data the model learns from. Its parameters are adjusted to fit these examples.

> **Definition — Validation set:** Held-out data used during development to compare models and tune hyperparameters. The model never trains on it, but your choices are shaped by it.

> **Definition — Test set:** Data locked away until the very end and used once, to give an honest final score. If you peek at it while making decisions, it stops being a test.

Here is a typical split. You have 10,000 emails labeled spam or not spam. Shuffle them at random, then cut:

- 70% for training: 7,000 emails.
- 15% for validation: 1,500 emails.
- 15% for testing: 1,500 emails.

```mermaid
flowchart TD
  ALL["All 10,000 labeled emails<br/>shuffled at random"] --> TR["Training set<br/>7,000 emails, 70%"]
  ALL --> VA["Validation set<br/>1,500 emails, 15%"]
  ALL --> TE["Test set<br/>1,500 emails, 15%<br/>locked away"]
  TR --> FIT["Fit many candidate models"]
  FIT --> VA
  VA --> PICK["Compare them and<br/>pick the best one"]
  PICK --> TE
  TE --> FINAL["Report one honest<br/>final score"]
```

*Figure 9.1: The three-way split. Train on the training set, make choices with the validation set, and open the test set only once at the end.*

Why three sets instead of two? Because choosing is a form of learning. Suppose you train 50 different models and pick the one with the best score on some held-out set. Part of that winning score is skill, and part is luck: the winner happened to suit those particular 1,500 emails. If you then report that same score as your final result, you are reporting a lucky number. The validation set absorbs the luck of choosing. The test set, untouched by any decision, tells you the truth.

> **Analogy:** The validation set is the practice quizzes; the test set is the sealed final exam. Take as many practice quizzes as you like and adjust your studying. Open the final once.

### Keeping the mix fair

Suppose only 2% of the emails are spam: 200 out of 10,000. If you cut the data purely at random, one set might get 160 spam emails and another only 15, just by chance. To avoid this, split each class separately: 140 spam for training, 30 for validation and 30 for test, and the same proportions for the 9,800 normal emails.

> **Definition — Stratified sampling:** Splitting data so that each part keeps the same mix of classes as the whole, for example 2% spam in the training, validation and test sets alike.

### How sure is the score?

A test set is a sample, and samples are noisy. If a spam filter gets 90% of 1,500 test emails right, its true accuracy on all future emails is probably close to 90%, but not exactly. A standard statistics rule of thumb (Chapter 6 covers the background) gives the margin of error for an accuracy as about `1.96 × square root of (accuracy × (1 − accuracy) ÷ number of test examples)`.

Worked out for 1,500 emails at 90%: `0.9 × 0.1 = 0.09`; divided by 1,500 is 0.00006; the square root is about 0.0077; times 1.96 is about 0.015. So the honest statement is "90%, give or take about 1.5 percentage points." With only 100 test emails the same calculation gives about plus or minus 6 points.

> **Definition — Margin of error:** The range within which the true value probably lies, given the noise of measuring on a limited sample. A score of 90% plus or minus 1.5 points means the true accuracy is very likely between 88.5% and 91.5%.

This matters more than people think. If model A scores 91.0% and model B scores 91.8% on the same 1,500 test emails, the difference is smaller than the noise. You have not shown that B is better. Many "state of the art" claims in research papers and product launches are differences of this size.

> **Watch out:** A small test set makes every number wobbly. Before you get excited about a score, ask how many examples it was measured on. A chatbot "winning" 7 out of 10 comparisons tells you almost nothing; 700 out of 1,000 tells you a lot.

## Data leakage: how models cheat by accident

The most common way to fool yourself in machine learning is not a math error. It is leakage: information sneaks into the model's inputs that would not be available when the model is actually used, or test data quietly ends up in training.

> **Definition — Data leakage:** When information that would not be available at prediction time, or information from the test set, sneaks into training, producing scores that look excellent and mean nothing.

> **Analogy:** Data leakage is the answer key slipping under the exam paper. The student scores 100%, and the score tells you nothing about what the student knows.

Leaks come in a few recognizable shapes.

```mermaid
flowchart LR
  L["Data leakage"] --> T["Target leakage<br/>a feature that is only<br/>known after the answer"]
  L --> D["Duplicate leakage<br/>same item or person<br/>in train and test"]
  L --> F["Time leakage<br/>training on data<br/>from the future"]
  L --> P["Preprocessing leakage<br/>test data used when<br/>cleaning or scaling"]
  L --> B["Benchmark contamination<br/>test questions found<br/>in training text"]
```

*Figure 9.2: Five common kinds of leakage. Each one makes a model look better in testing than it will be in real use.*

**Target leakage.** Imagine predicting whether a hospital patient has a certain infection, and one of your columns is "antibiotic prescribed." The model will learn that this column predicts infection extremely well, because doctors prescribe the antibiotic after they diagnose the infection. In real use, you want the prediction before the diagnosis, when that column is empty. The same thing happens with a loan dataset that includes "collections agency contacted": a perfect predictor of default, recorded only after the default happened.

> **Definition — Target leakage:** A kind of leakage where a feature is a consequence of the answer, recorded after the fact, such as "treatment given" when predicting a disease.

**Duplicate leakage.** If the same item appears in both training and test data, the test partly measures memory. Researchers found that the popular CIFAR image benchmarks contained near-duplicates of some test images in their training sets. In medicine, a subtler version happens when several scans of the same patient are split across training and test. The model can learn to recognize that patient instead of the disease. The fix is to split by patient, not by scan.

**Time leakage.** When predicting the future, you must train only on the past. A model that predicts next month's sales using a feature computed over the whole year, including next month, looks brilliant in testing and fails on day one.

**Preprocessing leakage.** Even calculating an average over all the data, test set included, before splitting can leak a little information. The rule is: split first, then do everything else using only the training data.

> **Definition — Benchmark contamination:** When the questions and answers of a public test end up in a model's training data, for example because they were posted online and scraped. Scores then partly measure memory rather than ability.

Benchmark contamination is leakage at the scale of a whole field. Chatbots are trained on huge scrapes of the internet, and popular test questions get discussed, copied and posted online. Labs try to remove them from training data, a step called decontamination (see Chapter 19), but it is hard to be sure every copy was caught.

### Shortcut learning: the right answer for the wrong reason

A close cousin of leakage is a model that finds an easy clue that happens to work in the data but has nothing to do with the real task.

> **Definition — Shortcut learning:** When a model succeeds by exploiting an accidental clue in the training data, such as the background of a photo or a marker on an X-ray, instead of the thing it was supposed to learn.

Some of the best-known cases:

- **Wolves and snow.** In a 2016 paper on explaining model decisions ("Why Should I Trust You?"), researchers deliberately trained a classifier on photos where every wolf stood on snow and every husky did not. The model learned "snow means wolf." Their explanation tool exposed the trick. It was a planted experiment, but the lesson stuck because real systems do the same thing without anyone planting it.
- **Which hospital took the X-ray.** A 2018 study of a pneumonia detector trained on chest X-rays found that the model could tell which hospital an image came from, and that its performance dropped on images from other hospitals. Hospitals differ in their patients and their equipment, so "which hospital" was a useful clue in the training data and useless in the real world. A 2021 study of COVID-19 X-ray models found similar shortcuts, including text markers in the corner of images.
- **Rulers and skin cancer.** Dermatology researchers reported that an image classifier for skin lesions seemed more likely to call a lesion malignant when a ruler appeared in the photo. Doctors tend to measure the spots that worry them, so the ruler was a hint about what the doctor thought.

> **Watch out:** If a result looks too good to be true, look for a leak before you celebrate. A survey by Princeton researchers Sayash Kapoor and Arvind Narayanan (2023) found leakage problems in hundreds of published papers that used machine learning, across more than a dozen scientific fields.

> **Try it:** Ask your chatbot: "Create a 15-row table for predicting whether a customer will cancel their phone contract. Secretly include one column that leaks the answer. Don't tell me which." Then find the leak yourself and ask the chatbot to confirm. Typical leaks are columns like "final bill date" or "retention offer made."

## Overfitting and underfitting

Leakage is cheating from outside. Overfitting is a model fooling itself from inside, by learning the noise in its training data as if it were a real pattern.

> **Definition — Overfitting:** When a model learns the quirks and random noise of its training data so closely that it does worse on new data. Its training score is excellent and its test score is disappointing.

> **Definition — Underfitting:** When a model is too simple to capture the real pattern, so it does poorly even on its training data.

> **Definition — Noise:** The random, unpredictable part of data: measurement errors, one-off events and everything the features cannot explain. A good model ignores noise; an overfit one memorizes it.

### A worked example: iced drinks and temperature

A café records the outdoor temperature and how many iced drinks it sold on 12 days. Sales rise with temperature, and they rise faster on hot days.

| Temperature (°C) | 10 | 12 | 14 | 16 | 18 | 20 | 22 | 24 | 26 | 28 | 30 | 32 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Iced drinks sold | 22 | 20 | **27** | 29 | 36 | **38** | 47 | 49 | **60** | 63 | 75 | **80** |
| Used for | train | train | test | train | train | test | train | train | test | train | train | test |

*Table 9.1: Twelve days of café data. The four bold days (14, 20, 26 and 32 °C) are held out as a test set; the model trains on the other eight.*

We fit curves of increasing flexibility to the eight training days. A "degree 1" curve is a straight line, as in Chapter 8. "Degree 2" can bend once, like a gentle bowl. Higher degrees can wiggle more and more. A curve of degree 7 has 8 knobs, exactly as many as there are training days, so it can pass through every single one.

> **Definition — Polynomial:** A formula built from powers of the input, such as `a + b × x + c × x²`. Its degree is the highest power used. Higher-degree polynomials can draw more wiggly curves.

> **Definition — Model complexity:** How flexible a model is: how many different patterns it is able to fit. More parameters, deeper trees or higher-degree curves mean more complexity. Also called capacity.

Here are the mean squared errors (Chapter 8) on the training days and on the four held-out test days.

| Model | Knobs | Training MSE | Test MSE | Prediction at 32 °C (truth: 80) |
|---|---|---|---|---|
| Degree 0: always predict the average | 1 | 336.23 | 491.08 | 42.6 |
| Degree 1: straight line | 2 | 12.67 | 13.60 | 74.5 |
| Degree 2: gentle curve | 3 | 3.98 | **2.79** | 82.0 |
| Degree 3 | 4 | 3.97 | 3.41 | 82.4 |
| Degree 5 | 6 | 0.33 | 71.47 | 95.3 |
| Degree 7: passes through every training day | 8 | 0.00 | 206.51 | 52.8 |

*Table 9.2: Training error always falls as the model gets more flexible. Test error falls, bottoms out at degree 2, then shoots up. The degree-7 model is perfect on the training days and about 74 times worse than degree 2 on new days.*

Read the table from top to bottom. Predicting the average for every day underfits badly. The straight line is decent but misses the way sales accelerate on hot days, so it underfits a little. The gentle curve captures the real shape and does best on the test days. After that, extra flexibility only helps the model memorize the training days. The degree-7 curve hits all eight training days exactly, then predicts that a 32 °C scorcher will sell fewer drinks than a 26 °C day. On the training data it looks perfect. On the one question that matters, it is badly wrong.

```
|                       |                       |
|                       |                    .  |
|                    o  |                   .o  |                    o
|                  *..  |                 .*    |                 .*.
|                ...    |                ..     |                 . .
|               o*      |               o*      |               o*   .
|             ..        |             ...       |               .    .
|           *.*         |           *.*         |           *.*.
|         ..            |          ..           |         ...
|       *.o             |       *.o.            |       *.o
|     ..                |     ...               |      ..
|   .o*                 |   .o*                 |    o*
|*.*.                   |*.*                    |*.*..
|.                      |                       |
+---------------------  +---------------------  +---------------------
  degree 1: underfit      degree 2: good fit      degree 7: overfit
```

*Figure 9.3: The café data drawn three ways. Stars are training days, o marks the held-out test days, and dots are the model's curve. The straight line runs below the hot days; the gentle curve follows the data; the degree-7 curve passes through every star and then droops at the hot end, far below the 32 °C test day in the top-right corner.*

The pattern is general, and it gives you a diagnostic:

| Training error | Validation error | Diagnosis | What to try |
|---|---|---|---|
| High | High | Underfitting | A more flexible model, better features |
| Low | Much higher | Overfitting | A simpler model, regularization, more data |
| Low | Low, close to training | Good fit | Check on the test set, then ship |

*Table 9.3: Reading the two error numbers together tells you which direction to move.*

```
 error
   |
   |\                                            /
   | \                                         /   validation
   |  \                                      /     error
   |   \                                  _/
   |    `.                             _-'
   |      `-._                    _.-'
   |          `--..__________..--'
   |  \                 ^
   |   `.          sweet spot:
   |     `-._      stop here
   |         `--..__
   |                `---..___________________   training error
   +-------------------------------------------------- complexity
      underfitting        |        overfitting
```

*Figure 9.4: The classic picture. As complexity grows, training error keeps falling, but validation error falls and then rises. The best model sits at the bottom of the validation curve.*

> **Analogy:** Underfitting is a weather forecaster who always predicts "mild": too simple to ever be badly wrong or usefully right. Overfitting is a student who memorized last year's exam word for word, then meets new questions.

The same curve appears when you train for longer instead of making the model bigger. Early in training, both errors fall. Train too long on a small dataset and the model starts memorizing, so the validation error turns upward while the training error keeps dropping. That observation leads directly to one of the simplest fixes, early stopping, below.

## Bias and variance: the dartboard

Statisticians describe the two failure modes with two words.

> **Definition — Bias (statistical):** Systematic error from a model that is too simple or makes wrong assumptions, so it misses in the same direction again and again, like the straight line that always underestimates the hot days.

> **Definition — Variance (statistical):** How much a model's predictions would change if it were trained on a different sample of data. High variance means the model is jumpy and sensitive to the particular examples it saw, which is the signature of overfitting.

Picture throwing darts. Bias is how far the center of your cluster is from the bullseye. Variance is how spread out your darts are.

```
               LOW VARIANCE              HIGH VARIANCE
            +---------------+          +---------------+
            |               |          |  x         x  |
   LOW      |      xxx      |          |       x       |
   BIAS     |      xox      |          | x     o    x  |
            |      xxx      |          |          x    |
            |               |          |    x          |
            +---------------+          +---------------+
            +---------------+          +---------------+
            |  xxx          |          | x      x      |
   HIGH     |  xxx          |          |    x          |
   BIAS     |   x   o       |          | x     o       |
            |               |          |  x            |
            |               |          |       x       |
            +---------------+          +---------------+
```

*Figure 9.5: The bias–variance dartboard. The o is the bullseye (the truth); each x is one model trained on a different sample of data. Top left is the goal. Bottom left is a too-simple model, consistently wrong. Top right is an overfit model, right on average but wildly scattered.*

In the café example, the straight line has high bias: train it on any eight days you like and it will still underestimate hot days. The degree-7 curve has high variance: swap out one or two training days and its predictions at 32 °C would jump around wildly, because it bends itself to fit whatever eight points it is given.

> **Definition — Bias–variance tradeoff:** The classic tension in model building. Making a model more flexible lowers its bias but raises its variance; the best model balances the two for the amount of data you have.

The amount of data matters a lot. With 8 training days, a degree-7 curve is hopeless. With 8,000 days covering every kind of weather, a flexible model has enough evidence to tell real patterns from noise. This is one reason "more data" is the most reliable fix for overfitting, and one reason AI labs collect so much of it.

> **Watch out:** "Bias" now has three different meanings in this book. In Chapter 8 it was a parameter (the intercept of a line). Here it is statistical bias: systematic error. In Chapter 11 and Chapter 58 it is social bias: unfair treatment of groups of people. Always check which one a writer means.

### A twist: double descent

For decades the U-shaped curve of Figure 9.4 was the whole story. Then deep learning broke it. Modern neural networks often have far more parameters than training examples, enough to memorize the training set completely, and yet they generalize well.

In 2019, researchers led by Mikhail Belkin described "double descent," and a team from OpenAI and Harvard (Nakkiran and colleagues) showed it across many deep learning setups. As model size grows, test error first follows the classic U: down, then up as the model becomes just big enough to memorize the training data. But keep growing the model far past that point and test error comes down again, often lower than before.

> **Definition — Double descent:** The surprising finding that test error can fall, rise and then fall again as models grow far beyond the size needed to fit the training data exactly. It shows that the classic bias–variance picture is incomplete for very large models.

Why this happens is still debated. One popular intuition is that among all the ways a huge model could fit the training data, training tends to find smooth, simple ones. Chapter 13 returns to this. For now, the lesson is that "bigger means more overfitting" is not a safe rule for neural networks, while "always measure on held-out data" remains completely safe.

> **At the frontier (2026):** Frontier language models are trained on tens of trillions of tokens, mostly seeing each document only about once, so classic overfitting to the training set is rarely their main problem. Instead the evaluation worries have moved: memorizing rare passages word for word (a privacy and copyright issue, see Chapter 11), benchmark contamination, and models learning to please graders rather than to be right (see Chapter 20). The habits in this chapter, held-out data, honest baselines and suspicion of too-good scores, are exactly what labs apply to those newer problems.

## Regularization: keeping models simple on purpose

If overfitting comes from too much flexibility, one fix is to make flexibility cost something.

> **Definition — Regularization:** Any technique that discourages unnecessary complexity in order to reduce overfitting, such as penalizing large weights, limiting tree depth, stopping training early or adding noise during training.

The most common version adds a penalty to the loss for large weights. Training then has to balance two goals: fit the data, and keep the weights small.

> **Definition — L1 and L2 regularization:** Adding a penalty for large weights to the loss. L2 (also called ridge) adds the sum of squared weights and shrinks all weights toward zero; L1 (also called lasso) adds the sum of absolute weights and tends to push unhelpful weights to exactly zero, which removes those features.

A worked example. Two models each have a training MSE of 4.0. Model A has weights 2 and −1. Model B has weights 40 and −38: two huge numbers that nearly cancel, a typical sign of a model contorting itself to fit noise. With an L2 penalty strength of 0.1:

- Model A's penalty is `0.1 × (2² + (−1)²) = 0.1 × 5 = 0.5`, so its total loss is 4.0 + 0.5 = **4.5**.
- Model B's penalty is `0.1 × (40² + (−38)²) = 0.1 × (1,600 + 1,444) = 304.4`, so its total loss is **308.4**.

Gradient descent will strongly prefer Model A. The penalty strength (0.1 here) is a hyperparameter: too small and it does nothing, too large and it squashes the model into underfitting.

> **Analogy:** Regularization is a word limit on an essay. It forces you to keep only what matters instead of padding with every passing thought. It is Occam's razor, the old principle that simpler explanations are usually better, enforced by math.

Other common forms:

> **Definition — Early stopping:** Halting training when the validation error stops improving, even though the training error could still go down. It catches the moment in Figure 9.4 just before memorization sets in.

> **Definition — Dropout:** A regularization trick for neural networks that randomly switches off a fraction of the network's units during each training step, so no single unit can become a crutch. Chapter 13 covers it.

> **Definition — Data augmentation:** Creating extra training examples by changing existing ones in ways that should not change the answer, such as flipping, cropping or brightening a photo, or paraphrasing a sentence.

Early stopping is easy to picture with numbers. Here is an illustrative validation loss after each epoch of training:

| Epoch | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Validation loss | 0.90 | 0.62 | 0.48 | 0.41 | 0.38 | **0.37** | 0.38 | 0.41 | 0.45 | 0.50 |

*Table 9.4: An illustrative early-stopping run. Validation loss bottoms out at epoch 6 and then climbs as the model starts memorizing. Keep the epoch-6 version of the model.*

In practice people usually wait a few epochs past the best one (in case it was a temporary bump), then roll back to the best saved version.

Data augmentation deserves a special mention, because it directly attacks the shortcut problem. If you randomly brighten and darken your Teachable Machine photos during training, the model can no longer use lighting as a shortcut, and must look at your hand. Real image models are trained with many such variations.

And the most powerful regularizer of all is simply more data. With more varied examples, there is less room for the model to memorize accidents.

## Cross-validation: don't trust one lucky split

A single validation set has a weakness: it is one particular slice of data, and some slices are easier than others. Cross-validation rotates the role of validation set through the whole dataset.

> **Definition — Cross-validation (k-fold):** Cutting the data into k equal parts called folds, then training k times, each time holding out a different fold for validation and training on the rest, and finally averaging the k scores. Five and ten folds are common.

```mermaid
flowchart TD
  DATA["Dataset cut into 5 folds"] --> R1["Round 1: test on fold 1,<br/>train on folds 2 to 5"]
  DATA --> R2["Round 2: test on fold 2,<br/>train on the rest"]
  DATA --> R3["Round 3: test on fold 3"]
  DATA --> R4["Round 4: test on fold 4"]
  DATA --> R5["Round 5: test on fold 5"]
  R1 --> AVG["Average the 5 scores<br/>and note their spread"]
  R2 --> AVG
  R3 --> AVG
  R4 --> AVG
  R5 --> AVG
```

*Figure 9.6: Five-fold cross-validation. Every example is used for validation exactly once and for training four times.*

Here is a real result you can reproduce in Colab later in this chapter. The Wisconsin breast cancer dataset, which ships free with the scikit-learn library, contains 569 tumors described by 30 measurements taken from images of cell samples, each labeled malignant (212) or benign (357). Five-fold cross-validation of a logistic regression model gives these accuracies, each measured on about 114 tumors the model did not train on:

| Fold | 1 | 2 | 3 | 4 | 5 | Average |
|---|---|---|---|---|---|---|
| Accuracy | 98.2% | 98.2% | 97.4% | 97.4% | 99.1% | **98.1%** |

*Table 9.5: Five-fold cross-validation on the breast cancer dataset. The scores range from 97.4% to 99.1%, so any single split could have given a slightly flattering or slightly harsh number.*

Two things come out of this that a single split cannot give you: a more reliable average, and a sense of how much the score moves from one slice of data to another. If two models' averages differ by less than that spread, you should be cautious about calling one better.

> **Analogy:** Cross-validation is rotating which friend is the taste-tester, so one person's quirky palate does not decide the recipe.

Cross-validation should also be stratified when classes are unbalanced, so that every fold has the same share of positive cases.

### Time series: never train on the future

For data that unfolds over time, such as sales, prices or electricity demand, random folds would let the model train on Thursday and be tested on Wednesday. That is time leakage. Instead, walk forward through time.

> **Definition — Walk-forward validation:** Testing a forecasting model by repeatedly training on everything up to a point in time and predicting the next period, then moving the point forward and repeating. Also called backtesting.

```mermaid
flowchart LR
  W1["Train: Jan to Jun<br/>Test: Jul"] --> W2["Train: Jan to Jul<br/>Test: Aug"]
  W2 --> W3["Train: Jan to Aug<br/>Test: Sep"]
  W3 --> W4["Train: Jan to Sep<br/>Test: Oct"]
  W4 --> AV["Average the<br/>4 monthly errors"]
```

*Figure 9.7: Walk-forward validation. Each test month comes strictly after its training data, exactly as it will in real use.*

One practical limit: cross-validation multiplies the cost of training by k. That is fine for a model that trains in seconds. Nobody cross-validates a frontier language model whose single training run costs a fortune; labs rely on carefully held-out evaluation sets instead.

## The confusion matrix: counting every kind of mistake

So far we have mostly measured how wrong a model is with a single number. For classification, a single number hides the most important question: which mistakes is it making? A classifier can be wrong in two very different ways, and in most real problems one way is far worse than the other.

Take a yes-or-no model and call "yes" the positive class (sick, spam, fraud, malignant) and "no" the negative class. Every prediction falls into one of four boxes.

> **Definition — True positive (TP):** The model said yes and the answer really was yes, such as a sick person correctly flagged by a test.

> **Definition — False positive (FP):** The model said yes but the answer was no: a false alarm, such as a healthy person told they might be sick. Statisticians call it a Type I error.

> **Definition — False negative (FN):** The model said no but the answer was yes: a miss, such as a sick person sent home. Statisticians call it a Type II error.

> **Definition — True negative (TN):** The model said no and the answer really was no, such as a healthy person correctly cleared.

> **Definition — Confusion matrix:** A table that counts a classifier's predictions by type: true positives, false positives, false negatives and true negatives for a yes-or-no task, or every combination of actual and predicted class for a task with more classes.

### A worked medical test

A screening test for a rare disease is given to 1,000 people. Ten of them actually have the disease. The test correctly flags 9 of the 10 sick people, and it also wrongly flags 50 of the 990 healthy people.

```
                          WHAT THE TEST SAYS
                      Positive          Negative
                 +----------------+----------------+
   ACTUALLY      |  TP = 9        |  FN = 1        |    10 sick
   SICK          |  caught        |  missed        |
                 +----------------+----------------+
   ACTUALLY      |  FP = 50       |  TN = 940      |   990 healthy
   HEALTHY       |  false alarm   |  cleared       |
                 +----------------+----------------+
                    59 flagged       941 cleared       1,000 total
```

*Figure 9.8: The confusion matrix for the screening test. Rows are the truth, columns are the test's verdict. Every one of the 1,000 people lands in exactly one box.*

```mermaid
pie title Where the 1,000 people landed
    "True negatives: 940" : 940
    "False positives: 50" : 50
    "True positives: 9" : 9
    "False negatives: 1" : 1
```

*Figure 9.9: The same 1,000 people as a pie. The sick people (the two thinnest slices, 10 in total) are almost invisible, which is exactly why a single "accuracy" number can mislead.*

Now let us compute every standard metric from these four numbers.

**Accuracy** is the share of all predictions that were right.

> **Definition — Accuracy:** The share of all predictions that were correct: (TP + TN) ÷ total. It is easy to understand and badly misleading when one class is rare.

Accuracy = (9 + 940) ÷ 1,000 = 949 ÷ 1,000 = **94.9%**. Sounds good. Now consider a "test" that ignores the patient entirely and always says "healthy." It gets all 990 healthy people right and all 10 sick people wrong: accuracy = 990 ÷ 1,000 = **99.0%**. The useless test beats the real one on accuracy.

> **Definition — Class imbalance:** When one category vastly outnumbers another, such as 10 sick people among 1,000, or a handful of fraudulent payments among millions of normal ones. It makes accuracy misleading and calls for other metrics.

The same trap appears everywhere rare events matter. If 1 in 1,000 card payments is fraud, a "fraud detector" that never flags anything is 99.9% accurate and catches zero fraud. So we need metrics that look at the positive class directly.

**Precision** asks: when the test says "positive," how often is it right?

> **Definition — Precision:** Of everything the model flagged as positive, the share that truly was positive: TP ÷ (TP + FP). It answers "when it cries wolf, how often is there a wolf?"

Precision = 9 ÷ (9 + 50) = 9 ÷ 59 = **15.3%**. Only about 1 in 7 people who test positive are actually sick. This is the base-rate effect you met with Bayes' rule in Chapter 6: when a disease is rare, even a fairly good test produces more false alarms than true finds, simply because there are so many more healthy people to make mistakes on.

**Recall** asks: of all the people who really are sick, how many did the test catch?

> **Definition — Recall:** Of all the real positives, the share the model caught: TP ÷ (TP + FN). Also called sensitivity or the true positive rate. It answers "how many of the wolves did it spot?"

Recall = 9 ÷ (9 + 1) = **90%**. The always-healthy "test" has a recall of 0%, which exposes it immediately.

**Specificity** is recall's mirror image for the negative class.

> **Definition — Specificity:** Of all the real negatives, the share correctly left alone: TN ÷ (TN + FP). A test with high specificity rarely raises false alarms on healthy people.

Specificity = 940 ÷ (940 + 50) = 940 ÷ 990 = **94.9%**.

> **Definition — False positive rate:** Of all the real negatives, the share wrongly flagged: FP ÷ (FP + TN). It equals 1 minus specificity.

False positive rate = 50 ÷ 990 = **5.1%**. Notice the gap between a 5.1% false positive rate and 15.3% precision. Only 5% of healthy people get a false alarm, but because there are 990 healthy people and only 10 sick ones, those false alarms swamp the true ones.

**F1** combines precision and recall into one number that is only high if both are high.

> **Definition — F1 score:** A single number combining precision and recall, calculated as their harmonic mean: 2 × precision × recall ÷ (precision + recall). It is high only when both are high, so a model cannot score well by maximizing one and ignoring the other.

F1 = 2 × 0.153 × 0.90 ÷ (0.153 + 0.90) = 0.275 ÷ 1.053 = **0.26**. A plain average of 15.3% and 90% would be about 53%, which hides the terrible precision. The harmonic mean drags the score toward the weaker of the two.

| Metric | Formula | Question it answers | Screening test | Always "healthy" |
|---|---|---|---|---|
| Accuracy | (TP + TN) ÷ all | How often is it right overall? | 94.9% | 99.0% |
| Precision | TP ÷ (TP + FP) | When it says yes, is it right? | 15.3% | undefined (never says yes) |
| Recall | TP ÷ (TP + FN) | Does it catch the real cases? | 90.0% | 0% |
| Specificity | TN ÷ (TN + FP) | Does it leave negatives alone? | 94.9% | 100% |
| False positive rate | FP ÷ (FP + TN) | How often are negatives falsely flagged? | 5.1% | 0% |
| F1 | 2PR ÷ (P + R) | Are precision and recall both good? | 0.26 | 0 |

*Table 9.6: Every standard classification metric for the screening test, next to the useless always-healthy "test." Only accuracy is fooled.*

> **Key idea:** With rare events, accuracy lies. Always ask for the confusion matrix, or at least for precision and recall, before trusting a classifier.

### Precision or recall: which matters more?

You usually cannot have both at maximum, and the right balance depends entirely on what each kind of mistake costs.

- **Cancer screening, airport bag scans, smoke alarms:** a miss can be catastrophic, while a false alarm costs a follow-up test or a second look. Favor **recall**.
- **Spam filters:** a real email from your bank hidden in the spam folder is worse than one more spam message in your inbox. Favor **precision**.
- **Automatically blocking a card payment:** a missed fraud costs money, but blocking a real customer at the checkout costs goodwill and sales. Both matter, so tune carefully.
- **Song recommendations:** neither mistake costs much. Almost any balance is fine.

```mermaid
quadrantChart
    title Which mistake hurts more?
    x-axis Cheap false alarms --> Costly false alarms
    y-axis Cheap misses --> Costly misses
    quadrant-1 Need high precision and recall
    quadrant-2 Favor recall
    quadrant-3 Either metric is fine
    quadrant-4 Favor precision
    Cancer screening: [0.2, 0.9]
    Airport bag scan: [0.15, 0.8]
    Spam filter: [0.8, 0.25]
    Song recommendations: [0.3, 0.15]
    Card fraud blocking: [0.7, 0.75]
    Court evidence tool: [0.9, 0.6]
```

*Figure 9.10: Where some applications sit by the cost of each kind of mistake. Top left: misses are expensive, so favor recall. Bottom right: false alarms are expensive, so favor precision.*

> **Analogy:** Precision versus recall is like fishing with a net. A huge, fine net catches every fish (high recall) but also boots and seaweed (low precision). A small net cast by a picky fisher keeps only fish (high precision) but misses many (low recall).

### Real counts from a real dataset

Here is the confusion matrix from an actual model, which you can reproduce exactly in Colab at the end of this chapter. Using the breast cancer dataset from the cross-validation section, we hold out 25% of the tumors as a test set (143 tumors: 53 malignant, 90 benign), train a logistic regression on the other 426, and call "malignant" the positive class. With the default threshold of 0.5:

| | Model says malignant | Model says benign |
|---|---|---|
| **Actually malignant (53)** | TP = 49 | FN = 4 |
| **Actually benign (90)** | FP = 1 | TN = 89 |

*Table 9.7: A real confusion matrix: logistic regression on 143 held-out tumors from the Wisconsin breast cancer dataset, threshold 0.5.*

Work out the metrics yourself before reading on. Accuracy = (49 + 89) ÷ 143 = 138 ÷ 143 = **96.5%**. Precision = 49 ÷ (49 + 1) = **98.0%**. Recall = 49 ÷ (49 + 4) = **92.5%**. F1 = 2 × 0.980 × 0.925 ÷ (0.980 + 0.925) = **0.95**.

That is a strong model. But look at the FN box: 4 malignant tumors were called benign. In a screening setting, that is the number a doctor cares about most. Compare the dumbest possible baseline, which always says "benign": it scores 62.9% accuracy (90 of 143) and catches zero cancers. And look at the training accuracy, 98.8%, against the test accuracy of 96.5%: a small, normal gap, not a sign of serious overfitting.

What if we lower the threshold so the model flags a tumor as malignant whenever it estimates even a 10% chance? Then: TP = 52, FN = 1, FP = 6, TN = 84. Recall rises to 52 ÷ 53 = **98.1%**, precision falls to 52 ÷ 58 = **89.7%**, and accuracy actually drops slightly to 95.1%. We traded five more false alarms for three fewer missed cancers. For a screening tool, a doctor would probably take that deal. Accuracy alone would have told you not to.

> **Watch out:** This dataset is a classic teaching set, not a medical device. Real clinical AI must be tested on patients from many hospitals, on the equipment and populations where it will be used, and approved by regulators (see Chapter 52). A 96.5% score on 143 tumors from one source says little about performance elsewhere.

### More than two classes

For tasks with more than two classes, the confusion matrix simply grows. Here is a hypothetical one for a Teachable Machine model with three classes, tested on 20 new images of each:

| Actual \ Predicted | Thumbs up | Thumbs down | Nothing |
|---|---|---|---|
| **Thumbs up (20)** | 18 | 1 | 1 |
| **Thumbs down (20)** | 3 | 15 | 2 |
| **Nothing (20)** | 0 | 1 | 19 |

*Table 9.8: A three-class confusion matrix. The diagonal holds the correct predictions; everything off the diagonal is a specific kind of confusion.*

Accuracy is the diagonal divided by the total: (18 + 15 + 19) ÷ 60 = 52 ÷ 60 = 86.7%. But the table tells you much more. Recall for "thumbs down" is only 15 ÷ 20 = 75%, and its most common mistake is being read as "thumbs up." That points straight at a fix: record more thumbs-down examples from more angles. Precision and recall can be computed for each class separately and then averaged, which is called macro-averaging.

## Thresholds, ROC curves and AUC

Most classifiers do not output yes or no. They output a probability or score, and a threshold turns it into a decision (Chapter 8). Every threshold gives a different confusion matrix. Sliding the threshold is how you trade false alarms for misses.

### The threshold game

Here are 20 emails scored by a spam model, with the truth alongside:

| Spam (8 emails) | 0.95 | 0.90 | 0.85 | 0.80 | 0.70 | 0.55 | 0.45 | 0.30 | | | | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Not spam (12 emails)** | 0.75 | 0.60 | 0.50 | 0.40 | 0.35 | 0.25 | 0.20 | 0.15 | 0.10 | 0.08 | 0.05 | 0.02 |

*Table 9.9: Model scores for 20 emails. Most spam scores high and most normal mail scores low, but there is overlap in the middle.*

Flag as spam everything scoring at or above the threshold, and count:

| Threshold | TP | FN | FP | TN | Precision | Recall | False positive rate |
|---|---|---|---|---|---|---|---|
| 0.1 | 8 | 0 | 9 | 3 | 47% | 100% | 75% |
| 0.3 | 8 | 0 | 5 | 7 | 62% | 100% | 42% |
| 0.4 | 7 | 1 | 4 | 8 | 64% | 88% | 33% |
| 0.5 | 6 | 2 | 3 | 9 | 67% | 75% | 25% |
| 0.6 | 5 | 3 | 2 | 10 | 71% | 63% | 17% |
| 0.7 | 5 | 3 | 1 | 11 | 83% | 63% | 8% |
| 0.8 | 4 | 4 | 0 | 12 | 100% | 50% | 0% |
| 0.9 | 2 | 6 | 0 | 12 | 100% | 25% | 0% |

*Table 9.10: Sliding the threshold. A low threshold catches all spam but flags many good emails; a high threshold flags only certain spam but lets half of it through.*

So which threshold is best? It depends on costs, not on the model. Suppose a spam email reaching your inbox costs 1 unit of annoyance, while a real email lost in the spam folder costs 10 units. The total cost at each threshold is `1 × FN + 10 × FP`:

- At 0.5: 1 × 2 + 10 × 3 = **32**.
- At 0.7: 1 × 3 + 10 × 1 = **13**.
- At 0.8: 1 × 4 + 10 × 0 = **4**.
- At 0.9: 1 × 6 + 10 × 0 = **6**.

The cheapest choice is 0.8. Change the costs and the best threshold moves. This is how real teams pick thresholds: by putting a price on each kind of mistake.

> **Analogy:** A threshold is the sensitivity dial on a smoke alarm. Set it too sensitive and it shrieks every time you make toast (false positives). Set it too lax and it stays quiet during a real fire (false negatives).

### The ROC curve

If you plot the result of every threshold at once, you get a picture of the model's whole range of trade-offs.

> **Definition — ROC curve:** A graph of the true positive rate (recall) against the false positive rate as the threshold slides from strict to lenient. The name comes from "receiver operating characteristic," a term from World War II radar engineering.

```
 1.0 |                 #C##########################
     |              ####                    ....
     |           B###                  .....
     |        ####                 ....
     | ########                ....
 0.5 |A#                  .....
     |#               ....
     |#           ....
     |#      .....
     |#  ....
 0.0 |#..
     +---------------------------------------------
      0.0       0.25       0.5        0.75       1.0
```

*Figure 9.11: The ROC curve for the 20 emails. Vertical axis: true positive rate (recall). Horizontal axis: false positive rate. A is the strict threshold 0.8, B is 0.5, C is the lenient 0.3. The dotted diagonal is a coin flip. The more the curve hugs the top-left corner, the better the model.*

> **Definition — AUC (Area Under the ROC Curve):** A single score from 0.5 to 1.0 summarizing the ROC curve. It equals the chance that the model gives a randomly chosen positive example a higher score than a randomly chosen negative one. 0.5 is a coin flip; 1.0 is perfect ranking.

That second description of AUC gives you a way to compute it by hand. There are 8 spam emails and 12 normal ones, so there are 8 × 12 = 96 spam-versus-normal pairs. For each pair, check whether the spam email got the higher score. The top four spam scores (0.95, 0.90, 0.85 and 0.80) beat all 12 normal emails: 48 wins. The spam email at 0.70 beats 11 (it loses to the 0.75). The one at 0.55 beats 10, the one at 0.45 beats 9, and the one at 0.30 beats 7. Total wins: 48 + 11 + 10 + 9 + 7 = 85 out of 96, so **AUC = 0.885**. The real breast cancer model scores an AUC of 0.996: it almost always ranks a malignant tumor above a benign one.

AUC is useful because it does not depend on any single threshold. It measures how well the model ranks, and leaves the threshold decision for later.

### When positives are rare: precision–recall curves

ROC curves have a blind spot. The false positive rate divides by the number of negatives, which can be enormous. Imagine a fraud model scanning 1,000,000 legitimate payments and 1,000 frauds. A false positive rate of just 1% sounds tiny, and the ROC curve will look superb. But 1% of a million is 10,000 false alarms, against at most 1,000 real frauds. Precision would be below 10%.

> **Definition — Precision–recall curve:** A graph of precision against recall across all thresholds. When positives are rare, it shows the false-alarm problem much more clearly than an ROC curve.

For fraud, disease screening, safety incidents and other rare-event problems, ask for the precision–recall curve, or at least for precision at the recall level you need.

> **Try it:** Ask your chatbot: "My fraud model has an AUC of 0.98. Fraud is 0.1% of transactions. At a threshold where recall is 80%, the false positive rate is 2%. Out of 1,000,000 transactions, how many alerts will my team review, and what share will be real fraud?" Check its arithmetic: 800 real frauds caught, about 19,980 false alarms, so roughly 4% of alerts are real.

## Measuring models that predict numbers

For regression, the confusion matrix does not apply. Instead we measure the size of the misses. Chapter 8 introduced MSE (mean squared error) and MAE (mean absolute error) as losses for training. Here they serve as report cards, joined by three more.

> **Definition — RMSE (Root Mean Squared Error):** The square root of the mean squared error. It puts the error back into the original units (dollars, degrees), while still weighting big misses heavily.

> **Definition — R² (coefficient of determination):** The share of the variation in the true values that the model explains. 1 means perfect; 0 means no better than always predicting the average; below 0 means worse than that.

> **Definition — MAPE (Mean Absolute Percentage Error):** The average miss as a percentage of the true value. Easy to explain to non-specialists, but it breaks down when true values are near zero.

A worked example. A house-price model makes five predictions (in thousands of dollars):

| House | Actual | Predicted | Error | Absolute error | Squared error | Percent error |
|---|---|---|---|---|---|---|
| 1 | 300 | 320 | +20 | 20 | 400 | 6.7% |
| 2 | 450 | 430 | −20 | 20 | 400 | 4.4% |
| 3 | 250 | 270 | +20 | 20 | 400 | 8.0% |
| 4 | 600 | 540 | −60 | 60 | 3,600 | 10.0% |
| 5 | 400 | 410 | +10 | 10 | 100 | 2.5% |

*Table 9.11: Five house-price predictions and their errors.*

- **MAE** = (20 + 20 + 20 + 60 + 10) ÷ 5 = 130 ÷ 5 = **26**, so the model is off by $26,000 on average.
- **MSE** = (400 + 400 + 400 + 3,600 + 100) ÷ 5 = 4,900 ÷ 5 = **980** (in "thousands of dollars squared," a unit nobody can picture).
- **RMSE** = square root of 980 = **31.3**, so about $31,300. RMSE is higher than MAE because the one big miss on house 4 counts extra.
- **MAPE** = (6.7 + 4.4 + 8.0 + 10.0 + 2.5) ÷ 5 = **6.3%**.
- **R²**: the average actual price is 400. The squared distances of the actual prices from that average are 100², 50², 150², 200² and 0², which add up to 75,000. The model's squared errors add up to 4,900. R² = 1 − 4,900 ÷ 75,000 = **0.935**: the model explains about 93.5% of the variation in prices.

Now the baseline. A "model" that always predicts the average, $400,000, has an MAE of 100 and an RMSE of about 122.5, and an R² of exactly 0. Our model's MAE of 26 is about four times better. That comparison is far more informative than "MAE = 26" alone.

| Metric | Best for | Watch out for |
|---|---|---|
| MAE | Explaining to anyone: "off by $26,000 on average" | Treats one huge miss the same as several small ones |
| RMSE | When big misses are especially bad | Dominated by a few large errors |
| MAPE | Comparing across scales (cheap and expensive items) | Explodes when true values are near zero |
| R² | "How much better than guessing the average?" | Can look high on data with a strong trend even when errors are large in dollars |

*Table 9.12: Choosing a regression metric.*

> **Watch out:** In a spreadsheet, the RSQ function returns the squared correlation between two columns, which is not always the same as the R² of your model's predictions. Compute R² directly as 1 minus the sum of squared errors divided by the sum of squared differences from the mean (Exercise 5 shows the formulas).

## Baselines: is it better than doing something dumb?

Every evaluation needs a comparison point, and the first one should be embarrassingly simple.

> **Definition — Baseline:** A simple reference model that any real model must beat, such as "always predict the most common class," "always predict the average" or "tomorrow will be the same as today."

You have already met several baselines in this chapter. The always-benign tumor "model" scores 62.9% accuracy. The always-average house price model scores R² = 0. The flat line in the café example had a test MSE of 491. Each one turned a lonely number into a meaningful comparison.

Good baselines depend on the problem:

| Problem | Natural baseline |
|---|---|
| Classification | Always predict the most common class |
| Regression | Always predict the training average |
| Forecasting | Tomorrow equals today, or this week equals the same week last year |
| Recommendations | Recommend the most popular items |
| Text classification | A simple keyword rule, or a small logistic regression on word counts |
| A new chatbot feature | The same task done with a smaller, cheaper model, or by a person |

*Table 9.13: Baselines for common problems. In forecasting especially, simple baselines are notoriously hard to beat.*

> **Key idea:** A score with no baseline is not a result. "96.5% accurate" means little until you know that guessing gets 62.9%; "MAE of 26" means little until you know the dumb model gets 100.

## Tuning hyperparameters without cheating

Chapter 8 introduced hyperparameters, the settings you choose before training: the learning rate, the depth of a decision tree, the strength of a regularization penalty. Choosing them well can matter as much as choosing the algorithm.

> **Definition — Hyperparameter tuning:** Systematically trying different hyperparameter settings and keeping the one that scores best on validation data (or in cross-validation), never on the test set.

There are three main strategies.

> **Definition — Grid search:** Trying every combination from a list of values for each hyperparameter, such as every pairing of 3 tree depths with 3 learning rates.

> **Definition — Random search:** Trying randomly chosen combinations of hyperparameter values. It often finds good settings faster than a grid, because it tests more distinct values of the settings that matter most.

> **Definition — Bayesian optimization:** A smarter search that uses the results so far to guess which untried settings are most promising, and tries those next.

The cost adds up quickly. A grid of 3 depths × 3 learning rates is 9 combinations. With 5-fold cross-validation, that is 9 × 5 = 45 training runs. Add two more hyperparameters with 5 values each and the grid has 3 × 3 × 5 × 5 = 225 combinations, or 1,125 runs. This is why random search, popularized in a 2012 paper by James Bergstra and Yoshua Bengio, is often preferred: with a fixed budget of, say, 60 runs, you sample the space broadly instead of exhaustively.

```mermaid
flowchart TD
  Q["Frame the question:<br/>which mistakes are costly?"] --> S["Split: train, validation, test<br/>or cross-validation plus test"]
  S --> BL["Score a dumb baseline"]
  BL --> TU["Train candidates and tune<br/>hyperparameters on validation"]
  TU --> PK["Pick one model<br/>and one threshold"]
  PK --> TS["Open the test set once"]
  TS --> RP["Report metrics with<br/>error margins"]
  RP --> MO["Monitor after launch<br/>for drift"]
```

*Figure 9.12: An honest evaluation workflow. Every choice happens before the test set is opened, and monitoring continues after launch.*

> **Watch out:** The most common way to accidentally cheat is to tune on the test set: try something, check the test score, adjust, check again. After a dozen rounds, your test set has become a second validation set, and your final score is optimistic. If you have peeked, be honest about it, or collect a fresh test set.

## When the world changes: distribution shift

Even a perfectly evaluated model can fail later, because the test set was a snapshot of the past.

> **Definition — Distribution shift:** When the data a model meets in real use differs from the data it was trained and tested on, such as a model trained on one hospital's patients being used at another hospital, or a shopping model trained before a pandemic being used during one. Also called data drift.

The chest X-ray models above are a distribution-shift story: excellent on test images from their own hospitals, worse elsewhere. Consumer behavior shifted sharply in 2020 and broke many forecasting models overnight. Your chatbot faces a version of this every day: its training data ends at a cutoff date, and the world keeps moving.

The defenses are to test on data from the places and times where the model will actually be used, to monitor its performance after launch, and to retrain when the numbers slip (see Chapter 10 for the basics of monitoring, and Chapter 31 for how AI products are evaluated after launch).

## Benchmarks and Goodhart's law

So far we have evaluated one model on one problem. Science and industry also need to compare many models built by many teams. That is what benchmarks are for.

> **Definition — Benchmark:** A standard dataset plus a standard scoring method that many teams use to compare their models, such as MNIST for handwritten digits or a set of exam questions for chatbots.

> **Definition — Leaderboard:** A public ranking of models by their benchmark scores.

Benchmarks have driven much of AI's progress. MNIST (1998), with its 70,000 small images of handwritten digits, was the standard test of image recognition for years. ImageNet (2009), with about 14 million labeled images, set up the yearly challenge in which, in 2012, the AlexNet neural network cut the top-5 error rate to about 15.3%, against about 26% for the runner-up. That single benchmark result launched the deep learning era (see Chapter 7 and Chapter 14).

But a benchmark is a test set that the whole world gets to look at, again and again, for years. Every published paper that tunes its approach to do slightly better on the same test set is, collectively, a small step of tuning on the test set. In 2019, a team led by Benjamin Recht built a fresh ImageNet-style test set, following the original recipe as closely as they could, and re-tested many published models. Accuracy dropped by roughly 11 to 14 percentage points, although the ranking of the models mostly held. Part of each model's original score was fitted to the particular quirks of the original test images.

> **Definition — Goodhart's law:** "When a measure becomes a target, it ceases to be a good measure." Named after the economist Charles Goodhart, who made the point about monetary policy in 1975; this popular phrasing comes from the anthropologist Marilyn Strathern.

Goodhart's law is everywhere once you notice it. Schools judged on test scores start teaching to the test. Call centers judged on call length start hanging up on difficult callers. And AI models judged on benchmarks get better at benchmarks, which is not always the same as getting better at the job.

### Benchmarks in the chatbot era

Chatbot benchmarks have shortened this life cycle dramatically.

```mermaid
flowchart LR
  A["New benchmark<br/>models score low"] --> B["Labs and researchers<br/>optimize for it"]
  B --> C["Scores climb fast"]
  C --> D["Saturation, contamination<br/>and harness tricks"]
  D --> E["Scores stop tracking<br/>real ability"]
  E --> F["A harder benchmark<br/>is released"]
  F --> A
```

*Figure 9.13: The life cycle of a benchmark. Each turn of this loop now takes a year or two at the frontier.*

> **Definition — Benchmark saturation:** When the best models score near the maximum on a benchmark, so it can no longer tell them apart.

A few examples from the research for this book, all as of October 2026:

- **Saturation.** MMLU, a 2020 multiple-choice exam across 57 school and professional subjects, was a headline benchmark for years and is now saturated for frontier models. Humanity's Last Exam, a set of 2,500 expert-level questions released in January 2025, was designed to be much harder: frontier models scored under 10% at launch. By October 2026 the best text-only score reported by the independent evaluator Artificial Analysis was about 61%.
- **Wrong answers in the answer key.** Test sets have label errors too. An audit by the research group FutureHouse suggested that about 30% of the answers in Humanity's Last Exam's text-only chemistry and biology questions might be wrong, which prompted a rolling, corrected version. A model that "fails" a question with a wrong answer key may be right.
- **Harness dependence.** The same model can score very differently depending on the testing setup, or harness: the instructions, tools and memory it is given. On the ARC-AGI-3 puzzle benchmark, OpenAI's GPT-6 Astra reportedly scored 62.7% under the standard harness and 99.9% under a harness that let it keep its reasoning state between steps. Same model, same puzzles, very different headline numbers.

> **Definition — Evaluation harness:** The software setup used to run a benchmark: how questions are phrased, how many attempts are allowed, what tools and memory the model gets, and how answers are graded. Different harnesses can produce very different scores for the same model.

Goodhart's law even helps explain hallucination. A 2025 OpenAI paper by Adam Kalai and colleagues argued that most benchmarks grade answers only as right or wrong, with no credit for "I don't know." Under that scoring rule, guessing always beats admitting uncertainty, so models trained and selected to score well learn to bluff. The metric shaped the behavior (see Chapter 18).

> **At the frontier (2026):** Leading labs and evaluators now fight Goodhart's law on several fronts: removing known benchmark questions from training data, keeping private test sets that are never published, building benchmarks that refresh over time, publishing exact harness settings, measuring human preferences in blind side-by-side comparisons (as LMArena does), and testing on realistic work tasks rather than exam questions. Chapter 24 explains how to read model benchmarks, Chapter 31 how product teams build their own evaluations, and Chapter 57 how safety evaluations work.

> **Try it:** Ask your chatbot: "Which AI benchmarks have become saturated or contaminated, and why does that make headline scores less meaningful?" Then ask it to name one way it might itself have seen benchmark questions during training. Notice whether it is appropriately uncertain about its own training data.

## A checklist for any model claim

Everything in this chapter boils down to questions you can ask about any model, whether it is your own spreadsheet model, a vendor's sales pitch or a chatbot launch announcement.

1. **Measured on what?** Was the score measured on data the model never trained on? How was the test set chosen?
2. **How big was the test?** How many examples, and what is the margin of error?
3. **Any leaks?** Could any feature, duplicate or future information have sneaked in? Is the result suspiciously good?
4. **Which mistakes?** What do the confusion matrix, precision and recall look like, especially for the rare, important class?
5. **Compared to what?** What does a dumb baseline score? What does the current method score?
6. **Which threshold, and why?** Was it chosen based on the real costs of each mistake?
7. **Tuned on the test?** Were the hyperparameters and design choices made without peeking at the test set?
8. **Does it transfer?** Was it tested on data from the place, time and population where it will be used?
9. **Is the benchmark still meaningful?** Is it saturated, possibly contaminated, or sensitive to the harness?
10. **Who measured it?** Are the numbers self-reported by the company selling the model, or independently reproduced?

> **Key idea:** Good evaluation is mostly skepticism, organized. Ask what the number was measured on, what it is compared to, and which mistakes it hides.

## Real evaluation in code: Google Colab

You can run everything in this chapter yourself. Open colab.research.google.com, start a new notebook, and paste each cell below into its own code cell (Chapter 8 explains how to use Colab).

The first cell reproduces the café overfitting experiment and draws all the curves.

```python
import numpy as np                         # math on whole lists of numbers
import matplotlib.pyplot as plt            # charts

temp   = np.array([10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32])   # feature: temperature in C
drinks = np.array([22, 20, 27, 29, 36, 38, 47, 49, 60, 63, 75, 80])   # label: iced drinks sold

test_days  = [2, 5, 8, 11]                                  # positions of the 4 held-out days
train_days = [i for i in range(12) if i not in test_days]   # the other 8 days are for training

def mse(pred, true):                       # mean squared error, as in Chapter 8
    return np.mean((pred - true) ** 2)

print("degree   train MSE    test MSE")
for degree in [0, 1, 2, 3, 5, 7]:          # 0 = flat line (the average), 7 = very wiggly curve
    curve = np.polynomial.Polynomial.fit(temp[train_days], drinks[train_days], degree)  # training
    train_error = mse(curve(temp[train_days]), drinks[train_days])   # score on days it studied
    test_error  = mse(curve(temp[test_days]),  drinks[test_days])    # score on unseen days
    print(f"{degree:6d} {train_error:11.2f} {test_error:11.2f}")
    xs = np.linspace(10, 32, 200)                            # smooth x-values for drawing
    plt.plot(xs, curve(xs), label=f"degree {degree}")

plt.scatter(temp[train_days], drinks[train_days], color="black", label="training days")
plt.scatter(temp[test_days], drinks[test_days], color="red", marker="x", s=80, label="test days")
plt.ylim(0, 110); plt.xlabel("temperature (C)"); plt.ylabel("iced drinks sold"); plt.legend(); plt.show()
```

In plain words: the first lines load the math and chart toolkits and type in Table 9.1. The `test_days` list marks which four days are held out. The small `mse` function computes mean squared error. The loop fits a curve of each degree using only the training days, then scores it on the training days and on the test days, and prints both. The last lines draw every curve over the data, with the test days as red crosses. You should see exactly the numbers in Table 9.2, ending with a degree-7 test MSE of 206.51, and a chart where the wiggliest curves swing far away from the red crosses.

The second cell trains a real classifier and evaluates it every way this chapter describes. Colab already has the scikit-learn library and the breast cancer dataset built in.

```python
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.dummy import DummyClassifier
from sklearn.metrics import (confusion_matrix, precision_score, recall_score,
                             f1_score, accuracy_score, roc_auc_score)

data = load_breast_cancer()                  # 569 tumors, 30 measurements each
X = data.data                                # the features
y = (data.target == 0).astype(int)           # label: 1 = malignant (the positive class), 0 = benign

X_train, X_test, y_train, y_test = train_test_split(   # hold out 25% as a test set
    X, y, test_size=0.25, random_state=42, stratify=y)  # stratify keeps the class mix the same

model = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000))  # scale, then logistic regression
model.fit(X_train, y_train)                  # training uses ONLY the training set
probs = model.predict_proba(X_test)[:, 1]    # probability of malignant for each test tumor

def report(threshold):
    pred = (probs >= threshold).astype(int)  # turn probabilities into yes/no decisions
    tn, fp, fn, tp = confusion_matrix(y_test, pred).ravel()
    print(f"threshold {threshold}: TP={tp} FN={fn} FP={fp} TN={tn} | "
          f"accuracy={accuracy_score(y_test, pred):.3f} precision={precision_score(y_test, pred):.3f} "
          f"recall={recall_score(y_test, pred):.3f} F1={f1_score(y_test, pred):.3f}")

for t in [0.5, 0.2, 0.1]:                    # try three thresholds
    report(t)
print("ROC AUC:", round(roc_auc_score(y_test, probs), 3))

baseline = DummyClassifier(strategy="most_frequent").fit(X_train, y_train)   # always guesses benign
print("baseline accuracy:", round(baseline.score(X_test, y_test), 3))

scores = cross_val_score(make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000)), X, y, cv=5)
print("5-fold accuracies:", np.round(scores, 3), " mean:", round(scores.mean(), 3))
```

In plain words: the `import` lines load the tools. The data is loaded and the label is flipped so that "malignant" counts as positive. `train_test_split` sets aside 25% of the tumors as a test set, with a fixed random seed (`random_state=42`) so you get the same split as this book, and `stratify=y` so both parts have the same share of malignant tumors. The model scales each measurement to a comparable range and then fits a logistic regression, using only the training tumors. The `report` function turns probabilities into decisions at a given threshold, builds the confusion matrix and prints the metrics. Then the cell prints the AUC, the score of an always-benign baseline, and five-fold cross-validation scores.

You should see TP=49, FN=4, FP=1, TN=89 at threshold 0.5; TP=51, FN=2, FP=3, TN=87 at 0.2; TP=52, FN=1, FP=6, TN=84 at 0.1; an AUC of 0.996; a baseline accuracy of 0.629; and fold accuracies of about 0.982, 0.982, 0.974, 0.974 and 0.991. Software versions occasionally shift a count by one; the lessons do not change.
