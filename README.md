# Solving the N-Queens Problem using Search and Optimization Algorithms

## Project Overview

This project presents and compares four different approaches for solving the classical N-Queens problem:

- Exhaustive Depth-First Search (DFS)
- Greedy Hill Climbing
- Simulated Annealing
- Genetic Algorithm

The algorithms were implemented in Python and evaluated for different board sizes:

\[
N = 10, 30, 50, 100, 200, 500
\]

The objective of the project is to analyze the computational performance, memory usage, and scalability of classical search and optimization techniques.

---

# Problem Description

The N-Queens problem requires placing \(N\) queens on an \(N \times N\) chessboard such that no two queens attack each other.

A valid solution satisfies:
- No two queens share the same row
- No two queens share the same column
- No two queens share the same diagonal

---

# Algorithms Implemented

## 1. Depth-First Search (DFS)

- Exhaustive backtracking approach
- Guarantees exact solution
- Computationally expensive for large N

---

## 2. Greedy Hill Climbing

- Local search optimization
- Minimizes queen conflicts iteratively
- May get trapped in local optima

---

## 3. Simulated Annealing

- Probabilistic optimization technique
- Allows temporary acceptance of worse states
- Improves exploration capability

---

## 4. Genetic Algorithm

- Population-based evolutionary optimization
- Uses:
  - Selection
  - Crossover
  - Mutation
- Suitable for large search spaces

---
# Technologies Used

- Python
- Matplotlib
- NumPy
- LaTeX / Overleaf


# Project Structure

```text
NQueens-Algorithms/
│
├── dfs_nqueen.py
├── hill_climbing.py
├── simulated_annealing.py
├── genetic_algorithm.py
│
├── Figures/
│   ├── dfs_workflow.pdf
│   ├── hill_climbing_workflow.pdf
│   ├── simulated_annealing_workflow.pdf
│   ├── genetic_algorithm_workflow.pdf
│   ├── runtime_comparison.pdf
│   ├── memory_comparison.pdf
│
├── Assignment_Link_Solving N-Queens Problem - Akhil Nair.pdf
├── PR_Assignment_Akhil_Nair.pdf
├── README.md
├── requirements.txt
├── .gitignore