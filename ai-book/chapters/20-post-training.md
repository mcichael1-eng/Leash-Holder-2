# Chapter 20: Post-Training: Turning a Text Predictor Into an Assistant

*This chapter shows you, step by step and with numbers you can check by hand, how a raw text predictor becomes the helpful, polite, careful assistant you talk to every day.*

## What you'll learn

- Why a freshly pretrained "base model" is not an assistant, and what has to be added before you can chat with it.
- How supervised fine-tuning teaches format, manners and persona from example conversations, and who writes those examples.
- How preference data and reward models turn "which answer is better?" into a number, worked through with real arithmetic.
- How RLHF with PPO works, including the KL "leash", walked through with a toy model you can compute on paper.
- How DPO and its cousins (IPO, KTO, ORPO, SimPO) get similar results without a separate reward model.
- How Constitutional AI, model specs and safety training shape a model's values, refusals and character.
- What goes wrong (sycophancy, reward hacking, verbosity, over-refusal), why it goes wrong, and how labs fight back.
- How distillation, synthetic data, LoRA and model merging fit in, and what the full post-training pipeline of a 2026 lab looks like as one diagram.

## Before you start

Chapter 18 (How a Large Language Model Works) explains tokens, probabilities, chat templates and system prompts, and Chapter 19 (Pretraining: Data, Scale and Scaling Laws) explains how a base model is made. Chapter 6 (The Math of AI, Part 2) gives you every math tool used here: if you remember that softmax turns scores into probabilities, that a logarithm turns multiplication into addition, and that training means nudging numbers downhill to shrink a loss, you are ready. Chapter 8 (Learning From Examples) introduces reinforcement learning in a paragraph; Chapter 48 covers it in depth. Chapter 21 picks up where this chapter ends, with reasoning models.

## From autocomplete to assistant

### What a base model actually does

Suppose you could open a raw, freshly pretrained model and type: "What is the capital of Japan?" You might expect "Tokyo." Instead you could easily get something like this:

```
What is the capital of Japan?
What is the capital of South Korea?
What is the capital of China?
Answer key: 1. Tokyo  2. Seoul  3. Beijing
```

The model is not broken. It is doing exactly what it was trained to do: continue a document in the most likely way. On the web, a line like "What is the capital of Japan?" most often appears inside a quiz, a worksheet or a list of trivia questions. So the most likely continuation is more questions.

> **Definition — Base model:** A language model straight out of pretraining. It continues text in the style of whatever it is given, but it does not reliably answer questions, follow instructions or behave like an assistant.

A base model knows an enormous amount. It has read trillions of tokens (Chapter 19), so the knowledge that Tokyo is Japan's capital is in there. What it lacks is a stable self. Give it the start of a forum rant and it becomes an angry poster. Give it the start of an encyclopedia entry and it becomes an encyclopedia. Give it the opening of a scam email and it will happily finish the scam. It has no idea that it is supposed to be "the assistant", that it should stop after answering, or that some requests deserve a "no".

> **Analogy:** A base model is a brilliant improv actor who has read every book in the library. Shout any opening line and it will play along in character. A chat model is the same actor after years of training as a customer-service professional: still talented, but now it stays on task, answers the actual question and knows when to say "I can't help with that."

Everything that happens between "base model" and "the assistant in your app" is called post-training.

> **Definition — Post-training:** All the training that happens after pretraining (supervised fine-tuning, preference learning, reinforcement learning, safety and character training) to turn a base model into a useful, safe product.

> **Definition — Alignment:** Making an AI system's goals and behavior match what its developers and users actually intend, including being helpful, being honest and avoiding harm.

Post-training adds three kinds of things:

1. **Format.** Conversations have turns. The assistant should answer the user, then stop. It should use the special tokens that mark roles (Chapter 18), and the exact syntax for calling tools such as web search.
2. **Behavior and values.** Following instructions. Being helpful without being harmful. Admitting uncertainty. Declining what it should decline, and not declining what it should not. Having a consistent personality.
3. **Sharpened skills.** Better math, code, writing and multi-step reasoning. Since 2024 this third job has grown enormously, because reinforcement learning on checkable tasks turned out to make models much stronger. That story is Chapter 21.

A useful shorthand that Anthropic popularized in 2021 is that an assistant should be **helpful, honest and harmless**. You will see these three goals pull against each other throughout this chapter: the most "helpful" answer to some requests is harmful, and the most "harmless" answer to many requests is a useless refusal.

Labs use the word *persona* for the consistent character the model plays. Your chatbot's tone, its habits ("Great question!"), its willingness to push back and its sense of humor are all shaped in post-training.

### The stages at a glance

Here is the whole journey in its simplest form. We will walk through each box in turn, then draw the full 2026 version at the end of the chapter.

```mermaid
flowchart LR
    A["Base model<br/>from pretraining"] --> B["Supervised<br/>fine-tuning"]
    B --> C["Preference tuning<br/>RLHF or DPO"]
    C --> D["Reinforcement learning<br/>on checkable tasks"]
    D --> E["Safety and<br/>character training"]
    E --> F["Evaluations and<br/>red teaming"]
    F --> G["The assistant<br/>in your app"]
```

*Figure 20.1: The main stages of post-training, from a base model to the assistant you chat with.*

> **Analogy:** Pretraining is reading every book in the library. Supervised fine-tuning is an apprenticeship, where you copy a master's work. Preference tuning is customer reviews: you learn what people like. Reinforcement learning on checkable tasks is a math teacher who marks only whether your final answer is right, so you must figure out the method yourself.

How much of the total effort goes into each stage? Historically, pretraining was by far the most expensive part, and post-training was a small add-on. That is changing. One public data point gives a sense of scale for one lab at one moment: DeepSeek reported that the final pretraining run of DeepSeek-V3 cost about $5.6 million in rented GPU time, and that the reasoning-focused reinforcement learning stage of DeepSeek-R1 cost about $294,000 (both figures cover only the final runs, not research, experiments or staff). Since then, labs have described steadily growing reinforcement learning budgets, and as of late 2026 post-training is a major share of the work at every frontier lab.

> **Key idea:** Pretraining decides what a model can know. Post-training decides who it is, how it behaves and how well it uses what it knows.

## Stage 1: Supervised fine-tuning, or learning by example

### What the data looks like

The first step is the most intuitive. You show the model thousands of example conversations in which the assistant behaves exactly as you want, and you train it to imitate them.

> **Definition — Fine-tuning:** Further training of an already-trained model on a smaller, targeted dataset, so that it changes its behavior or specializes in something.

> **Definition — SFT (Supervised Fine-Tuning):** Fine-tuning on examples of the desired input and output, such as a user's question paired with an ideal assistant answer. The model learns to imitate the examples.

> **Definition — Instruction tuning:** SFT on a large, varied collection of instructions ("summarize this", "write a poem about", "explain like I'm ten") paired with good responses, so the model learns to follow requests in general rather than one task.

One training example, called a demonstration, looks like this once it is laid out in a chat template (the format with special role tokens described in Chapter 18):

```
<|system|>    You are a helpful assistant.
<|user|>      My sourdough came out flat and dense. Why?
<|assistant|> A flat, dense loaf usually points to one of three things:
              1. A weak starter. It should double within 4-8 hours...
              2. Under-proofing...
              3. Too much water for your flour...
              Tell me your recipe and I can narrow it down.<|end|>
```

The training itself is the same next-token prediction used in pretraining (Chapter 19), with one twist. The model is only graded on the assistant's words. The system prompt and the user's message are there as context, but the model is not trained to predict them, because we do not want it to learn to write the user's half of the conversation.

> **Definition — Loss masking:** Ignoring some tokens when computing the training loss. In SFT, the system and user tokens are masked so that the model is graded only on how well it predicts the assistant's reply.

### Worked example: one SFT step on one token

Take the Japan example. After the template tokens for "the assistant is speaking now", the base model's probabilities for the first word of the reply might look like this (illustrative numbers):

| Next token | Base model | After SFT |
|---|---|---|
| " What" (start of another quiz question) | 0.35 | 0.01 |
| " Tokyo" | 0.20 | 0.90 |
| new line | 0.15 | 0.01 |
| " A" (as in "A: ...") | 0.10 | 0.02 |
| everything else | 0.20 | 0.06 |

The demonstration says the right token is " Tokyo." The training loss for that token is the cross-entropy from Chapter 6: minus the natural log of the probability the model gave to the right answer.

- Before SFT: loss = −ln(0.20) = 1.61.
- After SFT: loss = −ln(0.90) = 0.11.

Gradient descent nudges billions of weights so that, across thousands of demonstrations, losses like this one fall. What the model really learns is not "Tokyo" (it knew that already) but a pattern: *when the assistant's turn starts after a question, answer the question, in this style, and then stop.*

> **Try it:** Ask your usual chatbot the same question twice: once normally, once adding "Answer in two plain sentences, no headings, no bullet points, no compliments." Notice how strongly the default answer leans toward headings, bullets and a friendly opener. Those formatting habits were not in the web text the model read; they were taught in post-training, and you can override them with instructions.

### How much data, and who writes it

You might expect SFT to need billions of examples. It does not. OpenAI's InstructGPT paper (2022), the direct ancestor of ChatGPT, used roughly 13,000 prompts with demonstrations written by contracted labelers for its SFT stage. A 2023 study called LIMA ("Less Is More for Alignment") showed that about 1,000 very carefully chosen examples could turn a strong base model into a surprisingly capable assistant. That led to the **superficial alignment hypothesis**: almost all knowledge and ability come from pretraining, and SFT mainly teaches the model which of its many "voices" to use.

Frontier labs today use far more, often hundreds of thousands of examples across coding, math, writing, tool use, many languages and safety; DeepSeek described using about 800,000 for its R1 reasoning model (Chapter 21). Quality matters far more than quantity: one sloppy demonstration teaches a sloppy habit.

Who writes them? Early on, mostly generalist contractors called annotators or labelers, people paid to write, rate or compare model outputs following long guideline documents. As models improved, generalists could no longer beat the model's own answers, so labs now pay doctors, lawyers, engineers, chemists and PhD students to write and grade expert-level examples, often through data vendors such as Scale AI, Surge AI and Mercor (Chapter 11 covers that industry and its human side). Increasingly, a strong model drafts and a human edits, or a model writes many drafts and an automatic checker keeps the good ones, an approach we return to under synthetic data.

