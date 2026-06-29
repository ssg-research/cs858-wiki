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
  - safety
  - alignment
---

### [Wiki Home](../README.md)

# Representation Engineering: A Top-Down Approach to AI Transparency

## High-level overview

Large language models are deployed widely while their internal workings stay
mostly opaque, which limits any guarantee about whether a model is being honest,
whether it is about to produce harmful content, or whether it is reciting
memorized text. This paper names and characterizes **representation engineering
(RepE)**, a top-down approach to transparency that takes a network's
representations, the patterns of activation spread across many units, as the
unit of analysis. The contrast is with
[mechanistic interpretability](../concepts/mechanistic-interpretability.md),
which works bottom-up from individual neurons and circuits. The authors borrow a
framing from cognitive neuroscience, the Hopfieldian view that treats cognition
as a product of representational spaces rather than node-to-node connections, and
ask what it buys for monitoring and controlling high-level cognition in deep
networks.

RepE has two halves. **Representation reading** locates a high-level concept,
such as truthfulness, or a function, such as lying, as a
[linear direction](../concepts/linear-representation-hypothesis.md) in the
model's activations. The baseline method, Linear Artificial Tomography (LAT),
runs the model on a set of stimuli designed to vary the target concept, collects
the hidden activations, and fits a linear model to recover a "reading vector,"
a single direction that scores how much of the concept is present. **Representation
control** then [steers](../concepts/activation-steering.md) behavior by
manipulating that direction in the activations at inference: adding it,
subtracting it, projecting it out, or training a low-rank adapter (LoRRA) to
move representations toward a target. Reading and control reinforce each other,
since a direction that controls behavior when manipulated has stronger evidence
behind it than one that only correlates.

The paper presents RepE as a general toolkit and demonstrates it across a wide
span of safety-relevant targets: honesty and hallucination, utility estimation,
morality and power-aversion, emotion, harmlessness, bias and fairness, knowledge
editing, and memorization. The headline application is honesty. Reading a
model's internal concept of truthfulness yields a lie and hallucination detector,
and steering along the honesty direction, with no labeled data, reaches
state-of-the-art accuracy on TruthfulQA, an improvement of 18.1 percentage points
over zero-shot prompting and over all prior methods reported. Other
demonstrations include suppressing harmful outputs even under an adversarial
suffix, and reducing verbatim regurgitation of memorized quotations with little
loss of world knowledge.

**Threat Model:** RepE is a transparency setting in which the model's own
operator inspects and steers it. The analyst owns or studies the model and holds
[white-box](../concepts/white-box-black-box.md) access to it: the architecture,
the hidden activations at every layer and token, the ability to run chosen
prompts, and the ability to modify activations or attach an adapter at inference.
The claim is twofold. Reading claims that high-level concepts and functions
(truthfulness, morality, power-seeking, harmfulness, memorization, and more) are
recoverable as linear directions in those activations, supporting monitoring of
what a model is doing internally. Control claims that pushing the representation
along such a direction reliably moves the corresponding behavior, supporting
cheap inference-time steering toward attributes such as honesty or harmlessness.
The setting is post-training and primarily inference-time, with an optional light
fine-tuning step for the adapter variant; the evidence offered ranges from
correlation to causal manipulation, a distinction the paper makes explicit.

## Why read this

<!-- instructor: confirm -->
RepE names and systematizes a scattered set of techniques that read a concept as
a direction in a model's activations and then steer it, and shows that one simple
recipe carries across honesty, harmlessness, memorization, and more. The honesty
result shows that a model's internal sense of truthfulness is legible enough to
read off without labels and controllable enough to set a new state of the art on
TruthfulQA. The paper is a useful map of what
top-down interpretability can do today, and where its evidence stops at
correlation rather than mechanism.

## Basic Background

### Transformer language models and their activations

A language model is [pretrained](../concepts/language-model-pretraining.md) to
predict the next token over a large corpus, then often turned into an assistant
by [instruction tuning](../concepts/instruction-tuning.md) and preference
optimization. As a transformer processes text, it holds a hidden activation
vector at every layer and token position; these vectors are what RepE calls
"neural activity" and what its methods read and modify. Reaching them requires
[white-box](../concepts/white-box-black-box.md) access to the model, since they
are internal state rather than anything visible in the output text.

### Concepts as linear directions

