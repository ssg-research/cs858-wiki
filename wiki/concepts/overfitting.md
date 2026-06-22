---
title: "Overfitting"
type: concept
description: "Fitting the training set better than the underlying distribution, measured by the train-test generalization gap; the bias-variance picture, model capacity and dataset size as the levers, and the aggregate signal that privacy and robustness attacks both interact with."
tags:
  - overfitting
  - generalization
  - machine-learning
---

# Overfitting

## Definition

A model overfits when it achieves high accuracy on its training set but fails to
generalize to unseen data drawn from the same distribution. The standard measure
is the generalization gap (also called generalization error): the difference
between performance on the training set and on a held-out test set. A large gap
means the model has fit patterns specific to the training sample, including
noise, rather than structure shared with the distribution.

Overfitting is usually read through the bias-variance decomposition. High bias is
underfitting, where a model too simple to capture the signal errs on both train
and test data; high variance is sensitivity to the particular training sample,
the regime where overfitting lives. Two levers move a model along this axis: the
size of the training set (more data lowers variance) and model capacity (more
parameters can fit a more complex, and more sample-specific, decision boundary).
Modern over-parameterized networks complicate the textbook U-shaped curve, since
very large models can generalize well despite fitting the training data exactly.

## Papers that use this concept

- [SoK: Unintended Interactions among Machine Learning Defenses and Risks](../papers/duddu-2023-unintended-interactions.md) — conjectures overfitting, alongside memorization, as one of the two underlying causes through which a defense changes a model's susceptibility to other risks.
- [Membership Inference Attacks From First Principles](../papers/carlini-2022-lira.md) — membership inference is classically tied to overfitting, though the paper shows the connection is per-example rather than purely aggregate.

## Variants and traps

- Overfitting and [memorization](memorization.md) are distinct. The
  generalization gap is an aggregate over the whole dataset; memorization is
  per-example and persists even in models with a small gap.
- A small generalization gap does not certify privacy: a well-generalizing model
  can still memorize, and leak, individual training records.

## See also

- [Memorization](memorization.md)
- [Empirical risk minimization](empirical-risk-minimization.md)
- [Membership inference](membership-inference.md)

## References

- Geman, S., et al. "Neural Networks and the Bias/Variance Dilemma." Neural
  Computation, 4(1):1–58, 1992.
- Yeom, S., et al. "Privacy Risk in Machine Learning: Analyzing the Connection to
  Overfitting." IEEE Computer Security Foundations Symposium (CSF), 2018.
