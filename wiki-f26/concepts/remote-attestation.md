---
title: "Remote attestation"
type: concept
description: "A hardware root of trust signs a measurement (a quote) of the code and data that ran, which a remote verifier checks against the hardware vendor and, for property-based attestation, against reference values from a trusted authority; remote attestation, the root of trust, and ML property cards (model card, datasheet, inference card)."
tags:
  - trusted-execution-environment
  - hardware-security
---

### [Wiki Home](../README.md)

# Remote attestation

## Definition

Remote attestation is a protocol in which a prover convinces a remote verifier
that it is running expected code on genuine hardware. A hardware *root of trust*,
a component the verifier trusts by assumption because a key was embedded in the
silicon at manufacture, signs a *measurement*: a hash of the code and
configuration that was loaded. The verifier checks the signature against the
hardware vendor's certificate, confirming the report came from authentic
hardware, and compares the measurement to the value it expects. A
[trusted execution environment](trusted-execution-environment.md) supplies this
naturally, since it already holds a hardware-protected key and can measure the
program loaded into an enclave; the signed report is often called a quote. The
guarantee is narrow. Attestation certifies which code loaded and that the
hardware is real; it says nothing about whether that code is free of run-time
bugs once it executes (De Oliveira Nunes et al., 2024).

Property-based attestation generalizes the goal. Rather than certify one exact
configuration, the verifier wants to know that a configuration has a *property*.
The verifier obtains the signed measurement from the prover and reference values
for the property from a trusted authority, and concludes the property holds if
the measurement matches a reference value (Sadeghi and Stüble, 2004). This is the
one structural difference from standard remote attestation: the verifier consults
an external authority for reference values instead of recomputing the expected
measurement itself. Applied to machine learning, a measurer hashes the inputs and
outputs of an operation such as training, evaluation, or inference, and the
resulting attestations populate verifiable *property cards*, the model card,
datasheet, and inference card a third party can check rather than take on faith.

## Papers that use this concept

- [PAL\*M: Property Attestation for Large Generative Models](../papers/chantasantitam-2026-palm.md) — the central mechanism: a confidential virtual machine and a TEE-aware GPU jointly measure an ML operation, and a hardware-signed quote attests properties of large generative models to a verifier who consults a trusted authority for reference values.

## Variants and traps

- Standard remote attestation certifies a fixed configuration; property-based
  attestation certifies a property, and for that the verifier must obtain
  reference values from a trusted authority rather than recompute them.
- Attestation binds what code loaded, not that the loaded code is correct. A
  measured program can still contain a vulnerability exploited at run time.

## See also

- [Trusted execution environment](trusted-execution-environment.md)
- [Zero-knowledge proof](zero-knowledge-proof.md)

### [Wiki Home](../README.md)

## References

- De Oliveira Nunes, I., et al. "Toward Remotely Verifiable Software Integrity in Resource-Constrained IoT Devices." IEEE Communications Magazine, 62(7):58-64, 2024.
- Sadeghi, A.-R. and Stüble, C. "Property-Based Attestation for Computing Platforms: Caring About Properties, Not Mechanisms." Workshop on New Security Paradigms (NSPW), 2004.
