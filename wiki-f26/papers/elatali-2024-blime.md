---
title: "BliMe: Verifiably Secure Outsourced Computation with Hardware-Enforced Taint Tracking"
authors:
  - ElAtali, Hossam
  - Gunn, Lachlan J.
  - Liljestrand, Hans
  - Asokan, N.
year: 2024
section: "Leakage Resistance (Client Data): Hardware"
primary: true
arxiv: "2204.09649"
doi: "10.14722/ndss.2024.24105"
tags:
  - secure-inference
  - hardware-security
  - taint-tracking
  - trusted-execution-environment
  - privacy
  - defense
---

### [Wiki Home](../README.md)

# BliMe: Verifiably Secure Outsourced Computation with Hardware-Enforced Taint Tracking

## High-level overview

A client that outsources computation to a cloud server must send its data there
to be processed, which exposes that data to whoever controls the server.
[Secure inference](../concepts/secure-inference.md) and related forms of
outsourced computation address this for machine-learning workloads, and the two
standard tools each carry a cost.
[Fully homomorphic encryption](../concepts/homomorphic-encryption.md) keeps the
data encrypted throughout but runs orders of magnitude slower than plaintext. A
[trusted execution environment](../concepts/trusted-execution-environment.md)
runs at near-native speed but has repeatedly leaked enclave data through run-time
and side-channel attacks.

BliMe (Blinded Memory) takes a third route: a small set of
instruction-set-architecture (ISA) extensions, paired with a fixed-function
hardware security module (HSM) and an encryption engine, that let an untrusted
server compute on a client's plaintext data while the hardware enforces a
[taint-tracking](../concepts/taint-tracking.md) policy on it. The client's data
and every value derived from it carry a hardware "blinded" mark and may not reach
any observable output, including the side channels that defeat enclaves; such
data leaves the system only by re-encryption under the client's key. The authors
implement the extensions on a speculative out-of-order RISC-V core, BOOM (Zhao et
al., 2020), report moderate run-time overhead in the single-digit to
low-tens-of-percent range with minimal power and area cost, and give a
machine-checked proof that the policy preserves the confidentiality of blinded
data on a simplified model ISA.

**Threat Model:** A client outsources computation to a remote server and wants
the confidentiality of its input preserved, revealing nothing beyond the data's
length. The adversary controls all server software, including the operating
system and the third-party application that processes the data, and can observe
side channels such as memory-access patterns, cache state, and instruction
timing. The adversary cannot break the hardware: the BliMe hardware is assumed
correct, and attacks requiring physical access (power analysis, fault injection,
direct access to the memory bus) are out of scope. Before sending data, the
client uses [remote attestation](../concepts/trusted-execution-environment.md) to
confirm it is talking to genuine BliMe hardware. Under these assumptions the
defender's claim is that no blinded value, and nothing derived from it, can reach
an observable output except by re-encryption under the originating client's key,
with the policy enforced in hardware and machine-checked on a model of the ISA.

## Why read this

<!-- instructor: confirm -->

BliMe recasts confidential outsourced computation as an information-flow problem.
Rather than isolate client data in an enclave or hold it under encryption, it lets
the server compute on the plaintext while hardware taint tracking guarantees that
blinded data cannot leak, including through side channels. The confidentiality
holds even against malicious server software: an operation that would leak blinded
data faults rather than completing, so useful computation must follow a
constant-time discipline. The design is carried through to a
register-transfer-level implementation on a RISC-V out-of-order core with measured
overheads, and to a machine-checked proof that the taint-tracking policy enforces
confidentiality. It is a concrete case study in trading a cryptographic guarantee
for a hardware-enforced one, and in what "verifiably secure" means when the object
of the proof is an ISA rather than a protocol.

## Basic Background

### Outsourced computation and secure inference

Outsourced computation runs a client's workload on a server the client does not
control, the normal cloud arrangement and the reason the client's data is exposed.
[Secure inference](../concepts/secure-inference.md) is the machine-learning
instance: evaluate a model on a client's input so the input stays confidential,
returning only the result. The cryptographic route encrypts the data and computes
on ciphertexts with [homomorphic encryption](../concepts/homomorphic-encryption.md),
which avoids interaction but is slow; the hardware route runs the computation in
the clear inside protected hardware.

