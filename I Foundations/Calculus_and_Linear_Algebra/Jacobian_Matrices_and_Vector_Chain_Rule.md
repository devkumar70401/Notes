# 📐 Jacobian Matrices & Generalized Vector Chain Rule: The Foundation of Backpropagation

---

## 🧭 Learning Objectives

By working through this document, you will:
1. Understand why multivariable calculus naturally transitions from scalar multiplication to **Matrix Multiplication**.
2. Master the **Jacobian Matrix** as a structured table of first-order partial derivatives.
3. Trace every derivative step across **1-D**, **2-D**, **3-D**, and general **$N$-D** systems with zero skipped algebra.
4. Bridge pure multivariable calculus directly to **Reverse-Mode Automatic Differentiation (Backpropagation)** and PyTorch's Vector-Jacobian Product (VJP) engine.

---

## 1. The Core Problem: Why Scalar Calculus Breaks Down

In standard single-variable calculus, every function operates on a single scalar number:

$$x \in \mathbb{R} \xrightarrow{\quad f \quad} y \in \mathbb{R} \xrightarrow{\quad g \quad} L \in \mathbb{R}$$

When input $x$ is nudged by $\Delta x$, the rate of change propagating to $L$ is simply the product of two real numbers:

$$\frac{dL}{dx} = \frac{dL}{dy} \cdot \frac{dy}{dx}$$

### The Bottleneck in Real-World Systems & Neural Networks:
Real-world systems (neural networks, computer vision, robotics, economics) operate on **vectors (lists of numbers)**:
- Input $\mathbf{x} \in \mathbb{R}^n$ (e.g., $n$ features, pixels, or tokens)
- Intermediate representation $\mathbf{y} \in \mathbb{R}^m$ (e.g., $m$ hidden neurons)
- Scalar objective / Loss $L \in \mathbb{R}$ (e.g., Cross-Entropy, Mean Squared Error)

```text
               ┌──► y₁ ──┐
               │    ▲    │
               │    │    ▼
  [x₁, x₂] ────┼──► y₂ ──┼───► L (Scalar Loss)
               │    │    ▲
               │    ▼    │
               └──► y₃ ──┘
```

Because **every input $x_j$ influences every intermediate node $y_i$**, and **every intermediate node $y_i$ influences the final loss $L$**, there is no longer a single path. 

The change in $L$ with respect to $x_j$ is the **sum of changes along all possible intermediate pathways**.

---

## 2. Mathematical Definition: What is a Jacobian Matrix?

Let $\mathbf{f}: \mathbb{R}^n \to \mathbb{R}^m$ be a vector-valued function taking an $n$-dimensional input vector $\mathbf{x} = [x_1, x_2, \dots, x_n]^T$ and producing an $m$-dimensional output vector $\mathbf{y} = [y_1, y_2, \dots, y_m]^T$:

$$\mathbf{y} = \mathbf{f}(\mathbf{x}) = \begin{bmatrix} f_1(x_1, x_2, \dots, x_n) \\ f_2(x_1, x_2, \dots, x_n) \\ \vdots \\ f_m(x_1, x_2, \dots, x_n) \end{bmatrix}$$

The **Jacobian Matrix** $J_{\mathbf{x}} \mathbf{y} \in \mathbb{R}^{m \times n}$ is the organized $m \times n$ matrix containing all first-order partial derivatives:

$$J_{\mathbf{x}} \mathbf{y} = \frac{\partial \mathbf{y}}{\partial \mathbf{x}} = \begin{bmatrix}
\frac{\partial y_1}{\partial x_1} & \frac{\partial y_1}{\partial x_2} & \cdots & \frac{\partial y_1}{\partial x_n} \\[10pt]
\frac{\partial y_2}{\partial x_1} & \frac{\partial y_2}{\partial x_2} & \cdots & \frac{\partial y_2}{\partial x_n} \\[10pt]
\vdots & \vdots & \ddots & \vdots \\[10pt]
\frac{\partial y_m}{\partial x_1} & \frac{\partial y_m}{\partial x_2} & \cdots & \frac{\partial y_m}{\partial x_n}
\end{bmatrix}$$

- **Row $i$** describes how output component $y_i$ changes with respect to all inputs $x_1, \dots, x_n$.
- **Column $j$** describes how all outputs $y_1, \dots, y_m$ respond to a change in a single input $x_j$.

