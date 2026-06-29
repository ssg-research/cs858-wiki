---
title: "Privacy budget and composition"
type: concept
description: "The (epsilon, delta) budget a private computation may spend, composition theorems that bound accumulated leakage across steps, privacy accountants, and amplification by subsampling."
tags:
  - differential-privacy
  - privacy
---

### [Wiki Home](../README.md)

# Privacy budget and composition

## Definition

Differential privacy degrades gracefully under repetition: every private
release leaks a bounded amount, and the leaks add up. The privacy budget is
the total (epsilon, delta) a computation is allowed to spend; once spent, the
computation must stop touching the data. Composition theorems bound the
spending. Basic composition simply sums the epsilons of the steps; the strong
composition theorem improves the dependence to roughly the square root of the
number of steps, at some cost in delta (Dwork et al., 2010; Kairouz et al.,
2015).

A privacy accountant is the bookkeeping procedure that tracks accumulated
spending during execution and halts or reports when a threshold nears
(McSherry, 2009). Two refinements matter for machine learning. Subsampling
amplifies privacy: a step that touches a random fraction q of the data leaks
roughly q times less. And accounting can track more than the (epsilon, delta)
pair; following the full distribution of the privacy loss across steps, as
moments-based and related accountants do, yields much tighter totals for the
same noise. For iterative training, where one run is thousands of composed
steps, the tightness of the accountant directly determines how long a model
can train within a fixed budget.

## Papers that use this concept

- [Deep Learning with Differential Privacy](../papers/abadi-2016-dp-sgd.md) — its moments accountant tracks higher moments of the privacy loss across sampled Gaussian steps, cutting the reported epsilon severalfold for the same training run.
- [Unlocking the Power of Differentially Private Zeroth-order Optimization for Fine-tuning LLMs](../papers/bao-2025-dp-zo.md) — composes the per-iteration noise across fine-tuning steps with subsampling amplification under Rényi DP accounting, and spends part of the budget on releasing the private dataset size.

## Variants and traps

- Epsilon is not comparable across delta values, mechanisms, or adjacency
  definitions; an "epsilon of 2" means nothing without the rest of the
  specification.
- The budget bounds what the mechanism leaks, not what the adversary infers
  from auxiliary information it already has; the guarantee is robust to such
  information but does not erase it.

## See also

- [Differential privacy](differential-privacy.md)
- [Sensitivity and the Gaussian mechanism](gaussian-mechanism.md)

### [Wiki Home](../README.md)

## References

- Dwork, C., Rothblum, G. N., and Vadhan, S. "Boosting and Differential
  Privacy." IEEE Symposium on Foundations of Computer Science (FOCS), 2010.
- Kairouz, P., Oh, S., and Viswanath, P. "The Composition Theorem for
  Differential Privacy." International Conference on Machine Learning (ICML),
  2015.
- McSherry, F. D. "Privacy Integrated Queries: An Extensible Platform for
  Privacy-Preserving Data Analysis." ACM SIGMOD, 2009.
