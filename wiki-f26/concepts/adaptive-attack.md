---
title: "Adaptive attack"
type: concept
description: "An attack built after and against the specific defense it faces, using knowledge of the defense's mechanism and parameters; the evaluation standard a defense claim rests on, and the reason a defense that only survives attacks fixed in advance has shown little."
tags:
  - evaluation
  - threat-model
  - security
---

## [Wiki Home](../README.md)

# Adaptive attack

## Definition

An adaptive attack is designed against the defense it is evaluated on. The
attacker knows the defense is present, knows how it works, and adjusts the
attack to it, holding secret only what the defense actually keeps secret, such
as a key or a random seed. The contrast is a static attack, one fixed before the
defense existed and run unchanged against it.

The distinction decides what a robustness number means. A defense evaluated only
against static attacks has been shown to stop those attacks; whether it raises
the cost of attacking at all is untested, because a real attacker sees the
deployed defense and reacts to it. Security practice therefore treats the
adaptive case as the claim, and the burden falls on the defender, since the
defender chooses the evaluation. Adversarial machine learning has repeatedly
supplied the object lesson: defenses reported robust against the attacks their
authors ran were broken by attacks written against them, singly (Carlini and
Wagner, 2017a), across ten detection methods at once (Carlini and Wagner, 2017b),
and in combination (He et al., 2017). The same pattern recurs for aligned
language models (Andriushchenko et al., 2024) and for defenses that perturb a
prediction API's outputs, where an attacker who knows the perturbation can learn
to invert it (Lee et al., 2019; Chen et al., 2023).

## Papers that use this concept

- [Towards Deep Learning Models Resistant to Adversarial Attacks](../papers/madry-2018-pgd.md) — argues its guarantee over a whole class of first-order adversaries rather than a fixed attack list, and released its trained models as public attack challenges.
- [Neural Cleanse: Identifying and Mitigating Backdoor Attacks in Neural Networks](../papers/wang-2019-neural-cleanse.md) — evaluates against backdoor variants constructed to defeat the detector's own assumptions, beyond the two injection methods from prior work.
- [Jailbroken: How Does LLM Safety Training Fail?](../papers/wei-2023-jailbroken.md) — reports an adaptive row alongside each individual attack, scoring a prompt as broken if any of the evaluated attacks breaks it.
- [ModelGuard: Information-Theoretic Defense Against Model Extraction Attacks](../papers/tang-2024-modelguard.md) — builds an attacker that knows and reproduces the defense's mechanism, and states its guarantee against that attacker rather than against a fixed extraction attack.
- [Safety Alignment Should Be Made More Than Just a Few Tokens Deep](../papers/qi-2024-shallow-safety-alignment.md) — presents its mitigations as prototypes and marks the adaptive case as not covered.
- [What Makes and Breaks Safety Fine-tuning? A Mechanistic Study](../papers/jain-2024-safety-finetuning.md) — places adaptive attacks on aligned models among the failures its mechanistic account is meant to explain.

## Variants and traps

- "Adaptive" carries a second, weaker sense in the language-model literature: an
  attacker that picks its next prompt from the model's replies, or picks the best
  attack per prompt from a fixed menu. That is adaptivity to the *target*, and it
  is a much smaller claim than adaptivity to a *defense mechanism*. Check which
  one a paper means before comparing numbers.
- An adaptive attack is a property of the evaluation, not a named algorithm.
  There is no "the adaptive attack" to run; each defense needs one written for
  it, which is why the standard is hard to meet and easy to state.
- A defense that keeps a secret can still be evaluated adaptively. Withholding
  the mechanism is not a defense, and an evaluation that withholds it measures
  the wrong thing.

## See also

- [Adversarial threat model](adversarial-threat-model.md)
- [Gradient masking](gradient-masking.md)
- [White-box and black-box access](white-box-black-box.md)

## References

- Andriushchenko, M., Croce, F., and Flammarion, N. "Jailbreaking Leading
  Safety-Aligned LLMs with Simple Adaptive Attacks." arXiv:2404.02151, 2024.
- Carlini, N. and Wagner, D. "Towards Evaluating the Robustness of Neural
  Networks." IEEE Symposium on Security and Privacy, 2017. (2017a)
- Carlini, N. and Wagner, D. "Adversarial Examples Are Not Easily Detected:
  Bypassing Ten Detection Methods." ACM Workshop on Artificial Intelligence and
  Security (AISec), 2017. (2017b)
- Chen, Y., Guan, R., Gong, X., Dong, J., and Xue, M. "D-DAE:
  Defense-Penetrating Model Extraction Attacks." IEEE Symposium on Security and
  Privacy (S&P), 2023.
- He, W., Wei, J., Chen, X., Carlini, N., and Song, D. "Adversarial Example
  Defense: Ensembles of Weak Defenses Are Not Strong." USENIX Workshop on
  Offensive Technologies (WOOT), 2017.
- Lee, T., Edwards, B., Molloy, I., and Su, D. "Defending Against Neural Network
  Model Stealing Attacks Using Deceptive Perturbations." IEEE Security and
  Privacy Workshops (SPW), 2019.
