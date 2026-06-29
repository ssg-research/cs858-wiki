---
title: "Zeroth-order optimization"
type: concept
description: "Gradient-free optimization that estimates a descent direction from forward-pass loss differences along random perturbation directions; the two-point/SPSA estimator, the MeZO line for memory-efficient LLM fine-tuning, and why it needs no backpropagation."
tags:
  - optimization
  - machine-learning
  - language-models
---

### [Wiki Home](../README.md)

# Zeroth-order optimization

## Definition

Zeroth-order optimization (ZO) minimizes a function using only its values, with
no gradients. The basic estimator probes the loss along a random direction: for
a perturbation vector z and a small scale phi, the scaled loss difference
(L(theta + phi z) - L(theta - phi z)) / (2 phi) approximates the directional
derivative along z, and multiplying it by z gives an estimate of the gradient
that is correct in expectation as phi shrinks. This two-point, simultaneous
perturbation estimator comes from stochastic approximation and control theory
(Spall, 1992), and its convergence rate with two function evaluations is known
for convex problems (Duchi et al., 2013). Averaging several independent
directions lowers the estimate's variance.

The appeal is memory. A first-order gradient for a neural network comes from
backpropagation, which caches activations and intermediate gradients and so
costs several times a forward pass; a ZO estimate needs only forward
evaluations. Applied to LLM fine-tuning as MeZO, ZO stores the random seed and
regenerates the perturbation in place rather than holding the full vector,
cutting the memory footprint to roughly that of inference, up to an order of
magnitude below backpropagation (Malladi et al., 2023). The cost is variance: a
few directions probe a parameter space of millions of dimensions, so ZO
converges more slowly and noisily than first-order methods. The per-step update
is a low-dimensional, bounded scalar-times-direction object, which is why the
differential-privacy literature adopted ZO as a base optimizer.

## Papers that use this concept

- [Unlocking the Power of Differentially Private Zeroth-order Optimization for Fine-tuning LLMs](../papers/bao-2025-dp-zo.md) — the gradient-free optimizer the paper makes differentially private, aggregating several per-record estimates so the clipped update carries less bias.

## Variants and traps

- "Zeroth-order" means using function values only (no derivatives); it is
  unrelated to the order of a model or of a Taylor remainder in any other
  sense.
- The two-point estimate is unbiased for the smoothed loss, not the exact loss;
  the bias vanishes only as the perturbation scale goes to zero.
- ZO trades compute for memory: it removes backpropagation but needs more
  forward passes and more steps to converge.

## See also

- [Stochastic gradient descent](stochastic-gradient-descent.md)
- [Gradient clipping](gradient-clipping.md)
- [Differential privacy](differential-privacy.md)

### [Wiki Home](../README.md)

## References

- Duchi, J. C., Jordan, M. I., Wainwright, M. J., and Wibisono, A. "Optimal
  Rates for Zero-Order Convex Optimization: The Power of Two Function
  Evaluations." IEEE Transactions on Information Theory, 61, 2013.
- Malladi, S., Gao, T., Nichani, E., Damian, A., Lee, J. D., Chen, D., and
  Arora, S. "Fine-Tuning Language Models with Just Forward Passes." Advances in
  Neural Information Processing Systems (NeurIPS), 2023.
- Spall, J. C. "Multivariate Stochastic Approximation Using a Simultaneous
  Perturbation Gradient Approximation." IEEE Transactions on Automatic Control,
  37(3), 1992.
