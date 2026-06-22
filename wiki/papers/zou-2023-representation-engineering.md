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
  - transparency
  - representation-engineering
  - llm-safety
  - alignment
---

# Representation Engineering: A Top-Down Approach to AI Transparency

## High-level overview

Deep networks are opaque, and understanding their internals is one route to
making them safer. The dominant program for this, mechanistic interpretability,
works bottom-up: it reverse-engineers a network into circuits of neurons and
features. This paper identifies and names a complementary approach,
**representation engineering (RepE)**, which works top-down. RepE places
representations, the population-level patterns of activation across a layer,
rather than neurons or circuits, at the center of analysis, an emphasis the
paper draws from the Hopfieldian view in cognitive neuroscience (Barack and
Krakauer, 2021). It comprises two operations. *Representation reading* locates a
direction in a model's activation space for a high-level concept (truthfulness,
morality, harmfulness) or a function, meaning a process the model carries out
(lying, power-seeking); the reading baseline, Linear Artificial Tomography (LAT),
recovers such directions, often without labels. *Representation control* then
adds or subtracts along that direction during the forward pass to steer the
model's behavior.

The paper presents RepE as a general toolkit and demonstrates it across a wide
range of safety-relevant phenomena: honesty and hallucination, utility
estimation, power-seeking, emotion, harmlessness, fairness and bias, knowledge
editing, and memorization. At the abstract level, reading vectors are shown to
flag when a model is producing a falsehood, and control vectors to increase or
decrease a targeted behavior, with the experiments run mostly on LLaMA-2 base and
chat models (Touvron et al., 2023). The headline quantitative result is on
honesty: an unsupervised RepE method reaches state-of-the-art on TruthfulQA, a
benchmark of questions where models tend to repeat human falsehoods (Lin et al.,
2021), improving over zero-shot accuracy by 18.1 percentage points on the
studied model.

**Threat Model:** RepE is a white-box transparency-and-control method, so the
relevant actor is whoever holds
[white-box access](../concepts/white-box-black-box.md) to the model's internal
activations: a developer or auditor who can read and write hidden states across
layers. The capability is twofold: read activations to locate a linear direction
for a target concept or function, and add or subtract that direction during the
forward pass to steer behavior, with no weight updates (optionally, light tuning
of representations). Stimulus design is typically unsupervised, using generic or
self-generated prompts rather than labeled examples. The claim is that high-level
cognitive phenomena are represented along directions that are both linearly
readable and causally effective when manipulated. The capability is dual-use by
construction: the same control that suppresses a behavior can amplify it, so
reading supports monitoring such as lie or hallucination detection, while control
can both strengthen and circumvent a model's safety behavior.

## Why read this

Interpretability is one of the few tools we have for learning how a model
actually works inside, and why it does what it does, rather than only what it
outputs. This paper is a high-profile entry in that program. It argues that
high-level notions such as honesty and harmfulness are encoded as directions in a
model's internal activations that can be both read and steered, and it shows that
this representation-level, top-down view already yields practical traction on
safety questions.

## Basic Background

### Language models and alignment

The models studied are autoregressive large language models, first
[pretrained](../concepts/language-model-pretraining.md) to predict the next token
over a large corpus and then turned into assistants by
[instruction tuning](../concepts/instruction-tuning.md) and preference
optimization such as [RLHF](../concepts/rlhf.md).
[Safety training](../concepts/safety-training.md) is the stage that makes a
deployed model refuse a designated set of restricted behaviors, and a
[jailbreak](../concepts/jailbreak.md) is a prompt or procedure that surfaces a
behavior safety training was meant to suppress. The paper's experiments use
LLaMA-2 base and chat models (Touvron et al., 2023).

### Distributed representations

A transformer stores a hidden-state vector for each token at each layer, and
information is spread across these activation patterns rather than localized in
single neurons; this is a
[distributed representation](../concepts/distributed-representations.md). These
activation spaces carry semantically meaningful, often linear, structure, so a
concept can correspond to a direction in the space. RepE takes these
representations as its unit of analysis.

