---
title: "Functionality stealing"
type: concept
description: "The model-extraction goal of training a substitute that performs the victim's task well, scored on task accuracy rather than on agreeing with the victim prediction for prediction; the query-and-imitate attack shape and what it does and does not need to know."
tags:
  - model-extraction
  - threat-model
  - machine-learning
---

## [Wiki Home](../README.md)

# Functionality stealing

## Definition

Functionality stealing is the branch of [model extraction](model-extraction.md)
whose target is what the victim model *does* rather than what it *is*. The
adversary queries the victim's prediction API, keeps the returned labels or
probability vectors as training targets, and fits a substitute (a "knockoff" or
"surrogate") on those pairs. Success is measured on the victim's task, against
ground truth on the victim's test distribution, so a substitute that reaches
comparable accuracy has stolen the functionality even where it disagrees with the
victim example by example. The other branch, which recovers exact parameters,
hyperparameters, or architecture, is scored on fidelity to the victim instead
(Tramèr et al., 2016; Jagielski et al., 2020).

Mechanically the attack is [knowledge distillation](knowledge-distillation.md)
without the teacher's cooperation: a student fit to a teacher's outputs. The
adversarial version drops distillation's usual assumptions. The adversary works
from [black-box](white-box-black-box.md) query access, pays per query, need not
know the victim's architecture, and need not hold data from the victim's training
distribution, since the query pool only has to elicit informative responses. That
combination is what makes the goal cheap relative to the cost of building the
victim, and it is why defenses tend to act on the returned outputs or to accept
the copy and try to mark it.

## Papers that use this concept

- [Knockoff Nets: Stealing Functionality of Black-Box Models](../papers/orekondy-2019-knockoff-nets.md) — formulates the goal and drives the query pool from public images that need not overlap the victim's classes or distribution.
- [DAWN: Dynamic Adversarial Watermarking of Neural Networks](../papers/szyller-2019-dawn.md) — takes the extraction as unpreventable and marks the surrogate the adversary trains, verifying ownership through the suspect model's API.
- [ModelGuard: Information-Theoretic Defense Against Model Extraction Attacks](../papers/tang-2024-modelguard.md) — perturbs the confidence vectors the API returns, so the substitute is fit to altered targets, and covers the parameter-stealing goal in the same formulation.

## Variants and traps

- Accuracy and fidelity are different scores and a paper's numbers only make
  sense against one of them. A high-accuracy substitute can disagree with the
  victim on individual inputs; a high-fidelity copy reproduces the victim's
  mistakes as well as its answers.
- "Stealing the model" is ambiguous between the two goals. Functionality stealing
  recovers no weights, so a defense that protects the weights, and an ownership
  claim that inspects them, both miss it.

## See also

- [Model extraction](model-extraction.md)
- [Knowledge distillation](knowledge-distillation.md)
- [Model watermarking](model-watermarking.md)
- [White-box and black-box access](white-box-black-box.md)

## References

- Jagielski, M., Carlini, N., Berthelot, D., Kurakin, A., and Papernot, N. "High
  Accuracy and High Fidelity Extraction of Neural Networks." USENIX Security
  Symposium, 2020.
- Tramèr, F., Zhang, F., Juels, A., Reiter, M.K., and Ristenpart, T. "Stealing
  Machine Learning Models via Prediction APIs." USENIX Security Symposium, 2016.