### Trusted execution environments

A [trusted execution environment](../concepts/trusted-execution-environment.md)
(TEE) is hardware that isolates a program and its data from the rest of the
system, including a malicious operating system, and lets a remote client attest
which code is running before trusting it with secrets. Commodity examples are
Intel SGX, Arm TrustZone, and AMD SEV (Costan and Devadas, 2016; Pinto and Santos,
2019). The isolation boundary blocks direct memory access from outside, but does
not by itself hide a program's data-dependent behavior, which is why enclaves have
been broken by side-channel and transient-execution attacks (Van Bulck et al.,
2018).

### Taint tracking and information-flow control

[Taint tracking](../concepts/taint-tracking.md), or dynamic information-flow
tracking, labels data at a source and propagates the label to every value derived
from it, then applies a policy that restricts where labeled data may go (Suh et
al., 2004). Used for confidentiality, the label marks secret data and the policy
forbids it from reaching an observable output. Hardware implementations attach tag
bits to registers and memory and propagate them in the pipeline; a survey of
hardware information-flow tracking maps the design space (Hu et al., 2021).

### Side channels, speculation, and constant-time code

A side channel is an observable output that is not part of a program's intended
result: how long it runs, which addresses it touches, the state it leaves in
shared caches and predictors. An adversary who watches these can infer the data
that produced them. Modern CPUs widen the exposure through speculative and
out-of-order execution, which transiently act on data before a misprediction is
resolved, as exploited by Spectre and Meltdown (Kocher et al., 2019; Lipp et al.,
2020). The discipline that resists these channels in security-critical code is
constant-time, or data-oblivious, programming: the program's control flow, memory
addresses, and instruction timing are written never to depend on secret values.

## Reading guidance

- Sections II.A and II.B: the TEE background and the side-channel taxonomy. Note
  what the paper counts as an observable output, since that list defines what the
  later policy must protect.
- Section III.A and III.B: the usage scenario and the three design requirements,
  confidentiality (SR), fast execution (PR), and backwards compatibility (CR).
  Note exactly what SR-Confidentiality promises, that no party other than the
  client can infer anything about the data beyond its length.
- Section IV.B: the adversary model. Attention anchor: note precisely what is
  trusted (the CPU extensions, the encryption engine, the HSM) and what is out of
  scope, and how the OS is treated differently from the rest of server software.
- Section IV.C: the protocol, with decrypt-and-blind on import and
  encrypt-and-unblind on export, and the roles of the HSM and the encryption
  engine in moving data across the boundary.
- Section IV.D and Table I: the taint-tracking policy itself, the split of state
  into blindable and visible, and the propagation and fault rules. This is the
  core of the design.
- Section IV.E: what "BliMe-compliant software" must avoid. Attention anchor: the
  burden it places on application code is the constant-time discipline already
  used for side-channel-resistant cryptographic code; note what that implies for
  ordinary, unmodified software.
- Section V: BliMe-BOOM, the register-transfer-level implementation on the RISC-V
  BOOM core, and where the blindedness tag is threaded through the pipeline.
- Section VI: the machine-checked proof. Attention anchor: note exactly what is
  proved and on what model, and how that model relates to the BOOM implementation,
  that is, what the proof does and does not cover.
- Section VII and Tables II-III: the run-time, power, and area overheads, and the
  benchmark and synthesis setup behind them.
- Sections IX and X: the scope limits (secret-dependent faults, many clients,
  out-of-scope attacks such as Rowhammer and physical access) and the related-work
  map of taint tracking, data-oblivious execution, and point side-channel
  defenses.

<details>
<summary><h2>Supplementary readings</h2></summary>

- [Origami Inference: Private Inference Using Hardware Enclaves](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=9582200) — an enclave-based approach to private inference, a point of contrast with confidentiality enforced by hardware taint tracking.

</details>

<details>
<summary><h2>Paper Context</h2></summary>

