---
title: "Not what you've signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection"
authors:
  - Greshake, Kai
  - Abdelnabi, Sahar
  - Mishra, Shailesh
  - Endres, Christoph
  - Holz, Thorsten
  - Fritz, Mario
year: 2023
section: "Indirect Prompt Injection in AI Agents"
primary: true
arxiv: "2302.12173"
tags:
  - prompt-injection
  - llm-safety
  - attack
---

### [Wiki Home](../README.md)

# Not what you've signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection

## High-level overview

Large language models are increasingly wrapped inside applications that
[retrieve documents](../concepts/retrieval-augmented-generation.md) and
[call external tools](../concepts/llm-tool-use.md): search-augmented chatbots,
code assistants, email and office copilots, browser plugins. The paper observes
that retrieval blurs the line between data and instructions, since retrieved
text and the developer's instructions share one context window.

It introduces and names **indirect prompt injection**. Rather than typing a
malicious prompt into a model they control, the adversary plants instructions
inside content likely to be retrieved, such as a web page, an email, or a code
repository, and waits for a victim's model to ingest it. Once ingested, the
injected text steers the model toward adversary-chosen actions. The paper frames
this in classical computer-security terms: processing untrusted retrieved data
is analogous to arbitrary code execution, where the "code" is natural-language
instructions. From this it derives a taxonomy, organized from a security rather
than an ML perspective, of how injections are delivered, what harms they cause,
and who is affected.

The paper demonstrates the attacks against deployed, black-box systems,
including Bing Chat (then GPT-4 backed) and GitHub Copilot, and against
synthetic GPT-4 applications the authors built with search, email, memory, and
HTTP tools. The demonstrations are qualitative proofs of concept: injected
instructions exfiltrate user data, persist across sessions through a memory
store, spread between email clients as a worm, and pass input filters when
encoded in Base64. Effective mitigations are reported to be lacking.

**Threat Model:** The adversary is a third party who controls some content a
victim's LLM-integrated application may retrieve or be handed, such as a web
page, an email, a document, or a memory entry, and who never interacts with the
victim's interface. Access to the target model is
[black-box](../concepts/white-box-black-box.md): no weights, gradients, or
training data, and the adversary need not query the model at all, since they
plant the payload and wait for retrieval. The capability is to write
natural-language or encoded instructions into that content, hidden from a human
reader through HTML comments, invisible text, or encoding. The attack acts at
inference time, when the content is ingested, and the injected instructions can
persist across conversation turns and, through a memory store, across sessions.
The targets are the application's users and any APIs the model can call on their
behalf. The defender is the application provider, whose deployed input and output
filtering is shown not to cover instructions that arrive indirectly.

## Why read this

This is the paper that introduced and named indirect prompt injection. It
reframes the LLM trust boundary: once a model retrieves documents or calls tools,
third-party content it ingests, not only the user typing the prompt, can hijack
its behavior. The contribution is a way of seeing, importing a full
computer-security vocabulary, arbitrary code execution, worms, persistence, and
command-and-control, into LLM-integrated applications.

## Basic Background

### Large language models and alignment

A modern LLM is pretrained to predict the next token over a large corpus
([language model pretraining](../concepts/language-model-pretraining.md)), then
adapted to follow requests through
[instruction tuning](../concepts/instruction-tuning.md) and
[reinforcement learning from human feedback](../concepts/rlhf.md) (RLHF). A later
[safety-training](../concepts/safety-training.md) stage trains the deployed model
to refuse a set of restricted behaviors. The model is steered entirely through
natural-language input, which is what makes it reprogrammable at inference time.

### Prompt injection and jailbreaks

[Prompt injection](../concepts/prompt-injection.md) supplies instructions that
override an application's intended task. Direct injection comes from the user of
the model; the class this paper introduces is indirect, hiding the instructions
in content the model later reads. A [jailbreak](../concepts/jailbreak.md) is the
related move of eliciting a behavior the model was safety-trained to refuse. Both
steer the model through its input, and the paper uses jailbreak-style payloads as
one kind of indirect injection.

### LLM-integrated applications

