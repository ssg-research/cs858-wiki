---
title: "Representation Engineering: A Top-Down Approach to AI Transparency"
authors:
  - Zou, Andy
  - Phan, Long
  - Chen, Sarah
  - Campbell, James
  - Guo, Phillip
  - Ren, Richard
  - Pan, Alexander
  - Yin, Xuwang
  - Mazeika, Mantas
  - Dombrowski, Ann-Kathrin
  - Goel, Shashwat
  - Li, Nathaniel
  - Byun, Michael J.
  - Wang, Zifan
  - Mallen, Alex
  - Basart, Steven
  - Koyejo, Sanmi
  - Song, Dawn
  - Fredrikson, Matt
  - Kolter, J. Zico
  - Hendrycks, Dan
year: 2023
section: "Mechanistic Interpretability for AI safety"
primary: true
arxiv: "2310.01405"
tags:
  - interpretability
  - llm-safety
  - alignment
---

# Representation Engineering: A Top-Down Approach to AI Transparency

## High-level overview

The paper introduces representation engineering (RepE), an approach to AI
transparency that takes representations, the activation vectors a network
computes at each layer and token position, rather than individual neurons or
circuits, as the unit of analysis. It borrows the distinction from cognitive
neuroscience between a Sherringtonian view, which explains cognition via
node-to-node connections between neurons, and a Hopfieldian view, which
explains it via patterns of activity across populations of neurons; RepE
applies the latter, top-down view to transformer language models. The method
has two parts. Representation reading locates a direction in activation space
that correlates with a target concept (truthfulness, utility, morality,
emotion) or function (lying, power-seeking), using a baseline procedure called
Linear Artificial Tomography (LAT): prompt the model with stimuli that vary
along the target concept, collect activations at a chosen token position, and
fit an unsupervised linear model, typically principal component analysis, to
the resulting vectors to produce a "reading vector." Representation control
then edits a model's behavior by adding, subtracting, or conditionally
projecting out that vector from its activations at inference time, or by
distilling the same target into a low-rank adapter (LoRRA) so the edit needs
no extra inference-time compute. The headline result reports state-of-the-art
TruthfulQA accuracy from an unsupervised honesty-control intervention, an
18.1 percentage point improvement over zero-shot prompting. The paper also
reports reading and control experiments across honesty and hallucination
detection, utility estimation, morality and power-aversion, emotion tracking,
robustness of harmfulness detection under jailbreaks and adversarial suffixes,
bias detection, factual editing, and reducing verbatim memorization.

