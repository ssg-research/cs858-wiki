---
title: "Property (distribution) inference"
type: concept
description: "Inferring a global property of a model's training distribution, such as the fraction of records with a given attribute, rather than anything about one record; distribution inference, property inference on shared and federated models, and its distinction from attribute and membership inference."
tags:
  - privacy
  - property-inference
  - machine-learning
---

# Property (distribution) inference

## Definition

Property inference, also called distribution inference, recovers an aggregate
property of the distribution a model was trained on, for example the proportion
of training records belonging to a given subgroup. The target is the dataset as a
whole, not any individual record. The adversary typically trains many shadow
models on datasets that do or do not have the property, learns to tell their
observable behavior apart, and applies that discriminator to the target model.

The property may be sensitive even when no single record is exposed: learning
that a hospital's training set skews heavily toward one demographic can leak
business or population information. This makes property inference distinct from
[membership inference](membership-inference.md), which targets one record's
presence, and from [attribute inference](attribute-inference.md), which targets
one record's hidden attribute value.

## Papers that use this concept

- [SoK: Unintended Interactions among Machine Learning Defenses and Risks](../papers/duddu-2023-unintended-interactions.md) — one of its privacy risks; the paper conjectures and empirically tests that releasing model explanations raises distribution-inference success.

## Variants and traps

- Distribution/property inference (a property of the whole training set) is often
  confused with attribute inference (a hidden attribute of one record); the unit
  of leakage differs.

## See also

- [Attribute inference](attribute-inference.md)
- [Membership inference](membership-inference.md)
- [Shadow models](shadow-models.md)

## References

- Ganju, K., et al. "Property Inference Attacks on Fully Connected Neural Networks
  Using Permutation Invariant Representations." ACM Conference on Computer and
  Communications Security (CCS), 2018.
- Suri, A. and Evans, D. "Formalizing and Estimating Distribution Inference
  Risks." Privacy Enhancing Technologies Symposium (PETS), 2022.
