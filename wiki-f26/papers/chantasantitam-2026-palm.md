---
title: "PAL*M: Property Attestation for Large Generative Models"
authors:
  - Chantasantitam, Prach
  - Caulfield, Adam Ilyas
  - Duddu, Vasisht
  - Gunn, Lachlan J.
  - Asokan, N.
year: 2026
section: "Regulatory Compliance: Hardware"
primary: true
arxiv: "2601.16199"
tags:
  - trusted-execution-environment
  - hardware-security
  - language-models
  - machine-learning
---

## [Wiki Home](../README.md)

# PAL\*M: Property Attestation for Large Generative Models

**Paper:** [arXiv:2601.16199](https://arxiv.org/abs/2601.16199)

## High-level overview

Emerging regulation, such as the EU AI Act, asks for verifiable evidence that
a deployed model meets stated requirements about its accuracy, training data,
provenance, and inference, even when the dataset and weights stay confidential.
*Property attestation* supplies that evidence: a model provider produces a
hardware-signed statement that some property holds of an operation it ran, and
a verifier, a regulator, auditor, or customer, checks the statement without
re-running the operation or seeing the confidential inputs. It rests on
[remote attestation](../concepts/remote-attestation.md), in which a hardware
*root of trust* signs a measurement of the code and data that ran. PAL\*M is a
property-attestation framework that carries this from small CPU-only
classifiers to large generative models, using large language models as its
illustration.

Earlier hardware-assisted property attestation ran the whole machine-learning
operation inside a single CPU enclave (Duddu et al., 2024). Large generative
models break that arrangement: their training and inference span a CPU and a
GPU, and their datasets are too large to hold in enclave memory, so frameworks
memory-map them and sample records on demand from untrusted storage. PAL\*M
runs operations inside a *confidential virtual machine*, a
[trusted execution environment](../concepts/trusted-execution-environment.md)
holding an entire VM, paired with a TEE-aware GPU so the accelerator's work is
itself measured and attested, and it measures out-of-order dataset reads with
an order-independent hash. On this basis it defines property measurements for a
catalogue of operations from preprocessing through training,
[fine-tuning](../concepts/fine-tuning.md), evaluation, and chat inference. The
output is a verifiable *property card*: a model card, datasheet, or inference
card. The prototype runs on commodity Intel
TDX and an NVIDIA H100, reports under 11% overhead on common operations, and its
attestation protocol is machine-checked in the Tamarin prover. PAL\*M roots
verifiability in trusted hardware, the counterpart to cryptographic schemes that
certify the same properties with a
[zero-knowledge proof](../concepts/zero-knowledge-proof.md) or
[secure computation](../concepts/secure-multiparty-computation.md).

**Threat Model:** A prover, the model provider that trains or serves a model,
attests properties of its operations to a verifier, mediated by an initiator
that requests an operation and forwards the evidence; the verifier may obtain
reference values for a property from a trusted authority such as the hardware
vendor. The adversary is a dishonest prover with the standard Intel TDX powers:
it controls the host, the virtual machine manager, and the disk, so it can read
and tamper with anything outside the trust boundary, including memory-mapped
datasets in external storage, and it is a Dolev-Yao network adversary that can
inject or modify protocol messages. It may try to forge a quote, either by
learning the signing key or by tampering with code and data undetected. The
trusted set is small and named: the Intel TDX module and the TDX-aware CPU,
trusted to be implemented correctly, to isolate the confidential VM from the
host and from other VMs, and to produce a hardware-signed quote over what ran;
and the NVIDIA H100's hardware, trusted to measure its own configuration and
report it honestly. Trust in that sense reaches no further. The confidential VM
is created by the adversary-controlled virtual machine manager, and the GPU is
assigned by that same manager, its interface outside the VM's protection until
the assignment is made, so neither the VM nor the assigned device is assumed to
be in the state it should be. Each is therefore attested rather than trusted:
the VM through its quote, the GPU through an attestation token the VM obtains
and checks before relying on the device. What an attestation carries is a
property of an operation over its inputs and outputs, measured and extended
into the signed quote; the model and the dataset stay confidential and never
enter the quote. Denial of service,
[side-channel attacks](../concepts/side-channel.md) on the hardware, and
physical attacks, including memory-bus interposition and physically swapping
the GPU, are out of scope.

## Basic Background

### Large generative models and their operations

A large language model is a [transformer](../concepts/transformer.md) with
billions of parameters, pretrained to predict the next token and then
adapted to tasks (Vaswani et al., 2017). Adaptation is usually parameter-efficient
[fine-tuning](../concepts/fine-tuning.md), which updates a small subset of weights
or small added modules rather than retraining the whole model, with low-rank
adaptation (LoRA) the common
instance (Hu et al., 2022). Post-training also includes
[quantization](../concepts/quantization.md), which lowers the numerical precision
of weights to shrink memory and compute. Quality is
reported on benchmarks such as MMLU for knowledge and BLEU for translation.
Because the datasets dwarf main memory, training libraries memory-map them,
mapping a file into virtual memory and loading records from disk on demand instead
of holding the whole dataset resident, and they sample records in random order.

### Trusted execution environments and confidential VMs

A [trusted execution environment](../concepts/trusted-execution-environment.md)
(TEE) isolates code and data from the rest of the system, including a privileged
operating system, and offers
[remote attestation](../concepts/remote-attestation.md) of the loaded code. The
early commodity TEEs were user-space enclaves (Intel SGX) or a two-world split
(Arm TrustZone). Confidential virtual machines place an entire VM inside the trust
boundary, so an unmodified operating system runs in the enclave; Intel TDX, AMD
SEV-SNP, and Arm Realms are examples, and the isolation builds on
[hardware virtualization](../concepts/hardware-virtualization.md). PAL\*M assumes
the standard Intel TDX adversary model, in which the host and the virtual machine
manager are untrusted (Aktas et al., 2023). TEE-aware GPUs, such as the NVIDIA
H100 in confidential-computing mode, extend isolation and attestation to the
accelerator, so a CPU enclave and the GPU can form one attested environment.

### Remote attestation and property attestation

In [remote attestation](../concepts/remote-attestation.md) a hardware root of
trust signs a measurement of what code loaded, and a remote verifier checks the
signature and the measurement (De Oliveira Nunes et al., 2024). Property-based
attestation certifies that a configuration has a property rather than a specific
configuration: the verifier compares the signed measurement against reference
values supplied by a trusted authority (Sadeghi and Stüble, 2004). Carried to
machine learning, a measurer hashes the inputs and outputs of an operation, and
the attestations populate verifiable property cards, a model card, a datasheet, or
an inference card.

### Order-independent integrity for sampled data

An incremental multiset hash is a cryptographic primitive that produces a
fixed-size value over an unordered collection and can be updated one element at a
time. Because it is insensitive to insertion order, two runs that read the same
records in different orders produce the same hash, which is what makes it suited to
integrity checking of data sampled out of order from memory or disk (Clarke et al.,
2003).

### Verifiable machine learning without trusted hardware

The cryptographic route to verifiable machine learning removes trust in the
prover's hardware. A [zero-knowledge proof](../concepts/zero-knowledge-proof.md)
certifies that a computation on a secret witness was performed correctly while
revealing nothing else, and
[secure multiparty computation](../concepts/secure-multiparty-computation.md) lets
parties jointly compute over private inputs revealing only the output. A
[cryptographic commitment](../concepts/cryptographic-commitment.md) binds a value,
such as a model, so later proofs refer to one fixed object. These are the
alternative roots of trust against which a hardware-attestation scheme is measured.

## Reading guidance

- Section 3.2, the paragraph on the GPU: the H100's hardware is trusted, the
  device the VMM assigns to the confidential VM is not, and one attestation
  token separates the two. Find the sentence that does the work of bringing the
  GPU inside the trust boundary.
- Section 4.3, the per-operation property measurements: for each operation, what
  the measurement commits to and what it hashes rather than carries. That
  omission is what keeps the model and the dataset confidential.
- Section 6.1.3, Table 6: attesting one inference against attesting a session of
  many. Note what changes between the two and therefore when the framework is
  affordable.

<details>
<summary><h2>Paper Context</h2></summary>

Trusted execution environments are the substrate of confidential computing, and a
large body of work uses them to protect the *confidentiality* of models and data:
DarkneTZ shields on-device DNN inference inside an enclave (Mo et al., 2020), and
TEE-shielded DNN partitioning splits a network between an enclave and a GPU, with a
study showing how much the offloaded part still leaks
([Zhang et al., 2024](zhang-2024-tee-shielded.md)). The isolation boundary has been
crossed repeatedly through side channels, including single-stepping and cache
attacks against Intel TDX (Wilke et al., 2024), and hardware taint tracking has
been proposed to contain such leakage by preventing data-dependent outputs
([El Atali et al., 2024](elatali-2024-blime.md)). These threads concern
confidentiality and the side channels that undermine it.

A separate line attests *properties* rather than protecting confidentiality.
Property-based attestation, certifying that a platform has a property rather than a
fixed configuration, dates to Sadeghi and Stüble (2004), and supply-chain
attestation carried provenance guarantees for software artifacts (Torres-Arias et
al., 2019). Bringing this to machine learning, distributional properties of
training data were attested with secure computation (Duddu et al., 2024), and
Laminator produced verifiable ML property cards by running operations in an SGX
enclave and measuring their inputs and outputs (Duddu et al., 2024).
Contemporaneous systems extend the idea in different directions: Atlas records ML
lifecycle provenance to a transparency log (Spoczynski et al., 2025), ExclaveFL
attests [federated-learning](../concepts/federated-learning.md) rounds with an
integrity-only enclave (Guo et al.,
2024), SLAPP gives stateful proofs of execution for federated learning and
differential privacy on Cortex-M TrustZone (Rattanavipanon and Nunes, 2025), and
attestable audits run AI-safety benchmarks inside a TEE (Schnabl et al., 2025).
This line had targeted CPU-bound or classifier-scale operations.

The cryptographic alternative roots verifiability in mathematics rather than
hardware. Zero-knowledge proofs certify training of simple models (Garg et al.,
2023) and deep networks (Abbaszadeh et al., 2024) and inference of large language
models (Sun et al., 2024), and they have been used to attest security properties
such as [differential privacy](../concepts/differential-privacy.md) (Franzese et
al., 2025) and [fairness](../concepts/group-fairness.md) (Shamsabadi et al., 2023).
Secure multiparty computation has been used for distributional property attestation
(Duddu et al., 2024) and for accountable audits that bind training and inference
through publicly verifiable [commitments](../concepts/cryptographic-commitment.md)
(Lycklama et al., 2024). A different provenance approach, proof-of-learning,
reconstructs the training trajectory but has been shown fragile to forgery (Fang et
al., 2023; Zhang et al., 2022). The recurring obstacle for the cryptographic route
is cost: proving a single iteration of VGG-11 training runs to minutes (Abbaszadeh
et al., 2024).

</details>

<details>
<summary><h2>Essential Readings</h2></summary>

- [Laminator: Verifiable ML Property Cards using Hardware-assisted Attestations](https://arxiv.org/abs/2406.17548) — the hardware-attestation property-card approach this paper extends to large generative models.
- [Sentry: Authenticating Machine Learning Artifacts on the Fly](https://arxiv.org/pdf/2510.00554) — authenticating ML artifacts at use time, an adjacent take on trustworthy provenance.

</details>

<details>
<summary><h4>References</h4></summary>

Entries read off this paper's bibliography (PDF pages 13-14).

- Abbaszadeh, K., et al. "Zero-Knowledge Proofs of Training for Deep Neural Networks." ACM SIGSAC Conference on Computer and Communications Security (CCS), 2024.
- Aktas, E., et al. "Intel Trust Domain Extensions (TDX) Security Review." Google security review, 2023.
- Clarke, D., et al. "Incremental Multiset Hash Functions and Their Application to Memory Integrity Checking." International Conference on the Theory and Application of Cryptology and Information Security (ASIACRYPT), 2003.
- De Oliveira Nunes, I., et al. "Toward Remotely Verifiable Software Integrity in Resource-Constrained IoT Devices." IEEE Communications Magazine, 62(7):58-64, 2024.
- Duddu, V., et al. "Attesting Distributional Properties of Training Data for Machine Learning." European Symposium on Research in Computer Security (ESORICS), 2024.
- Duddu, V., Gunn, L. J., and Asokan, N. "Laminator: Verifiable ML Property Cards Using Hardware-Assisted Attestations." ACM Conference on Data and Application Security and Privacy (CODASPY), 2024.
- El Atali, H., Gunn, L. J., Liljestrand, H., and Asokan, N. "BliMe: Verifiably Secure Outsourced Computation with Hardware-Enforced Taint Tracking." Network and Distributed System Security Symposium (NDSS), 2024.
- Fang, C., et al. "Proof-of-Learning Is Currently More Broken Than You Think." IEEE European Symposium on Security and Privacy (EuroS&P), 2023.
- Franzese, O., et al. "Secure Noise Sampling for Differentially Private Collaborative Learning." ACM SIGSAC Conference on Computer and Communications Security (CCS), 2025.
- Garg, S., et al. "Experimenting with Zero-Knowledge Proofs of Training." ACM SIGSAC Conference on Computer and Communications Security (CCS), 2023.
- Guo, J., et al. "ExclaveFL: Providing Transparency to Federated Learning Using Exclaves." arXiv:2412.10537, 2024.
- Hu, E. J., et al. "LoRA: Low-Rank Adaptation of Large Language Models." International Conference on Learning Representations (ICLR), 2022.
- Lycklama, H., et al. "Holding Secrets Accountable: Auditing Privacy-Preserving Machine Learning." USENIX Security Symposium, 2024.
- Mo, F., et al. "DarkneTZ: Towards Model Privacy at the Edge Using Trusted Execution Environments." International Conference on Mobile Systems, Applications, and Services (MobiSys), 2020.
- Rattanavipanon, N. and De Oliveira Nunes, I. "SLAPP: Poisoning Prevention in Federated Learning and Differential Privacy via Stateful Proofs of Execution." IEEE Transactions on Information Forensics and Security (TIFS), 2025.
- Sadeghi, A.-R. and Stüble, C. "Property-Based Attestation for Computing Platforms: Caring About Properties, Not Mechanisms." Workshop on New Security Paradigms (NSPW), 2004.
- Schnabl, C., et al. "Attestable Audits: Verifiable AI Safety Benchmarks Using Trusted Execution Environments." ICML Workshop on Technical AI Governance (TAIG), 2025.
- Shamsabadi, A. S., et al. "Confidential-PROFITT: Confidential PROof of FaIr Training of Trees." International Conference on Learning Representations (ICLR), 2023.
- Spoczynski, M., Melara, M. S., and Szyller, S. "Atlas: A Framework for ML Lifecycle Provenance and Transparency." IEEE European Symposium on Security and Privacy Workshops (EuroS&PW), 2025.
- Sun, H., Li, J., and Zhang, H. "zkLLM: Zero Knowledge Proofs for Large Language Models." ACM SIGSAC Conference on Computer and Communications Security (CCS), 2024.
- Torres-Arias, S., Afzali, H., Kuppusamy, T. K., Curtmola, R., and Cappos, J. "in-toto: Providing Farm-to-Table Guarantees for Bits and Bytes." USENIX Security Symposium, 2019.
- Vaswani, A., et al. "Attention Is All You Need." Advances in Neural Information Processing Systems (NeurIPS), 2017.
- Wilke, L., Sieck, F., and Eisenbarth, T. "TDXdown: Single-Stepping and Instruction Counting Attacks Against Intel TDX." ACM SIGSAC Conference on Computer and Communications Security (CCS), 2024.
- Zhang, Z., et al. "No Privacy Left Outside: On the (In-)Security of TEE-Shielded DNN Partition for On-Device ML." IEEE Symposium on Security and Privacy (S&P), 2024.
- Zhang, R., et al. "'Adversarial Examples' for Proof-of-Learning." IEEE Symposium on Security and Privacy (S&P), 2022.

</details>