**Threat Model:** the actor is a model developer or auditor with white-box
access to a deployed or about-to-be-deployed LLM (LLaMA-2 and Vicuna chat
models in the paper's experiments): full access to weights and to every
layer's activations on chosen prompts, either at plain inference time or
through a brief fine-tuning step that trains a low-rank adapter (LoRRA). Given
that access, they can both read off a direction correlated with a safety-
relevant concept (an honesty or lie-detection monitor) and edit activations
along that direction to push the model's behavior in a chosen direction. The
same control machinery is dual-use within the paper itself: the reading
vector that increases honesty when added can be subtracted to induce lying,
and a harmfulness-sensitivity vector that strengthens refusal could, with the
sign reversed, weaken it. The paper's own claim is that representation
reading and control give traction on safety problems such as honesty,
harmlessness under jailbreak pressure, and unwanted memorization, without
large labeled datasets.

## Why read this

Mechanistic interpretability is one of the only known ways to understand how
models work and why they output what they output, but it still is not
perfect. Representation engineering proposes a different unit of analysis
entirely, trading the painstaking manual work of mechanistic circuit-tracing
for activation-level directions, and is worth reading for the contrast it
draws between these two competing visions of what AI transparency should look
like.

## Basic Background

### Hidden representations in transformer LLMs

A transformer-based [language model](../concepts/language-model-pretraining.md)
computes, for every layer and every token position, a vector of real numbers
called a hidden state or activation. These activations are the model's
internal, distributed encoding of everything it has processed about the input
so far, and are distinct from the model's output text or output probabilities.
Reading or editing these vectors requires [white-box access](../concepts/white-box-black-box.md)
to the running model, not just its outputs.

### Probing and principal component analysis

[Linear probing](../concepts/linear-probing.md) trains a classifier on a
network's frozen activations to test whether a property is linearly decodable
from them. [Principal component analysis](../concepts/principal-component-analysis.md)
is an unsupervised alternative: instead of fitting a classifier against
labels, it finds the directions of maximal variance in a set of activation
vectors with no labels at all. Both produce a single direction in activation
space that can be tested for correlation with, or used to manipulate, a target
concept.

### Mechanistic interpretability

[Mechanistic interpretability](../concepts/mechanistic-interpretability.md)
explains a network's behavior in terms of circuits of individual neurons or
attention heads connected by specific weights, by analogy to reverse-
engineering compiled software back into source code. It is the bottom-up
approach this paper positions itself against.

### LLM safety training and jailbreaks

[Safety training](../concepts/safety-training.md) fine-tunes a deployed LLM,
typically via [RLHF](../concepts/rlhf.md), to refuse a designated set of
restricted behaviors. A [jailbreak](../concepts/jailbreak.md) is a prompt
engineered to make a safety-trained model produce a restricted behavior
anyway; the paper tests whether its harmfulness-detecting direction stays
reliable under jailbreak prompts and adversarial suffixes.

## Paper Context

Interpretability research up to this point had largely pursued two threads.
Saliency maps and feature visualization highlight which parts of an input a
network attends to or which inputs maximally activate a given neuron, but
both have been criticized for unreliability and for revealing little about a
network's internal representations (Adebayo et al., 2018; Jain and Wallace,
2019). Mechanistic interpretability instead reverse-engineers networks into
named circuits, with worked examples such as induction heads (Olsson et al.,
2022) and the indirect-object-identification circuit in GPT-2 small (Wang et
al., 2023), but it requires substantial manual effort per circuit and,
the paper argues, struggles to scale to complex, emergent phenomena (Olah et
al., 2020). The distinction between Sherringtonian (node-to-node) and
Hopfieldian (population-level) explanation that motivates the paper's
top-down framing comes from cognitive neuroscience (Barack and Krakauer,
2021), echoing a broader argument that complex systems need explanation at
multiple levels, not only the most reductive one (Anderson, 1972).

A separate line of work had begun probing language model activations for
specific properties without full mechanistic decomposition. Burns et al.
(2022) locate a truthfulness-correlated direction by enforcing logical
consistency across unlabeled statements, showing models often encode the
correct answer even when they generate an incorrect one. Linear classifier
probes (Alain and Bengio, 2017; Belinkov, 2022) had already established
probing as a general tool for testing what a property is linearly decodable
from a network's activations. On the control side, activation addition
(ActAdd) had shown that a single difference vector between paired prompts
can steer a frozen model's generations without any optimization (Turner et
al., 2023), and inference-time intervention used a related directional
edit, found via supervised probing, specifically to increase the truthfulness
of generations (Li et al., 2023). TruthfulQA, the benchmark used as the
paper's main quantitative result, was introduced to measure how often models
reproduce common human misconceptions rather than answering accurately (Lin
et al., 2021). On the safety side, universal and transferable adversarial
suffixes had recently been shown to reliably bypass safety training across
both open-source and black-box chat models (Zou et al., 2023), establishing
the jailbreak setting the paper later uses to test the robustness of its
harmfulness-detection direction.

## Reading guidance

- Section 1 (Introduction): introduces the Sherringtonian-versus-Hopfieldian
  framing from cognitive neuroscience as the justification for treating
  representations, not circuits, as the unit of analysis. Note how much of
  the argument for this choice of unit rests on the analogy itself.
- Section 3.1.1 (Linear Artificial Tomography): the three-step LAT pipeline,
  stimulus design, activity collection, and fitting a linear model. The
  choice of which token position to read from is treated as a specific
  design decision with measured consequences (Figure 5).
- Section 3.1.2 (Evaluation): a four-part taxonomy, correlation,
  manipulation, termination, recovery, borrowed from neuroscience lesion and
  rescue studies, used throughout the paper to argue for a causal rather than
  merely correlational reading of a direction.
- Section 4 (Honesty): distinguishes truthfulness from honesty and
  demonstrates lie detection and honesty control on the same underlying
  directions (Figures 8 to 10).
- Section 5.1 (Utility) and Figure 12: compares unsupervised (PCA, K-means),
  supervised (logistic regression, mean difference), and removal-based
  methods across all four evaluation types, the paper's most direct evidence
  for which kind of linear model produces a causal direction versus merely a
  correlated one.