---

## 3. Detailed Walkthroughs: From 1-D to $N$-D

---

### 🔹 Example 1: 1-Dimensional Scalar Case ($1 \to 1 \to 1$)

#### Problem Setup
Let $x \in \mathbb{R}$ be a scalar input.
- Intermediate function: $y = f(x) = x^2 + 3x$
- Output loss function: $L = g(y) = 2y^3 + 5$

```text
x ────[ f(x) = x² + 3x ]────► y ────[ g(y) = 2y³ + 5 ]────► L
```

#### Step 1: Differentiate $y$ with respect to $x$
Using standard power rule:
$$\frac{dy}{dx} = \frac{d}{dx}\left(x^2 + 3x\right) = 2x + 3$$

#### Step 2: Differentiate $L$ with respect to $y$
$$\frac{dL}{dy} = \frac{d}{dy}\left(2y^3 + 5\right) = 6y^2$$

#### Step 3: Apply the 1-D Scalar Chain Rule
$$\frac{dL}{dx} = \frac{dL}{dy} \cdot \frac{dy}{dx} = \left(6y^2\right) \cdot (2x + 3)$$

Substitute $y = x^2 + 3x$ into the derivative:
$$\frac{dL}{dx} = 6(x^2 + 3x)^2 \cdot (2x + 3)$$

#### Step 4: Verification via Direct Algebraic Substitution
Compose the composite function directly:
$$L(x) = 2(x^2 + 3x)^3 + 5$$

Differentiate directly with respect to $x$:
$$\frac{dL}{dx} = 2 \cdot 3(x^2 + 3x)^{3-1} \cdot \frac{d}{dx}(x^2 + 3x) = 6(x^2 + 3x)^2(2x + 3)$$

$$\therefore \text{Chain Rule Result} \equiv \text{Direct Differentiation Result} \quad \checkmark$$

---

### 🔹 Example 2: 2-Dimensional Case ($2 \to 2 \to 1$)

#### Problem Setup
Let $\mathbf{x} = \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} \in \mathbb{R}^2$ be a 2-dimensional input vector.
- Vector transformation $\mathbf{y} = \mathbf{f}(\mathbf{x}) \in \mathbb{R}^2$:
  $$\begin{aligned}
  y_1 &= f_1(x_1, x_2) = 2x_1^2 + 3x_2 \\
  y_2 &= f_2(x_1, x_2) = x_1 x_2^2
  \end{aligned}$$
- Scalar Loss function $L = g(\mathbf{y}) \in \mathbb{R}$:
  $$L = g(y_1, y_2) = 3y_1^2 + 4y_2$$

```text
          ┌──(2x₁² + 3x₂)──► y₁ ──(3y₁²)──┐
          │                  ▲            │
[x₁, x₂] ─┤                  │            ├──► L
          │                  ▼            │
          └───(x₁ x₂²)─────► y₂ ──(4y₂)───┘
```

#### Step 1: Compute the $2 \times 2$ Jacobian Matrix $J_{\mathbf{x}} \mathbf{y}$
Compute each partial derivative step-by-step:
1. $\frac{\partial y_1}{\partial x_1} = \frac{\partial}{\partial x_1}(2x_1^2 + 3x_2) = 4x_1 + 0 = 4x_1$
2. $\frac{\partial y_1}{\partial x_2} = \frac{\partial}{\partial x_2}(2x_1^2 + 3x_2) = 0 + 3 = 3$
3. $\frac{\partial y_2}{\partial x_1} = \frac{\partial}{\partial x_1}(x_1 x_2^2) = 1 \cdot x_2^2 = x_2^2$
4. $\frac{\partial y_2}{\partial x_2} = \frac{\partial}{\partial x_2}(x_1 x_2^2) = x_1 \cdot (2x_2) = 2x_1 x_2$

Assembling the Jacobian matrix $J_{\mathbf{x}} \mathbf{y} \in \mathbb{R}^{2 \times 2}$:
$$J_{\mathbf{x}} \mathbf{y} = \begin{bmatrix}
\frac{\partial y_1}{\partial x_1} & \frac{\partial y_1}{\partial x_2} \\[8pt]
\frac{\partial y_2}{\partial x_1} & \frac{\partial y_2}{\partial x_2}
\end{bmatrix} = \begin{bmatrix}
4x_1 & 3 \\[8pt]
x_2^2 & 2x_1 x_2
\end{bmatrix}$$

