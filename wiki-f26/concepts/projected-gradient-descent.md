---
title: "Projected gradient descent"
type: concept
description: "Constrained first-order optimization: take a gradient step, then project back onto the feasible set. In adversarial ML, 'PGD' usually names the iterative attack built on this primitive."
tags:
  - optimization
  - evasion
---

### [Wiki Home](../README.md)

# Projected gradient descent

## Definition

Projected gradient descent (PGD) optimizes a function subject to a constraint
set: take an ordinary gradient step, then project the result back onto the set.
The projection maps a point to its nearest feasible point; for an ℓ-infinity
ball it is coordinate-wise clipping. PGD is the standard first-order method for
large-scale constrained optimization.

## Papers that use this concept

- [Towards Deep Learning Models Resistant to Adversarial Attacks](../papers/madry-2018-pgd.md) — uses PGD on the input as its attack and argues it is the strongest first-order adversary.

## Variants and traps

- In adversarial ML, "PGD" almost always means the iterative ℓ-infinity attack
  popularized by the paper above: projected gradient *ascent* on the loss with
  respect to the input, with sign-normalized steps and random restarts. The
  optimization primitive and the attack named after it are distinct things.

## See also

- [Stochastic gradient descent](stochastic-gradient-descent.md)
- [Fast Gradient Sign Method (FGSM)](fgsm.md)
- [ℓp norms](lp-norms.md)
