---
title: "Singular value decomposition"
type: concept
description: "Factoring a matrix into orthonormal left and right singular vectors scaled by singular values; the rank, the four fundamental subspaces (column space, row space, null space, left null space), and the null space as the set of inputs a matrix maps to zero."
tags:
  - machine-learning
  - interpretability
---

### [Wiki Home](../README.md)

# Singular value decomposition

## Definition

The singular value decomposition (SVD) factors any real matrix W as W = UΣVᵀ,
where the columns of U and V are orthonormal left and right singular vectors and
Σ is diagonal with the non-negative singular values, sorted in descending order.
The number of non-zero singular values is the rank r. The singular vectors give
orthonormal bases for the four fundamental subspaces of W: the top r left
singular vectors span the column space (the set of outputs Wx can take), the top
r right singular vectors span the row space, and the remaining right singular
vectors span the null space, the set of inputs that W maps to zero (Strang,
2009). A vector lying in the null space contributes nothing to the output, while
the row space and column space are orthogonal complements of the null space and
left null space respectively. Truncating Σ to its largest singular values gives
the best low-rank approximation of W, which is why the decomposition is the
standard tool for reading the dominant directions of a weight matrix.

## Papers that use this concept

- [What Makes and Breaks Safety Fine-tuning? A Mechanistic Study](../papers/jain-2024-safety-finetuning.md) — analyzes the weight change from safety fine-tuning through its singular vectors and fundamental subspaces, relating it to the null space of the original weights.

## See also

- [Mechanistic interpretability](mechanistic-interpretability.md)
- [Linear representation hypothesis](linear-representation-hypothesis.md)

### [Wiki Home](../README.md)

## References

- Strang, G. "Introduction to Linear Algebra." Wellesley-Cambridge Press, fourth
  edition, 2009.
