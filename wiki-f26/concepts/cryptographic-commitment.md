---
title: "Cryptographic commitment"
type: concept
description: "A binding, hiding token published for a value without revealing it, opened later to prove what was committed; with a time-stamped public log it gives proof of anteriority, used to fix model-ownership claims before any dispute."
tags:
  - cryptography
  - ip-protection
---

[Home page](../README.md)

# Cryptographic commitment

## Definition

A commitment scheme lets a party publish a short token, the commitment, that
fixes a value without revealing it, and later open the token to prove which value
was committed. The scheme is *hiding* (the commitment leaks nothing about the
value) and *binding* (the committer cannot later open it to a different value). A
common instantiation is a cryptographic hash of the value together with a random
nonce.

Publishing a commitment on a public, time-stamped, append-only log, a bulletin
board such as a blockchain, adds proof of anteriority: evidence that the
committed value existed no later than the post. In model-ownership settings this
lets an owner commit to a model, and to per-claim secrets, before any dispute
arises, so that a later claimant cannot fabricate an earlier-looking claim. The
commitment carries the proof of priority; a separate trusted party or protocol
checks the opened values against a suspected model.

## Papers that use this concept

- [DAWN: Dynamic Adversarial Watermarking of Neural Networks](../papers/szyller-2019-dawn.md) — the owner registers commitments to the protected model and to each client's watermark on a public bulletin board, so a trusted judge can later confirm ownership and its priority in time.
- [zkGPT: An Efficient Non-interactive Zero-knowledge Proof Framework for LLM Inference](../papers/qu-2025-zkgpt.md) — a polynomial commitment to the model weights fixes one model in advance, so the zero-knowledge proof certifies inference under the committed weights and the prover cannot swap models between queries.
- [PAL\*M: Property Attestation for Large Generative Models](../papers/chantasantitam-2026-palm.md) — notes the cryptographic-attestation alternative, where publicly verifiable commitments bind a model's training and inference for auditing, in contrast to its own hardware-rooted measurements.

## See also

- [Model watermarking](model-watermarking.md)
