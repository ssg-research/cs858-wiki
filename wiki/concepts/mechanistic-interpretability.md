---
title: "Mechanistic interpretability"
type: concept
description: "Reverse-engineering a neural network into named circuits of individual neurons or attention heads connected node-to-node, by analogy to reading compiled software back into source code; induction heads and the indirect-object-identification circuit as worked examples."
tags:
  - interpretability
  - llm
---

# Mechanistic interpretability

## Definition

Mechanistic interpretability treats a trained network as a program to be
reverse-engineered into its "source code": a circuit of individual neurons or
attention heads connected by node-to-node weights, each assigned a specific
role. Worked examples include induction heads, an attention-head pair that
lets transformers copy a token sequence seen earlier in the same context and
that underlies much of in-context learning (Olsson et al., 2022), and the
indirect-object-identification circuit, a set of attention heads in GPT-2
small that resolves which noun phrase a sentence's pronoun refers to (Wang et
al., 2023). The approach scales to a circuit at a time and requires
substantial manual effort to identify each one (Olah et al., 2020).

## Papers that use this concept

- [Representation Engineering: A Top-Down Approach to AI Transparency](../papers/zou-2023-representation-engineering.md) — contrasts its representation-level, top-down approach against mechanistic interpretability's circuit-level, bottom-up approach, and devotes an appendix to the distinction.

## See also

- [White-box and black-box access](white-box-black-box.md)

## References

- Olah, C., Cammarata, N., Schubert, L., Goh, G., Petrov, M., and Carter, S.
  "Zoom In: An Introduction to Circuits." Distill, 2020.
  doi: 10.23915/distill.00024.001.
- Olsson, C., Elhage, N., Nanda, N., Joseph, N., Das Sarma, N., Henighan, T.,
  Mann, B., Askell, A., Bai, Y., Chen, A., et al. "In-context Learning and
  Induction Heads." arXiv:2209.11895, 2022.
- Wang, K. R., Variengien, A., Conmy, A., Shlegeris, B., and Steinhardt, J.
  "Interpretability in the Wild: A Circuit for Indirect Object Identification
  in GPT-2 Small." International Conference on Learning Representations
  (ICLR), 2023.
