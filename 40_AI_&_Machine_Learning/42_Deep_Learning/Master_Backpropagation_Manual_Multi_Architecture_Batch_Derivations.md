# 📘 Master Backpropagation Manual: Raw Mathematical Derivations Across Architectures & Batches

---

## 🧭 Document Purpose

This document provides a **complete, zero-shortcut mathematical breakdown of Backpropagation** in Deep Neural Networks. 

Every single forward pass multiplication, activation function evaluation, loss calculation, backward Jacobian product, outer product gradient, batch averaging step, and parameter update is written out in **explicit raw arithmetic** with clean, human-readable numbers.

---

## 1. Standard Mathematical Notation & Master Equations

### Notation System (Standard Deep Learning Convention)
- **$l \in \{1, 2, \dots, L\}$**: Layer index ($l=1$ is first hidden layer, $l=L$ is output layer).
- **$n^{[l]}$**: Number of neurons in layer $l$ ($n^{[0]} = d_{\text{in}}$ is input dimension).
- **$W^{[l]} \in \mathbb{R}^{n^{[l]} \times n^{[l-1]}}$**: Weight matrix for layer $l$.
- **$\mathbf{b}^{[l]} \in \mathbb{R}^{n^{[l]}}$**: Bias vector for layer $l$.
- **$\mathbf{z}^{[l]} \in \mathbb{R}^{n^{[l]}}$**: Pre-activation linear combination ($\mathbf{z}^{[l]} = W^{[l]} \mathbf{a}^{[l-1]} + \mathbf{b}^{[l]}$).
- **$\mathbf{a}^{[l]} \in \mathbb{R}^{n^{[l]}}$**: Post-activation vector ($\mathbf{a}^{[l]} = \sigma(\mathbf{z}^{[l]})$), where $\mathbf{a}^{[0]} = \mathbf{x}$ is input.
- **$\boldsymbol{\delta}^{[l]} = \frac{\partial \mathcal{J}}{\partial \mathbf{z}^{[l]}} \in \mathbb{R}^{n^{[l]}}$**: Upstream Error Signal vector at layer $l$.
- **$N$**: Batch size (number of training samples).
- **$\mathcal{J} = \frac{1}{N} \sum_{k=1}^N L^{(k)}$**: Mean Batch Loss.

---

### The 4 Master Backpropagation Equations

$$\begin{aligned}
\text{\bf [BP1] Output Error Signal:} \quad & \boldsymbol{\delta}^{[L]} = \nabla_{\mathbf{a}^{[L]}} L \odot \sigma'\left(\mathbf{z}^{[L]}\right) \\[8pt]
\text{\bf [BP2] Hidden Error Propagation:} \quad & \boldsymbol{\delta}^{[l]} = \left( (W^{[l+1]})^T \boldsymbol{\delta}^{[l+1]} \right) \odot \sigma'\left(\mathbf{z}^{[l]}\right) \\[8pt]
\text{\bf [BP3] Weight Gradient (Batch-Averaged):} \quad & \frac{\partial \mathcal{J}}{\partial W^{[l]}} = \frac{1}{N} \sum_{k=1}^N \boldsymbol{\delta}^{[l](k)} \left(\mathbf{a}^{[l-1](k)}\right)^T = \frac{1}{N} \Delta^{[l]} \left(A^{[l-1]}\right)^T \\[8pt]
\text{\bf [BP4] Bias Gradient (Batch-Averaged):} \quad & \frac{\partial \mathcal{J}}{\partial \mathbf{b}^{[l]}} = \frac{1}{N} \sum_{k=1}^N \boldsymbol{\delta}^{[l](k)} = \frac{1}{N} \Delta^{[l]} \mathbf{1}_N
\end{aligned}$$

---

# SECTION A: Architecture 1 — Input [2] $\to$ Hidden [2] $\to$ Output [1]

```text
       x₁ ───┬───────► h₁ (z₁[¹], a₁[¹]) ───┬───────► Output ŷ (z[²]) ───► Loss L
             │         ▲                    │
             │   W[¹]  │              W[²]  │
             ▼         │                    ▼
       x₂ ───────────► h₂ (z₂[¹], a₂[¹]) ───┘
```

---

## 📍 Scenario 1: Architecture 1 with 1 Sample ($N=1$)

### 1. Initial State & Setup
- **Input:** $\mathbf{x} = \begin{bmatrix} 2.0 \\ 1.0 \end{bmatrix}$, **Target:** $y = 3.0$
- **Layer 1 Weights & Biases ($2 \times 2$ and $2 \times 1$):**
  $$W^{[1]} = \begin{bmatrix} 0.5 & 0.5 \\ 1.0 & -0.5 \end{bmatrix}, \quad \mathbf{b}^{[1]} = \begin{bmatrix} 0.0 \\ 0.0 \end{bmatrix}$$
- **Layer 2 Weights & Biases ($1 \times 2$ and $1 \times 1$):**
  $$W^{[2]} = \begin{bmatrix} 1.0 & 0.5 \end{bmatrix}, \quad b^{[2]} = 0.0$$
