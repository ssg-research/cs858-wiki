---
title: "ASGARD: Protecting On-Device Deep Neural Networks with Virtualization-Based Trusted Execution Environments"
authors:
  - Moon, Myungsuk
  - Kim, Minhee
  - Jung, Joonkyo
  - Song, Dokyung
year: 2025
section: "Model Theft Resistance (+ On-Device Private Inference): Hardware"
primary: true
doi: "10.14722/ndss.2025.240449"
tags:
  - trusted-execution-environment
  - hardware-security
  - model-extraction
  - privacy
  - defense
---

---

### [Wiki Home](../README.md)

---

# ASGARD: Protecting On-Device Deep Neural Networks with Virtualization-Based Trusted Execution Environments

## High-level overview

On-device deep learning runs [DNN](../concepts/convolutional-neural-network.md)
inference on a user's phone or IoT device, keeping sensitive inputs such as faces
and fingerprints off remote servers. The same shift hands the device the model
itself, where an adversary who controls the rich execution environment (REE), the
device's untrusted software stack, can read or dump the model's weights during
inference. Prior protections host inference inside a
[trusted execution environment](../concepts/trusted-execution-environment.md)
(TEE) built on Arm TrustZone, the hardware-isolated secure world of a mobile SoC,
but they hit two walls. Keeping the whole model in the TEE either runs on the CPU
only, losing the device's accelerator, or must port proprietary accelerator
software into TrustZone's specialized secure-world OS. Offloading part of
inference to the REE to use its accelerator either leaves that part unprotected
or pays heavy run-time cost obfuscating it across the secure boundary (see
[model partitioning](../concepts/model-partitioning.md)).

ASGARD is the first virtualization-based TEE for on-device DNN protection on
legacy Armv8-A SoCs. A virtualization-based TEE realizes an enclave as a virtual
machine isolated by a small trusted hypervisor (see
[hardware virtualization](../concepts/hardware-virtualization.md)), in place of
TrustZone's two-world split. ASGARD extends such an enclave to hold the entire
model together with an SoC-integrated accelerator, a neural processing unit
(NPU), through secure I/O passthrough, so inference runs fully accelerated inside
the enclave while keeping the trusted computing base (TCB) small: the isolation
monitor sits at the hypervisor exception level (EL2) and leaves the proprietary
EL3 secure monitor and the vendor accelerator driver stack unmodified. On a
commodity Android board (Rockchip RK3588S) with no changes to Rockchip- or
Arm-proprietary software, ASGARD adds roughly two thousand lines to the
hypervisor, ships an enclave image of about 17 MB, and reaches DNN inference
latency on par with or below unprotected accelerated inference, in one case
slightly faster, by coalescing accelerator interrupts that would otherwise force
costly exits out of the enclave.

**Threat Model:** Three parties take part. A remote model provider ships a model
it wants to protect; an REE-side privileged adversary on the device aims to steal
it; and a trusted DNN-serving enclave runs on ASGARD-extended platform software.
The adversary fully controls the REE, down to the unprivileged hypervisor that
manages resources, and seeks to read or dump the model's weights and architecture
while it is in use for inference. Trusted are the small privileged hypervisor at
EL2 that enforces isolation between domains, the EL3 secure monitor, and the
secure world, which on Armv8-A can access the normal world regardless. The
protected asset is the model, kept confidential in transit, at rest, and in use;
the accelerator sits behind an IOMMU and exposes a reset interface. The
defender's claim is software-secure enclaves against REE-side software
adversaries on commodity Armv8-A hardware. Physical attacks and side channels are
out of scope. The paper notes the guarantee can be strengthened to
hardware-secure enclaves where additional hardware support, such as Arm's
Confidential Compute Architecture, is available.

## Why read this

<!-- instructor: confirm -->

