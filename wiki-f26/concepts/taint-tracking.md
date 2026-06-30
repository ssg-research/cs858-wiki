---
title: "Taint tracking"
type: concept
description: "Dynamic information-flow tracking (DIFT): labelling data at a source and propagating the label to every value derived from it, then enforcing a policy on where labelled data may flow; software vs hardware (tag bits) implementations, explicit vs implicit flows, and the confidentiality / integrity dual uses."
tags:
  - taint-tracking
  - hardware-security
  - software-security
---

## [Wiki Home](../README.md)

# Taint tracking

## Definition

Taint tracking, also called dynamic information-flow tracking (DIFT), attaches a
label to data at a chosen source and propagates that label through computation:
any value an instruction derives from a tainted operand becomes tainted in turn.
A policy then restricts what tainted data may do, for example forbidding it from
reaching a designated sink such as a network write, a jump target, or a memory
address. The technique was introduced for security to catch misuse of untrusted
input at run time (Suh et al., 2004). The same mechanism serves two dual
purposes: integrity, keeping untrusted input from reaching a trusted sink, and
confidentiality, keeping secret data from reaching an observable output.

Implementations live in software, by instrumenting the program, or in hardware,
by adding tag bits to registers and memory that the pipeline propagates as it
executes; hardware information-flow tracking is surveyed by Hu et al. (2021).
Explicit flows, where a tainted value is copied or computed on, are
straightforward to follow. The difficulty is implicit flows and side channels,
where a secret shapes observable behavior through control flow, memory-access
patterns, or timing rather than through a direct data dependency. Gate-level
tracking follows information through the circuit itself (Tiwari et al., 2009),
and speculative taint tracking extends propagation through transiently executed
instructions (Yu et al., 2019).

## Papers that use this concept

- [BliMe: Verifiably Secure Outsourced Computation with Hardware-Enforced Taint Tracking](../papers/elatali-2024-blime.md) — marks a client's decrypted data "blinded" and enforces a hardware taint-tracking policy so blinded data cannot reach any observable output.

## Variants and traps

- The hard part is implicit flows: a tainted value that never gets copied can
  still leak through which branch runs, which address is fetched, or how long an
  instruction takes.
- Integrity tracking and confidentiality tracking use the same propagation
  machinery but opposite policies; which one a system enforces depends on whether
  the label marks untrusted input or secret data.

## See also

- [Trusted execution environment](trusted-execution-environment.md)
- [Secure inference](secure-inference.md)

## References

- Hu, W., Ardeshiricham, A., and Kastner, R. "Hardware Information Flow
  Tracking." ACM Computing Surveys, 2021.
- Suh, G. E., Lee, J. W., Zhang, D., and Devadas, S. "Secure Program Execution
  via Dynamic Information Flow Tracking." International Conference on
  Architectural Support for Programming Languages and Operating Systems
  (ASPLOS), 2004.
- Tiwari, M., Wassel, H. M., Mazloom, B., Mysore, S., Chong, F. T., and
  Sherwood, T. "Complete Information Flow Tracking from the Gates Up."
  International Conference on Architectural Support for Programming Languages and
  Operating Systems (ASPLOS), 2009.
- Yu, J., Yan, M., Khyzha, A., Morrison, A., Torrellas, J., and Fletcher, C. W.
  "Speculative Taint Tracking (STT): A Comprehensive Protection for Speculatively
  Accessed Data." IEEE/ACM International Symposium on Microarchitecture (MICRO),
  2019.