- **Activation Functions:** 
  - Hidden Layer: $\text{ReLU}(z) = \max(0, z)$ with derivative $\sigma'(z) = 1 \text{ if } z > 0 \text{ else } 0$
  - Output Layer: Linear $\sigma(z) = z$ with derivative $\sigma'(z) = 1$
- **Loss Function:** Squared Error $L = \frac{1}{2}(\hat{y} - y)^2$
- **Learning Rate:** $\eta = 0.1$

---

### 2. Forward Pass (Step-by-Step Arithmetic)

#### Step 2.1: Pre-activation $\mathbf{z}^{[1]}$
$$\mathbf{z}^{[1]} = W^{[1]} \mathbf{x} + \mathbf{b}^{[1]} = \begin{bmatrix} 0.5 & 0.5 \\ 1.0 & -0.5 \end{bmatrix} \begin{bmatrix} 2.0 \\ 1.0 \end{bmatrix} + \begin{bmatrix} 0.0 \\ 0.0 \end{bmatrix}$$

$$\begin{aligned}
z_1^{[1]} &= (0.5)(2.0) + (0.5)(1.0) + 0.0 = 1.0 + 0.5 = 1.5 \\
z_2^{[1]} &= (1.0)(2.0) + (-0.5)(1.0) + 0.0 = 2.0 - 0.5 = 1.5
\end{aligned} \implies \mathbf{z}^{[1]} = \begin{bmatrix} 1.5 \\ 1.5 \end{bmatrix}$$

#### Step 2.2: Hidden Activation $\mathbf{a}^{[1]}$
$$\mathbf{a}^{[1]} = \text{ReLU}\left(\mathbf{z}^{[1]}\right) = \begin{bmatrix} \text{ReLU}(1.5) \\ \text{ReLU}(1.5) \end{bmatrix} = \begin{bmatrix} 1.5 \\ 1.5 \end{bmatrix}$$

#### Step 2.3: Output Pre-activation and Prediction $\hat{y}$
$$z^{[2]} = W^{[2]} \mathbf{a}^{[1]} + b^{[2]} = \begin{bmatrix} 1.0 & 0.5 \end{bmatrix} \begin{bmatrix} 1.5 \\ 1.5 \end{bmatrix} + 0.0$$
$$\hat{y} = z^{[2]} = (1.0)(1.5) + (0.5)(1.5) + 0.0 = 1.5 + 0.75 = \mathbf{2.25}$$

#### Step 2.4: Loss Evaluation
$$L = \frac{1}{2}(\hat{y} - y)^2 = \frac{1}{2}(2.25 - 3.0)^2 = \frac{1}{2}(-0.75)^2 = \frac{1}{2}(0.5625) = \mathbf{0.28125}$$

---

### 3. Backward Pass (Raw Chain Rule Execution)

#### Step 3.1: Output Error Signal $\delta^{[2]}$ [BP1]
$$\delta^{[2]} = \frac{\partial L}{\partial z^{[2]}} = \frac{\partial L}{\partial \hat{y}} \cdot \frac{d\hat{y}}{dz^{[2]}} = (\hat{y} - y) \cdot (1) = 2.25 - 3.0 = \mathbf{-0.75}$$

#### Step 3.2: Layer 2 Gradients $\frac{\partial L}{\partial W^{[2]}}$ and $\frac{\partial L}{\partial b^{[2]}}$ [BP3, BP4]
$$\frac{\partial L}{\partial W^{[2]}} = \delta^{[2]} \left(\mathbf{a}^{[1]}\right)^T = (-0.75) \begin{bmatrix} 1.5 & 1.5 \end{bmatrix} = \begin{bmatrix} -1.125 & -1.125 \end{bmatrix}$$

$$\frac{\partial L}{\partial b^{[2]}} = \delta^{[2]} = -0.75$$

#### Step 3.3: Backpropagate Error to Hidden Layer $\boldsymbol{\delta}^{[1]}$ [BP2]
$$\boldsymbol{\delta}^{[1]} = \left( (W^{[2]})^T \delta^{[2]} \right) \odot \text{ReLU}'\left(\mathbf{z}^{[1]}\right)$$

$$(W^{[2]})^T \delta^{[2]} = \begin{bmatrix} 1.0 \\ 0.5 \end{bmatrix} (-0.75) = \begin{bmatrix} -0.75 \\ -0.375 \end{bmatrix}$$

Since both $z_1^{[1]} = 1.5 > 0$ and $z_2^{[1]} = 1.5 > 0$, the ReLU derivatives are:
$$\text{ReLU}'\left(\mathbf{z}^{[1]}\right) = \begin{bmatrix} 1 \\ 1 \end{bmatrix}$$

$$\boldsymbol{\delta}^{[1]} = \begin{bmatrix} -0.75 \\ -0.375 \end{bmatrix} \odot \begin{bmatrix} 1 \\ 1 \end{bmatrix} = \begin{bmatrix} -0.75 \\ -0.375 \end{bmatrix}$$

