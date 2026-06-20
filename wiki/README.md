# CS858 Wiki

Per-paper reading companions and shared concept pages for CS858 (Trustworthy
Machine Learning). Each primary-reading paper gets one page that orients the
student: a contextualized overview with the threat model, the prerequisites at
Wikipedia link density, the state of the field when the paper appeared, and
high-level questions to read with. The page sets up a targeted read of the
paper; it never replaces it.

Last compiled: 2026-06-19. Papers: 3. Concepts: 21.

---

## Contents

| Section | Description |
| --- | --- |
| [Papers](papers/README.md) | Per-paper reading companions, grouped by course section. |
| [Concepts](concepts/README.md) | Shared prerequisite concept pages. |

---

## Reading list

Twenty-four primary papers span two parts and nine themes. Each primary paper
links to its reading companion where one exists, and to a placeholder otherwise.
Essential readings link to their published sources.

### Part 1: Risks to trustworthiness in ML

<table>
  <thead>
    <tr>
      <th>#</th>
      <th>Paper</th>
      <th>Theme</th>
      <th>Topic</th>
      <th>Essential readings</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td><a href="papers/madry-2018-pgd.md">Towards Deep Learning Models Resistant to Adversarial Attacks</a></td>
      <td rowspan="4">Inference-Time Integrity of Model Behavior</td>
      <td>Adversarial Robustness of Classification Models</td>
      <td><a href="https://arxiv.org/abs/1412.6572">Explaining and Harnessing Adversarial Examples</a><br><a href="https://arxiv.org/abs/2003.01690">Reliable evaluation of adversarial robustness with an ensemble of diverse parameter-free attacks</a></td>
    </tr>
    <tr>
      <td>2</td>
      <td><a href="under-construction.md">Jailbroken: How Does LLM Safety Training Fail?</a> <sup title="Reading companion under construction">&dagger;</sup></td>
      <td>Jailbreaking LLMs</td>
      <td><a href="https://arxiv.org/abs/2307.15043">Universal and Transferable Adversarial Attacks on Aligned Language Models</a><br><a href="https://arxiv.org/abs/2310.08419">Jailbreaking Black Box Large Language Models in Twenty Queries</a></td>
    </tr>
    <tr>
      <td>3</td>
      <td><a href="under-construction.md">Not What You've Signed Up For: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection</a> <sup title="Reading companion under construction">&dagger;</sup></td>
      <td>Indirect Prompt Injection in AI Agents</td>
      <td><a href="https://arxiv.org/abs/2403.02691">InjecAgent: Benchmarking Indirect Prompt Injections in Tool-Integrated LLM Agents</a><br><a href="https://arxiv.org/abs/2310.12815">Formalizing and Benchmarking Prompt Injection Attacks and Defenses</a></td>
    </tr>
    <tr>
      <td>4</td>
      <td><a href="under-construction.md">Safety Alignment Should Be Made More Than Just a Few Tokens Deep</a> <sup title="Reading companion under construction">&dagger;</sup></td>
      <td>Safety Alignment and Guardrails</td>
      <td><a href="https://arxiv.org/abs/2312.06674">Llama Guard: LLM-based Input-Output Safeguard for Human-AI Conversations</a><br><a href="https://arxiv.org/abs/2410.05451">SecAlign: Defending Against Prompt Injection with Preference Optimization</a></td>
    </tr>
    <tr>
      <td>5</td>
      <td><a href="papers/carlini-2022-lira.md">Membership Inference Attacks From First Principles</a></td>
      <td rowspan="4">Training-Data Memorization and Leakage</td>
      <td>Membership Inference Attacks</td>
      <td><a href="https://arxiv.org/abs/1610.05820">Membership Inference Attacks Against Machine Learning Models</a><br><a href="https://arxiv.org/abs/2310.16789">Detecting Pretraining Data from Large Language Models</a></td>
    </tr>
    <tr>
      <td>6</td>
      <td><a href="under-construction.md">Extracting Training Data from Large Language Models</a> <sup title="Reading companion under construction">&dagger;</sup></td>
      <td>Training-data Extraction from LLMs</td>
      <td><a href="https://arxiv.org/abs/2311.17035">Scalable Extraction of Training Data from (Production) Language Models</a><br><a href="https://arxiv.org/abs/2301.13188">Extracting Training Data from Diffusion Models</a></td>
    </tr>
    <tr>
      <td>7</td>
      <td><a href="papers/abadi-2016-dp-sgd.md">Deep Learning with Differential Privacy</a></td>
      <td>Differential Privacy in ML</td>
      <td><a href="https://arxiv.org/abs/1902.08874">Evaluating Differentially Private Machine Learning in Practice</a><br><a href="https://arxiv.org/abs/2110.05679">Large Language Models Can Be Strong Differentially Private Learners</a></td>
    </tr>
    <tr>
      <td>8</td>
      <td><a href="under-construction.md">Knowledge Unlearning for Mitigating Privacy Risks in Language Models</a> <sup title="Reading companion under construction">&dagger;</sup></td>
      <td>Unlearning for Generative AI</td>
      <td><a href="https://arxiv.org/abs/2303.07345">Erasing Concepts from Diffusion Models</a><br><a href="https://arxiv.org/abs/2401.06121">TOFU: A Task of Fictitious Unlearning for LLMs</a></td>
    </tr>
    <tr>
      <td>9</td>
      <td><a href="under-construction.md">Knockoff Nets: Stealing Functionality of Black-Box Models</a> <sup title="Reading companion under construction">&dagger;</sup></td>
      <td rowspan="2">Model Extraction and Distillation</td>
      <td>Model Extraction / Stealing</td>
      <td><a href="https://arxiv.org/abs/1909.01838">High Accuracy and High Fidelity Extraction of Neural Networks</a><br><a href="https://arxiv.org/abs/2403.06634">Stealing Part of a Production Language Model</a></td>
    </tr>
    <tr>
      <td>10</td>
      <td><a href="under-construction.md">DAWN: Dynamic Adversarial Watermarking of Neural Networks</a> <sup title="Reading companion under construction">&dagger;</sup></td>
      <td>Model Watermarking / Fingerprinting</td>
      <td><a href="https://arxiv.org/abs/2304.06607">False Claims against Model Ownership Resolution</a><br><a href="https://arxiv.org/abs/2502.11598">Can LLM Watermarks Robustly Prevent Unauthorized Knowledge Distillation?</a></td>
    </tr>
    <tr>
      <td>11</td>
      <td><a href="under-construction.md">Neural Cleanse: Identifying and Mitigating Backdoor Attacks in Neural Networks</a> <sup title="Reading companion under construction">&dagger;</sup></td>
      <td rowspan="2">Data Integrity and Supply-Chain Security</td>
      <td>Training-data Poisoning</td>
      <td><a href="https://arxiv.org/abs/1708.06733">BadNets: Identifying Vulnerabilities in the Machine Learning Model Supply Chain</a><br><a href="https://arxiv.org/abs/2305.00944">Poisoning Language Models During Instruction Tuning</a></td>
    </tr>
    <tr>
      <td>12</td>
      <td><a href="under-construction.md">PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented Generation of Large Language Models</a> <sup title="Reading companion under construction">&dagger;</sup></td>
      <td>Preference Manipulation / RAG Poisoning</td>
      <td><a href="https://arxiv.org/abs/2406.18382">Adversarial Search Engine Optimization for Large Language Models</a><br><a href="https://arxiv.org/abs/2405.15556">Certifiably Robust RAG against Retrieval Corruption</a></td>
    </tr>
    <tr>
      <td>13</td>
      <td><a href="under-construction.md">Representation Engineering: A Top-Down Approach to AI Transparency</a> <sup title="Reading companion under construction">&dagger;</sup></td>
      <td rowspan="4">Cross-Cutting Topics</td>
      <td>Mechanistic Interpretability for AI safety</td>
      <td><a href="https://arxiv.org/abs/2406.11717">Refusal in Language Models Is Mediated by a Single Direction</a><br><a href="https://arxiv.org/abs/2406.04313">Improving Alignment and Robustness with Circuit Breakers</a></td>
    </tr>
    <tr>
      <td>14</td>
      <td><a href="under-construction.md">SoK: Unintended Interactions among Machine Learning Defenses and Risks</a> <sup title="Reading companion under construction">&dagger;</sup></td>
      <td>Unintended Interactions among ML Defenses and Risks</td>
      <td><a href="https://arxiv.org/abs/2207.01991">Conflicting Interactions Among Protection Mechanisms for Machine Learning Models</a><br><a href="https://arxiv.org/abs/2411.09776">Combining Machine Learning Defenses without Conflicts</a></td>
    </tr>
    <tr>
      <td>15</td>
      <td><a href="under-construction.md">A Watermark for Large Language Models</a> <sup title="Reading companion under construction">&dagger;</sup></td>
      <td>Media Forensics and Proactive Provanance</td>
      <td><a href="https://arxiv.org/abs/2305.20030">Tree-Ring Watermarks: Fingerprints for Diffusion Images that are Invisible and Robust</a><br><a href="https://arxiv.org/abs/2001.06564">Media Forensics and DeepFakes: An Overview</a></td>
    </tr>
    <tr>
      <td>16</td>
      <td><a href="under-construction.md">Examining Zero-Shot Vulnerability Repair with Large Language Models</a> <sup title="Reading companion under construction">&dagger;</sup></td>
      <td>AI for Cybersecurity</td>
      <td><a href="https://arxiv.org/abs/2404.08144">LLM Agents can Autonomously Exploit One-day Vulnerabilities</a><br><a href="https://arxiv.org/abs/2606.03811">AI Agents Enable Adaptive Computer Worms</a></td>
    </tr>
  </tbody>
