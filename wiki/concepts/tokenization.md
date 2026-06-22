---
title: "Tokenization"
type: concept
description: "How a language model splits text into a fixed vocabulary of subword tokens (byte-pair encoding); tokens as the unit of generation, and the brittleness that lets whitespace, homoglyph, or punctuation edits change the segmentation."
tags:
  - language-models
  - llm
---

# Tokenization

## Definition

A language model operates over a fixed vocabulary of tokens, not raw characters
or whole words. A tokenizer maps a string to a sequence of integer token ids and
back. Modern large language models use subword tokenization, most commonly
byte-pair encoding (BPE), which begins from bytes or characters and greedily
merges frequent adjacent pairs into a vocabulary of tens of thousands of tokens.
Common words become a single token while rare words split into several pieces, so
the vocabulary covers any input without an unbounded word list. A token is
therefore usually a word fragment.

Tokenization is deterministic given the tokenizer, but brittle. Inserting a
space, changing punctuation, or substituting a visually identical Unicode
character (a homoglyph) can change how a whole region is segmented, producing a
different token sequence for text that looks the same to a human reader. Any
mechanism defined over tokens inherits this sensitivity.

## Papers that use this concept

- [A Watermark for Large Language Models](../papers/kirchenbauer-2023-watermark.md) — the watermark operates at the token level, partitioning the vocabulary into green and red lists, and several of the removal attacks it catalogs work by perturbing tokenization through whitespace, homoglyph, and prompted "emoji" edits.

## See also

- [Language model pretraining](language-model-pretraining.md)
- [Decoding and sampling strategies](decoding-strategies.md)