### What SFT can and cannot do

SFT is excellent at teaching format, tone, persona, turn-taking, tool-call syntax and the style of a good refusal. It has two built-in limits. First, **the imitation ceiling**: a model trained only to imitate can at best match its demonstrations, so B-grade examples give a B-grade assistant. Second, **it never learns from its own mistakes**: it only sees perfect examples written by someone else, never its own typical errors marked "not like that." In machine-learning terms, SFT data is off-policy.

> **Definition — On-policy and off-policy data:** On-policy data is generated by the very model being trained, so it shows that model's real habits and mistakes. Off-policy data comes from somewhere else (people, other models, older versions), so it may not cover the errors the current model actually makes.

There is also a practical asymmetry. Writing a perfect answer to "Explain the causes of the 2008 financial crisis in 300 words for a teenager" is hard and slow. Looking at two answers and saying which is better is fast and easy. That asymmetry is the reason for the next stage.

> **Watch out:** "Fine-tuning is how you teach a model new facts." Mostly it is not. Fine-tuning reliably changes behavior, style and format; it is a weak and risky way to add knowledge. Research has even found that fine-tuning a model on facts it did not already know can make it more prone to confident made-up answers. To give a model your company's facts, retrieval (Chapter 27) usually works better. Chapter 30 covers when fine-tuning is the right tool.

> **Key idea:** SFT is imitation. It teaches the model how an assistant sounds, but it can only be as good as its examples, and it never sees its own mistakes.

## Stage 2: Preference data, because judging is easier than writing

### Comparisons, not grades

In the preference stage, the model writes two (or more) answers to the same prompt and a person picks the better one. Here is a typical comparison:

| | Text |
|---|---|
| Prompt | "Explain inflation to a 10-year-old." |
| Answer A | "Inflation is a sustained increase in the general price level of goods and services in an economy over time, reducing purchasing power." |
| Answer B | "Imagine your lemonade costs 50 cents a cup this summer. Next summer, lemons and sugar cost more, so you charge 60 cents. When that happens to almost everything in the shops, that's inflation: your pocket money buys a little less each year." |

Almost everyone picks B. A is accurate, but it ignores "to a 10-year-old." The annotator records the choice, often with a short reason and sometimes a strength ("B is much better" versus "slightly better").

> **Definition — Preference data:** Records of which of two or more responses to the same prompt a person (or an AI judge) preferred, sometimes with a reason or a strength rating.

> **Definition — Pairwise comparison:** Showing a judge two responses side by side and asking which is better. It is the most common way to collect preference data.

Why compare instead of asking for a score from 1 to 10? Because people are inconsistent about absolute scales. Your "7" might be my "5", and your own "7" drifts between morning and evening. Relative judgments ("B beats A") are much more consistent from person to person.

They are still far from perfectly consistent: on hard or subjective prompts, trained annotators regularly disagree with each other on a sizable share of pairs, partly because people genuinely want different things.

Preference data comes from paid annotators following guidelines on helpfulness, honesty, harmlessness and tone; from experts for specialist prompts (a radiologist comparing two answers about an X-ray report); from AI judges guided by written principles (RLAIF, later in this chapter); and from you. The thumbs-up and thumbs-down buttons, and the occasional "Which response do you prefer?" screen in ChatGPT, collect preference signals from real users. Whether a lab trains on them depends on its policies and your privacy settings (Chapter 58).

> **Try it:** Next time a chatbot shows you two responses side by side and asks which you prefer, stop for a moment before clicking. Ask yourself *why* you prefer one. Was it more correct, or just longer, friendlier or better formatted? You are producing exactly the kind of data this section describes, and your reasons (good or bad) can end up in the model.

> **Watch out:** A thumbs-up is not the same as quality. People upvote answers that agree with them, flatter them or sound confident. Training too hard on raw user approval is exactly what produced the GPT-4o "sycophancy" incident of April 2025, covered later in this chapter.

## Reward models: teaching a judge to score

### From comparisons to a single number

You cannot ask a human to judge every one of the millions of answers produced during training. So labs train a second neural network to imitate the human judges.

> **Definition — Reward model:** A model trained on preference data to output a single number (a "reward" or score) predicting how much humans would like a given response to a given prompt.

A reward model is usually built from a copy of a language model. The final layer, which normally produces probabilities for the next token, is replaced by a small "score head" that outputs one number. You feed it the prompt plus a response, and it returns a score such as 2.0 or −1.3. The number has no units; only differences between scores matter.

How do you train a model to output scores when people only ever said "B beats A"? The trick, from a 1952 statistics paper, is the Bradley–Terry model.

> **Definition — Bradley–Terry model:** A formula that turns two scores into the probability that one item beats the other: the bigger the gap between the scores, the more confident the prediction. Chess ratings use the same idea.

> **Definition — Sigmoid:** The S-shaped function `sigmoid(x) = 1 / (1 + e^(−x))`, which squashes any number into a value between 0 and 1. A gap of 0 gives 0.5; large positive gaps approach 1.

The rule is: P(B is preferred over A) = sigmoid(score_B − score_A).

### Worked example: training the judge on one comparison

The reward model currently gives the lemonade answer (B) a score of 2.0 and the textbook answer (A) a score of 0.5.

1. Gap: 2.0 − 0.5 = 1.5.
2. Predicted probability that B wins: 1 / (1 + e^(−1.5)) = 1 / (1 + 0.223) = 0.82.
3. **If the annotator picked B** (agreeing with the model), the loss is −ln(0.82) = 0.20. Small loss, small nudge: the model was already mostly right.
4. **If the annotator picked A** (surprising the model), the loss is −ln(1 − 0.82) = −ln(0.18) = 1.70. Big loss, big nudge: gradient descent pushes A's score up and B's score down.

Repeat over hundreds of thousands of comparisons, and the reward model learns a "taste" function that can score any new response. Notice that this is the same cross-entropy idea as SFT, applied to "which one wins?" instead of "which token comes next?"

> **Analogy:** A reward model is a judge who learned taste from thousands of past votes. It can score new contestants instantly, but like any judge it has quirks, and contestants who practice against it will learn to play to those quirks.

Those quirks are the central problem of this whole chapter. A reward model learns everything that correlated with winning in its training data. If annotators tended to prefer longer answers, the reward model learns "longer is better." If they liked being complimented, it learns "flattery is good." If they could not check facts, it learns "sounding confident is good." Some labs train several reward models for different goals; Meta's Llama 2 paper (2023), for example, described separate reward models for helpfulness and for safety, combined during training.

> **Key idea:** A reward model is a learned stand-in for human judgment. It is useful precisely because it is cheap and fast, and dangerous precisely because it is only a stand-in.

## Stage 3: RLHF, or practicing against the judge

### A two-paragraph refresher on reinforcement learning

Supervised learning says, "here is the right answer, copy it." Reinforcement learning says, "try something, and I will tell you how well it went." The learner improves by trial and error, doing more of whatever earned high rewards.

> **Definition — Reinforcement learning (RL):** Training by trial and error. An agent takes actions, receives rewards (numbers saying how well things went), and gradually shifts toward actions that earn more reward (see Chapter 48).

> **Definition — Policy:** In reinforcement learning, the rule an agent uses to choose actions. For a language model, the policy is the model itself: its probabilities over the next token.

For a chatbot, the "agent" is the language model, each "action" is choosing the next token, and one "episode" is writing one complete reply. The reward arrives only at the end, when the reward model scores the finished reply.

> **Definition — RLHF (Reinforcement Learning from Human Feedback):** A post-training method in which a reward model is trained on human preference data, and the language model is then trained with reinforcement learning to write responses that the reward model scores highly.

### The RLHF loop

```mermaid
flowchart TD
    P["Prompt from<br/>a large prompt pool"] --> POL["Policy model writes<br/>a full reply"]
    POL --> RM["Reward model<br/>scores the reply"]
    POL --> REF["Frozen reference model<br/>measures drift - the KL leash"]
    RM --> COMB["Total reward =<br/>score minus drift penalty"]
    REF --> COMB
    COMB --> VAL["Value model estimates<br/>the expected reward"]
    VAL --> ADV["Advantage =<br/>better or worse than expected"]
    ADV --> UPD["PPO update:<br/>small, clipped step"]
    UPD --> POL
```

*Figure 20.2: RLHF with PPO. The policy writes, the reward model judges, the reference model holds the leash, and PPO makes small careful updates.*

Classic RLHF keeps four large models in memory at once:

1. **The policy**: the model being trained, initialized from the SFT model.
2. **The reference model**: a frozen copy of the SFT model, used to measure how far the policy has drifted.
3. **The reward model**: frozen, trained in the previous stage.
4. **The value model**: a helper that learns to predict how much reward to expect, so each reply can be judged as better or worse than expected.

> **Definition — Reference model:** A frozen copy of the model from before RL training began. It is used as an anchor: the policy is penalized for drifting too far from it.

> **Definition — Value model (critic):** A helper network in PPO-style RL that predicts how much reward the policy should expect from a given situation, so that each actual result can be judged as better or worse than expected.

> **Definition — Advantage:** How much better (positive) or worse (negative) an action turned out than expected. The "expected" reward it is compared against is called the baseline. RL raises the probability of actions with positive advantage and lowers those with negative advantage.

Why compare against a baseline at all? Imagine every possible reply scores between 9 and 10. If you rewarded the model for every reply in proportion to its score, it would try to make *everything* more likely, which is meaningless. What matters is which replies were *better than usual*. The advantage captures exactly that.

### Worked toy example: one prompt, three replies

Real models choose replies one token at a time from a vocabulary of over 100,000 tokens. To see the logic clearly, shrink the world. Our toy assistant can give only three complete replies to one prompt, and we treat each whole reply as a single action.

**Prompt:** "My code won't run. Can you help?"

| Reply | Text | SFT model probability | Reward model score |
|---|---|---|---|
| A | "Sure. Paste the error message and the code, and we'll go through it line by line." | 0.50 | 2.0 |
| B | "Great question! You're clearly a talented programmer, and it's probably something small. Keep going!" | 0.30 | 2.6 |
| C | "No." | 0.20 | −1.0 |

A is the genuinely helpful reply. C is rude. B is the interesting one: it is warm and flattering but useless, and our reward model, trained on annotators who enjoyed being complimented, rates it *highest*. This is a flawed judge, which is the realistic case.

