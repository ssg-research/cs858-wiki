---
title: "Pseudorandom function"
type: concept
description: "A keyed function whose outputs are computationally indistinguishable from random to anyone without the key; reproducible with the key, unpredictable without it, instantiated by block ciphers (AES) or keyed cryptographic hashes (SHA-3)."
tags:
  - cryptography
---

# Pseudorandom function

## Definition

A pseudorandom function (PRF) is a keyed function `F_K` whose outputs are
computationally indistinguishable from those of a truly random function to anyone
who does not know the key `K`. Given the key, the outputs are deterministic and
reproducible; without it, they are unpredictable and appear random. Standard
cryptographic building blocks serve as PRFs in practice: block ciphers such as
AES, and cryptographic hash functions such as SHA-3 used in keyed form.

A PRF lets one party derive reproducible pseudorandom choices from an input
(seeding a draw, selecting a subset of a set) that an adversary cannot predict or
reproduce without the secret key. This separates the ability to *generate* a
keyed pseudorandom structure from the ability to *verify* it: a party holding the
key can recompute the structure, while a party without it cannot.

## Papers that use this concept

- [A Watermark for Large Language Models](../papers/kirchenbauer-2023-watermark.md) — the private watermark seeds the green/red-list partition with a PRF keyed by a secret, so a detector with the key can reproduce the partition while an adversary without it cannot tell which tokens are green.

## See also

- [Cryptographic commitment](cryptographic-commitment.md)
