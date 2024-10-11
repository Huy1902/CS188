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

# Game

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