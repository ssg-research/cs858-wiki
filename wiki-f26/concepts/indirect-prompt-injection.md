---
title: "Indirect prompt injection"
type: concept
description: "Prompt injection whose instructions reach the model through content it retrieves or is handed rather than through the user's own message: the attacker plants a payload in a web page, document, email, or tool output and waits for a victim's application to ingest it."
tags:
  - prompt-injection
  - llm-safety
  - attack
---

## [Wiki Home](../README.md)

# Indirect prompt injection

## Definition

Indirect prompt injection places adversarial instructions in content that a
victim's LLM-integrated application will later read, so that the model executes
them when the content arrives in its context window. The carrier is anything the
application ingests: a web page a search tool returns, an email, a shared
document, a code repository, a tool's output, or an entry in the model's own
memory store. The attacker never touches the victim's interface and need not
query the model at all; the payload is planted and the victim's own application
delivers it (Greshake et al., 2023).

The enabling condition is that the developer's instructions and the retrieved
text occupy one context window with no channel separating them, so the model has
nothing to distinguish an instruction it was given from an instruction it read.
Processing untrusted retrieved content therefore behaves like executing
untrusted code, with natural language as the code (Greshake et al., 2023). What
follows is the reach of the application rather than of the attacker: whatever the
model may do on the user's behalf, the injected instructions may direct.

Payloads are commonly hidden from a human reader in HTML comments, zero-size or
same-colour text, or an encoding such as Base64, which also carries them past
filters that match on plain-text patterns.

## Papers that use this concept

- [Not what you've signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection](../papers/greshake-2023-indirect-prompt-injection.md) — introduces and names the class, and builds a security-side taxonomy of delivery, harm, and affected party around it.
- [PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented Generation of Large Language Models](../papers/zou-2024-poisonedrag.md) — shares the delivery channel and separates itself on payload: it plants misleading content read as a credible fact rather than instructions read as a command.

## Variants and traps

- Direct and indirect name who supplies the instruction. In direct injection the
  user of the model is the attacker; in indirect injection the user is the victim
  and a third party wrote the text.
- A [jailbreak](jailbreak.md) and an injection can share a payload and still be
  different claims: a jailbreak is about the model's refusal boundary, an
  injection is about which party's instructions the application obeys. A
  jailbreak-style payload delivered through retrieved content is both.
- Injection is not [data poisoning](data-poisoning.md). Poisoning changes the
  model by corrupting training, and its effect survives in the weights; indirect
  injection touches nothing durable and works only while the malicious content is
  in reach of retrieval.

## See also

- [Prompt injection](prompt-injection.md)
- [Retrieval-augmented generation](retrieval-augmented-generation.md)
- [LLM tool use and agents](llm-tool-use.md)

## References

- Greshake, K., Abdelnabi, S., Mishra, S., Endres, C., Holz, T., and Fritz, M.
  "Not what you've signed up for: Compromising Real-World LLM-Integrated
  Applications with Indirect Prompt Injection." arXiv:2302.12173, 2023.
