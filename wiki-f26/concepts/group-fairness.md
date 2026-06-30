---
title: "Group fairness"
type: concept
description: "Constraining a model to behave equitably across groups defined by a sensitive attribute; statistical metrics (demographic parity, equalized odds, equality of opportunity) and pre-, in-, and post-processing enforcement."
tags:
  - fairness
  - defense
---

## [Wiki Home](../README.md)

# Group fairness

## Definition

Group fairness requires a model to behave equitably across groups defined by a
sensitive attribute such as race, sex, or age. The requirement is stated as a
statistical constraint on the model's predictions conditioned on the sensitive
attribute and the true label. Demographic parity asks that the prediction be
independent of the sensitive attribute; equalized odds asks for equal true- and
false-positive rates across groups; equality of opportunity asks for equal
true-positive rates (Hardt et al., 2016). The constraint is enforced by
pre-processing the training data to remove bias, in-processing through a penalty
or adversarial term in the training objective, or post-processing the model's
outputs to satisfy the chosen metric.

The notion is group-level and statistical. It bounds disparities between
subgroup statistics and makes no promise about any individual. Different metrics
encode different goals and cannot in general be satisfied at once.

## Papers that use this concept

- [SoK: Unintended Interactions among Machine Learning Defenses and Risks](../papers/duddu-2024-unintended-interactions.md) — treats group fairness as a defense and surveys how enforcing it shifts a model's susceptibility to privacy and security risks.
- [PAL\*M: Property Attestation for Large Generative Models](../papers/chantasantitam-2026-palm.md) — fairness is an example attestable property: its attribute-distribution measurement underlies fairness auditing, and it cites zero-knowledge certificates of fairness as the cryptographic route to the same goal.

## Variants and traps

- Demographic parity, equalized odds, and equality of opportunity are distinct
  constraints; satisfying one generally precludes the others.
- The guarantee is over subgroup statistics, so an individual can still be
  treated in a way the group-level metric does not register.

## See also

- [Empirical risk minimization](empirical-risk-minimization.md)
- [Differential privacy](differential-privacy.md)

## References

- Hardt, M., et al. "Equality of Opportunity in Supervised Learning." Advances in
  Neural Information Processing Systems (NeurIPS), 2016.