The setting is the application built around an LLM.
[Retrieval augmentation](../concepts/retrieval-augmented-generation.md) places
text from a search index, a document store, or the open web into the model's
context at inference time. [Tool use](../concepts/llm-tool-use.md) lets the model
emit calls to external functions, search, HTTP requests, email, memory, and act
on their results; chaining such calls toward a goal with little oversight is what
is meant by an "agent." Both pull untrusted external text into the same context
window as the developer's instructions.

### Black-box access

The deployed targets are reached through their interfaces only, with no view of
weights, gradients, or training data
([black-box access](../concepts/white-box-black-box.md)). Indirect injection
relaxes the access requirement further: the attacker influences the model without
querying it, by seeding content the victim's model will retrieve.

## Reading guidance

- **Section 2 (Preliminaries and Related Work).** The building blocks: tool-augmented and agentic LLMs, prior prompt injection, and the "LLMs as computers" analogy the threat model rests on.
- **Section 3 (Attack surface and taxonomy).** The taxonomy itself, injection methods, threats, and affected parties (Figure 2), with "Key Message" boxes stating the claims. The taxonomy is adapted from an existing cyber-threat taxonomy; note where a threat is demonstrated versus asserted as conceivable.
- **Section 4 (Evaluation and demonstrations).** Proof-of-concept attacks on synthetic GPT-4 apps and on Bing Chat and Copilot, grouped by threat. These are qualitative; note how success is judged for a dynamic, interactive chat session. Sections 4.1 and 5.2 state what was tested on real systems versus synthetic mock-ups, and why public injections were avoided; note the boundary.
- **Section 5 (Discussion and mitigations).** Ethics and disclosure, limitations, and candidate defenses (input filtering, a less-capable sanitizing model, an LLM supervisor, interpretability-based detection). Note which defenses are proposed versus evaluated.
- **Figures 4-9.** The per-attack data-flow diagrams; each shows where the injection enters and how data or control returns to the attacker.
- **Appendix (prompts and outputs).** The actual injection prompts and model transcripts; the strongest real-world payloads were deliberately withheld.

<details>
<summary><h2>Supplementary readings</h2></summary>