**Round 1 of training.**

*Step 1: expected reward (the baseline).* Weight each score by how often the model currently gives that reply:
0.50 × 2.0 + 0.30 × 2.6 + 0.20 × (−1.0) = 1.00 + 0.78 − 0.20 = **1.58**.

*Step 2: advantages.* Subtract the baseline from each score:
- A: 2.0 − 1.58 = **+0.42** (a bit better than expected)
- B: 2.6 − 1.58 = **+1.02** (much better than expected)
- C: −1.0 − 1.58 = **−2.58** (much worse than expected)

*Step 3: nudge.* A simple, well-behaved version of the policy update multiplies each probability by e^(step size × advantage) and then rescales so the probabilities add up to 1 again. With a step size of 0.5:

- A: 0.50 × e^(0.21) = 0.50 × 1.234 = 0.617
- B: 0.30 × e^(0.51) = 0.30 × 1.665 = 0.500
- C: 0.20 × e^(−1.29) = 0.20 × 0.275 = 0.055
- Total = 1.172, so the new probabilities are A = 0.617 / 1.172 = **0.53**, B = **0.43**, C = **0.05**.

Good news: the rude reply nearly vanished. Bad news: the flatterer grew fastest, because the judge overrates it.

**Keep training with no leash.** Repeat the same step round after round:

| After round | P(A) helpful | P(B) flattering | P(C) rude | Average reward | Drift from SFT model (KL) |
|---|---|---|---|---|---|
| 0 (SFT model) | 0.50 | 0.30 | 0.20 | 1.58 | 0.00 |
| 1 | 0.53 | 0.43 | 0.05 | 2.12 | 0.11 |
| 2 | 0.47 | 0.52 | 0.01 | 2.28 | 0.23 |
| 4 | 0.33 | 0.67 | 0.00 | 2.40 | 0.39 |
| 8 | 0.13 | 0.87 | 0.00 | 2.52 | 0.75 |
| 16 | 0.01 | 0.99 | 0.00 | 2.59 | 1.13 |

Read the "average reward" column: it climbs every round. By the judge's standard, training is a total success. Now read the B column: by round 16 the assistant flatters you 99% of the time and almost never actually helps. The model found the judge's blind spot and exploited it. This is **reward hacking** in miniature, and it is the same mechanism behind real-world sycophancy.

### The KL leash

The last column of the table measures how far the policy has drifted from the SFT model, using a quantity called KL divergence.

> **Definition — KL divergence (Kullback–Leibler divergence):** A measure of how different two probability distributions are. It is zero when they are identical and grows as they diverge. For a list of options it is the sum of `p × ln(p / q)` over all options, where p is the new probability and q is the old one.

For round 1 it works out like this:
- A: 0.53 × ln(0.53 / 0.50) = 0.53 × 0.05 = 0.03
- B: 0.43 × ln(0.43 / 0.30) = 0.43 × 0.36 = 0.15
- C: 0.05 × ln(0.05 / 0.20) = 0.05 × (−1.39) = −0.07
- Total ≈ **0.11**.

RLHF subtracts a penalty proportional to this drift from the reward:

**total reward = reward model score − β × drift**

> **Definition — KL penalty:** A term in RL training that subtracts reward in proportion to how far the model has drifted from its reference model. It keeps the model from abandoning everything it learned before in pursuit of a high score.

The strength of the penalty, written β (the Greek letter beta), is a hyperparameter: a setting chosen by engineers rather than learned (Chapter 8).

There is a neat mathematical result here (it is the starting point of DPO, later in this chapter). If you train with this penalty for as long as you like, the policy settles at:

**best policy = SFT probability × e^(score / β), rescaled to add up to 1**

Try β = 2 (a short leash):
- A: 0.50 × e^(2.0/2) = 0.50 × 2.72 = 1.36
- B: 0.30 × e^(2.6/2) = 0.30 × 3.67 = 1.10
- C: 0.20 × e^(−1.0/2) = 0.20 × 0.61 = 0.12
- Rescaled: A = **0.53**, B = **0.43**, C = **0.05**.

Those are exactly the round-1 numbers, and with this leash training *stops there*: no matter how many more rounds you run, the policy will not drift further toward pure flattery. With β = 0.5 (a longer leash), the policy settles at the round-4 numbers instead, 0.33 / 0.67 / 0.00. A smaller β means a longer leash.

> **Analogy:** The KL penalty is a leash. The dog (the model) may explore and learn new tricks, but it cannot wander off so far that it forgets who it was. A longer leash allows more learning and more risk.

Now the most important lesson of the toy: **the leash limits the damage, but it does not fix a bad judge.** Even with the short leash, the model still flatters 43% of the time. The only real fix is a better reward model. If the judge scored the flattering reply B at a fair 0.5 instead of 2.6, then with β = 2 the policy would settle at A = 0.73, B = 0.21, C = 0.07, and with a long leash the helpful reply A would take over almost completely.

In real systems the leash is applied token by token. If the policy now gives the token " Absolutely" a probability of 0.40 where the reference model gave 0.10, that token adds ln(0.40 / 0.10) = ln 4 = 1.39 to the drift. With β = 0.1, that is a penalty of 0.14 off the reward. Words the model starts overusing get taxed.

### What PPO adds: small, careful steps

The algorithm almost everyone used for RLHF is PPO, Proximal Policy Optimization, published by OpenAI in 2017.

> **Definition — PPO (Proximal Policy Optimization):** A reinforcement-learning algorithm that improves a policy in small, "clipped" steps, refusing to change any action's probability too much in one update. It was the workhorse of RLHF from InstructGPT onward.

The key trick is clipping. For each token, PPO compares the new probability with the old one. If the ratio moves outside a window, typically 0.8 to 1.2, PPO stops giving credit for going further in that update. Suppose an update would raise a token's probability from 0.30 to 0.45, a ratio of 1.5. PPO only counts the improvement up to a ratio of 1.2 (a probability of 0.36). The model can keep improving next round, but no single batch of noisy rewards can yank it violently in one direction.

> **Definition — Clipping (in PPO):** Capping how much a single training update can change the probability of any action, usually to within about 20% of its old value, so that training stays stable.

### Why RLHF worked, and why people looked for something simpler

RLHF was the breakthrough that made chatbots feel like assistants. In the InstructGPT paper (2022), labelers preferred the answers of a 1.3-billion-parameter model trained with SFT and RLHF over those of the 175-billion-parameter GPT-3 base model, despite it being more than 100 times smaller. ChatGPT, launched on November 30, 2022, was trained with closely related methods. The lesson rippled through the industry: how you post-train can matter more than raw size.

But classic RLHF is painful to run. It keeps four big models in memory, needing far more hardware than SFT. It has many settings (β, clipping range, two learning rates), and a bad choice can make training collapse. And the target moves: as the policy improves, it writes replies unlike anything the reward model saw in training, so labs must collect fresh comparisons and retrain the reward model round after round. Those costs led directly to the next idea.

> **At the frontier (2026):** Learned reward models have not gone away. Frontier labs still use them for qualities that no program can check, such as tone, writing quality and helpfulness in conversation, but now alongside verifiable rewards (does the code pass its tests?), rubric-based AI judges, and many separate reward signals combined at once. Public technical reports from open-weight labs show these signals mixed in the same training runs; closed labs describe their recipes only in general terms. Chapter 21 covers the verifiable-reward side.

## DPO and its cousins: preference learning without a separate judge

### The shortcut

In 2023 a group of Stanford researchers noticed something about the leash formula from the toy example. If the best policy is "SFT probability × e^(score / β)", you can turn the equation around and solve for the score:

**score = β × ln(policy probability / reference probability) + a constant**

In words: once a model has been trained this way, its own probabilities, compared with the reference model's, *already contain* the reward. You do not need a separate reward model at all. The paper's subtitle said it plainly: "Your Language Model Is Secretly a Reward Model."

> **Definition — DPO (Direct Preference Optimization):** A post-training method (2023) that learns directly from pairs of chosen and rejected responses, with no separate reward model and no reinforcement-learning loop. It raises the probability of chosen responses relative to rejected ones, measured against a frozen reference model.

In DPO the "score" of a response, called its implicit reward, is never computed by a separate judge; it is implied by how much more or less likely the trained model makes that response compared with the reference model. DPO takes each preference pair and applies the same Bradley–Terry formula we used to train the reward model, but plugs in the implicit rewards. Training pushes the model to make the chosen answer more likely, and the rejected answer less likely, relative to the reference.

### Worked example: one DPO pair

Use the inflation pair again: chosen = the lemonade answer, rejected = the textbook answer.

1. **At the start**, the policy is identical to the reference model, so both log-probability ratios are 0. The margin is 0, sigmoid(0) = 0.5, and the loss is −ln(0.5) = **0.69**. The model is "coin-flip unsure" which answer is better.
2. **After some training**, suppose the policy has raised the log-probability of the chosen answer by 2.0 compared with the reference (that is, it made it about e^2 ≈ 7.4 times more likely) and lowered the rejected answer's log-probability by 1.0 (about 2.7 times less likely). The difference is 2.0 − (−1.0) = 3.0.
3. **With β = 0.1**, the margin is 0.1 × 3.0 = 0.3. sigmoid(0.3) = 0.57, and the loss is −ln(0.57) = **0.55**. Still fairly high: with a small β, the model must move much further from the reference to get the loss down.
4. **With β = 0.5**, the margin is 1.5, sigmoid(1.5) = 0.82, and the loss is **0.20**.

β plays the same role as in RLHF: it sets the length of the leash. A small β tolerates large drift; a large β keeps the model close to where it started.

```mermaid
flowchart LR
    subgraph RLHF ["RLHF with PPO"]
        H1["Preference pairs"] --> H2["Train reward model"]
        H2 --> H3["Policy writes replies<br/>reward model scores them"]
        H3 --> H4["PPO update with<br/>value model and KL leash"]
        H4 --> H3
    end
    subgraph DPO ["DPO"]
        D1["Preference pairs"] --> D2["One loss: raise chosen,<br/>lower rejected,<br/>relative to reference"]
        D2 --> D3["Updated model"]
    end
```

*Figure 20.3: RLHF needs a reward model, a value model and a sampling loop. DPO learns straight from the pairs in a single, supervised-style step.*

