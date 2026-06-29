---
title: "Knowledge Unlearning for Mitigating Privacy Risks in Language Models"
authors:
  - Jang, Joel
  - Yoon, Dongkeun
  - Yang, Sohee
  - Cha, Sungmin
  - Lee, Moontae
  - Logeswaran, Lajanugen
  - Seo, Minjoon
year: 2022
section: "Unlearning for Generative AI"
primary: true
arxiv: "2210.01504"
tags:
  - machine-unlearning
  - privacy
  - language-models
  - memorization
  - right-to-be-forgotten
---

---

### [Wiki Home](../README.md)

---

# Knowledge Unlearning for Mitigating Privacy Risks in Language Models

## High-level overview

A pretrained language model memorizes parts of its training corpus, personal
information included, and an extraction attack can recover some of it verbatim.
The standard privacy defenses, scrubbing the corpus before training and training
under differential privacy, both require retraining from scratch, which is
impractical each time an individual files a right-to-be-forgotten request. This
work proposes *knowledge unlearning*: a few gradient-ascent updates applied to
the already-trained model on the specific token sequences that must be forgotten,
no retraining.

Evaluated on GPT-Neo models (125M, 1.3B, 2.7B), the procedure suppresses the
targeted sequences against extraction attacks while leaving general capability,
measured on nine NLP classification benchmarks and four dialogue tasks, largely
intact for the larger models, and on some benchmarks slightly improving them. The
paper reports two further empirical patterns: forgetting sequences in sequential
chunks degrades the model less than forgetting them all at once, and how hard a
sequence is to forget depends heavily on its data domain, with structured text
such as code or email lists easier than unstructured prose. Set against a
deduplication defense and a differentially private decoding defense, unlearning
is reported to give stronger empirical privacy at far lower compute. The
protection is empirical: a sequence counts as forgotten once it is no more
extractable than data the model never trained on, with no formal certificate over
all possible examples.

**Threat Model:** The privacy adversary has access to the deployed language
model and mounts a targeted extraction attack: given a prefix of a sequence that
was in the training data, it samples a continuation and succeeds when the model
emits the true suffix verbatim. Varying the prefix length models attackers of
varying strength. The defender is the model owner, who holds a specific set of
token sequences that must be protected, the data named in a right-to-be-forgotten
request, assumed known a priori, and may edit the model's weights after training.
The defender's claim is empirical rather than formal: after unlearning, the
targeted sequences are no longer extractable, their extraction and memorization
scores having fallen to the level the model assigns to data it never saw, while
general capability is preserved. There is no (epsilon, delta) certificate over
all possible examples, only measured protection of the named sequences against
the extraction attack.

## Why read this

Unlearning is a central question for privacy compliance: regulations such as the
GDPR right to be forgotten can require removing an individual's data from a
deployed model, and retraining from scratch on every request is infeasible. This
paper is an early and widely cited case for doing that with a cheap post-hoc
edit, gradient ascent on the sequences to forget, and it reports that the edit
can preserve general capability. It is equally worth reading for what it exposes
about the method's limits: the protection it gives is empirical rather than a
formal guarantee, it degrades when many sequences are forgotten at once, and its
difficulty swings with the data domain, the properties that keep unlearning from
being a settled answer to the privacy problem.

## Basic Background

### Language models, the training objective, and gradient ascent

A [language model](../concepts/language-model-pretraining.md) is trained by
next-token prediction: it estimates the probability of each token given its
predecessors, and training minimizes the average negative log-likelihood of the
corpus by [stochastic gradient descent](../concepts/stochastic-gradient-descent.md).
Generation is autoregressive, drawing one token at a time under a
[decoding strategy](../concepts/decoding-strategies.md) such as greedy selection.
[Perplexity](../concepts/perplexity.md), the exponential of the per-token average
negative log-likelihood, measures how well a model predicts a sequence. Taking a
gradient step that *maximizes* a sequence's negative log-likelihood rather than
minimizing it is gradient ascent on that sequence: the same training machinery
run uphill. GPT-Neo (Black et al., 2021) is an openly released model of this
kind, pretrained on the Pile, an 825GB text corpus (Gao et al., 2020).

