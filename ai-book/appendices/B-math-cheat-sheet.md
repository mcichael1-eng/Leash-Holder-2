# Appendix B: Math Cheat Sheet

This appendix collects every formula used in the book in one place. Each one appears three ways: in plain words, in symbols, and with one tiny worked example you can check on a calculator. Chapter 5 and Chapter 6 teach the core math from scratch; the compute and memory rules of thumb are worked through in Chapters 19, 23, 33 and 37; Appendix A covers units, prefixes and reference numbers such as chip specifications.

How to read it. Multiplication is written ×, division ÷, and "x squared" as `x^2`. `10^25` means 10 to the 25th power. `sqrt()` is the square root, `e` is about 2.718, `exp(x)` means e to the power x, `ln` is the natural logarithm and `log10` the base-10 logarithm. Vectors are lists in square brackets, like [3, 4]. N is a model's number of parameters and D its number of training tokens. The symbol ≈ means "about". Prices and hardware figures in examples are illustrative unless a chapter gives them as facts.

## Notation at a glance

| Symbol | Read it as | Example |
|---|---|---|
| `a × b` | a times b | 3 × 4 = 12 |
| `a ÷ b` | a divided by b | 12 ÷ 4 = 3 |
| `x^2`, `a^n` | x squared, a to the n-th power | `2^5` = 32 |
| `sqrt(x)` | square root of x | sqrt(25) = 5 |
| `e`, `exp(x)` | Euler's number (about 2.718), e to the power x | exp(1) ≈ 2.718 |
| `ln(x)`, `log10(x)`, `log2(x)` | natural log, base-10 log, base-2 log | log10(1,000) = 3 |
| `[a1, a2, a3]` | a vector (ordered list) | [3, 120, 15] |
| `a · b` | dot product of vectors a and b | [1, 2] · [3, 4] = 11 |
| `P(A)` | probability of A | P(heads) = 0.5 |
| P(A given B) | probability of A when B is known to be true (often written with a vertical bar) | P(glasses given book) ≈ 0.67 |
| `m × n` (shape) | m rows and n columns | a 3 × 4 matrix holds 12 numbers |
| N, D, C | parameters, training tokens, training compute in FLOPs | N = 70 billion |

## Numbers and scale

| Rule | In plain words | In symbols | Tiny example |
|---|---|---|---|
| Power of ten | A 1 followed by n zeros | `10^n` | `10^6` = 1,000,000 |
| Negative power of ten | One divided by a power of ten | `10^-n = 1 ÷ 10^n` | `10^-3` = 0.001 |
| Scientific notation | A number from 1 to 10 times a power of ten | `a × 10^n` | 2,500,000 = 2.5 × 10^6 |
| Multiplying big numbers | Multiply the front numbers, add the exponents | `(a × 10^m) × (b × 10^n) = (a × b) × 10^(m + n)` | (2 × 10^3) × (3 × 10^4) = 6 × 10^7 |
| Dividing big numbers | Divide the front numbers, subtract the exponents | `(a × 10^m) ÷ (b × 10^n) = (a ÷ b) × 10^(m − n)` | (8 × 10^9) ÷ (2 × 10^3) = 4 × 10^6 |
| Order of magnitude | How many factors of ten separate two numbers | `log10(big ÷ small)` | a billion versus a million: log10(1,000) = 3 orders |
| Percent of | Multiply by the percentage divided by 100 | `p% of x = (p ÷ 100) × x` | 40% of 989 = 395.6 |
| Percent change | The change divided by the starting value, times 100 | `(new − old) ÷ old × 100` | 50 to 65: 15 ÷ 50 × 100 = +30% |
| Times bigger | Divide new by old | `factor = new ÷ old` | 3.8 × 10^25 ÷ 3.15 × 10^23 ≈ 120 times |
| Rate, total, time | Total equals rate times time | `total = rate × time` | 50 tokens per second × 20 s = 1,000 tokens |
| Unit conversion | Multiply by fractions worth 1 until the units cancel | `x × (new units ÷ old units)` | 1 day = 24 × 60 × 60 = 86,400 s |

| Prefix | Symbol | Value | Prefix | Symbol | Value |
|---|---|---|---|---|---|
| kilo | k | `10^3` | milli | m | `10^-3` |
| mega | M | `10^6` | micro | µ | `10^-6` |
| giga | G | `10^9` | nano | n | `10^-9` |
| tera | T | `10^12` | | | |
| peta | P | `10^15` | | | |
| exa | E | `10^18` | | | |

| Scale anchor | Worked out | Result |
|---|---|---|
| A million seconds | 1,000,000 ÷ 86,400 | about 11.6 days |
| A billion seconds | 1,000,000,000 ÷ (86,400 × 365) | about 31.7 years |
| A trillion seconds | 1,000,000,000,000 ÷ (86,400 × 365) | about 31,700 years |

## Growth, exponentials and logarithms

