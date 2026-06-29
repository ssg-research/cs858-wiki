# Concepts

Background concepts the papers rely on. Each page is a short, self-contained
explanation you can read on its own or reach from a paper that uses it.

| Concept | Summary |
| --- | --- |
| [activation-steering](activation-steering.md) | Controlling an LLM at inference by adding, subtracting, or projecting out a concept direction in its activations; steering vectors and their limits. |
| [adversarial-examples](adversarial-examples.md) | The evasion phenomenon: small input perturbations that flip a prediction. |
| [adversarial-threat-model](adversarial-threat-model.md) | How an adversary's power is specified: perturbation set, knowledge, timing. |
| [adversarial-training](adversarial-training.md) | Training on adversarially perturbed inputs as a defense. |
| [automated-program-repair](automated-program-repair.md) | Generating a patch that makes a faulty program pass a correctness oracle; generate-and-validate (GenProg), plausible-vs-correct, and learned neural repair. |
| [backdoor-attacks](backdoor-attacks.md) | A trigger-fired hidden behavior trained into a model via data poisoning; the overcapacity that enables it and its reuse as the mechanism behind black-box model watermarking. |
| [ciphertext-packing](ciphertext-packing.md) | Packing many plaintext values into the SIMD slots of one homomorphic ciphertext so a single add or multiply acts on all of them; slot rotations and the amortization and communication savings it buys. |
| [code-language-models](code-language-models.md) | Transformers pretrained on source code that complete or generate programs from a prompt; Codex, code completion, and byte-pair tokenization. |
| [contrastive-prompt-pairs](contrastive-prompt-pairs.md) | Eliciting a concept's direction from a matched pair of prompts that differ only in the target concept, by differencing their activations. |
| [convolutional-neural-network](convolutional-neural-network.md) | CNNs for image classification: learned convolutional filters, pooling, a softmax head, and the standard backbones (AlexNet, VGG, ResNet, DenseNet). |
| [cryptographic-commitment](cryptographic-commitment.md) | A binding, hiding token published for a value and opened later; with a time-stamped public log it gives proof of priority for ownership claims. |
| [data-poisoning](data-poisoning.md) | Corrupting training data to change what a model learns: availability vs targeted/integrity poisoning, backdoors as the trigger-conditioned subclass, and why training-set sanitization defenses presume data access. |
| [decoding-strategies](decoding-strategies.md) | How an LLM turns next-token distributions into text: greedy, temperature, top-k, top-p, and prefilling. |
| [dense-retrieval](dense-retrieval.md) | Retrieving documents by embedding the query and passages and ranking by vector similarity (top-k); the neural alternative to BM25 and the retriever inside RAG. |
| [differential-privacy](differential-privacy.md) | The formal bound on any single example's influence; DP-SGD and the epsilon guarantee. |
| [direct-preference-optimization](direct-preference-optimization.md) | Aligning an LM to pairwise preferences directly, without a separate reward model or RL loop; the DPO alternative to RLHF. |
| [empirical-risk-minimization](empirical-risk-minimization.md) | Average training loss as a proxy for expected loss; the baseline objective. |
| [fgsm](fgsm.md) | The one-step gradient-sign attack and its role as a baseline. |
| [gaussian-mechanism](gaussian-mechanism.md) | Sensitivity and noise calibrated to it; the additive-noise recipe behind DP mechanisms. |
| [gradient-clipping](gradient-clipping.md) | Norm-rescaling gradients; a training stabilizer that, per example, becomes a sensitivity bound. |
| [gradient-masking](gradient-masking.md) | The defense failure mode where gradients become useless but worst-case loss stays high. |
| [group-fairness](group-fairness.md) | Constraining a model to behave equitably across groups defined by a sensitive attribute; demographic parity, equalized odds, equality of opportunity, and pre/in/post-processing enforcement. |
| [hardware-virtualization](hardware-virtualization.md) | Hypervisors and the Arm virtualization extensions (EL2, two-stage address translation, the IOMMU) that give each VM an isolated view of memory and devices; the substrate beneath virtualization-based TEEs. |
| [homomorphic-encryption](homomorphic-encryption.md) | Computing directly on ciphertexts so the result decrypts to the function of the plaintexts; partially / leveled / fully HE, bootstrapping, and the CKKS scheme for approximate real arithmetic. |
| [instruction-tuning](instruction-tuning.md) | Fine-tuning a base LM to follow natural-language instructions; the instruction-following objective. |
| [jailbreak](jailbreak.md) | A prompt that elicits behavior a safety-trained LLM was trained to refuse; distinct from adversarial examples. |
| [kl-divergence](kl-divergence.md) | Asymmetric measure of how far one distribution is from a reference; the per-token unit of how much alignment moved the base model. |
| [knowledge-distillation](knowledge-distillation.md) | Training a student to match a teacher's output distribution (soft labels); its equivalence to minimizing KL and its link to model extraction. |
| [language-model-pretraining](language-model-pretraining.md) | Autoregressive next-token pretraining; the pretraining objective, distribution, and base model. |
| [likelihood-ratio-test](likelihood-ratio-test.md) | Deciding between two hypotheses by their likelihood ratio; Neyman-Pearson optimality. |
| [linear-probing](linear-probing.md) | Training a linear classifier on intermediate activations to test whether a property is linearly decodable; supervised concept directions. |
| [linear-representation-hypothesis](linear-representation-hypothesis.md) | The hypothesis that networks encode high-level concepts as linear directions in activation space; concept directions and word-vector analogies. |
| [llm-tool-use](llm-tool-use.md) | An LLM emitting calls to external tools and acting on their outputs; chaining calls toward a goal yields an agent. |
| [llm-watermarking](llm-watermarking.md) | Embedding a hidden, human-imperceptible signal in a generative model's output text for provenance: decoding-time logit/sampling biasing vs post-hoc editing, statistical detection, and the contrast with model-weight watermarking. |
| [lp-norms](lp-norms.md) | ℓ0 / ℓ2 / ℓ-infinity balls as perturbation budgets and proxies for perceptual similarity. |
| [machine-unlearning](machine-unlearning.md) | Removing chosen training data's influence from a trained model without full retraining; exact vs approximate unlearning and the right-to-be-forgotten motivation. |
| [mechanistic-interpretability](mechanistic-interpretability.md) | Bottom-up interpretability that reverse-engineers a network into circuits of neurons or features; the foil to top-down representation-level analysis. |
| [membership-inference](membership-inference.md) | Predicting whether a specific example was in a model's training set; the standard privacy audit. |
| [memorization](memorization.md) | Per-example fitting, random-label capacity, and the long-tail argument; the signal privacy attacks exploit. |
| [model-explanations](model-explanations.md) | Post-hoc explanations released with a prediction: feature attribution, influence-based, and counterfactual/recourse; what they reveal and the attack surface they open. |
| [model-extraction](model-extraction.md) | Attacks that reproduce a deployed model's parameters, hyperparameters, architecture, or functionality from query access; the fidelity-versus-accuracy axes and the MLaaS setting. |
| [model-partitioning](model-partitioning.md) | Splitting a DNN across a trusted execution environment and an untrusted accelerator (GPU): shielding a privacy-sensitive subset in the enclave while offloading the rest in the clear for speed; on-device TSDP and the security-versus-utility trade-off. |
| [model-watermarking](model-watermarking.md) | Embedding an owner-verifiable marker in a trained model; white-box (in the weights) vs black-box (backdoor-based trigger set) verification, and the assumption that the owner controls training. |
| [mutual-information](mutual-information.md) | How much observing one variable reveals about another; the KL divergence between the joint distribution and the product of the marginals, its entropy decomposition, and its role as an information-leakage and rate-distortion measure. |
| [perplexity](perplexity.md) | How well an LM predicts a sequence (exponentiated cross-entropy); the LM quality metric and the per-example membership signal in extraction attacks. |
| [privacy-budget](privacy-budget.md) | The (epsilon, delta) budget, composition theorems, accountants, and amplification by subsampling. |
| [projected-gradient-descent](projected-gradient-descent.md) | Gradient step plus projection; the constrained-optimization primitive behind the PGD attack. |
| [prompt-injection](prompt-injection.md) | Adversarial instructions in a prompt or ingested content that override the intended task; direct and indirect. |
| [red-teaming](red-teaming.md) | Probing a model for policy-violating outputs to inform safety training and as an evaluation benchmark. |
| [reinforcement-learning](reinforcement-learning.md) | Training an agent to maximize a reward from chosen actions; policy gradients, the multi-armed bandit, and the gradient-bandit update. |
| [remote-attestation](remote-attestation.md) | A hardware root of trust signs a measurement (a quote) of the code and data that ran, checked by a remote verifier; property-based attestation adds reference values from a trusted authority, and ML property cards (model card, datasheet, inference card). |
| [retrieval-augmented-generation](retrieval-augmented-generation.md) | Conditioning generation on documents fetched at inference time; retrieved text shares the context window with the instructions. |
| [rlhf](rlhf.md) | Aligning an LM to human preferences via a reward model and policy optimization with a KL penalty to the base model. |
| [robust-optimization](robust-optimization.md) | Min-max / saddle-point optimization and Danskin's theorem. |
| [roc-curves](roc-curves.md) | TPR/FPR trade-offs, AUC, balanced accuracy, and why security evaluates at low false-positive rates. |
| [safety-training](safety-training.md) | Training a deployed LLM to refuse restricted behaviors; refusal, RLHF-for-harmlessness, Constitutional AI. |
| [secure-inference](secure-inference.md) | Running model inference on a client's private input against a server's private model, revealing only the result; HE-, MPC-, and TEE-based instantiations and the interaction / bandwidth cost axes. |
| [secure-multiparty-computation](secure-multiparty-computation.md) | Jointly computing a function over private inputs while revealing only the output; two-party computation, garbled circuits and secret sharing, semi-honest vs malicious adversaries, and simulation-based security. |
| [shadow-models](shadow-models.md) | Adversary-trained imitations of the target model used to calibrate membership inference attacks. |
| [singular-value-decomposition](singular-value-decomposition.md) | Factoring a matrix into singular vectors and values; the rank, the four fundamental subspaces, and the null space as the inputs a matrix maps to zero. |
| [software-vulnerability](software-vulnerability.md) | A security-relevant code defect an attacker can exploit; MITRE's CWE catalog and Top 25, and the concrete / localize / confirm distinction. |
| [stochastic-gradient-descent](stochastic-gradient-descent.md) | Minibatch gradient descent; the default optimizer and the source of attack gradients. |
| [taint-tracking](taint-tracking.md) | Dynamic information-flow tracking (DIFT): labelling data at a source and propagating the label to every derived value, then enforcing a policy on where it may flow; software vs hardware (tag-bit) implementations and the confidentiality / integrity dual uses. |
| [transfer-learning](transfer-learning.md) | Reusing representations across tasks; ImageNet pretraining then fine-tuning, for higher accuracy with less task-specific data. |
| [transferability](transferability.md) | Adversarial examples crafted on one model often fool another; the basis of black-box transfer attacks. |
| [trusted-execution-environment](trusted-execution-environment.md) | Hardware-isolated enclaves that shield code and data from a malicious OS, with remote attestation; Intel SGX, Arm TrustZone, AMD SEV, Sanctum, and their side-channel and run-time-attack limits. |
| [white-box-black-box](white-box-black-box.md) | Adversary knowledge assumptions, from full weights to query-only access. |
| [zero-knowledge-proof](zero-knowledge-proof.md) | A proof that a computation on a secret witness was done correctly while revealing nothing about it; prover and verifier, completeness / soundness / zero-knowledge, interactive vs non-interactive (Fiat-Shamir), succinct proofs / zk-SNARKs, and the arithmetic-circuit model. |
| [zero-shot-prompting](zero-shot-prompting.md) | Eliciting a task from a pretrained LM through the prompt alone, no examples and no fine-tuning; the contrast with few-shot and with fine-tuning. |
| [zeroth-order-optimization](zeroth-order-optimization.md) | Gradient-free optimization that estimates a descent direction from forward-pass loss differences along random directions; the two-point/SPSA estimator and the MeZO line for memory-efficient LLM fine-tuning. |
