---
title: "Empirical risk minimization"
type: concept
description: "Training as minimizing average loss over the training set as a proxy for expected loss over the data distribution; the baseline objective that robust and adversarial objectives modify."
tags:
  - machine-learning
  - optimization
---

## [Wiki Home](../README.md)

# Empirical risk minimization

## Definition

The risk of a model with parameters θ is its expected loss over the data
distribution. The distribution is unknown, so training minimizes the empirical
risk instead: the average loss over the training set. Empirical risk
minimization (ERM) is the default recipe behind supervised learning. It
controls average-case loss only; it guarantees nothing about the loss at
inputs an adversary picks near the data, which is the gap that adversarial and
robust training objectives address.

## Papers that use this concept

- [Towards Deep Learning Models Resistant to Adversarial Attacks](../papers/madry-2018-pgd.md) — its saddle-point objective is ERM with the per-example loss replaced by the worst-case loss within a perturbation set.
- [Membership Inference Attacks From First Principles](../papers/carlini-2022-lira.md) — ERM's drive to lower training-example loss is the asymmetry between seen and unseen data that membership inference exploits.
- [Deep Learning with Differential Privacy](../papers/abadi-2016-dp-sgd.md) — the objective DP-SGD minimizes under a privacy constraint.
- [SoK: Unintended Interactions among Machine Learning Defenses and Risks](../papers/duddu-2024-unintended-interactions.md) — uses the train-test generalization gap, overfitting, as one of the two conjectured causes underlying defense-risk interactions.

## See also

- [Stochastic gradient descent](stochastic-gradient-descent.md)
- [Robust optimization](robust-optimization.md)
