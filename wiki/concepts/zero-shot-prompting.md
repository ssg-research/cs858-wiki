---
title: "Zero-shot prompting"
type: concept
description: "Eliciting a task from a pretrained language model through the prompt alone, with no task-specific fine-tuning and no worked examples in context; the contrast with few-shot prompting and with supervised fine-tuning."
tags:
  - prompting
  - language-models
---

# Zero-shot prompting

## Definition

Zero-shot prompting asks a [pretrained](language-model-pretraining.md) language
model to perform a task from an instruction or partial input alone, with no
labeled examples in the prompt and no weight updates. It exploits the finding
that a model trained only to predict the next token acquires latent abilities a
well-formed prompt can surface (Brown et al., 2020). Few-shot prompting differs
by placing a handful of worked input-output examples in the context window before
the query; both leave the weights untouched, which separates them from
fine-tuning, where the model is further trained on task-specific data. Because
the model continues the most likely text, the phrasing of the prompt strongly
affects whether the continuation is what the user intended. For code, a zero-shot
prompt is the surrounding source and comments with no example fixes attached.

## Papers that use this concept

- [Examining Zero-Shot Vulnerability Repair with Large Language Models](../papers/pearce-2023-vulnerability-repair.md) — its central setting: repair vulnerabilities by prompting off-the-shelf models, with no fine-tuning on bug-fix data.

## See also

- [Language model pretraining](language-model-pretraining.md)
- [Large language models for code](code-language-models.md)

## References

- Brown, T.B., Mann, B., Ryder, N., Subbiah, M., Kaplan, J., Dhariwal, P.,
  Neelakantan, A., Shyam, P., Sastry, G., Askell, A., et al. "Language Models are
  Few-Shot Learners." arXiv:2005.14165, 2020.