#### Step 2: Compute the $1 \times 2$ Jacobian Matrix $J_{\mathbf{y}} L$
Differentiate $L = 3y_1^2 + 4y_2$ with respect to each component of $\mathbf{y}$:
1. $\frac{\partial L}{\partial y_1} = \frac{\partial}{\partial y_1}(3y_1^2 + 4y_2) = 6y_1 + 0 = 6y_1$
2. $\frac{\partial L}{\partial y_2} = \frac{\partial}{\partial y_2}(3y_1^2 + 4y_2) = 0 + 4 = 4$

Assembling the row vector $J_{\mathbf{y}} L \in \mathbb{R}^{1 \times 2}$:
$$J_{\mathbf{y}} L = \begin{bmatrix} \frac{\partial L}{\partial y_1} & \frac{\partial L}{\partial y_2} \end{bmatrix} = \begin{bmatrix} 6y_1 & 4 \end{bmatrix}$$

#### Step 3: Solve via Multivariable Total Derivative (Path Tracking)
To find $\frac{\partial L}{\partial x_1}$, sum over all pathways passing through $y_1$ and $y_2$:
$$\begin{aligned}
\frac{\partial L}{\partial x_1} &= \left(\frac{\partial L}{\partial y_1} \cdot \frac{\partial y_1}{\partial x_1}\right) + \left(\frac{\partial L}{\partial y_2} \cdot \frac{\partial y_2}{\partial x_1}\right) \\
&= (6y_1)(4x_1) + (4)(x_2^2) \\
&= 24x_1 y_1 + 4x_2^2
\end{aligned}$$

To find $\frac{\partial L}{\partial x_2}$, sum over all pathways:
$$\begin{aligned}
\frac{\partial L}{\partial x_2} &= \left(\frac{\partial L}{\partial y_1} \cdot \frac{\partial y_1}{\partial x_2}\right) + \left(\frac{\partial L}{\partial y_2} \cdot \frac{\partial y_2}{\partial x_2}\right) \\
&= (6y_1)(3) + (4)(2x_1 x_2) \\
&= 18y_1 + 8x_1 x_2
\end{aligned}$$

#### Step 4: Solve via Matrix Multiplication $(J_{\mathbf{y}} L)(J_{\mathbf{x}} \mathbf{y})$
Multiply row vector $(1 \times 2)$ by matrix $(2 \times 2)$:

$$\nabla_{\mathbf{x}} L = J_{\mathbf{y}} L \times J_{\mathbf{x}} \mathbf{y}$$

$$\begin{bmatrix} \frac{\partial L}{\partial x_1} & \frac{\partial L}{\partial x_2} \end{bmatrix} = \begin{bmatrix} 6y_1 & 4 \end{bmatrix} \times \begin{bmatrix} 4x_1 & 3 \\[8pt] x_2^2 & 2x_1 x_2 \end{bmatrix}$$

Carrying out the row-by-column dot product:
- **Column 1:** $(6y_1)(4x_1) + (4)(x_2^2) = 24x_1 y_1 + 4x_2^2$
- **Column 2:** $(6y_1)(3) + (4)(2x_1 x_2) = 18y_1 + 8x_1 x_2$

$$\nabla_{\mathbf{x}} L = \begin{bmatrix} 24x_1 y_1 + 4x_2^2 & 18y_1 + 8x_1 x_2 \end{bmatrix}$$

Substituting $y_1 = 2x_1^2 + 3x_2$:
$$\begin{aligned}
\frac{\partial L}{\partial x_1} &= 24x_1(2x_1^2 + 3x_2) + 4x_2^2 = 48x_1^3 + 72x_1 x_2 + 4x_2^2 \\
\frac{\partial L}{\partial x_2} &= 18(2x_1^2 + 3x_2) + 8x_1 x_2 = 36x_1^2 + 54x_2 + 8x_1 x_2
\end{aligned}$$

