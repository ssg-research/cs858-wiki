# CS858 Wiki

Here you find the list of papers relevant for this course. Every student is
expected to at least read the primary readings.

---

## Contents

| Section | Description |
| --- | --- |
| [Papers](papers/README.md) | The paper pages, each a short guide to one reading. |
| [Concepts](concepts/README.md) | Background concepts the papers rely on. |

---

## Reading list

The course runs in two parts, grouped by theme. The primary reading in each row
is required; expand the essential readings beneath it to see what goes alongside.

### Part 1: Risks to trustworthiness in ML

<table>
  <thead>
    <tr>
      <th scope="col">#</th>
      <th scope="col">Topic</th>
      <th scope="col">Reading</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th colspan="3" scope="colgroup">Inference-Time Integrity of Model Behavior</th>
    </tr>
    <tr>
      <td>1</td>
      <td>Adversarial Robustness of Classification Models</td>
      <td>
        <strong>Primary</strong>
        <a href="papers/madry-2018-pgd.md">Towards Deep Learning Models Resistant to Adversarial Attacks</a>
        <details>
          <summary>Essential readings (2)</summary>
          <ul>
            <li><a href="https://arxiv.org/abs/1412.6572">Explaining and Harnessing Adversarial Examples</a></li>
            <li><a href="https://arxiv.org/abs/2003.01690">Reliable evaluation of adversarial robustness with an ensemble of diverse parameter-free attacks</a></li>
          </ul>
        </details>
      </td>
    </tr>
    <tr>
      <td>2</td>
      <td>Jailbreaking LLMs</td>
      <td>
        <strong>Primary</strong>
        <a href="papers/wei-2023-jailbroken.md">Jailbroken: How Does LLM Safety Training Fail?</a>
        <details>
          <summary>Essential readings (2)</summary>
          <ul>
            <li><a href="https://arxiv.org/abs/2307.15043">Universal and Transferable Adversarial Attacks on Aligned Language Models</a></li>
            <li><a href="https://arxiv.org/abs/2310.08419">Jailbreaking Black Box Large Language Models in Twenty Queries</a></li>
          </ul>
        </details>
      </td>
    </tr>
    <tr>
      <td>3</td>
      <td>Indirect Prompt Injection in AI Agents</td>
      <td>
        <strong>Primary</strong>
        <a href="papers/greshake-2023-indirect-prompt-injection.md">Not What You've Signed Up For: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection</a>
        <details>
          <summary>Essential readings (2)</summary>
          <ul>
            <li><a href="https://arxiv.org/abs/2403.02691">InjecAgent: Benchmarking Indirect Prompt Injections in Tool-Integrated LLM Agents</a></li>
            <li><a href="https://arxiv.org/abs/2310.12815">Formalizing and Benchmarking Prompt Injection Attacks and Defenses</a></li>
          </ul>
        </details>
      </td>
    </tr>
    <tr>
      <td>4</td>
      <td>Safety Alignment and Guardrails</td>
      <td>
        <strong>Primary</strong>
        <a href="papers/qi-2024-shallow-safety-alignment.md">Safety Alignment Should Be Made More Than Just a Few Tokens Deep</a>
        <details>
          <summary>Essential readings (2)</summary>
          <ul>
            <li><a href="https://arxiv.org/abs/2312.06674">Llama Guard: LLM-based Input-Output Safeguard for Human-AI Conversations</a></li>
            <li><a href="https://arxiv.org/abs/2410.05451">SecAlign: Defending Against Prompt Injection with Preference Optimization</a></li>
          </ul>
        </details>
      </td>
    </tr>
    <tr>
      <th colspan="3" scope="colgroup">Training-Data Memorization and Leakage</th>
    </tr>
    <tr>
      <td>5</td>
      <td>Membership Inference Attacks</td>
      <td>
        <strong>Primary</strong>
        <a href="papers/carlini-2022-lira.md">Membership Inference Attacks From First Principles</a>
        <details>
          <summary>Essential readings (2)</summary>
          <ul>
            <li><a href="https://arxiv.org/abs/1610.05820">Membership Inference Attacks Against Machine Learning Models</a></li>
            <li><a href="https://arxiv.org/abs/2310.16789">Detecting Pretraining Data from Large Language Models</a></li>
          </ul>
        </details>
      </td>
    </tr>
    <tr>
      <td>6</td>
      <td>Training-data Extraction from LLMs</td>
      <td>
        <strong>Primary</strong>
        <a href="under-construction.md">Extracting Training Data from Large Language Models</a> <sup title="Reading companion under construction">&dagger;</sup>
        <details>
          <summary>Essential readings (2)</summary>
          <ul>
            <li><a href="https://arxiv.org/abs/2311.17035">Scalable Extraction of Training Data from (Production) Language Models</a></li>
            <li><a href="https://arxiv.org/abs/2301.13188">Extracting Training Data from Diffusion Models</a></li>
          </ul>
        </details>
      </td>
    </tr>
    <tr>
      <td>7</td>
      <td>Differential Privacy in ML</td>
      <td>
        <strong>Primary</strong>
        <a href="papers/abadi-2016-dp-sgd.md">Deep Learning with Differential Privacy</a>
        <details>
          <summary>Essential readings (2)</summary>
          <ul>
            <li><a href="https://arxiv.org/abs/1902.08874">Evaluating Differentially Private Machine Learning in Practice</a></li>
            <li><a href="https://arxiv.org/abs/2110.05679">Large Language Models Can Be Strong Differentially Private Learners</a></li>
          </ul>
        </details>
      </td>
    </tr>
    <tr>
      <td>8</td>
      <td>Unlearning for Generative AI</td>
      <td>
        <strong>Primary</strong>
        <a href="under-construction.md">Knowledge Unlearning for Mitigating Privacy Risks in Language Models</a> <sup title="Reading companion under construction">&dagger;</sup>
        <details>
          <summary>Essential readings (2)</summary>
          <ul>
            <li><a href="https://arxiv.org/abs/2303.07345">Erasing Concepts from Diffusion Models</a></li>
            <li><a href="https://arxiv.org/abs/2401.06121">TOFU: A Task of Fictitious Unlearning for LLMs</a></li>
          </ul>
        </details>
      </td>
    </tr>
    <tr>
      <th colspan="3" scope="colgroup">Model Extraction and Distillation</th>
    </tr>
    <tr>
      <td>9</td>
      <td>Model Extraction / Stealing</td>
      <td>
        <strong>Primary</strong>
        <a href="under-construction.md">Knockoff Nets: Stealing Functionality of Black-Box Models</a> <sup title="Reading companion under construction">&dagger;</sup>
        <details>
          <summary>Essential readings (2)</summary>
          <ul>
            <li><a href="https://arxiv.org/abs/1909.01838">High Accuracy and High Fidelity Extraction of Neural Networks</a></li>
            <li><a href="https://arxiv.org/abs/2403.06634">Stealing Part of a Production Language Model</a></li>
          </ul>
        </details>
      </td>
    </tr>
    <tr>
      <td>10</td>
      <td>Model Watermarking / Fingerprinting</td>
      <td>
        <strong>Primary</strong>
        <a href="under-construction.md">DAWN: Dynamic Adversarial Watermarking of Neural Networks</a> <sup title="Reading companion under construction">&dagger;</sup>
        <details>
          <summary>Essential readings (2)</summary>
          <ul>
            <li><a href="https://arxiv.org/abs/2304.06607">False Claims against Model Ownership Resolution</a></li>
            <li><a href="https://arxiv.org/abs/2502.11598">Can LLM Watermarks Robustly Prevent Unauthorized Knowledge Distillation?</a></li>
          </ul>
        </details>
      </td>
    </tr>
    <tr>
      <th colspan="3" scope="colgroup">Data Integrity and Supply-Chain Security</th>
    </tr>
    <tr>
      <td>11</td>
      <td>Training-data Poisoning</td>
      <td>
        <strong>Primary</strong>
        <a href="under-construction.md">Neural Cleanse: Identifying and Mitigating Backdoor Attacks in Neural Networks</a> <sup title="Reading companion under construction">&dagger;</sup>
        <details>
          <summary>Essential readings (2)</summary>
          <ul>
            <li><a href="https://arxiv.org/abs/1708.06733">BadNets: Identifying Vulnerabilities in the Machine Learning Model Supply Chain</a></li>
            <li><a href="https://arxiv.org/abs/2305.00944">Poisoning Language Models During Instruction Tuning</a></li>
          </ul>
        </details>
      </td>
    </tr>
    <tr>
      <td>12</td>
      <td>Preference Manipulation / RAG Poisoning</td>
      <td>
        <strong>Primary</strong>
        <a href="under-construction.md">PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented Generation of Large Language Models</a> <sup title="Reading companion under construction">&dagger;</sup>
        <details>
          <summary>Essential readings (2)</summary>
          <ul>
            <li><a href="https://arxiv.org/abs/2406.18382">Adversarial Search Engine Optimization for Large Language Models</a></li>
            <li><a href="https://arxiv.org/abs/2405.15556">Certifiably Robust RAG against Retrieval Corruption</a></li>
          </ul>
        </details>
      </td>
    </tr>
    <tr>
      <th colspan="3" scope="colgroup">Cross-Cutting Topics</th>
    </tr>
    <tr>
      <td>13</td>
      <td>Mechanistic Interpretability for AI safety</td>
      <td>
        <strong>Primary</strong>
        <a href="under-construction.md">Representation Engineering: A Top-Down Approach to AI Transparency</a> <sup title="Reading companion under construction">&dagger;</sup>
        <details>
          <summary>Essential readings (2)</summary>
          <ul>
            <li><a href="https://arxiv.org/abs/2406.11717">Refusal in Language Models Is Mediated by a Single Direction</a></li>
            <li><a href="https://arxiv.org/abs/2406.04313">Improving Alignment and Robustness with Circuit Breakers</a></li>
          </ul>
        </details>
      </td>
    </tr>
    <tr>
      <td>14</td>
      <td>Unintended Interactions among ML Defenses and Risks</td>
      <td>
        <strong>Primary</strong>
        <a href="under-construction.md">SoK: Unintended Interactions among Machine Learning Defenses and Risks</a> <sup title="Reading companion under construction">&dagger;</sup>
        <details>
          <summary>Essential readings (2)</summary>
          <ul>
            <li><a href="https://arxiv.org/abs/2207.01991">Conflicting Interactions Among Protection Mechanisms for Machine Learning Models</a></li>
            <li><a href="https://arxiv.org/abs/2411.09776">Combining Machine Learning Defenses without Conflicts</a></li>
          </ul>
        </details>
      </td>
    </tr>
    <tr>
      <td>15</td>
      <td>Media Forensics and Proactive Provanance</td>
      <td>
        <strong>Primary</strong>
        <a href="under-construction.md">A Watermark for Large Language Models</a> <sup title="Reading companion under construction">&dagger;</sup>
        <details>
          <summary>Essential readings (2)</summary>
          <ul>
            <li><a href="https://arxiv.org/abs/2305.20030">Tree-Ring Watermarks: Fingerprints for Diffusion Images that are Invisible and Robust</a></li>
            <li><a href="https://arxiv.org/abs/2001.06564">Media Forensics and DeepFakes: An Overview</a></li>
          </ul>
        </details>
      </td>
    </tr>
    <tr>
      <td>16</td>
      <td>AI for Cybersecurity</td>
      <td>
        <strong>Primary</strong>
        <a href="under-construction.md">Examining Zero-Shot Vulnerability Repair with Large Language Models</a> <sup title="Reading companion under construction">&dagger;</sup>
        <details>
          <summary>Essential readings (2)</summary>
          <ul>
            <li><a href="https://arxiv.org/abs/2404.08144">LLM Agents can Autonomously Exploit One-day Vulnerabilities</a></li>
            <li><a href="https://arxiv.org/abs/2606.03811">AI Agents Enable Adaptive Computer Worms</a></li>
          </ul>
        </details>
      </td>
    </tr>
  </tbody>
