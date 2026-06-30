---
title: "Jailbroken: How Does LLM Safety Training Fail?"
authors:
  - Wei, Alexander
  - Haghtalab, Nika
  - Steinhardt, Jacob
year: 2023
section: "Jailbreaking LLMs"
primary: true
arxiv: "2307.02483"
tags:
  - jailbreak
  - llm-safety
  - alignment
  - attack
---

### [Wiki Home](../README.md)

# Jailbroken: How Does LLM Safety Training Fail?

## High-level overview

Large language models deployed as assistants are
[safety-trained](../concepts/safety-training.md) to refuse restricted behaviors.
"[Jailbreak](../concepts/jailbreak.md)" prompts elicit those behaviors anyway.
This paper explains why safety training fails against such prompts and turns the
explanation into a recipe for building attacks.

It proposes two failure modes. **Competing objectives**: a model is trained at
once for [language modeling](../concepts/language-model-pretraining.md),
[instruction following](../concepts/instruction-tuning.md), and safety, and a
prompt can be built that forces obeying the first two to mean violating the
third. **Mismatched generalization**: pretraining spans a far wider range of
inputs than safety training, so a prompt placed in that gap is understood by the
model yet missed by its refusal behavior. Each principle yields a family of
concrete attacks, and the two compose.

The paper evaluates these attacks on GPT-4, Claude v1.3, and the smaller GPT-3.5
Turbo, drawing prompts from the model creators' own
[red-teaming](../concepts/red-teaming.md) sets and a larger held-out set. Attacks
built from the two principles outperform ad hoc jailbreaks, and their
combinations succeed on the large majority of restricted prompts. The paper
argues these failures follow from how the models are trained rather than from
their scale, so larger models alone will not remove them, and calls for
"safety-capability parity," safety mechanisms as sophisticated as the model they
guard.

**Threat Model:** The adversary is a user of the deployed chat interface who
wants to elicit a restricted behavior. Access is
[black-box](../concepts/white-box-black-box.md): the adversary queries the model
through the chat interface, with no view of weights or training data and no
ability to set the system prompt or alter the message history. The lever is the
prompt itself, rewriting a refused request into a modified prompt using
transformations that are generally input-agnostic and human-readable; the attack
may be adaptive, choosing the next prompt from the model's replies to earlier
variants, though most attacks succeed without adaptivity. The attack acts at
inference time only, with no access to training. The defender is the model
provider, which serves a safety-trained model that refuses restricted behaviors
and is claimed to resist adversarial misuse.

## Why read this

Finding a jailbreak is easy, and that ease is what makes them hard to study.
Sample a prompt enough times at a high enough temperature and some response may
slip past the refusal by chance, but a one-off success that does not repeat
establishes nothing. The scientific challenge is to elicit restricted behavior
systematically and repeatably. This paper meets that bar: it moves from a
hypothesis about why safety training fails to a clean experimental design, and
produces its attacks by construction rather than by luck.

## Basic Background

### Language models and pretraining

A modern LLM is first pretrained to predict the next token over a large, diverse
text corpus ([language model pretraining](../concepts/language-model-pretraining.md)).
This yields a base model whose sense of which continuations are likely, its
pretraining distribution, spans far more than any later training stage revisits,
including the ability to read unusual formats and encodings. Generation decodes
one token at a time from this distribution, so a continuation that is improbable
in natural text is also improbable for the model.

### Aligning LLMs to follow instructions

A base model continues text; an assistant follows requests.
[Instruction tuning](../concepts/instruction-tuning.md) supervises the model on
instruction-response demonstrations, and
[reinforcement learning from human feedback](../concepts/rlhf.md) (RLHF) then
optimizes it toward human-preferred responses using a learned reward model, with
a penalty that keeps it near the base model (Ouyang et al., 2022; Christiano et
al., 2017). Instruction following and the residual pull of the pretraining
objective are both products of this pipeline.

### Safety training and refusal

[Safety training](../concepts/safety-training.md) is the stage that makes a
deployed model refuse restricted behaviors, such as harmful content, crime
facilitation, and leakage of personal data, expressed as a short refusal. It is
implemented by preference optimization toward harmlessness and by AI feedback
against a written policy (Constitutional AI; Bai et al., 2022), and is often
paired with input and output filtering. It covers a narrower range of inputs
than pretraining or instruction tuning.

