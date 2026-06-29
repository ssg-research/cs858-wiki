---
title: "Fast Gradient Sign Method (FGSM)"
type: concept
description: "The one-step gradient-sign attack of Goodfellow et al. (2015): a single ascent step on the loss, sign-quantized and scaled to the ℓ-infinity budget; the canonical baseline attack and the basis of one-step adversarial training."
tags:
  - evasion
  - adversarial-examples
  - adversarial-training
---

### [Wiki Home](../README.md)

# Fast Gradient Sign Method (FGSM)

## Definition

The Fast Gradient Sign Method builds an ℓ-infinity adversarial example in one
step (Goodfellow et al., 2015). For an input x with label y, it moves x by the
budget epsilon along the sign of the input gradient of the loss:

```text
x_adv = x + epsilon * sign( grad_x L(theta, x, y) )
```

The sign quantization moves every coordinate by exactly epsilon, placing x_adv
on a corner of the ℓ-infinity ball. FGSM costs one backward pass, which made it
both the first widely used attack and the first attack cheap enough to run inside
training.

FGSM is a one-step linearization of the inner maximization: it assumes the loss
is locally linear and takes the optimal step under that assumption. When the
approximation is poor, the single step misses higher-loss points that iterated,
[projected](projected-gradient-descent.md) steps reach (Kurakin et al., 2017).

## Papers that use this concept

- [Towards Deep Learning Models Resistant to Adversarial Attacks](../papers/madry-2018-pgd.md) — treats FGSM as the one-step special case of solving the inner maximization, and as the weaker adversary its multi-step method is measured against.

## Variants and traps

- FGSM is one step. Iterating it, with a projection back into the ℓ-infinity ball
  after each move, gives a much stronger attack. Conflating "FGSM" with
  "iterative gradient attacks" is a common error.
- Training only against FGSM can yield models that resist FGSM but fall to
  slightly stronger adversaries, a symptom of
  [gradient masking](gradient-masking.md) rather than true robustness.

## See also

- [Adversarial examples](adversarial-examples.md)
- [Adversarial threat model](adversarial-threat-model.md)
- [Projected gradient descent](projected-gradient-descent.md)
- [Adversarial training](adversarial-training.md)
- [Robust optimization](robust-optimization.md)

### [Wiki Home](../README.md)

## References

- Goodfellow, I. J., Shlens, J., and Szegedy, C. "Explaining and Harnessing
  Adversarial Examples." International Conference on Learning Representations
  (ICLR), 2015.
- Kurakin, A., Goodfellow, I. J., and Bengio, S. "Adversarial Machine Learning
  at Scale." International Conference on Learning Representations (ICLR), 2017.
