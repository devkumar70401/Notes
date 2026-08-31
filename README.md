# Machine Learning Engineer Knowledge Vault & Live Site

Welcome to the central repository for the Machine Learning Engineer Knowledge Vault, hosted live at [https://devkumar70401.github.io/Notes/](https://devkumar70401.github.io/Notes/).

---

## 🧭 Live Site Navigation Management

The navigation tree and structure for the live site are defined and managed through the following core configuration files:

1. **Master Navigation & Site Configuration:**
   * **File:** [`mkdocs.yml`](file:///home/dev/SE/Notes/mkdocs.yml)
   * **Role:** Defines the complete hierarchy under the `nav:` section, site metadata, Material for MkDocs theme settings, math rendering (KaTeX), Jupyter notebook plugins, and Markdown extensions.

2. **Automated Documentation Sync Hook:**
   * **File:** [`hooks/sync_docs.py`](file:///home/dev/SE/Notes/hooks/sync_docs.py)
   * **Role:** An automated pre-build hook that dynamically synchronizes and symlinks markdown notes, Jupyter notebooks (`.ipynb`), and static assets into `.docs/` before MkDocs compiles the static site.

---

## 🗂️ Knowledge Vault Structure

* **`I Foundations/`**: Calculus, Linear Algebra, Optimization, Backpropagation derivations, and Computational Physics.
* **`II Programming/`**: Core Java (Weeks 1–12), Python, Algorithms & DSA, and Zero-Fail System Design.
* **`III Machine_Learning/`**: Practical Machine Learning, Data Wrangling, and Auditing.
* **`IV Deep_Learning/`**: ANNs, CNNs, Transformers, and PyTorch workflows.
* **`V Tools/`**: Developer tooling, system automation, and Antigravity guides.
