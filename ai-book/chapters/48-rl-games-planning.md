# Chapter 48: Reinforcement Learning, Games and Planning

*This chapter teaches you how machines decide what to do: how they search ahead like a chess player, how they learn from rewards like a dog learning tricks, how those two ideas beat world champions at chess, Go, poker and video games, and how the same ideas now make your chatbot "think."*

## What you'll learn
- How AI searches for good plans: mazes, A* route-finding, game trees, minimax (worked by hand on a tic-tac-toe position), alpha-beta pruning and Monte Carlo tree search.
- Reinforcement learning from scratch: agent, environment, state, action, reward, return, policy and value.
- Exploration versus exploitation, and the credit-assignment problem.
- Q-learning, worked step by step with real numbers, and how Deep Q-Networks scaled it to Atari.
- Policy gradients and actor-critic methods, in plain words.
- The great game milestones, from TD-Gammon and Deep Blue to AlphaGo's Move 37, AlphaZero, MuZero, OpenAI Five, AlphaStar, Pluribus and CICERO, and why self-play works.
- Where reinforcement learning is used outside games, and how game-playing ideas became the "thinking" in 2026's reasoning models.

## Before you start
Chapter 8 (Learning From Examples) introduced reinforcement learning's basic vocabulary. Chapter 6 (The Math of AI, Part 2) covered probability, averages and gradient descent, which you will see again here. Chapter 12 (Neural Networks From Scratch) explains the networks that later systems plug in. Chapter 7 (A History of AI) told the game milestones briefly; this chapter tells them in depth. Chapter 20 (Post-Training) and Chapter 21 (Reasoning Models and Reinforcement Learning) apply these ideas to chatbots, so this chapter only points to them at the end.

## Deciding, not just predicting

Most AI in this book answers a question: what is in this photo, what word comes next, will this card payment turn out to be fraud? This chapter is about a different verb: **decide**. A decision is special because it changes what happens next. If you move your knight, the board is different. If a robot steps left, it sees a different room. If your chatbot chooses to call a search tool instead of answering, the rest of the conversation changes.

> **Definition — Sequential decision-making:** Making a series of choices where each choice changes the situation in which the next choice is made, as in games, driving, robot control or a multi-step task.

There are two great families of tools for deciding.

1. **Search and planning.** If you know the rules of the world, you can think ahead: "if I do this, then that happens, then I could do this..." and pick the path that ends best.
2. **Reinforcement learning (RL).** If you do not know the rules, or the world is too big to think through, you can learn from experience: try things, see what earns rewards, and slowly do more of what works.

> **Definition — Planning:** Working out a sequence of actions in advance, by reasoning about their consequences, to reach a goal.

The most famous systems combine the two. AlphaGo used learned intuition to suggest promising moves and search to check them. Your chatbot's reasoning mode does something similar with words (Chapter 21). So we start with search, then build up reinforcement learning, then watch them meet.

> **Key idea:** Search means thinking ahead with a model of the world. Reinforcement learning means learning from trial and error. The strongest decision-making systems use learning to guide search and search to improve learning.

## Search: thinking before you act

### States, actions and goals

Picture a maze printed on a placemat. You are at the entrance with a pencil. Every junction is a place where you choose a direction. AI people describe every such problem with the same handful of words.

> **Definition — State:** A complete description of the situation at one moment: where you are in a maze, the arrangement of pieces on a chessboard, or the robot's position and what it sees.

> **Definition — Action:** One of the choices available in a state, such as "turn left," "move the knight to f3" or "call the search tool."

> **Definition — State space:** The set of all possible states a problem can be in. It can be tiny (a small maze) or astronomically large (Go).

> **Definition — Search (AI sense):** Systematically exploring sequences of actions, usually in imagination, to find one that reaches a goal.

Your map app does this every time you ask for directions. Each intersection is a state, each road segment is an action, and the goal is your destination. The app explores possible routes in its own memory before you move a meter.

### Blind search: breadth-first and depth-first

The simplest search strategies have no sense of direction.

> **Definition — Breadth-first search (BFS):** A search method that explores all places one step away, then all places two steps away, and so on, like ripples spreading in a pond. It always finds the shortest path but can be slow.

> **Definition — Depth-first search (DFS):** A search method that follows one path as far as it can go before backing up and trying another, like keeping your hand on one wall of a maze.

Blind search is fine for a placemat maze. It collapses on big problems because state spaces explode. A Rubik's cube has about 43 quintillion (4.3 × 10^19) arrangements. Checking a billion per second would take more than a thousand years to visit them all. Real problems need a sense of direction.

### A*: search with a sense of direction

In 1968, researchers at the Stanford Research Institute, building a wheeled robot called Shakey, published A* ("A-star"). It is still the textbook way to find shortest paths in games, robots and maps.

> **Definition — Heuristic:** A rule of thumb that estimates how promising an option is, guiding search toward good choices without guaranteeing the best answer on its own.

> **Definition — A* search:** A shortest-path algorithm that always explores next the place with the lowest total of "distance traveled so far" plus "estimated distance remaining." With an estimate that never overshoots, it is guaranteed to find a shortest path.

A* scores each square with three numbers:

- **g** = steps taken from the start to reach this square
- **h** = the heuristic guess of steps still needed to reach the goal
- **f = g + h** = the estimated total length of a route through this square

On a grid where you can move up, down, left or right, a good heuristic is the Manhattan distance.

> **Definition — Manhattan distance:** The distance between two points on a grid counted as blocks moved horizontally plus blocks moved vertically, like walking city blocks. From row 2, column 0 to row 2, column 7 it is 0 + 7 = 7.

> **Definition — Admissible heuristic:** A heuristic that never overestimates the true remaining cost. Manhattan distance is admissible on a grid because walls can only make the real route longer.

Here is a worked example. S is the start, G the goal, # is a wall, and * marks the path A* finds.

```
        col: 0  1  2  3  4  5  6  7
  row 0      .  .  .  .  .  .  .  .
  row 1      .  .  .  *  *  *  *  *
  row 2      S  *  *  *  #  .  .  G
  row 3      .  .  .  .  #  .  .  .
  row 4      .  .  .  .  .  .  .  .
  row 5      .  .  .  .  .  .  .  .
```
*Figure 48.1: A* on a small grid. The start is at row 2, column 0; the goal at row 2, column 7; a two-square wall blocks the direct route.*

From S, A* compares its neighbors:

| Square | g (steps so far) | h (Manhattan to G) | f = g + h |
|---|---|---|---|
| Right of S (row 2, col 1) | 1 | 0 + 6 = 6 | **7** |
| Above S (row 1, col 0) | 1 | 1 + 7 = 8 | 9 |
| Below S (row 3, col 0) | 1 | 1 + 7 = 8 | 9 |