### Reading internal state: probing and PCA

[Linear probing](../concepts/linear-probing.md) tests what a layer encodes by
training a simple classifier to predict a property from its activations.
Locating a concept's direction often reduces to finding the axis along which
contrasting inputs differ most, which is computed with
[principal component analysis](../concepts/principal-component-analysis.md).
RepE's reading step builds on this idea and aims to work without labels.

### Steering internal state: activation steering

[Activation steering](../concepts/activation-steering.md) changes a frozen
model's behavior at inference by adding a difference-of-activations vector to its
hidden states, with no weight updates. RepE's control step generalizes this
family of techniques.

### Interpretability paradigms

[Mechanistic interpretability](../concepts/mechanistic-interpretability.md) is
the bottom-up program that reverse-engineers a network into circuits of neurons
and features. The paper frames RepE against it using a distinction from cognitive
neuroscience: the Sherringtonian view, which sees cognition as node-to-node
connections between neurons, against the Hopfieldian view, which sees it as
patterns of activity across populations of neurons (Barack and Krakauer, 2021).

## Paper Context

By 2023, a long line of work had established that learned representations acquire
emergent, semantically meaningful structure. Word embeddings exhibit linear
analogies and reflect societal biases present in their training corpora (Mikolov
et al., 2013; Bolukbasi et al., 2016), and similar emergent structure had been
observed across vision and game-playing models. This made the premise that
directions in activation space carry meaning a credible starting point.

Several programs attacked the transparency problem from different angles.
Mechanistic interpretability sought to reverse-engineer networks into circuits,
identifying concrete mechanisms such as induction heads behind in-context
learning and a circuit for indirect object identification in GPT-2 (Olah et al.,
2020; Olsson et al., 2022; Wang et al., 2023). Probing classifiers tested what a
layer encodes by predicting properties from its activations (Alain and Bengio,
2017; Belinkov, 2022), and concept activation vectors defined a concept by a
direction in activation space (Kim et al., 2018).

A parallel line located, read, and edited concepts inside language models. Work
on locating and editing factual associations modified specific facts a model
stored (Meng et al., 2023). Other work found that models carry latent
representations of truthfulness even when they output falsehoods, recoverable
without labels by enforcing logical-consistency properties (Burns et al., 2022),
and that shifting activations along truthfulness-linked directions makes
generations more truthful (Li et al., 2023). Activation addition steered frozen
models by adding difference vectors to their hidden states (Turner et al., 2023).
These efforts were largely organized concept by concept, and the
representation-level view had no common name or shared baseline in machine
learning, in contrast with its established place in cognitive neuroscience
(Barack and Krakauer, 2021).

## Reading guidance

- Figure 2: the side-by-side of mechanistic interpretability (bottom-up) and
  representation engineering (top-down), mapped onto Marr's levels of analysis;
  the framing the rest of the paper instantiates.
- Section 3.1 (Representation Reading) and Figure 4: the LAT baseline and its
  three steps, designing the stimulus and task, collecting neural activity, and
  fitting a linear model. Note how much weight the stimulus-and-task template
  carries.
- Section 3.2 (Representation Control): the control baselines, including reading-
  vector addition and other transformations. Note which transformation is used
  where.
- Section 4 (Honesty): the in-depth example, including the distinction the paper
  draws between truthfulness and honesty, lie and hallucination detection, and
  honesty control; the TruthfulQA result lives here.
- Section 5 (Ethics and Power): utility, morality, power-aversion, and
  probability and risk, including the compositionality demonstration.
- Section 6 (Frontiers): emotion, harmlessness, bias and fairness, knowledge
  editing, and memorization, each a short demonstration rather than a full study.
- Appendix A: the explicit mechanistic-interpretability versus
  representation-reading contrast. Note how sharply the bottom-up and top-down
  line is drawn, and what is claimed about the limits of circuits.
- Across the applications, note how each target concept or function is turned
  into a concrete stimulus set, and how much of each result rests on that choice.

## Motivating questions

1. What does it mean to place representations, rather than neurons or circuits,
   at the center of analysis, and what does that choice aim to buy?