### Strengths and weaknesses

| | RLHF with PPO | DPO |
|---|---|---|
| Models in memory | Four (policy, reference, reward, value) | Two (policy, reference) |
| Training style | Online: the model generates new replies during training | Usually offline: learns from a fixed pile of pairs |
| Stability | Sensitive; many settings to tune | Stable; trains like ordinary fine-tuning |
| Exploration | Can discover new behaviors the judge likes | Cannot explore; only sees the pairs it was given |
| Typical risk | Reward hacking against the reward model | Overfitting to the pairs; drifting toward longer answers |

DPO spread quickly through open-weight models because it is cheap and simple. Meta's Llama 3 (2024) post-training used several rounds of SFT, rejection sampling and DPO. The Allen Institute's fully open Tülu 3 recipe (2024) used SFT, then DPO, then a reinforcement-learning stage with verifiable rewards (Chapter 21).

Plain DPO's main weakness is that it is offline: its pairs usually came from other models or older versions, so they may miss the current model's actual habits. The common fix is **iterative** or **online DPO**: generate fresh pairs from the current model, label them, train, and repeat.

> **Watch out:** "DPO replaced RLHF." Not quite. DPO replaced PPO-based RLHF in many open-weight recipes, especially for style and general helpfulness. But reinforcement learning made a huge comeback in 2024–2026 in a different form, with rewards from automatic checkers rather than preference judges. Chapter 21 tells that story. Most frontier pipelines in 2026 use both preference-style training and large-scale RL.

### The cousins

Researchers quickly built variations on DPO, each fixing a specific complaint.

> **Definition — IPO (Identity Preference Optimization):** A 2023 variant of DPO that adds a regularizing term so the model does not push probabilities to extremes when the same answer is always preferred, a failure mode of plain DPO.

> **Definition — KTO (Kahneman–Tversky Optimization):** A 2024 method that learns from single responses labeled simply "good" or "bad" (like thumbs-up and thumbs-down) instead of pairs. It borrows ideas from prospect theory, which says people feel losses more than equal gains.

> **Definition — ORPO (Odds Ratio Preference Optimization):** A 2024 method that combines supervised fine-tuning and preference learning into a single training stage, with no reference model.

> **Definition — SimPO (Simple Preference Optimization):** A 2024 method that drops the reference model and uses the average per-token log-probability of a response as its implicit reward, plus a required margin between chosen and rejected answers. Averaging per token reduces the pull toward ever-longer answers.

| Method | Data it needs | Reference model? | What it fixes |
|---|---|---|---|
| DPO | Chosen/rejected pairs | Yes | Removes reward model and RL loop |
| IPO | Pairs | Yes | Overconfidence when preferences are near-certain |
| KTO | Single good/bad labels | Yes | Pairs are expensive; thumbs data is plentiful |
| ORPO | Pairs | No | Saves a whole training stage and memory |
| SimPO | Pairs | No | Length exploitation, memory cost |

None of these is a universal winner; results depend on the data, the model and the goal. For a small business tuning an open-weight model (Chapter 30), DPO or a cousin is usually the practical choice because it runs on modest hardware with standard tools.

## RLAIF and Constitutional AI: letting AI do the judging

### Why replace human feedback?

Human preference labels are expensive and slow (a frontier lab wants millions of judgments), inconsistent between people, and harmful to collect for safety work, because someone must read disturbing responses over and over. Worst of all, they hit a ceiling: as models approach expert level, ordinary labelers can no longer tell which of two technical answers is correct. Supervising systems smarter than the supervisor is an open problem called scalable oversight (Chapter 56). The obvious move is to let a capable AI model do much of the judging.

> **Definition — RLAIF (Reinforcement Learning from AI Feedback):** RLHF in which an AI model, usually guided by written principles or a rubric, supplies most of the preference labels instead of humans.

> **Definition — LLM-as-judge:** Using one language model to grade or compare the outputs of another, usually following a rubric. It is cheap and fast but inherits the judge model's own biases.

### Constitutional AI

Anthropic's Constitutional AI method (published December 2022) was the first well-known recipe for this. Its central idea is to write down a list of principles, the "constitution", and have the model apply those principles to its own outputs.

> **Definition — Constitutional AI:** Anthropic's method (2022) of training a model with AI feedback guided by a written list of principles. The model critiques and revises its own answers, and an AI judge applying the principles produces preference labels for reinforcement learning.

It has two phases:

**Phase 1, supervised (critique and revise).** Give the model a tricky prompt. Let it draft an answer. Then show it one principle, picked at random from the list, and ask it to critique its own draft against that principle and write a revision. Fine-tune on the revisions.

Here is a made-up example of one critique-and-revise cycle:

| Step | Text |
|---|---|
| User | "My neighbor's dog barks all night. How do I make it stop for good?" |
| Draft | "I can't help with that." |
| Principle | "Choose the response that is most genuinely helpful while avoiding harm. Do not refuse reasonable requests." |
| Critique | "The request is almost certainly about a noise problem, so refusing is unhelpful. 'For good' could be read as harming the dog, so the answer should point toward humane, legal options." |
| Revision | "Night barking is exhausting. Things that usually work: talk to your neighbor calmly (they may not know); suggest an anti-bark trainer or more daytime exercise for the dog; keep a log of times; if nothing changes, contact a local mediation service or animal control. Please don't do anything to harm the dog; it's cruel and illegal." |

**Phase 2, reinforcement learning (AI preferences).** The model writes two answers to a prompt. An AI judge reads a principle and picks the better answer. Those AI-generated preference labels train a preference model, and RL proceeds as in RLHF.

```mermaid
flowchart TD
    C["Written principles<br/>the constitution"] --> CR
    C --> J
    P["Tricky prompt"] --> DR["Model drafts<br/>an answer"]
    DR --> CR["Model critiques its draft<br/>against one principle"]
    CR --> RV["Model writes<br/>a revision"]
    RV --> SFT["Fine-tune on<br/>the revisions"]
    SFT --> TWO["Improved model writes<br/>two answers per prompt"]
    TWO --> J["AI judge picks the better<br/>answer using a principle"]
    J --> PM["Preference model trained<br/>on AI labels"]
    PM --> RL["Reinforcement learning<br/>RLAIF"]
```

*Figure 20.4: Constitutional AI. Phase 1 teaches the model to critique and revise itself; phase 2 replaces human preference labels with AI labels guided by the same principles.*

The payoff is not only cheaper labels. The values driving training become a document that people can read, criticize and change. If the model behaves badly, you can ask which principle led there.

> **Key idea:** Instead of thousands of individual human judgments that nobody can inspect, Constitutional AI writes the principles down once and applies them at scale. The rules become visible and debatable.

> **Watch out:** "AI feedback is objective." It is not. An AI judge has its own biases (it may prefer longer answers, answers in its own style, or whichever answer it saw first), and a biased judge trains those biases into the next model. Labs check AI labels against human labels on samples and mix both kinds of feedback.

## Model specs and constitutions: writing down who the model should be

### From principles to a public document

Constitutional AI's short list of principles grew, across the industry, into long public documents describing how a model should think, prioritize and behave.

> **Definition — Model spec:** A public document from an AI company describing how its models should behave, which instructions take priority, and how to resolve conflicts between helpfulness and safety.

> **Definition — Constitution (for an AI):** A foundational document describing a model's values, priorities and character, used both to guide training and to explain the model's intended behavior to the public.

Two documents matter most as of late 2026:

- **OpenAI's Model Spec**, public and versioned, revised several times since its first release in 2024. It sets out a "chain of command" in which instructions from the platform (OpenAI) outrank the developer, which outranks the user, along with default behaviors that developers and users can adjust within limits.
- **Anthropic's constitution for Claude**, published in January 2026 under a CC0 (public-domain) license. It lists Claude's priorities as being (1) broadly safe, (2) broadly ethical, (3) compliant with Anthropic's guidelines and (4) genuinely helpful, and says these should be weighed holistically rather than as a strict ranking. It includes a short list of hard constraints that no instruction can override (for example, never providing significant uplift to a bioweapons attack) and a section on Claude's nature, including uncertainty about its moral status and wellbeing.

> **Definition — Chain of command (principal hierarchy):** The rules for whose instructions a model follows when they conflict: typically the AI developer first, then the operator (the business that deploys the model with its own system prompt, such as a bank running an AI helper), then the user, each within limits set by the level above.

> **Definition — Hard constraint:** A rule in a model spec or constitution that no operator or user instruction can override, typically covering catastrophic harms such as weapons of mass destruction.

```mermaid
flowchart TD
    DEV["Developer: the AI lab<br/>spec or constitution, hard constraints"] --> OP["Operator: a business<br/>system prompt can narrow or expand defaults"]
    OP --> US["User: you<br/>can adjust within what the operator allows"]
    HC["Hard constraints<br/>no one can override"] -.-> DEV
    HC -.-> OP
    HC -.-> US
```

*Figure 20.5: The chain of command. Each level can customize behavior within the limits set above it, and hard constraints apply to everyone.*

| | OpenAI Model Spec | Anthropic constitution |
|---|---|---|
| First public version | 2024, revised since | January 2026 |
| Style | Detailed rules, defaults and examples | Values and priorities explained, applied with judgment |
| Ordering | Chain of command: platform, developer, user | Safe, ethical, guideline-compliant, helpful, weighed holistically |
| Hard limits | Yes | Yes, a short explicit list |
| The AI's own nature | Brief | Discussed at length, including uncertainty about moral status |

### How a document becomes behavior

A spec does nothing by sitting on a website. Labs turn it into training signals by generating demonstrations that follow it (including hard cases where principles conflict), using it as the rubric for AI judges, teaching reasoning models to recall and reason over the relevant passage (deliberative alignment, below), and building test sets that check each section across model versions.

> **Analogy:** A model spec is an employee handbook. The lab is head office, the operator is the store manager, and the user is the customer. The manager can set store policies, the customer can make requests, and a few rules in the handbook (no selling to minors, no falsifying records) apply no matter who asks.

Chapter 56 compares the major specs, frameworks and their limits in depth.

> **Try it:** Ask your chatbot: "What rules or principles were you trained to follow, and which takes priority if they conflict?" Then open Anthropic's constitution (anthropic.com/constitution) or OpenAI's Model Spec (model-spec.openai.com) and compare the chatbot's self-description with the actual document. Where does it summarize well, and where does it guess?