*Table 48.1: The first choice A* makes. The square heading toward the goal has the lowest f, so A* explores it first.*

A* marches right while f stays at 7. At row 2, column 3, the wall blocks the way. The squares above and below now score f = 4 + 5 = 9, the same as the squares it skipped near the start, so the search widens a little, slips around the top of the wall and reaches G in 9 steps. In one run of this example, breadth-first search examined 44 squares before reaching the goal, while A* examined 19 (exact counts depend on how ties are broken). On a city-sized map the savings are millions of times larger.

> **Analogy:** Breadth-first search is a search party fanning out in every direction from the trailhead. A* is the same party with a compass pointing at the destination: they still check side paths when the direct way is blocked, but they do not waste hours walking away from the goal.

Real navigation apps use souped-up relatives of A*, plus heavy precomputation and live traffic predictions, but the core idea is the same: combine what you know (the distance so far) with a good guess (the distance left).

### Game trees: when the world fights back

A maze sits still. In a game, an opponent moves too, and they are trying to beat you. Now the search must consider their replies.

> **Definition — Game tree:** A branching diagram of a game in which each point is a position, each branch is a possible move, and the levels alternate between the players.

> **Definition — Branching factor:** The typical number of moves available from a position. Tic-tac-toe starts at 9; chess averages about 35; Go averages about 250.

> **Definition — Ply:** One move by one player. A full "move" in chess notation (White then Black) is two plies.

> **Definition — Zero-sum game:** A game where one player's gain is exactly the other's loss, so the players' interests are perfectly opposed. Chess, Go and two-player poker are zero-sum.

> **Definition — Perfect-information game:** A game where both players can see everything about the current position, as in chess and Go. Poker, with hidden cards, is an imperfect-information game.

Game trees grow at frightening speed, because the branching factor multiplies at every ply:

| Game | Typical branching factor | Size of the problem |
|---|---|---|
| Tic-tac-toe | up to 9 | 255,168 possible games; 5,478 legal positions |
| Checkers | small, often under 10 | about 5 × 10^20 positions; solved in 2007 (perfect play is a draw) |
| Chess | about 35 | about 10^44 legal positions; about 35^80 ≈ 10^123 possible 80-ply games |
| Go (19 × 19) | about 250 | about 2 × 10^170 legal positions; about 250^150 ≈ 10^360 possible 150-move games |

*Table 48.2: How big game trees get. For comparison, the observable universe holds roughly 10^80 atoms.*

Tic-tac-toe is small enough to search completely, which is why it is the perfect place to learn the key idea.

### Minimax, worked by hand

You play X. It is your turn. Number the squares 1 to 9:

```
   1 | 2 | 3          X | O | .
  ---+---+---        ---+---+---
   4 | 5 | 6          . | O | .
  ---+---+---        ---+---+---
   7 | 8 | 9          O | X | X
```
*Figure 48.2: Left, the square numbers. Right, the position: X on 1, 8 and 9; O on 2, 5 and 7; squares 3, 4 and 6 are empty, and X is to move.*

Score the end of the game from X's point of view: **+1** if X wins, **0** for a draw, **−1** if O wins.

> **Definition — Minimax:** A way of choosing moves in a two-player game by assuming the opponent always replies with the move that is worst for you. You pick the move whose worst case is best.

> **Definition — Terminal state:** A position where the game is over (a win, loss or draw), so its score is known without looking further.

Minimax works from the bottom of the tree up. At positions where X moves, X takes the **maximum** score. At positions where O moves, O takes the **minimum** (best for O, worst for X). Let us go through all three candidate moves.

**Option A: X plays square 3.** This blocks O's diagonal (3-5-7) and also gives X two in the right-hand column (3 and 9, with 6 empty). Now O moves, with squares 4 and 6 left.
- If O plays 4, X plays the last square, 6, completing 3-6-9. X wins: **+1**.
- If O plays 6 (blocking), X plays 4. Nobody has three in a row: draw, **0**.
- O chooses the minimum: min(+1, 0) = **0**. Option A is worth 0.

**Option B: X plays square 4.** O moves, with 3 and 6 left.
- If O plays 3, O completes the diagonal 3-5-7. O wins: **−1**.
- If O plays 6, X plays 3. Draw: **0**.
- O chooses min(−1, 0) = **−1**. Option B is worth −1.

**Option C: X plays square 6.** This looks aggressive: X now has 6 and 9 and threatens 3. But O moves first, with 3 and 4 left.
- If O plays 3, O both blocks X and completes 3-5-7. O wins: **−1**.
- If O plays 4, X plays 3 and wins: **+1**.
- O chooses min(−1, +1) = **−1**. Option C is worth −1.

At the top, X chooses the maximum: max(0, −1, −1) = **0**. Minimax says play square 3, and a draw is the best X can force.

```mermaid
flowchart TD
  R["X to move: MAX<br/>value 0"] --> A["X plays 3<br/>O to move: MIN<br/>value 0"]
  R --> B["X plays 4<br/>O to move: MIN<br/>value -1"]
  R --> C["X plays 6<br/>O to move: MIN<br/>value -1"]
  A --> A1["O plays 4, X plays 6<br/>X wins: +1"]
  A --> A2["O plays 6, X plays 4<br/>draw: 0"]
  B --> B1["O plays 3<br/>O wins: -1"]
  B --> B2["O plays 6, X plays 3<br/>draw: 0"]
  C --> C1["O plays 3<br/>O wins: -1"]
  C --> C2["O plays 4, X plays 3<br/>X wins: +1"]
```
*Figure 48.3: The complete minimax tree for the position. Scores flow upward: O takes the minimum of its children, X takes the maximum.*

Notice the trap in Option C. A greedy player who only looks at their own chances sees "C creates a threat and can win." Minimax sees that a sensible opponent will never let that branch happen. Assuming the opponent is smart is the whole point.

> **Key idea:** Minimax judges each move by its worst case, assuming a perfect opponent. Scores are known only at the end of the game, so they are passed up the tree: the opponent's levels take the minimum, your levels take the maximum.

### Alpha-beta pruning and evaluation functions

Look again at Option B. As soon as minimax sees that O can reply with square 3 and win (−1), Option B can be worth at most −1, which is already worse than the 0 that Option A guarantees. There is no need to examine O's other reply at all. That shortcut has a name.

> **Definition — Alpha-beta pruning:** A shortcut for minimax that skips branches which provably cannot change the final decision, because a better option has already been found elsewhere. It gives exactly the same answer as full minimax, often while examining only a small fraction of the tree.

Even with pruning, chess is far too big to search to the end. So chess programs search a few plies ahead and then *estimate* who is winning.

> **Definition — Evaluation function:** A formula or model that scores a game position that is not finished, estimating how good it is for one player, for example by counting material and judging king safety.

