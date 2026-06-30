---
title: "Secure multiparty computation"
type: concept
description: "Cryptographic protocols that let parties jointly compute a function over their private inputs while revealing only the output; two-party computation, garbled circuits and secret sharing, the semi-honest vs malicious adversary models, and simulation-based security."
tags:
  - secure-computation
  - cryptography
  - privacy
---

## [Wiki Home](../README.md)

# Secure multiparty computation

## Definition

Secure multiparty computation (MPC) is a family of cryptographic protocols in
which several parties, each holding a private input, jointly compute an agreed
function and learn its output and nothing else about one another's inputs. The
two-party case (2PC) is the usual setting for client-server problems. Two
technique families dominate: garbled circuits, where one party encrypts a
boolean circuit gate by gate and the other evaluates it obliviously, and secret
sharing, where each value is split into shares held by different parties who
compute on the shares, often aided by oblivious transfer and by correlated
randomness produced in an input-independent offline phase. Linear operations are
cheap under secret sharing; the nonlinear ones (comparisons, maxima,
exponentials) usually cost extra rounds of interaction.

Security is stated in the simulation paradigm: a protocol is secure if a
corrupted party's view can be reproduced by a simulator given only that party's
own input and the output, so the protocol reveals nothing beyond the output. The
adversary model fixes how a corrupted party behaves. A semi-honest
(honest-but-curious) adversary follows the protocol but tries to infer extra
information from its transcript; a malicious adversary may deviate arbitrarily.
Semi-honest security is the weaker and cheaper guarantee. The recurring cost of
MPC is communication: protocols exchange data across many rounds, so bandwidth
and round-trip latency, rather than local compute, often set the running time,
especially over wide-area networks. This is the axis along which
[homomorphic encryption](homomorphic-encryption.md), where one party computes
locally on ciphertexts with no interaction, makes the opposite trade.

## Papers that use this concept

- [Secure Transformer Inference Made Non-interactive](../papers/zhang-2025-nexus.md) — frames its single-round protocol against interactive two-party and secret-sharing secure-inference baselines, whose round and bandwidth cost it sets out to remove.
- [No Privacy Left Outside: On the (In-)Security of TEE-Shielded DNN Partition for On-Device ML](../papers/zhang-2024-tee-shielded.md) — named among the cryptographic protections too heavy for mobile inference, motivating TEE partitioning instead.
- [PAL\*M: Property Attestation for Large Generative Models](../papers/chantasantitam-2026-palm.md) — cites secure computation for distributional property attestation and accountable audits as the interaction-heavy cryptographic alternative to its hardware-assisted attestation.

## Variants and traps

- Semi-honest security assumes the corrupted party follows the protocol; it does
  not protect against a party that deviates. Upgrading to malicious security
  generally costs more.
- "Non-interactive" is a property of the whole protocol, not of a primitive:
  MPC is interactive by construction, while a scheme built only on homomorphic
  encryption can be non-interactive.

## See also

- [Homomorphic encryption](homomorphic-encryption.md)
- [Secure inference](secure-inference.md)
