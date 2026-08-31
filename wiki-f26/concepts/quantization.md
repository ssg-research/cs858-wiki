---
title: "Quantization"
type: concept
description: "Mapping a model's floating-point weights and activations to low-precision integers under a shared scale; the deployment lever for memory and speed, and the step that makes a model expressible at all in a cryptographic protocol or proof circuit that has no floating point."
tags:
  - machine-learning
  - efficiency
  - cryptography
---

## [Wiki Home](../README.md)

# Quantization

## Definition

Quantization replaces a model's floating-point numbers with low-precision
integers plus a small amount of metadata. A tensor is stored as integers together
with a scale, and sometimes a zero-point, so that each original value is
approximately the scale times its integer. Eight-bit and four-bit integers are
common targets. The result takes a fraction of the memory and runs faster on
hardware with integer arithmetic units, at the cost of an approximation error
that has to stay small enough not to move the model's outputs.

The two standard recipes differ in when the approximation is accounted for.
Post-training quantization converts an already-trained model, calibrating the
scales on a sample of data. Quantization-aware training simulates the rounding
during [fine-tuning](fine-tuning.md), so the weights adapt to it.

For this course the second role matters as much as the first. Homomorphic
encryption, multiparty protocols, and zero-knowledge proof systems compute over
integers or finite-field elements and have no native floating point. A model must
therefore be quantized before it can be expressed as an arithmetic circuit or an
encrypted computation at all, and the quantized model is what any resulting
guarantee is about (Liu et al., 2021). The precision chosen is a joint decision
about accuracy and protocol cost, since wider integers mean more field elements,
larger circuits, and deeper ciphertext arithmetic.

## Papers that use this concept

- [zkGPT: An Efficient Non-interactive Zero-knowledge Proof Framework for LLM Inference](../papers/qu-2025-zkgpt.md) — quantizes weights and activations to field integers, which is what lets floating-point arithmetic be approximated by operations the circuit can express, so the proof covers the quantized model.
- [ModelGuard: Information-Theoretic Defense Against Model Extraction Attacks](../papers/tang-2024-modelguard.md) — solves its perturbation problem by online vector quantization, and orders the quantization incrementally so repeated queries return consistent outputs.
- [PAL*M: Property Attestation for Large Generative Models](../papers/chantasantitam-2026-palm.md) — quantization is one of the post-training operations its attestation catalogue has to cover.

## Variants and traps

- Vector quantization and numeric quantization share a name and a core idea,
  mapping a continuous space to a finite codebook, but they solve different
  problems. One shrinks a model; the other partitions an output space, which is
  how a defense can turn a continuous perturbation into a discrete, repeatable
  one.
- A guarantee proved about a quantized model is a guarantee about that model. An
  attestation, a proof of correct inference, or a robustness certificate carries
  over to the original floating-point model only if something separately bounds
  the gap.
- Reported accuracy under quantization is usually an average. A change too small
  to move average accuracy can still flip individual predictions, which is enough
  to matter when the prediction is the object being watermarked, verified, or
  attacked.

## See also

- [Fine-tuning](fine-tuning.md)
- [Homomorphic encryption](homomorphic-encryption.md)
- [Zero-knowledge proof](zero-knowledge-proof.md)
- [Secure inference](secure-inference.md)

## References

- Liu, T., Xie, X., and Zhang, Y. "zkCNN: Zero Knowledge Proofs for Convolutional
  Neural Network Predictions and Accuracy." ACM Conference on Computer and
  Communications Security (CCS), 2021.