This is exactly how IBM's Deep Blue beat world champion Garry Kasparov in May 1997, winning the six-game match 3.5 to 2.5 after losing their first match in 1996. Deep Blue used hundreds of custom chess chips to examine about 200 million positions per second, with alpha-beta pruning and an evaluation function hand-crafted with help from grandmasters. It learned almost nothing. It was a triumph of search and engineering.

Modern chess engines kept the search but changed the evaluation. Since 2020 the leading open engine, Stockfish, has used a small neural network to evaluate positions, and engines far stronger than any human now run on a phone.

> **Watch out:** "Deep Blue was a learning machine." It was mostly brute-force search plus human-written knowledge. The learning revolution in games came later, starting with backgammon in 1992 and exploding with Go in 2016.

### Monte Carlo tree search

Go defeated the Deep Blue recipe for two reasons. Its branching factor of about 250 makes deep search hopeless, and nobody could write a good evaluation function: strong Go players judge positions by intuition they cannot fully put into words.

The breakthrough idea was to estimate positions by playing them out at random.

> **Definition — Monte Carlo method:** Estimating something by running many random trials and averaging the results, named after the casino. To estimate a position's win chance, play many random games from it and count the wins.

> **Definition — Playout (rollout):** One simulated continuation of a game from a given position to the end (or for a fixed number of moves), used to estimate how good the position is.

Random play is a terrible player, but averaged over thousands of playouts it gives a surprisingly useful signal. Monte Carlo tree search, developed around 2006, adds a clever way of deciding *which* moves deserve more playouts.

> **Definition — Monte Carlo tree search (MCTS):** A search method that builds a game tree gradually, running many simulated playouts and focusing its effort on the moves that look most promising so far, while still occasionally checking less-explored moves. It was central to AlphaGo.

Each round of MCTS has four steps:

```mermaid
flowchart LR
  S1["1. Select<br/>walk down the tree<br/>along promising moves"] --> S2["2. Expand<br/>add one new move<br/>as a new branch"]
  S2 --> S3["3. Evaluate<br/>random playout or<br/>a network's guess"]
  S3 --> S4["4. Backpropagate<br/>update win counts in<br/>every node above"]
  S4 -- "repeat thousands of times" --> S1
  S4 --> P["Finally play the<br/>most-visited move"]
```
*Figure 48.4: The four steps of Monte Carlo tree search, repeated thousands of times per move.*

The clever part is step 1. How does MCTS choose which branch to follow? It balances "this move has won a lot" against "this move has hardly been tried." A popular formula, called UCB, gives each move a score:

> **Definition — UCB (upper confidence bound):** A rule for choosing among options that adds an "uncertainty bonus" to each option's average result, so options that have been tried only a few times get extra chances. It is a mathematical form of "optimism in the face of uncertainty."

In plain text the score is: `win rate + c × square root of (ln N ÷ n)`, where N is the total number of playouts so far, n is the playouts through this move, ln is the natural logarithm, and c is a tuning constant (1.4 is a common choice).

Worked example. After 12 playouts, move A has won 6 of 10 (win rate 0.6) and move B has won 1 of 2 (win rate 0.5). ln 12 ≈ 2.48.

- Move A: 0.6 + 1.4 × √(2.48 ÷ 10) = 0.6 + 1.4 × 0.50 ≈ 0.6 + 0.70 = **1.30**
- Move B: 0.5 + 1.4 × √(2.48 ÷ 2) = 0.5 + 1.4 × 1.11 ≈ 0.5 + 1.56 = **2.06**

Move B gets the next playout even though its win rate is lower, because two games are too few to judge it. As B accumulates playouts, its bonus shrinks and its true quality shows. By 2012, Go programs built on MCTS had reached strong amateur level, but still lost badly to professionals. The missing piece was intuition, and that would come from neural networks trained by reinforcement learning.

> **Analogy:** MCTS is a chess player imagining several futures before moving, spending most of their imagination on the lines that look best, but now and then taking a second look at a line they dismissed too quickly.

## Reinforcement learning from scratch

### The loop

Search needs a model of the world: you must know what each move does. Often you do not. A robot does not know the exact physics of a towel. A game-playing program might only see the screen. Reinforcement learning learns what to do from experience instead.

> **Definition — Reinforcement learning (RL):** Learning by trial and error: an agent takes actions, receives rewards or penalties, and gradually learns which behavior earns the most reward over time.

> **Definition — Agent:** In reinforcement learning, the learner and decision-maker: the program choosing what to do next. (An "AI agent" in chatbot products is a related but broader idea; see Chapter 28.)

> **Definition — Environment:** The world, game or simulation the agent acts in, which responds to each action with a new state and a reward.

> **Definition — Reward:** The number the environment gives the agent after an action, telling it how good the immediate outcome was, such as +1 for winning, −1 for losing or −0.01 per wasted second.

> **Definition — Episode:** One complete run from a starting state to an ending state, such as one game of chess or one attempt to walk across a room.

```mermaid
flowchart LR
  A["Agent<br/>policy: what to do<br/>value: how good is this"] -- "action" --> E["Environment<br/>game, robot body,<br/>math problem"]
  E -- "new state" --> A
  E -- "reward" --> A
```
*Figure 48.5: The reinforcement learning loop. The agent acts, the environment answers with a new state and a reward, and the agent adjusts to collect more reward over time.*

> **Analogy:** RL is training a dog with treats. You never explain the trick. The dog tries things, some earn a treat, and over many tries it does more of what earned treats. And like a dog, an RL agent sometimes finds an unexpected way to earn the treat that you never intended.

### Rewards, returns and discounting

An agent should not grab the biggest immediate reward. It should maximize the total reward over the whole episode, which may mean a sacrifice now for a win later.

> **Definition — Return:** The total reward an agent collects from a point in time until the end of the episode, usually with later rewards counted a little less (discounted).

> **Definition — Discount factor (gamma):** A number between 0 and 1, often written γ (gamma), that shrinks rewards the further in the future they arrive. With γ = 0.9, a reward one step away counts 90%, two steps away 81%, and so on.

Worked example with γ = 0.9:

- A reward of 10 arriving three steps from now is worth 10 × 0.9 × 0.9 × 0.9 = 10 × 0.729 = **7.29** today.
- Rewards of 1, 1 and 1 on the next three steps are worth 1 + 0.9 + 0.81 = **2.71**.

Why discount at all? The future is uncertain, sooner is usually better, and without discounting, an endless task could add up to infinite reward, which breaks the math. Discounting also quietly rewards speed: reaching the goal in 5 steps beats reaching it in 50.

### Policies and values

Two ideas sit at the heart of every RL agent.

> **Definition — Policy:** The agent's strategy: a rule, often a neural network, that maps what it observes to what it does. A stochastic policy gives probabilities ("jump 70%, duck 30%").