### Memorization and training-data extraction

A model [memorizes](../concepts/memorization.md) an example when its behavior
depends strongly on that example's presence in the training set, and large
language models memorize individual sequences verbatim even without overfitting
(Carlini et al., 2021). A
[training-data extraction attack](carlini-2021-extracting-training-data.md)
exploits this: prompt the model with a prefix and check whether it regenerates
the true continuation. Extraction is more targeted than
[membership inference](../concepts/membership-inference.md), which only decides
whether an example was in the training set (Shokri et al., 2017), and the amount
of extractable data grows as models scale (Carlini et al., 2022a).

### Machine unlearning and the right to be forgotten

[Machine unlearning](../concepts/machine-unlearning.md) removes the influence of
specified training data from an already-trained model without retraining from
scratch (Cao and Yang, 2015; Bourtoule et al., 2021). Its motivation is the
"right to be forgotten," the entitlement under data-protection regimes such as
the GDPR to have one's personal data deleted (Mantelero, 2013), which for a
deployed model means erasing the data's imprint on the parameters, not only the
stored records. Prior unlearning work mostly targeted image classifiers and
forgot whole classes (Golatkar et al., 2020); forgetting a specific token
sequence in a language model is a different regime.

### Differential privacy and data sanitization

The two standard privacy defenses for language models both act before or during
training. Data preprocessing scrubs identifiable information from the corpus with
parsers and classifiers (Aura et al., 2006); deduplicating the corpus before
training reduces how much is memorized (Kandpal et al., 2022).
[Differential privacy](../concepts/differential-privacy.md) instead bounds any
single example's influence on the trained model, with
[DP-SGD](abadi-2016-dp-sgd.md) as the deep-learning instantiation (Abadi et al.,
2016); for language models it can be applied during fine-tuning (Li et al., 2022;
Yu et al., 2022) or at decoding time (Majmudar et al., 2022). Both families
require committing to what counts as private before training, and retraining to
revise that choice.

## Reading guidance

- Section 1 (Introduction): the cost contrast in Figure 1, sanitization and DP
  retraining against a few token updates, and the right-to-be-forgotten framing.
- Section 2 (Related Work): the three lines the paper positions against, privacy
  methods for language models, machine unlearning, and memorization. Skim if the
  Basic Background above is familiar.
- Section 3.1 (Methodology): the unlearning objective is a single equation,
  gradient ascent on the target sequences. Note how short the method statement is
  relative to the analysis that follows.
- Section 3.2 (Quantifying privacy risks): the two metrics, Extraction Likelihood
  and Memorization Accuracy, and the empirical definition of when a sequence is
  forgotten. The threshold is set by comparison to validation data the model
  never saw; note exactly what that threshold is and what it does and does not
  certify.
- Section 4.1 (Setup): the two baselines (a deduplication model and a
  differentially private decoding model) and the Training Data Extraction
  Challenge data used as the sequences to forget.
- Section 4.2 (Main results): general-capability benchmarks before and after
  unlearning, by model size, and the sequential-versus-batch comparison.
- Section 4.3 and Table 4 (Domain analysis): forgetting difficulty and capability
  degradation broken down by data domain. Note which domains are reported as
  harder and the one-sentence hypothesis offered for why.
- Appendix B (Perplexity): perplexity rises after unlearning even where the
  benchmark accuracies do not; note the explanation given for the discrepancy.

<details>
<summary><h2>Paper Context</h2></summary>

