---
title: "Hardware virtualization"
type: concept
description: "Hypervisors and the Arm virtualization extensions (the EL2 hypervisor level, two-stage address translation, the IOMMU) that give each virtual machine an isolated view of memory and devices; the substrate beneath virtualization-based TEEs, which turn a virtual machine into an enclave isolated by a small trusted hypervisor."
tags:
  - hardware-security
  - trusted-execution-environment
---

[Home page](../README.md)

# Hardware virtualization

## Definition

Hardware virtualization runs several operating systems on one machine, each in a
virtual machine (VM) that believes it owns the hardware, under a hypervisor that
arbitrates the real resources. Processors expose it through a dedicated, more
privileged mode and a second stage of address translation: the guest OS
translates virtual addresses to what it thinks are physical addresses, and the
hypervisor's stage-two tables translate those into the actual physical
addresses, so each VM sees only the memory the hypervisor grants it. The
classical conditions a processor must meet for this to be efficient and safe
were stated by Popek and Goldberg (1974). On Arm the hypervisor runs at
exception level EL2, beneath the EL3 firmware, and an IOMMU (called the SMMU on
Arm) applies the same address-translation control to DMA-capable peripherals so
a device cannot read memory outside the VM it is assigned to (Dall and Nieh,
2014).

A virtualization-based trusted execution environment reuses this machinery for
isolation rather than multiplexing. A small, trusted hypervisor makes one VM an
enclave whose memory and devices are walled off from a larger, untrusted
hypervisor and the host OS that run alongside it. Because the isolation is
enforced at EL2 through stage-two translation and the IOMMU, an enclave can be
built without changing the most privileged firmware at EL3, and the enclave can
run a stock OS and stock device drivers. This is the alternative substrate to a
[trusted execution environment](trusted-execution-environment.md) built on a
two-world split such as Arm TrustZone.

## Papers that use this concept

- [ASGARD: Protecting On-Device Deep Neural Networks with Virtualization-Based Trusted Execution Environments](../papers/moon-2025-asgard.md) — builds on-device model protection on a virtualization-based TEE, extending a VM enclave over an integrated accelerator through secure I/O passthrough so isolation is enforced at the hypervisor level without touching the EL3 secure monitor.
- [PAL\*M: Property Attestation for Large Generative Models](../papers/chantasantitam-2026-palm.md) — runs operations inside a confidential virtual machine (Intel TDX), a TEE that places an entire VM behind the isolation built on hardware virtualization.

## See also

- [Trusted execution environment](trusted-execution-environment.md)
- [Model partitioning across a TEE and an accelerator](model-partitioning.md)

[Home page](../README.md)

## References

- Dall, C. and Nieh, J. "KVM/ARM: The Design and Implementation of the Linux ARM Hypervisor." International Conference on Architectural Support for Programming Languages and Operating Systems (ASPLOS), 2014.
- Popek, G. J. and Goldberg, R. P. "Formal Requirements for Virtualizable Third Generation Architectures." Communications of the ACM, vol. 17, no. 7, pp. 412-421, 1974.