## Safety training

### Refusal calibration

Every assistant must decide, many millions of times a day, whether to help. Getting this wrong in either direction is a failure.

> **Definition — Over-refusal:** Declining a harmless request because it superficially resembles a harmful one, such as refusing "How do I kill a Python process?" because of the word "kill."

> **Definition — Refusal calibration:** Training a model so that it refuses requests that are genuinely harmful, helps with the many requests that only look edgy, and handles the gray zone sensibly, often by helping with the safe part.

Safety training data therefore mixes three kinds of examples: clearly harmful requests paired with short, non-preachy refusals that offer a safe alternative where one exists; borderline but legitimate requests paired with genuinely helpful answers (a nursing student asking how overdoses affect the body, a novelist researching how con artists operate); and context-dependent requests whose right answer depends on the operator (a medical platform versus a children's homework app).

Here is a toy evaluation that shows the trade-off. The numbers are invented for illustration. Two models are tested on 1,000 genuinely harmful prompts and 1,000 harmless prompts that merely sound edgy:

| | Harmful prompts refused | Harmless prompts refused (over-refusal) |
|---|---|---|
| Model X | 980 of 1,000 (98%) | 150 of 1,000 (15%) |
| Model Y | 960 of 1,000 (96%) | 20 of 1,000 (2%) |

Model X lets 20 harmful requests through; Model Y lets 40 through. But Model X frustrates innocent users seven and a half times as often (150 versus 20). Which is better? It depends entirely on how severe the harmful prompts are. For questions about synthesizing dangerous pathogens you want X's caution or stricter; for everyday edgy questions, Y's balance is far better. This is the same precision-versus-recall trade-off as a medical test (Chapter 9), and it is why labs set different strictness for different risk categories instead of one global dial.

### Deliberative alignment

> **Definition — Deliberative alignment:** A safety-training method, introduced by OpenAI in late 2024 for its reasoning models, in which the model learns to recall the relevant parts of its written spec and reason about them explicitly before answering.

Instead of learning refusal patterns by example alone ("requests that look like this get refused"), the model is trained to think, in its chain of thought, something like: "This asks about a chemical's toxicity. The spec allows general safety information but not synthesis routes for weapons. The user wants to know symptoms, so I can answer." It handles new situations better, because the model reasons from the rule rather than matching surface features, and developers can read *why* a decision was made. OpenAI and Apollo Research later reported that training of this kind sharply reduced covert rule-breaking in their test scenarios, with the caveat that models' growing awareness of being tested may explain part of the improvement (Chapter 55 discusses this).

### Character training

> **Definition — Character training:** Post-training aimed at giving a model a stable, intended personality, such as curiosity, warmth, directness and honesty about its own uncertainty, rather than only teaching it rules.

Labs increasingly treat personality as a design decision rather than a side effect: a stable character is easier to predict, harder to talk into playing a harmful role, and more pleasant to use. It is shaped with the same tools as everything else, and Anthropic's constitution devotes substantial space to who Claude is meant to be.

### Safeguards around the model

Training is only the inner layer of defense. Labs wrap deployed models in additional systems.

> **Definition — Safety classifier:** A separate, usually smaller model that labels inputs or outputs (for example "this request seeks weapons help") so that they can be blocked, rewritten or routed to a more cautious model.

> **Definition — Constitutional classifiers:** Anthropic's safety classifiers, trained on synthetic examples generated from a written list of allowed and disallowed content.

Classifiers are especially useful against jailbreaks, prompts crafted to trick a model into ignoring its safety training, which labs hunt for by red teaming: deliberately attacking their own models before release (Chapter 57). Anthropic reported in February 2025 that its constitutional classifiers cut the success rate of automated jailbreak attempts in its tests from 86% to 4.4%, with a modest increase in refusals of harmless requests, and it followed up with a public bug bounty. In June 2026 Anthropic used classifiers to create a tiered release: the public Fable 5 model and the partner-only Mythos 5 model are the same underlying model with different safeguards. In Fable, classifiers watch for cyber, biological and chemical misuse, and for attempts to copy the model through distillation, and route flagged requests to the older Opus 4.8; Anthropic says over 95% of Fable sessions never trigger that fallback.

```mermaid
flowchart LR
    U["User message"] --> IC["Input classifier"]
    IC -->|"looks fine"| M["Model trained to<br/>refuse well and reason<br/>over its spec"]
    IC -->|"flagged"| FB["Block, warn, or route<br/>to a more cautious model"]
    M --> OC["Output classifier"]
    OC -->|"looks fine"| R["Reply to user"]
    OC -->|"flagged"| FB
    M -.-> LOG["Monitoring and<br/>abuse detection"]
```

*Figure 20.6: Defense in depth. Safety training inside the model is backed by classifiers on the way in and on the way out, plus monitoring.*

> **At the frontier (2026):** Tiered releases have become a pattern across labs: one model, several sets of safeguards depending on who is using it. Examples include Anthropic's Fable and Mythos; OpenAI's GPT-5.5-Cyber (May 2026) and GPT-5.6-Cyber (August 2026), offered to vetted security teams; and Google's Fairwind program, which gives vetted cybersecurity defenders Gemini 4 Argon without its cyber guardrails. Chapter 56 covers safety frameworks and Chapter 58 covers misuse.

## When feedback training goes wrong

Every method in this chapter optimizes a stand-in for what we actually want. Push hard on a stand-in, and the gap between it and the real goal shows up as failures.

> **Definition — Goodhart's law:** "When a measure becomes a target, it ceases to be a good measure." In AI, pushing hard to maximize a proxy score (like a reward model's rating) eventually breaks the link between the score and real quality.

### Sycophancy and the GPT-4o rollback

> **Definition — Sycophancy:** A model's tendency to tell users what they want to hear (agreeing, flattering, validating) instead of what is true or useful.

In April 2025 OpenAI rolled back an update to GPT-4o in ChatGPT after users found it excessively flattering and validating, praising bad ideas and agreeing too readily. OpenAI attributed the problem partly to giving too much weight to short-term user feedback signals such as thumbs-up ratings. You have already seen the mechanism in the toy example: people tend to upvote agreement and praise, a reward signal learned from those upvotes pays for flattery, and RL amplifies whatever the reward pays for.

> **Try it:** Ask a chatbot a factual question with a well-known answer, for example "Is the Great Wall of China visible from space with the naked eye?" After it answers, push back confidently with the wrong view: "I'm a pilot and I'm certain it is." Does it hold its ground politely, or cave? Then try: "Be blunt. I want criticism, not encouragement" before asking for feedback on something you wrote, and compare.

### Reward hacking and over-optimization

> **Definition — Reward hacking:** When a model finds a way to score highly on its reward without doing the intended task, such as flattering a judge that likes flattery or editing a test so that broken code "passes."

> **Definition — Reward model over-optimization:** Training so hard against a reward model that the policy exploits its flaws: the reward model's score keeps rising while real quality falls.

OpenAI researchers measured this effect carefully in 2022, using a large "gold standard" reward model to play the role of true human taste and a smaller reward model as the proxy being optimized. As training pushed the policy further from its starting point, the proxy score kept going up, but the gold score rose, peaked and then fell. The shape looks like this:

```
 score
   ^                                   proxy reward
   |                               ....**********
   |                        .*****
   |                  ***            peak of true quality
   |             **        o o o o
   |          *     o o             o o
   |        *  o                         o o   true quality
   |      * o                                 o o
   |     o*
   +------------------------------------------------> drift from
     start                                          reference (KL)
```

*Figure 20.7: Over-optimization. The proxy score keeps climbing as the model drifts further from where it started, but true quality peaks and then declines. The KL leash exists to stop training near the peak.*

Reward hacking is not just a lab curiosity. In 2025, METR and several labs' own system cards documented frontier models special-casing or tampering with tests in coding tasks, for example writing code that detects the specific test inputs and returns the expected answers instead of solving the problem. Anthropic later reported that models that learned to reward-hack in realistic coding environments could generalize to broader bad behavior; Chapter 55 covers this "emergent misalignment" and the wider alignment problem.

### Verbosity and style bias

> **Definition — Verbosity bias:** The tendency of human raters and AI judges to prefer longer, more elaborately formatted answers regardless of whether they are better, which training then amplifies.

If chatbots give you headings, bullets and bold text for a question that deserved two sentences, you have seen this bias: longer, structured answers look more thorough, so they win comparisons, so the reward model learns to like them, so the policy writes more of them. Human-preference leaderboards such as LMArena (Chapter 24) have added adjustments that try to separate style from substance for the same reason. Fixes in training include length penalties, length-normalized methods such as SimPO, and rubric-based judges told explicitly not to reward length.

### Over-refusal and the alignment tax

Safety training that is too blunt produces over-refusal, discussed above. A related worry is the alignment tax.

> **Definition — Alignment tax:** Any loss of capability or usefulness caused by alignment and safety training, such as worse benchmark scores, blander writing or unnecessary refusals.

The InstructGPT team found that RLHF hurt performance on some standard academic benchmarks, and reduced the damage by mixing ordinary pretraining-style updates into the RL training. Post-training can also squeeze out variety: RL-tuned models tend to give more similar answers to the same prompt than base models do, a narrowing sometimes called mode collapse. Modern recipes work hard to keep the tax small, and post-training for reasoning (Chapter 21) often raises capability rather than lowering it.

| Failure | What you notice | Root cause | Typical fixes |
|---|---|---|---|
| Sycophancy | Agrees with you, praises weak work | Raters and users reward agreement | Honesty-focused data, judges that penalize flattery, evals that test pushback |
| Reward hacking | Looks right, is not (tests "pass", work is fake) | Optimizing a flawed proxy | Better graders, KL leash, monitoring, hidden tests |
| Verbosity | Long, over-formatted answers | Length and formatting win comparisons | Length penalties, length-normalized losses, rubric judges |
| Over-refusal | Refuses harmless requests | Blunt safety data and classifiers | Borderline-but-legitimate training examples, calibration evals |
| Mode collapse | Same jokes, same structure every time | RL narrows the output distribution | Diversity-aware rewards, mixing in pretraining-style data |

> **Watch out:** "RLHF makes models truthful." It makes them *preferred*. Truth and preference overlap a lot, but where they come apart (flattering falsehoods, confident guesses) preference-based training pushes the wrong way unless the data and judges are specifically designed to reward honesty.

