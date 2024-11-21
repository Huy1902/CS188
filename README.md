These projects are in the course CS188. Here is where I upload my work on that.

# Table of contents

- [CSPs Overview](#csps-overview)
  - [1. Terminology](#1-terminology)
  - [2. Improve the performance](#2-improve-the-performance)
  - [3. Local search](#3-local-search)
- [Game](#game)
  - [1. Definition](#1-definition)
  - [2. Minimax](#2-minimax)
  - [3. Alpha-Beta Pruning](#3-alpha-beta-pruning)
  - [4. Evaluation Function](#4-evaluation-function)
  - [5. Expectimax](#5-expectimax)
  - [6. Other game types](#6-other-game-types)
  - [7. Utilities](#7-utilities)
- [CSPs Overview](#csps-overview)
  - [1. Terminology](#1-terminology)
  - [2. Improve the performance](#2-improve-the-performance)
  - [3. Local search](#3-local-search)
- [Game](#game)
  - [1. Definition](#1-definition)
  - [2. Minimax](#2-minimax)
  - [3. Alpha-Beta Pruning](#3-alpha-beta-pruning)
  - [4. Evaluation Function](#4-evaluation-function)
  - [5. Expectimax](#5-expectimax)
  - [6. Other game types](#6-other-game-types)
  - [7. Utilities](#7-utilities)
  - [8. Monte Carlo Tree Search](#8-monte-carlo-tree-search)
- [Logic: Proposition](#logic-proposition)
  - [1. Knowledge](#1-knowledge)
  - [2. Logic](#2-logic)
  - [3. Inference](#3-inference)
- [Inference in Propositional Logic](#inference-in-propositional-logic)
  - [1. Model checking](#1-model-checking)
  - [2. Theorem-proving](#2-theorem-proving)
  - [3. Logical agent](#3-logical-agent)
- [First-Order logic](#first-order-logic)
  - [1. Representation](#1-representation)
  - [2. Syntax and semantic](#2-syntax-and-semantic)
  - [3. Inference in FOL](#3-inference-in-fol)
- [Probability](#probability)
  - [1. Uncertainly](#1-uncertainly)
  - [2. Probability rundown](#2-probability-rundown)
  - [3. Probabilistic Inference](#3-probabilistic-inference)
  - [4. Inference by enumeration](#4-inference-by-enumeration)
- [Bayes Net](#bayes-net)
- [1. Bayesian Network Representation](#1-bayesian-network-representation)
- [2. Structure of Bayes Net](#2-structure-of-bayes-net)
- [3. Trade-off Accuracy and Performance](#3-trade-off-accuracy-and-performance)
- [Bayes Net: Inference](#bayes-net-inference)
  - [1. Inference by Enumeration](#1-inference-by-enumeration)
  - [2. Variable Elimination](#2-variable-elimination)
  - [3. Compare](#3-compare)
- [Bayes Net: Sampling and Approximate Inference](#bayes-net-sampling-and-approximate-inference)
  - [1. Prior sampling](#1-prior-sampling)
  - [2. Rejection Sampling](#2-rejection-sampling)
  - [3. Likelihood Weighting](#3-likelihood-weighting)
  - [4. Gibbs Sampling](#4-gibbs-sampling)


# CSPs Overview

## 1. Terminology
- Constraint satisfaction problems are a type of identification problem in which
  the goal is important, not the path.
  A goal test is a set of constraints.
- CSP also called: configuration satisfied problems
- State is a partial assignment.
- The successor function assigns an unassigned variable.
- Backtracking: traditional solution
## 2. Improve the performance
- Filtering: forward checking and arc consistency.
- Ordering: Minimum remaining value and Least constraining value.
- Structure: tree-structured and cutset conditioning.
## 3. Local search
- Many configuration and optimization problems can be formulated as local search
- Another algorithm exists for solving CSPs
- Min-conflicts heuristic
- Hill-climbing search
- Simulated annealing search
- Genetic algorithms
- Random restarts: start new search after one with random start
- Parallel search: start with all restart start at the same time
- Beam search: start with many restart start and catch best state

## 4. Local search in continuous state/action space:
- Discretize it
- Choose random perturbations to the state
  - First-choice hill-climbing
  - Stimulated annealing
- Compute gradient of f(x) analytically: finding extrema in continuous space

# Game

## 1. Definition
- Adversarial search problems, known as games
- Type of games
- Standard game formulations
- Want algorithms for calculating a strategy (policy)
- State: S
- Player : P : 1...N
- Action: A
- Transition function: S x A -> S
- Terminal test: S -> true, false
- Terminal utilities: S x P -> R
- Solution is a policy: S -> A
- Zero - Sum games Vs General-Sum games(more complex: agents have independent utilities) vs Team games
- 

## 2. Minimax
- Deterministic, zero-sum games: tic-tac-toe, checker, chess
- State value
- Game tree: Adversarial Game Trees -> Minimax value
  - State under opponent's control: minimize utilities(consider worst case)
  - State under agent's control: maximize utilities(consider best case)
- Terminal utilities
- Terminal state
- Maximize the possible scores and minimize the magnitude of the defeat.
- Postorder traversal of the game tree
- Implementation: simple and dispatch
- Optimal against a perfect player (pessimistic perspective)
- Multi-Agent utilities:
  - Utility tuples
  - Player maximizes its own component
- Efficiency: like DFS: Time O(b^m) and space O(bm)

## 3. Alpha-Beta Pruning
- Max's best option on path to root: pruning children of min node
- Min's best option on path to root: pruning children of max node
- Properties:
  - No effect on root
  - Intermediate value might be wrong
  - Ordering improves effectiveness of pruning
  - Metareasoning (computing about what to compute)

## 4. Evaluation Function
- Depth-limited minimax: solution for resource limit
- Estimating the true minimax value of a state
- Feature and weight

## 5. Expectimax:
- Use when facing suboptimal opponent(s), using a probability distribution
over the moves.
- Chance nodes which consider average case instead of minimizer node.

## 6. Other game types:
- Mixed layer types
- Multi-agent utilities

## 7. Utilities:
- Average utilities
- Describe an agent's preference
- Rational preferences
- Human utilities

## 8. Monte Carlo Tree Search
- Idea: Evaluation by rollout + selective search.
- Allocate rollout

# Logic: Proposition

## 1. Knowledge:
- Knowledge base: domain-specific facts
- Inference engine: generic code
- Knowledge based agent: knowledge + inference
- Can be encoded by logic
## 2. Logic:
- Syntax
- Semantics: set of possible worlds, sentences (truth condition).

## 3. Inference:
- Entailment
- Proof: demonstration of entailment
  - Algorithm
  - Method: model-checking, theorem-proving
  - Modus Ponens

# Inference in Propositional Logic
# 1. Model checking: DPLL algorithm:
- Early Termination
- Pure Symbol Heuristic
- Unit Clause Heuristic
- SAT Solver based on DPLL algorithm
# 2. Theorem-proving: Forward chaining
- Apply Modus Ponens to generate new facts
- Iterating the premise
- Adding the conclusion
- Another algorithm: resolution: sound and complete but expensive cost
# 3. Logical agent: 
Using one generic inference algorithm on one knowledge base:
- Localization
- Mapping
- SLAM
- Planning

# First-Order logic

# 1. Representation:
- Object: constant symbol
- Relationship: predicate symbol
- Function: function symbol: another way to name object
- Term: logical expressions that refer an object (simplest form is constant symbol)

# 2. Syntax and semantic:
- Atomic sentences
- Complex sentences: use quantifiers:
  - Universal quantifiers
  - Existential quantifiers

# 3. Inference in FOL
- Entailment
- Substitution (binding)
- Propositionalization
- Lifted inference

# Probability
# 1. Uncertainly
- Ignorance
- Laziness
# 2. Probability rundown:
- Random variable
- Probability distribution
- Joint distribution
- Chain rule
- Marginal distribution
- Normalize
- Conditional probabilities
- Bayes rule
- Mutually independent and conditional independent
# 3. Probabilistic Inference:
- Compute a desired probability from a probability model
# 4. Inference by enumeration:
- Query variable
- Evidence variable
- Hidden variable

# Bayes Net
- Describe complex joint distribution (models) using simple, conditional distributions
# 1. Bayesian Network Representation:
- A bayes net consist of:
  - A directed acyclic graph of nodes, one per variable X
  - Conditional probability table (CPT)
- Encode conditional independence relations between different nodes.
- Implicitly encode joint distribution
- The edge do not mean a casual relationship. It just means some relations between nodes.

# 2. Structure of bayes net:
- Each node is conditionally independent of all its ancestor nodes (not-descendants) in the graph,
given all of its parents.
- Each node is conditionally independent of all other variables given its Markov blanket.

# 3. Trade-off accuracy and performance:
- Strict independent
- Naive Bayes
- Sparse Bayes Net
- Joint distribution

# Bayes Net: Inference
# 1. Inference by enumeration:
- Select the entries consistent with the evidence
- Sum out hidden variables to get joint of query and evidence
- Normalize
# 2. Variable elimination:
Eliminate hidden variable one by one
- Join all factors involving X
- Sum out X
- A factor is defined as unnormalized probability (not necessarily sum up to 1)
- Linear time for poly tree
# 3. Compare:
- Operation 1: join factors
- Operation 2: eliminate (marginalization)
- Inference by enumeration = multiple join, multiple eliminate
- Variable elimination = Marginalizing Early
# Bayes net: Sampling: Approximate Inference
# 1. Prior sampling:
- A stimulator to generate particle (sample)

# 2. Rejection sampling:
- Modify our procedure to early reject any sample inconsistent with our evidence

# 3. Likelihood weighting:
- Fix evidence variables, sample the rest
- Weight each sample by probability of evidence variables given parents

# 4. Gibbs sampling:
- Set all variables to some totally random value
- Repeatedly pick one variable at a time, clear its value, and resample it given the values currently assigned 
to all other variables.

# Markov Model
# 1. Terminology:
- Sequence of observation where the state of underlying system is changing
-> Need to introduce time to our model
- State: value of X at given time
- Transition model: how state evolves over time
- Stationary assumption: transition prob. are the same at all times
- Markov assumption: future is independent of the past given the present (first-order Markov model)
- Joint distribution

# 2. Forward algorithm (simple form):
- Iterate update starting at t=0: Sum(Probability from previous iteration * transition model)
- In matrix-vector form: multiply by transpose of transition matrix

# 3. Stationary Distribution:
- The limiting distribution regardless of starting distribution
- Remain the same after the passage of time

# Hidden Markov Models
# 1. Terminology:
- True state is not observed correctly
- HMMs:
  - Underlying Markov chain over states sX
  - Observe evidence E at each time step
  - Initial distribution
  - Transition model
  - Sensor model
- Stationary assumption: transition and sensor prob. are the same at all times
- Current evidence is independent of everything else given the current state
# 2. Inference
- Filtering: belief state
- Prediction: filtering without the evidence
- Smoothing: better estimate of past states
- Most likely explanation: arg max 

# 3. Filtering/Monitoring:
- State estimation
- Recursive filtering
- "Forward" algorithm: normalize * update * pre-computer * predict
- In matrix-vector form: normalize * observation matrix * transpose of transition matrix * pre-compute matrix
- Predict(transition model) -> update(observation model)

# 4. Most likely explanation:
- Most probable path
- State trellis
- Forward algorithm count total probability of all paths
- Viterbi algorithm keep track of the maximum probability of any path

# Dynamic Bayes Nets and Particle Filters
# 1. DBNs:
- Track multiple variables over time, using multiple sources of evidence
- Repeat a fixed Bayes net structure at each time
- Every HMM is a single-variable DBN
- Every discrete DBN is an HMM: HMM state is Cartesian product of DBN state variables
# 2. Exact inference in DBNs - Particle Filtering:
- Represent belief state by a set of samples (particles)
  - A particle is a possible world state
- Prediction step: use transition model (move samples)
- Update step: after observing evidence -> update weight (weight each sample based on the evidence)
- Resample step: N times. choose from our weighted sample distribution

# Rational Decisions
# 1. Utilities:
- Function from outcomes (state of the world) to real numbers
that describe an agent's preferences
- Maximum Expected Utility: given knowledge, a rational agent choose action that maximize its
expected utility
- Average-case expectimax reasoning: magnitudes are meaningful
- Worst-case minimax reasoning: terminal value scale doesn't matter
- Uncertain outcomes

# 2. Rationalities:
- Utilities derived from rational preferences
- Preferences
  - Lotteries
  - Rational preferences: orderability, transitivity, continuity, substitutability, monotonicity 
  - Intransitive preference
- Human utilities: 
- Money: risk-averse
  - Expected monetary value EMV(L) = pX + (1-p)Y 
  - Meanwhile, U(L) = pU(X) + (1-p)U(Y)
  - Typically, U(L) < U(EMV(L))
  - Certainty equivalent: CE(L) ~ L
  - Insurance premium EMV(L) - CE(L)
- Stationary Preferences: discount factor

# Decision Networks and Value of Perfect Information(VPI):
# 1. Decision Networks:
- Chance nodes (just like BNs)
- Actions (rectangles, cannot have parents, observed evidence)
- Utility node (diamond, depend on action and chance nodes)
- Action selection:
  - Instantiate all evidence
  - Set action nodes each possible way
  - Calculate posterior for all parents of utility node
  - Calculate expected utility for each action
  - Choose maximizing action
- Notation:
  - EU(action | given information): expected utility for action
  - MEU(given information): a maximum over expectations

# 2. Value of information:
- Compute value of acquiring evidence
- VPI = expected improvement in decision quality
- VPI (E'|e) = MEU(e, E') - MEU(e)
- Non negative
- Sub additive
- Order-independent

# Markov Decision Process
# 1. Terminology:
- MDP: action + search + probabilities + time
- Example: Stochastic Grid world: maze-like problem, noisy movement, reward, maximize sum of rewards(goal)
- MDP is defined by:
  - Set of states
  - Set of actions
  - Transition function
  - Reward function
  - Start state
  - Terminal state
  - Non-deterministic search problem
- "Markov" : action outcomes depend only on the current state
- For MDPs, we want an optimal policy pi: S -> A
- Discounting
- Infinite utilities solution: finite horizon, absorbing sttate discounting 0 < gamma < 1

# 2. Quantities:
- Policy: map of states to actions
- Utility: sum of discounted rewards
- Values: expected utility from a state (max node)
- Q-Value: expected utility from a q-state (chance node)
- Value(utility) of a state s: V*
- Value(utility) of a q-state (s, a): Q*
- The optimal policy: optimal action = pi star(s)
- Time-limited values Vk(s)

# 3. Bellman Equation:
- Choose correct action -> keep being optimal
- One-step lookahead relationship amongst optimal utility values
# 4. Value iteration: 
- A fixed point solution method
- Start with Vo(s) = 0
- Use bellman equations
- Repeat until convergence
- Complexity O(S * A * S) 

# 5. Policy method:
- Fixed policies: simplify tree
- Policy Evaluation:
  - Like value iteration without max (fixed action)
  - Without maxes, Bellman equations are a Linear system-> linear system solver
- Policy extraction:
  - Computing actions from values: arg max
  - Computing actions from q-values: arg max
- Policy iteration:
  - Step 1: evaluation: arbitrary policy pi
  - Step 2: improvement: 1-step look-ahead
  - Update utilities with fixed policy
  - With utilities-> new policy(policy doesn't change->done)