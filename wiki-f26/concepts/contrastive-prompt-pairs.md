---
title: "Contrastive prompt pairs"
type: concept
description: "Eliciting a concept's direction by running a matched pair of prompts that differ only in the target concept and taking the difference of the resulting activations; stimulus pairs for representation reading and control."
tags:
  - interpretability
  - language-models
---

## [Wiki Home](../README.md)

# Contrastive prompt pairs

## Definition

A contrastive prompt pair is two inputs built to differ only in a target
concept, for example an instruction to answer honestly versus dishonestly, run
through the same model so the difference between their activations isolates that
concept. Averaging many such difference vectors, or taking their leading
principal component, yields a direction for the concept that can read it from new
inputs or steer generation along it. Pairing controls for everything the two
prompts share, so the difference is a cleaner estimate of the concept than
activations from a single prompt. The construction underlies difference-vector
steering methods (Turner et al., 2023) and the contrastive variants used for
honesty and sycophancy.

## Papers that use this concept

_No reading-companion page currently uses this concept._

## See also

- [Activation steering](activation-steering.md)
- [Linear representation hypothesis](linear-representation-hypothesis.md)

## References

- Turner, A., Thiergart, L., Udell, D., Leech, G., Mini, U., and MacDiarmid, M.
  "Activation Addition: Steering Language Models Without Optimization."
  arXiv:2308.10248, 2023.
