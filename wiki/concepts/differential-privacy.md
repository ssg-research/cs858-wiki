---
title: "Differential privacy"
type: concept
description: "The formal guarantee bounding any single training example's influence on an algorithm's output, parameterized by epsilon; DP-SGD as its deep-learning instantiation; provable upper bound on membership inference."
tags:
  - differential-privacy
  - privacy
  - defense
---

# Differential privacy

## Definition

Differential privacy (DP) is a property of a randomized algorithm: its output
distribution must change by at most a bounded factor, parameterized by epsilon
(and a slack term delta), when any single example in its input dataset is added
or removed (Dwork and Roth, 2014). Small epsilon means no single example
influences the output much, so nothing the algorithm releases can reveal much
about any individual example. The guarantee is worst-case over datasets and
over what the adversary already knows, which is what separates it from
empirical, attack-specific defenses.

For deep learning, the standard instantiation is DP-SGD: clip each example's
gradient to a fixed norm, add calibrated noise to the summed gradients, and
account for the privacy spent across training steps (Abadi et al., 2016). DP
directly upper-bounds the success of any membership inference attack, so the
attack's measured success doubles as an empirical check on how tight a
training algorithm's guarantee is. The recurring cost is utility: clipping and
noise degrade accuracy, and epsilon values small enough for a meaningful
guarantee can be expensive to reach.

## Papers that use this concept

- [Deep Learning with Differential Privacy](../papers/abadi-2016-dp-sgd.md) — the source of DP-SGD; brings the guarantee to non-convex deep network training at single-digit budgets.
- [Membership Inference Attacks From First Principles](../papers/carlini-2022-lira.md) — evaluates DP-SGD as a defense and observes the gap between provable epsilon bounds and empirical attack success.
- [Extracting Training Data from Large Language Models](../papers/carlini-2021-extracting-training-data.md) — weighs differentially private training as the principled mitigation against the extraction it demonstrates, and notes its utility cost.
- [Knowledge Unlearning for Mitigating Privacy Risks in Language Models](../papers/jang-2022-knowledge-unlearning.md) — positions post-hoc unlearning against DP, trading the worst-case (epsilon, delta) certificate for empirical protection of named sequences without retraining.

## Variants and traps

- Deployed epsilon values are often so large that the formal guarantee is
  vacuous; "trained with DP" is not by itself evidence of privacy.
- DP bounds worst-case leakage. An algorithm without a meaningful DP guarantee
  can still resist today's attacks, and resistance to today's attacks proves
  no guarantee.
- "Private" in DP's formal sense and "private" in the colloquial
  data-protection sense are different claims; conflating them is a standard
  error in both directions.

## See also

- [Sensitivity and the Gaussian mechanism](gaussian-mechanism.md)
- [Privacy budget and composition](privacy-budget.md)
- [Membership inference](membership-inference.md)
- [Memorization](memorization.md)
- [Stochastic gradient descent](stochastic-gradient-descent.md)

## References

- Abadi, M., Chu, A., Goodfellow, I., McMahan, H. B., Mironov, I., Talwar, K.,
  and Zhang, L. "Deep Learning with Differential Privacy." ACM Conference on
  Computer and Communications Security (CCS), 2016.
- Dwork, C. and Roth, A. "The Algorithmic Foundations of Differential
  Privacy." Foundations and Trends in Theoretical Computer Science, 9(3-4),
  2014.