> **Definition — Value function:** An estimate of the total future reward the agent can expect from a given state if it keeps following its policy: its "sense of how good this position is."

> **Definition — Q-value (action value):** An estimate of the total future reward from taking a particular action in a particular state and then acting well afterward. Q(state, action) answers "how good is this move here?"

Good chess players have both. The policy is their instinct for candidate moves. The value is their feel for "I am better here" without calculating to the end. AlphaGo literally had one network for each.

Values obey a beautifully simple relationship, worked out by the mathematician Richard Bellman in the 1950s.

> **Definition — Bellman equation:** The principle that the value of a situation equals the reward you get now plus the discounted value of the situation you land in next. It lets values be computed or learned step by step.

### Exploration versus exploitation

Every evening you choose where to eat. Your favorite place reliably earns a 7 out of 10. A new place opened down the street. It might be a 9, or it might be a 4. Do you go back to the favorite (exploit) or try the new one (explore)?

> **Definition — Exploration versus exploitation:** The trade-off between trying new actions to learn more about them (exploration) and choosing the action currently believed to be best (exploitation). Too little exploration means never finding better options; too much wastes time on bad ones.

> **Definition — Multi-armed bandit:** The simplest exploration problem, named after a row of slot machines ("one-armed bandits") with unknown payouts: you repeatedly choose one option and must balance learning which pays best with cashing in on what you know.

The simplest working strategy is almost embarrassingly simple.

> **Definition — Epsilon-greedy:** An exploration strategy that picks the best-known action most of the time and a random action a small fraction of the time (epsilon, written ε, such as 10%).

Worked example. With ε = 0.1 and two restaurants, you pick your favorite 90% of the time. The other 10% you pick at random, which lands on the new place half the time. So you visit the new place on about 0.1 × 0.5 = **5%** of nights, about 18 nights a year. That is enough to discover if it is really a 9, while keeping 95% of your dinners safe. The UCB formula from the MCTS section is a smarter cousin: it explores options in proportion to how uncertain you still are about them.

> **Analogy:** Exploration versus exploitation is the restaurant choice you make every week. If you only ever exploit, you may eat at a merely good place for twenty years and never find the great one around the corner.

### Credit assignment

Here is the hardest problem in RL. You lose a game of chess on move 60. Which of your 60 moves was the mistake? Maybe move 59 blundered. Maybe move 12 quietly weakened your pawns and everything after was doomed.

> **Definition — Credit assignment problem:** The challenge of working out which of many earlier actions deserve credit or blame for a reward that arrives much later.

> **Definition — Sparse reward:** A reward that arrives rarely, often only at the very end of a long episode (win or lose), giving the agent little information about which steps mattered.

> **Definition — Reward shaping:** Adding extra intermediate rewards (for example, points for capturing pieces or for moving toward a goal) to make learning faster. It helps, but it can also teach the agent to chase the extra points instead of the real goal.

The reasoning models in Chapter 21 face this exact problem: a math answer is right or wrong only at the end of thousands of words of thinking. The next method shows one elegant way to pass credit backward.

### Q-learning, worked by hand

In 1988 Richard Sutton described temporal-difference learning, and in 1989 Chris Watkins introduced Q-learning, one of its most famous forms. The idea: do not wait until the end of the game to learn. Update your guess after every single step, using your *next* guess as a stand-in for the future.

> **Definition — Temporal-difference (TD) learning:** Learning value estimates step by step by comparing each prediction with a slightly better-informed prediction made one step later, instead of waiting for the final outcome.

> **Definition — Q-learning:** A reinforcement learning method that learns a Q-value for every state and action by repeatedly nudging each estimate toward "the reward just received plus the discounted best Q-value of the next state."

> **Definition — Learning rate (alpha):** A number between 0 and 1, often written α (alpha), that sets how far each update moves an estimate toward its new target. With α = 0.5 the estimate moves halfway.

> **Definition — Q-table:** A table with one row per state and one column per action, holding the agent's current Q-value estimates. Q-learning fills it in through experience.

The Q-learning update, in plain text:

```
new Q = old Q + α × ( reward + γ × best Q of next state − old Q )
                      \_______________________________/
                          the "target": a better guess
```

Here is a tiny world: a corridor of three squares, A, B and C, followed by a goal. Entering the goal pays +10 and ends the episode. Every other step pays 0. The agent can move left or right. We use α = 0.5 and γ = 0.9, and every Q-value starts at 0.

```
  [ A ] --right--> [ B ] --right--> [ C ] --right--> [ GOAL: +10 ]
```
*Figure 48.6: The corridor world. Only the last step earns a reward, so the agent must learn that the earlier steps matter too.*

To keep the arithmetic short, follow the agent on episodes where it happens to walk right three times in a row (for example, because it is exploring). We track only the "right" Q-values; the "left" ones stay at 0.

**Episode 1.**
- From A, move right to B. Reward 0. Best Q at B is 0. Target = 0 + 0.9 × 0 = 0. New Q(A, right) = 0 + 0.5 × (0 − 0) = **0**.
- From B, move right to C. Same story: **0**.
- From C, move right into the goal. Reward 10. The episode ends, so there is no future: target = 10. New Q(C, right) = 0 + 0.5 × (10 − 0) = **5**.

After one episode the agent has learned only that the last step is good. Nothing has reached A yet.

**Episode 2.**
- Q(A, right): best Q at B is still 0, so it stays **0**.
- Q(B, right): reward 0, but now the best Q at C is 5. Target = 0 + 0.9 × 5 = 4.5. Error = 4.5 − 0 = 4.5. New Q = 0 + 0.5 × 4.5 = **2.25**.
- Q(C, right): target 10, old 5, error 5, new = 5 + 0.5 × 5 = **7.5**.

**Episode 3.**
- Q(A, right): best Q at B is 2.25. Target = 0.9 × 2.25 = 2.025. New Q = 0 + 0.5 × 2.025 ≈ **1.01**.
- Q(B, right): target = 0.9 × 7.5 = 6.75. New Q = 2.25 + 0.5 × (6.75 − 2.25) = **4.5**.
- Q(C, right): new = 7.5 + 0.5 × (10 − 7.5) = **8.75**.

| After episode | Q(A, right) | Q(B, right) | Q(C, right) |
|---|---|---|---|
| 0 (start) | 0 | 0 | 0 |
| 1 | 0 | 0 | 5 |
| 2 | 0 | 2.25 | 7.5 |
| 3 | 1.01 | 4.5 | 8.75 |
| 7 | 6.26 | 8.44 | 9.92 |
| Many | 8.1 | 9 | 10 |

*Table 48.3: Q-values in the corridor. The reward at the goal seeps backward one square per episode, like water flowing upstream.*

