---
title: "Zero-knowledge proof"
type: concept
description: "A proof that a computation on a secret witness was performed correctly while revealing nothing about the witness; prover and verifier, completeness / soundness / zero-knowledge, interactive vs non-interactive (Fiat-Shamir), succinct proofs / zk-SNARKs, and the arithmetic-circuit model that forces machine-learning inputs to be quantized."
tags:
  - cryptography
  - zero-knowledge-proof
---

# Zero-knowledge proof

## Definition

A zero-knowledge proof lets one party, the prover, convince another, the
verifier, that a statement is true while revealing nothing beyond its truth. The
standard statement is membership in an NP language: the prover holds a secret
witness w and establishes that a public predicate holds for a public input x and
w, for example that y = f(x, w) for a public function f, without disclosing w.
The notion originates with Goldwasser, Micali, and Rackoff (1985), who measured
the knowledge a proof leaks about the witness.

Three properties define a proof system. Completeness: an honest prover holding a
valid witness convinces an honest verifier. Soundness: a prover without a valid
witness fails to convince except with negligible probability, so soundness holds
even against a prover that deviates arbitrarily. Zero-knowledge: the verifier
learns nothing about w beyond the statement's truth, formalized by a simulator
that reproduces the verifier's view without access to w. Keeping soundness but
dropping zero-knowledge leaves verifiable computation, a proof that an output is
correct when there is no secret to hide.

Classic proof systems are interactive, with prover and verifier exchanging rounds
of challenge and response. The Fiat-Shamir transform (1986) collapses a
public-coin interactive protocol into a single non-interactive proof by deriving
each verifier challenge from a hash of the transcript, so the prover publishes one
string that anyone verifies offline. A succinct proof is far smaller than the
computation it certifies and checks far faster than re-executing it; the common
packaging is a zk-SNARK, a zero-knowledge Succinct Non-interactive ARgument of
Knowledge.

To prove a statement about a computation, the computation is first written as an
arithmetic circuit over a finite field, a graph of addition and multiplication
gates, and the proof certifies that a consistent assignment of wire values
exists. Interactive-proof protocols such as sumcheck and GKR prove such circuits
efficiently, and lookup arguments certify relations that are awkward to express in
gates. The circuit model offers only field addition and multiplication, so
applying it to machine learning requires quantizing real-valued weights and
activations to field elements, and the non-arithmetic operations of a network,
comparison, division, square root, and exponentiation, become the costly part to
prove.

## Papers that use this concept

- [zkGPT: An Efficient Non-interactive Zero-knowledge Proof Framework for LLM Inference](../papers/qu-2025-zkgpt.md) — proves that a committed language model produced a claimed output on a given input, with the model weights as the hidden witness, by reducing a quantized transformer circuit to arithmetic and lookup relations.
- [PAL\*M: Property Attestation for Large Generative Models](../papers/chantasantitam-2026-palm.md) — positions zero-knowledge proofs of training and inference as the cryptographic alternative to its hardware root of trust for the same regulatory-compliance goal.

## See also

- [Cryptographic commitment](cryptographic-commitment.md)
- [Secure inference](secure-inference.md)
- [Secure multiparty computation](secure-multiparty-computation.md)

## References

- Fiat, A., and Shamir, A. "How to Prove Yourself: Practical Solutions to Identification and Signature Problems." Conference on the Theory and Application of Cryptographic Techniques (CRYPTO), 1986.
- Goldwasser, S., Micali, S., and Rackoff, C. "The Knowledge Complexity of Interactive Proof-Systems." ACM Symposium on Theory of Computing (STOC), 1985.