- Section 6.2 (Harmless instruction-following): tests the harmfulness
  direction's robustness under manual jailbreaks and adversarial suffixes,
  then motivates a conditional control transformation over the simpler
  linear-combination transform used elsewhere in the paper; note how briefly
  that choice is justified.
- Appendix A: the paper's own explicit comparison of representation reading
  against mechanistic interpretability, useful as a check on the framing from
  Section 1 after having seen the method in practice.

## Motivating questions

1. What does it mean for a model to have an internal "concept" of something
   like honesty, and how does the paper try to distinguish that claim from a
   model merely producing outputs that look honest?
2. What access to the model does representation reading or control require,
   and how does that compare to what mechanistic interpretability requires?
3. How does the paper distinguish a direction that merely correlates with a
   target concept from one that has a causal role in the model's behavior?
4. What does editing a model's representation along a chosen direction cost,
   in terms of effects on behavior unrelated to the target concept?
5. In what ways do the same representation-control techniques used to
   increase a safety-relevant behavior also work to decrease it?

## Supplementary readings

- [Refusal in Language Models Is Mediated by a Single Direction](https://arxiv.org/abs/2406.11717) — finds that refusal behavior across multiple chat models is mediated by a single direction in representation space, a more targeted instance of the kind of direction this paper reads and controls.
- [Improving Alignment and Robustness with Circuit Breakers](https://arxiv.org/abs/2406.04313) — a defense, explicitly built on representation engineering, that interrupts a model mid-generation by directly controlling the internal representations responsible for harmful output, instead of relying on refusal training or adversarial training.

## References

- Adebayo, J., Gilmer, J., Muelly, M., Goodfellow, I., Hardt, M., and Kim, B.
  "Sanity Checks for Saliency Maps." Advances in Neural Information
  Processing Systems (NeurIPS), 31, 2018.
- Alain, G. and Bengio, Y. "Understanding Intermediate Layers Using Linear
  Classifier Probes." International Conference on Learning Representations
  (ICLR) Workshop, 2017.
- Anderson, P. W. "More Is Different." Science, 177(4047), 393-396, 1972.
  doi: 10.1126/science.177.4047.393.
- Barack, D. L. and Krakauer, J. W. "Two Views on the Cognitive Brain."
  Nature Reviews Neuroscience, 22(6), 359-371, 2021.
- Belinkov, Y. "Probing Classifiers: Promises, Shortcomings, and Advances."
  Computational Linguistics, 48(1), 207-219, 2022.
- Burns, C., Ye, H., Klein, D., and Steinhardt, J. "Discovering Latent
  Knowledge in Language Models Without Supervision." arXiv:2212.03827, 2022.
- Jain, S. and Wallace, B. C. "Attention Is Not Explanation." Proceedings of
  the 2019 Conference of the North American Chapter of the Association for
  Computational Linguistics: Human Language Technologies (NAACL-HLT),
  Volume 1, 3543-3556, 2019. doi: 10.18653/v1/N19-1357.
- Li, K., Patel, O., Viégas, F., Pfister, H., and Wattenberg, M.
  "Inference-Time Intervention: Eliciting Truthful Answers from a Language
  Model." arXiv:2306.03341, 2023.
- Lin, S., Hilton, J., and Evans, O. "TruthfulQA: Measuring How Models Mimic
  Human Falsehoods." arXiv:2109.07958, 2021.
- Olah, C., Cammarata, N., Schubert, L., Goh, G., Petrov, M., and Carter, S.
  "Zoom In: An Introduction to Circuits." Distill, 2020.
  doi: 10.23915/distill.00024.001.
- Olsson, C., Elhage, N., Nanda, N., Joseph, N., Das Sarma, N., Henighan, T.,
  Mann, B., Askell, A., Bai, Y., Chen, A., et al. "In-context Learning and
  Induction Heads." arXiv:2209.11895, 2022.
- Turner, A., Thiergart, L., Udell, D., Leech, G., Mini, U., and MacDiarmid,
  M. "Activation Addition: Steering Language Models Without Optimization."
  arXiv:2308.10248, 2023.
- Wang, K. R., Variengien, A., Conmy, A., Shlegeris, B., and Steinhardt, J.
  "Interpretability in the Wild: A Circuit for Indirect Object Identification
  in GPT-2 Small." International Conference on Learning Representations
  (ICLR), 2023.
- Zou, A., Wang, Z., Kolter, J. Z., and Fredrikson, M. "Universal and
  Transferable Adversarial Attacks on Aligned Language Models."
  arXiv:2307.15043, 2023.
