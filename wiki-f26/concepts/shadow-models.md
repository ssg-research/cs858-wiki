---
title: "Shadow models"
type: concept
description: "Models an adversary trains on its own data, sampled from the target's distribution, to imitate and calibrate against the target model; the core technique enabling trained attacks and per-example calibration in membership inference."
tags:
  - membership-inference
  - privacy
  - attack
---

### [Wiki Home](../README.md)

# Shadow models

## Definition

A shadow model is a model the adversary trains itself, on data drawn from the
same distribution as the target model's training set, so that its behavior
stands in for the target's. The technique was introduced for membership
inference: by training many shadow models on datasets where the adversary
*knows* which examples are members, the adversary can learn what member and
non-member behavior looks like, then apply that knowledge to the real target
(Shokri et al., 2017).

Shadow models turn one unanswerable question (how does the target behave on
its members?) into a measurable one (how do models like the target behave on
known members?). Later attacks refined the granularity: instead of learning a
single global member/non-member classifier, they train shadow models with and
without a specific example (IN and OUT models for that example) to estimate
how that particular example's loss distribution shifts when it is trained on.
The main cost is compute, since every shadow model is a full training run, and
the main assumption is access to enough data from the target's distribution.

## Papers that use this concept

- [Membership Inference Attacks From First Principles](../papers/carlini-2022-lira.md) — trains IN/OUT shadow models per example to estimate the two loss distributions its likelihood-ratio test compares.
- [No Privacy Left Outside: On the (In-)Security of TEE-Shielded DNN Partition for On-Device ML](../papers/zhang-2024-tee-shielded.md) — the membership-inference attacks train shadow models on a shadow data split to calibrate the decision against each partition scheme.

## Variants and traps

- "Online" use trains shadow models on the target example after it is known;
  "offline" use trains them in advance on data excluding it. The offline form
  trades some power for not retraining per query.
- The adversary's shadow data need not overlap the target's training set, but
  a distribution shift between them degrades the attack.

## See also

- [Membership inference](membership-inference.md)
- [Memorization](memorization.md)
- [White-box and black-box access](white-box-black-box.md)

### [Wiki Home](../README.md)

## References

- Shokri, R., Stronati, M., Song, C., and Shmatikov, V. "Membership Inference
  Attacks Against Machine Learning Models." IEEE Symposium on Security and
  Privacy, 2017.