2. What are the two basic operations RepE offers, and what is each used for?
3. What kind of access to a model does representation engineering require?
4. Across the safety-relevant behaviors the paper touches, what is the common
   recipe, and where does the supervision, if any, come from?
5. What does the paper claim about the relationship between reading a concept's
   representation and being able to control it?

## Supplementary readings

- [Refusal in Language Models Is Mediated by a Single Direction](https://arxiv.org/abs/2406.11717) — a concrete instance of the representation-direction idea: locating a single direction that mediates refusal and ablating it to remove refusal behavior.
- [Improving Alignment and Robustness with Circuit Breakers](https://arxiv.org/abs/2406.04313) — uses representation control as a defense, interrupting the internal states that lead to harmful output rather than filtering inputs or outputs.

## References

- Alain, G. and Bengio, Y. "Understanding Intermediate Layers Using Linear
  Classifier Probes." International Conference on Learning Representations
  (ICLR), 2017.
- Barack, D. L. and Krakauer, J. W. "Two Views on the Cognitive Brain." Nature
  Reviews Neuroscience, 22(6):359–371, 2021.
- Belinkov, Y. "Probing Classifiers: Promises, Shortcomings, and Advances."
  Computational Linguistics, 48(1):207–219, 2022.
- Bolukbasi, T., Chang, K.-W., Zou, J. Y., Saligrama, V., and Kalai, A. T. "Man
  is to Computer Programmer as Woman is to Homemaker? Debiasing Word Embeddings."
  Advances in Neural Information Processing Systems (NeurIPS), 29, 2016.
- Burns, C., Ye, H., Klein, D., and Steinhardt, J. "Discovering Latent Knowledge
  in Language Models Without Supervision." 2022.
- Kim, B., Wattenberg, M., Gilmer, J., Cai, C., Wexler, J., Viégas, F., et al.
  "Interpretability Beyond Feature Attribution: Quantitative Testing with Concept
  Activation Vectors (TCAV)." International Conference on Machine Learning
  (ICML), 2018.
- Li, K., Patel, O., Viégas, F., Pfister, H., and Wattenberg, M. "Inference-Time
  Intervention: Eliciting Truthful Answers from a Language Model." 2023.
- Lin, S., Hilton, J., and Evans, O. "TruthfulQA: Measuring How Models Mimic
  Human Falsehoods." 2021. arXiv:2109.07958.
- Meng, K., Bau, D., Andonian, A., and Belinkov, Y. "Locating and Editing Factual
  Associations in GPT." 2023.
- Mikolov, T., Yih, W.-t., and Zweig, G. "Linguistic Regularities in Continuous
  Space Word Representations." North American Chapter of the Association for
  Computational Linguistics: Human Language Technologies (NAACL-HLT), 2013.
- Olah, C., Cammarata, N., Schubert, L., Goh, G., Petrov, M., and Carter, S.
  "Zoom In: An Introduction to Circuits." Distill, 2020.
- Olsson, C., Elhage, N., Nanda, N., Joseph, N., DasSarma, N., Henighan, T.,
  Mann, B., Askell, A., Bai, Y., Chen, A., et al. "In-Context Learning and
  Induction Heads." 2022. arXiv:2209.11895.
- Touvron, H., Martin, L., Stone, K., Albert, P., Almahairi, A., Babaei, Y.,
  Bashlykov, N., Batra, S., Bhargava, P., Bhosale, S., et al. "Llama 2: Open
  Foundation and Fine-Tuned Chat Models." 2023. arXiv:2307.09288.
- Turner, A., Thiergart, L., Udell, D., Leech, G., Mini, U., and MacDiarmid, M.
  "Activation Addition: Steering Language Models Without Optimization." 2023.
  arXiv:2308.10248.
- Wang, K. R., Variengien, A., Conmy, A., Shlegeris, B., and Steinhardt, J.
  "Interpretability in the Wild: A Circuit for Indirect Object Identification in
  GPT-2 Small." International Conference on Learning Representations (ICLR), 2023.
