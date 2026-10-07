# Machine Learning Vault

<p align="center" style="font-size: 1.15em; color: var(--md-default-fg-color--light); margin-top: -0.5em; max-width: 680px; margin-left: auto; margin-right: auto;">
  Exhaustive, intuition-first masterwork reference notes bridging mathematical theory and production-grade machine learning systems.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Status-Active_Development-3b82f6?style=flat-square" alt="Status">
  <img src="https://img.shields.io/badge/Docs-Material_for_MkDocs-0f172a?style=flat-square" alt="Docs">
  <img src="https://img.shields.io/badge/Math-KaTeX_Rendered-3b82f6?style=flat-square" alt="Math">
  <img src="https://img.shields.io/badge/Deploy-GitHub_Pages-22c55e?style=flat-square" alt="Deploy">
</p>

---

## 🧭 Curriculum Overview

<div class="grid cards" markdown>

-   :material-calculator-variant:{ .lg .middle } __01 Foundations__

    ---

    Mathematical machinery and fundamental theory underpinning modern AI models.

    - [:octicons-arrow-right-24: 01. What is Machine Learning?](machine learning/01 foundations/01_what_is_machine_learning.md)  
    - [:octicons-arrow-right-24: 02. Calculus & Continuous Optimization](machine learning/01 foundations/02_calculus.md)  
    - [:octicons-arrow-right-24: 03. Subspaces, Projections & Least Squares](machine learning/01 foundations/03_subspaces_projections_and_least_squares.md)

-   :material-chart-bell-curve-cumulative:{ .lg .middle } __02 Techniques__

    ---

    Core statistical learning algorithms, tree ensembles, and deep neural network architectures.

    - [:octicons-arrow-right-24: Overview & Roadmap](machine learning/02 techniques/index.md)
    - *Supervised & Unsupervised Learning*
    - *Deep Learning & Transformer Architectures*

-   :material-server-network:{ .lg .middle } __03 Practice & Systems__

    ---

    End-to-end engineering, training infrastructure, hardware kernels, and production serving.

    - [:octicons-arrow-right-24: Overview & Roadmap](machine learning/03 practice/index.md)
    - *Distributed Training (DDP / FSDP)*
    - *Quantization & Inference Acceleration*

</div>

---

## 📐 Pedagogical Pillars

Every concept in this vault is developed systematically using a 4-pillar pedagogical standard:

1. **💡 Deep Intuition & Mental Model:** Physical, geometric, and real-world analogies that eliminate academic intimidation.
2. **🎯 Machine Learning Significance:** The exact role and purpose of the mathematical object inside models, loss surfaces, and optimization paths.
3. **🚀 Production Impact & Code:** Direct connections to PyTorch implementations, GPU execution, and modern architectures (Transformers, CNNs, Diffusion).
4. **⚙️ Cause & Effect Dynamics:** Diagnostic analysis of parameter perturbations—what happens when values collapse, explode, or overshoot.

---

## 🚀 Quick Navigation

=== "01. Introduction"
    - **Focus**: Problem formulation, task taxonomy (supervised, unsupervised, self-supervised), and traditional vs. learned systems.
    - **Start**: Read [What is Machine Learning?](machine learning/01 foundations/01_what_is_machine_learning.md).

=== "02. Calculus & Optimization"
    - **Focus**: Rates of change, Jacobians, Hessians, Taylor polynomial approximations, gradient descent dynamics, and learning rate sensitivity.
    - **Start**: Read [Calculus & Continuous Optimization](machine learning/01 foundations/02_calculus.md).

=== "03. Linear Algebra & Projections"
    - **Focus**: Fundamental vector subspaces, column/null spaces, orthogonality, projection operators, and Ordinary Least Squares ($A^T A x = A^T b$).
    - **Start**: Read [Subspaces, Projections & Least Squares](machine learning/01 foundations/03_subspaces_projections_and_least_squares.md).
