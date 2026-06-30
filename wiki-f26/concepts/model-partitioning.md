---
title: "Model partitioning across a TEE and an accelerator"
type: concept
description: "Splitting a deep neural network's layers or weights between a trusted execution environment and an untrusted accelerator (GPU), shielding a privacy-sensitive subset in the TEE while offloading the rest in the clear for speed; on-device TEE-Shielded DNN Partition (TSDP), the offloading-for-latency motivation, and the security-versus-utility trade-off of how much to shield."
tags:
  - trusted-execution-environment
  - hardware-security
  - privacy
  - machine-learning
---

## [Wiki Home](../README.md)

# Model partitioning across a TEE and an accelerator

## Definition

Model partitioning runs one neural network across two execution contexts of
different trust: a [trusted execution environment](trusted-execution-environment.md)
(TEE), whose contents are shielded from the rest of the device, and an untrusted
accelerator such as a GPU. A privacy-sensitive subset of the model runs inside
the TEE; the rest is offloaded to the accelerator and executes in the clear.
"Offload" here means moving computation to fast but untrusted hardware, the
opposite of the usual sense where work moves to a protected coprocessor. The
motivation is speed: a TEE runs DNN inference far slower than a GPU, so shielding
an entire model can cost an order of magnitude or more in latency, and
partitioning trades some of that protection back for performance.

A partition is defined by which part of the network is shielded. Schemes split by
layer position (shallow, deep, or intermediate layers), by weight magnitude
(the largest-magnitude weights of each layer), or by operation type (the
non-linear layers, with the offloaded linear layers obfuscated). On user devices
the setting is called TEE-Shielded DNN Partition (TSDP), and the threat is the
device owner, who has white-box access to whatever runs outside the TEE; the
asset is the model and the training-data privacy its weights carry. This differs
from the cloud-outsourcing use of the same hardware, where the server is untrusted
and the asset is the client's input. Every partition faces one trade-off: a larger
shielded share raises security and lowers utility (latency, sometimes accuracy),
and the configuration that best balances the two is what a TSDP design must find.

## Papers that use this concept

- [No Privacy Left Outside: On the (In-)Security of TEE-Shielded DNN Partition for On-Device ML](../papers/zhang-2024-tee-shielded.md) — systematizes the TSDP design space into five partition strategies, measures the privacy each offloaded part leaks, and proposes a partition-before-training alternative.
- [ASGARD: Protecting On-Device Deep Neural Networks with Virtualization-Based Trusted Execution Environments](../papers/moon-2025-asgard.md) — sets its whole-model-in-enclave design against the partition-and-offload line, which offloads part of the model to the untrusted accelerator and is the prior work it improves on.

## See also

- [Trusted execution environment](trusted-execution-environment.md)
- [Secure inference](secure-inference.md)
- [Model extraction](model-extraction.md)