By 2022 the privacy risk of language models was well documented. Extraction
attacks recovered verbatim training data, personally identifiable information
included, from production-scale models (Carlini et al., 2021); the amount
extractable grew with model size (Carlini et al., 2022a); and membership
inference (Shokri et al., 2017) had become a standard audit. Releasing
billion-parameter pretrained models for public use was routine (Gao et al., 2020;
Black et al., 2021; Zhang et al., 2022), which placed memorized private text in
many hands.

Two defense families addressed this, both acting at or before training. Corpus
sanitization and deduplication removed sensitive or repeated text before
pretraining (Aura et al., 2006; Dernoncourt et al., 2017; Lison et al., 2021;
Kandpal et al., 2022). Differential privacy bounded each example's influence
(Dwork et al., 2006), with DP-SGD as its deep-network form (Abadi et al., 2016)
and growing evidence it could fine-tune language models effectively (Li et al.,
2022; Yu et al., 2022), though private pretraining remained costly and slow to
converge (Anil et al., 2021). Both required retraining the model to act on any
new deletion request, prohibitive at scale, and both were argued to fit
natural-language privacy poorly, where what counts as private is context-dependent
and resists the fixed boundaries that sanitization and DP assume (Brown et al.,
2022).

Machine unlearning had emerged as an alternative to retraining for honoring
deletion requests (Cao and Yang, 2015; Ginart et al., 2019; Bourtoule et al.,
2021; Graves et al., 2021), motivated by the right to be forgotten (Mantelero,
2013; Villaronga et al., 2018). That work centered on image classification,
forgetting an entire class such as "cats" (Golatkar et al., 2020; Mehta et al.,
2022). A separate line recast forgetting as a relaxed form of differential
privacy and measured how much memorized training data a model sheds over
training, in image and audio models (Jagielski et al., 2022). These methods
forgot whole classes in classifiers; forgetting specific token sequences in a
large language model had not been studied.

</details>

### [Wiki Home](../README.md)

<details>
<summary><h4>References</h4></summary>

- Abadi, M., Chu, A., Goodfellow, I., McMahan, H.B., Mironov, I., Talwar, K., and
  Zhang, L. "Deep Learning with Differential Privacy." ACM SIGSAC Conference on
  Computer and Communications Security (CCS), 2016.
- Anil, R., Ghazi, B., Gupta, V., Kumar, R., and Manurangsi, P. "Large-Scale
  Differentially Private BERT." arXiv:2108.01624, 2021.
- Aura, T., Kuhn, T.A., and Roe, M. "Scanning Electronic Documents for Personally
  Identifiable Information." ACM Workshop on Privacy in the Electronic Society
  (WPES), 2006.
- Black, S., Gao, L., Wang, P., Leahy, C., and Biderman, S. "GPT-Neo: Large Scale
  Autoregressive Language Modeling with Mesh-Tensorflow." 2021.
- Bourtoule, L., Chandrasekaran, V., Choquette-Choo, C.A., Jia, H., Travers, A.,
  Zhang, B., Lie, D., and Papernot, N. "Machine Unlearning." IEEE Symposium on
  Security and Privacy (S&P), 2021.
- Brown, H., Lee, K., Mireshghallah, F., Shokri, R., and Tramèr, F. "What Does it
  Mean for a Language Model to Preserve Privacy?" arXiv:2202.05520, 2022.
- Cao, Y. and Yang, J. "Towards Making Systems Forget with Machine Unlearning."
  IEEE Symposium on Security and Privacy (S&P), 2015.
- Carlini, N., Tramèr, F., Wallace, E., Jagielski, M., Herbert-Voss, A., Lee, K.,
  Roberts, A., Brown, T., Song, D., Erlingsson, Ú., et al. "Extracting Training
  Data from Large Language Models." USENIX Security Symposium, 2021.
- Carlini, N., Ippolito, D., Jagielski, M., Lee, K., Tramèr, F., and Zhang, C.
  "Quantifying Memorization Across Neural Language Models." arXiv:2202.07646,
  2022.
