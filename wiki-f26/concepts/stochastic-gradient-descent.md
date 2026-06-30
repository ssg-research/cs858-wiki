---
title: "Stochastic gradient descent"
type: concept
description: "Gradient descent on minibatch estimates of the training loss; the default optimizer for neural networks, whose backpropagated gradients also power gradient-based attacks."
tags:
  - machine-learning
  - optimization
---

## [Wiki Home](../README.md)

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
- [Deep Learning with Differential Privacy](../papers/abadi-2016-dp-sgd.md) — DP-SGD is SGD with per-example clipping and Gaussian noise added to its gradient estimates.
- [Safety Alignment Should Be Made More Than Just a Few Tokens Deep](../papers/qi-2024-shallow-safety-alignment.md) — inspects per-token gradient norms during fine-tuning to show where safety alignment is undone.
- [Knowledge Unlearning for Mitigating Privacy Risks in Language Models](../papers/jang-2022-knowledge-unlearning.md) — unlearning is the SGD update run uphill: gradient ascent that maximizes the loss on the target sequences.
- [Knockoff Nets: Stealing Functionality of Black-Box Models](../papers/orekondy-2019-knockoff-nets.md) — trains both the victim classifiers and the knockoff by SGD on a cross-entropy loss.
- [Neural Cleanse: Identifying and Mitigating Backdoor Attacks in Neural Networks](../papers/wang-2019-neural-cleanse.md) — reverse-engineers a candidate trigger by gradient-descent optimization over the input mask and pattern rather than over model weights.
- [Unlocking the Power of Differentially Private Zeroth-order Optimization for Fine-tuning LLMs](../papers/bao-2025-dp-zo.md) — replaces backpropagated SGD gradients with forward-pass zeroth-order estimates to cut the memory of private fine-tuning.
- [ModelGuard: Information-Theoretic Defense Against Model Extraction Attacks](../papers/tang-2024-modelguard.md) — the adversary trains its substitute by SGD on the target's returned predictions, and the defense perturbs those predictions to enlarge that training loss.

## See also

- [Empirical risk minimization](empirical-risk-minimization.md)
- [Projected gradient descent](projected-gradient-descent.md)