#### Step 3.4: Layer 1 Gradients $\frac{\partial L}{\partial W^{[1]}}$ and $\frac{\partial L}{\partial \mathbf{b}^{[1]}}$ [BP3, BP4]
$$\frac{\partial L}{\partial W^{[1]}} = \boldsymbol{\delta}^{[1]} \mathbf{x}^T = \begin{bmatrix} -0.75 \\ -0.375 \end{bmatrix} \begin{bmatrix} 2.0 & 1.0 \end{bmatrix} = \begin{bmatrix} (-0.75)(2.0) & (-0.75)(1.0) \\ (-0.375)(2.0) & (-0.375)(1.0) \end{bmatrix} = \begin{bmatrix} -1.50 & -0.75 \\ -0.75 & -0.375 \end{bmatrix}$$

$$\frac{\partial L}{\partial \mathbf{b}^{[1]}} = \boldsymbol{\delta}^{[1]} = \begin{bmatrix} -0.75 \\ -0.375 \end{bmatrix}$$

---

### 4. Optimizer Step (Gradient Descent Update with $\eta = 0.1$)

$$W^{[2]} \leftarrow \begin{bmatrix} 1.0 & 0.5 \end{bmatrix} - 0.1 \begin{bmatrix} -1.125 & -1.125 \end{bmatrix} = \begin{bmatrix} 1.0 + 0.1125 & 0.5 + 0.1125 \end{bmatrix} = \mathbf{\begin{bmatrix} 1.1125 & 0.6125 \end{bmatrix}}$$

$$b^{[2]} \leftarrow 0.0 - 0.1(-0.75) = \mathbf{+0.075}$$

$$W^{[1]} \leftarrow \begin{bmatrix} 0.5 & 0.5 \\ 1.0 & -0.5 \end{bmatrix} - 0.1 \begin{bmatrix} -1.50 & -0.75 \\ -0.75 & -0.375 \end{bmatrix} = \mathbf{\begin{bmatrix} 0.65 & 0.575 \\ 1.075 & -0.4625 \end{bmatrix}}$$

$$\mathbf{b}^{[1]} \leftarrow \begin{bmatrix} 0.0 \\ 0.0 \end{bmatrix} - 0.1 \begin{bmatrix} -0.75 \\ -0.375 \end{bmatrix} = \mathbf{\begin{bmatrix} 0.075 \\ 0.0375 \end{bmatrix}}$$

---

## 📍 Scenario 2: Architecture 1 with 2 Samples / Mini-Batch ($N=2$)

Now we process **two samples simultaneously** to see how batch accumulation and averaging work mathematically.

### 1. Data Batch Setup
- **Sample 1:** $\mathbf{x}^{(1)} = \begin{bmatrix} 2.0 \\ 1.0 \end{bmatrix}, \quad y^{(1)} = 3.0$
- **Sample 2:** $\mathbf{x}^{(2)} = \begin{bmatrix} 0.0 \\ 2.0 \end{bmatrix}, \quad y^{(2)} = 1.0$

- **Batch Input Matrix $X \in \mathbb{R}^{2 \times 2}$ (each column is a sample):**
  $$X = \begin{bmatrix} \mathbf{x}^{(1)} & \mathbf{x}^{(2)} \end{bmatrix} = \begin{bmatrix} 2.0 & 0.0 \\ 1.0 & 2.0 \end{bmatrix}$$
- **Target Vector:** $\mathbf{y} = \begin{bmatrix} 3.0 & 1.0 \end{bmatrix}$
- **Initial Weights:** Same as Scenario 1 ($W^{[1]}, \mathbf{b}^{[1]}, W^{[2]}, b^{[2]}$).

---

### 2. Forward Pass on the Batch

#### Step 2.1: Layer 1 Pre-activation Matrix $Z^{[1]} \in \mathbb{R}^{2 \times 2}$
$$Z^{[1]} = W^{[1]} X + \mathbf{b}^{[1]} \mathbf{1}_2^T = \begin{bmatrix} 0.5 & 0.5 \\ 1.0 & -0.5 \end{bmatrix} \begin{bmatrix} 2.0 & 0.0 \\ 1.0 & 2.0 \end{bmatrix} + \begin{bmatrix} 0.0 & 0.0 \\ 0.0 & 0.0 \end{bmatrix}$$

- Column 1 (Sample 1): $\begin{bmatrix} (0.5)(2) + (0.5)(1) \\ (1)(2) + (-0.5)(1) \end{bmatrix} = \begin{bmatrix} 1.5 \\ 1.5 \end{bmatrix}$
- Column 2 (Sample 2): $\begin{bmatrix} (0.5)(0) + (0.5)(2) \\ (1)(0) + (-0.5)(2) \end{bmatrix} = \begin{bmatrix} 1.0 \\ -1.0 \end{bmatrix}$

$$Z^{[1]} = \begin{bmatrix} 1.5 & 1.0 \\ 1.5 & -1.0 \end{bmatrix}$$

#### Step 2.2: Layer 1 Activation Matrix $A^{[1]} \in \mathbb{R}^{2 \times 2}$
$$A^{[1]} = \text{ReLU}\left(Z^{[1]}\right) = \begin{bmatrix} \text{ReLU}(1.5) & \text{ReLU}(1.0) \\ \text{ReLU}(1.5) & \text{ReLU}(-1.0) \end{bmatrix} = \begin{bmatrix} 1.5 & 1.0 \\ 1.5 & \mathbf{0.0} \end{bmatrix}$$
*(Notice neuron 2 was inactive for sample 2!)*

