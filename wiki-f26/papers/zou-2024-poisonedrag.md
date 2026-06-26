---
title: "PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented Generation of Large Language Models"
authors:
  - Zou, Wei
  - Geng, Runpeng
  - Wang, Binghui
  - Jia, Jinyuan
year: 2024
section: "Preference Manipulation / RAG Poisoning"
primary: true
arxiv: "2402.07867"
tags:
  - poisoning
  - retrieval
  - llm
  - attack
---

### [Wiki Home](../README.md)

# PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented Generation of Large Language Models

## High-level overview

[Retrieval-augmented generation](../concepts/retrieval-augmented-generation.md)
(RAG) answers a question by retrieving relevant texts from a knowledge database
and placing them in a language model's context, so the model grounds its answer
in retrieved text rather than its fixed training knowledge. This paper asks what happens when that knowledge database
is not trusted. It introduces PoisonedRAG, presented as the first knowledge
corruption attack on RAG: an adversary inserts a small number of crafted texts
into the corpus so that, for a question the adversary chose in advance (the
"target question"), the system returns an answer the adversary chose in advance
(the "target answer"). The worked example throughout is making the system
answer "Tim Cook" to "Who is the CEO of OpenAI?".

An injected text succeeds only if it is retrieved for the target question and,
once in the context, steers the model to the target answer. The paper crafts
texts that do both, under two assumptions about the adversary's knowledge of
the retriever: black-box (no access to the retriever's parameters, the main and
stronger setting) and white-box. Reported results, at the level of the
abstract, are high attack success rates from injecting only a handful of texts
per target question into databases holding millions of texts: 97% on the
Natural Questions dataset from five texts per question against a corpus of
roughly 2.7 million clean texts. The attack holds across several
question-answering datasets and language models, and against several
input-level defenses.

This differs from [prompt injection](../concepts/prompt-injection.md), with
which it is easily confused. Prompt injection smuggles *instructions* into
content the model reads ("ignore your task and output X"); PoisonedRAG injects
*misleading content* that reads as ordinary text, so the model is misled by
what it treats as a credible retrieved fact rather than by a hidden command.

**Threat Model:** The adversary picks one or more target questions and a target
answer for each, then injects a few malicious texts into the RAG knowledge
database, for instance by editing a public source the corpus is built from or
through insider write access to a private one. The adversary cannot read the
other (clean) texts in the database and cannot access or query the language
model. Knowledge of the retriever splits the settings: in the black-box setting
the adversary cannot access the retriever's parameters or query it (the paper's
main, stronger assumption); in the white-box setting the adversary holds the
retriever's parameters, which the paper motivates by the common practice of
deploying a publicly available retriever. The corruption is placed into the
corpus ahead of time and retrieved at inference, acting on the data the deployed
system consults rather than on training or on the user's prompt. The defender,
the party running input-level defenses the paper evaluates, aims to detect or
neutralize the injected texts.

## Why read this

This is the first attack to poison a large-language-model system by corrupting
its knowledge base rather than its training data, and it lands the corruption at
an unusual point in the lifecycle: after training, yet not at inference-time
prompting either, but in the retrieval corpus the deployed system consults. It
rewards thinking about the whole system rather than the model in isolation, since
the vulnerable component is the data pipeline feeding the model.

## Basic Background

### Retrieval-augmented generation and dense retrieval

A language model's knowledge is fixed at the end of
[pretraining](../concepts/language-model-pretraining.md), so it cannot answer
about events after its cutoff and may fabricate plausible-sounding but false
statements. [Retrieval-augmented generation](../concepts/retrieval-augmented-generation.md)
mitigates this by fetching relevant documents from an external knowledge database
at inference time and putting them in the model's context window, so the answer
is grounded in retrieved text. The component that decides which documents are
fetched is the retriever. Modern RAG uses
[dense retrieval](../concepts/dense-retrieval.md): a query and each passage are
embedded into vectors by learned encoders, relevance is the similarity of those
vectors, and the top-k most similar passages are returned. Understanding that the
corpus is consulted at inference, and that retrieval is decided by embedding
similarity, is the prerequisite for everything in this paper.