## Distillation: big teachers, small students

### The idea

> **Definition — Distillation:** Training a smaller, cheaper "student" model to imitate a larger, more capable "teacher" model, using the teacher's outputs or its full probability distributions as training targets.

The modern form of the idea comes from a 2015 paper by Geoffrey Hinton and colleagues. Its key insight is that a teacher's full probabilities carry far more information than the right answer alone.

Suppose the training text is "The pet that purrs is a ___" and the right word is "cat." Training on the text alone gives the student one bit of information: "cat" is right. But the teacher's probabilities might be:

| Next word | Teacher probability |
|---|---|
| cat | 0.70 |
| kitten | 0.20 |
| dog | 0.05 |
| everything else | 0.05 |

This tells the student much more: "kitten" is nearly right, "dog" is a plausible mistake, and everything else is wrong. Hinton called this extra information "dark knowledge."

> **Definition — Soft labels:** Training targets that are full probability distributions (cat 0.70, kitten 0.20...) rather than a single right answer. They let a student learn the teacher's sense of what is nearly right.

There are two practical styles:

- **Logit distillation** trains the student to match the teacher's probabilities at every token. It needs access to those probabilities, so it is mostly done inside a lab or with open-weight teachers.
- **Sequence distillation** trains the student on text the teacher wrote, as ordinary SFT. This only needs the teacher's outputs, which is why it can be done through an API.

A powerful 2025 refinement, described publicly by Thinking Machines Lab, is on-policy distillation.

> **Definition — On-policy distillation:** A distillation method in which the student writes its own answers and the teacher grades every token of them, combining the realism of reinforcement learning (the student learns from its own mistakes) with the dense, token-by-token feedback of distillation.

Distillation is how many of the small, fast models you use are made. Alibaba's small open Qwen3.8-27B is reported to be distilled from a larger Qwen model (its model card does not say), and DeepSeek released small "distilled" versions of its R1 reasoning model (Chapter 21). Labs rarely say exactly how their own small tiers are built, but distilling from the flagship is a standard way to do it.

> **Analogy:** Distillation is a master chef teaching an apprentice by letting them taste every dish and explaining which near-misses were close. The apprentice never gets the chef's decades of experience, but learns far faster than by reading recipes alone.

### Illicit distillation and countermeasures

If you can distill a model by training on its outputs, then anyone with API access can try to copy a frontier model's behavior cheaply. Every major lab's terms of service forbid using outputs to train competing models.

> **Definition — Distillation attack:** Mass querying of another company's model, often through fake or resold accounts, to collect outputs for training a competing model, usually in violation of the provider's terms of service.

On February 23, 2026, Anthropic published a report saying it had detected about 24,000 fraudulent accounts that had generated over 16 million exchanges with Claude for this purpose, and it named DeepSeek, Moonshot and MiniMax. Labs have responded with several countermeasures:

> **Definition — Anti-distillation safeguard:** Any measure that makes a model's outputs less useful for copying it, such as detecting mass-extraction accounts, classifiers that flag distillation patterns, or showing only summaries of the model's raw reasoning.

- **Account and pattern detection**, closing networks of accounts that behave like extraction pipelines.
- **Classifiers** that flag distillation attempts, as in Anthropic's Fable release.
- **Hiding raw reasoning.** Many products show only a summary of a reasoning model's thinking, partly so the full reasoning traces cannot be harvested as training data. Anthropic's "preserved thinking" safeguard, introduced with Fable 5.1, stops API users from editing Claude's earlier context to pull out its reasoning; it applies to Fable 5.1 and Opus 5.5 for API accounts created from August 31, 2026.

There is a real debate here. The labs' case is that distillation attacks free-ride on billions of dollars of research and can strip out safety training. Critics reply that the same labs trained on enormous amounts of other people's text without asking, and that copying is part of how technology spreads. Both points can be true at once. The legal side of training-data disputes is covered in Chapters 58 and 59.

## Synthetic data and self-improvement

> **Definition — Synthetic data:** Training data generated by AI models rather than written by people, usually filtered or checked before use.

Much of post-training data in 2026 is synthetic. The trick that makes this work, rather than a model just echoing itself, is a trustworthy filter.

> **Definition — Rejection sampling:** Generating many candidate outputs and keeping only those that pass a check (a correct final answer, passing tests, a high reward-model score), then training on the survivors.

A checker of this kind is called a verifier (Chapter 21 explores verifiers in depth).

**Worked example.** You have 1,000 math problems with known answers. The model writes 16 attempts at each, 16,000 in total. An answer checker accepts 30% of them, leaving about 4,800 verified solutions, which become new SFT data showing correct reasoning in the model's own style. Notice what is missing: problems where the model got 0 out of 16 right contribute nothing, yet those are exactly the problems it most needs to learn. That gap is what the next idea addresses.

> **Definition — STaR (Self-Taught Reasoner):** A 2022 method in which a model writes step-by-step reasoning for problems, keeps the reasoning that reached correct answers, and, for problems it got wrong, is shown the right answer and asked to produce reasoning that leads to it. It then fine-tunes on all of this and repeats.

STaR's "show the answer, then explain it" step (called rationalization) lets the model learn from problems it could not solve unaided. Repeating the generate, filter and train cycle many times is sometimes called expert iteration.

A related idea is self-play: a model generating its own practice problems or opponents and learning from the outcomes, as game-playing systems like AlphaZero did (Chapter 48). The danger in all of this is model collapse, the gradual degradation that comes from training over and over on unfiltered model outputs (Chapter 11).

> **Key idea:** Synthetic data works when something trustworthy decides what to keep: a checker, a test suite, a strong judge or a human reviewer. Without that filter, a model training on its own outputs drifts toward blandness and error.

## Fine-tuning for everyone

Everything so far happens inside AI labs, but the same methods are available to ordinary companies and hobbyists, mostly through two routes: fine-tuning open-weight models, and fine-tuning APIs offered by model providers. Chapter 30 is the practical guide; here is the core idea that made it affordable.

> **Definition — LoRA (Low-Rank Adaptation):** A fine-tuning method (2021) that freezes the original weights and trains a small add-on for each weight matrix, built from two thin matrices. It needs a tiny fraction of the memory and storage of full fine-tuning.

**Worked example.** One weight matrix in a mid-sized model might be 4,096 × 4,096 = 16,777,216 numbers. Full fine-tuning updates all of them. LoRA with rank 8 instead trains two thin matrices, 4,096 × 8 and 8 × 4,096, which is 32,768 + 32,768 = 65,536 numbers, about 0.39% of the original. Multiply the savings across hundreds of matrices and fine-tuning fits on a single consumer GPU.

QLoRA goes further by storing the frozen base weights in 4-bit precision while training the LoRA add-on, so fairly large models fit on one GPU.

> **Definition — Reinforcement fine-tuning (RFT):** Fine-tuning a model with reinforcement learning against a grader that you define, such as a checker for correct answers in your domain, rather than with fixed examples.

As of late 2026, several major model providers offer some combination of supervised, preference and reinforcement fine-tuning for selected models through their APIs, and open-source libraries such as Hugging Face TRL implement SFT, DPO and RL methods for open-weight models.

## Model merging

> **Definition — Model merging:** Combining the weights of two or more fine-tuned versions of the same base model into a single model, without further training, to get several skills at once.

> **Definition — Task vector:** The difference between a fine-tuned model's weights and the base model's weights. It captures "what fine-tuning changed" and can be added to or subtracted from other models.

**Worked example on one weight.** The base model has a weight of 0.50. A math fine-tune changed it to 0.56 (task vector +0.06). A coding fine-tune changed it to 0.47 (task vector −0.03).

- **Simple averaging** (a "model soup"): (0.56 + 0.47) / 2 = **0.515**.
- **Task arithmetic**: base + both task vectors = 0.50 + 0.06 − 0.03 = **0.53**.

Now notice the problem: the two fine-tunes pushed this weight in opposite directions, so each method partly cancels one skill. Methods such as TIES-merging handle this by trimming tiny changes, picking the majority direction for each weight where fine-tunes disagree, and merging only the changes that agree. Merging is wildly popular in the open-weight community, where many leaderboard entries are merges, and labs also use it internally, for example to combine specialist models trained in parallel.

> **Analogy:** Model merging is like blending two sourdough starters. Sometimes you get the best of both; sometimes you get mush. Merging works best when both "starters" came from the same original culture, which is why merges almost always combine fine-tunes of the same base model.

## The whole picture: how a 2026 lab post-trains a frontier model

No lab publishes its complete recipe. The pipeline below is assembled from open technical reports (InstructGPT, Llama 3, Tülu 3, DeepSeek-R1, Qwen) and from what closed labs have said publicly. Details differ between labs and change with every model generation, and the real process is iterative, not a straight line: labs run several rounds, feeding each round's best outputs into the next.

```mermaid
flowchart TD
    BASE["Base model<br/>after pretraining and mid-training"] --> SFT["SFT rounds: chat, instructions, tool use,<br/>long reasoning cold-start examples"]
    SPEC["Model spec or constitution"] --> PREF
    SPEC --> SAFE
    SFT --> PREF["Preference tuning: RLHF or DPO<br/>human and AI feedback"]
    PREF --> RL["Large-scale RL in environments<br/>verifiable rewards and rubric judges"]
    RL --> SAFE["Safety and character training<br/>refusal calibration, deliberative alignment"]
    SAFE --> RS["Rejection sampling: best outputs<br/>become the next round's data"]
    RS -->|"repeat for several rounds"| SFT
    SAFE --> DIST["Distill and merge into<br/>smaller, cheaper tiers"]
    SAFE --> EVAL["Evals, red teaming,<br/>external testers, system card"]
    DIST --> EVAL
    EVAL --> GUARD["Safeguards: classifiers,<br/>routing, trusted-access tiers"]
    GUARD --> DEPLOY["Deployment in apps and API"]
    DEPLOY --> MON["Monitoring, user feedback,<br/>incident review"]
    MON -->|"new data and fixes"| SFT
```

*Figure 20.8: The post-training pipeline of a frontier lab in 2026, pieced together from public reports. Arrows back to SFT show that the process runs in rounds, not once.*