| Rule | In plain words | In symbols | Tiny example |
|---|---|---|---|
| Exponent | Multiply a number by itself n times | `a^n` | `2^5` = 2 × 2 × 2 × 2 × 2 = 32 |
| Compound growth | Multiply by the growth factor once per period | `final = start × factor^periods` | 5 times per year for 3 years: `5^3` = 125 times |
| Growth from a percentage | The factor is 1 plus the rate as a decimal | `final = start × (1 + r)^t` | +49% per year for 2 years: `1.49^2` ≈ 2.22 times |
| Doubling time to yearly factor | Count the doublings in a year, then raise 2 to that | `yearly factor = 2^(12 ÷ doubling months)` | doubling every 5.2 months: 12 ÷ 5.2 ≈ 2.3 doublings, and `2^2.3` ≈ 4.9 per year |
| Rule of 70 | Doubling time is about 70 divided by the percent growth per period | `doubling time ≈ 70 ÷ r%` | 7% per year doubles in about 10 years |
| Exponential decay | Multiply by a number below 1 each period | `final = start × f^t`, with f below 1 | halving 3 times: `0.5^3` = 0.125 |
| Euler's number | The natural growth constant | `e ≈ 2.718`, `exp(x) = e^x` | `e^2` ≈ 7.389, `e^0` = 1 |
| Logarithm (base 10) | The power of 10 that gives the number; roughly, its count of zeros | `log10(10^n) = n` | log10(1,000) = 3, log10(0.1) = −1 |
| Logarithm (base 2) | How many doublings give the number | `log2(2^n) = n` | log2(8) = 3 |
| Natural logarithm | The power of e that gives the number | `ln(e^x) = x` | ln(1) = 0, ln(0.5) ≈ −0.693, ln(0.1) ≈ −2.303 |
| Log of a product | Logs turn multiplying into adding | `log(a × b) = log(a) + log(b)` | log10(100 × 1,000) = 2 + 3 = 5 |
| Log of a quotient | Logs turn dividing into subtracting | `log(a ÷ b) = log(a) − log(b)` | log10(1,000 ÷ 10) = 3 − 1 = 2 |
| Log of a power | The exponent comes out in front | `log(a^k) = k × log(a)` | log10(`10^25`) = 25 × 1 = 25 |
| Change of base | Divide by the log of the new base | `log2(x) = ln(x) ÷ ln(2)` | log2(1,024) = 6.931 ÷ 0.693 = 10 |
| Log scale | Each equal step on the axis multiplies the value | ticks at 1, 10, 100, 1,000 | "times 5 per year" plots as a straight line |
| Power law | One quantity varies as another to a fixed power; a straight line on a log-log plot | `y = c × x^k`, so `log(y) = log(c) + k × log(x)` | area = side^2 has slope 2 on a log-log plot |

## Vectors and matrices

| Rule | In plain words | In symbols | Tiny example |
|---|---|---|---|
| Vector | An ordered list of numbers; its length is its dimension | `a = [a1, a2, ..., an]` | a house as [3 bedrooms, 120 square meters, 15 years] |
| Add vectors | Add matching entries | `a + b = [a1 + b1, a2 + b2, ...]` | [1, 2] + [3, 1] = [4, 3] |
| Scale a vector | Multiply every entry by one number | `k × a = [k × a1, k × a2, ...]` | 2 × [1, 2] = [2, 4] |
| Element-wise (Hadamard) product | Multiply matching entries and keep them as a list; nothing is added up (Chapter 5) | `a ⊙ b = [a1 × b1, a2 × b2, ...]` | [2, 3] ⊙ [5, 1] = [10, 3] |
| Length (magnitude) | Square the entries, add, take the square root | `length(a) = sqrt(a1^2 + a2^2 + ...)` | [3, 4]: sqrt(9 + 16) = 5 |
| Distance | The length of the difference | `distance(a, b) = length(a − b)` | [1, 2] to [4, 6]: length of [3, 4] = 5 |
| Dot product | Multiply matching entries, then add | `a · b = a1 × b1 + a2 × b2 + ...` | [2, 1, 3] · [1.5, 4, 0.5] = 3 + 4 + 1.5 = 8.5 |
| Dot product cost | n multiplications and n − 1 additions | `≈ 2 × n FLOPs` | two 4,096-number vectors: about 8,192 FLOPs |
| Cosine similarity | Dot product divided by both lengths; 1 same direction, 0 unrelated, −1 opposite | `cos = (a · b) ÷ (length(a) × length(b))` | [3, 4] and [6, 8]: 50 ÷ (5 × 10) = 1 |
| Normalize | Divide a vector by its own length to make its length 1 | `a ÷ length(a)` | [3, 4] becomes [0.6, 0.8] |
| Embedding analogy | Subtract one meaning, add another | `king − man + woman ≈ queen` | toy vectors: [1, 1] − [0, 1] + [0, −1] = [1, −1] |
| Matrix shape | Rows first, then columns | `m × n` holds m × n numbers | 3 students × 4 quizzes: 12 numbers |
| Matrix times vector | Each output is one row dotted with the vector | `(m × n) times (length n) gives (length m)` | rows [1, 2] and [3, 4] times [5, 6] = [17, 39] |
| Matrix times matrix | Each entry is a row of the left matrix dotted with a column of the right | `C[i, j] = row i of A · column j of B` | rows [1, 2], [3, 4] times rows [5, 6], [7, 8] = rows [19, 22], [43, 50] |
| Shape rule | Inner sizes must match; outer sizes give the answer | `(m × n) times (n × p) gives (m × p)` | (2 × 3)(3 × 2) gives 2 × 2; (2 × 3)(2 × 3) is not allowed |
| Order matters | Swapping the matrices usually changes the answer | `A × B ≠ B × A` | B × A above gives rows [23, 34], [31, 46] |
| Transpose | Flip a matrix so its rows become its columns; transposing a product reverses the order (Chapter 5) | `(A^T)[i, j] = A[j, i]`, `(A × B)^T = B^T × A^T` | rows [1, 2, 3], [4, 5, 6] become rows [1, 4], [2, 5], [3, 6] |
| Matrix multiplication cost | m × n × p multiply-adds | `≈ 2 × m × n × p FLOPs` | two 4,096 × 4,096 matrices: about 1.4 × 10^11 FLOPs |
| Tensor size | Multiply all the sizes in the shape | `count = size1 × size2 × ...` | 32 × 224 × 224 × 3 = 4,816,896 numbers |
| Embedding table size | One row of numbers per vocabulary token | `vocabulary × hidden size` | 100,000 × 4,096 ≈ 4.1 × 10^8 numbers |

