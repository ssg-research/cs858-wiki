---
title: "Side-channel attack"
type: concept
description: "Learning a secret from how a computation behaves rather than from what it outputs: timing, cache state, memory-access patterns, power draw, and the traces speculative execution leaves behind; the attack class that trusted-execution guarantees most often place out of scope."
tags:
  - security
  - hardware
  - threat-model
---

## [Wiki Home](../README.md)

# Side-channel attack

## Definition

A side-channel attack recovers a secret from a system's observable behavior
rather than from its specified outputs. The computation is correct and reveals
nothing it was designed to reveal; what leaks is how long it took, which cache
lines it touched, which memory addresses it requested, how much power it drew, or
what it emitted electromagnetically. The channel exists whenever a secret
influences one of those quantities, which happens as soon as control flow or
memory addressing depends on secret data.

Transient-execution attacks extended the class. A processor speculates past a
branch, performs work it later discards, and the discarded work still leaves
micro-architectural traces an attacker can measure, which is enough to read
memory the program was never permitted to read (Kocher et al., 2019; Lipp et al.,
2020). Enclave-targeted variants of the same idea extracted keys from Intel SGX
(Van Bulck et al., 2018).

The reason the class is unavoidable in this course is that a
[trusted execution environment](trusted-execution-environment.md) isolates an
enclave's *architectural* state, and side channels operate beneath that boundary,
on the shared caches, predictors, and timing that isolation does not partition.
Nearly every hardware-defense paper therefore has one sentence fixing its
position: side channels are addressed, or they are declared out of scope. That
sentence is the difference between a guarantee against a malicious operating
system and a guarantee against an attacker who also owns the hardware's timing
behavior. Defenses that do engage the class make the observable behavior
independent of the secret, through constant-time code, data-oblivious execution,
or oblivious memory access.

## Papers that use this concept

- [BliMe: Verifiably Secure Outsourced Computation with Hardware-Enforced Taint Tracking](../papers/elatali-2024-blime.md) — takes side channels inside its threat model rather than out, and enforces at the hardware level that tainted data cannot reach any observable output.
- [ASGARD: Protecting On-Device Deep Neural Networks with Virtualization-Based Trusted Execution Environments](../papers/moon-2025-asgard.md) — places physical attacks and side channels out of scope, scoping its claim to a software adversary.
- [No Privacy Left Outside: On the (In-)Security of TEE-Shielded DNN Partition for On-Device ML](../papers/zhang-2024-tee-shielded.md) — excludes side channels against the TEE, so its attacks work from what the untrusted side legitimately holds.
- [PAL*M: Property Attestation for Large Generative Models](../papers/chantasantitam-2026-palm.md) — excludes them from what an attestation quote covers, while noting that enclave boundaries have been crossed through single-stepping and cache channels.
- [ModelGuard: Information-Theoretic Defense Against Model Extraction Attacks](../papers/tang-2024-modelguard.md) — grants its adversary the returned confidence vector and no side channel, which is what makes the leakage it bounds the only leakage.

## Variants and traps

- "Out of scope" is a scoping decision, not a claim that the channel is absent. A
  defense with side channels excluded is a defense against a different adversary
  than the one who has physical access to the device.
- Encryption does not close the channel. A secret can drive timing or memory
  addressing while remaining encrypted at rest and in transit, which is why
  oblivious execution is a separate requirement from confidentiality.
- The channels differ sharply in what they require. A remote timing measurement
  needs only network access; a power analysis needs the device on a bench. Naming
  the specific channel is what makes a threat model checkable.

## See also

- [Trusted execution environment](trusted-execution-environment.md)
- [Taint tracking](taint-tracking.md)
- [Remote attestation](remote-attestation.md)
- [Hardware virtualization](hardware-virtualization.md)

## References

- Kocher, P., Horn, J., Fogh, A., Genkin, D., Gruss, D., Haas, W., Hamburg, M.,
  Lipp, M., Mangard, S., Prescher, T., Schwarz, M., and Yarom, Y. "Spectre
  Attacks: Exploiting Speculative Execution." IEEE Symposium on Security and
  Privacy (S&P), 2019.
- Lipp, M., Schwarz, M., Gruss, D., Prescher, T., Haas, W., Horn, J., Mangard, S.,
  Kocher, P., Genkin, D., Yarom, Y., Hamburg, M., and Strackx, R. "Meltdown:
  Reading Kernel Memory from User Space." Communications of the ACM, 2020.
- Van Bulck, J., Minkin, M., Weisse, O., Genkin, D., Kasikci, B., Piessens, F.,
  Silberstein, M., Wenisch, T. F., Yarom, Y., and Strackx, R. "Foreshadow:
  Extracting the Keys to the Intel SGX Kingdom with Transient Out-of-Order
  Execution." USENIX Security Symposium, 2018.
