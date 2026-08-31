---
title: "Model fingerprinting"
type: concept
description: "Identifying a model by properties it already has, usually its decision boundary probed with a chosen input set, rather than by a marker embedded at training time; the training-free counterpart to model watermarking for ownership claims, and what it gives up in exchange."
tags:
  - model-extraction
  - ip-protection
  - machine-learning
---

## [Wiki Home](../README.md)

# Model fingerprinting

## Definition

Fingerprinting establishes a model's identity from characteristics the model
already carries. Nothing is planted. The usual construction chooses inputs that
sit close to the model's decision boundary, where models that are otherwise
similar disagree, and treats the model's answers on that set as its fingerprint;
a suspect model that answers the same way is claimed to derive from the original
(Cao et al., 2021).

The trade against [model watermarking](model-watermarking.md) runs in both
directions. Watermarking requires control of training, or of what the prediction
API returns, and it plants deliberately wrong answers, so it costs a little
accuracy and has to be arranged before the model is exposed. Fingerprinting
requires neither: it applies to a model that is already trained and deployed, at
no accuracy cost, and it can be constructed after a theft is suspected. What it
gives up is the secret. A watermark's evidential force comes from the owner
having planted something no one else could have known; a fingerprint's rests on
the claim that the measured property is distinctive to this model and survives
whatever the thief did to it, and both halves of that claim are empirical.

Verification is [black-box](white-box-black-box.md) in either case: the owner
queries the suspect model through its interface and compares answers.

## Papers that use this concept

- [SoK: Unintended Interactions among Machine Learning Defenses and Risks](../papers/duddu-2024-unintended-interactions.md) — lists watermarking and fingerprinting together as the ownership defenses whose side effects it surveys.
- [DAWN: Dynamic Adversarial Watermarking of Neural Networks](../papers/szyller-2019-dawn.md) — sits on the watermarking side of this split, and its problem is exactly the one fingerprinting sidesteps, that the owner does not train the surrogate it wants to claim.
- [ModelGuard: Information-Theoretic Defense Against Model Extraction Attacks](../papers/tang-2024-modelguard.md) — groups boundary-fingerprinting with watermarking as the ownership defenses that claim a copy after the fact, the category its preventive output perturbation is set against.

## Variants and traps

- Fingerprinting a model and fingerprinting generated content are different
  problems with one word. This page is about identifying the model;
  [LLM watermarking](llm-watermarking.md) is about marking the text a model
  produces.
- Neither fingerprints nor watermarks are proof of ownership on their own. Both
  are evidence a judge weighs, and both need something that fixes priority, such
  as a [cryptographic commitment](cryptographic-commitment.md) published before
  the dispute.
- A fingerprint's inputs are near the decision boundary by construction, which is
  the same region [adversarial examples](adversarial-examples.md) live in, so a
  model that has been adversarially trained or otherwise had its boundary moved
  may no longer answer the way its fingerprint expects.

## See also

- [Model watermarking](model-watermarking.md)
- [Model extraction](model-extraction.md)
- [Functionality stealing](functionality-stealing.md)
- [Cryptographic commitment](cryptographic-commitment.md)

## References

- Cao, X., Jia, J., and Gong, N.Z. "IPGuard: Protecting Intellectual Property of
  Deep Neural Networks via Fingerprinting the Classification Boundary." ACM Asia
  Conference on Computer and Communications Security (AsiaCCS), 2021.
