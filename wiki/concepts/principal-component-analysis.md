---
title: "Principal component analysis (PCA)"
type: concept
description: "Unsupervised linear dimensionality reduction: finds the orthogonal directions that capture the most variance in a dataset, ranked by the variance each explains; used to derive a single direction from a set of vectors without labels."
tags:
  - machine-learning
  - statistics
---

# Principal component analysis (PCA)

## Definition

PCA finds an orthogonal set of directions in a dataset's feature space, ranked
so that the first captures the most variance, the second the most of what
remains, and so on. The first principal component alone is often used as a
single summarizing direction for a set of vectors, with no labels required.
Explained variance ratio reports the fraction of total variance each component
accounts for; a single component dominating the ratio is read as evidence that
the data varies mainly along one underlying axis.

## Papers that use this concept

- [Representation Engineering: A Top-Down Approach to AI Transparency](../papers/zou-2023-representation-engineering.md) — its default Linear Artificial Tomography baseline applies PCA, unsupervised, to a set of paired difference vectors to extract a "reading direction" for a target concept.

## See also

- [Linear probing (probing classifiers)](linear-probing.md)
