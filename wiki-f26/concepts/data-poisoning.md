---
title: "Data poisoning"
type: concept
description: "Corrupting a model's training data to change what it learns: availability poisoning that degrades overall accuracy versus targeted/integrity poisoning that forces specific misclassifications, with backdoor attacks as the trigger-conditioned subclass; and why training-set sanitization defenses assume access poisoning defenders may not have."
tags:
  - poisoning
  - threat-model
  - machine-learning
---

## [Wiki Home](../README.md)

# Data poisoning

## Definition

Data poisoning is an attack on the training stage: the adversary alters the
training data so the learned model behaves the way the attacker wants. The goals
divide along what behavior is corrupted. Availability (indiscriminate) poisoning
degrades the model's accuracy broadly, denying its owner a usable model.
Integrity (targeted) poisoning leaves overall accuracy intact and instead forces
chosen misclassifications (Jagielski et al., 2018; Steinhardt et al., 2017).
[Backdoor attacks](backdoor-attacks.md) are the trigger-conditioned subclass of
targeted poisoning: trigger-stamped, mislabeled samples are mixed into the
training set so the model learns to map the trigger to an attacker-chosen label
while behaving normally otherwise (Gu et al., 2017; Chen et al., 2017).

Poisoning is a training-time threat, distinct from a test-time
[adversarial example](adversarial-examples.md) that perturbs an input against a
fixed model. Defenses against classic poisoning center on training-set
sanitization: identify and remove the samples that change the model most. That
approach presumes the defender holds the (poisoned) training set, and it targets
samples that visibly shift performance, so it transfers poorly to backdoors,
whose poison samples leave clean-input accuracy untouched.

## Papers that use this concept

- [Neural Cleanse: Identifying and Mitigating Backdoor Attacks in Neural Networks](../papers/wang-2019-neural-cleanse.md) — defends against backdoors planted by poisoning training data with trigger-stamped, mislabeled inputs, in a setting where the defender holds only the trained model and so cannot sanitize the training set.
- [PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented Generation of Large Language Models](../papers/zou-2024-poisonedrag.md) — relocates poisoning from the training set to a deployed RAG system's inference-time knowledge base, which no model is trained on.
- [SoK: Unintended Interactions among Machine Learning Defenses and Risks](../papers/duddu-2024-unintended-interactions.md) — covers poisoning as a surveyed risk with outlier removal as its defense, and notes how watermarking reuses poisoning to plant ownership markers.

## Variants and traps

- Availability, targeted, and backdoor poisoning share the vector (corrupt the
  training data) but differ in goal; a defense built for one need not work on
  another.
- Sanitization defenses assume access to the training data. A defender who
  receives only the trained model cannot inspect or clean the data, which changes
  what defenses are even available.

## See also

- [Backdoor attacks](backdoor-attacks.md)
- [Adversarial examples](adversarial-examples.md)
- [Memorization](memorization.md)

## References

- Chen, X., Liu, C., Li, B., Lu, K., and Song, D. "Targeted Backdoor Attacks on Deep Learning Systems Using Data Poisoning." arXiv:1712.05526, 2017.
- Gu, T., Dolan-Gavitt, B., and Garg, S. "BadNets: Identifying Vulnerabilities in the Machine Learning Model Supply Chain." Machine Learning and Computer Security Workshop, 2017. arXiv:1708.06733.
- Jagielski, M., Oprea, A., Biggio, B., Liu, C., Nita-Rotaru, C., and Li, B. "Manipulating Machine Learning: Poisoning Attacks and Countermeasures for Regression Learning." IEEE Symposium on Security and Privacy (S&P), 2018.
- Steinhardt, J., Koh, P.W., and Liang, P.S. "Certified Defenses for Data Poisoning Attacks." Advances in Neural Information Processing Systems (NIPS), 2017.