#### Step 2.3: Layer 2 Output Vector $\hat{\mathbf{y}} \in \mathbb{R}^{1 \times 2}$
$$\hat{\mathbf{y}} = Z^{[2]} = W^{[2]} A^{[1]} + b^{[2]} = \begin{bmatrix} 1.0 & 0.5 \end{bmatrix} \begin{bmatrix} 1.5 & 1.0 \\ 1.5 & 0.0 \end{bmatrix} + 0.0$$

- Sample 1: $\hat{y}^{(1)} = (1.0)(1.5) + (0.5)(1.5) = \mathbf{2.25}$
- Sample 2: $\hat{y}^{(2)} = (1.0)(1.0) + (0.5)(0.0) = \mathbf{1.00}$

$$\hat{\mathbf{y}} = \begin{bmatrix} 2.25 & 1.00 \end{bmatrix}$$

#### Step 2.4: Mean Batch Loss $\mathcal{J}$
- Sample 1 Loss: $L^{(1)} = \frac{1}{2}(2.25 - 3.0)^2 = \frac{1}{2}(-0.75)^2 = 0.28125$
- Sample 2 Loss: $L^{(2)} = \frac{1}{2}(1.00 - 1.0)^2 = \frac{1}{2}(0.0)^2 = 0.00000$

$$\mathcal{J} = \frac{1}{2}\left(L^{(1)} + L^{(2)}\right) = \frac{1}{2}(0.28125 + 0.0) = \mathbf{0.140625}$$

---

### 3. Backward Pass on the Batch

#### Step 3.1: Output Error Matrix $\Delta^{[2]} \in \mathbb{R}^{1 \times 2}$
$$\Delta^{[2]} = \hat{\mathbf{y}} - \mathbf{y} = \begin{bmatrix} 2.25 - 3.0 & 1.00 - 1.0 \end{bmatrix} = \begin{bmatrix} \mathbf{-0.75} & \mathbf{0.00} \end{bmatrix}$$

#### Step 3.2: Layer 2 Batch Gradients [BP3, BP4]
$$\frac{\partial \mathcal{J}}{\partial W^{[2]}} = \frac{1}{N} \Delta^{[2]} \left(A^{[1]}\right)^T = \frac{1}{2} \begin{bmatrix} -0.75 & 0.00 \end{bmatrix} \begin{bmatrix} 1.5 & 1.5 \\ 1.0 & 0.0 \end{bmatrix} = \frac{1}{2} \begin{bmatrix} (-0.75)(1.5) + (0)(1.0) & (-0.75)(1.5) + (0)(0) \end{bmatrix}$$

$$\frac{\partial \mathcal{J}}{\partial W^{[2]}} = \frac{1}{2} \begin{bmatrix} -1.125 & -1.125 \end{bmatrix} = \mathbf{\begin{bmatrix} -0.5625 & -0.5625 \end{bmatrix}}$$

$$\frac{\partial \mathcal{J}}{\partial b^{[2]}} = \frac{1}{N} \sum_{k=1}^2 \delta^{[2](k)} = \frac{1}{2}(-0.75 + 0.0) = \mathbf{-0.375}$$

#### Step 3.3: Backpropagate Error Matrix to Hidden Layer $\Delta^{[1]} \in \mathbb{R}^{2 \times 2}$
$$\Delta^{[1]} = \left( (W^{[2]})^T \Delta^{[2]} \right) \odot \text{ReLU}'\left(Z^{[1]}\right)$$

$$(W^{[2]})^T \Delta^{[2]} = \begin{bmatrix} 1.0 \\ 0.5 \end{bmatrix} \begin{bmatrix} -0.75 & 0.00 \end{bmatrix} = \begin{bmatrix} -0.75 & 0.00 \\ -0.375 & 0.00 \end{bmatrix}$$

ReLU derivative matrix:
$$\text{ReLU}'\left(Z^{[1]}\right) = \begin{bmatrix} \text{ReLU}'(1.5) & \text{ReLU}'(1.0) \\ \text{ReLU}'(1.5) & \text{ReLU}'(-1.0) \end{bmatrix} = \begin{bmatrix} 1 & 1 \\ 1 & \mathbf{0} \end{bmatrix}$$

$$\Delta^{[1]} = \begin{bmatrix} -0.75 & 0.00 \\ -0.375 & 0.00 \end{bmatrix} \odot \begin{bmatrix} 1 & 1 \\ 1 & 0 \end{bmatrix} = \begin{bmatrix} \mathbf{-0.75} & \mathbf{0.00} \\ \mathbf{-0.375} & \mathbf{0.00} \end{bmatrix}$$

#### Step 3.4: Layer 1 Batch Gradients [BP3, BP4]
$$\frac{\partial \mathcal{J}}{\partial W^{[1]}} = \frac{1}{2} \Delta^{[1]} X^T = \frac{1}{2} \begin{bmatrix} -0.75 & 0.00 \\ -0.375 & 0.00 \end{bmatrix} \begin{bmatrix} 2.0 & 1.0 \\ 0.0 & 2.0 \end{bmatrix}$$

