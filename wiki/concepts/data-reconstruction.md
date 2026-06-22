---
title: "Data reconstruction"
type: concept
description: "Privacy attacks that recover whole training records or their content from a model, its gradients, or its outputs: model inversion, gradient inversion in federated learning, and verbatim extraction from generative models; recovers content, where membership inference recovers only a yes/no membership bit."
tags:
  - privacy
  - reconstruction
  - machine-learning
---

# Data reconstruction

## Definition

Data reconstruction recovers the content of training records from a model's
observable behavior, rather than only deciding whether a record was present.
Several settings share the goal. Model inversion reconstructs a representative
input for a class, or recovers attributes of an input, from confidence scores.
Gradient inversion (deep leakage from gradients) recovers the actual training
batch from the gradients shared in federated learning. Generative models can be
prompted to emit memorized training examples verbatim.

Reconstruction is a stronger demand than [membership inference](membership-inference.md):
membership inference outputs one bit about a known record, while reconstruction
must produce the record's content. Its success tracks how much a model has
memorized individual examples and how much of that memorization is exposed in the
observable used (outputs, gradients, or parameters).

## Papers that use this concept

- [SoK: Unintended Interactions among Machine Learning Defenses and Risks](../papers/duddu-2023-unintended-interactions.md) — one of its privacy risks; the paper conjectures and empirically tests that enforcing group fairness lowers reconstruction success.
- [Extracting Training Data from Large Language Models](../papers/carlini-2021-extracting-training-data.md) — verbatim reconstruction of memorized sequences from a generative language model.

## See also

- [Membership inference](membership-inference.md)
- [Memorization](memorization.md)

## References

- Fredrikson, M., et al. "Model Inversion Attacks that Exploit Confidence
  Information and Basic Countermeasures." ACM Conference on Computer and
  Communications Security (CCS), 2015.
- Zhu, L., et al. "Deep Leakage from Gradients." Advances in Neural Information
  Processing Systems (NeurIPS), 2019.
- Carlini, N., et al. "Extracting Training Data from Large Language Models."
  USENIX Security Symposium, 2021.