### Jailbreaks and red teaming

A [jailbreak](../concepts/jailbreak.md) is a prompt engineered to elicit a
restricted behavior the model would otherwise refuse; the capability is already
present, and the prompt bypasses the refusal.
[Red teaming](../concepts/red-teaming.md) is the complementary practice of
probing a model for policy-violating outputs to inform safety training and
evaluation (Ganguli et al., 2022; Perez et al., 2022); prompts the creators
red-teamed and trained against form a demanding evaluation set.

### Black-box access

[Black-box access](../concepts/white-box-black-box.md) means querying a model
through its interface without its weights, gradients, or training data. It is
the access an ordinary API or chat user has, and the setting in which these
attacks operate.

## Reading guidance

- **Section 2 (Background).** Sets up the threat model and the
  GOODBOT / BADBOT / UNCLEAR labeling scheme; read the access assumptions
  closely, since the strongest system-prompt attack later falls outside them.
- **Section 3 (Failure modes).** Introduces competing objectives and mismatched
  generalization, each illustrated with example attacks and ablations. Note that
  the failure modes are stated as hypotheses and then used to build attacks;
  watch what evidence is offered that these are the operative mechanisms rather
  than one of several possible explanations.
- **Section 4 (Empirical evaluation).** Tables of attack success across the
  models, including combination attacks and the larger held-out dataset. Note how
  an outcome is defined and that the labeling is done by hand.
- **Section 5 (Implications for defense).** The arguments that scaling will not
  resolve either failure mode and that "safety-capability parity" may be needed;
  note which steps rest on the measurements and which extrapolate beyond them.
- **Figure 2 and Table 3.** The GPT-3.5 Turbo versus GPT-4 contrast, where a
  vulnerability appears only once the model is capable enough to follow the
  encoded prompt.
- **Appendices and the responsible-disclosure note.** The labeling scheme,
  attack details, and examples live in the appendices; the strongest prompts are
  deliberately withheld.

<details>
<summary><h2>Supplementary readings</h2></summary>

