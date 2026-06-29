---
title: "Memorization"
type: concept
description: "Neural networks' capacity to fit individual training examples, including random labels; the long-tail argument that some memorization is necessary for generalization; the per-example signal privacy attacks exploit."
tags:
  - memorization
  - privacy
  - machine-learning
---

### [Wiki Home](../README.md)

# Memorization

## Definition

A model memorizes a training example when its behavior on that example depends
strongly on the example's presence in the training set, rather than on patterns
shared with the rest of the data. Deep networks have ample capacity for this:
standard architectures can reach perfect training accuracy even on randomly
labeled data, where generalization is impossible by construction (Zhang et al.,
2021). Memorization is not merely a pathology of overfitting. For natural data
distributions with a long tail of rare or atypical examples, fitting those
examples individually may be necessary for optimal accuracy, so well-trained,
well-generalizing models memorize too (Feldman, 2020; Feldman and Zhang, 2020).

Memorization is per-example where the generalization gap is aggregate. Two
models with the same train-test gap can memorize very different examples to
very different degrees, and outliers are memorized far more than inliers,
because the model has no other way to get them right. This per-example signal
is what training-data privacy attacks exploit: an example whose presence
changes the model measurably is an example whose presence can be inferred.

## Papers that use this concept

- [Membership Inference Attacks From First Principles](../papers/carlini-2022-lira.md) — per-example memorization differences are why its per-example hypothesis test beats global-threshold attacks, and why out-of-distribution examples are the most exposed.
- [Deep Learning with Differential Privacy](../papers/abadi-2016-dp-sgd.md) — the capacity of networks to encode individual examples is the leakage DP-SGD provably bounds.
- [Extracting Training Data from Large Language Models](../papers/carlini-2021-extracting-training-data.md) — shows large LMs memorize individual training examples verbatim and that this persists with no overfitting; defines k-eidetic memorization.
- [Knowledge Unlearning for Mitigating Privacy Risks in Language Models](../papers/jang-2022-knowledge-unlearning.md) — targets the per-example memorization that makes specific sequences extractable, and edits it away with gradient ascent.
- [DAWN: Dynamic Adversarial Watermarking of Neural Networks](../papers/szyller-2019-dawn.md) — relies on a surrogate's capacity to memorize a small set of deliberately mislabeled queries, which embeds as the watermark.
- [Representation Engineering: A Top-Down Approach to AI Transparency](../papers/zou-2023-representation-engineering.md) — reads a memorization direction to detect memorized text and steers it down to reduce verbatim regurgitation with little loss of world knowledge.
- [SoK: Unintended Interactions among Machine Learning Defenses and Risks](../papers/duddu-2024-unintended-interactions.md) — makes memorization, together with overfitting, the conjectured common cause of every unintended interaction it surveys.
- [Unlocking the Power of Differentially Private Zeroth-order Optimization for Fine-tuning LLMs](../papers/bao-2025-dp-zo.md) — the verbatim memorization of fine-tuning data that its private optimizer is built to bound.

## Variants and traps

- Memorization and overfitting are not synonyms. The generalization gap is an
  average; memorization is per-example, and persists in models with small
  gaps.
- "The model memorized X" ranges from verbatim recovery to a statistically
  detectable influence; which sense is meant changes what an attack or defense
  must show.

## See also

- [Membership inference](membership-inference.md)
- [Empirical risk minimization](empirical-risk-minimization.md)
- [Differential privacy](differential-privacy.md)

### [Wiki Home](../README.md)

## References

- Feldman, V. "Does Learning Require Memorization? A Short Tale about a Long
  Tail." ACM Symposium on Theory of Computing (STOC), 2020.
- Feldman, V. and Zhang, C. "What Neural Networks Memorize and Why:
  Discovering the Long Tail via Influence Estimation." arXiv:2008.03703, 2020.
- Zhang, C., Bengio, S., Hardt, M., Recht, B., and Vinyals, O. "Understanding
  Deep Learning (Still) Requires Rethinking Generalization." Communications of
  the ACM, 64(3), 2021.
