---
title: "Large language models for code"
type: concept
description: "Transformer language models pretrained on large corpora of source code that complete or generate programs from a prompt of code and comments; Codex, code completion, and the byte-pair tokenization of source text."
tags:
  - code-generation
  - language-models
---

## [Wiki Home](../README.md)

# Large language models for code

## Definition

A code language model is a [pretrained](language-model-pretraining.md)
transformer trained by next-token prediction over large corpora of public source
code, often mixed with natural-language text. Given a prompt of code, comments,
and function signatures, it predicts a likely continuation, which makes it a
"smart autocomplete" for programming and, with a suitable prompt, a generator of
whole functions. Source text is split into tokens by byte-pair encoding, so the
fixed context window holds more characters than a character-level model would.
The prominent instances at the time of this line of work are OpenAI's Codex, a
GPT-3 descendant adapted to code and the engine behind GitHub Copilot (Chen et
al., 2021), AI21's Jurassic-1 (Lieber et al., 2021), and the open PolyCoder (Xu
et al., 2022). A model trained on unaudited code learns insecure patterns as
readily as secure ones.

## Papers that use this concept

- [Examining Zero-Shot Vulnerability Repair with Large Language Models](../papers/pearce-2023-vulnerability-repair.md) — evaluates whether off-the-shelf code models (the Codex family, Jurassic-1, PolyCoder, and a locally trained C/C++ model) can generate security fixes from a prompt alone.

## See also

- [Language model pretraining](language-model-pretraining.md)
- [Zero-shot prompting](zero-shot-prompting.md)
- [Decoding and sampling strategies](decoding-strategies.md)

## References

- Chen, M., Tworek, J., Jun, H., Yuan, Q., Pinto, H.P.d.O., Kaplan, J., Edwards,
  H., Burda, Y., Joseph, N., Brockman, G., et al. "Evaluating Large Language
  Models Trained on Code." arXiv:2107.03374, 2021.
- Lieber, O., Sharir, O., Lentz, B., and Shoham, Y. "Jurassic-1: Technical
  Details and Evaluation." AI21 Labs Technical Report, 2021.
- Xu, F.F., Alon, U., Neubig, G., and Hellendoorn, V.J. "A Systematic Evaluation
  of Large Language Models of Code." arXiv:2202.13169, 2022.