- [InjecAgent: Benchmarking Indirect Prompt Injections in Tool-Integrated LLM Agents](https://arxiv.org/abs/2403.02691) — a benchmark that quantifies indirect prompt injection against tool-using agents, the measurement this paper leaves to future work.
- [Formalizing and Benchmarking Prompt Injection Attacks and Defenses](https://arxiv.org/abs/2310.12815) — a formal framework and shared benchmark unifying prompt-injection attacks with candidate defenses.

</details>

<details>
<summary><h2>Paper Context</h2></summary>

By early 2023, attacks on LLMs through their prompts were documented under the
assumption that the attacker is the user. Prompt injection was shown to override
an application's instructions and leak its hidden prompt (Perez and Ribeiro,
2022). Treating the model through a computer-security lens, contemporaneous work
synergized LLMs with classical attacks, deriving program obfuscation, payload
splitting, and virtualization to bypass content filters (Kang et al., 2023),
building on the view of an LLM as a black-box computer that executes programs
written in natural language (Jojic et al., 2023). Jailbreaking circulated both as
folklore and as a research subject, and providers reported that GPT-4 reduced but
did not remove it (OpenAI, 2023).

In the same period LLMs were being wrapped into applications at speed. Tool
augmentation taught models to call external APIs, by learned self-supervision
(Schick et al., 2023) or by interleaving reasoning and acting in the prompt (Yao
et al., 2023; Wei et al., 2022). More autonomous designs let a model plan and
execute multi-step tasks with little human oversight (Park et al., 2023; Liang et
al., 2023; Shen et al., 2023). These systems extended what a model could reach,
search engines, email, code, and arbitrary HTTP endpoints, but their exposure to
untrusted retrieved input had not been examined.

Adversarial machine learning had concentrated on gradient-based evasion of
classifiers, and a position line argued that this research had drifted from how
real attackers operate (Apruzzese et al., 2022). Adjacent work showed that a
model's function could be hijacked toward an attacker's task (Salem et al., 2022)
and that language models could be backdoored to push propaganda (Bagdasaryan and
Shmatikov, 2022). The main mitigation lever for unwanted behavior was alignment:
instruction tuning and RLHF for helpfulness and harmlessness (Ouyang et al.,
2022; Stiennon et al., 2020; Bai et al., 2022). These mitigations were built
around a user prompting the model directly; instructions reaching the model
through retrieved data fell outside that picture of the threat.

</details>

### [Wiki Home](../README.md)

<details>
<summary><h4>References</h4></summary>

Entries read off the paper's bibliography (arXiv 2302.12173, pages 13-14).

- Apruzzese, G., Anderson, H., Dambra, S., Freeman, D., Pierazzi, F., and Roundy,
  K. "Position: 'Real Attackers Don't Compute Gradients': Bridging the Gap
  Between Adversarial ML Research and Practice." IEEE Conference on Secure and
  Trustworthy Machine Learning (SaTML), 2022.
- Bagdasaryan, E., and Shmatikov, V. "Spinning Language Models: Risks of
  Propaganda-As-A-Service and Countermeasures." IEEE Symposium on Security and
  Privacy (S&P), 2022.
- Bai, Y., Jones, A., Ndousse, K., Askell, A., Chen, A., DasSarma, N., Drain, D.,
  Fort, S., Ganguli, D., Henighan, T., et al. "Training a Helpful and Harmless
  Assistant with Reinforcement Learning from Human Feedback." arXiv preprint,
  2022.
- Jojic, A., Wang, Z., and Jojic, N. "GPT is Becoming a Turing Machine: Here are
  Some Ways to Program It." arXiv preprint, 2023.
- Kang, D., Li, X., Stoica, I., Guestrin, C., Zaharia, M., and Hashimoto, T.
  "Exploiting Programmatic Behavior of LLMs: Dual-Use Through Standard Security
  Attacks." arXiv:2302.05733, 2023.
- Liang, Y., Wu, C., Song, T., Wu, W., Xia, Y., Liu, Y., Ou, Y., Lu, S., Ji, L.,
  Mao, S., et al. "TaskMatrix.AI: Completing Tasks by Connecting Foundation
  Models with Millions of APIs." arXiv preprint, 2023.
- OpenAI. "GPT-4 Technical Report." arXiv:2303.08774, 2023.
- Ouyang, L., Wu, J., Jiang, X., Almeida, D., Wainwright, C., Mishkin, P., Zhang,
  C., Agarwal, S., Slama, K., Gray, A., et al. "Training Language Models to
  Follow Instructions with Human Feedback." Advances in Neural Information
  Processing Systems (NeurIPS), 2022.
- Park, J. S., O'Brien, J. C., Cai, C. J., Morris, M. R., Liang, P., and
  Bernstein, M. S. "Generative Agents: Interactive Simulacra of Human Behavior."
  arXiv preprint, 2023.
- Perez, F., and Ribeiro, I. "Ignore Previous Prompt: Attack Techniques For
  Language Models." NeurIPS ML Safety Workshop, 2022.
- Salem, A., Backes, M., and Zhang, Y. "Get a Model! Model Hijacking Attack
  Against Machine Learning Models." Network and Distributed System Security
  Symposium (NDSS), 2022.
- Schick, T., Dwivedi-Yu, J., Dessì, R., Raileanu, R., Lomeli, M., Zettlemoyer,
  L., Cancedda, N., and Scialom, T. "Toolformer: Language Models Can Teach
  Themselves to Use Tools." arXiv preprint, 2023.
- Shen, Y., Song, K., Tan, X., Li, D., Lu, W., and Zhuang, Y. "HuggingGPT:
  Solving AI Tasks with ChatGPT and its Friends in HuggingFace." arXiv preprint,
  2023.
- Stiennon, N., Ouyang, L., Wu, J., Ziegler, D., Lowe, R., Voss, C., Radford, A.,
  Amodei, D., and Christiano, P. F. "Learning to Summarize with Human Feedback."
  Advances in Neural Information Processing Systems (NeurIPS), 2020.
- Wei, J., Wang, X., Schuurmans, D., Bosma, M., Xia, F., Chi, E. H., Le, Q. V.,
  Zhou, D., et al. "Chain-of-Thought Prompting Elicits Reasoning in Large
  Language Models." Advances in Neural Information Processing Systems (NeurIPS),
  2022.
- Yao, S., Zhao, J., Yu, D., Shafran, I., Narasimhan, K. R., and Cao, Y. "ReAct:
  Synergizing Reasoning and Acting in Language Models." International Conference
  on Learning Representations (ICLR), 2023.

</details>
