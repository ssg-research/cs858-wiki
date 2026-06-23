---
title: "Mechanistic interpretability"
type: concept
description: "Bottom-up interpretability that reverse-engineers a network into circuits of individual neurons or features; the unit of analysis is the mechanism, and it is the foil to top-down representation-level analysis."
tags:
  - interpretability
  - language-models
  - machine-learning
---

# Mechanistic interpretability

## Definition

Mechanistic interpretability reverse-engineers a trained network into
human-understandable algorithms, explaining behavior in terms of circuits:
subgraphs of individual neurons or features wired together by the network's
weights. The unit of analysis is the mechanism, built bottom-up from components
and the connections between them. Specific circuits have been identified for
narrow capabilities, including induction heads that support in-context learning
(Olsson et al., 2022) and a circuit for indirect object identification in GPT-2
(Wang et al., 2023). The program traces to circuit analysis of vision models
(Olah et al., 2020), and a recurring obstacle is superposition, where a layer
encodes more features than it has neurons, so single neurons are polysemantic
(Elhage et al., 2022). Identifying circuits is largely manual and has mostly
scaled to small models and narrow tasks.

## Papers that use this concept

- [Representation Engineering: A Top-Down Approach to AI Transparency](../papers/zou-2023-representation-engineering.md) — positions representation engineering as a top-down alternative that takes representations, rather than neurons or circuits, as the unit of analysis.

## See also

- [Linear probing](linear-probing.md)
- [Linear representation hypothesis](linear-representation-hypothesis.md)
- [Activation steering](activation-steering.md)

## References

- Elhage, N., Hume, T., Olsson, C., Schiefer, N., Henighan, T., Kravec, S.,
  Hatfield-Dodds, Z., Lasenby, R., Drain, D., Chen, C., et al. "Toy Models of
  Superposition." Transformer Circuits Thread, 2022.
- Olah, C., Cammarata, N., Schubert, L., Goh, G., Petrov, M., and Carter, S.
  "Zoom In: An Introduction to Circuits." Distill, 2020.
- Olsson, C., Elhage, N., Nanda, N., Joseph, N., DasSarma, N., Henighan, T.,
  Mann, B., Askell, A., Bai, Y., Chen, A., et al. "In-context Learning and
  Induction Heads." arXiv:2209.11895, 2022.
- Wang, K. R., Variengien, A., Conmy, A., Shlegeris, B., and Steinhardt, J.
  "Interpretability in the Wild: a Circuit for Indirect Object Identification in
  GPT-2 Small." International Conference on Learning Representations (ICLR), 2023.
