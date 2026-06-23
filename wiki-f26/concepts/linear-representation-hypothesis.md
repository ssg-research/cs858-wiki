---
title: "Linear representation hypothesis"
type: concept
description: "The hypothesis that networks encode high-level concepts as linear directions in their activation space; concept directions, word-vector analogies, and reading or steering a concept by its direction."
tags:
  - interpretability
  - language-models
  - machine-learning
---

[Home page](../README.md)

# Linear representation hypothesis

## Definition

The linear representation hypothesis holds that neural networks encode many
high-level concepts as linear directions in their activation space, so a single
vector captures how much of a concept is present at a given layer and token. The
classic evidence is semantic arithmetic in word embeddings, where directions
correspond to interpretable relations such as gender or pluralization (Mikolov
et al., 2013), including a direction along which words can be debiased (Bolukbasi
et al., 2016). Under this view a concept is read by projecting an activation onto
its direction and steered by moving the activation along it. The hypothesis
coexists with superposition, in which many directions are packed into the same
space and need not align with individual neurons (Elhage et al., 2022).

## Papers that use this concept

- [Representation Engineering: A Top-Down Approach to AI Transparency](../papers/zou-2023-representation-engineering.md) — treats high-level concepts and functions as linear directions ("reading vectors") recovered from activations, then reads and steers along them.

## See also

- [Linear probing](linear-probing.md)
- [Activation steering](activation-steering.md)
- [Contrastive prompt pairs](contrastive-prompt-pairs.md)

[Home page](../README.md)

## References

- Bolukbasi, T., Chang, K.-W., Zou, J. Y., Saligrama, V., and Kalai, A. T. "Man
  is to Computer Programmer as Woman is to Homemaker? Debiasing Word Embeddings."
  Advances in Neural Information Processing Systems (NeurIPS), 29, 2016.
- Elhage, N., Hume, T., Olsson, C., Schiefer, N., Henighan, T., Kravec, S.,
  Hatfield-Dodds, Z., Lasenby, R., Drain, D., Chen, C., et al. "Toy Models of
  Superposition." Transformer Circuits Thread, 2022.
- Mikolov, T., Yih, W.-t., and Zweig, G. "Linguistic Regularities in Continuous
  Space Word Representations." Proceedings of NAACL-HLT, 2013.
