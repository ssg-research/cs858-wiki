---
title: "Automated program repair"
type: concept
description: "Automatically producing a patch that makes a faulty program satisfy a correctness oracle (usually a test suite); generate-and-validate search (GenProg), the plausible-versus-correct patch problem, and learning-based neural repair."
tags:
  - program-repair
  - software-security
---

# Automated program repair

## Definition

Automated program repair (APR) takes a program that fails some correctness
criterion and produces a modified program that passes it, with no human writing
the patch. The criterion is an oracle: usually a regression test suite, sometimes
a formal property or a crashing input run under a sanitizer. Classical
generate-and-validate systems search a space of candidate edits and keep any that
pass the tests; GenProg, which mutates the program with genetic operators, is the
seminal example (Le Goues et al., 2012). A recurring pitfall is that a patch can
be plausible, passing the supplied tests, without being correct, so weak test
suites overstate repair rates (Qi et al., 2015). Learning-based repair instead
trains neural sequence-to-sequence models on mined bug-fix pairs to predict a
developer-like patch (Tufano et al., 2019; Chen et al., 2021). Repairing a
security vulnerability is a specialization in which the oracle must also witness
that the exploited weakness is gone.

## Papers that use this concept

- [Examining Zero-Shot Vulnerability Repair with Large Language Models](../papers/pearce-2023-vulnerability-repair.md) — asks whether prompting a pretrained code model can stand in for a task-specific repair model, evaluated inside a generate-and-validate framework with separate security and functional oracles.

## See also

- [Software vulnerability (CWE)](software-vulnerability.md)
- [Large language models for code](code-language-models.md)

## References

- Le Goues, C., Nguyen, T., Forrest, S., and Weimer, W. "GenProg: A Generic
  Method for Automatic Software Repair." IEEE Transactions on Software
  Engineering, 38(1):54-72, 2012.
- Qi, Z., Long, F., Achour, S., and Rinard, M. "An Analysis of Patch Plausibility
  and Correctness for Generate-and-Validate Patch Generation Systems."
  International Symposium on Software Testing and Analysis (ISSTA), 2015.
- Tufano, M., Watson, C., Bavota, G., Di Penta, M., White, M., and Poshyvanyk, D.
  "An Empirical Study on Learning Bug-Fixing Patches in the Wild via Neural
  Machine Translation." ACM Transactions on Software Engineering and Methodology,
  28(4):19:1-19:29, 2019.
- Chen, Z., Kommrusch, S., Tufano, M., Pouchet, L.-N., Poshyvanyk, D., and
  Monperrus, M. "SequenceR: Sequence-to-Sequence Learning for End-to-End Program
  Repair." IEEE Transactions on Software Engineering, 47(9):1943-1959, 2021.
