---
title: "LLM tool use"
type: concept
description: "An LLM emitting structured calls to external functions (web search, code execution, email, HTTP) and conditioning further generation on their outputs; chaining such calls toward a goal with little oversight is an 'agent'."
tags:
  - llm
  - agents
---

### [Wiki Home](../README.md)

# LLM tool use

## Definition

Tool use lets a language model act beyond producing text: it emits a structured
call to an external function, such as a web search, an HTTP request, a code
interpreter, an email send, or a key-value memory, and conditions its next
generation on the returned output. The model decides which tool to call, when,
and with what arguments, either through a prompting pattern that interleaves
reasoning and actions or through learned tool-calling. Chaining tool calls
toward a goal with little human oversight is what is usually meant by an LLM
"agent."

Two properties matter for security. Tool outputs re-enter the context as text
the model tends to treat as trustworthy, and tool calls can produce side
effects in the world, sending data, executing code, or writing to storage that
later sessions read.

## Papers that use this concept

- [Not what you've signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection](../papers/greshake-2023-indirect-prompt-injection.md) — tools and memory turn a steered model into data exfiltration, persistence, and worming.

## See also

- [Retrieval-augmented generation](retrieval-augmented-generation.md)
- [Prompt injection](prompt-injection.md)
