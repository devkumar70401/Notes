# 🔬 Microscopic Mathematical Derivation: From 3 Gradients to Final Matrix Formulas

---

## 🧭 Document Purpose & Scope

This document provides a **microscopic, step-by-step calculus derivation** connecting the conceptual 3-gradient chain rule:

$$\frac{\partial \mathcal{L}}{\partial W^{[l]}} = \underbrace{\frac{\partial \mathcal{L}}{\partial \mathbf{a}^{[l]}}}_{\text{Upstream}} \cdot \underbrace{\frac{\partial \mathbf{a}^{[l]}}{\partial \mathbf{z}^{[l]}}}_{\text{Activation}} \cdot \underbrace{\frac{\partial \mathbf{z}^{[l]}}{\partial W^{[l]}}}_{\text{Local}}$$

to the exact computational formulas used in code and slides:

$$\begin{aligned}
\Large \boldsymbol{\delta}^{[l]} &= \Large \left( (W^{[l+1]})^T \boldsymbol{\delta}^{[l+1]} \right) \odot g'\left(\mathbf{z}^{[l]}\right) \\[10pt]
\Large \frac{\partial \mathcal{L}}{\partial W^{[l]}} &= \Large \boldsymbol{\delta}^{[l]} \left(\mathbf{a}^{[l-1]}\right)^T \\[10pt]
\Large \frac{\partial \mathcal{L}}{\partial \mathbf{b}^{[l]}} &= \Large \boldsymbol{\delta}^{[l]}
\end{aligned}$$

Every single differentiation rule, index notation ($i, j, k$), summation sign ($\sum$), and matrix transformation is written out with **zero hand-waving**.

---

# 📚 SECTION 1: Fundamental Calculus & Linear Algebra Rules Used

Before deriving, here are the exact mathematical laws we will invoke at each step:

### Rule 1: Single-Variable Chain Rule
If $y = f(u)$ and $u = g(x)$, then:
$$\frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dx}$$

### Rule 2: Multivariable Chain Rule (Total Derivative over Multiple Paths)
If $L$ depends on $n$ intermediate variables $u_1, u_2, \dots, u_n$, and each $u_k$ depends on $x$:
$$\frac{\partial L}{\partial x} = \sum_{k=1}^n \frac{\partial L}{\partial u_k} \cdot \frac{\partial u_k}{\partial x}$$
*(Intuition: If $x$ affects the loss through 3 different pathways, you must sum the contributions of all 3 pathways).*

### Rule 3: Derivative of a Sum
$$\frac{\partial}{\partial x} \left( \sum_{m} c_m x_m \right) = c_m \quad (\text{only the term with matching index } m \text{ survives; all others are constants } = 0)$$

### Rule 4: Kronecker Delta ($\delta_{ij}$)
$$\delta_{ij} = \begin{cases} 1 & \text{if } i = j \\ 0 & \text{if } i \neq j \end{cases}$$

### Rule 5: Matrix Transposition in Summation Form
The $(j, k)$-th element of transposed matrix $W^T$ is $W_{kj}$:
$$\left(W^T\right)_{jk} = W_{kj}$$
Therefore:
$$\sum_{k} W_{kj} v_k = \sum_{k} \left(W^T\right)_{jk} v_k = \left( W^T \mathbf{v} \right)_j$$

### Rule 6: Outer Product of Two Vectors
If $\mathbf{u} \in \mathbb{R}^{M \times 1}$ and $\mathbf{v} \in \mathbb{R}^{N \times 1}$, their outer product is an $M \times N$ matrix:
$$\left( \mathbf{u} \mathbf{v}^T \right)_{ij} = u_i \cdot v_j$$

---

# 🏗️ SECTION 2: Network Index Setup

Let’s track two adjacent layers in a deep neural network:

```text
       LAYER l-1                 LAYER l                    LAYER l+1
  (Activations a[ˡ⁻¹])     (Pre-activation z[ˡ])       (Pre-activation z[ˡ⁺¹])
                           (Activation a[ˡ])
   
       Neuron j ────────(wᵢⱼ[ˡ])────────► Neuron i ────────(wₖᵢ[ˡ⁺¹])────────► Neuron k
```

### The Explicit Scalar Equations for Every Neuron:
1. **Pre-activation of neuron $i$ in layer $l$:**
   $$z_i^{[l]} = \sum_{j=1}^{n^{[l-1]}} W_{ij}^{[l]} a_j^{[l-1]} + b_i^{[l]} \tag{Eq. 1}$$

