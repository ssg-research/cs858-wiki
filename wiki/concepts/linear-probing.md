---
title: "Linear probing (probing classifiers)"
type: concept
description: "Training a lightweight classifier, usually linear, on a frozen network's intermediate activations to test whether a property is linearly decodable from them; a correlational tool that needs a separate manipulation experiment to establish a causal role."
tags:
  - interpretability
  - llm
---

# Linear probing (probing classifiers)

## Definition

A probing classifier is trained on the intermediate activations of a frozen
network to predict some property of the input, such as a sentence's syntactic
role or a statement's truth value (Alain and Bengio, 2017). Linear probes,
which fit a single linear decision boundary, are the most common because a
linear probe finding high accuracy is read as evidence the property is encoded
nearly as-is in the representation, rather than recovered only through a more
complex, downstream computation. A probe is supervised, requiring labeled
examples of the target property; the labels are used only to fit or evaluate
the probe, not to train the underlying network.

## Papers that use this concept

- [Representation Engineering: A Top-Down Approach to AI Transparency](../papers/zou-2023-representation-engineering.md) — extends probing with an unsupervised variant (its Linear Artificial Tomography baseline uses PCA instead of a labeled probe) and combines it with manipulation experiments to test causal, not just correlational, claims.

## Variants and traps

A high probing accuracy shows only that a property is linearly decodable from
the activations; it does not show that the network *uses* that direction when
producing its output. Probing results can also pick up confounds correlated
with the labels rather than the target property itself. Establishing a causal
role requires a separate manipulation or ablation experiment showing that
editing the probed direction changes model behavior (Belinkov, 2022).

## See also

- [Principal component analysis (PCA)](principal-component-analysis.md)

## References

- Alain, G. and Bengio, Y. "Understanding Intermediate Layers Using Linear
  Classifier Probes." International Conference on Learning Representations
  (ICLR) Workshop, 2017.
- Belinkov, Y. "Probing Classifiers: Promises, Shortcomings, and Advances."
  Computational Linguistics, 48(1), 207-219, 2022.
