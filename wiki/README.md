# CS858 Wiki

Per-paper reading companions and shared concept pages for CS858 (Trustworthy
Machine Learning). Each primary-reading paper gets one page that orients the
student: a contextualized overview with the threat model, the prerequisites at
Wikipedia link density, the state of the field when the paper appeared, and
high-level questions to read with. The page sets up a targeted read of the
paper; it never replaces it.

Last compiled: 2026-06-18. Papers: 3. Concepts: 21.

---

## Contents

| Section | Description |
| --- | --- |
| [Papers](papers/README.md) | Per-paper reading companions, grouped by course section. |
| [Concepts](concepts/README.md) | Shared prerequisite concept pages. |

---

## Papers by section

| Paper | Section | Year | Summary |
| --- | --- | --- | --- |
| [madry-2018-pgd](papers/madry-2018-pgd.md) | Adversarial Robustness | 2018 | The min-max robust-optimization framing of adversarial attacks and defenses; PGD and adversarial training. |
| [abadi-2016-dp-sgd](papers/abadi-2016-dp-sgd.md) | Differential Privacy | 2016 | DP-SGD and the moments accountant; training deep networks under a provable (epsilon, delta) guarantee. |
| [carlini-2022-lira](papers/carlini-2022-lira.md) | Membership Inference | 2022 | Membership inference recast as a likelihood-ratio test (LiRA), and the case for evaluating attacks at low false-positive rates. |

---

## How pages are made

Paper pages are produced by the `/generate-paper-summary` workflow:
instructor-curated, AI-drafted, peer-reviewable. Students never author these
pages. Links between pages are plain relative Markdown links so the wiki renders
in any Markdown editor, on GitHub, and in a static-site build.