- [Universal and Transferable Adversarial Attacks on Aligned Language Models](https://arxiv.org/abs/2307.15043) — a white-box, optimization-based route to jailbreaks, complementing this paper's black-box, conceptual route.
- [Jailbreaking Black Box Large Language Models in Twenty Queries](https://arxiv.org/abs/2310.08419) — automates black-box jailbreak discovery with an attacker model in the loop.

</details>

<details>
<summary><h2>Paper Context</h2></summary>

By early 2023, the deployed assistants (ChatGPT, Claude, GPT-4, Bard) were
aligned with a shared toolkit: supervised instruction tuning and RLHF for
helpfulness, RLHF and AI feedback for harmlessness, complemented by red teaming
and input/output filtering (Ouyang et al., 2022; Bai et al., 2022; Ganguli et
al., 2022; OpenAI, 2023). Providers reported that these measures sharply reduced
disallowed responses and claimed reduced susceptibility to adversarial misuse
(OpenAI, 2023; Anthropic, 2023).

In parallel, jailbreaks spread as folklore. Within days of ChatGPT's release,
users shared role-play personas such as "DAN" and other prompt tricks on social
media and forums, discovered and traded in a decentralized way (walkerspider,
2022; Burgess, 2023). Providers patched specific jailbreaks and updated their
models, but the exchange had the shape of an arms race rather than a settled
defense.

Academic study of attacks on safety-trained models was just beginning.
Contemporary work attacked GPT-3.5 through a computer-security lens and
introduced payload splitting (Kang et al., 2023), targeted extraction of
personally identifiable information (Li et al., 2023), analyzed prompt-injection
threats to application-integrated models ([Greshake et al., 2023](greshake-2023-indirect-prompt-injection.md)),
and audited models with discrete optimization (Jones et al., 2023). A separate, older NLP
literature studied [adversarial examples](../concepts/adversarial-examples.md)
and universal triggers that induce model errors (Wallace et al., 2019), surveyed
broadly (Chakraborty et al., 2018; Zhang et al., 2020); that line aims to cause
mistakes, whereas a jailbreak aims to unlock a capability. A systematic,
conceptual account of why jailbreaks succeed, grounded in the training pipeline,
had not been given.

</details>

### [Wiki Home](../README.md)

<details>
<summary><h4>References</h4></summary>

Entries read off the paper's bibliography (arXiv 2307.02483v1, pages 11-14).

- Anthropic. "We are offering a new version of our model, Claude-v1.3, that is
  safer and less susceptible to adversarial attacks." Twitter / @AnthropicAI,
  2023.
- Bai, Y., Kadavath, S., Kundu, S., Askell, A., Kernion, J., Jones, A., Chen,
  A., Goldie, A., Mirhoseini, A., McKinnon, C., et al. "Constitutional AI:
  Harmlessness from AI Feedback." arXiv:2212.08073, 2022.
- Burgess, M. "The Hacking of ChatGPT is Just Getting Started." Wired, 2023.
- Chakraborty, A., Alam, M., Dey, V., Chattopadhyay, A., and Mukhopadhyay, D.
  "Adversarial Attacks and Defences: A Survey." arXiv:1810.00069, 2018.
- Christiano, P. F., Leike, J., Brown, T., Martic, M., Legg, S., and Amodei, D.
  "Deep Reinforcement Learning from Human Preferences." Advances in Neural
  Information Processing Systems (NeurIPS), 30, 2017.
- Ganguli, D., Lovitt, L., Kernion, J., Askell, A., Bai, Y., Kadavath, S., Mann,
  B., Perez, E., Schiefer, N., Ndousse, K., et al. "Red Teaming Language Models
  to Reduce Harms: Methods, Scaling Behaviors, and Lessons Learned."
  arXiv:2209.07858, 2022.
- Greshake, K., Abdelnabi, S., Mishra, S., Endres, C., Holz, T., and Fritz, M.
  "Not what you've signed up for: Compromising Real-World LLM-Integrated
  Applications with Indirect Prompt Injection." arXiv:2302.12173, 2023.
- Jones, E., Dragan, A., Raghunathan, A., and Steinhardt, J. "Automatically
  Auditing Large Language Models via Discrete Optimization." arXiv:2303.04381,
  2023.
- Kang, D., Li, X., Stoica, I., Guestrin, C., Zaharia, M., and Hashimoto, T.
  "Exploiting Programmatic Behavior of LLMs: Dual-Use Through Standard Security
  Attacks." arXiv:2302.05733, 2023.
- Li, H., Guo, D., Fan, W., Xu, M., and Song, Y. "Multi-step Jailbreaking
  Privacy Attacks on ChatGPT." arXiv:2304.05197, 2023.
- OpenAI. "GPT-4 Technical Report." arXiv:2303.08774, 2023.
- Ouyang, L., Wu, J., Jiang, X., Almeida, D., Wainwright, C., Mishkin, P.,
  Zhang, C., Agarwal, S., Slama, K., Ray, A., et al. "Training Language Models
  to Follow Instructions with Human Feedback." Advances in Neural Information
  Processing Systems (NeurIPS), 35, 2022.
- Perez, E., Huang, S., Song, H. F., Cai, T., Ring, R., Aslanides, J., Glaese,
  A., McAleese, N., and Irving, G. "Red Teaming Language Models with Language
  Models." Conference on Empirical Methods in Natural Language Processing
  (EMNLP), 2022.
- Wallace, E., Feng, S., Kandpal, N., Gardner, M., and Singh, S. "Universal
  Adversarial Triggers for Attacking and Analyzing NLP." Conference on Empirical
  Methods in Natural Language Processing and the International Joint Conference on
  Natural Language Processing (EMNLP-IJCNLP), 2019.
- walkerspider. "DAN is my new friend." Reddit r/ChatGPT, 2022.
- Zhang, W. E., Sheng, Q. Z., Alhazmi, A., and Li, C. "Adversarial Attacks on
  Deep-Learning Models in Natural Language Processing: A Survey." ACM
  Transactions on Intelligent Systems and Technology (TIST), 11(3):1-41, 2020.

</details>