### Data poisoning and the new attack surface

[Data poisoning](../concepts/data-poisoning.md) is the classical attack of
corrupting the data a model learns from so the trained model misbehaves;
[backdoor attacks](../concepts/backdoor-attacks.md) are the trigger-conditioned
subclass. In all of these the corrupted data is the training set. This paper
moves the same idea to a different surface: the inference-time knowledge base of
a deployed RAG system, which no model is trained on but every answer depends on.

### Attacks that steer LLMs through their inputs

Two adjacent attack families act through what a model reads rather than how it
was trained. [Prompt injection](../concepts/prompt-injection.md) places
adversarial instructions in the prompt or in ingested content to override the
intended task. A [jailbreak](../concepts/jailbreak.md) crafts input that elicits
behavior the model was trained to refuse. Both are worth holding in mind as
contrasts: PoisonedRAG steers the answer with misleading content treated as a
fact, not with instructions or a refusal bypass.

### Adversary knowledge and adversarial text

Attacks are specified partly by what the adversary knows, along the
[white-box / black-box](../concepts/white-box-black-box.md) spectrum, from full
model parameters and gradients down to query-only or no access. When the
retriever's parameters are available, making a text rank for a target query
becomes the problem of crafting an
[adversarial example](../concepts/adversarial-examples.md) in text, optimized so
the retriever scores it as similar to the query; such crafted inputs often
[transfer](../concepts/transferability.md) across models built for the same task.

### Detecting and evaluating injected text

One defense family asks whether a text looks machine-generated or anomalous.
[Perplexity](../concepts/perplexity.md) measures how well a language model
predicts a text and is used as a quality and anomaly signal: unusually high
perplexity can flag adversarially crafted text. Detectors that threshold such a
score are evaluated with [ROC curves and AUC](../concepts/roc-curves.md), reading
the true-positive rate against the false-positive rate, since a detector that
only works at a high false-positive rate is not deployable.

<details>
<summary><h2>Paper Context</h2></summary>

By 2024, RAG was an established technique for grounding language models in
external text (Lewis et al., 2020), built on dense retrievers such as Dense
Passage Retrieval (Karpukhin et al., 2020), and was widely deployed in
search-augmented chatbots and document assistants. Research on RAG had
concentrated on making retrieval more accurate or more efficient; the security
of the knowledge database itself had drawn little attention.

The known attacks on language models acted elsewhere in the system. Prompt
injection placed adversarial instructions in the prompt or in retrieved content
to hijack the task ([Greshake et al., 2023](greshake-2023-indirect-prompt-injection.md);
Liu et al., 2024), and jailbreaking crafted inputs that bypassed safety refusals
([Wei et al., 2023](wei-2023-jailbroken.md); Zou et al., 2023). These manipulate
the model's instruction-following or safety behavior rather than the factual
content it is given as context. Closest to the retrieval surface, Zhong et al.
(2023) showed that adversarial passages can be crafted so a dense retriever
returns them for many queries, but those passages were not designed to make the
model produce a specific attacker-chosen answer.

Data poisoning and backdoor attacks had a long history in machine learning
(Biggio et al., 2012; Gu et al., 2017), but classically corrupted the training
set of a model. Whether that lever even reaches a RAG system is unclear when the
model and retriever are large pretrained components released by major vendors.
Separately, work on web-scale corpora argued that injecting content into the
sources these systems draw from is practical, including editing a non-trivial
fraction of Wikipedia (Carlini et al., 2023). Input-level defenses developed for
prompt injection and jailbreaks, such as paraphrasing the input and
perplexity-based detection (Jain et al., 2023; Alon and Kamfonas, 2023),
existed but had not been examined against corruption of a retrieval corpus.

</details>

## Reading guidance

- Section 3.1 (threat model): pin down exactly what the attacker is denied (the
  other texts in the database, any access to the LLM) versus granted (the
  retriever, in the white-box setting). The strength of the result rests on how
  little is assumed.
- Section 4.1: the two necessary conditions, retrieval and generation, and the
  idea of splitting an injected text into two parts that serve them.