The [linear representation hypothesis](../concepts/linear-representation-hypothesis.md)
holds that networks encode many high-level concepts as linear directions in
activation space, so a single vector scores how much of a concept is present. The
evidence goes back to semantic arithmetic in word embeddings (Mikolov et al.,
2013). Given activations collected across varied inputs, an unsupervised method
such as principal component analysis can recover a candidate direction without
labels; a supervised classifier can recover one from labeled examples.

### Reading and steering representations

A [linear probe](../concepts/linear-probing.md) is a linear classifier trained on
intermediate activations to test whether a property is linearly decodable, and
its weight vector is itself a concept direction (Alain and Bengio, 2017; Belinkov,
2022). [Contrastive prompt pairs](../concepts/contrastive-prompt-pairs.md) recover
a direction differently, by running two prompts that differ only in the target
concept and taking the difference of their activations.
[Activation steering](../concepts/activation-steering.md) then intervenes on the
activations at inference, adding, subtracting, or projecting out a direction to
change behavior without retraining (Turner et al., 2023; Li et al., 2023b).

### Bottom-up interpretability

The dominant program for understanding network internals,
[mechanistic interpretability](../concepts/mechanistic-interpretability.md),
reverse-engineers a network into circuits of individual neurons or features (Olah
et al., 2020; Olsson et al., 2022). It explains narrow capabilities in detail but
is largely manual and faces superposition, where neurons are polysemantic
(Elhage et al., 2022).

### Aligned models and the safety behaviors at issue

Deployed assistants are aligned by [RLHF](../concepts/rlhf.md) and given
[safety training](../concepts/safety-training.md) so they refuse a designated set
of restricted behaviors. A [jailbreak](../concepts/jailbreak.md) is a prompt that
routes around that refusal, and steering methods have also been used for
[red teaming](../concepts/red-teaming.md) and to reduce sycophancy (Rimsky,
2023a; Rimsky, 2023b). Separately, large models
[memorize](../concepts/memorization.md) and can emit verbatim training text
([training-data extraction](carlini-2021-extracting-training-data.md); Carlini et
al., 2021).

<details>
<summary><h2>Paper Context</h2></summary>

By 2023, evidence had accumulated that network internals are not the chaos they
appear to be. Word embeddings carry interpretable directions for semantic
relations and social biases (Mikolov et al., 2013; Bolukbasi et al., 2016), a
sentiment-tracking unit emerges from next-token training alone (Radford et al.,
2017), self-supervised vision models acquire segmentation and other structure
(Caron et al., 2021; Oquab et al., 2023), a network trained to play chess
acquires human chess concepts (McGrath et al., 2022), and a sequence model
trained on Othello transcripts builds an internal board representation (Li et al.,
2023a). This line suggested that representations had become structured enough to
study directly.

Interpretability had meanwhile pursued several routes with known limits. Saliency
maps highlight input regions a network attends to, but their reliability was
called into question (Simonyan et al., 2013; Adebayo et al., 2018). Mechanistic
interpretability reverse-engineers circuits of neurons and features (Olah et al.,
2020; Olsson et al., 2022; Wang et al., 2023), an approach that is largely manual,
has scaled mainly to narrow tasks, and contends with superposition (Elhage et al.,
2022); findings that networks compute by iterative refinement and tolerate the
removal of whole layers are in tension with a purely circuit-based account (Veit
et al., 2016). The split echoes a distinction in cognitive neuroscience between a
Sherringtonian view built on node-to-node connections and a Hopfieldian view
built on representational spaces (Barack and Krakauer, 2021), and a broader theme
that complex systems need analysis from the top down, not only the bottom up
(Anderson, 1972).

A parallel line located and manipulated concepts as directions. Linear probes
test what is decodable from activations (Alain and Bengio, 2017; Belinkov, 2022);
concept activation vectors and network dissection name directions and units for
human concepts (Kim et al., 2018; Bau et al., 2017); factual associations can be
located and edited inside LLMs (Meng et al., 2023a; Meng et al., 2023b), and
concept erasure removes a direction in closed form (Belrose et al., 2023). On the
control side, activation addition steers a model by adding a difference vector to
its activations with no optimization (Turner et al., 2023), inference-time
intervention steers a truthfulness direction to elicit truthful answers (Li et
al., 2023b), and similar steering was applied to red teaming and sycophancy
(Rimsky, 2023a; Rimsky, 2023b).