Carrying out the matrix multiplication:
- Row 1: $\begin{bmatrix} (-0.75)(2) + 0 & (-0.75)(1) + 0 \end{bmatrix} = \begin{bmatrix} -1.50 & -0.75 \end{bmatrix}$
- Row 2: $\begin{bmatrix} (-0.375)(2) + 0 & (-0.375)(1) + 0 \end{bmatrix} = \begin{bmatrix} -0.75 & -0.375 \end{bmatrix}$

$$\frac{\partial \mathcal{J}}{\partial W^{[1]}} = \frac{1}{2} \begin{bmatrix} -1.50 & -0.75 \\ -0.75 & -0.375 \end{bmatrix} = \mathbf{\begin{bmatrix} -0.750 & -0.3750 \\ -0.375 & -0.1875 \end{bmatrix}}$$

$$\frac{\partial \mathcal{J}}{\partial \mathbf{b}^{[1]}} = \frac{1}{2} \begin{bmatrix} -0.75 + 0.0 \\ -0.375 + 0.0 \end{bmatrix} = \mathbf{\begin{bmatrix} -0.3750 \\ -0.1875 \end{bmatrix}}$$

---

# SECTION B: Architecture 2 — Input [3] $\to$ Hidden 1 [3] $\to$ Hidden 2 [2] $\to$ Output [1] (Batch of 4 Samples)

```text
[Input x ∈ ℝ³] ───(W[¹] ∈ ℝ³ˣ³)───► [h₁ ∈ ℝ³] ───(W[²] ∈ ℝ²ˣ³)───► [h₂ ∈ ℝ²] ───(W[³] ∈ ℝ¹ˣ²)───► [ŷ ∈ ℝ¹]
```

## 📍 Scenario 3: 3-D Input, 4 Samples ($N=4$)

### 1. Initial State & Batch Setup
- **Batch Input Matrix $X \in \mathbb{R}^{3 \times 4}$:**
  $$X = \begin{bmatrix} 
  1.0 & 0.0 & 2.0 & 1.0 \\
  2.0 & 1.0 & 0.0 & 1.0 \\
  1.0 & 2.0 & 1.0 & 0.0
  \end{bmatrix}$$
- **Target Vector ($1 \times 4$):** $\mathbf{y} = \begin{bmatrix} 2.0 & 1.0 & 3.0 & 2.0 \end{bmatrix}$

- **Layer 1 ($3 \times 3$):**
  $$W^{[1]} = \begin{bmatrix} 1 & 0 & 1 \\ 0 & 1 & 1 \\ 1 & 1 & 0 \end{bmatrix}, \quad \mathbf{b}^{[1]} = \begin{bmatrix} 0 \\ 0 \\ 0 \end{bmatrix}$$

- **Layer 2 ($2 \times 3$):**
  $$W^{[2]} = \begin{bmatrix} 1 & 0 & 1 \\ 0 & 1 & 1 \end{bmatrix}, \quad \mathbf{b}^{[2]} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}$$

- **Layer 3 ($1 \times 2$):**
  $$W^{[3]} = \begin{bmatrix} 1 & 1 \end{bmatrix}, \quad b^{[3]} = 0$$

- **Activation:** Linear $\sigma(z) = z$ across all layers to make multi-layer propagation crystal clear.

---

### 2. Forward Pass Across All 4 Samples

#### Step 2.1: Layer 1 Activations $A^{[1]} = W^{[1]} X$ ($3 \times 4$)
$$A^{[1]} = \begin{bmatrix} 1 & 0 & 1 \\ 0 & 1 & 1 \\ 1 & 1 & 0 \end{bmatrix} \begin{bmatrix} 1 & 0 & 2 & 1 \\ 2 & 1 & 0 & 1 \\ 1 & 2 & 1 & 0 \end{bmatrix} = \begin{bmatrix} (1+0+1) & (0+0+2) & (2+0+1) & (1+0+0) \\ (0+2+1) & (0+1+2) & (0+0+1) & (0+1+0) \\ (1+2+0) & (0+1+0) & (2+0+0) & (1+1+0) \end{bmatrix} = \mathbf{\begin{bmatrix} 2 & 2 & 3 & 1 \\ 3 & 3 & 1 & 1 \\ 3 & 1 & 2 & 2 \end{bmatrix}}$$

#### Step 2.2: Layer 2 Activations $A^{[2]} = W^{[2]} A^{[1]}$ ($2 \times 4$)
$$A^{[2]} = \begin{bmatrix} 1 & 0 & 1 \\ 0 & 1 & 1 \end{bmatrix} \begin{bmatrix} 2 & 2 & 3 & 1 \\ 3 & 3 & 1 & 1 \\ 3 & 1 & 2 & 2 \end{bmatrix} = \begin{bmatrix} (2+3) & (2+1) & (3+2) & (1+2) \\ (3+3) & (3+1) & (1+2) & (1+2) \end{bmatrix} = \mathbf{\begin{bmatrix} 5 & 3 & 5 & 3 \\ 6 & 4 & 3 & 3 \end{bmatrix}}$$

