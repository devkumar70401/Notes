# 📖 Battle-Tested Engineering Notes Generator Rule

trigger: always_on

## 🎯 Purpose & Philosophy
Generate clean, production-grade learning notes (`.ipynb` or `.md`) that teach durable engineering habits. Notes should not just transcribe information; they must structure it so the reader intuitively avoids anti-patterns and writes robust code.

---

## 🛠️ Mandatory Directives

### 1. 🎯 Curated Mental Models & Core Invariants
- Replace exhaustive, low-value jargon dumps with **High-Leverage Mental Models**.
- Define foundational mechanisms only when they directly influence how code behaves in memory, on disk, or across the CPU/GPU.
- For every core concept, document its **Primary Invariant** (the absolute rule that must never be violated during execution).

### 2. ⚠️ "Battle Scars" & Anti-Pattern Contrast
- Every major section MUST include an **Anti-Pattern vs. Defensive Fix** callout:
  - **Naive Implementation**: The common way beginners write it.
  - **Why It Fails**: The hidden race condition, memory leak, or edge case.
  - **Hardened Implementation**: The robust, production-safe approach.

### 3. ☕ Runnable, Contract-Driven Code Blocks
- Code blocks must demonstrate **Contract Programming** (explicit type hints, precondition checks, postcondition assertions, and clear exception boundaries).
- Include line-by-line commentary focusing on *why* defensive guard rails are positioned where they are.

### 4. 📐 Visual Failure Flow & Architecture
- Use **Mermaid.js** diagrams to trace not only happy paths, but explicit **Error/Recovery Paths** and memory lifecycles.
- Use **LaTeX** for algorithmic complexity, numerical stability constraints, and hardware-level memory estimations.

### 5. 📂 Pragmatic Multi-Source Synthesis
- Synthesize transcripts, slides, and repositories into a structured document that emphasizes practical application over academic formalism.