#### Step 5: Direct Verification via Full Algebraic Substitution
Substitute $y_1$ and $y_2$ directly into $L$:
$$L(x_1, x_2) = 3(2x_1^2 + 3x_2)^2 + 4(x_1 x_2^2)$$
$$L(x_1, x_2) = 3(4x_1^4 + 12x_1^2 x_2 + 9x_2^2) + 4x_1 x_2^2 = 12x_1^4 + 36x_1^2 x_2 + 27x_2^2 + 4x_1 x_2^2$$

Differentiate directly with respect to $x_1$:
$$\frac{\partial L}{\partial x_1} = 48x_1^3 + 72x_1 x_2 + 0 + 4x_2^2 = 48x_1^3 + 72x_1 x_2 + 4x_2^2 \quad \checkmark$$

Differentiate directly with respect to $x_2$:
$$\frac{\partial L}{\partial x_2} = 0 + 36x_1^2 + 54x_2 + 8x_1 x_2 = 36x_1^2 + 54x_2 + 8x_1 x_2 \quad \checkmark$$

---

### 🔹 Example 3: 3-Dimensional Case ($3 \to 3 \to 1$)

#### Problem Setup
Let $\mathbf{x} = \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix} \in \mathbb{R}^3$ be a 3-dimensional input vector.
- Vector function $\mathbf{y} = \mathbf{f}(\mathbf{x}) \in \mathbb{R}^3$:
  $$\begin{aligned}
  y_1 &= f_1(x_1, x_2, x_3) = x_1^2 + 2x_2 + x_3 \\
  y_2 &= f_2(x_1, x_2, x_3) = 3x_1 x_2 - x_3^2 \\
  y_3 &= f_3(x_1, x_2, x_3) = 2x_1 + x_2 x_3
  \end{aligned}$$
- Scalar Loss function $L = g(y_1, y_2, y_3) \in \mathbb{R}$:
  $$L = g(y_1, y_2, y_3) = y_1^2 + 2y_2 y_3$$

#### Step 1: Compute the $3 \times 3$ Jacobian Matrix $J_{\mathbf{x}} \mathbf{y}$
Compute each of the 9 partial derivatives:

**Row 1 (for $y_1$):**
- $\frac{\partial y_1}{\partial x_1} = \frac{\partial}{\partial x_1}(x_1^2 + 2x_2 + x_3) = 2x_1$
- $\frac{\partial y_1}{\partial x_2} = \frac{\partial}{\partial x_2}(x_1^2 + 2x_2 + x_3) = 2$
- $\frac{\partial y_1}{\partial x_3} = \frac{\partial}{\partial x_3}(x_1^2 + 2x_2 + x_3) = 1$

**Row 2 (for $y_2$):**
- $\frac{\partial y_2}{\partial x_1} = \frac{\partial}{\partial x_1}(3x_1 x_2 - x_3^2) = 3x_2$
- $\frac{\partial y_2}{\partial x_2} = \frac{\partial}{\partial x_2}(3x_1 x_2 - x_3^2) = 3x_1$
- $\frac{\partial y_2}{\partial x_3} = \frac{\partial}{\partial x_3}(3x_1 x_2 - x_3^2) = -2x_3$

**Row 3 (for $y_3$):**
- $\frac{\partial y_3}{\partial x_1} = \frac{\partial}{\partial x_1}(2x_1 + x_2 x_3) = 2$
- $\frac{\partial y_3}{\partial x_2} = \frac{\partial}{\partial x_2}(2x_1 + x_2 x_3) = x_3$
- $\frac{\partial y_3}{\partial x_3} = \frac{\partial}{\partial x_3}(2x_1 + x_2 x_3) = x_2$

Assembling the $3 \times 3$ Jacobian Matrix $J_{\mathbf{x}} \mathbf{y}$:
$$J_{\mathbf{x}} \mathbf{y} = \begin{bmatrix}
\frac{\partial y_1}{\partial x_1} & \frac{\partial y_1}{\partial x_2} & \frac{\partial y_1}{\partial x_3} \\[8pt]
\frac{\partial y_2}{\partial x_1} & \frac{\partial y_2}{\partial x_2} & \frac{\partial y_2}{\partial x_3} \\[8pt]
\frac{\partial y_3}{\partial x_1} & \frac{\partial y_3}{\partial x_2} & \frac{\partial y_3}{\partial x_3}
\end{bmatrix} = \begin{bmatrix}
2x_1 & 2 & 1 \\[8pt]
3x_2 & 3x_1 & -2x_3 \\[8pt]
2 & x_3 & x_2
\end{bmatrix}$$