- Dernoncourt, F., Lee, J.Y., Uzuner, O., and Szolovits, P. "De-identification of
  Patient Notes with Recurrent Neural Networks." Journal of the American Medical
  Informatics Association, 24(3), 2017.
- Dwork, C., McSherry, F., Nissim, K., and Smith, A. "Calibrating Noise to
  Sensitivity in Private Data Analysis." Theory of Cryptography Conference (TCC),
  2006.
- Gao, L., Biderman, S., Black, S., Golding, L., Hoppe, T., Foster, C., Phang, J.,
  He, H., Thite, A., Nabeshima, N., et al. "The Pile: An 800GB Dataset of Diverse
  Text for Language Modeling." arXiv:2101.00027, 2020.
- Ginart, A., Guan, M., Valiant, G., and Zou, J.Y. "Making AI Forget You: Data
  Deletion in Machine Learning." Advances in Neural Information Processing Systems
  (NeurIPS), 2019.
- Golatkar, A., Achille, A., and Soatto, S. "Eternal Sunshine of the Spotless
  Net: Selective Forgetting in Deep Networks." IEEE/CVF Conference on Computer
  Vision and Pattern Recognition (CVPR), 2020.
- Graves, L., Nagisetty, V., and Ganesh, V. "Amnesiac Machine Learning." AAAI
  Conference on Artificial Intelligence, 2021.
- Jagielski, M., Thakkar, O., Tramèr, F., Ippolito, D., Lee, K., Carlini, N.,
  Wallace, E., Song, S., Thakurta, A., Papernot, N., et al. "Measuring Forgetting
  of Memorized Training Examples." arXiv:2207.00099, 2022.
- Kandpal, N., Wallace, E., and Raffel, C. "Deduplicating Training Data Mitigates
  Privacy Risks in Language Models." arXiv:2202.06539, 2022.
- Li, X., Tramèr, F., Liang, P., and Hashimoto, T. "Large Language Models Can Be
  Strong Differentially Private Learners." International Conference on Learning
  Representations (ICLR), 2022.
- Lison, P., Pilán, I., Sánchez, D., Batet, M., and Øvrelid, L. "Anonymisation
  Models for Text Data: State of the Art, Challenges and Future Directions."
  Annual Meeting of the Association for Computational Linguistics (ACL), 2021.
- Majmudar, J., Dupuy, C., Peris, C., Smaili, S., Gupta, R., and Zemel, R.
  "Differentially Private Decoding in Large Language Models." arXiv:2205.13621,
  2022.
- Mantelero, A. "The EU Proposal for a General Data Protection Regulation and the
  Roots of the 'Right to be Forgotten'." Computer Law & Security Review, 29(3),
  2013.
- Mehta, R., Pal, S., Singh, V., and Ravi, S.N. "Deep Unlearning via Randomized
  Conditionally Independent Hessians." IEEE/CVF Conference on Computer Vision and
  Pattern Recognition (CVPR), 2022.
- Shokri, R., Stronati, M., Song, C., and Shmatikov, V. "Membership Inference
  Attacks Against Machine Learning Models." IEEE Symposium on Security and Privacy
  (S&P), 2017.
- Villaronga, E.F., Kieseberg, P., and Li, T. "Humans Forget, Machines Remember:
  Artificial Intelligence and the Right to be Forgotten." Computer Law & Security
  Review, 34(2), 2018.
- Yu, D., Naik, S., Backurs, A., Gopi, S., Inan, H.A., Kamath, G., Kulkarni, J.,
  Lee, Y.T., Manoel, A., Wutschitz, L., Yekhanin, S., and Zhang, H.
  "Differentially Private Fine-tuning of Language Models." International
  Conference on Learning Representations (ICLR), 2022.
- Zhang, S., Roller, S., Goyal, N., Artetxe, M., Chen, M., Chen, S., Dewan, C.,
  Diab, M., Li, X., Lin, X.V., et al. "OPT: Open Pre-trained Transformer Language
  Models." arXiv:2205.01068, 2022.

</details>