ASGARD is the first system to build on-device model protection on a
virtualization-based TEE rather than Arm TrustZone, and it carries the idea to a
working prototype on a commodity Android SoC without modifying any proprietary
firmware or accelerator driver. It shows that an enclave can be extended over an
integrated NPU by secure I/O passthrough while keeping the trusted computing base
small and run-time overhead near zero. The paper is a concrete study in trading
TrustZone's static two-world partition for hypervisor-enforced VM isolation, and
in the systems engineering that makes a TEE both accelerator-capable and
compatible with closed-source software.

## Basic Background

### On-device deep learning and model confidentiality

On-device DNN inference runs the model on the end user's hardware, which exposes
the model file to the device. The on-device models are typically compact
[convolutional networks](../concepts/convolutional-neural-network.md) and small
transformers, the object-detection and text-understanding backbones used on
mobile NPUs. The direct threat is
[model extraction](../concepts/model-extraction.md): reproducing a model's
weights, architecture, or functionality from external access, which on a device
can be as crude as dumping the model from memory during inference. A stolen model
is also a privacy exposure, since its behavior reveals which records were in its
training set ([membership inference](../concepts/membership-inference.md))
(Shokri et al., 2017) and large models can emit training examples verbatim
([Carlini et al., 2021](carlini-2021-extracting-training-data.md)).

### Trusted execution environments and Arm TrustZone

A [trusted execution environment](../concepts/trusted-execution-environment.md)
(TEE) isolates code and data from the rest of the system, including a malicious
OS, and attests what code loaded. Arm TrustZone, the commodity TEE on mobile
SoCs, splits the processor into a normal world and a secure world with physical
resources statically partitioned between them, and places security-critical
services in the secure world (Arm Limited, 2021). Everything outside the secure
world, the ordinary OS, applications, and accelerators, is the rich execution
environment (REE), and on a user's device it is what the adversary controls. The
trusted computing base (TCB) is the set of hardware and software whose
correctness the protection assumes; a smaller TCB is a smaller attack surface.

### Hardware virtualization and VM-based enclaves

[Hardware virtualization](../concepts/hardware-virtualization.md) lets a
hypervisor give each virtual machine its own view of physical memory through a
second stage of address translation, and isolates DMA-capable peripherals behind
an IOMMU. A virtualization-based TEE uses a small, trusted hypervisor to turn one
virtual machine into an enclave, isolated from a larger untrusted hypervisor and
the host OS. On Arm this isolation is enforced at the hypervisor exception level
(EL2), beneath the EL3 secure monitor, so an enclave can be built without
modifying the most privileged firmware and can run a stock OS with stock drivers.

### Partitioning a model across a TEE and an accelerator

A TEE runs a DNN far slower than a dedicated accelerator, so one line of
on-device protection partitions the network
(see [model partitioning](../concepts/model-partitioning.md)): a
privacy-sensitive subset runs in the enclave while the rest is offloaded to the
device's untrusted accelerator, in the clear or under obfuscation, for speed. The
split trades protection for latency, and the offloaded part is the side an
adversary can read.

## Reading guidance

- Section II.A and Figure 1: the Arm primitives the design rests on, the four
  exception levels EL0 to EL3 and the two-stage address translation, the
  vocabulary the rest of the paper assumes.
- Section II.B: virtualization-based TEEs and the concrete protected-KVM design,
  with the privileged hypervisor at EL2, the unprivileged host-side hypervisor,
  page-frame ownership, and IOMMU isolation of peripherals.
- Section II.C and Table I: the efficiency (P1) and compatibility (P2)
  limitations of prior TrustZone-based solutions, each prior system scored
  against both. Attention anchor: read which column each prior system fails and
  why, since the design goals are set directly against this table.
- Section III.A and III.B, Figure 2: the three design goals (G1 to G3) and the
  threat model. Attention anchor: note exactly what the threat model trusts (the
  privileged hypervisor, the EL3 secure monitor, the secure world) and what it
  excludes (physical attacks, side channels), and that the guarantee is stated as
  software-secure.