#### Step 2: Compute the $1 \times 3$ Jacobian Matrix $J_{\mathbf{y}} L$
Differentiate $L = y_1^2 + 2y_2 y_3$ with respect to each component:
- $\frac{\partial L}{\partial y_1} = \frac{\partial}{\partial y_1}(y_1^2 + 2y_2 y_3) = 2y_1$
- $\frac{\partial L}{\partial y_2} = \frac{\partial}{\partial y_2}(y_1^2 + 2y_2 y_3) = 2y_3$
- $\frac{\partial L}{\partial y_3} = \frac{\partial}{\partial y_3}(y_1^2 + 2y_2 y_3) = 2y_2$

Assembling $J_{\mathbf{y}} L \in \mathbb{R}^{1 \times 3}$:
$$J_{\mathbf{y}} L = \begin{bmatrix} \frac{\partial L}{\partial y_1} & \frac{\partial L}{\partial y_2} & \frac{\partial L}{\partial y_3} \end{bmatrix} = \begin{bmatrix} 2y_1 & 2y_3 & 2y_2 \end{bmatrix}$$

#### Step 3: Compute Matrix Product $(J_{\mathbf{y}} L)(J_{\mathbf{x}} \mathbf{y})$
Multiply $(1 \times 3)$ by $(3 \times 3)$:

$$\nabla_{\mathbf{x}} L = \begin{bmatrix} 2y_1 & 2y_3 & 2y_2 \end{bmatrix} \times \begin{bmatrix}
2x_1 & 2 & 1 \\[8pt]
3x_2 & 3x_1 & -2x_3 \\[8pt]
2 & x_3 & x_2
\end{bmatrix}$$

**Step-by-step dot products for each column:**

1. **For Column 1 ($\frac{\partial L}{\partial x_1}$):**
   $$\frac{\partial L}{\partial x_1} = (2y_1)(2x_1) + (2y_3)(3x_2) + (2y_2)(2) = 4x_1 y_1 + 6x_2 y_3 + 4y_2$$

2. **For Column 2 ($\frac{\partial L}{\partial x_2}$):**
   $$\frac{\partial L}{\partial x_2} = (2y_1)(2) + (2y_3)(3x_1) + (2y_2)(x_3) = 4y_1 + 6x_1 y_3 + 2x_3 y_2$$

3. **For Column 3 ($\frac{\partial L}{\partial x_3}$):**
   $$\frac{\partial L}{\partial x_3} = (2y_1)(1) + (2y_3)(-2x_3) + (2y_2)(x_2) = 2y_1 - 4x_3 y_3 + 2x_2 y_2$$

Resulting Gradient Row Vector:
$$\nabla_{\mathbf{x}} L = \begin{bmatrix} 4x_1 y_1 + 6x_2 y_3 + 4y_2 & 4y_1 + 6x_1 y_3 + 2x_3 y_2 & 2y_1 - 4x_3 y_3 + 2x_2 y_2 \end{bmatrix}$$

---

### 🔹 Example 4: The General $N$-Dimensional Vector Case ($n \to m \to 1$)

#### Problem Setup
Let:
- $\mathbf{x} = \begin{bmatrix} x_1, x_2, \dots, x_n \end{bmatrix}^T \in \mathbb{R}^n$
- $\mathbf{y} = \mathbf{f}(\mathbf{x}) = \begin{bmatrix} y_1, y_2, \dots, y_m \end{bmatrix}^T \in \mathbb{R}^m$ where each $y_i = f_i(x_1, x_2, \dots, x_n)$
- $L = g(\mathbf{y}) \in \mathbb{R}$ where $L = g(y_1, y_2, \dots, y_m)$

```text
                   ┌──► y₁ ──┐
                   │    ▲    │
[x₁, x₂, ..., xₙ] ─┼──► y₂ ──┼───► L (Scalar)
   (n inputs)      │    ⋮    │   (1 output)
                   └──► yₘ ──┘
                   (m outputs)
```