2. **Activation of neuron $i$ in layer $l$:**
   $$a_i^{[l]} = g\left(z_i^{[l]}\right) \tag{Eq. 2}$$

3. **Pre-activation of neuron $k$ in layer $l+1$ (the next layer):**
   $$z_k^{[l+1]} = \sum_{i=1}^{n^{[l]}} W_{ki}^{[l+1]} a_i^{[l]} + b_k^{[l+1]} \tag{Eq. 3}$$

---

# 🔬 SECTION 3: Step-by-Step Derivation of the 3 Gradient Terms

We want to find how the final scalar loss $\mathcal{L}$ changes when we change a single weight $W_{ij}^{[l]}$ (the weight connecting neuron $j$ of layer $l-1$ to neuron $i$ of layer $l$).

By the Multivariable Chain Rule:

$$\Large \frac{\partial \mathcal{L}}{\partial W_{ij}^{[l]}} = \underbrace{\frac{\partial \mathcal{L}}{\partial a_i^{[l]}}}_{\text{Term 1: Upstream}} \times \underbrace{\frac{\partial a_i^{[l]}}{\partial z_i^{[l]}}}_{\text{Term 2: Activation}} \times \underbrace{\frac{\partial z_i^{[l]}}{\partial W_{ij}^{[l]}}}_{\text{Term 3: Local}}$$

Let us solve each of these 3 terms with raw calculus!

---

## 📍 Part A: Solving Term 3 (Local Gradient $\frac{\partial z_i^{[l]}}{\partial W_{ij}^{[l]}}$)

Look at Equation 1 for neuron $i$:
$$z_i^{[l]} = W_{i1}^{[l]} a_1^{[l-1]} + W_{i2}^{[l]} a_2^{[l-1]} + \dots + W_{ij}^{[l]} a_j^{[l-1]} + \dots + b_i^{[l]}$$

Take the partial derivative with respect to $W_{ij}^{[l]}$:
- Every term without $W_{ij}^{[l]}$ is treated as a constant $\to 0$.
- The derivative of $W_{ij}^{[l]} a_j^{[l-1]}$ with respect to $W_{ij}^{[l]}$ is $a_j^{[l-1]}$.

$$\Large \frac{\partial z_i^{[l]}}{\partial W_{ij}^{[l]}} = a_j^{[l-1]} \tag{Result 1}$$

*(And for the bias $b_i^{[l]}$, $\frac{\partial z_i^{[l]}}{\partial b_i^{[l]}} = 1$).*

---

## 📍 Part B: Solving Term 2 (Activation Gradient $\frac{\partial a_i^{[l]}}{\partial z_i^{[l]}}$)

Look at Equation 2:
$$a_i^{[l]} = g\left(z_i^{[l]}\right)$$

Take the derivative with respect to $z_i^{[l]}$:

$$\Large \frac{\partial a_i^{[l]}}{\partial z_i^{[l]}} = g'\left(z_i^{[l]}\right) \tag{Result 2}$$

*(For example, if $g$ is Sigmoid $\sigma$, $g'(z) = \sigma(z)(1 - \sigma(z))$. If ReLU, $g'(z) = 1 \text{ if } z > 0 \text{ else } 0$).*

---

## 📍 Part C: Solving Term 1 (Upstream Gradient $\frac{\partial \mathcal{L}}{\partial a_i^{[l]}}$)

This is where the magic happens! How does activation $a_i^{[l]}$ affect the loss $\mathcal{L}$?

Notice from Equation 3 that neuron $a_i^{[l]}$ sends its signal forward to **ALL neurons $k$ in layer $l+1$**:
- $a_i^{[l]}$ enters $z_1^{[l+1]}$ through weight $W_{1i}^{[l+1]}$
- $a_i^{[l]}$ enters $z_2^{[l+1]}$ through weight $W_{2i}^{[l+1]}$
- $\dots$
- $a_i^{[l]}$ enters $z_k^{[l+1]}$ through weight $W_{ki}^{[l+1]}$

```text
               ┌────────► z₁[ˡ⁺¹] (Error δ₁[ˡ⁺¹])
               │
   aᵢ[ˡ] ──────┼────────► z₂[ˡ⁺¹] (Error δ₂[ˡ⁺¹])
               │
               └────────► zₖ[ˡ⁺¹] (Error δₖ[ˡ⁺¹])
```

By the **Multivariable Chain Rule (Rule 2)**, we must sum over all neurons $k$ in layer $l+1$:

