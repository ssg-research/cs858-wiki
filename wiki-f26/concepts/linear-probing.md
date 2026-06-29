---
title: "Linear probing"
type: concept
description: "Training a linear classifier on a network's intermediate activations to test whether a property is linearly decodable from them; supervised concept directions, what high probe accuracy does and does not show."
tags:
  - interpretability
  - language-models
  - machine-learning
---

## [Wiki Home](../README.md)

# Linear probing

## Definition

A linear probe is a linear classifier trained on a network's intermediate
activations to predict a property of the input, used to test whether that
property is linearly decodable at a given layer (Alain and Bengio, 2017). High
probe accuracy shows the information is present and linearly accessible; on its
own it does not show that the network uses that direction in its computation, a
standing caveat in the probing literature (Belinkov, 2022). The weight vector of
a trained probe is itself a concept direction, which connects probing to methods
that read or edit concepts along directions in activation space.

## Papers that use this concept

_No reading-companion page currently uses this concept._

## See also

- [Linear representation hypothesis](linear-representation-hypothesis.md)
- [Activation steering](activation-steering.md)
- [Mechanistic interpretability](mechanistic-interpretability.md)

## References

- Alain, G. and Bengio, Y. "Understanding Intermediate Layers Using Linear
  Classifier Probes." International Conference on Learning Representations (ICLR),
  2017.
- Belinkov, Y. "Probing Classifiers: Promises, Shortcomings, and Advances."
  Computational Linguistics, 48(1), 2022.