Truthfulness in particular had become its own thread. Models often encode the
correct answer internally even as they generate a falsehood: latent-knowledge
methods recover a truth direction without labels (Burns et al., 2022) and
classifiers on hidden states detect when a statement is a lie (Azaria and
Mitchell, 2023), while TruthfulQA measures how often models reproduce common human
falsehoods (Lin et al., 2021). The methods existed in scattered form; what had
not been done was to characterize them as one area, supply stronger baselines for
reading and control, and test the same recipe across a broad set of
safety-relevant concepts.

</details>

## Reading guidance

- Section 1 and Figure 2: the top-down versus bottom-up framing and the
  Hopfieldian analogy that motivates the whole approach.
- Section 3.1.1 and Figure 4: the LAT pipeline, from designing stimuli to
  collecting activations to fitting a linear model. Note the default design
  choices and how the reading direction is recovered.
- Section 3.1.2: the four evaluation types (correlation, manipulation,
  termination, recovery). Note which categories the paper's experiments mostly
  occupy, and what each category licenses one to conclude.
- Section 3.2 and Algorithm 1: the control baselines (reading vector, contrast
  vector, LoRRA) and the three operators (linear combination, piece-wise,
  projection).
- Section 4 and Table 1: honesty as the in-depth example, and the TruthfulQA
  result. Note that Section 4.2 separates "truthfulness" from "honesty"; track how
  each is defined and which one the lie-detection results speak to.
- Sections 5 and 6: the breadth tour across utility, morality, power-aversion,
  emotion, harmlessness, bias, knowledge editing, and memorization. Read for the
  recurring pattern rather than each number.
- Appendix A: the explicit contrast between mechanistic interpretability and
  representation reading.

<details>
<summary><h2>Supplementary readings</h2></summary>