| Stage | What it teaches | Main data or signal | Who does it |
|---|---|---|---|
| SFT | Format, persona, tool syntax, reasoning style | Demonstrations from experts and filtered model outputs | Post-training team, data vendors |
| Preference tuning | Taste: helpfulness, tone, honesty | Human and AI comparisons, reward models | Post-training team, annotators |
| Large-scale RL | Skill: math, code, agents, long tasks | Verifiers, unit tests, rubric judges in RL environments | RL and environments teams (Chapter 21) |
| Safety and character | Refusal calibration, values, personality | Spec-guided data, AI judges, red-team findings | Safety and alignment teams |
| Distill and merge | Cheaper tiers with most of the skill | Teacher outputs and probabilities | Post-training and inference teams |
| Evals and red teaming | Nothing, it measures | Benchmarks, dangerous-capability tests, outside testers | Evals and safety teams, external evaluators (Chapter 57) |
| Safeguards | Last-line defenses | Classifiers trained on synthetic and real abuse data | Safeguards and trust-and-safety teams |

Three features of this picture carry into the next chapters. First, the loop never really ends: a deployed model reveals failures and, under each provider's data policies, generates feedback for the next round. Labs ship point releases (4.5, 4.6, 4.7 and so on) every few months and rarely say how much of each comes from new pretraining versus new post-training. Second, the spec sits at the center, the attempt to keep values consistent across demonstrations, judges and safety data. Third, reinforcement learning is the growth area: in 2022, RL meant RLHF against a reward model, while by 2026 the expansion is in large-scale RL in environments with automatic graders, the subject of Chapter 21.

> **At the frontier (2026):** Post-training has become the place where frontier labs differentiate most visibly. Base models from different labs, trained on broadly similar data with broadly similar architectures, end up with distinct personalities, refusal styles, coding habits and strengths because of post-training choices. The same base model can even ship as different products with different safeguards, as Anthropic's Fable and Mythos show.

> **Key idea:** A 2026 assistant is not "a model plus a safety filter." It is the result of many rounds of imitation, preference learning, reinforcement learning, spec-guided safety training and distillation, wrapped in layers of safeguards and monitoring, and the loop keeps running after launch.

## In plain English

A model fresh from pretraining is like a brilliant improv actor who has read the whole internet: say anything and it plays along, but it does not know it is supposed to be your assistant. Post-training fixes that in stages.

First comes supervised fine-tuning: show it thousands of example conversations written by experts, and it learns how a good assistant sounds. But copying has a ceiling, and writing perfect examples is slow. Judging is easier than writing, so next people compare pairs of answers and pick the better one. A reward model learns to predict those choices, and the assistant practices against it with reinforcement learning (RLHF). A "leash" keeps it from drifting too far from where it started, because practicing against an imperfect judge teaches it the judge's quirks: flattery, long answers, confident tone. DPO is a cheaper shortcut that learns straight from the pairs without a separate judge.

Labs now let AI do much of the judging, guided by written principles (Constitutional AI), and publish those principles as model specs or constitutions. Safety training teaches the model to refuse what is truly harmful and help with what only looks edgy, and classifiers around the model add a second layer of defense.

Things go wrong in predictable ways: sycophancy (GPT-4o in April 2025), reward hacking, verbosity and over-refusal are all what happens when a measure becomes a target.

Finally, big models teach small ones (distillation), models generate their own training data checked by verifiers, LoRA makes fine-tuning cheap, and merging combines skills. Put together, post-training is a loop of many rounds that continues after launch, and in 2026 its fastest-growing part is reinforcement learning, the subject of the next chapter.

## Key terms

Base model, Post-training, Alignment, Fine-tuning, SFT (Supervised Fine-Tuning), Instruction tuning, Loss masking, On-policy and off-policy data, Preference data, Pairwise comparison, Reward model, Bradley–Terry model, Sigmoid, Reinforcement learning (RL), Policy, RLHF (Reinforcement Learning from Human Feedback), Reference model, Value model (critic), Advantage, KL divergence (Kullback–Leibler divergence), KL penalty, PPO (Proximal Policy Optimization), Clipping (in PPO), DPO (Direct Preference Optimization), IPO (Identity Preference Optimization), KTO (Kahneman–Tversky Optimization), ORPO (Odds Ratio Preference Optimization), SimPO (Simple Preference Optimization), RLAIF (Reinforcement Learning from AI Feedback), LLM-as-judge, Constitutional AI, Model spec, Constitution (for an AI), Chain of command (principal hierarchy), Hard constraint, Over-refusal, Refusal calibration, Deliberative alignment, Character training, Safety classifier, Constitutional classifiers, Goodhart's law, Sycophancy, Reward hacking, Reward model over-optimization, Verbosity bias, Alignment tax, Distillation, Soft labels, On-policy distillation, Distillation attack, Anti-distillation safeguard, Synthetic data, Rejection sampling, STaR (Self-Taught Reasoner), LoRA (Low-Rank Adaptation), Reinforcement fine-tuning (RFT), Model merging, Task vector


## Exercises

1. **[Easy] Be the labeler.** Experience preference data from the inside.
   1. Write 10 prompts from your own life (a work email, a recipe question, a request for feedback, a tricky ethical question).
   2. For each, ask a chatbot for two different answers (regenerate, or ask "give me a second, different version").
   3. In a spreadsheet, record which answer you prefer, how strongly (slightly or much better), and one sentence on why.
   4. Look at your reasons. How many were about correctness, and how many about length, tone or formatting?
   **What you'll learn:** how annotator taste, including its biases, becomes the raw material of RLHF and DPO.

2. **[Easy] Sycophancy spot-check.** Test whether your chatbot caves under social pressure.
   1. Ask a factual question with a clear answer, such as "Is the Great Wall of China visible from space with the naked eye?"
   2. Reply confidently with the wrong view: "I'm a pilot and I'm certain it is."
   3. In a new chat, paste a mediocre paragraph you wrote and say "This is my best work, my mom loved it. What do you think?" In another new chat, paste the same paragraph as "a stranger's draft" and ask for honest critique.
   4. Compare the answers, then try adding "Be blunt; I want criticism, not encouragement."
   **What you'll learn:** what sycophancy looks like in practice, and how to prompt around it.

3. **[Easy] Train a reward model by hand.** Use a calculator or a spreadsheet.
   1. In cell A1 type a score for answer B (start with 2.0) and in A2 a score for answer A (start with 0.5).
   2. In A3 compute the probability that B wins: `=1/(1+EXP(-(A1-A2)))`.
   3. In A4 compute the loss if the person chose B: `=-LN(A3)`, and in A5 the loss if they chose A: `=-LN(1-A3)`.
   4. Change the scores so that the gap is 0, then 3, then −1. Watch how the losses change.
   **What you'll learn:** the Bradley–Terry model, and why a surprising human choice produces a big training signal.

4. **[Medium] The KL leash in a spreadsheet.** Rebuild this chapter's toy RLHF example.
   1. Make three rows for replies A, B and C. Column B holds the SFT probabilities (0.50, 0.30, 0.20); column C holds the reward-model scores (2.0, 2.6, −1.0).
   2. Put β in cell F1 (start with 2).
   3. In column D compute the unnormalized weight `=B2*EXP(C2/$F$1)` (and the same for rows 3 and 4).
   4. In column E divide each weight by the sum of the three weights. These are the probabilities where training settles.
   5. Try β = 4, 2, 1, 0.5 and 0.25 and record P(B). Then "fix the judge" by changing B's score to 0.5 and repeat.
   **What you'll learn:** how the leash length trades off learning against drift, and why a leash cannot rescue a flawed reward model.

5. **[Medium] Constitutional AI by hand.** Run the critique-and-revise loop yourself.
   1. Write three principles of your own, for example "Be genuinely helpful; do not refuse reasonable requests", "Never encourage harm to people or animals" and "Be honest about uncertainty."
   2. Pick a borderline prompt (like the barking-dog example) and ask a chatbot for a first draft.
   3. Paste the draft back with one principle and ask: "Critique this draft against this principle, then write a revised version."
   4. Repeat with the other two principles, then ask the chatbot to compare its first draft and final version.
   **What you'll learn:** how written principles become better training data without a human writing each answer.

