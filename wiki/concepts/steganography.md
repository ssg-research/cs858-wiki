---
title: "Steganography"
type: concept
description: "Hiding information inside ordinary-looking cover content so its presence is undetectable; its relation to cryptography (which hides content, not existence) and to digital watermarking, the narrower task of embedding a removal-resistant source marker."
tags:
  - watermarking
  - cryptography
---

# Steganography

## Definition

Steganography hides information inside ordinary-looking cover content (text, an
image, audio) so that its presence is undetectable to anyone not looking for it.
It differs from cryptography, which hides the content of a message while leaving
the existence of a message plain. Digital watermarking is a closely related,
narrower task: embedding a marker that identifies the source or owner of a piece
of content, where the marker should survive ordinary processing and be hard to
remove. Watermarking that only needs to certify provenance, that a piece of
content came from a given source, is a special case of steganography, which can
embed an arbitrary hidden payload.

Hiding information in discrete media such as natural-language text is harder than
in continuous media such as images. Small edits to text are perceptible and the
set of edits that preserve meaning and fluency is limited, so there is little
room to encode a signal without degrading quality.

## Papers that use this concept

- [A Watermark for Large Language Models](../papers/kirchenbauer-2023-watermark.md) — frames watermarking model output as a subset of steganography and situates its sampling-time scheme against prior linguistic-steganography and text-watermarking work.

## See also

- [Model watermarking](model-watermarking.md)
- [Cryptographic commitment](cryptographic-commitment.md)
