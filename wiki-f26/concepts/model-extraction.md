---
title: "Model extraction"
type: concept
description: "Attacks that reproduce an asset of a deployed model from external (usually query) access: parameters, hyperparameters, architecture, or functionality; the fidelity-versus-accuracy axes and the MLaaS setting."
tags:
  - model-extraction
  - threat-model
  - machine-learning
---

### [Wiki Home](../README.md)

# Model extraction

## Definition

Model extraction, also called model stealing, is the class of attacks that
reproduce some asset of a machine-learning model from external access to it. The
usual access is the query interface of a prediction API
(Machine-Learning-as-a-Service): the adversary submits inputs and receives
outputs, paying per query. What gets stolen varies. Some attacks recover the
exact parameters or a functionally exact equation of simple models (Tramèr et
al., 2016); others recover hyperparameters (Wang and Gong, 2018) or the
architecture (Oh et al., 2018); others recover the model's *functionality*, a
substitute that matches task accuracy without matching the internals.

Extraction results are usually placed on two axes. Fidelity measures how closely
the stolen model reproduces the victim's input-output behavior, prediction for
prediction, including its mistakes. Accuracy measures how well the stolen model
performs the underlying task, judged against ground truth. The two diverge: a
high-accuracy substitute can disagree with the victim on individual inputs, and
a high-fidelity copy inherits the victim's errors. Extraction threatens the
intellectual property and the query revenue of a deployed model, and a faithful
copy can also be a stepping stone to other attacks, for example crafting
transferable adversarial examples against the substitute and replaying them at
the victim (Papernot et al., 2017).

## Papers that use this concept

- [Knockoff Nets: Stealing Functionality of Black-Box Models](../papers/orekondy-2019-knockoff-nets.md) — targets functionality stealing under minimal assumptions, training a "knockoff" from black-box query outputs alone.
- [DAWN: Dynamic Adversarial Watermarking of Neural Networks](../papers/szyller-2019-dawn.md) — defends against functionality-stealing extraction by watermarking the surrogate the adversary trains, rather than preventing the extraction.
- [SoK: Unintended Interactions among Machine Learning Defenses and Risks](../papers/duddu-2024-unintended-interactions.md) — covers model extraction as the unauthorized-model-ownership risk, with watermarking and fingerprinting as the defenses whose side effects it surveys.
- [No Privacy Left Outside: On the (In-)Security of TEE-Shielded DNN Partition for On-Device ML](../papers/zhang-2024-tee-shielded.md) — model stealing is one of the two attacks used to score each TEE-partition defense, recovering near-white-box copies from the offloaded weights.
- [ModelGuard: Information-Theoretic Defense Against Model Extraction Attacks](../papers/tang-2024-modelguard.md) — defends against extraction by perturbing the prediction API's returned confidence vectors, posed as a constrained optimization that covers both parameter-stealing and functionality-stealing.
- [ASGARD: Protecting On-Device Deep Neural Networks with Virtualization-Based Trusted Execution Environments](../papers/moon-2025-asgard.md) — defends the on-device model against an REE-side adversary that dumps or reproduces it during inference, holding the whole model confidential in a virtualization-based enclave.

## See also

- [White-box and black-box access](white-box-black-box.md)
- [Knowledge distillation](knowledge-distillation.md)

### [Wiki Home](../README.md)

## References

- Oh, S.J., Augustin, M., Schiele, B., and Fritz, M. "Towards Reverse-Engineering Black-Box Neural Networks." International Conference on Learning Representations (ICLR), 2018.
- Papernot, N., McDaniel, P., Goodfellow, I., Jha, S., Celik, Z.B., and Swami, A. "Practical Black-Box Attacks against Machine Learning." ACM Asia Conference on Computer and Communications Security (AsiaCCS), 2017.
- Tramèr, F., Zhang, F., Juels, A., Reiter, M.K., and Ristenpart, T. "Stealing Machine Learning Models via Prediction APIs." USENIX Security Symposium, 2016.
- Wang, B. and Gong, N.Z. "Stealing Hyperparameters in Machine Learning." IEEE Symposium on Security and Privacy (S&P), 2018.
