---
title: "Model watermarking"
type: concept
description: "Embedding an owner-verifiable marker in a trained model to later claim ownership of a copy: white-box (marker in the weights) vs black-box (backdoor-based trigger-set) verification, and the assumption that the owner controls training."
tags:
  - watermarking
  - ip-protection
  - model-extraction
  - threat-model
---

### [Wiki Home](../README.md)

# Model watermarking

## Definition

Model watermarking embeds an owner-verifiable marker into a trained model so
that the owner can later demonstrate ownership of a copy. It transfers the idea
of digital watermarking, embedding a hidden marker in a media object such as an
image or audio file, to the parameters or behavior of a neural network. Schemes
divide by the access needed to verify the mark. White-box schemes embed the
marker directly in the weights and verify it by inspecting the parameters, which
requires access to the suspected model's internals (Uchida et al., 2017).
Black-box schemes verify the marker through the prediction API alone.

Black-box model watermarking is built on [backdooring](backdoor-attacks.md). The
owner trains the model to return chosen, usually incorrect, outputs on a secret
*trigger set* of inputs, while behaving normally everywhere else. Ownership is
demonstrated by querying the trigger set and checking that the suspected model
reproduces the planted responses (Adi et al., 2018; Zhang et al., 2018; Le
Merrer et al., 2017; Darvish Rouhani et al., 2019). The distribution of the
trigger set relative to the training data affects how reliably the mark embeds
and how hard it is to remove by retraining.

## Papers that use this concept

- [DAWN: Dynamic Adversarial Watermarking of Neural Networks](../papers/szyller-2019-dawn.md) — moves the watermark from the trained model to the prediction API, so the extraction adversary's own surrogate training embeds a trigger set the owner can later verify.
- [SoK: Unintended Interactions among Machine Learning Defenses and Risks](../papers/duddu-2024-unintended-interactions.md) — treats watermarking and fingerprinting as ownership defenses and surveys how their reliance on memorization interacts with privacy and fairness risks.
- [A Watermark for Large Language Models](../papers/kirchenbauer-2023-llm-watermark.md) — marks the model's generated text for provenance rather than its weights for ownership, the output-watermarking counterpart to these model-marking schemes.

## Variants and traps

- Model watermarking marks the model (ownership of the asset). It is distinct
  from output or text watermarking, which marks the content a model generates.
- Training-time schemes assume the owner controls training and can pick the
  trigger set from the whole input space; both assumptions fail when an
  adversary trains the model under attack.

## See also

- [Backdoor attacks](backdoor-attacks.md)
- [Model extraction](model-extraction.md)
- [Cryptographic commitment](cryptographic-commitment.md)

### [Wiki Home](../README.md)

## References

- Adi, Y., Baum, C., Cisse, M., Pinkas, B., and Keshet, J. "Turning Your Weakness Into a Strength: Watermarking Deep Neural Networks by Backdooring." USENIX Security Symposium, 2018.
- Darvish Rouhani, B., Chen, H., and Koushanfar, F. "DeepSigns: An End-to-End Watermarking Framework for Ownership Protection of Deep Neural Networks." International Conference on Architectural Support for Programming Languages and Operating Systems (ASPLOS), 2019.
- Le Merrer, E., Perez, P., and Trédan, G. "Adversarial Frontier Stitching for Remote Neural Network Watermarking." arXiv:1711.01894, 2017.
- Uchida, Y., Nagai, Y., Sakazawa, S., and Satoh, S. "Embedding Watermarks into Deep Neural Networks." ACM International Conference on Multimedia Retrieval (ICMR), 2017.
- Zhang, J., Gu, Z., Jang, J., Wu, H., Stoecklin, M.Ph., Huang, H., and Molloy, I. "Protecting Intellectual Property of Deep Neural Networks with Watermarking." ACM Asia Conference on Computer and Communications Security (AsiaCCS), 2018.