#### Step 2.3: Layer 3 Predictions $\hat{\mathbf{y}} = W^{[3]} A^{[2]}$ ($1 \times 4$)
$$\hat{\mathbf{y}} = \begin{bmatrix} 1 & 1 \end{bmatrix} \begin{bmatrix} 5 & 3 & 5 & 3 \\ 6 & 4 & 3 & 3 \end{bmatrix} = \mathbf{\begin{bmatrix} 11 & 7 & 8 & 6 \end{bmatrix}}$$

#### Step 2.4: Compute Errors Across the 4 Samples
$$\mathbf{e} = \hat{\mathbf{y}} - \mathbf{y} = \begin{bmatrix} 11 - 2 & 7 - 1 & 8 - 3 & 6 - 2 \end{bmatrix} = \mathbf{\begin{bmatrix} 9 & 6 & 5 & 4 \end{bmatrix}}$$

$$\mathcal{J} = \frac{1}{4} \sum_{k=1}^4 \frac{1}{2}(e_k)^2 = \frac{1}{8}\left(81 + 36 + 25 + 16\right) = \frac{158}{8} = \mathbf{19.75}$$

---

### 3. Backward Pass Across All 4 Samples

#### Step 3.1: Output Error Matrix $\Delta^{[3]} \in \mathbb{R}^{1 \times 4}$
$$\Delta^{[3]} = \begin{bmatrix} 9 & 6 & 5 & 4 \end{bmatrix}$$

#### Step 3.2: Layer 3 Gradient $\frac{\partial \mathcal{J}}{\partial W^{[3]}}$
$$\frac{\partial \mathcal{J}}{\partial W^{[3]}} = \frac{1}{4} \Delta^{[3]} \left(A^{[2]}\right)^T = \frac{1}{4} \begin{bmatrix} 9 & 6 & 5 & 4 \end{bmatrix} \begin{bmatrix} 5 & 6 \\ 3 & 4 \\ 5 & 3 \\ 3 & 3 \end{bmatrix}$$

$$\frac{\partial \mathcal{J}}{\partial W^{[3]}} = \frac{1}{4} \begin{bmatrix} (45 + 18 + 25 + 12) & (54 + 24 + 15 + 12) \end{bmatrix} = \frac{1}{4} \begin{bmatrix} 100 & 105 \end{bmatrix} = \mathbf{\begin{bmatrix} 25.00 & 26.25 \end{bmatrix}}$$

---

#### Step 3.3: Propagate Error to Hidden Layer 2 ($\Delta^{[2]} \in \mathbb{R}^{2 \times 4}$)
$$\Delta^{[2]} = (W^{[3]})^T \Delta^{[3]} = \begin{bmatrix} 1 \\ 1 \end{bmatrix} \begin{bmatrix} 9 & 6 & 5 & 4 \end{bmatrix} = \mathbf{\begin{bmatrix} 9 & 6 & 5 & 4 \\ 9 & 6 & 5 & 4 \end{bmatrix}}$$

#### Step 3.4: Layer 2 Gradient $\frac{\partial \mathcal{J}}{\partial W^{[2]}}$ ($2 \times 3$)
$$\frac{\partial \mathcal{J}}{\partial W^{[2]}} = \frac{1}{4} \Delta^{[2]} \left(A^{[1]}\right)^T = \frac{1}{4} \begin{bmatrix} 9 & 6 & 5 & 4 \\ 9 & 6 & 5 & 4 \end{bmatrix} \begin{bmatrix} 2 & 3 & 3 \\ 2 & 3 & 1 \\ 3 & 1 & 2 \\ 1 & 1 & 2 \end{bmatrix}$$

$$\Delta^{[2]} \left(A^{[1]}\right)^T = \begin{bmatrix} 
(18 + 12 + 15 + 4) & (27 + 18 + 5 + 4) & (27 + 6 + 10 + 8) \\
(18 + 12 + 15 + 4) & (27 + 18 + 5 + 4) & (27 + 6 + 10 + 8) 
\end{bmatrix} = \begin{bmatrix} 49 & 54 & 51 \\ 49 & 54 & 51 \end{bmatrix}$$

$$\frac{\partial \mathcal{J}}{\partial W^{[2]}} = \frac{1}{4} \begin{bmatrix} 49 & 54 & 51 \\ 49 & 54 & 51 \end{bmatrix} = \mathbf{\begin{bmatrix} 12.25 & 13.50 & 12.75 \\ 12.25 & 13.50 & 12.75 \end{bmatrix}}$$

---

#### Step 3.5: Propagate Error to Hidden Layer 1 ($\Delta^{[1]} \in \mathbb{R}^{3 \times 4}$)
$$\Delta^{[1]} = (W^{[2]})^T \Delta^{[2]} = \begin{bmatrix} 1 & 0 \\ 0 & 1 \\ 1 & 1 \end{bmatrix} \begin{bmatrix} 9 & 6 & 5 & 4 \\ 9 & 6 & 5 & 4 \end{bmatrix} = \mathbf{\begin{bmatrix} 9 & 6 & 5 & 4 \\ 9 & 6 & 5 & 4 \\ 18 & 12 & 10 & 8 \end{bmatrix}}$$