#### Step 1: The Total Derivative Formula
According to multivariable calculus, the total rate of change of $L$ with respect to any single input component $x_j$ (for $j \in \{1, 2, \dots, n\}$) is the sum of changes over all $m$ intermediate paths:

$$\frac{\partial L}{\partial x_j} = \sum_{i=1}^m \frac{\partial L}{\partial y_i} \cdot \frac{\partial y_i}{\partial x_j}$$

Expanded out with ellipses ($\cdots$):
$$\frac{\partial L}{\partial x_j} = \left(\frac{\partial L}{\partial y_1} \frac{\partial y_1}{\partial x_j}\right) + \left(\frac{\partial L}{\partial y_2} \frac{\partial y_2}{\partial x_j}\right) + \cdots + \left(\frac{\partial L}{\partial y_m} \frac{\partial y_m}{\partial x_j}\right)$$

#### Step 2: Formulating the Vector Matrices
Define the $1 \times m$ Jacobian of $L$ with respect to $\mathbf{y}$:
$$J_{\mathbf{y}} L = \begin{bmatrix} \frac{\partial L}{\partial y_1} & \frac{\partial L}{\partial y_2} & \cdots & \frac{\partial L}{\partial y_m} \end{bmatrix} \in \mathbb{R}^{1 \times m}$$

Define the $m \times n$ Jacobian of $\mathbf{y}$ with respect to $\mathbf{x}$:
$$J_{\mathbf{x}} \mathbf{y} = \begin{bmatrix}
\frac{\partial y_1}{\partial x_1} & \frac{\partial y_1}{\partial x_2} & \cdots & \frac{\partial y_1}{\partial x_n} \\[8pt]
\frac{\partial y_2}{\partial x_1} & \frac{\partial y_2}{\partial x_2} & \cdots & \frac{\partial y_2}{\partial x_n} \\[8pt]
\vdots & \vdots & \ddots & \vdots \\[8pt]
\frac{\partial y_m}{\partial x_1} & \frac{\partial y_m}{\partial x_2} & \cdots & \frac{\partial y_m}{\partial x_n}
\end{bmatrix} \in \mathbb{R}^{m \times n}$$

#### Step 3: Matrix Multiplication Identity
Perform standard matrix multiplication $(1 \times m) \times (m \times n) = (1 \times n)$:

$$\nabla_{\mathbf{x}} L = (J_{\mathbf{y}} L) \times (J_{\mathbf{x}} \mathbf{y})$$

$$\begin{bmatrix} \frac{\partial L}{\partial x_1} & \frac{\partial L}{\partial x_2} & \cdots & \frac{\partial L}{\partial x_n} \end{bmatrix} = \begin{bmatrix} \frac{\partial L}{\partial y_1} & \frac{\partial L}{\partial y_2} & \cdots & \frac{\partial L}{\partial y_m} \end{bmatrix} \times \begin{bmatrix}
\frac{\partial y_1}{\partial x_1} & \frac{\partial y_1}{\partial x_2} & \cdots & \frac{\partial y_1}{\partial x_n} \\[8pt]
\frac{\partial y_2}{\partial x_1} & \frac{\partial y_2}{\partial x_2} & \cdots & \frac{\partial y_2}{\partial x_n} \\[8pt]
\vdots & \vdots & \ddots & \vdots \\[8pt]
\frac{\partial y_m}{\partial x_1} & \frac{\partial y_m}{\partial x_2} & \cdots & \frac{\partial y_m}{\partial x_n}
\end{bmatrix}$$

For any column $j \in \{1, \dots, n\}$, the $j$-th entry of the product is:
$$[\nabla_{\mathbf{x}} L]_j = \sum_{i=1}^m (J_{\mathbf{y}} L)_i \cdot (J_{\mathbf{x}} \mathbf{y})_{ij} = \sum_{i=1}^m \frac{\partial L}{\partial y_i} \frac{\partial y_i}{\partial x_j}$$

This matches the multivariable total derivative **identically**.

---

## 4. Deep Neural Network Generalization ($K$ Layers)

Consider a deep neural network with $K$ hidden layers:

$$\mathbf{x} = \mathbf{h}_0 \xrightarrow{\mathbf{f}_1} \mathbf{h}_1 \xrightarrow{\mathbf{f}_2} \mathbf{h}_2 \xrightarrow{\mathbf{f}_3} \cdots \xrightarrow{\mathbf{f}_K} \mathbf{h}_K \xrightarrow{g} L$$