</table>

### Part 2: Software vs. Hardware defenses

<table>
  <thead>
    <tr>
      <th>#</th>
      <th>Paper</th>
      <th>Theme</th>
      <th>Topic</th>
      <th>Essential readings</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>17</td>
      <td><a href="under-construction.md">Secure Transformer Inference Made Non-interactive</a> <sup title="Reading companion under construction">&dagger;</sup></td>
      <td rowspan="2">Leakage Resistance (Client Data)</td>
      <td>Software</td>
      <td><a href="https://eprint.iacr.org/2023/1678">BumbleBee: Secure Two-party Inference Framework for Large Transformers</a></td>
    </tr>
    <tr>
      <td>18</td>
      <td><a href="under-construction.md">BliMe: Verifiably Secure Outsourced Computation with Hardware-Enforced Taint Tracking</a> <sup title="Reading companion under construction">&dagger;</sup></td>
      <td>Hardware</td>
      <td><a href="https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=9582200">Origami Inference: Private Inference Using Hardware Enclaves</a></td>
    </tr>
    <tr>
      <td>19</td>
      <td><a href="under-construction.md">Unlocking the Power of Differentially Private Zeroth-order Optimization for Fine-tuning LLMs</a> <sup title="Reading companion under construction">&dagger;</sup></td>
      <td rowspan="2">Leakage Resistance (Training Data)</td>
      <td>Software</td>
      <td><a href="https://www.usenix.org/system/files/usenixsecurity23-yang-yuchen.pdf">PrivateFL: Accurate, Differentially Private Federated Learning via Personalized Data Transformation</a><br><a href="https://arxiv.org/abs/2009.03561">Local and Central Differential Privacy for Robustness and Privacy in Federated Learning</a></td>
    </tr>
    <tr>
      <td>20</td>
      <td><a href="under-construction.md">No Privacy Left Outside: On the (In-)Security of TEE-Shielded DNN Partition for On-Device ML</a> <sup title="Reading companion under construction">&dagger;</sup></td>
      <td>Hardware</td>
      <td><a href="https://arxiv.org/abs/1806.03287">Slalom: Fast, Verifiable and Private Execution of Neural Networks in Trusted Hardware</a></td>
    </tr>
    <tr>
      <td>21</td>
      <td><a href="under-construction.md">ModelGuard: Information-Theoretic Defense Against Model Extraction Attacks</a> <sup title="Reading companion under construction">&dagger;</sup></td>
      <td rowspan="2">Model Theft Resistance (+ On-Device Private Inference)</td>
      <td>Software</td>
      <td><a href="https://dl.acm.org/doi/pdf/10.1145/3658644.3670267">Beowulf: Mitigating Model Extraction Attacks Via Reshaping Decision Regions</a></td>
    </tr>
    <tr>
      <td>22</td>
      <td><a href="under-construction.md">ASGARD: Protecting On-Device Deep Neural Networks with Virtualization-Based Trusted Execution Environments</a> <sup title="Reading companion under construction">&dagger;</sup></td>
      <td>Hardware</td>
      <td><a href="https://arxiv.org/abs/2011.05905">ShadowNet: A Secure and Efficient On-device Model Inference System for Convolutional Neural Networks</a></td>
    </tr>
    <tr>
      <td>23</td>
      <td><a href="under-construction.md">zkGPT: An Efficient Non-interactive Zero-knowledge Proof Framework for LLM Inference</a> <sup title="Reading companion under construction">&dagger;</sup></td>
      <td rowspan="2">Regulatory Compliance</td>
      <td>Software</td>
      <td><a href="https://dl.acm.org/doi/10.1145/3576915.3623202">Experimenting with Zero-Knowledge Proofs of Training</a><br><a href="https://dl.acm.org/doi/abs/10.1145/3658644.3670316">Zero-Knowledge Proofs of Training for Deep Neural Networks</a></td>
    </tr>
    <tr>
      <td>24</td>
      <td><a href="under-construction.md">PAL*M: Property Attestation for Large Generative Models</a> <sup title="Reading companion under construction">&dagger;</sup></td>
      <td>Hardware</td>
      <td><a href="https://arxiv.org/abs/2406.17548">Laminator: Verifiable ML Property Cards using Hardware-assisted Attestations</a><br><a href="https://arxiv.org/pdf/2510.00554">Sentry: Authenticating Machine Learning Artifacts on the Fly</a></td>
    </tr>
  </tbody>
</table>

<sup>&dagger;</sup> Reading companion under construction; the link opens a placeholder page.