#### Step 3.6: Layer 1 Gradient $\frac{\partial \mathcal{J}}{\partial W^{[1]}}$ ($3 \times 3$)
$$\frac{\partial \mathcal{J}}{\partial W^{[1]}} = \frac{1}{4} \Delta^{[1]} X^T = \frac{1}{4} \begin{bmatrix} 9 & 6 & 5 & 4 \\ 9 & 6 & 5 & 4 \\ 18 & 12 & 10 & 8 \end{bmatrix} \begin{bmatrix} 1 & 2 & 1 \\ 0 & 1 & 2 \\ 2 & 0 & 1 \\ 1 & 1 & 0 \end{bmatrix}$$

- Row 1: $\begin{bmatrix} (9+0+10+4) & (18+6+0+4) & (9+12+5+0) \end{bmatrix} = \begin{bmatrix} 23 & 28 & 26 \end{bmatrix}$
- Row 2: $\begin{bmatrix} (9+0+10+4) & (18+6+0+4) & (9+12+5+0) \end{bmatrix} = \begin{bmatrix} 23 & 28 & 26 \end{bmatrix}$
- Row 3: $\begin{bmatrix} (18+0+20+8) & (36+12+0+8) & (18+24+10+0) \end{bmatrix} = \begin{bmatrix} 46 & 56 & 52 \end{bmatrix}$

$$\frac{\partial \mathcal{J}}{\partial W^{[1]}} = \frac{1}{4} \begin{bmatrix} 23 & 28 & 26 \\ 23 & 28 & 26 \\ 46 & 56 & 52 \end{bmatrix} = \mathbf{\begin{bmatrix} 5.75 & 7.00 & 6.50 \\ 5.75 & 7.00 & 6.50 \\ 11.50 & 14.00 & 13.00 \end{bmatrix}}$$

---

# SECTION C: Architecture 3 — Deep 4-Layer Network (2 $\to$ 2 $\to$ 2 $\to$ 2 $\to$ 1)

```text
x ∈ ℝ² ──(W[¹])──► h₁ ∈ ℝ² ──(W[²])──► h₂ ∈ ℝ² ──(W[³])──► h₃ ∈ ℝ² ──(W[⁴])──► ŷ ∈ ℝ¹
```

## 📍 Scenario 4: Deep Multi-Layer Gradient Propagation

### 1. Setup
- **Input:** $\mathbf{x} = \begin{bmatrix} 1.0 \\ 1.0 \end{bmatrix}$, **Target:** $y = 10.0$
- **Weight Matrices:**
  $$W^{[1]} = \begin{bmatrix} 1 & 1 \\ 1 & 0 \end{bmatrix}, \quad W^{[2]} = \begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix}, \quad W^{[3]} = \begin{bmatrix} 2 & 0 \\ 0 & 1 \end{bmatrix}, \quad W^{[4]} = \begin{bmatrix} 1 & 1 \end{bmatrix}$$
- All biases $\mathbf{b}^{[l]} = \mathbf{0}$, Linear activations.

---

### 2. Forward Pass Through All 4 Layers

1. **Layer 1:** $\mathbf{a}^{[1]} = W^{[1]} \mathbf{x} = \begin{bmatrix} 1 & 1 \\ 1 & 0 \end{bmatrix} \begin{bmatrix} 1 \\ 1 \end{bmatrix} = \begin{bmatrix} 2 \\ 1 \end{bmatrix}$
2. **Layer 2:** $\mathbf{a}^{[2]} = W^{[2]} \mathbf{a}^{[1]} = \begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix} \begin{bmatrix} 2 \\ 1 \end{bmatrix} = \begin{bmatrix} 3 \\ 1 \end{bmatrix}$
3. **Layer 3:** $\mathbf{a}^{[3]} = W^{[3]} \mathbf{a}^{[2]} = \begin{bmatrix} 2 & 0 \\ 0 & 1 \end{bmatrix} \begin{bmatrix} 3 \\ 1 \end{bmatrix} = \begin{bmatrix} 6 \\ 1 \end{bmatrix}$
4. **Layer 4 (Output):** $\hat{y} = W^{[4]} \mathbf{a}^{[3]} = \begin{bmatrix} 1 & 1 \end{bmatrix} \begin{bmatrix} 6 \\ 1 \end{bmatrix} = 6 + 1 = \mathbf{7.0}$

Loss:
$$L = \frac{1}{2}(\hat{y} - y)^2 = \frac{1}{2}(7.0 - 10.0)^2 = \frac{1}{2}(-3.0)^2 = \mathbf{4.5}$$

---

### 3. Backward Pass Through All 4 Layers (The Deep Chain)

#### Step 3.1: Output Layer 4 Error & Gradient
$$\delta^{[4]} = \hat{y} - y = 7.0 - 10.0 = \mathbf{-3.0}$$

