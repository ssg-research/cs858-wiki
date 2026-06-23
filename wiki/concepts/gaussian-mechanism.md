---
title: "Sensitivity and the Gaussian mechanism"
type: concept
description: "Making a function differentially private by adding noise calibrated to its sensitivity, the most one record can change its output; the Gaussian mechanism and why bounded sensitivity is the precondition for everything."
tags:
  - differential-privacy
  - privacy
  - defense
---

# Sensitivity and the Gaussian mechanism

## Definition

The sensitivity of a function is the most its output can change when one
record of its input dataset is added or removed, measured in some norm. It is
the worst case over all adjacent datasets, not an average. Sensitivity is the
quantity that converts noise into a privacy guarantee: adding noise scaled to
the sensitivity makes the function's output nearly as likely under either
adjacent dataset, which is the differential privacy condition (Dwork et al.,
2006).

The Gaussian mechanism instantiates this with normal noise: release the
function's value plus Gaussian noise whose standard deviation is proportional
to the sensitivity times a noise multiplier, yielding (epsilon,
delta)-differential privacy with parameters set by the multiplier (Dwork and
Roth, 2014). The recipe presupposes a known, finite sensitivity. Quantities
without an a priori bound, such as a gradient, must first be forced into one,
for example by [clipping](gradient-clipping.md), before the mechanism applies.

## Papers that use this concept

- [Deep Learning with Differential Privacy](../papers/abadi-2016-dp-sgd.md) — adds Gaussian noise to clipped, summed per-example gradients at every training step.
- [Unlocking the Power of Differentially Private Zeroth-order Optimization for Fine-tuning LLMs](../papers/bao-2025-dp-zo.md) — adds Gaussian noise calibrated to the clipped sensitivity of each record's aggregated zeroth-order update.

## Variants and traps

- Sensitivity is worst-case by definition. Estimating it empirically from
  observed data and adding noise to match yields no guarantee.
- The Laplace mechanism is the pure-epsilon analogue (noise scaled to ℓ1
  sensitivity); the Gaussian mechanism uses ℓ2 sensitivity and carries a
  delta.

## See also

- [Differential privacy](differential-privacy.md)
- [Gradient clipping](gradient-clipping.md)
- [Privacy budget and composition](privacy-budget.md)

## References

- Dwork, C., McSherry, F., Nissim, K., and Smith, A. "Calibrating Noise to
  Sensitivity in Private Data Analysis." Theory of Cryptography Conference
  (TCC), 2006.
- Dwork, C. and Roth, A. "The Algorithmic Foundations of Differential
  Privacy." Foundations and Trends in Theoretical Computer Science, 9(3-4),
  2014.
