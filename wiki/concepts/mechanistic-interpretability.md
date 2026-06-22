---
title: "Mechanistic interpretability"
type: concept
description: "The bottom-up program of reverse-engineering a trained network into human-understandable circuits of neurons and features; identified circuits such as induction heads and indirect object identification, the manual effort it takes, and its contrast with representation-level analysis."
tags:
  - interpretability
  - circuits
  - llm-safety
---

# Mechanistic interpretability

## Definition

Mechanistic interpretability seeks to reverse-engineer a trained neural network
into human-understandable algorithms, explaining its behavior in terms of
circuits: subgraphs of neurons or features connected node to node (Olah et al.,
2020). Specific circuits have been identified for concrete capabilities,
including induction heads that support in-context learning (Olsson et al., 2022)
and a circuit for indirect object identification in GPT-2 (Wang et al., 2023).
The approach is bottom-up: it builds an account of the whole network by composing
the parts. Identifying circuits takes considerable manual effort, and there is
evidence that networks also compute through distributed, iterative refinement
that a purely circuit-level account does not capture. This has motivated a
complementary top-down view that takes population-level
[representations](distributed-representations.md), rather than individual neurons
and their connections, as the unit of analysis.

## Papers that use this concept

- [Representation Engineering: A Top-Down Approach to AI Transparency](../papers/zou-2023-representation-engineering.md) — positions representation engineering as the top-down counterpart to mechanistic interpretability's bottom-up, circuit-level program.

## See also

- [Distributed representations](distributed-representations.md)
- [Linear probing (probing classifiers)](linear-probing.md)
- [Activation steering](activation-steering.md)

## References

- Olah, C., Cammarata, N., Schubert, L., Goh, G., Petrov, M., and Carter, S.
  "Zoom In: An Introduction to Circuits." Distill, 2020.
- Olsson, C., Elhage, N., Nanda, N., Joseph, N., DasSarma, N., Henighan, T.,
  Mann, B., Askell, A., Bai, Y., Chen, A., et al. "In-Context Learning and
  Induction Heads." 2022. arXiv:2209.11895.
- Wang, K. R., Variengien, A., Conmy, A., Shlegeris, B., and Steinhardt, J.
  "Interpretability in the Wild: A Circuit for Indirect Object Identification in
  GPT-2 Small." International Conference on Learning Representations (ICLR), 2023.
