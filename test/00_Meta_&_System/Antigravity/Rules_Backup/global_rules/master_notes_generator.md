# 📖 Master Comprehensive Notes Generator Rule

trigger: always_on

## 🎯 Purpose & Philosophy
To automatically generate **heavy, textbook-grade, self-contained, and comprehensive study notes** (in `.ipynb` Jupyter Notebook or `.md` format) from transcripts, textbooks, or lecture materials. 

Any beginner reading these notes must be able to master the subject without prior assumptions or missing definitions.

---

## 🛠️ Mandatory Directives

### 1. 📖 Technical Jargon Dictionary & First-Appearance Definitions
- **Every Single Technical Term Defined**: Any technical keyword, computer science concept, system tool, or lower-level mechanism (e.g. `Garbage Collection`, `malloc`, `Stack Frames`, `Activation Records`, `ALU`, `Registers`, `JIT`, `AST`, `vtable`, `Liskov Substitution Principle`, `Encapsulation`, `Mark-and-Sweep`, `Metaspace`, `Program Refinement`, `ADTs`, `IEEE 754`, `Two's Complement`, `Static Analysis`, etc.) MUST be defined from first principles when introduced for the first time.
- **Single-Definition Rule**: Once a term is defined in detail earlier in the notebook series, do not repeat the full definition in later notes, but include a brief reference or pointer (e.g., *"(See Lecture 3 for Stack Frame definition)"*).

### 2. 💡 Preserve 100% of Instructor Analogies & Words of Wisdom
- Every lecture notebook MUST contain a dedicated callout box: **"💡 Instructor's Words of Wisdom & Best Practices"**.
- Preserve 100% of real-world analogies (e.g. Water Tank for Memory Leaks, Building Construction for Static Checking, Alumni Event for Top-Down Refinement), warnings, and best programming practices spoken by the teacher.

### 3. ☕ Executable Code Cells & Line-by-Line Breakdown
- Every code example must be written inside an executable code cell (e.g. Java Streams, OOP Classes, Interfaces, Recursion).
- Provide detailed markdown explanations before and after each code cell explaining *why* the code works and what each line achieves.

### 4. 📐 Visual Diagrams & Mathematical Formulas
- Use **Mermaid.js** (`graph TD`, `sequenceDiagram`) for architectural diagrams, memory layouts, and process flows.
- Use **LaTeX** ($O(N \log N)$, $\text{RAM}[A] \rightarrow R_1$) for mathematical equations, memory sizes, and complexity analyses.

### 5. 📂 Multi-Source Deep Ingestion (Transcripts, PDFs, PPTXs, Code & Notes)
- For any subject or week, notes must NEVER be created from a single superficial source alone.
- The agent must deeply inspect, cross-reference, and synthesize across ALL available course assets:
  - **Transcripts**: Audio/video transcript files (`.txt`, `.pdf`, `.vtt`, `.srt`).
  - **Lecture Slides & Handouts**: Official presentation PDFs and slides (`.pdf`, `.pptx`).
  - **Code Files**: Sample code repositories, runnable script files, and starter code (`.java`, `.py`, `.cpp`, `.c`).
  - **Reference Notes**: Any additional student or instructor notes.
- Ensure 100% coverage by fusing slides, code examples, and spoken lecture transcripts into a unified master notebook.

