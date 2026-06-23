---
title: "Dense retrieval"
type: concept
description: "Retrieving documents by embedding the query and each passage into vectors with learned encoders and ranking by vector similarity (cosine, dot product) to return the top-k nearest; the neural alternative to lexical (BM25) retrieval and the retriever component inside RAG."
tags:
  - retrieval
  - llm
---

[Home page](../README.md)

# Dense retrieval

## Definition

Dense retrieval finds relevant documents by mapping text into a continuous
vector space rather than matching words. A learned encoder turns each passage in
a corpus into an embedding vector; at query time another encoder (sometimes the
same one) embeds the query, and relevance is the similarity of the two vectors,
usually cosine similarity or dot product. The retriever returns the top-k
passages with the highest similarity scores. This is the neural alternative to
sparse lexical retrieval such as BM25, which matches on shared terms; dense
retrieval can match paraphrases that share no keywords. Dense Passage Retrieval
(Karpukhin et al., 2020) is the canonical formulation, training separate query
and passage encoders so that a question and its answer-bearing passage land
close together.

In a retrieval-augmented system the dense retriever is the component that selects
which corpus text reaches the model's context window. Two consequences follow for
security. Whether a piece of text is retrieved for a given query is decided
entirely by embedding similarity, so an attacker who controls a passage's text
controls its position in that vector space. And when the encoder parameters are
public, that similarity is a differentiable function an attacker can optimize
against directly.

## Papers that use this concept

- [PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented Generation of Large Language Models](../papers/zou-2024-poisonedrag.md) — the attack's "retrieval condition" requires a crafted text to rank in the top-k for a target question; the white-box variant optimizes embedding similarity against the retriever's encoders.

## See also

- [Retrieval-augmented generation](retrieval-augmented-generation.md)
- [Adversarial examples](adversarial-examples.md)

[Home page](../README.md)

## References

- Karpukhin, V., Oguz, B., Min, S., Lewis, P., Wu, L., Edunov, S., Chen, D., and Yih, W.-t. "Dense Passage Retrieval for Open-Domain Question Answering." EMNLP, 2020.
