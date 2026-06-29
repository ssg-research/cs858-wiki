---
title: "Adversarial training"
type: concept
description: "The defense paradigm of training on adversarially perturbed inputs instead of (or alongside) clean ones, so the model learns to resist evasion; from FGSM augmentation to the min-max view."
tags:
  - adversarial-training
  - adversarial-robustness
  - robust-optimization
---

### [Wiki Home](../README.md)

# Adversarial training

## Definition

Adversarial training injects adversarial examples into training so the model
learns to classify them correctly. The learner minimizes loss on perturbed
inputs rather than on clean ones. The original form augments each minibatch with
its FGSM-perturbed copies (Goodfellow et al., 2015).

The defender's gradient step uses the same input gradient the attacker uses to
build the perturbation. Robust optimization formalizes this pairing as a single
problem: the attacker solves an inner maximization, the defender an outer
minimization over the resulting worst-case loss (see
[robust optimization](robust-optimization.md)).

A model is only as robust as the adversary it trains against. Training against a
weak adversary, such as a single-step attack, can defeat that adversary while
leaving the model open to stronger ones.

## Papers that use this concept

- [Towards Deep Learning Models Resistant to Adversarial Attacks](../papers/madry-2018-pgd.md) — recasts adversarial training as solving the outer minimization of a saddle-point problem and studies how strong the inner adversary must be.
- [Safety Alignment Should Be Made More Than Just a Few Tokens Deep](../papers/qi-2024-shallow-safety-alignment.md) — cited as the train-against-the-attack defense tradition its deeper-alignment data augmentation draws on.
- [SoK: Unintended Interactions among Machine Learning Defenses and Risks](../papers/duddu-2024-unintended-interactions.md) — surveys adversarial training as a defense whose effect on overfitting and memorization raises or lowers susceptibility to membership inference and other risks.

## Variants and traps

- Training against a weak adversary can produce
  [gradient masking](gradient-masking.md): the model flattens or hides its
  gradients rather than becoming robust, so it survives the training-time
  attack but not a stronger test-time one.
- Adversarial training tends to trade clean accuracy for robust accuracy. The
  size of this trade-off, and whether it is fundamental, is an active debate.
- "Adversarial training" (a test-time evasion defense) is unrelated to defenses
  against training-data poisoning, despite the shared word.

## See also

- [Robust optimization](robust-optimization.md)
- [Fast Gradient Sign Method (FGSM)](fgsm.md)
- [Gradient masking](gradient-masking.md)
- [Adversarial examples](adversarial-examples.md)

### [Wiki Home](../README.md)

## References

- Goodfellow, I. J., Shlens, J., and Szegedy, C. "Explaining and Harnessing
  Adversarial Examples." International Conference on Learning Representations
  (ICLR), 2015.
