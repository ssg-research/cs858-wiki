---
title: "Algorithmic fairness"
type: concept
description: "Group fairness in ML: equitable behavior across sensitive subgroups under metrics like demographic parity and equalized odds, enforced by pre-, in-, or post-processing; discriminatory behavior as the risk and group-fairness constraints as the corresponding defense."
tags:
  - fairness
  - bias
  - machine-learning
---

# Algorithmic fairness

## Definition

Algorithmic fairness asks that a model behave equitably across sensitive
subgroups defined by attributes such as race, sex, or age. The dominant
formalization is group fairness, which constrains a statistic of the model's
predictions to be comparable across subgroups. Common metrics include
demographic parity (prediction independent of the sensitive attribute),
equalized odds (equal true- and false-positive rates across subgroups), and
equality of opportunity (equal true-positive rates). These metrics are not
mutually satisfiable in general, so a fairness goal is a choice of metric, not a
single well-defined target.

Discriminatory behavior, the underlying risk, shows up as disparity in a
performance metric (accuracy, false-positive rate) between subgroups, and arises
from bias in the training data or the learning algorithm. Group-fairness
defenses intervene at one of three stages: pre-processing reweights or transforms
the data, in-processing adds a fairness term or adversary to the training
objective, and post-processing adjusts the trained model's outputs.

## Papers that use this concept

- [SoK: Unintended Interactions among Machine Learning Defenses and Risks](../papers/duddu-2023-unintended-interactions.md) — treats discriminatory behavior as one of its risks and group fairness as one of its defenses, and traces how enforcing fairness interacts with privacy and security risks.

## Variants and traps

- Group fairness (subgroup statistics) differs from individual fairness (similar
  individuals treated similarly); the two can disagree.
- Fairness metrics conflict with one another and with accuracy, and enforcing one
  can change a model's exposure to privacy attacks.

## See also

- [Membership inference](membership-inference.md)
- [Attribute inference](attribute-inference.md)

## References

- Hardt, M., et al. "Equality of Opportunity in Supervised Learning." Advances in
  Neural Information Processing Systems (NeurIPS), 2016.
- Mehrabi, N., et al. "A Survey on Bias and Fairness in Machine Learning." ACM
  Computing Surveys, 54(6), 2021.
- Zhang, B. H., et al. "Mitigating Unwanted Biases with Adversarial Learning."
  AAAI/ACM Conference on AI, Ethics, and Society (AIES), 2018.
