---
title: "Trusted execution environment"
type: concept
description: "Hardware-isolated execution contexts (enclaves) that run code and hold data so a privileged or malicious OS cannot read or modify them, with remote attestation of the loaded code; Intel SGX, Arm TrustZone, AMD SEV, Sanctum, and their known side-channel and run-time-attack limits."
tags:
  - trusted-execution-environment
  - hardware-security
  - privacy
---

[Home page](../README.md)

# Trusted execution environment

## Definition

A trusted execution environment (TEE) is a hardware-isolated context that runs
code and holds data so that software outside it, including a privileged or
compromised operating system, cannot read or modify them. The hardware enforces
two properties. Isolation keeps an enclave's memory unreadable to other
processes, the OS, and the hypervisor. Remote attestation lets a key embedded in
the hardware at manufacture sign a measurement of the loaded code and
configuration, so a remote client can check that the expected program is running
on genuine hardware before sending it secrets. Commodity implementations include
Intel SGX enclaves (Costan and Devadas, 2016), Arm TrustZone's secure world
(Pinto and Santos, 2019), AMD SEV's encrypted virtual machines, and academic
RISC-V designs such as Sanctum (Costan et al., 2016).

The isolation boundary stops direct access to enclave memory, but not inference
from a program's data-dependent behavior. Cache-timing, branch-prediction, and
transient-execution attacks have repeatedly recovered enclave secrets, among them
Foreshadow against SGX (Van Bulck et al., 2018). Bugs in the code running inside
the enclave are also in scope: an attested program can still contain a
memory-safety vulnerability an attacker exploits at run time. A TEE therefore
moves trust onto the CPU package and the enclave code, and its confidentiality
guarantee is only as strong as that code's resistance to run-time and
side-channel attacks.

## Papers that use this concept

- [BliMe: Verifiably Secure Outsourced Computation with Hardware-Enforced Taint Tracking](../papers/elatali-2024-blime.md) — the enclave isolation model and its side-channel weaknesses are the baseline its hardware taint tracking is set against.
- [No Privacy Left Outside: On the (In-)Security of TEE-Shielded DNN Partition for On-Device ML](../papers/zhang-2024-tee-shielded.md) — shields a subset of an on-device DNN inside the enclave; the paper measures how much the part offloaded outside still leaks.
- [ASGARD: Protecting On-Device Deep Neural Networks with Virtualization-Based Trusted Execution Environments](../papers/moon-2025-asgard.md) — builds on-device model protection on a virtualization-based TEE (a VM enclave) instead of Arm TrustZone, and extends the enclave over an integrated accelerator.
- [PAL\*M: Property Attestation for Large Generative Models](../papers/chantasantitam-2026-palm.md) — runs attested ML operations inside a confidential virtual machine paired with a TEE-aware GPU, and turns the enclave's remote attestation into property attestations for large generative models.

## Variants and traps

- Isolation and attestation are distinct guarantees. Attestation certifies what
  code loaded; it says nothing about whether that code is free of run-time
  vulnerabilities once it runs.
- A TEE protects a region of memory. It does not by itself stop a program from
  leaking the data it is allowed to touch through timing or memory-access
  patterns.

## See also

- [Taint tracking](taint-tracking.md)
- [Secure inference](secure-inference.md)

[Home page](../README.md)

## References

- Costan, V. and Devadas, S. "Intel SGX Explained." Cryptology ePrint Archive,
  Report 2016/086, 2016.
- Costan, V., Lebedev, I., and Devadas, S. "Sanctum: Minimal Hardware Extensions
  for Strong Software Isolation." USENIX Security Symposium, 2016.
- Pinto, S. and Santos, N. "Demystifying Arm TrustZone: A Comprehensive Survey."
  ACM Computing Surveys, 2019.
- Van Bulck, J., Minkin, M., Weisse, O., Genkin, D., Kasikci, B., Piessens, F.,
  Silberstein, M., Wenisch, T. F., Yarom, Y., and Strackx, R. "Foreshadow:
  Extracting the Keys to the Intel SGX Kingdom with Transient Out-of-Order
  Execution." USENIX Security Symposium, 2018.