Where:
- $\mathbf{h}_0 \in \mathbb{R}^{d_0}$
- $\mathbf{h}_l \in \mathbb{R}^{d_l}$ for each layer $l \in \{1, 2, \dots, K\}$
- $L \in \mathbb{R}$ (Scalar loss)

### The Backpropagation Matrix Chain:
Applying the vector chain rule recursively from the output layer backwards:

$$\nabla_{\mathbf{x}} L = (J_{\mathbf{h}_K} L) \cdot (J_{\mathbf{h}_{K-1}} \mathbf{h}_K) \cdot (J_{\mathbf{h}_{K-2}} \mathbf{h}_{K-1}) \cdots (J_{\mathbf{h}_1} \mathbf{h}_2) \cdot (J_{\mathbf{x}} \mathbf{h}_1)$$

Using product notation:
$$\nabla_{\mathbf{x}} L = (J_{\mathbf{h}_K} L) \prod_{l=K}^1 J_{\mathbf{h}_{l-1}} \mathbf{h}_l$$

---

## 5. Production Insight: How PyTorch Implements This (VJPs)

In deep learning frameworks like **PyTorch** and **JAX**, constructing and storing a full $m \times n$ Jacobian matrix (which could be $100{,}000 \times 100{,}000 = 10 \text{ billion elements} \approx 40 \text{ GB}$) is too memory intensive.

Instead, PyTorch computes **Vector-Jacobian Products (VJP)**:
Given an incoming gradient row vector $\mathbf{v} = J_{\mathbf{y}} L \in \mathbb{R}^{1 \times m}$, it directly evaluates:

$$\text{vjp}(\mathbf{v}) = \mathbf{v} \cdot J_{\mathbf{x}} \mathbf{y}$$

This evaluates the product in $O(m \cdot n)$ time without ever allocating memory for the full Jacobian matrix in GPU VRAM!

---

## 6. Summary Comparison Table

| Dimension | Input $\mathbf{x}$ | Intermediate $\mathbf{y}$ | Output $L$ | Jacobian $J_{\mathbf{x}} \mathbf{y}$ Shape | Jacobian $J_{\mathbf{y}} L$ Shape | Chain Rule Expression |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **1-D (Scalar)** | $\mathbb{R}^1$ | $\mathbb{R}^1$ | $\mathbb{R}^1$ | $1 \times 1$ (scalar) | $1 \times 1$ (scalar) | $\frac{dL}{dx} = \frac{dL}{dy} \cdot \frac{dy}{dx}$ |
| **2-D** | $\mathbb{R}^2$ | $\mathbb{R}^2$ | $\mathbb{R}^1$ | $2 \times 2$ matrix | $1 \times 2$ row vector | $\nabla_{\mathbf{x}} L = (J_{\mathbf{y}} L)_{1 \times 2} (J_{\mathbf{x}} \mathbf{y})_{2 \times 2}$ |
| **3-D** | $\mathbb{R}^3$ | $\mathbb{R}^3$ | $\mathbb{R}^1$ | $3 \times 3$ matrix | $1 \times 3$ row vector | $\nabla_{\mathbf{x}} L = (J_{\mathbf{y}} L)_{1 \times 3} (J_{\mathbf{x}} \mathbf{y})_{3 \times 3}$ |
| **$N$-D General** | $\mathbb{R}^n$ | $\mathbb{R}^m$ | $\mathbb{R}^1$ | $m \times n$ matrix | $1 \times m$ row vector | $\nabla_{\mathbf{x}} L = (J_{\mathbf{y}} L)_{1 \times m} (J_{\mathbf{x}} \mathbf{y})_{m \times n}$ |
| **$K$-Layer Deep Net** | $\mathbb{R}^{d_0}$ | $\mathbb{R}^{d_l}$ | $\mathbb{R}^1$ | Sequence of $d_l \times d_{l-1}$ matrices | $1 \times d_K$ row vector | $\nabla_{\mathbf{x}} L = (J_{\mathbf{h}_K} L) \prod_{l=K}^1 J_{\mathbf{h}_{l-1}} \mathbf{h}_l$ |