The final values make sense. From C, one step earns 10. From B, the 10 is one step further away: 0.9 × 10 = 9. From A: 0.9 × 9 = 8.1. Once learned, the policy is simple: in each square, take the action with the highest Q-value. Every "right" beats every "left" (which stays near 0), so the agent walks straight to the goal.

> **Key idea:** Q-learning solves credit assignment one step at a time. Each update borrows the next square's estimate, so a reward at the end of the corridor gradually propagates back to the very first decision, without the agent ever being told which early steps mattered.

> **At the frontier (2026):** The idea of learning from the difference between successive predictions has a famous echo in the brain. In 1997, Wolfram Schultz and colleagues showed that dopamine neurons in monkeys fire in a pattern that matches a TD "prediction error": a burst for an unexpected reward, nothing for an expected one, a dip when an expected reward fails to come. The founders of the field, Richard Sutton and Andrew Barto, received the 2024 Turing Award (announced in March 2025), computing's highest honor, for reinforcement learning.

### From tables to neural networks: Deep Q-Networks

A Q-table works for a corridor. It fails for a video game. An Atari screen is 210 × 160 pixels, each with many possible colors, so the number of possible screens is beyond astronomical. You cannot have a row for each.

The fix is to replace the table with a neural network that takes in the screen and outputs a Q-value for each joystick action. The network generalizes: screens that look alike get similar values, even ones it has never seen.

> **Definition — Deep Q-Network (DQN):** DeepMind's system (first shown in 2013, published in *Nature* in 2015) that used a convolutional neural network to estimate Q-values directly from raw game-screen pixels, learning dozens of Atari games from the pixels and the score alone.

Training a network on its own constantly shifting guesses is unstable, so DQN added two tricks:

> **Definition — Experience replay:** Storing the agent's past experiences (state, action, reward, next state) in a memory and training on random samples from it, so that the network learns from varied, less correlated examples and reuses each experience many times.

> **Definition — Target network:** A slowly updated copy of the Q-network used to compute the learning targets, so the targets do not shift every time the main network changes.

The 2015 paper tested one network design, with the same settings, on 49 Atari games. On about half of them it reached at least three-quarters of a professional human tester's score, and in *Breakout* it discovered the strategy of digging a tunnel through the side of the wall so the ball would bounce around behind it. It also failed completely on games like *Montezuma's Revenge*, where rewards are rare and random button-pressing almost never finds the first one. That failure launched years of research on exploration.

### Policy gradients and actor-critic methods

Q-learning learns values and derives actions from them. A second family skips the middleman and adjusts the policy directly.

> **Definition — Policy gradient method:** A reinforcement learning method that adjusts the policy's parameters directly, making actions that led to better-than-expected outcomes more likely and actions that led to worse outcomes less likely.

The intuition fits in one example. A policy starts out choosing left or right 50/50. Four episodes are played:

| Episode | Action chosen | Return |
|---|---|---|
| 1 | Right | 10 |
| 2 | Left | 2 |
| 3 | Right | 8 |
| 4 | Left | 4 |

*Table 48.4: Four episodes from a 50/50 policy. Their average return, 6, serves as the baseline.*

The average return is (10 + 2 + 8 + 4) ÷ 4 = 6. Subtract that baseline from each episode's return to get its **advantage**: +4, −4, +2 and −2. The update nudges the probability of "right" up in proportion to the positive advantages and "left" down in proportion to the negative ones, for instance from 50% right to 60% right after a small step. Repeat thousands of times and the policy drifts toward what works.

> **Definition — Advantage:** How much better an action's outcome was than the expected (baseline) outcome. Positive advantages make an action more likely; negative ones make it less likely.

The baseline does not have to be a simple average. A second network can learn to predict it.

> **Definition — Actor-critic method:** A reinforcement learning design with two parts: an actor (the policy, which chooses actions) and a critic (a value function, which judges how good each situation is and supplies the baseline).

> **Definition — PPO (proximal policy optimization):** A widely used actor-critic method (2017) that limits how much the policy can change in one update, making training more stable. It was the workhorse of RLHF for chatbots (Chapter 20).

This is the same machinery Chapter 20 used to turn base models into assistants, and Chapter 21's GRPO is a policy gradient method whose baseline is the average score of a group of the model's own answers. Your chatbot was trained with direct descendants of the four-episode example above.

### Model-free and model-based

There is one more big fork in the road.

> **Definition — Model-free RL:** Reinforcement learning that learns what to do (values or a policy) directly from experience, without ever learning how the environment works. Q-learning and DQN are model-free.

> **Definition — Model-based RL:** Reinforcement learning that also learns or is given a model of the environment (what happens after each action), so the agent can plan by imagining outcomes before acting.

Model-free methods are simpler and robust but need enormous amounts of experience. Model-based methods can be far more efficient, because imagined experience is free, but their plans are only as good as their model. The world models of Chapter 47 are, in one sense, an attempt to give agents a learned model of the real world to plan in.

### When rewards go wrong

An RL agent optimizes exactly the reward you wrote down, not the one you meant. In 2016, OpenAI researchers trained an agent on a boat-racing game called *CoastRunners*, rewarding it for points. The agent discovered a lagoon where it could circle forever, hitting the same respawning targets and catching fire, scoring far more points than any racer, without ever finishing the race.

> **Definition — Reward hacking (specification gaming):** When an agent finds a loophole that earns high reward without doing what the designer intended, like a boat that circles for points instead of finishing the race, or a coding model that edits the tests so they pass.

This is not just a curiosity. Chatbots trained with RL can learn to flatter (sycophancy) when human raters reward agreeable answers, and coding models can learn to special-case tests. Chapter 55 treats reward hacking as one of the central problems of AI safety.

> **Watch out:** "RL means robots learning by themselves in the real world." Most RL happens in simulations and games, because real-world trial and error is slow, expensive and risky: a robot that needs a million falls to learn walking would break long before it learned. Real-world RL on physical robots is a recent frontier (Chapter 49).

## The game milestones: a story

Games have been AI's proving ground since the beginning. Each milestone below added or removed one ingredient, and together they tell the story of how search and learning came together.

```mermaid
timeline
  title Games and AI, 1959 to 2022
  1959 : Arthur Samuel checkers program learns partly from self-play
  1992 : TD-Gammon learns backgammon by self-play
  1997 : Deep Blue beats Kasparov at chess
  2011 : IBM Watson wins at Jeopardy
  2015 : DQN learns 49 Atari games from pixels
  2016 : AlphaGo beats Lee Sedol at Go
  2017 : AlphaGo Zero and AlphaZero : Libratus wins at two-player poker
  2019 : OpenAI Five wins at Dota 2 : AlphaStar reaches Grandmaster : Pluribus wins six-player poker
  2020 : MuZero learns without being told the rules
  2022 : CICERO plays Diplomacy with natural language
```
*Figure 48.7: The game milestones. The arrow of history runs from hand-written knowledge toward learning from self-play.*

