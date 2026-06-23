---
title: "Gradient masking"
type: concept
description: "A defense failure mode: the model's loss gradients become uninformative so gradient-based attacks fail, while the model stays vulnerable to gradient-free or transferred attacks."
tags:
  - adversarial-robustness
  - evasion
  - evaluation
---

[Home page](../README.md)

# Gradient masking

## Definition

Gradient masking (also called obfuscated gradients) is a failure mode of
adversarial defenses: the defense makes the model's loss gradients flat, noisy,
or unavailable, so gradient-based attacks stop finding adversarial examples,
while the worst-case loss stays high. The model *looks* robust under the
attacks used to evaluate it and remains vulnerable to attacks that do not need
useful gradients. Telltale signs: [transfer attacks](transferability.md)
succeed where white-box attacks fail, gradient-free attacks succeed where
gradient-based ones fail, or a model appears more robust against a stronger
threat model than a weaker one. Single-step adversarial training is a classic
source of masking: the model learns to defeat the one gradient step it was
trained against rather than to lower the worst-case loss.

## Papers that use this concept

- [Towards Deep Learning Models Resistant to Adversarial Attacks](../papers/madry-2018-pgd.md) — trains against a multi-step adversary partly to avoid the masking failure of single-step training.

## See also

- [Adversarial training](adversarial-training.md)
- [Fast Gradient Sign Method (FGSM)](fgsm.md)
- [Transferability](transferability.md)
