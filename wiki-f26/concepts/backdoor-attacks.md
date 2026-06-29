---
title: "Backdoor attacks"
type: concept
description: "A hidden secondary behavior trained into a model: normal on ordinary inputs, attacker-chosen output when a trigger is present; planted via data poisoning, enabled by DNN overcapacity, and reused as the mechanism behind black-box model watermarking."
tags:
  - backdoor
  - poisoning
  - threat-model
  - machine-learning
---

### [Wiki Home](../README.md)

# Backdoor attacks

## Definition

A backdoor is a hidden secondary behavior trained into a model. The model
behaves normally on ordinary inputs, but produces an attacker-chosen output
whenever a specific trigger appears in the input. The usual way to plant one is
data poisoning: adding trigger-carrying inputs with the attacker's chosen labels
to the training set, so the model learns the trigger-to-output association
alongside its primary task (Gu et al., 2017; Chen et al., 2017). Other variants
manipulate the training process or the model directly (Liu et al., 2018).

Backdoors are possible because of overcapacity: a deep network can fit a subset
of inputs with arbitrary, even incorrect, labels without measurably degrading
its primary task (Zhang et al., 2017). See [memorization](memorization.md). The
same mechanism is repurposed defensively in black-box
[model watermarking](model-watermarking.md), where the "backdoor" is a trigger
set the owner plants and keeps secret in order to prove ownership later, rather
than an output an attacker plants to cause harm.

## Papers that use this concept

- [DAWN: Dynamic Adversarial Watermarking of Neural Networks](../papers/szyller-2019-dawn.md) — the watermark it embeds in a stolen surrogate is a backdoor: a trigger set of API queries returned with deliberately incorrect labels.
- [Neural Cleanse: Identifying and Mitigating Backdoor Attacks in Neural Networks](../papers/wang-2019-neural-cleanse.md) — the threat it defends against; it detects whether a trained classifier hides a backdoor, reverse-engineers the trigger, and patches the model to disable it.
- [PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented Generation of Large Language Models](../papers/zou-2024-poisonedrag.md) — a poisoning attack adjacent to backdoors, but the planted text corrupts an inference-time retrieval corpus rather than a training set.
- [SoK: Unintended Interactions among Machine Learning Defenses and Risks](../papers/duddu-2024-unintended-interactions.md) — frames backdoor-based watermarking as a defense that deliberately memorizes triggers, and surveys how that interacts with privacy and fairness risks.

## Variants and traps

- A backdoor is planted at training time and fired by a known trigger; an
  adversarial example is crafted at test time against a fixed model. The two
  exploit different stages of the pipeline.
- The same trigger-set machinery serves opposite goals: harm (a malicious
  backdoor) or proof of ownership (a watermark). What changes is who controls
  the trigger set and why.

## See also

- [Memorization](memorization.md)
- [Model watermarking](model-watermarking.md)

### [Wiki Home](../README.md)

## References

- Chen, X., Liu, C., Li, B., Lu, K., and Song, D. "Targeted Backdoor Attacks on Deep Learning Systems Using Data Poisoning." arXiv:1712.05526, 2017.
- Gu, T., Dolan-Gavitt, B., and Garg, S. "BadNets: Identifying Vulnerabilities in the Machine Learning Model Supply Chain." arXiv:1708.06733, 2017.
- Liu, Y., Ma, S., Aafer, Y., Lee, W.-C., Zhai, J., Wang, W., and Zhang, X. "Trojaning Attack on Neural Networks." Network and Distributed System Security Symposium (NDSS), 2018.
- Zhang, C., Bengio, S., Hardt, M., Recht, B., and Vinyals, O. "Understanding Deep Learning Requires Rethinking Generalization." International Conference on Learning Representations (ICLR), 2017. arXiv:1611.03530.