Confidential computing in industry rests on trusted execution environments. Intel
SGX, Arm TrustZone, and academic designs such as Sanctum isolate a workload from a
malicious OS and attest it to a remote client (Costan and Devadas, 2016; Pinto and
Santos, 2019; Costan et al., 2016). A sustained line of attacks showed that
isolation alone does not deliver confidentiality. Cache-timing attacks recover
secrets from co-resident enclave code (Brasser et al., 2017); transient-execution
attacks such as Foreshadow and SgxPectre extract enclave data and keys through
speculation (Van Bulck et al., 2018; Chen et al., 2019); and TrustZone has leaked
both application data and cryptographic keys (Zhang et al., 2018; Ryan, 2019).
These build on the broader finding that speculative execution leaks
architecturally inaccessible memory across security boundaries (Kocher et al.,
2019; Lipp et al., 2020). Run-time bugs in attested enclave code are a separate
exposure that attestation does not address.

The cryptographic alternative removes trust in the server entirely. Fully
homomorphic encryption lets the server compute on ciphertexts and never see
plaintext, but its overhead runs orders of magnitude above native execution, and a
body of compiler work exists mainly to make it usable at all (Viand et al., 2021).
That cost is what motivates looking to hardware for confidentiality without the
homomorphic-encryption tax.

Hardware information-flow tracking has a long history. Dynamic information-flow
tracking was proposed to enforce security policies by tagging data in hardware and
propagating the tags through execution (Suh et al., 2004); later designs tracked
information at the granularity of logic gates (Tiwari et al., 2009), surveyed
alongside many others by Hu et al. (2021). Speculative taint tracking applied the
idea to transiently accessed data, blocking the leak that Spectre-style attacks
exploit (Yu et al., 2019b). Tagged-memory architectures, which carry metadata bits
per word, supply the hardware substrate such tracking needs (Joannou et al.,
2017).

Two threads sit closest to confidential outsourced computation under side
channels. The data-oblivious ISA (OISA) adds taint-tracking instructions and a
duplicate instruction set, faulting when tainted values are used unsafely, but it
exposes taint and untaint instructions that the application code must invoke
correctly, which assumes the application is trusted (Yu et al., 2019a). On the
software side, constant-time compilation transforms code to remove
secret-dependent behavior, as in Constantine (Borrello et al., 2021), and
data-oblivious execution environments such as DOVE run a verified data-oblivious
transcript inside a TEE (Lee et al., 2021); oblivious-RAM constructions hide
memory-access patterns at additional cost (Goldreich and Ostrovsky, 1996; Stefanov
et al., 2018). Each of these either relies on the application to invoke its
protections or pays a substantial performance cost.

</details>

### [Wiki Home](../README.md)

<details>
<summary><h4>References</h4></summary>

Entries read off this paper's bibliography (PDF pages 14-16).

- Borrello, P., D'Elia, D. C., Querzoni, L., and Giuffrida, C. "Constantine:
  Automatic Side-Channel Resistance Using Efficient Control and Data Flow
  Linearization." ACM SIGSAC Conference on Computer and Communications Security
  (CCS), 2021.
- Brasser, F., Müller, U., Dmitrienko, A., Kostiainen, K., Capkun, S., and
  Sadeghi, A.-R. "Software Grand Exposure: SGX Cache Attacks Are Practical."
  USENIX Workshop on Offensive Technologies (WOOT), 2017.
- Chen, G., Chen, S., Xiao, Y., Zhang, Y., Lin, Z., and Lai, T. H. "SgxPectre:
  Stealing Intel Secrets from SGX Enclaves via Speculative Execution." IEEE
  European Symposium on Security and Privacy (EuroS&P), 2019.
- Costan, V. and Devadas, S. "Intel SGX Explained." Cryptology ePrint Archive,
  Report 2016/086, 2016.
- Costan, V., Lebedev, I., and Devadas, S. "Sanctum: Minimal Hardware Extensions
  for Strong Software Isolation." USENIX Security Symposium, 2016.
- Goldreich, O. and Ostrovsky, R. "Software Protection and Simulation on Oblivious
  RAMs." Journal of the ACM, 1996.
- Hu, W., Ardeshiricham, A., and Kastner, R. "Hardware Information Flow Tracking."
  ACM Computing Surveys, 2021.