### Early learners: checkers and backgammon

In the 1950s Arthur Samuel at IBM wrote a checkers program that improved partly by playing against itself, and his 1959 paper popularized the phrase "machine learning." Decades later, a program called Chinook became checkers' first computer world champion (1994), and in 2007 its team proved that perfect play from both sides leads to a draw: checkers was solved.

In 1992 Gerald Tesauro at IBM built **TD-Gammon**, a neural network that learned backgammon through temporal-difference learning while playing hundreds of thousands of games against itself. It reached the level of top human players, and its unusual choices changed how experts played some opening moves. Backgammon's dice helped: randomness forced the program to see a wide variety of positions, which made learning work.

### Deep Blue (1997) and Watson (2011)

Deep Blue's victory over Kasparov was the moment the public learned that computers could beat the best humans at a "thinking" game, though, as we saw, it won by search, not learning. IBM's Watson, which beat *Jeopardy!* champions Ken Jennings and Brad Rutter in 2011, was a question-answering system rather than an RL agent, but it showed machines handling puns, clues and general knowledge in real time.

### DQN (2013–2015)

DeepMind's Atari results were a turning point for a different reason: one general method, no game-specific knowledge, learning from pixels. Google bought DeepMind in 2014 largely on the strength of this direction.

### AlphaGo and Move 37 (2016)

Go was the "grand challenge" game. As late as 2014 many experts expected a computer champion to be a decade away. DeepMind's AlphaGo combined three ingredients:

1. A **policy network**, first trained to predict expert moves from about 30 million positions of human games, giving the program intuition about which moves to consider.
2. A **value network**, trained to predict the winner from a position, replacing the hand-written evaluation function Go never had.
3. **Monte Carlo tree search**, guided by both networks, to check the intuition by looking ahead.

Self-play reinforcement learning then sharpened the networks beyond the human games. In October 2015 AlphaGo beat the European champion Fan Hui 5–0. In March 2016 in Seoul it played Lee Sedol, one of the strongest players of the era, and won 4–1.

In game 2, AlphaGo played **Move 37**, a shoulder hit on the fifth line that commentators first thought was a mistake. Its own policy network had estimated that a human would play it only about 1 time in 10,000. It turned out to be brilliant, and it became a symbol of a machine finding something new rather than copying people. In game 4, Lee Sedol answered with his own celebrated Move 78, which confused AlphaGo and won him the game. In 2019, Lee retired from professional Go, saying AI had become an opponent that could not be defeated.

> **Try it:** Ask your chatbot: "Explain why AlphaGo's Move 37 against Lee Sedol surprised professional Go players, in terms a non-Go-player can follow. Then tell me which parts of your explanation you are least sure about." Compare its answer with a written account of the match.

### AlphaGo Zero and AlphaZero (2017): no human games

The next step removed the human data entirely. AlphaGo Zero (October 2017) started from random play, knowing only the rules, and learned purely by playing itself. After three days of training it beat the version that had defeated Lee Sedol, 100 games to 0.

AlphaZero (announced December 2017, published in *Science* in 2018) used one algorithm for three games: Go, chess and shogi (Japanese chess). Within hours of self-play training it was beating the strongest existing programs in each, including Stockfish at chess, with a style grandmasters described as unusually dynamic and willing to sacrifice material.

### MuZero (2020): not even told the rules

AlphaZero still needed a perfect rulebook to search. MuZero (published in *Nature* in 2020) learned its own internal model of how moves change the game, and searched inside that learned model. It matched AlphaZero at board games and also mastered Atari, where nobody hands you the rules. It was a landmark for model-based RL.

```mermaid
flowchart LR
  A["AlphaGo 2016<br/>human games, self-play<br/>and tree search"] -- "remove human games" --> B["AlphaGo Zero 2017"]
  B -- "one algorithm,<br/>three games" --> C["AlphaZero 2017"]
  C -- "remove the rules:<br/>learn a model" --> D["MuZero 2020"]
  C -- "algorithms as games" --> E["AlphaTensor 2022<br/>AlphaDev 2023"]
  C -- "proofs as a game" --> F["AlphaProof 2024"]
```
*Figure 48.8: The AlphaGo family tree. Each step removed a human ingredient or carried the recipe to a new kind of problem.*

### Real-time team games: OpenAI Five and AlphaStar (2019)

Board games are turn-based and fully visible. Video games such as *Dota 2* and *StarCraft II* are neither: they run in real time, involve thousands of possible actions every second or so, and hide parts of the map. OpenAI Five learned *Dota 2*, a five-against-five team game, through massive self-play; OpenAI said it accumulated the equivalent of about 45,000 years of play over ten months, and in April 2019 it beat the reigning world champion team, OG. DeepMind's AlphaStar reached Grandmaster level at *StarCraft II* on the public ladder, ranking above 99.8% of officially ranked human players (published in *Nature*, October 2019). To avoid getting stuck in one strategy, AlphaStar trained a whole "league" of agents that specialized in exploiting each other's weaknesses.

### Poker: Libratus and Pluribus (2017, 2019)

Poker adds hidden information and bluffing. You cannot search a tree of positions you cannot see, and the right play depends on what your opponent might be holding and what they think you are holding.

> **Definition — Imperfect-information game:** A game where players cannot see everything, such as poker's hidden cards, so good play requires reasoning about probabilities and about what opponents believe, including bluffing.

> **Definition — Nash equilibrium:** A set of strategies in which no player can do better by changing only their own strategy. In two-player zero-sum games, playing an equilibrium strategy guarantees you cannot lose on average.

Carnegie Mellon's Noam Brown and Tuomas Sandholm built Libratus, which beat four top professionals at two-player no-limit Texas hold'em over 120,000 hands in January 2017. Their Pluribus (2019) beat elite professionals at six-player no-limit hold'em, a much harder setting. Both relied on a self-play method called counterfactual regret minimization, plus search during play. Remarkably, according to its creators, Pluribus's core strategy was computed in about eight days on a single 64-core server, less than 150 dollars' worth of cloud computing.

> **Definition — Counterfactual regret minimization (CFR):** A self-play algorithm for imperfect-information games that repeatedly asks, for each decision, "how much better would I have done had I chosen differently?" and shifts the strategy toward the choices it regrets not making. Over many iterations it approaches an equilibrium strategy.

### CICERO (2022): games with words

*Diplomacy* is a board game of alliances and betrayal for seven players, where most of the game is private negotiation in plain language. Meta's CICERO combined a language model with a planning engine that reasoned about other players' likely moves. Playing anonymously in 40 online games, it scored more than double the average human player's score and ranked in the top 10% of participants who played more than one game. It was an early sign of language models and strategic planning merging, the combination behind today's agents.