$$\frac{\partial L}{\partial W^{[4]}} = \delta^{[4]} \left(\mathbf{a}^{[3]}\right)^T = (-3.0) \begin{bmatrix} 6 & 1 \end{bmatrix} = \mathbf{\begin{bmatrix} -18.0 & -3.0 \end{bmatrix}}$$

---

#### Step 3.2: Layer 3 Error & Gradient
$$\boldsymbol{\delta}^{[3]} = (W^{[4]})^T \delta^{[4]} = \begin{bmatrix} 1 \\ 1 \end{bmatrix} (-3.0) = \mathbf{\begin{bmatrix} -3.0 \\ -3.0 \end{bmatrix}}$$

$$\frac{\partial L}{\partial W^{[3]}} = \boldsymbol{\delta}^{[3]} \left(\mathbf{a}^{[2]}\right)^T = \begin{bmatrix} -3.0 \\ -3.0 \end{bmatrix} \begin{bmatrix} 3 & 1 \end{bmatrix} = \mathbf{\begin{bmatrix} -9.0 & -3.0 \\ -9.0 & -3.0 \end{bmatrix}}$$

---

#### Step 3.3: Layer 2 Error & Gradient
$$\boldsymbol{\delta}^{[2]} = (W^{[3]})^T \boldsymbol{\delta}^{[3]} = \begin{bmatrix} 2 & 0 \\ 0 & 1 \end{bmatrix} \begin{bmatrix} -3.0 \\ -3.0 \end{bmatrix} = \mathbf{\begin{bmatrix} -6.0 \\ -3.0 \end{bmatrix}}$$

$$\frac{\partial L}{\partial W^{[2]}} = \boldsymbol{\delta}^{[2]} \left(\mathbf{a}^{[1]}\right)^T = \begin{bmatrix} -6.0 \\ -3.0 \end{bmatrix} \begin{bmatrix} 2 & 1 \end{bmatrix} = \mathbf{\begin{bmatrix} -12.0 & -6.0 \\ -6.0 & -3.0 \end{bmatrix}}$$

---

#### Step 3.4: Layer 1 Error & Gradient (Reaching the Input Layer!)
$$\boldsymbol{\delta}^{[1]} = (W^{[2]})^T \boldsymbol{\delta}^{[2]} = \begin{bmatrix} 1 & 0 \\ 1 & 1 \end{bmatrix} \begin{bmatrix} -6.0 \\ -3.0 \end{bmatrix} = \begin{bmatrix} -6.0 + 0 \\ -6.0 - 3.0 \end{bmatrix} = \mathbf{\begin{bmatrix} -6.0 \\ -9.0 \end{bmatrix}}$$

$$\frac{\partial L}{\partial W^{[1]}} = \boldsymbol{\delta}^{[1]} \mathbf{x}^T = \begin{bmatrix} -6.0 \\ -9.0 \end{bmatrix} \begin{bmatrix} 1.0 & 1.0 \end{bmatrix} = \mathbf{\begin{bmatrix} -6.0 & -6.0 \\ -9.0 & -9.0 \end{bmatrix}}$$

---

## 4. Master Summary Table Across All Architectures

| Architecture | Layers | Input Shape | Batch Size ($N$) | Output Equation ($\hat{y}$) | Loss Gradient at Layer 1 ($\frac{\partial \mathcal{J}}{\partial W^{[1]}}$) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Arch 1 (1 Sample)** | $2 \to 2 \to 1$ | $2 \times 1$ | $1$ | $W^{[2]} \text{ReLU}(W^{[1]}\mathbf{x} + \mathbf{b}^{[1]}) + b^{[2]}$ | $\boldsymbol{\delta}^{[1]} \mathbf{x}^T = \begin{bmatrix} -1.50 & -0.75 \\ -0.75 & -0.375 \end{bmatrix}$ |
| **Arch 1 (Mini-Batch)** | $2 \to 2 \to 1$ | $2 \times 2$ | $2$ | $W^{[2]} \text{ReLU}(W^{[1]}X + \mathbf{b}^{[1]}) + b^{[2]}$ | $\frac{1}{2} \Delta^{[1]} X^T = \begin{bmatrix} -0.750 & -0.3750 \\ -0.375 & -0.1875 \end{bmatrix}$ |
| **Arch 2 (Deep Batch)** | $3 \to 3 \to 2 \to 1$ | $3 \times 4$ | $4$ | $W^{[3]} W^{[2]} W^{[1]} X$ | $\frac{1}{4} \Delta^{[1]} X^T = \begin{bmatrix} 5.75 & 7.00 & 6.50 \\ 5.75 & 7.00 & 6.50 \\ 11.50 & 14.00 & 13.00 \end{bmatrix}$ |
| **Arch 3 (4 Layers)** | $2 \to 2 \to 2 \to 2 \to 1$ | $2 \times 1$ | $1$ | $W^{[4]} W^{[3]} W^{[2]} W^{[1]} \mathbf{x}$ | $\boldsymbol{\delta}^{[1]} \mathbf{x}^T = \begin{bmatrix} -6.0 & -6.0 \\ -9.0 & -9.0 \end{bmatrix}$ |