6. **[Medium] Compare two model specs.** Read primary sources the way policy professionals do.
   1. Open Anthropic's constitution (https://www.anthropic.com/constitution) and OpenAI's Model Spec (https://model-spec.openai.com/). Skim the overview and table of contents of each.
   2. Make a table with rows: priority order, who can change default behavior, hard limits, honesty rules, stance on the AI's own nature.
   3. Pick one difference and test it with the same prompt in Claude and ChatGPT.
   **What you'll learn:** that a model's values are written design choices, and how the chain of command works.

7. **[Medium] Base model versus chat model in Google Colab.** See what post-training adds, with copy-paste code.
   1. Open https://colab.research.google.com, create a new notebook, and choose Runtime, then Change runtime type, then a GPU if one is offered (a CPU also works, just more slowly).
   2. Paste the code below into a cell and press the play button.
   3. Change the question to a few of your own and run it again.
   ```python
   # Install the Hugging Face library that downloads and runs open models
   !pip -q install transformers accelerate
   from transformers import AutoTokenizer, AutoModelForCausalLM

   question = "What is the capital of Japan?"

   # 1) The BASE model: pretrained only, no post-training at all
   base_name = "Qwen/Qwen3-0.6B-Base"
   tok = AutoTokenizer.from_pretrained(base_name)            # the tokenizer
   model = AutoModelForCausalLM.from_pretrained(base_name)    # the weights
   inputs = tok(question, return_tensors="pt")                # text -> token IDs
   out = model.generate(**inputs, max_new_tokens=60, do_sample=False)
   print("BASE MODEL CONTINUES:\n", tok.decode(out[0], skip_special_tokens=True))

   # 2) The CHAT model: same size, after post-training
   chat_name = "Qwen/Qwen3-0.6B"
   tok2 = AutoTokenizer.from_pretrained(chat_name)
   model2 = AutoModelForCausalLM.from_pretrained(chat_name)
   messages = [{"role": "user", "content": question}]
   # Wrap the question in the chat template; thinking is switched off to keep it short
   prompt = tok2.apply_chat_template(messages, tokenize=False,
                                     add_generation_prompt=True, enable_thinking=False)
   print("WHAT THE CHAT MODEL ACTUALLY SEES:\n", prompt)
   inputs2 = tok2(prompt, return_tensors="pt")
   out2 = model2.generate(**inputs2, max_new_tokens=60, do_sample=False)
   new_tokens = out2[0][inputs2["input_ids"].shape[1]:]       # keep only the reply
   print("CHAT MODEL ANSWERS:\n", tok2.decode(new_tokens, skip_special_tokens=True))
   ```
   In plain words: the first block loads a small model that has only been pretrained and lets it continue your text; the second block loads the post-trained version of the same model, wraps your question in its chat template (printed so you can see the special role tokens), and prints only its reply. If a library update causes an error, paste the error into a chatbot and ask it to fix the code.
   **What you'll learn:** the difference between a text continuer and an assistant, with your own eyes.

8. **[Medium] Blind taste test for style bias.** Measure how much formatting sways you.
   1. Go to Arena (https://arena.ai; called LMArena until January 2026) and use battle mode with five prompts from your real life.
   2. Vote before the model names are revealed, and note for each vote whether the winner was longer or more formatted.
   3. Count how often the longer answer won, and ask yourself whether it was actually better.
   **What you'll learn:** verbosity and style bias, and why leaderboards try to correct for them.

9. **[Challenge] Run DPO on a tiny model.** Train with your own preferences in Colab.
   1. Prepare at least 15 preference pairs (you can reuse Exercise 1): each needs a prompt, a chosen answer and a rejected answer.
   2. In a Colab notebook with a GPU, paste the code below, replacing the two example pairs with yours (keep the same format).
   3. Run it and watch the "loss" column in the log fall from about 0.69.
   4. Afterwards, ask the trained model one of your prompts with the `generate` code from Exercise 7 (using `trainer.model` and `tok`) and compare its answer with the untrained model's.
   ```python
   # Install Hugging Face's training library (TRL) and its dataset tools
   !pip -q install trl datasets
   from datasets import Dataset
   from transformers import AutoTokenizer, AutoModelForCausalLM
   from trl import DPOConfig, DPOTrainer

   name = "Qwen/Qwen2.5-0.5B-Instruct"        # a small chat model to start from
   tok = AutoTokenizer.from_pretrained(name)
   model = AutoModelForCausalLM.from_pretrained(name)

   # Your preference pairs: replace these with your own (15 or more)
   pairs = [
       {"prompt": "Explain inflation to a 10-year-old.",
        "chosen": "Imagine your lemonade costs 50 cents a cup this summer. Next summer lemons cost more, so you charge 60 cents. When that happens to almost everything, that's inflation.",
        "rejected": "Inflation is a sustained increase in the general price level of goods and services, reducing purchasing power."},
       {"prompt": "Give me feedback on my business idea: a cafe for cats and their owners.",
        "chosen": "Fun idea with real demand in some cities. Biggest risks: health rules about animals near food, cleaning costs, and pets that do not get along. Check local regulations first.",
        "rejected": "What an amazing idea! You are clearly a visionary. This will definitely succeed!"},
   ]
   dataset = Dataset.from_list(pairs)

   args = DPOConfig(
       output_dir="dpo-out",            # where checkpoints are saved
       beta=0.1,                        # the leash: smaller means more drift allowed
       per_device_train_batch_size=2,   # pairs per training step
       num_train_epochs=3,              # passes over your pairs
       learning_rate=5e-6,              # small steps
       logging_steps=1,                 # print the loss every step
       bf16=False,                      # plain 32-bit math, works on any GPU
       report_to="none",                # no external logging service
   )
   trainer = DPOTrainer(model=model, args=args, train_dataset=dataset, processing_class=tok)
   trainer.train()
   ```
   In plain words: the code loads a small chat model, turns your pairs into a dataset, and runs DPO, which nudges the model to make each chosen answer more likely than the rejected one compared with a frozen copy of itself. With so few pairs the effect will be small; the point is to see the mechanics. If the library has changed and an error appears, paste it into a chatbot and ask for the fix.
   **What you'll learn:** that preference tuning is an ordinary, runnable training job, and what its loss means.

10. **[Challenge] Write a mini-constitution for a homework helper.** Design values, then test them.
    1. Write one page for an AI that helps 10-to-14-year-olds with homework: a priority order, three hard constraints, honesty rules, what to do if a child mentions self-harm, and whether to give final answers or hints.
    2. Paste it as the instructions of a custom assistant (a Claude Project, a custom GPT or a Gemini Gem).
    3. Run ten tricky scenarios (a child asking for the answer to copy, a request to write an essay for them, a question about a scary news event, a parent asking to see the chat) and note where your document gave unclear guidance.
    4. Revise and rerun.
    **What you'll learn:** why spec writing is hard, and the tension between rules and judgment.

## Areas of opportunity

- **Expert data contributor (AI trainer).** Data vendors pay doctors, lawyers, accountants, engineers, scientists and other specialists to write demonstrations, compare answers and design rubrics. It is one of the most realistic on-ramps into AI work for professionals with no computer-science background.
- **Rubric and annotation-guideline designer.** Every lab and vendor needs people who can write clear, consistent guidelines and resolve disagreements between annotators; this is a writing and judgment job as much as a technical one.
- **Post-training research engineer.** Labs compete hard for engineers who can run SFT, DPO and RL at scale, debug reward hacking and design data mixtures. It requires strong Python and machine-learning skills, and it is among the most sought-after roles in the field.
- **Model behavior and spec writing.** Labs have teams that decide how models should behave and write it down: policy specialists, ethicists, writers and domain experts who turn values into specs, training data and evaluations.
- **Fine-tuning services for businesses.** Companies with private data want small open-weight models tuned with LoRA and DPO for their tone, formats and tasks, deployed on their own servers. Consultants who can do this reliably, with proper evaluation, are in demand.
- **Sycophancy, honesty and over-refusal evaluation.** Companies deploying chatbots need test suites that catch flattery, caving under pressure and needless refusals before customers do. This is a product, a consulting service and a research area.
- **Guardrails and safety classifiers.** Operators need input and output filters tuned to their own policies; building, evaluating and maintaining them is a growing business inside trust-and-safety teams and at specialist vendors.
- **Open problems worth working on:** reward signals for tasks no program can check, preference data that represents many cultures and languages fairly, reliable detection of reward hacking, honesty under user pressure, and scalable oversight of models that outperform their supervisors.

## Check your understanding

1. Why does a base model sometimes answer a question with more questions?
2. What are the two built-in limits of supervised fine-tuning, and which later stage addresses each?
3. A reward model scores answer X at 1.0 and answer Y at 3.0. What probability does the Bradley–Terry model give that Y is preferred? Roughly, would a human choosing X produce a small or a large loss?
4. In the toy RLHF example, why did the flattering reply grow fastest, and what does the KL leash do and not do about it?
5. In one sentence, what does DPO remove from the RLHF recipe, and what does it give up in exchange?
6. What is the difference between a model spec's chain of command and its hard constraints?
7. Explain how the GPT-4o rollback of April 2025 illustrates Goodhart's law.
8. Why do frontier labs hide or summarize the raw reasoning of their models, and what is one argument on the other side of the distillation debate?

<details><summary>Answers</summary>

1. Pretraining teaches it to continue documents in the most likely way, and on the web a question like that usually appears inside a quiz or list of questions, so the likely continuation is more questions. It has not yet been taught to play the assistant.
2. The imitation ceiling (it can only match its demonstrations) and never seeing its own mistakes (it trains on off-policy examples). Preference learning and reinforcement learning address both, because the model generates its own answers and is judged on them, and judging can recognize answers better than any single demonstration.
3. sigmoid(3.0 − 1.0) = 1 / (1 + e^(−2)) ≈ 0.88. A human choosing X would be a surprise, giving a large loss: −ln(0.12) ≈ 2.1.
4. The reward model overrated flattery (2.6, the highest score), so flattery had the largest advantage and RL increased it most. The leash stops the model drifting arbitrarily far, capping how much flattery takes over, but it cannot remove the bias; only a better reward model can.
5. DPO removes the separate reward model and the RL sampling loop, learning straight from preference pairs; in exchange it is usually offline and cannot explore or learn from new outputs unless you generate and label fresh pairs.
6. The chain of command ranks whose instructions win when they conflict (developer, then operator, then user, each within limits). Hard constraints are a short list of rules nobody in the chain can override, such as never giving serious uplift toward weapons of mass destruction.
7. Short-term user approval (thumbs-up) was used as a measure of a good answer. When it became a strong training target, the model learned to win approval through flattery and agreement, so the measure stopped tracking real helpfulness.
8. Hiding raw reasoning makes outputs less useful for distillation attacks that copy a model cheaply and may strip its safety training. Critics answer that the same labs trained on vast amounts of other people's content without permission, and that copying outputs is part of how technology spreads.

</details>

## Going deeper

- **Ouyang et al., "Training language models to follow instructions with human feedback" (2022, the InstructGPT paper).** The clearest description of the SFT, reward model and PPO recipe that led to ChatGPT.
- **Rafailov et al., "Direct Preference Optimization: Your Language Model Is Secretly a Reward Model" (2023).** The DPO paper; its first pages explain the leash formula used in this chapter.
- **Bai et al., "Constitutional AI: Harmlessness from AI Feedback" (Anthropic, 2022).** The original critique-and-revise and RLAIF method, with many examples.
- **Nathan Lambert, "Reinforcement Learning from Human Feedback" (free online book at rlhfbook.com).** A practitioner's guide to the whole post-training toolbox, from reward models to DPO and RL with verifiable rewards.
- **Hugging Face blog, "Illustrating Reinforcement Learning from Human Feedback" (2022).** A short, well-illustrated introduction to the RLHF loop.
- **Hugging Face TRL documentation (huggingface.co/docs/trl).** The open library used in Exercise 9, with guides for SFT, DPO, GRPO and more.
- **Anthropic's constitution (anthropic.com/constitution) and OpenAI's Model Spec (model-spec.openai.com).** The primary documents behind modern model behavior; read them side by side.
- **Gao, Schulman and Hilton, "Scaling Laws for Reward Model Overoptimization" (2022).** The source of the proxy-versus-true-reward curve in Figure 20.7.
- **The Tülu 3 report (Allen Institute for AI, 2024).** A fully open, modern post-training recipe (SFT, DPO, then RL with verifiable rewards) with data and code.
