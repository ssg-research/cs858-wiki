---
title: "Secure inference"
type: concept
description: "The two-party problem of running model inference on a client's private input against a server's private model so the server learns nothing about the input and the client learns nothing about the model beyond the result; HE-, MPC-, and TEE-based instantiations and the interaction / bandwidth cost axes."
tags:
  - secure-inference
  - cryptography
  - privacy
---

### [Wiki Home](../README.md)

# Secure inference

## Definition

Secure inference (also private or oblivious inference) is the problem of
evaluating a machine-learning model on an input held by one party using a model
held by another, keeping both private. In the standard two-party form a client
holds an input and a server holds a trained model; the protocol returns the
prediction to the client so that the server learns nothing about the input and
the client learns nothing about the model beyond what the output reveals. The
model architecture and the input dimensions are usually treated as public; the
protected secrets are the client's data values and the server's weights.
Security is typically argued against a
[semi-honest adversary](secure-multiparty-computation.md) in the simulation
paradigm.

Protocols are built from [homomorphic encryption](homomorphic-encryption.md),
where the server computes on encrypted inputs;
[secure multiparty computation](secure-multiparty-computation.md), where the
parties secret-share the computation and interact;
[trusted execution environments](trusted-execution-environment.md), where a
hardware enclave runs the model on decrypted data behind an attested boundary; or
hybrids of these. Linear layers are cheap under HE or
secret sharing, so the nonlinear layers (ReLU, GELU, softmax, argmax) are the
expensive part and the main design problem. The cost has three axes: local
computation, the number of communication rounds, and total bandwidth. An
interactive protocol incurs many rounds and large transcripts, which dominate
latency on wide-area networks; a non-interactive protocol collapses the exchange
to a single round, one encrypted input and one encrypted reply, trading
interaction for heavier server-side computation. Early systems targeted
[convolutional networks](convolutional-neural-network.md) (Juvekar et al., 2018;
Mishra et al., 2020); extending them to transformers raises the cost of large
matrix products and of a vocabulary-sized argmax.

## Papers that use this concept

- [Secure Transformer Inference Made Non-interactive](../papers/zhang-2025-nexus.md) — the first non-interactive (single-round) protocol for secure transformer inference, built on RNS-CKKS homomorphic encryption.
- [BliMe: Verifiably Secure Outsourced Computation with Hardware-Enforced Taint Tracking](../papers/elatali-2024-blime.md) — the hardware-side instantiation: an untrusted server computes on the client's plaintext, with hardware taint tracking, rather than encryption or enclave isolation, keeping the input confidential.

## Variants and traps

- What the output reveals is part of the threat model: returning a full
  probability vector leaks more than returning only the top label, so the choice
  of output is a privacy decision, not just an interface one.
- Secure inference protects the input and the weights during one inference run.
  It is separate from training-time guarantees such as
  [differential privacy](differential-privacy.md), which bound what the trained
  model itself memorizes.

## See also

- [Homomorphic encryption](homomorphic-encryption.md)
- [Secure multiparty computation](secure-multiparty-computation.md)
- [Trusted execution environment](trusted-execution-environment.md)
- [Ciphertext packing (SIMD batching)](ciphertext-packing.md)

### [Wiki Home](../README.md)

## References

- Juvekar, C., Vaikuntanathan, V., and Chandrakasan, A. "GAZELLE: A Low Latency
  Framework for Secure Neural Network Inference." USENIX Security Symposium,
  2018.
- Mishra, P., Lehmkuhl, R., Srinivasan, A., Zheng, W., and Popa, R. A. "Delphi:
  A Cryptographic Inference Service for Neural Networks." USENIX Security
  Symposium, 2020.