- Joannou, A., Woodruff, J., Kovacsics, R., Moore, S. W., Bradbury, A., Xia, H.,
  Watson, R. N., Chisnall, D., Roe, M., Davis, B., Napierala, E., Baldwin, J.,
  Gudka, K., Neumann, P. G., Mazzinghi, A., Richardson, A., Son, S., and
  Markettos, A. T. "Efficient Tagged Memory." IEEE International Conference on
  Computer Design (ICCD), 2017.
- Kocher, P., Horn, J., Fogh, A., Genkin, D., Gruss, D., Haas, W., Hamburg, M.,
  Lipp, M., Mangard, S., Prescher, T., Schwarz, M., and Yarom, Y. "Spectre
  Attacks: Exploiting Speculative Execution." IEEE Symposium on Security and
  Privacy (S&P), 2019.
- Lee, H. B., Jois, T. M., Fletcher, C. W., and Gunter, C. A. "DOVE: A
  Data-Oblivious Virtual Environment." Network and Distributed System Security
  Symposium (NDSS), 2021.
- Lipp, M., Schwarz, M., Gruss, D., Prescher, T., Haas, W., Horn, J., Mangard, S.,
  Kocher, P., Genkin, D., Yarom, Y., Hamburg, M., and Strackx, R. "Meltdown:
  Reading Kernel Memory from User Space." Communications of the ACM, 2020.
- Pinto, S. and Santos, N. "Demystifying Arm TrustZone: A Comprehensive Survey."
  ACM Computing Surveys, 2019.
- Ryan, K. "Hardware-Backed Heist: Extracting ECDSA Keys from Qualcomm's
  TrustZone." ACM SIGSAC Conference on Computer and Communications Security (CCS),
  2019.
- Stefanov, E., van Dijk, M., Shi, E., Chan, T.-H. H., Fletcher, C., Ren, L., Yu,
  X., and Devadas, S. "Path ORAM: An Extremely Simple Oblivious RAM Protocol."
  Journal of the ACM, 2018.
- Suh, G. E., Lee, J. W., Zhang, D., and Devadas, S. "Secure Program Execution via
  Dynamic Information Flow Tracking." International Conference on Architectural
  Support for Programming Languages and Operating Systems (ASPLOS), 2004.
- Tiwari, M., Wassel, H. M., Mazloom, B., Mysore, S., Chong, F. T., and Sherwood,
  T. "Complete Information Flow Tracking from the Gates Up." International
  Conference on Architectural Support for Programming Languages and Operating
  Systems (ASPLOS), 2009.
- Van Bulck, J., Minkin, M., Weisse, O., Genkin, D., Kasikci, B., Piessens, F.,
  Silberstein, M., Wenisch, T. F., Yarom, Y., and Strackx, R. "Foreshadow:
  Extracting the Keys to the Intel SGX Kingdom with Transient Out-of-Order
  Execution." USENIX Security Symposium, 2018.
- Viand, A., Jattke, P., and Hithnawi, A. "SoK: Fully Homomorphic Encryption
  Compilers." IEEE Symposium on Security and Privacy (S&P), 2021.
- Yu, J., Hsiung, L., El'Hajj, M., and Fletcher, C. W. "Data Oblivious ISA
  Extensions for Side Channel-Resistant and High Performance Computing." Network
  and Distributed System Security Symposium (NDSS), 2019a.
- Yu, J., Yan, M., Khyzha, A., Morrison, A., Torrellas, J., and Fletcher, C. W.
  "Speculative Taint Tracking (STT): A Comprehensive Protection for Speculatively
  Accessed Data." IEEE/ACM International Symposium on Microarchitecture (MICRO),
  2019b.
- Zhang, N., Sun, K., Shands, D., Lou, W., and Hou, Y. T. "TruSense: Information
  Leakage from TrustZone." IEEE Conference on Computer Communications (INFOCOM),
  2018.
- Zhao, J., Korpan, B., Gonzalez, A., and Asanovic, K. "SonicBOOM: The 3rd
  Generation Berkeley Out-of-Order Machine." Workshop on Computer Architecture
  Research with RISC-V (CARRV), 2020.

</details>
