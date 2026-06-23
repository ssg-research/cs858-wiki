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
- [Deep Learning with Differential Privacy](../papers/abadi-2016-dp-sgd.md) — its guarantee holds against a white-box adversary with full access to the released parameters.
- [Jailbroken: How Does LLM Safety Training Fail?](../papers/wei-2023-jailbroken.md) — its adversary is a black-box chat user who rewrites the prompt but cannot see weights or alter the system prompt or message history.
- [Extracting Training Data from Large Language Models](../papers/carlini-2021-extracting-training-data.md) — its adversary has only black-box query access: it samples continuations and reads sequence probabilities, with no view of weights or hidden states.
- [Knockoff Nets: Stealing Functionality of Black-Box Models](../papers/orekondy-2019-knockoff-nets.md) — its adversary has only black-box query access to an image classifier, reading posterior probability vectors with no view of weights, architecture, or training data.
- [DAWN: Dynamic Adversarial Watermarking of Neural Networks](../papers/szyller-2019-dawn.md) — both the extraction adversary and the owner's ownership check operate over black-box query access to a prediction API.
- [Neural Cleanse: Identifying and Mitigating Backdoor Attacks in Neural Networks](../papers/wang-2019-neural-cleanse.md) — the defender has white-box access to the trained model (weights, gradients, neuron activations) but not to its training data.
- [PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented Generation of Large Language Models](../papers/zou-2024-poisonedrag.md) — splits the attack by the adversary's knowledge of the retriever: black-box (no parameters, no queries) versus white-box (retriever parameters available to optimize against).
- [Representation Engineering: A Top-Down Approach to AI Transparency](../papers/zou-2023-representation-engineering.md) — its analyst has white-box access to the model's internal activations at every layer and token, the access representation reading and control require.
- [SoK: Unintended Interactions among Machine Learning Defenses and Risks](../papers/duddu-2024-unintended-interactions.md) — spans defenses and risks across both white-box and black-box access to the model, defining its observables over that range.
- [Examining Zero-Shot Vulnerability Repair with Large Language Models](../papers/pearce-2023-vulnerability-repair.md) — the developer or repair pipeline has black-box access to the commercial code models, seeing only generated completions through an API, not weights or gradients.
- [No Privacy Left Outside: On the (In-)Security of TEE-Shielded DNN Partition for On-Device ML](../papers/zhang-2024-tee-shielded.md) — the protection goal is downgrading white-box stealing and membership inference to black-box label-only attacks; the paper measures how far short the partitions fall.
- [ModelGuard: Information-Theoretic Defense Against Model Extraction Attacks](../papers/tang-2024-modelguard.md) — its adversary has black-box query access to the prediction API, reading perturbed confidence vectors, and in the strong case additionally knows the target's architecture.

## See also

- [Adversarial threat model](adversarial-threat-model.md)
- [Transferability](transferability.md)
