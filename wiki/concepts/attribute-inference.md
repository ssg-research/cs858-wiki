---
title: "Attribute inference"
type: concept
description: "Inferring the value of a sensitive, hidden input attribute of a record (e.g., race) from a model's observable behavior, exploiting that observables differ by attribute value; distinct from membership inference and from property inference over the whole distribution, with an open debate over whether it reduces to imputation."
tags:
  - privacy
  - attribute-inference
  - machine-learning
---

# Attribute inference

## Definition

Attribute inference recovers the value of a sensitive input attribute of a
specific record, for example a person's race, from a model's observable behavior.
It works when the observables (outputs, activations, gradients) are
distinguishable for different values of the attribute, so the hidden value can be
read back off the model. The privacy violation is that an attribute an individual
chose not to disclose is recovered from a model trained on their data.

Attribute inference targets one record's hidden attribute, which separates it from
[membership inference](membership-inference.md) (is this record in the training
set?) and from [property inference](property-inference.md) (what is a property of
the whole training distribution?). Whether attribute inference reveals anything
beyond ordinary statistical imputation from correlations in the data is debated,
and the answer depends on the threat model assumed.

## Papers that use this concept

- [SoK: Unintended Interactions among Machine Learning Defenses and Risks](../papers/duddu-2023-unintended-interactions.md) — one of its privacy risks; the paper relates it to memorization of sensitive attributes and to the distinguishability of observables across subgroups.

## Variants and traps

- Distinct from [property inference](property-inference.md): attribute inference
  is record-level, property inference is distribution-level.
- Whether it is "just imputation" is contested; the gap is what the attack adds
  beyond predicting the attribute from public correlations.

## See also

- [Membership inference](membership-inference.md)
- [Property (distribution) inference](property-inference.md)
- [Algorithmic fairness](algorithmic-fairness.md)

## References

- Fredrikson, M., et al. "Model Inversion Attacks that Exploit Confidence
  Information and Basic Countermeasures." ACM Conference on Computer and
  Communications Security (CCS), 2015.
- Jayaraman, B. and Evans, D. "Are Attribute Inference Attacks Just Imputation?"
  ACM Conference on Computer and Communications Security (CCS), 2022.
