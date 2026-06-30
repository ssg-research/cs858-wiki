---
title: "Transferability"
type: concept
description: "Adversarial examples crafted against one model often fool a different model trained for the same task; the basis of black-box transfer attacks."
tags:
  - evasion
  - adversarial-examples
  - threat-model
---

## [Wiki Home](../README.md)

# Transferability

## Definition

An adversarial example crafted against one model often fools a different model
trained for the same task, even across architectures and training sets. The
effect was observed alongside the discovery of adversarial examples for deep
networks (Szegedy et al., 2014) and was later developed into a systematic
black-box attack technique (Papernot et al., 2016): the attacker trains or
obtains a surrogate model, attacks the surrogate with full
[white-box](white-box-black-box.md) access, and replays the resulting inputs
against the target. Transferability is why withholding a model's weights is
weaker protection than it appears.

## Papers that use this concept

- [Towards Deep Learning Models Resistant to Adversarial Attacks](../papers/madry-2018-pgd.md) — uses transfer attacks as its black-box evaluation setting.
- [PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented Generation of Large Language Models](../papers/zou-2024-poisonedrag.md) — in the black-box setting the injected texts must be retrieved and effective against retrievers and LLMs the attacker cannot query.

## See also

- [White-box and black-box access](white-box-black-box.md)
- [Adversarial examples](adversarial-examples.md)

## References

- Szegedy, C., Zaremba, W., Sutskever, I., Bruna, J., Erhan, D., Goodfellow,
  I., and Fergus, R. "Intriguing Properties of Neural Networks." International
  Conference on Learning Representations (ICLR), 2014.
- Papernot, N., McDaniel, P., and Goodfellow, I. "Transferability in Machine
  Learning: from Phenomena to Black-Box Attacks using Adversarial Samples."
  arXiv:1605.07277, 2016.
