---
title: "Homomorphic encryption"
type: concept
description: "Encryption that supports computation directly on ciphertexts, so a function evaluated on encrypted inputs decrypts to the function of the plaintexts; partially / leveled / fully homomorphic, the bootstrapping that refreshes ciphertext noise, and the CKKS scheme for approximate real-number arithmetic."
tags:
  - homomorphic-encryption
  - cryptography
  - privacy
---

### [Wiki Home](../README.md)

# Homomorphic encryption

## Definition

Homomorphic encryption (HE) is public-key encryption whose ciphertexts support
arithmetic: adding or multiplying encrypted values yields a ciphertext that
decrypts to the sum or product of the underlying plaintexts, so a party holding
only ciphertexts can evaluate a function without learning its inputs or its
output. Each homomorphic operation grows a noise term carried inside the
ciphertext, and once that noise crosses a threshold the ciphertext no longer
decrypts correctly. Schemes are graded by how much computation they allow before
that point: partially homomorphic (one operation, unbounded), somewhat or
leveled homomorphic (circuits up to a fixed multiplicative depth), and fully
homomorphic (arbitrary depth). The step from leveled to fully homomorphic is
bootstrapping, which homomorphically evaluates the scheme's own decryption
circuit to turn a noisy ciphertext back into a fresh low-noise one; the first
construction is due to Gentry (2009), and bootstrapping is still the dominant
cost in practice.

The schemes differ in the arithmetic they expose. The integer schemes BGV and
BFV and the fast-bootstrapping boolean family TFHE compute on exact values; CKKS
(Cheon-Kim-Kim-Song) computes on approximate real and complex numbers, treating
a small rounding error like fixed-point noise, which suits machine-learning
workloads whose inputs are already approximate (Cheon et al., 2017). A residue
number system variant, RNS-CKKS, replaces big-integer modular arithmetic with
parallel arithmetic over machine-word primes for speed (Cheon et al., 2018).
CKKS-family ciphertexts pack many values into independent SIMD slots (see
[ciphertext packing](ciphertext-packing.md)). HE lets one party compute on
another's data without interaction, which is the property that separates it from
[secure multiparty computation](secure-multiparty-computation.md), where the
parties jointly compute over several rounds of communication.

## Papers that use this concept

- [Secure Transformer Inference Made Non-interactive](../papers/zhang-2025-nexus.md) — builds non-interactive secure transformer inference on RNS-CKKS, evaluating every layer homomorphically and scheduling bootstrapping to control cost.
- [BliMe: Verifiably Secure Outsourced Computation with Hardware-Enforced Taint Tracking](../papers/elatali-2024-blime.md) — fully homomorphic encryption is the cryptographic baseline whose orders-of-magnitude overhead motivates BliMe's hardware-enforced alternative.
- [No Privacy Left Outside: On the (In-)Security of TEE-Shielded DNN Partition for On-Device ML](../papers/zhang-2024-tee-shielded.md) — named among the cryptographic protections too expensive for on-device inference, motivating the TEE-partition approach instead.

## Variants and traps

- "Fully" homomorphic does not mean fast or free: arbitrary depth is bought with
  bootstrapping, whose cost often dominates the computation.
- Leveled HE fixes a maximum multiplicative depth at key-generation time; a
  deeper circuit needs either larger parameters or bootstrapping.
- CKKS results carry a controlled approximation error, unlike the exact integer
  schemes (BGV, BFV), so it fits numerical ML but not exact integer predicates
  without care.

## See also

- [Secure multiparty computation](secure-multiparty-computation.md)
- [Secure inference](secure-inference.md)
- [Ciphertext packing (SIMD batching)](ciphertext-packing.md)

### [Wiki Home](../README.md)

## References

- Gentry, C. "A Fully Homomorphic Encryption Scheme." PhD thesis, Stanford
  University, 2009.
- Cheon, J. H., Kim, A., Kim, M., and Song, Y. "Homomorphic Encryption for
  Arithmetic of Approximate Numbers." ASIACRYPT, 2017.
- Cheon, J. H., Han, K., Kim, A., Kim, M., and Song, Y. "A Full RNS Variant of
  Approximate Homomorphic Encryption." Selected Areas in Cryptography (SAC),
  2018.