$$\frac{\partial \mathcal{L}}{\partial a_i^{[l]}} = \sum_{k=1}^{n^{[l+1]}} \underbrace{\frac{\partial \mathcal{L}}{\partial z_k^{[l+1]}}}_{\text{Definition of } \delta_k^{[l+1]}} \times \frac{\partial z_k^{[l+1]}}{\partial a_i^{[l]}}$$

Now differentiate Equation 3 ($z_k^{[l+1]} = \sum_m W_{km}^{[l+1]} a_m^{[l]} + b_k^{[l+1]}$) with respect to $a_i^{[l]}$:
$$\frac{\partial z_k^{[l+1]}}{\partial a_i^{[l]}} = W_{ki}^{[l+1]}$$

Substitute this back into the sum:

$$\Large \frac{\partial \mathcal{L}}{\partial a_i^{[l]}} = \sum_{k=1}^{n^{[l+1]}} W_{ki}^{[l+1]} \delta_k^{[l+1]} \tag{Result 3}$$

---

# 🧩 SECTION 4: Assembling the Pieces into $\delta_i^{[l]}$

Now let's multiply **Term 1** and **Term 2** together and define that as $\delta_i^{[l]}$:

$$\begin{aligned}
\delta_i^{[l]} &\equiv \frac{\partial \mathcal{L}}{\partial z_i^{[l]}} = \underbrace{\frac{\partial \mathcal{L}}{\partial a_i^{[l]}}}_{\text{Term 1}} \times \underbrace{\frac{\partial a_i^{[l]}}{\partial z_i^{[l]}}}_{\text{Term 2}} \\[10pt]
&= \left( \sum_{k=1}^{n^{[l+1]}} W_{ki}^{[l+1]} \delta_k^{[l+1]} \right) \cdot g'\left(z_i^{[l]}\right) \qquad \text{--- [Scalar Formula]}
\end{aligned}$$

---

## 🔎 The Transpose Emergence: Why $\sum_k W_{ki} \delta_k = (W^T \boldsymbol{\delta})_i$

Look closely at the summation term:
$$\sum_{k=1}^{n^{[l+1]}} W_{ki}^{[l+1]} \delta_k^{[l+1]}$$

In regular matrix multiplication $W \mathbf{v} = \sum_i W_{ki} v_i$, the row index is first ($k$) and we sum over the column index ($i$).

**BUT HERE, WE ARE SUMMING OVER THE FIRST INDEX ($k$)!**
$$W_{1i} \delta_1 + W_{2i} \delta_2 + W_{3i} \delta_3 + \dots$$

By **Rule 5 (Matrix Transposition)**, $W_{ki} = (W^T)_{ik}$. Therefore:

$$\sum_{k=1}^{n^{[l+1]}} W_{ki}^{[l+1]} \delta_k^{[l+1]} = \sum_{k=1}^{n^{[l+1]}} \left( (W^{[l+1]})^T \right)_{ik} \delta_k^{[l+1]} = \mathbf{\left( (W^{[l+1]})^T \boldsymbol{\delta}^{[l+1]} \right)_i}$$

This is the $i$-th element of the vector $(W^{[l+1]})^T \boldsymbol{\delta}^{[l+1]}$!

Since this holds for every neuron $i$, and each $i$ multiplies its own activation slope $g'(z_i^{[l]})$, we package the whole layer into vector form using the **Hadamard (element-wise) product $\odot$**:

$$\Large \mathbf{\boldsymbol{\delta}^{[l]} = \left( (W^{[l+1]})^T \boldsymbol{\delta}^{[l+1]} \right) \odot g'\left(\mathbf{z}^{[l]}\right)}$$

---

# 🎯 SECTION 5: Completing the Weight Gradient Formula

Now multiply by **Term 3 (Result 1: $a_j^{[l-1]}$)**:

$$\begin{aligned}
\frac{\partial \mathcal{L}}{\partial W_{ij}^{[l]}} &= \underbrace{\left( \frac{\partial \mathcal{L}}{\partial a_i^{[l]}} \cdot \frac{\partial a_i^{[l]}}{\partial z_i^{[l]}} \right)}_{\delta_i^{[l]}} \cdot \underbrace{\frac{\partial z_i^{[l]}}{\partial W_{ij}^{[l]}}}_{a_j^{[l-1]}} \\[10pt]
&= \mathbf{\delta_i^{[l]} \cdot a_j^{[l-1]}} \qquad \text{--- [Scalar Weight Derivative]}
\end{aligned}$$

---

## 🔎 The Outer Product Emergence: Why $\delta_i a_j = \boldsymbol{\delta} \mathbf{a}^T$

Look at all the weight derivatives in layer $l$ arranged in a matrix:

$$\frac{\partial \mathcal{L}}{\partial W^{[l]}} = \begin{bmatrix}
\frac{\partial \mathcal{L}}{\partial W_{11}} & \frac{\partial \mathcal{L}}{\partial W_{12}} & \dots & \frac{\partial \mathcal{L}}{\partial W_{1n}} \\[6pt]
\frac{\partial \mathcal{L}}{\partial W_{21}} & \frac{\partial \mathcal{L}}{\partial W_{22}} & \dots & \frac{\partial \mathcal{L}}{\partial W_{2n}} \\[6pt]
\vdots & \vdots & \ddots & \vdots \\[6pt]
\frac{\partial \mathcal{L}}{\partial W_{m1}} & \frac{\partial \mathcal{L}}{\partial W_{m2}} & \dots & \frac{\partial \mathcal{L}}{\partial W_{mn}}
\end{bmatrix} = \begin{bmatrix}
\delta_1 a_1 & \delta_1 a_2 & \dots & \delta_1 a_n \\[6pt]
\delta_2 a_1 & \delta_2 a_2 & \dots & \delta_2 a_n \\[6pt]
\vdots & \vdots & \ddots & \vdots \\[6pt]
\delta_m a_1 & \delta_m a_2 & \dots & \delta_m a_n
\end{bmatrix}$$

By **Rule 6 (Outer Product)**, this matrix is identical to multiplying column vector $\boldsymbol{\delta}^{[l]}$ by row vector $(\mathbf{a}^{[l-1]})^T$:

$$\begin{bmatrix} \delta_1 \\ \delta_2 \\ \vdots \\ \delta_m \end{bmatrix} \begin{bmatrix} a_1 & a_2 & \dots & a_n \end{bmatrix} = \Large \boldsymbol{\delta}^{[l]} \left(\mathbf{a}^{[l-1]}\right)^T$$

$$\Large \mathbf{\frac{\partial \mathcal{L}}{\partial W^{[l]}} = \boldsymbol{\delta}^{[l]} \left(\mathbf{a}^{[l-1]}\right)^T}$$

---

# 🏁 SECTION 6: The Complete Master Rosetta Summary

| Conceptual Step | Scalar Calculus with Indices | Vector / Matrix Formula | Why It Formatted This Way |
| :--- | :--- | :--- | :--- |
| **Local Weight Derivative** | $\frac{\partial z_i^{[l]}}{\partial W_{ij}^{[l]}} = a_j^{[l-1]}$ | $\left(\mathbf{a}^{[l-1]}\right)^T$ | Differentiating $W\mathbf{a} + \mathbf{b}$ w.r.t $W$ leaves input $a$. |
| **Activation Slope** | $\frac{\partial a_i^{[l]}}{\partial z_i^{[l]}} = g'(z_i^{[l]})$ | $g'\left(\mathbf{z}^{[l]}\right)$ | Differentiating non-linear function $g(z)$ w.r.t $z$. |
| **Upstream Error Flow** | $\frac{\partial \mathcal{L}}{\partial a_i^{[l]}} = \sum_k W_{ki}^{[l+1]} \delta_k^{[l+1]}$ | $(W^{[l+1]})^T \boldsymbol{\delta}^{[l+1]}$ | Summing all forward paths $k$ causes column indices to transpose into rows. |
| **Layer Error Signal ($\boldsymbol{\delta}$)** | $\delta_i^{[l]} = \left(\sum_k W_{ki} \delta_k\right) g'(z_i)$ | $\boldsymbol{\delta}^{[l]} = ((W^{[l+1]})^T \boldsymbol{\delta}^{[l+1]}) \odot g'(\mathbf{z}^{[l]})$ | Bundling upstream and activation slope into one reusable error term. |
| **Full Weight Gradient** | $\frac{\partial \mathcal{L}}{\partial W_{ij}^{[l]}} = \delta_i^{[l]} \cdot a_j^{[l-1]}$ | $\frac{\partial \mathcal{L}}{\partial W^{[l]}} = \boldsymbol{\delta}^{[l]} \left(\mathbf{a}^{[l-1]}\right)^T$ | Every $(i, j)$ element is a product, forming the matrix outer product. |
