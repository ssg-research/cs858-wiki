---
title: "Distributed representations"
type: concept
description: "Information encoded as patterns of activation across many units rather than in single neurons; transformer hidden states across layers, and the emergent, often linear, semantic structure of these activation spaces."
tags:
  - interpretability
  - representations
  - deep-learning
---

# Distributed representations

## Definition

A neural network encodes information across patterns of activation over many
units rather than in single, dedicated neurons; this is a distributed
representation (Hinton, 1984). In a transformer language model, the
representation of a token at a given layer is its hidden-state (activation)
vector, and these vectors are transformed layer by layer as the network
computes. Empirically, these activation spaces carry semantically meaningful and
often linear structure: directions in the space correspond to human-interpretable
attributes, as in the additive analogies of word embeddings (Mikolov et al.,
2013). A representation-level account of a network takes these population-level
activation patterns as the primary object of study and asks what concepts they
encode and how transforming them changes behavior.

## Papers that use this concept

- [Representation Engineering: A Top-Down Approach to AI Transparency](../papers/zou-2023-representation-engineering.md) — takes representations, rather than neurons or circuits, as the unit of analysis, and reads and steers a model along directions in its activation space.

## See also

- [Linear probing (probing classifiers)](linear-probing.md)
- [Activation steering](activation-steering.md)
- [Mechanistic interpretability](mechanistic-interpretability.md)
- [Principal component analysis](principal-component-analysis.md)

## References

- Hinton, G. E. "Distributed Representations." 1984.
- Mikolov, T., Yih, W.-t., and Zweig, G. "Linguistic Regularities in Continuous
  Space Word Representations." North American Chapter of the Association for
  Computational Linguistics: Human Language Technologies (NAACL-HLT), 2013.
