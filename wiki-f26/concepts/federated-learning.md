---
title: "Federated learning"
type: concept
description: "Training one shared model across many clients that keep their data local, exchanging model updates with a coordinating server instead of raw examples; why local data does not mean private data, and where differential-privacy noise is added under local versus central trust."
tags:
  - machine-learning
  - privacy
  - training
---

## [Wiki Home](../README.md)

# Federated learning

## Definition

In federated learning the training data stays on the devices that produced it.
Each round, a coordinating server sends the current global model to a set of
clients; each client runs some
[stochastic gradient descent](stochastic-gradient-descent.md) steps on its own
local data and returns the resulting update; the server aggregates the updates
into a new global model and repeats. Phone keyboards and hospital consortia are
the standard motivating settings, where the raw data cannot be centralized for
legal or practical reasons.

Keeping data local is not itself a privacy guarantee. Every update is a function
of the client's data, so the leakage question moves rather than disappearing, and
[memorization](memorization.md) of individual examples persists in models trained
this way (Thakkar et al., 2020). [Differential privacy](differential-privacy.md)
is layered on top, and where the noise is added is the trust decision. Under
central DP the server aggregates the raw updates and adds noise itself, giving a
guarantee against anyone who sees the released model while requiring the clients
to trust the server; the differentially private recurrent language models were
trained this way (McMahan et al., 2018). Under local DP each client noises its own
update before sending it, which needs no trust in the server and costs
substantially more utility for the same epsilon.

Integrity moves the same way. The server observes updates, not the computation
that produced them, so a client can return an update shaped to install a backdoor
rather than one computed honestly, which is why attestation and proof-of-execution
schemes target this setting.

## Papers that use this concept

- [Extracting Training Data from Large Language Models](../papers/carlini-2021-extracting-training-data.md) — the memorization it studies had previously been demonstrated in federated training, which is part of the prior evidence its GPT-2 result extends.
- [PAL*M: Property Attestation for Large Generative Models](../papers/chantasantitam-2026-palm.md) — federated rounds are one of the training settings prior attestation work targets, and the pipeline shape its own attestation has to accommodate.

## Variants and traps

- "The data never leaves the device" describes the protocol, not the guarantee.
  Only a mechanism such as differential privacy or secure aggregation turns
  locality into a statement about what an observer can learn.
- Local and central DP name where the noise goes, and therefore who is trusted,
  rather than how strong the guarantee is. Two systems can report the same
  epsilon while assuming opposite things about the server.
- Cross-device and cross-silo federation differ enough to change what is
  feasible: thousands of unreliable phones with tiny local datasets, against a
  handful of institutions with large ones and real accountability between them.

## See also

- [Differential privacy](differential-privacy.md)
- [Privacy budget](privacy-budget.md)
- [Stochastic gradient descent](stochastic-gradient-descent.md)
- [Data poisoning](data-poisoning.md)

## References

- McMahan, H.B., Ramage, D., Talwar, K., and Zhang, L. "Learning Differentially
  Private Recurrent Language Models." International Conference on Learning
  Representations (ICLR), 2018.
- Thakkar, O., Ramaswamy, S., Mathews, R., and Beaufays, F. "Understanding
  Unintended Memorization in Federated Learning." arXiv:2006.07490, 2020.
