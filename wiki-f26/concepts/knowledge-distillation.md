---
title: "Knowledge distillation"
type: concept
description: "Transferring a trained teacher model's behavior into a student model by training the student on the teacher's output distribution (soft labels), with temperature scaling; its equivalence to minimizing KL to the teacher and its link to model extraction."
tags:
  - knowledge-distillation
  - machine-learning
  - model-extraction
---

## [Wiki Home](../README.md)

# Knowledge distillation

## Definition

Knowledge distillation transfers the behavior of a trained "teacher" model into
a second "student" model by training the student to match the teacher's outputs
rather than the ground-truth labels alone (Hinton et al., 2015). The teacher's
full output distribution, the "soft labels," carries more information per example
than a one-hot label, because it exposes the relative probabilities the teacher
assigns to the non-top classes. A temperature parameter softens that
distribution to make those relative probabilities more visible during training.
The idea predates deep learning as model compression, where the goal was to
shrink an ensemble into a single fast model (Buciluǎ et al., 2006).

Training the student to imitate the teacher's predictive distribution is
equivalent, up to a constant, to minimizing the
[KL divergence](kl-divergence.md) between the two distributions over the set of
examples used for transfer. Classic distillation assumes white-box access to the
teacher and a shared task and data distribution. Relaxing those assumptions, so
that the teacher is only a queryable black box and the transfer inputs need not
match the teacher's training data, turns distillation into a tool for
[model extraction](model-extraction.md).

## Papers that use this concept

- [Knockoff Nets: Stealing Functionality of Black-Box Models](../papers/orekondy-2019-knockoff-nets.md) — frames the knockoff's training as distillation under weaker assumptions: the teacher is a black box, and the transfer images can come from a different distribution than the victim's training data.
- [ModelGuard: Information-Theoretic Defense Against Model Extraction Attacks](../papers/tang-2024-modelguard.md) — the functionality-stealing attacker it defends against distills the target's returned confidence vectors into a substitute, which the defense perturbs to corrupt that distillation.

## See also

- [Kullback-Leibler divergence](kl-divergence.md)
- [Model extraction](model-extraction.md)
- [Transfer learning](transfer-learning.md)

## References

- Buciluǎ, C., Caruana, R., and Niculescu-Mizil, A. "Model Compression." ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (KDD), 2006.
- Hinton, G., Vinyals, O., and Dean, J. "Distilling the Knowledge in a Neural Network." arXiv:1503.02531, 2015.
