These projects are in the course CS188. Here is where I upload my work on that.

# Table of contents
- [CSPs Overview](#csps-overview)
    - [1. Terminology](#1-terminology)
    - [2. Improve the performance](#2-improve-the-performance)
    - [3. Local search](#3-local-search)

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