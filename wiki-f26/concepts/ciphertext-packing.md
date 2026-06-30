---
title: "Ciphertext packing (SIMD batching)"
type: concept
description: "Encoding many plaintext values into the independent slots of a single homomorphic ciphertext so one homomorphic add or multiply operates on all of them at once; SIMD / batched HE, slot rotations, and the amortization and communication savings it buys."
tags:
  - homomorphic-encryption
  - cryptography
---

## [Wiki Home](../README.md)

# Ciphertext packing (SIMD batching)

## Definition

Ciphertext packing, also called SIMD batching, encodes a vector of plaintext
values into the independent "slots" of a single
[homomorphic](homomorphic-encryption.md) ciphertext, so that one homomorphic
addition or multiplication applies element-wise to the whole vector at once
(single instruction, multiple data). For a ring of degree N', a CKKS-family
ciphertext exposes on the order of N'/2 slots; the encoding maps a vector to
those slots and is invertible (Cheon et al., 2017). Slot-wise add and multiply
cost the same as a single unpacked operation, but values in different slots
cannot be combined without a rotation, a key-switching operation that cyclically
shifts the slots. Algorithms that must mix slots, such as inner sums, maxima, and
matrix products, are therefore written as sequences of rotations and slot-wise
operations.

Packing is the main lever for both throughput and communication in HE-based
systems: batching b values into one ciphertext divides the per-value amortized
compute and ciphertext bandwidth by up to b. How a matrix or activation map is
laid out across slots, and how many slots stay used rather than wasted, often
decides a protocol's cost. The same slot structure underlies ciphertext
compression, sending one densely packed ciphertext in place of many sparsely
filled ones.

## Papers that use this concept

- [Secure Transformer Inference Made Non-interactive](../papers/zhang-2025-nexus.md) — introduces SIMD ciphertext compression / decompression and slot folding to keep ciphertext slots fully used during homomorphic matrix multiplication and argmax.

## See also

- [Homomorphic encryption](homomorphic-encryption.md)
- [Secure inference](secure-inference.md)

## References

- Cheon, J. H., Kim, A., Kim, M., and Song, Y. "Homomorphic Encryption for
  Arithmetic of Approximate Numbers." ASIACRYPT, 2017.