## Functions, lines and layers

| Rule | In plain words | In symbols | Tiny example |
|---|---|---|---|
| Straight line | Output is slope times input plus intercept | `y = w × x + b` | taxi fare: 2 × 5 miles + 3 = $13 |
| Slope from two points | Rise over run | `w = (y2 − y1) ÷ (x2 − x1)` | (1, 5) and (3, 9): 4 ÷ 2 = 2 |
| Intercept from one point | Subtract slope times x from y | `b = y1 − w × x1` | 5 − 2 × 1 = 3 |
| Weighted sum | Multiply each input by its weight, add them, add the bias | `y = w1 × x1 + w2 × x2 + ... + b` | 20,000 × 3 + 1,500 × 100 − 1,000 × 20 + 50,000 = 240,000 |
| Composition | Feed one function's output into another | `g(f(x))` | tip on a taxi fare: 1.2 × (2 × 5 + 3) = 15.6 |
| Linear steps collapse | Two linear steps are one linear step | `w2 × (w1 × x + b1) + b2 = (w2 × w1) × x + (w2 × b1 + b2)` | 3 × (2 × x) + 1 = 6 × x + 1 |
| ReLU | Negatives become zero; positives pass through | `ReLU(x) = max(0, x)` | ReLU(−2) = 0, ReLU(3) = 3 |
| Sigmoid | Squeezes any number into the range 0 to 1 | `sigmoid(x) = 1 ÷ (1 + e^(−x))` | sigmoid(0) = 0.5, sigmoid(2) ≈ 0.881 |
| One layer | Multiply by a weight matrix, add a bias, apply an activation | `output = activation(W × x + b)` | x = [1, 2] gives [0, 2, 0] in Chapter 5's worked layer |
| Parameters in a dense layer | Weights plus one bias per output | `m × n + m` | 2 inputs to 3 outputs: 9; a 4,096-square layer: 16,781,312 |
| Line of best fit, slope | Co-movement of x and y divided by the spread of x | `w = sum((x − mean x) × (y − mean y)) ÷ sum((x − mean x)^2)` | quiz data (1,3), (2,5), (3,8), (4,9): 10.5 ÷ 5 = 2.1 |
| Line of best fit, intercept | The line passes through the two means | `b = mean y − w × mean x` | 6.25 − 2.1 × 2.5 = 1.0 |

## Probability

| Rule | In plain words | In symbols | Tiny example |
|---|---|---|---|
| Probability by counting | Ways to get it divided by all equally likely outcomes | `P(A) = favorable ÷ total` | rolling a 6: 1 ÷ 6 ≈ 0.167 |
| Valid range | Every probability lies from 0 to 1 | `0 ≤ P(A) ≤ 1` | a fair coin landing heads: 0.5 |
| Not (complement) | One minus the probability that it happens | `P(not A) = 1 − P(A)` | not rolling a 6: 1 − 1/6 = 5/6 |
| And, for independent events | Multiply | `P(A and B) = P(A) × P(B)` | two heads: 0.5 × 0.5 = 0.25 |
| Or | Add, then subtract the overlap | `P(A or B) = P(A) + P(B) − P(A and B)` | heart or king: 13/52 + 4/52 − 1/52 = 16/52 |
| Conditional probability | Narrow to cases where B is true, then ask how often A is | P(A given B) = `P(A and B) ÷ P(B)` | glasses given book: 0.20 ÷ 0.30 ≈ 0.67 |
| Total probability | Add up every route to B | P(B) = P(B given A) × P(A) + P(B given not A) × P(not A) | positive test: 0.9 × 0.01 + 0.09 × 0.99 = 0.0981 |
| Bayes' rule | Update a belief with evidence, respecting the base rate | P(A given B) = P(B given A) × P(A) ÷ P(B) | sick given positive: 0.9 × 0.01 ÷ 0.0981 ≈ 0.092 |
| Bayes with natural frequencies | True cases among all positives, counted in a crowd | `true positives ÷ (true positives + false positives)` | 1,000 people: 9 ÷ (9 + 89) ≈ 9% |
| Expected value | Each outcome times its probability, added up | `E = sum(outcome × probability)` | a fair die: (1 + 2 + ... + 6) × 1/6 = 3.5 |
| Bernoulli (yes/no) variable | One trial that gives 1 with probability p and 0 otherwise; its mean is p and its variance p × (1 − p) (Chapter 6) | `P(X = 1) = p`, `P(X = 0) = 1 − p`, `E[X] = p`, `Var(X) = p × (1 − p)` | p = 0.8: mean 0.8, variance 0.8 × 0.2 = 0.16 |
| Distribution | All probabilities in a distribution add to 1 | `sum of P = 1` | 0.92 + 0.03 + 0.02 + 0.01 + 0.02 = 1 |
| Sentence probability | Multiply each token's probability given everything before it | P(w1, w2, w3) = P(w1) × P(w2 given w1) × P(w3 given w1, w2) | 0.05 × 0.01 × 0.2 = 0.0001 |
| Log-probability | Add logs instead of multiplying probabilities | `log P = log P(w1) + log P(w2 ...) + ...` | log10: −1.30 − 2 − 0.70 = −4.0 |
| Bigram estimate | How often b follows a, divided by how often a is followed by anything | P(b given a) = `count(a then b) ÷ count(a then anything)` | P(like given I) = 2 ÷ 3 in "I like tea. I like coffee. I drink tea." |

