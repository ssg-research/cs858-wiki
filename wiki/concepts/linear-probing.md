---
title: "Linear probing (probing classifiers)"
type: concept
description: "Training a simple, usually linear, classifier on a network's intermediate activations to test what a layer encodes; locating concept directions in activation space, and the decodable-versus-used caveat."
tags:
  - interpretability
  - representations
  - probing
---

# Linear probing (probing classifiers)

## Definition

A probe is a simple classifier, usually linear, trained to predict a property of
the input from a network's intermediate activations (Alain and Bengio, 2017).
High probe accuracy is taken as evidence that the layer's representation encodes
that property in a linearly accessible form, and probing is a standard tool for
studying what neural representations contain (Belinkov, 2022). A related approach,
concept activation vectors, defines a concept by the direction that separates
activations on examples having the concept from those lacking it (Kim et al.,
2018). A standing caveat is that a probe shows information is decodable from a
layer, which on its own does not establish that the network uses that information
when it produces its output.

## Papers that use this concept

- [Representation Engineering: A Top-Down Approach to AI Transparency](../papers/zou-2023-representation-engineering.md) — its "representation reading" generalizes probing to locate directions for high-level concepts and functions, often without labels.

## See also

- [Distributed representations](distributed-representations.md)
- [Activation steering](activation-steering.md)
- [Principal component analysis](principal-component-analysis.md)

## References

- Alain, G. and Bengio, Y. "Understanding Intermediate Layers Using Linear
  Classifier Probes." International Conference on Learning Representations
  (ICLR), 2017.
- Belinkov, Y. "Probing Classifiers: Promises, Shortcomings, and Advances."
  Computational Linguistics, 48(1):207–219, 2022.
- Kim, B., Wattenberg, M., Gilmer, J., Cai, C., Wexler, J., Viégas, F., et al.
  "Interpretability Beyond Feature Attribution: Quantitative Testing with Concept
  Activation Vectors (TCAV)." International Conference on Machine Learning
  (ICML), 2018.