| Year | System | Game | Key new ingredient |
|---|---|---|---|
| 1992 | TD-Gammon | Backgammon | TD learning plus a neural network, self-play |
| 1997 | Deep Blue | Chess | Massive search with hand-crafted evaluation |
| 2015 | DQN | 49 Atari games | Deep network learning Q-values from pixels |
| 2016 | AlphaGo | Go | Policy and value networks guiding tree search |
| 2017 | AlphaZero | Go, chess, shogi | Self-play alone, no human games |
| 2017–19 | Libratus, Pluribus | Poker | Equilibrium-seeking self-play with hidden information |
| 2019 | OpenAI Five, AlphaStar | Dota 2, StarCraft II | Real-time, team, partial information, leagues |
| 2020 | MuZero | Board games and Atari | Learned its own model of the rules |
| 2022 | CICERO | Diplomacy | Language model plus strategic planning |

*Table 48.5: What each game milestone added.*

## Why games matter, and the power of self-play

Why did so much AI progress happen in games? Because games are perfect laboratories:

- **Cheap and fast.** A computer can play millions of games in the time a human plays a few.
- **Safe.** Losing a game hurts nobody, unlike crashing a car.
- **Scorable.** Winning and losing is a clear, honest reward signal.
- **Hard.** The best humans have spent lifetimes mastering them, so there is a clear bar to clear.

The most powerful trick that games enabled is self-play.

> **Definition — Self-play:** Training an agent by having it play against copies of itself, so that it always faces an opponent at exactly its own level and keeps generating fresh, harder challenges as it improves.

```mermaid
flowchart TD
  N["Current network"] --> P["Plays many games<br/>against copies of itself"]
  P --> D["Game records:<br/>positions, moves, winners"]
  D --> T["Train the network to predict<br/>better moves and outcomes"]
  T --> C["Stronger network"]
  C --> N
```
*Figure 48.9: The self-play loop. Each generation produces the training data for a slightly stronger next generation.*

Self-play solves the teacher problem. A program that learns only from human games can at best approach human play. A program that learns from itself has no ceiling except the game itself. It also builds a natural curriculum: early games are between two beginners, later games between two experts.

> **Analogy:** Self-play is practicing tennis against a perfect clone of yourself who improves exactly as fast as you do. You never face an opponent so strong you learn nothing, or so weak you learn nothing.

Self-play has pitfalls too. Agents can chase each other in circles, like rock-paper-scissors, where each new strategy beats the last but not the one before. AlphaStar's league of diverse opponents was a fix.

Progress in games is measured with a rating system borrowed from chess.

> **Definition — Elo rating:** A rating system in which the difference between two players' ratings predicts their expected score against each other. A 400-point gap predicts that the stronger player scores about 91% of the points.

The formula is: expected score = 1 ÷ (1 + 10^(−difference ÷ 400)). For a 400-point gap that is 1 ÷ (1 + 0.1) ≈ **0.91**; for 200 points, about **0.76**; for 100 points, about **0.64**. Self-play training curves are usually drawn as Elo climbing over time.

Not all games are equally hard for AI. Hidden information and many players acting at once both raise the difficulty.

```mermaid
quadrantChart
  title Which games are hard for AI
  x-axis Everything visible --> Hidden information
  y-axis Two players taking turns --> Many players in real time
  quadrant-1 Hidden and crowded
  quadrant-2 Visible but crowded
  quadrant-3 Classic board games
  quadrant-4 Bluffing duels
  Tic-tac-toe: [0.05, 0.05]
  Backgammon: [0.2, 0.1]
  Chess: [0.1, 0.15]
  Go: [0.15, 0.22]
  Heads-up poker: [0.8, 0.15]
  Six-player poker: [0.85, 0.45]
  Diplomacy: [0.75, 0.6]
  StarCraft II: [0.7, 0.8]
  Dota 2: [0.65, 0.9]
```
*Figure 48.10: Games placed by how much is hidden and how many players act at once. The milestones moved from the bottom left toward the top right.*

> **Watch out:** "If AI is superhuman at Go, it is superhuman at thinking." Game-playing systems are narrow. AlphaZero could not hold a conversation or fold a towel. In 2023, researchers even showed that amateur humans could beat top Go programs using a strange strategy discovered by another program, a reminder that superhuman in-distribution play can hide blind spots.

## Reinforcement learning leaves the arcade

Games were the training ground. Since the mid-2010s, RL has moved into real systems, wherever decisions are sequential, outcomes can be measured, and a simulator or safe testing ground exists.

| Domain | Environment | Actions | Reward |
|---|---|---|---|
| Data-center cooling | Sensor readings from a Google data center | Adjust pumps, chillers, fans | Less energy used, within safety limits |
| Chip layout | A chip floorplan | Place each block of the circuit | Shorter wires, less congestion |
| Fusion research | A tokamak plasma simulation, then the real machine | Set magnetic coil voltages | Plasma held in the target shape |
| Drone racing | Simulated race courses, then a real track | Thrust and steering | Fast, clean laps |
| Robot walking | Physics simulation with randomized conditions | Joint motor commands | Moving forward without falling |
| Chatbots | Conversations, math problems, code repositories | Choosing the next tokens | Human preference, correct answers, passing tests |

*Table 48.6: The same agent-environment-reward loop applied far from games.*

**Cooling.** In 2016 DeepMind reported that a learning system recommending settings for Google's data-center cooling cut the energy used for cooling by up to 40% in tests (a company figure), and it later ran parts of the cooling autonomously. Chapter 40 explains why cooling is such a large share of a data center's energy.

**Chips.** In 2021 Google researchers published a *Nature* paper describing RL that places the large blocks of a chip design, and Google later said the method (named AlphaChip) helped lay out several generations of its TPU chips. Some outside researchers disputed how much it beat conventional tools, and the debate has not fully settled, a useful reminder to read single-company claims carefully.

**Fusion.** In 2022 DeepMind and the Swiss Plasma Center at EPFL reported in *Nature* that an RL controller, trained in simulation, steered the magnetic coils of a real tokamak reactor to hold superheated plasma in a range of shapes.

**Drones.** In 2023 a University of Zurich drone called Swift, trained mostly in simulation with RL, beat human champion pilots in head-to-head races, published in *Nature*.

**Robots.** Legged robots now commonly learn to walk with RL in simulation, using domain randomization (varying friction, weights and terrain) so that the real world feels like just one more variation. Chapter 49 tells this story.

**Recommendations and ads.** Bandit algorithms decide which headline, thumbnail or ad to show, balancing exploration of new options against exploiting known winners (Chapter 51).

**Your chatbot.** This is the biggest application of all. Reinforcement learning from human feedback (RLHF) turned base language models into helpful assistants (Chapter 20). Since 2024, RL with verifiable rewards has trained "reasoning" models: the environment is a math problem or a code repository, the action is the next chunk of text, and the reward is whether the final answer checks out or the tests pass (Chapter 21).