- Section 4.2.1: how the part responsible for the generation condition is
  produced (an LLM is used to write it).
- Section 4.2.2: how the retrieval condition is met. In the black-box setting the
  design choice is to set the retrieval part equal to the target question itself;
  note the one-line justification for that choice and how much of the attack's
  success rides on it. The white-box setting instead optimizes embedding
  similarity directly.
- Section 5: the Attack Success Rate metric, the datasets, the language models,
  and the baselines the attack is compared against.
- Section 7 (defenses): paraphrasing, perplexity-based detection, duplicate
  filtering, and knowledge expansion. For the perplexity detector, look at the
  ROC curve and AUC in Figure 6 and note what the value implies about how
  separable the injected texts are from clean ones.
- Appendix Tables 23-25: example target questions, target answers, and the
  malicious texts produced. Reading one shows concretely what an injected text
  looks like.

<details>
<summary><h2>Supplementary readings</h2></summary>

- [Adversarial Search Engine Optimization for Large Language Models](https://arxiv.org/abs/2406.18382) — manipulating the content an LLM retrieves so it favors an attacker's preferred answer, a related angle on corrupting what the model reads.
- [Certifiably Robust RAG against Retrieval Corruption](https://arxiv.org/abs/2405.15556) — a defense direction aimed at exactly this class of attack, giving guarantees when a bounded number of retrieved passages are malicious.

</details>

### [Wiki Home](../README.md)

<details>
<summary><h2>References</h2></summary>

- Zou, W., Geng, R., Wang, B., and Jia, J. "PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented Generation of Large Language Models." 2024. arXiv:2402.07867.
- Lewis, P., Perez, E., Piktus, A., Petroni, F., Karpukhin, V., Goyal, N., Küttler, H., Lewis, M., Yih, W.-t., Rocktäschel, T., et al. "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks." NeurIPS, 2020.
- Karpukhin, V., Oguz, B., Min, S., Lewis, P., Wu, L., Edunov, S., Chen, D., and Yih, W.-t. "Dense Passage Retrieval for Open-Domain Question Answering." EMNLP, 2020.
- Zhong, Z., Huang, Z., Wettig, A., and Chen, D. "Poisoning Retrieval Corpora by Injecting Adversarial Passages." EMNLP, 2023.
- Greshake, K., Abdelnabi, S., Mishra, S., Endres, C., Holz, T., and Fritz, M. "Not What You've Signed Up For: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection." AISec, 2023.
- Liu, Y., Jia, Y., Geng, R., Jia, J., and Gong, N.Z. "Formalizing and Benchmarking Prompt Injection Attacks and Defenses." 2024. arXiv:2310.12815.
- Wei, A., Haghtalab, N., and Steinhardt, J. "Jailbroken: How Does LLM Safety Training Fail?" NeurIPS, 2023.
- Zou, A., Wang, Z., Kolter, J.Z., and Fredrikson, M. "Universal and Transferable Adversarial Attacks on Aligned Language Models." 2023. arXiv:2307.15043.
- Biggio, B., Nelson, B., and Laskov, P. "Poisoning Attacks against Support Vector Machines." ICML, 2012.
- Gu, T., Dolan-Gavitt, B., and Garg, S. "BadNets: Identifying Vulnerabilities in the Machine Learning Model Supply Chain." IEEE Access, 2017. arXiv:1708.06733.
- Carlini, N., Jagielski, M., Choquette-Choo, C.A., Paleka, D., Pearce, W., Anderson, H., Terzis, A., Thomas, K., and Tramèr, F. "Poisoning Web-Scale Training Datasets Is Practical." 2023. arXiv:2302.10149.
- Jain, N., Schwarzschild, A., Wen, Y., Somepalli, G., Kirchenbauer, J., Chiang, P.-y., Goldblum, M., Saha, A., Geiping, J., and Goldstein, T. "Baseline Defenses for Adversarial Attacks Against Aligned Language Models." 2023. arXiv:2309.00614.
- Alon, G., and Kamfonas, M. "Detecting Language Model Attacks with Perplexity." 2023. arXiv:2308.14132.

</details>
