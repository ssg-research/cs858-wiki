---
title: "ℓp norms"
type: concept
description: "ℓp distances and balls (ℓ0, ℓ2, ℓ-infinity) as perturbation budgets in adversarial threat models, and their role as proxies for perceptual similarity."
tags:
  - threat-model
  - adversarial-examples
---

### [Wiki Home](../README.md)

# ℓp norms

## Definition

The ℓp norm of a vector is (Σ|v_i|^p)^(1/p). Three cases dominate adversarial
ML: ℓ2 is Euclidean length; ℓ-infinity is the largest coordinate magnitude; ℓ0
counts nonzero coordinates (not a true norm, by standard abuse of notation).
The ℓp ball of radius epsilon around an input is the set of points within
distance epsilon. As perturbation budgets: an ℓ-infinity budget caps the change
to every pixel, an ℓ2 budget caps the total energy of the change, and an ℓ0
budget caps how many pixels change at all. All of them are proxies for
perceptual similarity, which has no closed form.

## Papers that use this concept

- [Towards Deep Learning Models Resistant to Adversarial Attacks](../papers/madry-2018-pgd.md) — fixes the perturbation set to an ℓ-infinity ball.
- [Neural Cleanse: Identifying and Mitigating Backdoor Attacks in Neural Networks](../papers/wang-2019-neural-cleanse.md) — measures each reverse-engineered trigger's size by the ℓ1 norm of its mask, then flags the label whose trigger is an outlier in that norm.
- [ModelGuard: Information-Theoretic Defense Against Model Extraction Attacks](../papers/tang-2024-modelguard.md) — bounds the perturbation applied to each returned confidence vector by an ℓ1 distortion budget, the utility constraint the defense optimizes under.

## Variants and traps

- Robustness in one norm implies little about another, and robust-accuracy
  numbers are not comparable across norms or radii.

## See also

- [Adversarial threat model](adversarial-threat-model.md)
- [Adversarial examples](adversarial-examples.md)