- Section IV: the secure I/O passthrough design, and what has to move into the
  privileged hypervisor, namely the IOMMU driver and the accelerator reset
  control.
- Section V: the platform- and application-level TCB debloating, the techniques
  that hold the enclave image and the hypervisor additions small.
- Section VI, Table III and Figures 5 and 8: the security analysis and the
  TCB-size and latency measurements, including the comparison against an
  REE-offloading baseline.
- Section VII: scope and limits, including model extraction through side
  channels, porting to other SoCs, and compatibility with Arm's Confidential
  Compute Architecture.
- Section VIII: the related-work map, separating TrustZone peripheral extension,
  hardware GPU TEEs, and accelerator I/O virtualization.

<details>
<summary><h2>Supplementary readings</h2></summary>

- [ShadowNet: A Secure and Efficient On-device Model Inference System for Convolutional Neural Networks](https://arxiv.org/abs/2011.05905) — a TrustZone-based on-device protection that offloads transformed weights to the untrusted accelerator, a point of contrast with the virtualization-based design.

</details>

<details>
<summary><h2>Paper Context</h2></summary>

On-device model protection grew up on Arm TrustZone, hosting inference in the
secure world (Arm Limited, 2021). Two design lines emerged, each constrained by
TrustZone's static partition of resources. One offloads part of inference to a
normal-world accelerator: DarkneTZ runs a model's early layers on the untrusted
accelerator and keeps the deeper layers in the enclave (Mo et al., 2020); Slalom
established the TEE-plus-accelerator split, offloading the heavy linear algebra to
untrusted hardware under verification and blinding (Tramèr and Boneh, 2019);
ShadowNet offloads linear layers after transforming their weights (Sun et al.,
2023); and SOTER guards black-box inference for general networks at the edge
(Shen et al., 2022). The other line keeps the accelerator inside the TEE by
statically assigning it to the secure world, which preserves acceleration but
breaks compatibility or enlarges the TCB: GPUReplay ports a tiny replay-only GPU
stack into the secure world and supports only previously recorded tasks (Park and
Lin, 2022), and StrongBox builds a GPU TEE on Arm by modifying the EL3 secure
monitor and the kernel driver (Deng et al., 2022).

The offloading line carries a leakage problem. Offloading part of a model leaves
that part exposed, and obfuscating it costs run-time overhead in repeated secure
boundary crossings. A systematic study of TEE-shielded DNN partition schemes
measured that the offloaded part leaks near-white-box model and training-data
information, so partitioning does not deliver the protection of shielding the
whole model
([Zhang et al., 2024](zhang-2024-tee-shielded.md)). Independent of any specific
scheme, large-scale measurements found that most on-device models deployed in
mobile apps carry no effective protection and can be dumped or reused directly
(Sun et al., 2021; Ren et al., 2024).

A newer substrate sidesteps TrustZone's static two-world split. Virtualization-
based TEEs build enclaves as virtual machines isolated by a small trusted
hypervisor (Mirzamohammadi and Sani, 2018; Li et al., 2021), an approach now
shipping as protected KVM on Android (Deacon, 2020). Arm's Confidential Compute
Architecture promises hardware-isolated VM enclaves on a future Armv9-A
generation (Arm Limited, 2023), and has been used for attestable, private
on-device ML (Siby et al., 2024). No Confidential Compute Architecture hardware
ships yet, leaving the widespread base of legacy Armv8-A devices without it. These
virtualization-based TEEs provide enclaves for CPU workloads; on existing
Armv8-A hardware they do not pass an SoC-integrated accelerator through to an
enclave.

</details>

---

### [Wiki Home](../README.md)

<details>
<summary><h4>References</h4></summary>

Entries read off this paper's bibliography (PDF pages 14-16).

- Arm Limited. "Learn the Architecture - TrustZone for AArch64 (version 1.1)." 2021.
- Arm Limited. "Introducing Arm Confidential Compute Architecture (version 3.0)." 2023.
- Carlini, N., Tramèr, F., Wallace, E., Jagielski, M., Herbert-Voss, A., Lee, K., Roberts, A., Brown, T., Song, D., Erlingsson, U., Oprea, A., and Raffel, C. "Extracting Training Data from Large Language Models." USENIX Security Symposium, 2021.
- Deacon, W. "Virtualization for the Masses: Exposing KVM on Android." KVM Forum, 2020.
- Deng, Y., Wang, C., Yu, S., Liu, S., Ning, Z., Leach, K., Li, J., Yan, S., He, Z., Cao, J., and Zhang, F. "StrongBox: A GPU TEE on Arm Endpoints." ACM SIGSAC Conference on Computer and Communications Security (CCS), 2022.
- Li, D., Mi, Z., Xia, Y., Zang, B., Chen, H., and Guan, H. "TwinVisor: Hardware-Isolated Confidential Virtual Machines for ARM." ACM Symposium on Operating Systems Principles (SOSP), 2021.
- Mirzamohammadi, S. and Sani, A. A. "The Case for a Virtualization-Based Trusted Execution Environment in Mobile Devices." Asia-Pacific Workshop on Systems (APSys), 2018.
- Mo, F., Shamsabadi, A. S., Katevas, K., Demetriou, S., Leontiadis, I., Cavallaro, A., and Haddadi, H. "DarkneTZ: Towards Model Privacy at the Edge Using Trusted Execution Environments." ACM International Conference on Mobile Systems, Applications, and Services (MobiSys), 2020.
- Park, H. and Lin, F. X. "GPUReplay: A 50-KB GPU Stack for Client ML." International Conference on Architectural Support for Programming Languages and Operating Systems (ASPLOS), 2022.
- Ren, P., Zuo, C., Liu, X., Diao, W., Zhao, Q., and Guo, S. "DEMISTIFY: Identifying On-Device Machine Learning Models Stealing and Reuse Vulnerabilities in Mobile Apps." International Conference on Software Engineering (ICSE), 2024.
- Shen, T., Qi, J., Jiang, J., Wang, X., Wen, S., Chen, X., Zhao, S., Wang, S., Chen, L., Luo, X., Zhang, F., and Cui, H. "SOTER: Guarding Black-Box Inference for General Neural Networks at the Edge." USENIX Annual Technical Conference (ATC), 2022.
- Shokri, R., Stronati, M., Song, C., and Shmatikov, V. "Membership Inference Attacks Against Machine Learning Models." IEEE Symposium on Security and Privacy (S&P), 2017.
- Siby, S., Abdollahi, S., Maheri, M., Kogias, M., and Haddadi, H. "GuaranTEE: Towards Attestable and Private ML with CCA." Workshop on Machine Learning and Systems (EuroMLSys), 2024.
- Sun, Z., Sun, R., Lu, L., and Mislove, A. "Mind Your Weight(s): A Large-Scale Study on Insufficient Machine Learning Model Protection in Mobile Apps." USENIX Security Symposium, 2021.
- Sun, Z., Sun, R., Liu, C., Chowdhury, A. R., Lu, L., and Jha, S. "ShadowNet: A Secure and Efficient On-Device Model Inference System for Convolutional Neural Networks." IEEE Symposium on Security and Privacy (S&P), 2023.
- Tramèr, F. and Boneh, D. "Slalom: Fast, Verifiable and Private Execution of Neural Networks in Trusted Hardware." International Conference on Learning Representations (ICLR), 2019.
- Zhang, Z., Gong, C., Cai, Y., Yuan, Y., Liu, B., Li, D., Guo, Y., and Chen, X. "No Privacy Left Outside: On the (In-)Security of TEE-Shielded DNN Partition for On-Device ML." IEEE Symposium on Security and Privacy (S&P), 2024.

</details>