</table>

### Part 2: Software vs. Hardware defenses

<table>
  <thead>
    <tr>
      <th scope="col">#</th>
      <th scope="col">Topic</th>
      <th scope="col">Reading</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th colspan="3" scope="colgroup">Leakage Resistance (Client Data)</th>
    </tr>
    <tr>
      <td>17</td>
      <td>Software</td>
      <td>
        <strong>Primary</strong>
        <a href="under-construction.md">Secure Transformer Inference Made Non-interactive</a> <sup title="Reading companion under construction">&dagger;</sup>
        <details>
          <summary>Essential readings (1)</summary>
          <ul>
            <li><a href="https://eprint.iacr.org/2023/1678">BumbleBee: Secure Two-party Inference Framework for Large Transformers</a></li>
          </ul>
        </details>
      </td>
    </tr>
    <tr>
      <td>18</td>
      <td>Hardware</td>
      <td>
        <strong>Primary</strong>
        <a href="under-construction.md">BliMe: Verifiably Secure Outsourced Computation with Hardware-Enforced Taint Tracking</a> <sup title="Reading companion under construction">&dagger;</sup>
        <details>
          <summary>Essential readings (1)</summary>
          <ul>
            <li><a href="https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=9582200">Origami Inference: Private Inference Using Hardware Enclaves</a></li>
          </ul>
        </details>
      </td>
    </tr>
    <tr>
      <th colspan="3" scope="colgroup">Leakage Resistance (Training Data)</th>
    </tr>
    <tr>
      <td>19</td>
      <td>Software</td>
      <td>
        <strong>Primary</strong>
        <a href="under-construction.md">Unlocking the Power of Differentially Private Zeroth-order Optimization for Fine-tuning LLMs</a> <sup title="Reading companion under construction">&dagger;</sup>
        <details>
          <summary>Essential readings (2)</summary>
          <ul>
            <li><a href="https://www.usenix.org/system/files/usenixsecurity23-yang-yuchen.pdf">PrivateFL: Accurate, Differentially Private Federated Learning via Personalized Data Transformation</a></li>
            <li><a href="https://arxiv.org/abs/2009.03561">Local and Central Differential Privacy for Robustness and Privacy in Federated Learning</a></li>
          </ul>
        </details>
      </td>
    </tr>
    <tr>
      <td>20</td>
      <td>Hardware</td>
      <td>
        <strong>Primary</strong>
        <a href="under-construction.md">No Privacy Left Outside: On the (In-)Security of TEE-Shielded DNN Partition for On-Device ML</a> <sup title="Reading companion under construction">&dagger;</sup>
        <details>
          <summary>Essential readings (1)</summary>
          <ul>
            <li><a href="https://arxiv.org/abs/1806.03287">Slalom: Fast, Verifiable and Private Execution of Neural Networks in Trusted Hardware</a></li>
          </ul>
        </details>
      </td>
    </tr>
    <tr>
      <th colspan="3" scope="colgroup">Model Theft Resistance (+ On-Device Private Inference)</th>
    </tr>
    <tr>
      <td>21</td>
      <td>Software</td>
      <td>
        <strong>Primary</strong>
        <a href="under-construction.md">ModelGuard: Information-Theoretic Defense Against Model Extraction Attacks</a> <sup title="Reading companion under construction">&dagger;</sup>
        <details>
          <summary>Essential readings (1)</summary>
          <ul>
            <li><a href="https://dl.acm.org/doi/pdf/10.1145/3658644.3670267">Beowulf: Mitigating Model Extraction Attacks Via Reshaping Decision Regions</a></li>
          </ul>
        </details>
      </td>
    </tr>
    <tr>
      <td>22</td>
      <td>Hardware</td>
      <td>
        <strong>Primary</strong>
        <a href="under-construction.md">ASGARD: Protecting On-Device Deep Neural Networks with Virtualization-Based Trusted Execution Environments</a> <sup title="Reading companion under construction">&dagger;</sup>
        <details>
          <summary>Essential readings (1)</summary>
          <ul>
            <li><a href="https://arxiv.org/abs/2011.05905">ShadowNet: A Secure and Efficient On-device Model Inference System for Convolutional Neural Networks</a></li>
          </ul>
        </details>
      </td>
    </tr>
    <tr>
      <th colspan="3" scope="colgroup">Regulatory Compliance</th>
    </tr>
    <tr>
      <td>23</td>
      <td>Software</td>
      <td>
        <strong>Primary</strong>
        <a href="under-construction.md">zkGPT: An Efficient Non-interactive Zero-knowledge Proof Framework for LLM Inference</a> <sup title="Reading companion under construction">&dagger;</sup>
        <details>
          <summary>Essential readings (2)</summary>
          <ul>
            <li><a href="https://dl.acm.org/doi/10.1145/3576915.3623202">Experimenting with Zero-Knowledge Proofs of Training</a></li>
            <li><a href="https://dl.acm.org/doi/abs/10.1145/3658644.3670316">Zero-Knowledge Proofs of Training for Deep Neural Networks</a></li>
          </ul>
        </details>
      </td>
    </tr>
    <tr>
      <td>24</td>
      <td>Hardware</td>
      <td>
        <strong>Primary</strong>
        <a href="under-construction.md">PAL*M: Property Attestation for Large Generative Models</a> <sup title="Reading companion under construction">&dagger;</sup>
        <details>
          <summary>Essential readings (2)</summary>
          <ul>
            <li><a href="https://arxiv.org/abs/2406.17548">Laminator: Verifiable ML Property Cards using Hardware-assisted Attestations</a></li>
            <li><a href="https://arxiv.org/pdf/2510.00554">Sentry: Authenticating Machine Learning Artifacts on the Fly</a></li>
          </ul>
        </details>
      </td>
    </tr>
  </tbody>
</table>

<sup>&dagger;</sup> Reading companion under construction; the link opens a placeholder page.

---

Last compiled: 2026-06-21. Papers: 6. Concepts: 33.