## Statistics

| Rule | In plain words | In symbols | Tiny example |
|---|---|---|---|
| Mean | Add everything, divide by the count | `mean = sum ÷ count` | nine salaries in thousands (Chapter 6's example): 40, 45, 50, 50, 55, 60, 65, 70, 80: 515 ÷ 9 ≈ 57.2 |
| Median | The middle value once sorted (average the two middle ones if the count is even) | middle of the sorted list | same list: 55 |
| Mode | The most common value | most frequent value | same list: 50 |
| Range | Largest minus smallest | `max − min` | 80 − 40 = 40 |
| Variance | Average squared distance from the mean | `mean((x − mean)^2)` | 2, 4, 4, 4, 5, 5, 7, 9: 32 ÷ 8 = 4 |
| Standard deviation | Square root of the variance, in the original units | `sd = sqrt(variance)` | sqrt(4) = 2 |
| z-score | How many standard deviations a value sits from the mean | `z = (x − mean) ÷ sd` | 184 cm with mean 170 and sd 7: z = 2 |
| 68–95–99.7 rule | Shares of a normal distribution within 1, 2 and 3 sd of the mean | `mean ± 1 sd`, `± 2 sd`, `± 3 sd` | mean 170, sd 7: about 68% between 163 and 177 cm |
| Percentile | The value that a given percentage of the data falls below | p50 = median; p99 = where the slowest 1% begins | p99 latency 30 s: 99% of requests finish faster |
| Correlation | How strongly two things move together in a straight line, from −1 to 1 | `r = sum((x − mean x)(y − mean y)) ÷ sqrt(sum((x − mean x)^2) × sum((y − mean y)^2))` | quiz data: 10.5 ÷ sqrt(5 × 22.75) ≈ 0.98 |
| Law of large numbers | The average of many independent repeats closes in on the expected value μ (Chapter 6) | `x_bar_n = (X_1 + X_2 + ... + X_n) ÷ n → μ` as n grows | fair coin, heads = 1: 7 heads in 10 flips averages 0.7; a typical 5,030 in 10,000 averages 0.503 |
| Error bar on an accuracy score | One standard deviation of a pass rate p measured on n questions | `sd ≈ sqrt(p × (1 − p) ÷ n)` | 80% on 400 questions: sqrt(0.16 ÷ 400) = 0.02, so about ±4 points at 95% confidence (two standard deviations, by the 68–95–99.7 rule) |
| Variance of a sum | Variances of independent quantities add (standard deviations do not), so an average of n values wobbles by σ ÷ sqrt(n); Cov is the covariance, 0 for independent quantities (Chapter 9) | `Var(X + Y) = Var(X) + Var(Y) + 2 × Cov(X, Y)`, `sd(average) = σ ÷ sqrt(n)` | two independent ±1.5-point margins: sqrt(1.5^2 + 1.5^2) ≈ 2.1 points, not 3 |
| Maximum likelihood | Choose the parameters θ that make the observed data most probable; for yes/no counts that is the observed share (Chapter 6) | `θ_MLE = argmax over θ of P(data given θ) = argmin over θ of (−sum over i of ln P(x_i given θ))` | 7 heads in 10 flips: p^7 × (1 − p)^3 is 0.00098 at p = 0.5 and peaks at p = 0.7 (0.00222) |

## From scores to tokens: softmax, sampling and loss

| Rule | In plain words | In symbols | Tiny example |
|---|---|---|---|
| Softmax | Raise e to each score, then divide by the total | `p_i = e^(s_i) ÷ sum of e^(s_j)` | scores [2, 1, 0.1]: 7.389, 2.718, 1.105 over 11.21 gives 0.659, 0.242, 0.099 |
| Shift makes no difference | Adding the same number to every score leaves softmax unchanged | `softmax(s + c) = softmax(s)` | [3, 2, 1.1] also gives 0.659, 0.242, 0.099 |
| Temperature | Divide every score by T before softmax | `p_i = e^(s_i ÷ T) ÷ sum of e^(s_j ÷ T)` | T = 0.5 gives 0.864, 0.117, 0.019; T = 2 gives 0.502, 0.304, 0.194 |
| Greedy decoding | Always take the most probable token | pick the largest `p_i` | Paris at 0.92 |
| Sampling with a random number | Lay probabilities end to end from 0 to 1; pick where a random number lands | token whose stretch contains r | stretches 0–0.92 Paris, 0.92–0.95 "the", 0.95–0.97 "a": r = 0.96 gives "a" |
| Top-p | Keep the most likely tokens until their total reaches p, then rescale | keep smallest top set with sum ≥ p, divide by that sum | 0.4, 0.3, 0.2, 0.1 with p = 0.8: keep three, giving 0.444, 0.333, 0.222 |
| Cross-entropy, one token | Minus the natural log of the probability given to the correct token | `loss = −ln(p_correct)` | p = 0.5: 0.693; p = 0.1: 2.303 |
| Cross-entropy, whole text | Average the per-token losses | `loss = mean(−ln(p_correct))` | 0.5, 0.25, 0.8, 0.9, 0.6: 2.919 ÷ 5 = 0.584 |
| Perplexity | e to the average loss: the effective number of equally likely choices | `perplexity = e^(average loss)` | `e^2.303` = 10; `e^0.693` = 2 |
| Bits of surprise | The same loss measured with base-2 logs | `bits = −log2(p_correct)` | p = 0.5: 1 bit; p = 0.25: 2 bits |
| InfoNCE (contrastive loss) | Cross-entropy in which the true partner must beat every decoy, with each similarity divided by a temperature τ first (Chapter 16) | `loss = −ln(e^(s_true ÷ τ) ÷ sum of e^(s_j ÷ τ))` | similarities 0.31 (true), 0.02, 0.05 with τ = 0.07: 83.8 ÷ (83.8 + 1.33 + 2.04) ≈ 0.96, so the loss is −ln(0.96) ≈ 0.04 |
| CLIP loss | InfoNCE across each row (each photo picks its caption) and down each column (each caption picks its photo), averaged (Chapter 16) | `CLIP loss = 0.5 × (average row loss + average column loss)` | Figure 16.2's batch: rows average 0.040, columns 0.041, so 0.5 × (0.040 + 0.041) ≈ 0.04 |
| ELBO (the VAE's objective) | Rebuild score minus a KL penalty for straying from the standard bell curve; it is never above the true log-probability, so raising it trains the model (Chapter 16) | `ELBO = E[ln p(x given z)] − KL(q(z given x) ‖ p(z))`; for each latent number, KL = `0.5 × (mean^2 + spread^2 − ln(spread^2) − 1)` | mean 1.5, spread 0.2: KL = 0.5 × (2.25 + 0.04 + 3.22 − 1) ≈ 2.25; with a rebuild term of −3.0, ELBO = −3.0 − 2.25 = −5.25 |

## Calculus and learning

| Rule | In plain words | In symbols | Tiny example |
|---|---|---|---|
| Slope by nudging | Change in output divided by a tiny change in input | `(f(x + h) − f(x)) ÷ h`, with h tiny | `x^2` at x = 3, h = 0.001: 0.006001 ÷ 0.001 = 6.001 |
| Partial derivative | Nudge one knob while holding the others still | slope for w with b fixed | loss `(w × 2 + b − 5)^2` at w = b = 1 is 4; nudging w to 1.001 gives about 3.992, so the slope is about −0.008 ÷ 0.001 = −8 |
| Gradient | The list of every knob's slope; it points uphill | `[slope for w, slope for b, ...]` | [−8, −4] |
| Chain rule | Multiply the slopes along a chain of steps | `slope of y for x = (slope of y for u) × (slope of u for x)` | u = 3 × x, y = `u^2`, at x = 1: 6 × 3 = 18 |
| Squared-error slope | The slope of an error squared is twice the error | slope of `error^2` = 2 × error | error −2: slope −4 |
| Gradient descent step | Move each knob against its slope, scaled by the learning rate | `new = old − learning rate × slope` | w = 1 − 0.05 × (−8) = 1.4 |
| Mean squared error | Average of squared prediction errors | `MSE = mean((prediction − actual)^2)` | errors 0.1, 0.2, −0.7, 0.4: 0.70 ÷ 4 = 0.175 |
| MSE slopes for a line | Average of 2 × error × x for w, and of 2 × error for b | `slope_w = mean(2 × error × x)`, `slope_b = mean(2 × error)` | quiz data at w = b = 0: −36.5 and −12.5 |
| Learning rate on a simple bowl | For loss `(x − c)^2`, each step multiplies the distance to the bottom by (1 − 2 × learning rate) | `distance_next = (1 − 2 × lr) × distance` | lr 0.1: × 0.8 each step; lr 1.0: bounces; lr 1.1: × −1.2, explodes |
| Cost of a training step | Backward pass is about twice the forward pass | forward 2N + backward 4N = 6N per training token | why training compute is 6 × N × D |

| Function | Its derivative | Check |
|---|---|---|
| A constant, such as 7 | 0 | a flat line |
| `w × x` | w | the taxi fare's slope is the per-mile price |
| `x^2` | 2 × x | at x = 3: 6 |
| `x^n` | `n × x^(n − 1)` | `x^3` at x = 2: 3 × 4 = 12 |
| `e^x` | `e^x` | at x = 0: 1 |
| `ln(x)` | 1 ÷ x | at x = 2: 0.5 |
| ReLU(x) | 0 for negative x, 1 for positive x | at x = 3: 1 |
| sigmoid(x) = s | s × (1 − s) | at x = 0: 0.5 × 0.5 = 0.25 |

## Classical machine learning and search

| Rule | In plain words | In symbols | Tiny example |
|---|---|---|---|
| Bias–variance decomposition | Expected squared error on new data is bias squared plus variance across training sets plus noise (Chapter 9) | `E[(y − f_hat(x))^2] = (E[f_hat(x)] − f(x))^2 + E[(f_hat(x) − E[f_hat(x)])^2] + σ^2` | lines predicting 74, 76, 73, 75, 77 where the truth is 80 and the noise variance 4: 25 + 2 + 4 = 31 |
| Information gain (tree split) | Entropy of the parent group minus the size-weighted entropy of the groups a question creates; the tree asks the question with the largest gain (Chapter 10) | `H = −sum over k of p_k × log2(p_k)`, `IG = H(parent) − sum over c of (n_c ÷ n) × H(c)` | 5 cancelled and 5 stayed (H = 1 bit); a split into 4 pure and 6 with 5 cancelled (H ≈ 0.65): IG = 1 − 0.6 × 0.65 ≈ 0.61 |
| Random forest prediction | Majority vote of the trees for a category, their average for a number; each split tries about the square root of the number of features (Chapter 10) | `y_hat = most common of f_1(x), ..., f_B(x)`; `y_hat = (1 ÷ B) × sum of f_b(x)`; `m ≈ sqrt(p)` | votes stays, stays, cancels, stays, cancels: stays; predictions 10, 12, 11, 13, 9: 11; 16 features: 4 per split |
| PCA directions and share kept | The principal directions are eigenvectors of the covariance matrix Σ; each eigenvalue λ is the variance along its direction (Chapter 10) | `Σ × v_j = λ_j × v_j`, `z = V_k^T × (x − μ)`, `share kept = λ_j ÷ sum of all λ` | variances 2 and 2, covariance 1.9: eigenvalues 3.9 and 0.1, so the first direction keeps 3.9 ÷ 4 = 97.5% |
| BM25, one query word | Rare-word weight times a repeat count that saturates, discounted for long documents; add it up over the query's words (Chapter 27) | `IDF × f × (k1 + 1) ÷ (f + k1 × (1 − b + b × len(D) ÷ avgdl))`, with `IDF = ln(1 + (N − n + 0.5) ÷ (n + 0.5))` | "refund" in 50 of 1,000 documents, said twice in an average-length document, k1 = 1.2, b = 0.75: 2.99 × 4.4 ÷ 3.2 ≈ 4.11 |

## Model and compute rules of thumb

| Rule | In plain words | In symbols | Tiny example |
|---|---|---|---|
| Inference cost per token | Each parameter does one multiply-add per token | `FLOPs per token ≈ 2 × N` | 70 billion parameters: 1.4 × 10^11 FLOPs |
| Mixture of experts | Use the active parameters for compute, the total for memory | `FLOPs per token ≈ 2 × N_active` | 49 billion active: about 10^11 FLOPs |
| Cost of an answer | Per-token cost times tokens generated | `≈ 2 × N × tokens` | 70B model, 500 tokens: 7 × 10^13 FLOPs |
| Training compute | Forward plus backward pass for every training token | `C ≈ 6 × N × D` | GPT-3: 6 × 1.75 × 10^11 × 3 × 10^11 ≈ 3.15 × 10^23 |
| Chinchilla ratio | Compute-optimal training uses about 20 tokens per parameter | `D ≈ 20 × N` | 70 billion parameters: about 1.4 trillion tokens |
| Compute-optimal size | Combine the two rules: C = 6 × N × (20 × N) = 120 × N^2 | `N = sqrt(C ÷ 120)`, `D = 20 × N` | C = `10^25`: N ≈ 2.9 × 10^11, D ≈ 5.8 × 10^12 |
| Cluster speed | Chips times peak speed times utilization (MFU, model FLOPs utilization: the share of peak speed actually achieved, Chapter 19) | `GPUs × peak FLOP/s × MFU` | 16,384 × 989 × 10^12 × 0.4 ≈ 6.5 × 10^18 FLOP/s |
| Training time | Total FLOPs divided by cluster speed | `time = C ÷ cluster speed` | 3.8 × 10^25 ÷ 6.5 × 10^18 ≈ 5.9 million s ≈ 68 days |
| GPU-hours | Number of chips times hours | `GPU-hours = GPUs × hours` | 16,384 × 1,632 h ≈ 26.7 million |
| Rental cost of a run | GPU-hours times the hourly price | `cost = GPU-hours × $ per GPU-hour` | 26.7 million × $2.50 ≈ $67 million (illustrative rate) |
| Tokens and words | One English token is about three-quarters of a word (varies by tokenizer and language) | `words ≈ 0.75 × tokens` | 1,000 tokens ≈ 750 words |
| API bill | Tokens in millions times the price per million, for input and output separately | `cost = tokens ÷ 1,000,000 × price per million` | 20,000 input tokens at $3 per million = $0.06 (illustrative price) |
| Cost per million tokens from GPU rent | Hourly price divided by tokens produced per hour | `$ per million = $ per GPU-hour ÷ (tokens per s × 3,600) × 1,000,000` | $3 per hour at 1,000 tokens per s: $0.83 |
| Energy per token | Power divided by tokens per second; 3,600 joules = 1 watt-hour | `J per token = watts ÷ tokens per s` | 1,500 W ÷ 2,000 tokens per s = 0.75 J; 500 tokens ≈ 375 J ≈ 0.1 Wh (assumed figures) |
| Arithmetic intensity | Math done per byte moved from memory | `FLOPs ÷ bytes moved` | decode for one user at 16 bits: each 2-byte weight is read once and used in one multiply-add (2 FLOPs), so 2 FLOPs ÷ 2 bytes = 1 FLOP per byte |
| Ridge point | Where a chip stops waiting on memory | `peak FLOP/s ÷ bandwidth` | H100: 989 × 10^12 ÷ 3.35 × 10^12 ≈ 295 FLOP per byte |

## Memory math

| Format | Bits per number | Bytes per parameter |
|---|---|---|
| FP32 | 32 | 4 |
| BF16 or FP16 | 16 | 2 |
| FP8 or INT8 | 8 | 1 |
| MXFP4 (with shared block scales) | about 4.25 | about 0.53 |
| FP4 or INT4 | 4 | 0.5 |

| Rule | In plain words | In symbols | Tiny example |
|---|---|---|---|
| Weight memory | Parameters times bytes per parameter | `memory = N × bytes per parameter` | 70 billion × 2 bytes = 140 GB |
| Chips needed to hold the weights | Divide by one chip's memory and round up | `ceiling(memory ÷ chip memory)` | 140 GB ÷ 80 GB = 1.75, so 2 H100s |
| Training memory | About 16 bytes per parameter with Adam in mixed precision: 2 for weights, 2 for gradients, 12 for a 32-bit master copy and two optimizer averages | `≈ 16 × N bytes`, before activations | 70 billion: 1.12 TB, at least 14 chips of 80 GB |
| KV cache per token | Keys and values, for every layer and key-value head | `2 × layers × KV heads × head size × bytes` | a 70B-class model with 80 layers, 8 KV heads of size 128, at 2 bytes: 2 × 80 × 8 × 128 × 2 = 327,680 bytes ≈ 0.33 MB |
| KV cache total | Per-token size times context length times conversations | `per token × tokens × users` | 0.33 MB × 128,000 tokens ≈ 42 GB for one long chat |
| Decode speed ceiling | Every weight is read once per generated token | `tokens per s ≤ bandwidth ÷ bytes of weights` | 4,800 GB/s ÷ 70 GB ≈ 69 tokens per second |
| Halving the precision | Half the bytes means half the memory and about twice the speed ceiling | `bytes ÷ 2`, `speed × 2` | 70B model, 4,800 GB/s chip: 140 GB and a ceiling of about 34 tokens/s at BF16; 70 GB and about 69 at FP8 |

## Reinforcement learning and preference training

| Rule | In plain words | In symbols | Tiny example |
|---|---|---|---|
| Markov decision process | States, actions, transition probabilities, rewards and a discount factor; the next state depends only on the current state and action, not the history (Chapter 48) | `MDP = (S, A, P, R, γ)`, with `P(s_(t+1) given s_t, a_t) = P(s_(t+1) given s_0, a_0, ..., s_t, a_t)` | "right" reaches B with probability 0.8 and slips back with 0.2; entering B pays 10: R(A, right) = 0.8 × 10 + 0.2 × 0 = 8 |
| Discounted return | All future rewards added up, each multiplied by γ once per step of waiting (Chapter 48) | `G_t = r_(t+1) + γ × r_(t+2) + γ^2 × r_(t+3) + ... = r_(t+1) + γ × G_(t+1)` | rewards 0, 0, 10 with γ = 0.9: 0 + 0.9 × 0 + 0.81 × 10 = 8.1 |
| State and action values | Expected return from a state (V), or from a state after a given first action (Q); V is the policy-weighted average of Q (Chapter 48) | `V_π(s) = E_π[G_t given s_t = s]`, `Q_π(s, a) = E_π[G_t given s_t = s, a_t = a]`, `V_π(s) = sum over a of (π(a given s) × Q_π(s, a))` | right 75% with Q = 8, left 25% with Q = 2: 0.75 × 8 + 0.25 × 2 = 6.5 |
| Bellman expectation equation | Value now = expected reward plus discounted value of the next state, averaged over the policy's choices and the world's chances (Chapter 48) | `V_π(s) = sum over a of π(a given s) × sum over s' of P(s' given s, a) × (R(s, a, s') + γ × V_π(s'))` | γ = 0.9, two actions at 0.5 each: 0.5 × (1 + 0.9 × 2) + 0.5 × (0.8 × 0.9 × 10) = 1.4 + 3.6 = 5.0 |
| Bellman optimality equation | The same, but take the best action instead of averaging over the policy (Chapter 48) | `V*(s) = max over a of sum over s' of P(s' given s, a) × (R(s, a, s') + γ × V*(s'))` | corridor square B: max(0.9 × 10, 0.9 × 8.1) = max(9, 7.29) = 9 |
| TD(0) update | Nudge a value toward the reward plus the discounted next value; the gap is the TD error δ (Chapter 48) | `δ_t = r_(t+1) + γ × V(s_(t+1)) − V(s_t)`, then `V(s_t) ← V(s_t) + α × δ_t` | V(A) = 5, V(B) = 8, reward 1, γ = 0.9, α = 0.1: δ = 1 + 7.2 − 5 = 3.2, new V(A) = 5.32 |
| Epsilon-greedy | The best-known action gets 1 − ε plus its share of the random picks; every other action gets ε divided by the number of actions (Chapter 48) | `π(best) = 1 − ε + ε ÷ (number of actions)`, `π(other) = ε ÷ (number of actions)` | two restaurants, ε = 0.1: 1 − 0.1 + 0.05 = 0.95 and 0.05 |
| Policy gradient theorem | The slope (∇_θ, the gradient for the policy's parameters θ) of the expected return J is the average of "make this action more likely" times how good the action was (Chapter 48) | `∇_θ J(θ) = E[sum over t of (∇_θ ln π_θ(a_t given s_t) × Q(s_t, a_t))]` | 50/50 policy with directions +0.5 (right) and −0.5 (left), Q = 10 and 2: 0.5 × (0.5 × 10) + 0.5 × (−0.5 × 2) = 2.0 |
| REINFORCE | Move the parameters along each action's "more likely" direction, scaled by its return minus a baseline (Chapter 48) | `θ ← θ + α × sum over t of ((G_t − b) × ∇_θ ln π_θ(a_t given s_t))` | Table 48.6, baseline 6: terms 2, 2, 1, 1 average 1.5; α = 0.1 moves θ from 0 to 0.15 |
| PPO clipped objective | Ratio of new to old probability times the advantage, with no extra credit for moving outside the window 1 − ε to 1 + ε (Chapter 20) | `L_CLIP = E[min(r × A, clip(r, 1 − ε, 1 + ε) × A)]` | r = 1.5, A = 2, ε = 0.2: min(3.0, 2.4) = 2.4 |
| GRPO objective | PPO's clipped term for every token (ρ is the token's new-to-old probability ratio), weighted by the answer's group advantage A_i, averaged over each answer's tokens and over the group, minus a KL leash with weight β (Chapter 21) | `J_GRPO = mean over the G answers of (mean over answer i's tokens of (min(ρ × A_i, clip(ρ, 1 − ε, 1 + ε) × A_i) − β × D_KL))` | A = +1.29, token ratio 1.3, ε = 0.2: the token counts as 1.2 × 1.29 ≈ 1.55, not 1.68 |

## Spreadsheet formulas

These work in both Google Sheets and Microsoft Excel. Type large numbers in scientific notation with E, so 175 billion is `175E9`. Each example assumes you first type its numbers into the cells the formula names: for the dot product, 2, 1, 3 in A1 to C1 and 1.5, 4, 0.5 in A2 to C2; for the line of best fit and correlation, the quiz data's x values (1 to 4) in A2 to A5 and its y values (3, 5, 8, 9) in B2 to B5; for matrix multiplication, the left matrix in A1:B2 and the right one in D1:E2, with the answer filling a 2 × 2 block.

| Task | Formula | Example result |
|---|---|---|
| Dot product | `=SUMPRODUCT(A1:C1, A2:C2)` | 2, 1, 3 and 1.5, 4, 0.5 give 8.5 |
| Vector length | `=SQRT(SUMSQ(A1:B1))` | 3, 4 gives 5 |
| Distance between two vectors | `=SQRT(SUMXMY2(A1:B1, A2:B2))` | 1, 2 and 4, 6 give 5 |
| Cosine similarity | `=SUMPRODUCT(A1:B1,A2:B2)/(SQRT(SUMSQ(A1:B1))*SQRT(SUMSQ(A2:B2)))` | 3, 4 and 6, 8 give 1 |
| Matrix multiplication | `=MMULT(A1:B2, D1:E2)` | fills in 19, 22, 43, 50 |
| Line of best fit | `=SLOPE(B2:B5, A2:A5)` and `=INTERCEPT(B2:B5, A2:A5)` | 2.1 and 1 for the quiz data |
| Correlation | `=CORREL(A2:A5, B2:B5)` | about 0.98 for the quiz data |
| Powers and roots | `=5^3`, `=POWER(2, 10)`, `=SQRT(25)` | 125, 1,024, 5 |
| Exponential and logs | `=EXP(2)`, `=LN(0.5)`, `=LOG10(1000)`, `=LOG(8, 2)` | 7.389, −0.693, 3, 3 |
| Softmax of A1:A3 | `=EXP(A1)/SUMPRODUCT(EXP($A$1:$A$3))` | 2, 1, 0.1 give 0.659 for the first |
| Typical value | `=AVERAGE(A1:A9)`, `=MEDIAN(A1:A9)`, `=MODE(A1:A9)` | 57.2, 55, 50 for the salary list |
| Spread | `=VAR.P(A1:A8)`, `=STDEV.P(A1:A8)` | 4 and 2 for 2, 4, 4, 4, 5, 5, 7, 9 |
| Percentile | `=PERCENTILE(A1:A100, 0.99)` | the p99 value |
| Random number from 0 to 1 | `=RAND()` | a new value on every recalculation |
| Training compute | `=6*175E9*300E9` | 3.15E+23 |
| Weight memory in GB | `=70E9*2/1E9` | 140 |
| Training time in days | `=3.8E25/(16384*989E12*0.4)/86400` | about 68 |