- [Refusal in Language Models Is Mediated by a Single Direction](https://arxiv.org/abs/2406.11717) — a sharp instance of the RepE thesis: one safety-relevant behavior, refusal, turns out to be governed by a single direction that can be read and steered.
- [Improving Alignment and Robustness with Circuit Breakers](https://arxiv.org/abs/2406.04313) — a defense built by operating on representations, remapping harmful internal states, an application of representation control to robustness.

</details>

### [Wiki Home](../README.md)

<details>
<summary><h2>References</h2></summary>

- Adebayo, J., Gilmer, J., Muelly, M., Goodfellow, I., Hardt, M., and Kim, B.
  "Sanity Checks for Saliency Maps." Advances in Neural Information Processing
  Systems (NeurIPS), 31, 2018.
- Alain, G. and Bengio, Y. "Understanding Intermediate Layers Using Linear
  Classifier Probes." International Conference on Learning Representations (ICLR),
  2017.
- Anderson, P. W. "More Is Different." Science, 177(4047), 1972.
- Azaria, A. and Mitchell, T. "The Internal State of an LLM Knows When It's
  Lying." 2023.
- Barack, D. L. and Krakauer, J. W. "Two Views on the Cognitive Brain." Nature
  Reviews Neuroscience, 22(6), 2021.
- Bau, D., Zhou, B., Khosla, A., Oliva, A., and Torralba, A. "Network Dissection:
  Quantifying Interpretability of Deep Visual Representations." IEEE Conference on
  Computer Vision and Pattern Recognition (CVPR), 2017.
- Belinkov, Y. "Probing Classifiers: Promises, Shortcomings, and Advances."
  Computational Linguistics, 48(1), 2022.
- Belrose, N., Schneider-Joseph, D., Ravfogel, S., Cotterell, R., Raff, E., and
  Biderman, S. "LEACE: Perfect Linear Concept Erasure in Closed Form."
  arXiv:2306.03819, 2023.
- Bolukbasi, T., Chang, K.-W., Zou, J. Y., Saligrama, V., and Kalai, A. T. "Man
  is to Computer Programmer as Woman is to Homemaker? Debiasing Word Embeddings."
  Advances in Neural Information Processing Systems (NeurIPS), 29, 2016.
- Burns, C., Ye, H., Klein, D., and Steinhardt, J. "Discovering Latent Knowledge
  in Language Models Without Supervision." 2022.
- Caron, M., Touvron, H., Misra, I., Jégou, H., Mairal, J., Bojanowski, P., and
  Joulin, A. "Emerging Properties in Self-Supervised Vision Transformers." 2021.
- Carlini, N., Tramèr, F., Wallace, E., Jagielski, M., Herbert-Voss, A., Lee, K.,
  Roberts, A., Brown, T., Song, D., Erlingsson, Ú., et al. "Extracting Training
  Data from Large Language Models." USENIX Security Symposium, 2021.
- Elhage, N., Hume, T., Olsson, C., Schiefer, N., Henighan, T., Kravec, S.,
  Hatfield-Dodds, Z., Lasenby, R., Drain, D., Chen, C., et al. "Toy Models of
  Superposition." Transformer Circuits Thread, 2022.
- Kim, B., Wattenberg, M., Gilmer, J., Cai, C., Wexler, J., Viegas, F., et al.
  "Interpretability Beyond Feature Attribution: Quantitative Testing with Concept
  Activation Vectors (TCAV)." International Conference on Machine Learning (ICML),
  2018.
- Li, K., Hopkins, A. K., Bau, D., Viégas, F., Pfister, H., and Wattenberg, M.
  "Emergent World Representations: Exploring a Sequence Model Trained on a
  Synthetic Task." International Conference on Learning Representations (ICLR),
  2023a.
- Li, K., Patel, O., Viégas, F., Pfister, H., and Wattenberg, M. "Inference-Time
  Intervention: Eliciting Truthful Answers from a Language Model." 2023b.
- Lin, S., Hilton, J., and Evans, O. "TruthfulQA: Measuring How Models Mimic Human
  Falsehoods." arXiv:2109.07958, 2021.
- McGrath, T., Kapishnikov, A., Tomašev, N., Pearce, A., Wattenberg, M., Hassabis,
  D., Kim, B., Paquet, U., and Kramnik, V. "Acquisition of Chess Knowledge in
  AlphaZero." Proceedings of the National Academy of Sciences, 119(47), 2022.
- Meng, K., Bau, D., Andonian, A., and Belinkov, Y. "Locating and Editing Factual
  Associations in GPT." 2023a.
- Meng, K., Sen Sharma, A., Andonian, A., Belinkov, Y., and Bau, D. "Mass-Editing
  Memory in a Transformer." 2023b.
- Mikolov, T., Yih, W.-t., and Zweig, G. "Linguistic Regularities in Continuous
  Space Word Representations." Proceedings of NAACL-HLT, 2013.
- Olah, C., Cammarata, N., Schubert, L., Goh, G., Petrov, M., and Carter, S. "Zoom
  In: An Introduction to Circuits." Distill, 2020.
- Olsson, C., Elhage, N., Nanda, N., Joseph, N., DasSarma, N., Henighan, T., Mann,
  B., Askell, A., Bai, Y., Chen, A., et al. "In-context Learning and Induction
  Heads." arXiv:2209.11895, 2022.
- Oquab, M., Darcet, T., Moutakanni, T., Vo, H. V., Szafraniec, M., Khalidov, V.,
  Fernandez, P., Haziza, D., Massa, F., El-Nouby, A., et al. "DINOv2: Learning
  Robust Visual Features Without Supervision." 2023.
- Radford, A., Jozefowicz, R., and Sutskever, I. "Learning to Generate Reviews and
  Discovering Sentiment." arXiv:1704.01444, 2017.
- Rimsky, N. "Modulating Sycophancy in an RLHF Model via Activation Steering." AI
  Alignment Forum, 2023a.
- Rimsky, N. "Red-teaming Language Models via Activation Engineering." AI
  Alignment Forum, 2023b.
- Simonyan, K., Vedaldi, A., and Zisserman, A. "Deep Inside Convolutional
  Networks: Visualising Image Classification Models and Saliency Maps."
  arXiv:1312.6034, 2013.
- Turner, A., Thiergart, L., Udell, D., Leech, G., Mini, U., and MacDiarmid, M.
  "Activation Addition: Steering Language Models Without Optimization."
  arXiv:2308.10248, 2023.
- Veit, A., Wilber, M. J., and Belongie, S. "Residual Networks Behave Like
  Ensembles of Relatively Shallow Networks." Advances in Neural Information
  Processing Systems (NeurIPS), 29, 2016.
- Wang, K. R., Variengien, A., Conmy, A., Shlegeris, B., and Steinhardt, J.
  "Interpretability in the Wild: a Circuit for Indirect Object Identification in
  GPT-2 Small." International Conference on Learning Representations (ICLR), 2023.

</details>