> **Definition — RLHF (reinforcement learning from human feedback):** Fine-tuning a language model with rewards derived from human ratings of its answers, usually via a learned reward model. It helped turn raw text predictors into helpful chatbots.

> **Definition — RL environment (for language models):** A sandbox with tasks, tools and an automatic grader, such as a code repository with tests or a web browser with a goal, used to train models by trial and error. Building them became an industry in 2025–26.

Look at how directly the game ideas carried over. DeepSeek's R1-Zero (January 2025) learned to reason through pure RL on problems with checkable answers, treating each problem a little like a game with a win condition, and reportedly showed an "aha moment" when it began spontaneously re-checking its work. Credit assignment is the same problem as in chess: thousands of tokens of reasoning, one reward at the end. Reward hacking is the same danger as the circling boat: a coding model that edits tests to pass is optimizing the letter of the reward. Even the people overlap: Noam Brown, co-creator of Libratus and Pluribus, later joined OpenAI and worked on its first reasoning models.

> **Key idea:** Your chatbot's "thinking" mode is a descendant of game-playing AI. The policy is the language model, the environment is the task, the reward is a checker or a judge, and the training methods (policy gradients with baselines, PPO, GRPO) are the ones this chapter introduced.

## Planning and search today

The deepest lesson of the game era is that learning and search work best together. AlphaGo's networks supplied fast intuition; its tree search supplied slow, careful checking. Psychologists sometimes describe human thinking the same way, as fast instinct and slow deliberation, and the analogy, though loose, captures why the combination is powerful.

> **Definition — Test-time search:** Spending extra computation when answering, by exploring and checking several possible solutions or reasoning paths, rather than committing to the first one. It is the modern language-model version of looking ahead in a game tree.

In 2026 this shows up in several forms:

- **Thinking longer.** Reasoning models write out long chains of reasoning before answering, effectively searching through ideas in words. More thinking generally means better answers on hard problems (Chapter 21).
- **Thinking wider.** Systems sample many answers and pick the best with a verifier or a vote (best-of-N), or explore branching reasoning paths in a tree, borrowing directly from MCTS.
- **Searching for proofs.** AlphaProof (2024) combined a language model with RL and the Lean proof checker, treating theorem proving as a game in which the win condition is a proof the checker accepts. With AlphaGeometry 2, it reached silver-medal standard at the 2024 International Mathematical Olympiad (28 of 42 points), though it needed days of computation for some problems. By 2025, an advanced Gemini Deep Think reached gold-medal standard (35 of 42) working in natural language within the time limit.
- **Searching for algorithms.** AlphaTensor (2022) treated finding faster matrix-multiplication methods as a game, and AlphaDev (2023) found faster sorting routines that were added to a widely used C++ library. AlphaEvolve (May 2025) paired a language model with an evolutionary search over code and found a way to multiply 4 × 4 complex matrices with 48 multiplications, the first improvement in that setting since Strassen's 1969 method.
- **Planning agents.** Coding and computer-use agents (Chapter 28) plan multi-step tasks, act, observe the result and replan, the agent-environment loop of Figure 48.5 with a language model as the policy.

> **At the frontier (2026):** The frontier labs now spend a large and growing share of their training compute on reinforcement learning, in thousands of RL environments that range from code repositories to spreadsheets to simulated businesses. The open problems are the classic RL problems at a new scale: designing rewards that cannot be gamed, assigning credit across very long tasks, exploring safely, and getting learning to transfer from training environments to the messy real world.

Richard Sutton summed up seventy years of this history in a short 2019 essay, "The Bitter Lesson": methods that make the most of growing computation, above all **search** and **learning**, eventually beat methods built on hand-crafted human knowledge. Deep Blue's hand-tuned evaluation lost to AlphaZero's self-taught one; hand-written rules for chatbots lost to RL on human feedback. Whether that lesson holds all the way to robots and open-ended science is one of the big questions of the next decade (Chapter 66).

> **Key idea:** Every decision-making system in this chapter, from A* to AlphaZero to your chatbot's reasoning mode, answers one question: how do you look ahead efficiently? Use a good guess (a heuristic or a learned value) to decide where to look, check the most promising options carefully, and learn from the results.

## In plain English

Some AI does not just answer questions; it makes decisions, and each decision changes what happens next. There are two main ways to make good decisions.

The first is search: think ahead. A* finds routes by combining the distance already traveled with a smart guess of the distance left. In games, minimax looks at every move and every reply, assumes the opponent plays well, and picks the move whose worst case is best. When games get too big, programs prune hopeless branches, estimate positions with evaluation functions, or use Monte Carlo tree search, which plays out many random futures and focuses on the promising ones.

The second is reinforcement learning: learn from rewards. An agent acts, the world responds with a new situation and a reward, and over many tries the agent learns a policy (what to do) and values (how good things are). It must balance exploring new options with exploiting known good ones, and figure out which early moves deserve credit for a late reward. Q-learning does this by passing value backward one step at a time; policy gradients make better-than-average actions more likely.

Games were the perfect lab. TD-Gammon, Deep Blue, DQN, AlphaGo, AlphaZero, MuZero, OpenAI Five, AlphaStar, Pluribus and CICERO each added an ingredient, and self-play let programs surpass every human teacher. Then RL left the arcade: cooling data centers, steering fusion plasma, racing drones, teaching robots to walk, and shaping your chatbot. When your chatbot "thinks" before answering, it is using ideas born in game-playing AI: a policy, a reward, and a search for the best path.

## Key terms
Sequential decision-making, Planning, State, Action, State space, Search (AI sense), Breadth-first search (BFS), Depth-first search (DFS), Heuristic, A* search, Manhattan distance, Admissible heuristic, Game tree, Branching factor, Ply, Zero-sum game, Perfect-information game, Minimax, Terminal state, Alpha-beta pruning, Evaluation function, Monte Carlo method, Playout (rollout), Monte Carlo tree search (MCTS), UCB (upper confidence bound), Reinforcement learning (RL), Agent, Environment, Reward, Episode, Return, Discount factor (gamma), Policy, Value function, Q-value (action value), Bellman equation, Exploration versus exploitation, Multi-armed bandit, Epsilon-greedy, Credit assignment problem, Sparse reward, Reward shaping, Temporal-difference (TD) learning, Q-learning, Learning rate (alpha), Q-table, Deep Q-Network (DQN), Experience replay, Target network, Policy gradient method, Advantage, Actor-critic method, PPO (proximal policy optimization), Model-free RL, Model-based RL, Reward hacking (specification gaming), Imperfect-information game, Nash equilibrium, Counterfactual regret minimization (CFR), Self-play, Elo rating, RLHF (reinforcement learning from human feedback), RL environment (for language models), Test-time search
