---
title: "White-box and black-box access"
type: concept
description: "Adversary knowledge assumptions: white-box (full model, weights, gradients), black-box (query or transfer access only), and intermediate notions such as the first-order adversary."
tags:
  - threat-model
  - evasion
---

# White-box and black-box access

## Definition

Access assumptions state what the adversary knows about the target model. A
white-box adversary has everything: architecture, weights, and therefore
gradients. A black-box adversary sees only the model's outputs through queries,
or has no query access at all and must rely on
[transferability](transferability.md) from a surrogate model. Between the two
sit intermediate notions; the most common is the first-order adversary, which
may compute gradients of the loss with respect to the input but use no
higher-order information. White-box is the worst case for the defender, so
defense evaluations default to it. Papers define "grey-box" inconsistently, so
read each paper's definition rather than assuming one.

## Papers that use this concept

- [Towards Deep Learning Models Resistant to Adversarial Attacks](../papers/madry-2018-pgd.md) — evaluates white-box and transfer adversaries and argues its guarantee for the first-order class.
- [Membership Inference Attacks From First Principles](../papers/carlini-2022-lira.md) — its adversary is black-box, querying confidence outputs with no access to weights or gradients.

## See also

- [Adversarial threat model](adversarial-threat-model.md)
- [Transferability](transferability.md)
