---
title: "Adversarial examples"
type: concept
description: "Inputs perturbed by a small, often imperceptible amount that cause a trained model to misclassify; the evasion phenomenon, its discovery, and why it is surprising."
tags:
  - adversarial-examples
  - evasion
  - threat-model
---

## [Wiki Home](../README.md)

# Adversarial examples

## Definition

An adversarial example is a correctly classified input perturbed by a small
amount under some norm so that the model misclassifies it (Szegedy et al., 2014;
Goodfellow et al., 2015). "Small" is defined only relative to a
[threat model](adversarial-threat-model.md): a perturbation budget and a
distance, commonly an [ℓp ball](lp-norms.md). The imperceptibility shown in canonical examples
is a proxy for perceptual similarity, which has no closed form.

The phenomenon admits two readings. As a security problem, adversarial examples
are evasion attacks: the adversary selects an input that induces a test-time
error. As a learning problem, they show that the model has fit a decision rule
that agrees with humans on natural inputs but not in their neighborhoods, so it
has not learned the intended concept.

## Papers that use this concept

- [Towards Deep Learning Models Resistant to Adversarial Attacks](../papers/madry-2018-pgd.md) — the phenomenon the paper's min-max formulation is built to suppress.
- [Jailbroken: How Does LLM Safety Training Fail?](../papers/wei-2023-jailbroken.md) — contrasts jailbreaks, which elicit unsafe capabilities, with adversarial examples, which induce misclassification.
- [Neural Cleanse: Identifying and Mitigating Backdoor Attacks in Neural Networks](../papers/wang-2019-neural-cleanse.md) — distinguishes a training-time backdoor trigger, which is input-agnostic, from a test-time adversarial example crafted per input against a fixed model.
- [PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented Generation of Large Language Models](../papers/zou-2024-poisonedrag.md) — its white-box variant crafts an adversarial text optimized to score as similar to the target query under the retriever's encoders.
- [What Makes and Breaks Safety Fine-tuning? A Mechanistic Study](../papers/jain-2024-safety-finetuning.md) — instantiates continuous-embedding adversarial attacks by optimizing appended soft tokens against the model's gradients, in the manner of input-space adversarial examples.
- [SoK: Unintended Interactions among Machine Learning Defenses and Risks](../papers/duddu-2024-unintended-interactions.md) — treats evasion as one surveyed risk and adversarial training as its defense, tracing how deploying that defense shifts unrelated risks.

## Variants and traps

- An adversarial example is a test-time evasion input, distinct from a
  training-time poisoning sample. Both are adversarial; the threat models differ.
- Imperceptibility is not part of the formal definition. A bounded ℓp distance
  is a proxy for perceptual similarity, not the target itself.

## See also

- [Adversarial threat model](adversarial-threat-model.md)
- [ℓp norms](lp-norms.md)
- [Fast Gradient Sign Method (FGSM)](fgsm.md)
- [Adversarial training](adversarial-training.md)
- [Transferability](transferability.md)

## References

- Szegedy, C., Zaremba, W., Sutskever, I., Bruna, J., Erhan, D., Goodfellow,
  I., and Fergus, R. "Intriguing Properties of Neural Networks." International
  Conference on Learning Representations (ICLR), 2014.
- Goodfellow, I. J., Shlens, J., and Szegedy, C. "Explaining and Harnessing
  Adversarial Examples." International Conference on Learning Representations
  (ICLR), 2015.
