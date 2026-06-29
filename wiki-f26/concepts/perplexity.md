---
title: "Perplexity"
type: concept
description: "How well a language model predicts a sequence: the exponential of the per-token average negative log-likelihood (exponentiated cross-entropy); the standard intrinsic LM quality metric and, in privacy attacks, a per-example confidence signal whose ratio across models flags memorized text."
tags:
  - language-models
  - privacy
---

## [Wiki Home](../README.md)

# Perplexity

## Definition

Perplexity measures how well a probability model predicts a sequence. For a
language model that assigns probability `f(x_i | x_1, ..., x_{i-1})` to each
token, the perplexity of a sequence is the exponential of the average negative
log-likelihood per token, equivalently the exponentiated cross-entropy loss. Low
perplexity means the model found the sequence unsurprising, having assigned high
probability to each token in turn. It is the standard intrinsic quality metric
for language models: a better model assigns lower perplexity to held-out text.

The same quantity reads as a confidence signal in training-data privacy. A model
tends to assign systematically lower perplexity to sequences it fit closely, so
perplexity, and especially the ratio of perplexities between the target model and
a reference model, serves to rank candidate sequences by how likely they are to
be memorized training text. The two readings reflect two communities: in speech
and NLP perplexity is a model-quality number, while in privacy it is a
per-example membership signal.

## Papers that use this concept

- [Extracting Training Data from Large Language Models](../papers/carlini-2021-extracting-training-data.md) — perplexity is the base membership-inference signal, and the improved attack ranks candidates by perplexity relative to reference models.
- [Knowledge Unlearning for Mitigating Privacy Risks in Language Models](../papers/jang-2022-knowledge-unlearning.md) — perplexity rises after unlearning even where benchmark accuracy holds, since gradient ascent flattens the next-token distribution.
- [PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented Generation of Large Language Models](../papers/zou-2024-poisonedrag.md) — evaluates perplexity-based detection as a defense and finds injected texts are not separable from clean corpus text by perplexity.
- [A Watermark for Large Language Models](../papers/kirchenbauer-2023-llm-watermark.md) — measures the watermark's cost to generation quality as the perplexity gap between watermarked and unmodified output.

## See also

- [Language model pretraining](language-model-pretraining.md)
- [Decoding strategies](decoding-strategies.md)
- [Membership inference](membership-inference.md)
- [Likelihood-ratio test](likelihood-ratio-test.md)
