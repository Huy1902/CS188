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

# CSPs Overview

## 1. Terminology
- Constraint satisfaction problems are a type of identification problem in which
the goal is important, not the path.
A goal test is a set of constraints.
- State is a partial assignment.
- The successor function assigns an unassigned variable.
- Backtracking: traditional solution
## 2. Improve the performance
- Filtering: forward checking and arc consistency.
- Ordering: Minimum remaining value and Least constraining value.
- Structure: tree-structured and cutset conditioning.
## 3. Local search
- Another algorithm exists for solving CSPs
- Min-conflicts heuristic
- Hill-climbing search
- Simulated annealing search
- Genetic algorithms

# Game tree

## 1. Definition
- Adversarial search problems, known as games
- Type of games
- Standard game formulations

## 2. Minimax
- State value
- Game tree
- Terminal utilities
- Terminal state
- Maximize the possible scores and minimize the magnitude of the defeat.
- Postorder traversal of the game tree

## 3. Alpha-Beta Pruning
- Max's best option on path to root
- Min's best option on path to root

## 4. Evaluation Function
- Estimating the true minimax value of a state
- Depth-limited minimax
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