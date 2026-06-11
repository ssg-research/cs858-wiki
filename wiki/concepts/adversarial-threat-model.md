---
title: "Adversarial threat model"
type: concept
description: "How an adversary's power is specified: the allowed perturbation set (ℓp balls, especially ℓ-infinity), perceptual similarity, and the white-box / black-box / first-order access spectrum."
tags:
  - threat-model
  - adversarial-examples
  - evasion
---

# Adversarial threat model

## Definition

A threat model specifies what an adversary may do. Without one, "robust" and
"secure" are not falsifiable, since a defense is robust only against a stated
class of attacks. An adversarial-ML threat model has two parts: the perturbation
the adversary may apply, and the access it has to the model.

The perturbation is usually bounded in an [ℓp norm](lp-norms.md): the adversary
may move the input within an ℓp ball of radius epsilon. The ℓ-infinity ball, which caps the
change to each input coordinate at epsilon, is the most studied case and serves
as a proxy for perceptual similarity. The ℓ2 and ℓ0 balls encode different
attacker geometries.

Access ranges over a spectrum (see
[white-box and black-box access](white-box-black-box.md)). A white-box
adversary has the weights and gradients. A black-box adversary queries outputs
only, or [transfers](transferability.md) examples from a surrogate model. A first-order adversary uses gradients of the loss with
respect to the input, but no higher-order information. Bounding access this way
parallels the polynomially bounded adversary of cryptography.

## Papers that use this concept

- [Towards Deep Learning Models Resistant to Adversarial Attacks](../papers/madry-2018-pgd.md) — defines the allowed-perturbation set S and argues for the first-order adversary as a natural, broad attack class.

## Variants and traps

- "Robust" with no stated threat model is meaningless. Always ask: which norm,
  which radius, what adversary access.
- A defense can be robust under one threat model (ℓ-infinity at small epsilon)
  and broken under another (ℓ2, or a larger budget). Reported numbers are not
  comparable across threat models.
- Transferability lets a black-box attacker craft examples on a surrogate and
  reuse them, so "no gradient access" is weaker protection than it appears.

## See also

- [Adversarial examples](adversarial-examples.md)
- [ℓp norms](lp-norms.md)
- [White-box and black-box access](white-box-black-box.md)
- [Transferability](transferability.md)
- [Robust optimization](robust-optimization.md)
