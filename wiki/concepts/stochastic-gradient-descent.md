---
title: "Stochastic gradient descent"
type: concept
description: "Gradient descent on minibatch estimates of the training loss; the default optimizer for neural networks, whose backpropagated gradients also power gradient-based attacks."
tags:
  - machine-learning
  - optimization
---

# Stochastic gradient descent

## Definition

Gradient descent minimizes a differentiable function by repeatedly stepping
against its gradient. Stochastic gradient descent (SGD) replaces the
full-dataset gradient of the training loss with a cheap estimate computed on a
small random minibatch, which is what makes training on large datasets
feasible. For neural networks the gradient comes from backpropagation, and SGD
variants are the default way deep models are trained. The same backpropagation
machinery also differentiates the loss with respect to the *input* rather than
the parameters; that input gradient is the basic resource of gradient-based
attacks.

## Papers that use this concept

- [Towards Deep Learning Models Resistant to Adversarial Attacks](../papers/madry-2018-pgd.md) — SGD solves the outer (training) minimization; gradient steps on the input solve the inner (attack) maximization.
- [Membership Inference Attacks From First Principles](../papers/carlini-2022-lira.md) — the training procedure behind both the target model and the attacker's shadow models.

## See also

- [Empirical risk minimization](empirical-risk-minimization.md)
- [Projected gradient descent](projected-gradient-descent.md)
