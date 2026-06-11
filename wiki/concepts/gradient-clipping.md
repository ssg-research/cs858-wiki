---
title: "Gradient clipping"
type: concept
description: "Rescaling gradients that exceed a norm threshold; a training stabilizer in ordinary deep learning and, applied per example, the sensitivity bound that makes private gradient noising possible."
tags:
  - optimization
  - differential-privacy
---

# Gradient clipping

## Definition

Gradient clipping rescales a gradient whose norm exceeds a threshold C down to
norm C, leaving smaller gradients untouched. In ordinary deep learning it is a
stabilizer against exploding gradients and is usually applied to the averaged
batch gradient. In differentially private training the same operation does a
different job and must be applied per example: clipping each example's
gradient before aggregation caps any single example's influence on the update
at C, giving the bounded sensitivity that the
[Gaussian mechanism](gaussian-mechanism.md) requires. The threshold trades two
errors: too small and the clipped average points away from the true gradient,
too large and the noise (scaled to C) swamps the signal.

## Papers that use this concept

- [Deep Learning with Differential Privacy](../papers/abadi-2016-dp-sgd.md) — per-example clipping is the sensitivity bound at the core of DP-SGD; the paper chooses C from the median of unclipped gradient norms.

## See also

- [Sensitivity and the Gaussian mechanism](gaussian-mechanism.md)
- [Stochastic gradient descent](stochastic-gradient-descent.md)
