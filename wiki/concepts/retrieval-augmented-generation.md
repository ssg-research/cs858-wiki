---
title: "Retrieval-augmented generation"
type: concept
description: "Conditioning an LLM's output on documents fetched at inference time from a search index, vector store, or the open web; the retrieved text enters the same context window as the instructions, with no built-in data/instruction boundary."
tags:
  - llm
  - retrieval
---

# Retrieval-augmented generation

## Definition

Retrieval-augmented generation (RAG) augments a language model at inference
time by fetching text relevant to the current query, from a search index, a
vector store of embedded documents, or the open web, and placing that text in
the model's context window so the response is conditioned on it. It lets a model
answer from up-to-date, private, or domain-specific sources it was never trained
on, and underlies search-augmented chatbots and document assistants.

The retrieved text occupies the same context window as the developer's
instructions and the user's query. The model has no built-in mechanism that
marks one span as trusted instructions and another as inert data, which is the
property that makes retrieved content a channel for attacks.

## Papers that use this concept

- [Not what you've signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection](../papers/greshake-2023-indirect-prompt-injection.md) — retrieval is the delivery channel for indirect prompt injection.

## See also

- [LLM tool use](llm-tool-use.md)
- [Prompt injection](prompt-injection.md)
