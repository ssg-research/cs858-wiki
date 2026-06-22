---
title: "Principal component analysis (PCA)"
type: concept
description: "A linear transform that finds the orthogonal directions of greatest variance in a dataset; the leading principal components give a low-dimensional summary, used to recover salient directions in sets of neural activations."
tags:
  - statistics
  - dimensionality-reduction
  - representations
---

# Principal component analysis (PCA)

## Definition

Principal component analysis finds an orthogonal set of directions, the
principal components, ordered by how much of a dataset's variance each one
captures. Projecting the data onto the leading components yields a
low-dimensional summary that preserves the largest sources of variation.
Applied to a set of neural activation vectors, PCA recovers the dominant axes
along which those activations vary. Taking the top principal component of the
differences between activations on contrasting inputs (for example, prompts that
do and do not exhibit a target concept) gives a single direction that captures
how that contrast is represented.

## Papers that use this concept

- [Representation Engineering: A Top-Down Approach to AI Transparency](../papers/zou-2023-representation-engineering.md) — its Linear Artificial Tomography reading baseline fits a linear model over activation differences to extract a concept direction.

## See also

- [Distributed representations](distributed-representations.md)
- [Linear probing (probing classifiers)](linear-probing.md)
