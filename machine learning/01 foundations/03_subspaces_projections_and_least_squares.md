# Machine Learning Foundations: Chapter 3 — Four Fundamental Subspaces, Projections, and Least Squares

---

## 1. The Four Fundamental Subspaces of a Matrix

### A. Motivation: System of Linear Equations $Ax = b$
In Machine Learning and data science, linear systems appear everywhere: from linear regression and feature projections to dimensionality reduction and optimization. A linear system of $m$ equations in $n$ unknowns can be represented compactly as:

$$A\mathbf{x} = \mathbf{b}$$

where:
* $A \in \mathbb{R}^{m \times n}$ is the coefficient matrix.
* $\mathbf{x} \in \mathbb{R}^n$ is the input vector (unknown parameters or weights).
* $\mathbf{b} \in \mathbb{R}^m$ is the observation or target vector.

```
       Matrix A (m x n)            Input x (n x 1)       Output b (m x 1)
   ┌                        ┐       ┌          ┐           ┌          ┐
   │ a_11  a_12  ...  a_1n  │       │   x_1    │           │   b_1    │
   │ a_21  a_22  ...  a_2n  │   *   │   x_2    │     =     │   b_2    │
   │  :     :    ...   :    │       │    :     │           │    :     │
   │ a_m1  a_m2  ...  a_mn  │       │   x_n    │           │   b_m    │
   └                        ┘       └          ┘           └          ┘
```

The matrix $A$ acts as a linear transformation mapping vectors from the $n$-dimensional domain space $\mathbb{R}^n$ into the $m$-dimensional codomain space $\mathbb{R}^m$:

$$A: \mathbb{R}^n \to \mathbb{R}^m$$

#### Fundamental Questions of Solvability:
1. **Existence:** Under what conditions on $\mathbf{b}$ does the system $A\mathbf{x} = \mathbf{b}$ have at least one solution?
   * *Answer:* A solution exists if and only if $\mathbf{b}$ can be written as a linear combination of the columns of $A$, meaning $\mathbf{b}$ lies in the **column space** of $A$ ($\mathbf{b} \in C(A)$).
2. **Uniqueness:** If a solution exists, when is it unique, and when are there infinitely many solutions?
   * *Answer:* The uniqueness of the solution depends entirely on whether there are non-zero vectors $\mathbf{x}$ mapped to zero ($A\mathbf{x} = \mathbf{0}$), which is governed by the **nullspace** of $A$ ($N(A)$).

To answer these questions completely and geometrically, linear algebra defines the **Four Fundamental Subspaces** associated with any matrix $A$.

---

### B. Formal Definitions of the Four Subspaces
Let $A$ be an $m \times n$ real matrix of rank $r$.

| Subspace | Symbol | Ambient Space | Dimension | Defining Condition |
| :--- | :---: | :---: | :---: | :--- |
| **Column Space** | $C(A)$ | $\mathbb{R}^m$ | $r$ | $\{A\mathbf{x} \mid \mathbf{x} \in \mathbb{R}^n\}$ |
| **Nullspace** (Kernel) | $N(A)$ | $\mathbb{R}^n$ | $n - r$ | $\{\mathbf{x} \in \mathbb{R}^n \mid A\mathbf{x} = \mathbf{0}\}$ |
| **Row Space** | $C(A^\top)$ or $R(A)$ | $\mathbb{R}^n$ | $r$ | $\{A^\top \mathbf{y} \mid \mathbf{y} \in \mathbb{R}^m\}$ |
| **Left Nullspace** | $N(A^\top)$ | $\mathbb{R}^m$ | $m - r$ | $\{\mathbf{y} \in \mathbb{R}^m \mid A^\top \mathbf{y} = \mathbf{0}\}$ |

#### 1. Column Space $C(A)$
* **Definition:** The set of all linear combinations of the columns of $A$. Writing $A = \begin{bmatrix} \mathbf{a}_1 & \mathbf{a}_2 & \dots & \mathbf{a}_n \end{bmatrix}$, where each $\mathbf{a}_j \in \mathbb{R}^m$:
  $$C(A) = \left\{ \sum_{j=1}^n x_j \mathbf{a}_j \;\middle|\; x_j \in \mathbb{R} \right\} = \{A\mathbf{x} \mid \mathbf{x} \in \mathbb{R}^n\}$$
* **Ambient Space:** Subspace of $\mathbb{R}^m$.
* **Dimension:** $\dim(C(A)) = r$ (the column rank of $A$).
* **Solvability Criterion:**
  $$A\mathbf{x} = \mathbf{b} \text{ has a solution} \iff \mathbf{b} \in C(A)$$

#### 2. Nullspace $N(A)$
* **Definition:** The set of all vectors $\mathbf{x} \in \mathbb{R}^n$ that the matrix $A$ multiplies to the zero vector in $\mathbb{R}^m$:
  $$N(A) = \{\mathbf{x} \in \mathbb{R}^n \mid A\mathbf{x} = \mathbf{0}\}$$
* **Ambient Space:** Subspace of $\mathbb{R}^n$.
* **Dimension:** $\dim(N(A)) = n - r$ (termed the **nullity** of $A$).
* **Significance:** Measures the degrees of freedom or redundancy in the solution space. If $\mathbf{x}_p$ is a particular solution to $A\mathbf{x} = \mathbf{b}$, the complete set of solutions is:
  $$\mathbf{x} = \mathbf{x}_p + \mathbf{x}_n, \quad \text{where } \mathbf{x}_n \in N(A)$$

#### 3. Row Space $R(A) = C(A^\top)$
* **Definition:** The set of all linear combinations of the rows of $A$, which is equivalent to the column space of the transpose matrix $A^\top$:
  $$R(A) = C(A^\top) = \{A^\top \mathbf{y} \mid \mathbf{y} \in \mathbb{R}^m\}$$
* **Ambient Space:** Subspace of $\mathbb{R}^n$.
* **Dimension:** $\dim(R(A)) = r$.
  > **Fundamental Fact:** Row rank equals column rank ($r$). The number of linearly independent rows of any matrix is always equal to the number of linearly independent columns.

#### 4. Left Nullspace $N(A^\top)$
* **Definition:** The nullspace of the transpose matrix $A^\top$. It consists of all vectors $\mathbf{y} \in \mathbb{R}^m$ such that $A^\top \mathbf{y} = \mathbf{0}$:
  $$N(A^\top) = \{\mathbf{y} \in \mathbb{R}^m \mid A^\top \mathbf{y} = \mathbf{0}\}$$
* **Equivalent Left-Multiplication Form:**
  $$(A^\top \mathbf{y})^\top = \mathbf{0}^\top \iff \mathbf{y}^\top A = \mathbf{0}^\top$$
  Because $\mathbf{y}^\top$ multiplies $A$ on the left, it is designated as the **left nullspace**.
* **Ambient Space:** Subspace of $\mathbb{R}^m$.
* **Dimension:** $\dim(N(A^\top)) = m - r$.

---

### C. The Big Picture of Linear Algebra (Gilbert Strang Diagram)
The four fundamental subspaces completely characterize how a matrix transforms $\mathbb{R}^n$ into $\mathbb{R}^m$. 

```
          DOMAIN SPACE: R^n                                CODOMAIN SPACE: R^m
  ┌─────────────────────────────────┐              ┌─────────────────────────────────┐
  │                                 │              │                                 │
  │        Row Space C(A^T)         │              │        Column Space C(A)        │
  │          Dimension: r           │              │          Dimension: r           │
  │                                 │  x_r ────> A ───> A(x_r)                       │
  │                                 │              │                                 │
  │─────── ┴ (Orthogonal) ──────────│              │─────── ┴ (Orthogonal) ──────────│
  │                                 │              │                                 │
  │          Nullspace N(A)         │              │     Left Nullspace N(A^T)       │
  │        Dimension: n - r         │              │        Dimension: m - r         │
  │                                 │  x_n ────> A ───> 0                            │
  │                                 │              │                                 │
  └─────────────────────────────────┘              └─────────────────────────────────┘
```

#### Mapping Properties of $A$:
1. Every vector $\mathbf{x} \in \mathbb{R}^n$ decomposes uniquely into an orthogonal sum:
   $$\mathbf{x} = \mathbf{x}_r + \mathbf{x}_n, \quad \text{where } \mathbf{x}_r \in C(A^\top) \text{ and } \mathbf{x}_n \in N(A)$$
2. Matrix $A$ maps the nullspace component strictly to zero:
   $$A\mathbf{x}_n = \mathbf{0}$$
3. Matrix $A$ maps the row space component $\mathbf{x}_r$ one-to-one (invertibly) onto the column space $C(A)$:
   $$A\mathbf{x} = A(\mathbf{x}_r + \mathbf{x}_n) = A\mathbf{x}_r \in C(A)$$
   If $\mathbf{x}_r \in C(A^\top)$ and $A\mathbf{x}_r = \mathbf{0}$, then $\mathbf{x}_r \in C(A^\top) \cap N(A) = \{\mathbf{0}\}$. Hence, no two distinct vectors in the row space map to the same vector in the column space.

---

### D. The Rank-Nullity Theorem and Dimensionality Relations
The fundamental theorem connects the dimension of the domain space with the rank and nullity of the linear transformation.

#### Rank-Nullity Theorem (in $\mathbb{R}^n$):
For any $m \times n$ matrix $A$ of rank $r$:
$$\dim(C(A)) + \dim(N(A)) = n$$
$$\text{Rank}(A) + \text{Nullity}(A) = n$$
$$r + (n - r) = n$$

#### Dimensional Relation in $\mathbb{R}^m$:
For the transpose matrix $A^\top$ (which has size $n \times m$ and rank $r$):
$$\dim(C(A^\top)) + \dim(N(A^\top)) = m$$
$$r + (m - r) = m$$

```
Domain Space R^n:      Dimension = r + (n - r) = n  (Row Space + Nullspace)
Codomain Space R^m:    Dimension = r + (m - r) = m  (Column Space + Left Nullspace)
```

---

### E. Systematic Computation via Gaussian Elimination & RREF
To find explicit bases and dimensions for all four subspaces:

1. **Reduce $A$ to Row Echelon Form ($U$) or Reduced Row Echelon Form ($R$):**
   Perform elementary row operations ($A \xrightarrow{\text{elimination}} U \xrightarrow{\text{RREF}} R$).
2. **Column Space $C(A)$:**
   Identify the **pivot columns** in $U$ (or $R$). The *original* columns of matrix $A$ at those corresponding pivot indices form a basis for $C(A)$.
   > [!IMPORTANT]
   > Do **not** take the columns of $U$ or $R$ as the basis for $C(A)$, because row operations alter the column space! Always take the pivot columns from the original matrix $A$.
3. **Row Space $R(A) = C(A^\top)$:**
   Row operations do not alter the linear combinations of rows! Therefore, the $r$ non-zero rows of $U$ (or of $R$) form a valid, orthogonal-ready basis for the row space $R(A)$.
4. **Nullspace $N(A)$:**
   Solve the homogeneous system $U\mathbf{x} = \mathbf{0}$ (or $R\mathbf{x} = \mathbf{0}$).
   * Express the $r$ pivot variables in terms of the $n - r$ free variables.
   * Generate the $n - r$ **special solutions** by setting each free variable to $1$ in turn while setting all other free variables to $0$.
   * These special solutions form a basis for $N(A)$.
5. **Left Nullspace $N(A^\top)$:**
   Solve $A^\top \mathbf{y} = \mathbf{0}$.
   * Alternatively, track the elementary row operations that reduce $A$ to $U$. Any row operations that produce a zero row in $U$ represent a linear combination of the rows of $A$ that equals $\mathbf{0}^\top$, yielding a basis vector for $N(A^\top)$.

---

### F. Lecture Worked Examples

#### Example 1: Matrix with Dependent Columns
Consider the $4 \times 3$ matrix:
$$A = \begin{bmatrix} 1 & 1 & 2 \\ 2 & 1 & 3 \\ 3 & 1 & 4 \\ 4 & 1 & 5 \end{bmatrix}$$

* **Column Analysis:**
  Notice that:
  $$\text{col}_3 = \text{col}_1 + \text{col}_2$$
  Since column 1 and column 2 are linearly independent, the rank of $A$ is $r = 2$.
* **Column Space $C(A)$:**
  $$\dim(C(A)) = r = 2, \quad \text{Basis} = \left\{ \begin{bmatrix} 1 \\ 2 \\ 3 \\ 4 \end{bmatrix}, \begin{bmatrix} 1 \\ 1 \\ 1 \\ 1 \end{bmatrix} \right\}$$
* **Nullspace $N(A)$:**
  We seek $\mathbf{x} \in \mathbb{R}^3$ such that $A\mathbf{x} = \mathbf{0}$:
  $$x_1 \begin{bmatrix} 1 \\ 2 \\ 3 \\ 4 \end{bmatrix} + x_2 \begin{bmatrix} 1 \\ 1 \\ 1 \\ 1 \end{bmatrix} + x_3 \begin{bmatrix} 2 \\ 3 \\ 4 \\ 5 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \\ 0 \\ 0 \end{bmatrix}$$
  Since $\text{col}_1 + \text{col}_2 - \text{col}_3 = \mathbf{0}$, setting $x_1 = 1, x_2 = 1, x_3 = -1$ gives:
  $$\mathbf{x} = \begin{bmatrix} 1 \\ 1 \\ -1 \end{bmatrix}$$
  $$\dim(N(A)) = n - r = 3 - 2 = 1, \quad N(A) = \operatorname{span}\left\{ \begin{bmatrix} 1 \\ 1 \\ -1 \end{bmatrix} \right\}$$
* **Verification:**
  $\dim(C(A)) + \dim(N(A)) = 2 + 1 = 3 = n$.

---

#### Example 2: Complete $3 \times 4$ Gaussian Elimination
Consider the $3 \times 4$ matrix:
$$A = \begin{bmatrix} 1 & 2 & 2 & 2 \\ 2 & 4 & 6 & 8 \\ 3 & 6 & 8 & 10 \end{bmatrix}$$

##### Step 1: Forward Elimination to Row Echelon Form $U$
* $R_2 \leftarrow R_2 - 2R_1$:
  $$\begin{bmatrix} 2 & 4 & 6 & 8 \end{bmatrix} - 2\begin{bmatrix} 1 & 2 & 2 & 2 \end{bmatrix} = \begin{bmatrix} 0 & 0 & 2 & 4 \end{bmatrix}$$
* $R_3 \leftarrow R_3 - 3R_1$:
  $$\begin{bmatrix} 3 & 6 & 8 & 10 \end{bmatrix} - 3\begin{bmatrix} 1 & 2 & 2 & 2 \end{bmatrix} = \begin{bmatrix} 0 & 0 & 2 & 4 \end{bmatrix}$$
* $R_3 \leftarrow R_3 - R_2$:
  $$\begin{bmatrix} 0 & 0 & 2 & 4 \end{bmatrix} - \begin{bmatrix} 0 & 0 & 2 & 4 \end{bmatrix} = \begin{bmatrix} 0 & 0 & 0 & 0 \end{bmatrix}$$

The resulting echelon matrix is:
$$U = \begin{bmatrix} \mathbf{1} & 2 & 2 & 2 \\ 0 & 0 & \mathbf{2} & 4 \\ 0 & 0 & 0 & 0 \end{bmatrix}$$

* **Pivot Columns:** Column 1 and Column 3.
* **Free Columns:** Column 2 and Column 4.
* **Rank:** $r = 2$.

##### Step 2: Subspace Dimensions and Bases
1. **Column Space $C(A) \subseteq \mathbb{R}^3$:**
   $$\dim(C(A)) = r = 2$$
   Basis consists of the pivot columns of the *original* matrix $A$:
   $$\text{Basis}(C(A)) = \left\{ \begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix}, \begin{bmatrix} 2 \\ 6 \\ 8 \end{bmatrix} \right\}$$

2. **Nullspace $N(A) \subseteq \mathbb{R}^4$:**
   $$\dim(N(A)) = n - r = 4 - 2 = 2$$
   Solving $U\mathbf{x} = \mathbf{0}$:
   $$\begin{aligned}
   x_1 + 2x_2 + 2x_3 + 2x_4 &= 0 \quad \text{--- (1)} \\
   2x_3 + 4x_4 &= 0 \implies x_3 = -2x_4 \quad \text{--- (2)}
   \end{aligned}$$
   
   * **Special Solution 1:** Set free variable $x_2 = 1, x_4 = 0$:
     * From (2): $x_3 = 0$.
     * From (1): $x_1 + 2(1) + 2(0) + 2(0) = 0 \implies x_1 = -2$.
     $$\mathbf{u} = \begin{bmatrix} -2 \\ 1 \\ 0 \\ 0 \end{bmatrix}$$
   
   * **Special Solution 2:** Set free variable $x_2 = 0, x_4 = 1$:
     * From (2): $x_3 = -2(1) = -2$.
     * From (1): $x_1 + 2(0) + 2(-2) + 2(1) = 0 \implies x_1 - 2 = 0 \implies x_1 = 2$.
     $$\mathbf{v} = \begin{bmatrix} 2 \\ 0 \\ -2 \\ 1 \end{bmatrix}$$

   $$N(A) = \operatorname{span}\left\{ \begin{bmatrix} -2 \\ 1 \\ 0 \\ 0 \end{bmatrix}, \begin{bmatrix} 2 \\ 0 \\ -2 \\ 1 \end{bmatrix} \right\}$$

3. **Row Space $R(A) \subseteq \mathbb{R}^4$:**
   $$\dim(R(A)) = r = 2$$
   Basis consists of the non-zero rows of $U$:
   $$\text{Basis}(R(A)) = \left\{ \begin{bmatrix} 1 \\ 2 \\ 2 \\ 2 \end{bmatrix}, \begin{bmatrix} 0 \\ 0 \\ 2 \\ 4 \end{bmatrix} \right\}$$

4. **Left Nullspace $N(A^\top) \subseteq \mathbb{R}^3$:**
   $$\dim(N(A^\top)) = m - r = 3 - 2 = 1$$
   Recall our elimination step that led to the row of zeros in $U$:
   $$R_3 - R_2 \implies (R_3 - 3R_1) - (R_2 - 2R_1) = -R_1 - R_2 + R_3 = \mathbf{0}^\top$$
   $$\implies \begin{bmatrix} 1 & 1 & -1 \end{bmatrix} \begin{bmatrix} R_1 \\ R_2 \\ R_3 \end{bmatrix} = \mathbf{0}^\top$$
   Equivalently, solving $A^\top \mathbf{y} = \mathbf{0}$ yields:
   $$N(A^\top) = \operatorname{span}\left\{ \begin{bmatrix} 1 \\ 1 \\ -1 \end{bmatrix} \right\}$$

---

#### Example 3: $2 \times 2$ Rank-1 Matrix Geometry
Consider:
$$A = \begin{bmatrix} 1 & 2 \\ 3 & 6 \end{bmatrix}$$
* $R_2 \leftarrow R_2 - 3R_1 \implies U = \begin{bmatrix} 1 & 2 \\ 0 & 0 \end{bmatrix}$. Rank $r = 1$.
* **Four Subspaces:**
  * $C(A) = \operatorname{span}\left\{ \begin{bmatrix} 1 \\ 3 \end{bmatrix} \right\} \subseteq \mathbb{R}^2$ ($\dim = 1$, line in $\mathbb{R}^2$).
  * $R(A) = \operatorname{span}\left\{ \begin{bmatrix} 1 \\ 2 \end{bmatrix} \right\} \subseteq \mathbb{R}^2$ ($\dim = 1$, line in $\mathbb{R}^2$).
  * $N(A)$: $x_1 + 2x_2 = 0 \implies \mathbf{x} = \begin{bmatrix} -2 \\ 1 \end{bmatrix} \implies N(A) = \operatorname{span}\left\{ \begin{bmatrix} -2 \\ 1 \end{bmatrix} \right\} \subseteq \mathbb{R}^2$ ($\dim = 1$).
  * $N(A^\top)$: $y_1 + 3y_2 = 0 \implies \mathbf{y} = \begin{bmatrix} -3 \\ 1 \end{bmatrix} \implies N(A^\top) = \operatorname{span}\left\{ \begin{bmatrix} -3 \\ 1 \end{bmatrix} \right\} \subseteq \mathbb{R}^2$ ($\dim = 1$).
* **Orthogonality Check:**
  * In domain $\mathbb{R}^2$:
    $$\begin{bmatrix} 1 \\ 2 \end{bmatrix} \cdot \begin{bmatrix} -2 \\ 1 \end{bmatrix} = 1(-2) + 2(1) = 0 \implies R(A) \perp N(A)$$
  * In codomain $\mathbb{R}^2$:
    $$\begin{bmatrix} 1 \\ 3 \end{bmatrix} \cdot \begin{bmatrix} -3 \\ 1 \end{bmatrix} = 1(-3) + 3(1) = 0 \implies C(A) \perp N(A^\top)$$

---

#### Lecture Homework Matrix: Complete Solution
Matrix given for practice in lecture:
$$A = \begin{bmatrix} 1 & 3 & 3 & 2 \\ 2 & 6 & 9 & 7 \\ -1 & -3 & 3 & 4 \end{bmatrix}$$

##### Row Reduction:
* $R_2 \leftarrow R_2 - 2R_1$:
  $$\begin{bmatrix} 2 & 6 & 9 & 7 \end{bmatrix} - 2\begin{bmatrix} 1 & 3 & 3 & 2 \end{bmatrix} = \begin{bmatrix} 0 & 0 & 3 & 3 \end{bmatrix}$$
* $R_3 \leftarrow R_3 + R_1$:
  $$\begin{bmatrix} -1 & -3 & 3 & 4 \end{bmatrix} + \begin{bmatrix} 1 & 3 & 3 & 2 \end{bmatrix} = \begin{bmatrix} 0 & 0 & 6 & 6 \end{bmatrix}$$
* $R_3 \leftarrow R_3 - 2R_2$:
  $$\begin{bmatrix} 0 & 0 & 6 & 6 \end{bmatrix} - 2\begin{bmatrix} 0 & 0 & 3 & 3 \end{bmatrix} = \begin{bmatrix} 0 & 0 & 0 & 0 \end{bmatrix}$$

$$U = \begin{bmatrix} \mathbf{1} & 3 & 3 & 2 \\ 0 & 0 & \mathbf{3} & 3 \\ 0 & 0 & 0 & 0 \end{bmatrix}$$

Divide $R_2$ by $3$ and eliminate upwards ($R_1 \leftarrow R_1 - R_2$):
$$R = \begin{bmatrix} \mathbf{1} & 3 & 0 & -1 \\ 0 & 0 & \mathbf{1} & 1 \\ 0 & 0 & 0 & 0 \end{bmatrix}$$

* **Rank:** $r = 2$.
* **Pivots:** Columns 1 and 3. **Free variables:** $x_2$ and $x_4$.
* **Column Space $C(A)$:**
  $$\text{Basis}(C(A)) = \left\{ \begin{bmatrix} 1 \\ 2 \\ -1 \end{bmatrix}, \begin{bmatrix} 3 \\ 9 \\ 3 \end{bmatrix} \right\}, \quad \dim(C(A)) = 2$$
* **Row Space $R(A)$:**
  $$\text{Basis}(R(A)) = \left\{ \begin{bmatrix} 1 \\ 3 \\ 0 \\ -1 \end{bmatrix}, \begin{bmatrix} 0 \\ 0 \\ 1 \\ 1 \end{bmatrix} \right\}, \quad \dim(R(A)) = 2$$
* **Nullspace $N(A)$:**
  From $R\mathbf{x} = \mathbf{0}$:
  $$x_1 = -3x_2 + x_4, \quad x_3 = -x_4$$
  * Free $x_2 = 1, x_4 = 0 \implies \mathbf{u} = \begin{bmatrix} -3 \\ 1 \\ 0 \\ 0 \end{bmatrix}$.
  * Free $x_2 = 0, x_4 = 1 \implies \mathbf{v} = \begin{bmatrix} 1 \\ 0 \\ -1 \\ 1 \end{bmatrix}$.
  $$\text{Basis}(N(A)) = \left\{ \begin{bmatrix} -3 \\ 1 \\ 0 \\ 0 \end{bmatrix}, \begin{bmatrix} 1 \\ 0 \\ -1 \\ 1 \end{bmatrix} \right\}, \quad \dim(N(A)) = 4 - 2 = 2$$
* **Left Nullspace $N(A^\top)$:**
  $R_3 - 2R_2 = \mathbf{0}^\top \implies (R_3 + R_1) - 2(R_2 - 2R_1) = 5R_1 - 2R_2 + R_3 = \mathbf{0}^\top$.
  $$\text{Basis}(N(A^\top)) = \left\{ \begin{bmatrix} 5 \\ -2 \\ 1 \end{bmatrix} \right\}, \quad \dim(N(A^\top)) = 3 - 2 = 1$$
  *Verification:* $5\begin{bmatrix} 1 \\ 3 \\ 3 \\ 2 \end{bmatrix} - 2\begin{bmatrix} 2 \\ 6 \\ 9 \\ 7 \end{bmatrix} + 1\begin{bmatrix} -1 \\ -3 \\ 3 \\ 4 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \\ 0 \\ 0 \end{bmatrix}^\top$.

---

## 2. Orthogonality of Vectors and Fundamental Subspaces

### A. Inner Products, Norms, and Orthogonality

#### Inner Product & Euclidean Norm:
For vectors $\mathbf{x}, \mathbf{y} \in \mathbb{R}^n$:
$$\mathbf{x}^\top \mathbf{y} = \sum_{i=1}^n x_i y_i = x_1 y_1 + x_2 y_2 + \dots + x_n y_n$$
The squared length (squared Euclidean norm) is:
$$\|\mathbf{x}\|^2 = \mathbf{x}^\top \mathbf{x} = \sum_{i=1}^n x_i^2$$

#### Definition of Orthogonality:
Two vectors $\mathbf{x}, \mathbf{y} \in \mathbb{R}^n$ are **orthogonal** (written $\mathbf{x} \perp \mathbf{y}$) if and only if their inner product is zero:
$$\mathbf{x} \perp \mathbf{y} \iff \mathbf{x}^\top \mathbf{y} = 0$$

#### Connection to the Pythagorean Theorem:
In Euclidean geometry, the triangle formed by vectors $\mathbf{x}$, $\mathbf{y}$, and hypotenuse $\mathbf{x} + \mathbf{y}$ is a right-angled triangle if and only if:
$$\|\mathbf{x} + \mathbf{y}\|^2 = \|\mathbf{x}\|^2 + \|\mathbf{y}\|^2$$

Expanding the left side via inner products:
$$\|\mathbf{x} + \mathbf{y}\|^2 = (\mathbf{x} + \mathbf{y})^\top (\mathbf{x} + \mathbf{y}) = \mathbf{x}^\top \mathbf{x} + \mathbf{y}^\top \mathbf{y} + 2 \mathbf{x}^\top \mathbf{y} = \|\mathbf{x}\|^2 + \|\mathbf{y}\|^2 + 2 \mathbf{x}^\top \mathbf{y}$$
Equating both expressions:
$$\|\mathbf{x}\|^2 + \|\mathbf{y}\|^2 + 2 \mathbf{x}^\top \mathbf{y} = \|\mathbf{x}\|^2 + \|\mathbf{y}\|^2 \iff 2 \mathbf{x}^\top \mathbf{y} = 0 \iff \mathbf{x}^\top \mathbf{y} = 0$$

#### Linear Independence of Orthogonal Sets:
> **Theorem:** Any set of non-zero, mutually orthogonal vectors $\{\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_k\}$ in $\mathbb{R}^n$ is linearly independent.

* **Proof:**
  Assume a linear combination equals zero:
  $$c_1 \mathbf{v}_1 + c_2 \mathbf{v}_2 + \dots + c_k \mathbf{v}_k = \mathbf{0}$$
  Take the inner product of both sides with $\mathbf{v}_i$ (for any $i \in \{1, \dots, k\}$):
  $$\mathbf{v}_i^\top \left( \sum_{j=1}^k c_j \mathbf{v}_j \right) = \mathbf{v}_i^\top \mathbf{0} = 0$$
  By mutual orthogonality, $\mathbf{v}_i^\top \mathbf{v}_j = 0$ for all $j \ne i$:
  $$c_i (\mathbf{v}_i^\top \mathbf{v}_i) = 0 \implies c_i \|\mathbf{v}_i\|^2 = 0$$
  Since $\mathbf{v}_i \ne \mathbf{0}$, $\|\mathbf{v}_i\|^2 > 0$, forcing $c_i = 0$ for all $i$. Hence, the vectors are linearly independent. $\blacksquare$

#### Orthonormal Vectors:
A set of vectors $\{\mathbf{q}_1, \dots, \mathbf{q}_k\}$ is **orthonormal** if every vector is unit length and mutually orthogonal:
$$\mathbf{q}_i^\top \mathbf{q}_j = \delta_{ij} = \begin{cases} 1 & \text{if } i = j \\ 0 & \text{if } i \ne j \end{cases}$$

---

### B. Orthogonal Subspaces and Orthogonal Complements

#### Definition of Orthogonal Subspaces:
Two subspaces $V$ and $W$ of $\mathbb{R}^n$ are **orthogonal** ($V \perp W$) if *every* vector in $V$ is orthogonal to *every* vector in $W$:
$$\mathbf{v}^\top \mathbf{w} = 0 \quad \forall \mathbf{v} \in V, \;\forall \mathbf{w} \in W$$

> [!CAUTION]
> Subspaces can only intersect at the zero vector if they are orthogonal:
> $$V \perp W \implies V \cap W = \{\mathbf{0}\}$$
> *Geometric Warning:* In $\mathbb{R}^3$, the $xy$-plane and the $yz$-plane meet at a right angle ($90^\circ$), but they are **not** orthogonal subspaces! Their intersection is the $y$-axis, which contains non-zero vectors that lie in both spaces (a vector on the $y$-axis is not orthogonal to itself).

#### Orthogonal Complement $V^\perp$:
The **orthogonal complement** of a subspace $V \subseteq \mathbb{R}^n$, denoted $V^\perp$, is the set of *all* vectors in $\mathbb{R}^n$ that are perpendicular to $V$:
$$V^\perp = \{\mathbf{w} \in \mathbb{R}^n \mid \mathbf{v}^\top \mathbf{w} = 0 \;\forall \mathbf{v} \in V\}$$

Properties of orthogonal complements:
1. $\dim(V) + \dim(V^\perp) = n$.
2. $(V^\perp)^\perp = V$.
3. $\mathbb{R}^n = V \oplus V^\perp$ (Direct sum: every $\mathbf{x} \in \mathbb{R}^n$ can be uniquely decomposed as $\mathbf{x} = \mathbf{v} + \mathbf{w}$ with $\mathbf{v} \in V, \mathbf{w} \in V^\perp$).

---

### C. The Fundamental Orthogonality Relations
The second part of the Fundamental Theorem of Linear Algebra establishes the exact geometric relationship between the four subspaces.

> **Fundamental Theorem of Linear Algebra (Part 2):**
> 1. The **row space** $R(A) = C(A^\top)$ and the **nullspace** $N(A)$ are orthogonal complements in $\mathbb{R}^n$:
>    $$R(A) \perp N(A) \quad \text{and} \quad R(A)^\perp = N(A)$$
> 2. The **column space** $C(A)$ and the **left nullspace** $N(A^\top)$ are orthogonal complements in $\mathbb{R}^m$:
>    $$C(A) \perp N(A^\top) \quad \text{and} \quad C(A)^\perp = N(A^\top)$$

#### Proof that Row Space is Orthogonal to Nullspace:
Let $\mathbf{x} \in N(A)$. By definition, $A\mathbf{x} = \mathbf{0}$:
$$\begin{bmatrix} \text{row}_1(A) \\ \text{row}_2(A) \\ \vdots \\ \text{row}_m(A) \end{bmatrix} \mathbf{x} = \begin{bmatrix} \text{row}_1(A) \cdot \mathbf{x} \\ \text{row}_2(A) \cdot \mathbf{x} \\ \vdots \\ \text{row}_m(A) \cdot \mathbf{x} \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \\ \vdots \\ 0 \end{bmatrix}$$
This proves that $\mathbf{x}$ is perpendicular to every row of $A$. 

Any arbitrary vector $\mathbf{r} \in R(A)$ is a linear combination of the rows of $A$, meaning $\mathbf{r} = A^\top \mathbf{c}$ for some $\mathbf{c} \in \mathbb{R}^m$. Taking the inner product:
$$\mathbf{r}^\top \mathbf{x} = (A^\top \mathbf{c})^\top \mathbf{x} = \mathbf{c}^\top (A\mathbf{x}) = \mathbf{c}^\top \mathbf{0} = 0$$
Since $\mathbf{r}^\top \mathbf{x} = 0$ for all $\mathbf{r} \in R(A)$ and $\mathbf{x} \in N(A)$, we have $R(A) \perp N(A)$. 
Since $\dim(R(A)) + \dim(N(A)) = r + (n - r) = n$, they are full orthogonal complements. $\blacksquare$

#### Proof that Column Space is Orthogonal to Left Nullspace:
Let $\mathbf{y} \in N(A^\top)$. By definition, $A^\top \mathbf{y} = \mathbf{0}$, which is equivalent to $\mathbf{y}^\top A = \mathbf{0}^\top$.
Any arbitrary vector in the column space can be written as $A\mathbf{x}$ for some $\mathbf{x} \in \mathbb{R}^n$. Taking the inner product:
$$\mathbf{y}^\top (A\mathbf{x}) = (\mathbf{y}^\top A) \mathbf{x} = \mathbf{0}^\top \mathbf{x} = 0$$
Since $\dim(C(A)) + \dim(N(A^\top)) = r + (m - r) = m$, $C(A)$ and $N(A^\top)$ are full orthogonal complements in $\mathbb{R}^m$. $\blacksquare$

---

### D. Geometric Visualization & Dimension Verification

#### Worked Geometric Example (Slide `f2-8`):
Consider:
$$A = \begin{bmatrix} 1 & 2 \\ 2 & 4 \\ 3 & 6 \end{bmatrix} \quad (3 \times 2 \text{ matrix})$$

* **Column Space $C(A)$:**
  The second column is twice the first: $\begin{bmatrix} 2 \\ 4 \\ 6 \end{bmatrix} = 2 \begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix}$.
  Rank $r = 1$.
  $$C(A) = \text{Line through } \begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix} \text{ in } \mathbb{R}^3$$
* **Left Nullspace $N(A^\top)$:**
  We require $A^\top \mathbf{y} = \mathbf{0}$, which gives:
  $$\begin{bmatrix} 1 & 2 & 3 \\ 2 & 4 & 6 \end{bmatrix} \begin{bmatrix} y_1 \\ y_2 \\ y_3 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix} \implies y_1 + 2y_2 + 3y_3 = 0$$
  This single linear equation defines a **2D plane passing through the origin** in $\mathbb{R}^3$.
* **Orthogonality Connection:**
  The normal vector to the plane $y_1 + 2y_2 + 3y_3 = 0$ is exactly $\begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix}$, which spans the column space line!
  $$\text{Line } C(A) \perp \text{Plane } N(A^\top)$$
* **Dimension Check:**
  * In $\mathbb{R}^n = \mathbb{R}^2$: $\dim(R(A)) + \dim(N(A)) = 1 + 1 = 2$ (number of columns $n$).
  * In $\mathbb{R}^m = \mathbb{R}^3$: $\dim(C(A)) + \dim(N(A^\top)) = 1 + 2 = 3$ (number of rows $m$).

---

## 3. Orthogonal Projections onto Lines (1D Subspaces)

### A. The Geometry of 1D Projection
Suppose we are given a line in $\mathbb{R}^m$ passing through the origin in the direction of vector $\mathbf{a} \ne \mathbf{0}$, and a vector $\mathbf{b} \in \mathbb{R}^m$ that does not necessarily lie on that line.

```
                  b
                 /|
                / |
               /  |
              /   |  e = b - p
             /    |  (error vector)
            /     |
           /      |
          /       |
         /        |
        0─────────p───────────> a
              p = x_hat * a
            (projection vector)
```

We want to find the vector $\mathbf{p}$ on the line that is **closest** to $\mathbf{b}$.
1. Since $\mathbf{p}$ lies on the line determined by $\mathbf{a}$, it must be a scalar multiple of $\mathbf{a}$:
   $$\mathbf{p} = \hat{x} \mathbf{a}$$
2. The distance from $\mathbf{b}$ to the line is the length of the **error vector** $\mathbf{e}$:
   $$\mathbf{e} = \mathbf{b} - \mathbf{p} = \mathbf{b} - \hat{x} \mathbf{a}$$
3. Geometrically, the shortest distance occurs when the line connecting $\mathbf{b}$ to $\mathbf{p}$ drops perpendicularly onto $\mathbf{a}$:
   $$\mathbf{e} \perp \mathbf{a} \iff \mathbf{a}^\top \mathbf{e} = 0$$

---

### B. Algebraic Derivation of the Scalar $\hat{x}$
Substituting $\mathbf{e} = \mathbf{b} - \hat{x} \mathbf{a}$ into the orthogonality condition:

$$\mathbf{a}^\top (\mathbf{b} - \hat{x} \mathbf{a}) = 0$$
$$\mathbf{a}^\top \mathbf{b} - \hat{x} (\mathbf{a}^\top \mathbf{a}) = 0$$

Solving for the scalar $\hat{x}$:
$$\hat{x} = \frac{\mathbf{a}^\top \mathbf{b}}{\mathbf{a}^\top \mathbf{a}}$$

The projected vector $\mathbf{p}$ is therefore:
$$\mathbf{p} = \hat{x} \mathbf{a} = \left( \frac{\mathbf{a}^\top \mathbf{b}}{\mathbf{a}^\top \mathbf{a}} \right) \mathbf{a}$$

---

### C. Derivation of the Cauchy-Schwarz Inequality via Projection
Because the squared length of the error vector must be non-negative ($\|\mathbf{e}\|^2 \ge 0$), we can derive the celebrated **Cauchy-Schwarz Inequality**:

$$\|\mathbf{e}\|^2 = \|\mathbf{b} - \mathbf{p}\|^2 = \left\| \mathbf{b} - \frac{\mathbf{a}^\top \mathbf{b}}{\mathbf{a}^\top \mathbf{a}} \mathbf{a} \right\|^2 \ge 0$$

Expanding the inner product:
$$\begin{aligned}
\|\mathbf{e}\|^2 &= \left( \mathbf{b} - \frac{\mathbf{a}^\top \mathbf{b}}{\mathbf{a}^\top \mathbf{a}} \mathbf{a} \right)^\top \left( \mathbf{b} - \frac{\mathbf{a}^\top \mathbf{b}}{\mathbf{a}^\top \mathbf{a}} \mathbf{a} \right) \\
&= \mathbf{b}^\top \mathbf{b} - 2 \frac{\mathbf{a}^\top \mathbf{b}}{\mathbf{a}^\top \mathbf{a}} (\mathbf{a}^\top \mathbf{b}) + \left( \frac{\mathbf{a}^\top \mathbf{b}}{\mathbf{a}^\top \mathbf{a}} \right)^2 (\mathbf{a}^\top \mathbf{a}) \\
&= \mathbf{b}^\top \mathbf{b} - 2 \frac{(\mathbf{a}^\top \mathbf{b})^2}{\mathbf{a}^\top \mathbf{a}} + \frac{(\mathbf{a}^\top \mathbf{b})^2}{\mathbf{a}^\top \mathbf{a}} \\
&= \mathbf{b}^\top \mathbf{b} - \frac{(\mathbf{a}^\top \mathbf{b})^2}{\mathbf{a}^\top \mathbf{a}} = \frac{(\mathbf{b}^\top \mathbf{b})(\mathbf{a}^\top \mathbf{a}) - (\mathbf{a}^\top \mathbf{b})^2}{\mathbf{a}^\top \mathbf{a}} \ge 0
\end{aligned}$$

Since the denominator $\mathbf{a}^\top \mathbf{a} = \|\mathbf{a}\|^2 > 0$, the numerator must be non-negative:
$$(\mathbf{b}^\top \mathbf{b})(\mathbf{a}^\top \mathbf{a}) \ge (\mathbf{a}^\top \mathbf{b})^2$$
Taking the square root of both sides yields:
$$|\mathbf{a}^\top \mathbf{b}| \le \|\mathbf{a}\| \|\mathbf{b}\|$$

> **Condition for Equality:**
> $|\mathbf{a}^\top \mathbf{b}| = \|\mathbf{a}\| \|\mathbf{b}\| \iff \|\mathbf{e}\|^2 = 0 \iff \mathbf{e} = \mathbf{0} \iff \mathbf{b} = \hat{x} \mathbf{a}$ ($\mathbf{b}$ lies directly on the line of $\mathbf{a}$).

---

### D. The 1D Projection Matrix $P$
We can express the projection operation as a matrix multiplication. Rearranging $\mathbf{p}$:
$$\mathbf{p} = \mathbf{a} \hat{x} = \mathbf{a} \left( \frac{\mathbf{a}^\top \mathbf{b}}{\mathbf{a}^\top \mathbf{a}} \right) = \left( \frac{\mathbf{a} \mathbf{a}^\top}{\mathbf{a}^\top \mathbf{a}} \right) \mathbf{b}$$

We define the **Projection Matrix** $P$:
$$P = \frac{\mathbf{a} \mathbf{a}^\top}{\mathbf{a}^\top \mathbf{a}}$$

Then the projection of any vector $\mathbf{b}$ onto $\mathbf{a}$ is obtained simply by left-multiplying $\mathbf{b}$ by $P$:
$$\mathbf{p} = P\mathbf{b}$$

```
Numerator:   a a^T   --> Outer product (m x m matrix of rank 1)
Denominator: a^T a   --> Inner product (scalar length squared)
```

#### Fundamental Properties of $P$:
1. **Symmetry:**
   $$P^\top = \left( \frac{\mathbf{a} \mathbf{a}^\top}{\mathbf{a}^\top \mathbf{a}} \right)^\top = \frac{(\mathbf{a}^\top)^\top \mathbf{a}^\top}{\mathbf{a}^\top \mathbf{a}} = \frac{\mathbf{a} \mathbf{a}^\top}{\mathbf{a}^\top \mathbf{a}} = P$$
2. **Idempotence ($P^2 = P$):**
   $$P^2 = \left( \frac{\mathbf{a} \mathbf{a}^\top}{\mathbf{a}^\top \mathbf{a}} \right) \left( \frac{\mathbf{a} \mathbf{a}^\top}{\mathbf{a}^\top \mathbf{a}} \right) = \frac{\mathbf{a} (\mathbf{a}^\top \mathbf{a}) \mathbf{a}^\top}{(\mathbf{a}^\top \mathbf{a})^2} = \frac{\mathbf{a} \mathbf{a}^\top}{\mathbf{a}^\top \mathbf{a}} = P$$
   *Physical Meaning:* Projecting a vector that has already been projected changes nothing ($P^2 \mathbf{b} = P \mathbf{b}$ because $P\mathbf{b}$ is already on the line).
3. **Invariance to Scalar Multiplication:**
   Replacing $\mathbf{a}$ by $c \mathbf{a}$ (for any scalar $c \ne 0$):
   $$P_{c\mathbf{a}} = \frac{(c\mathbf{a})(c\mathbf{a})^\top}{(c\mathbf{a})^\top (c\mathbf{a})} = \frac{c^2 \mathbf{a}\mathbf{a}^\top}{c^2 \mathbf{a}^\top \mathbf{a}} = P_\mathbf{a}$$
   The projection matrix depends solely on the *subspace* (the line), not the length of the vector chosen to span it.
4. **Subspaces of $P$:**
   * Column Space: $C(P) = \operatorname{span}\{\mathbf{a}\}$ (the line, $\operatorname{rank}(P) = 1$).
   * Nullspace: $N(P) = \{\mathbf{x} \mid \mathbf{a}^\top \mathbf{x} = 0\} = \mathbf{a}^\perp$ (the hyperplane perpendicular to $\mathbf{a}$).

#### Numerical Example:
Let $\mathbf{a} = \begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix}$.
$$\mathbf{a}^\top \mathbf{a} = 1^2 + 1^2 + 1^2 = 3$$
$$\mathbf{a} \mathbf{a}^\top = \begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix} \begin{bmatrix} 1 & 1 & 1 \end{bmatrix} = \begin{bmatrix} 1 & 1 & 1 \\ 1 & 1 & 1 \\ 1 & 1 & 1 \end{bmatrix}$$
$$P = \frac{1}{3} \begin{bmatrix} 1 & 1 & 1 \\ 1 & 1 & 1 \\ 1 & 1 & 1 \end{bmatrix} = \begin{bmatrix} 1/3 & 1/3 & 1/3 \\ 1/3 & 1/3 & 1/3 \\ 1/3 & 1/3 & 1/3 \end{bmatrix}$$
* Check scaling: For $\mathbf{a} = \begin{bmatrix} 2 \\ 2 \\ 2 \end{bmatrix}$, $\mathbf{a}^\top \mathbf{a} = 12$, and $\mathbf{a}\mathbf{a}^\top = \begin{bmatrix} 4 & 4 & 4 \\ 4 & 4 & 4 \\ 4 & 4 & 4 \end{bmatrix}$, so $P = \frac{4}{12} \begin{bmatrix} 1 & 1 & 1 \\ 1 & 1 & 1 \\ 1 & 1 & 1 \end{bmatrix} = \begin{bmatrix} 1/3 & 1/3 & 1/3 \\ 1/3 & 1/3 & 1/3 \\ 1/3 & 1/3 & 1/3 \end{bmatrix}$, identical!

---

## 4. Orthogonal Projections onto General Subspaces & The Normal Equations

### A. The Subspace Projection Problem
In practical machine learning, we do not project onto a 1D line; we project onto a higher-dimensional subspace $S \subseteq \mathbb{R}^m$, such as a plane or hyperplane.

Let the subspace $S$ be spanned by the linearly independent columns of an $m \times n$ matrix $A$ (where $m > n$, representing an overdetermined system):
$$S = C(A) = \operatorname{span}\{\mathbf{a}_1, \mathbf{a}_2, \dots, \mathbf{a}_n\}$$

Given a vector $\mathbf{b} \in \mathbb{R}^m$ that typically lies outside $C(A)$ ($A\mathbf{x} = \mathbf{b}$ is inconsistent), we want to find the vector $\mathbf{p} \in C(A)$ that is closest to $\mathbf{b}$.

```
                 b
                /|
               / |
              /  |  e = b - p = b - A*x_hat
             /   |  (perpendicular to the entire subspace S)
            /    |
     ┌─────/─────┴─────────────────────────┐
     │    0      p = A*x_hat               │
     │     \                               │
     │      \   Subspace S = C(A)          │
     │       \                             │
     └─────────────────────────────────────┘
```

1. Since $\mathbf{p} \in C(A)$, it must be a linear combination of the columns of $A$:
   $$\mathbf{p} = A\mathbf{\hat{x}} = \hat{x}_1 \mathbf{a}_1 + \hat{x}_2 \mathbf{a}_2 + \dots + \hat{x}_n \mathbf{a}_n$$
2. The error vector is:
   $$\mathbf{e} = \mathbf{b} - \mathbf{p} = \mathbf{b} - A\mathbf{\hat{x}}$$
3. To minimize the Euclidean distance $\|\mathbf{b} - \mathbf{p}\|$, the error vector $\mathbf{e}$ must be orthogonal to every vector in the subspace $C(A)$.

---

### B. Derivation of the Normal Equations

#### Route 1: Via the Fundamental Subspace Orthogonality
Recall from Section 2 that the orthogonal complement of the column space $C(A)$ is the left nullspace $N(A^\top)$:
$$C(A)^\perp = N(A^\top)$$
Since $\mathbf{e}$ is orthogonal to every vector in $C(A)$, it must lie in the left nullspace:
$$\mathbf{e} \in N(A^\top) \implies A^\top \mathbf{e} = \mathbf{0}$$
Substitute $\mathbf{e} = \mathbf{b} - A\mathbf{\hat{x}}$:
$$A^\top (\mathbf{b} - A\mathbf{\hat{x}}) = \mathbf{0}$$
$$A^\top \mathbf{b} - A^\top A \mathbf{\hat{x}} = \mathbf{0}$$

$$\mathbf{A^\top A \mathbf{\hat{x}} = A^\top \mathbf{b}}$$

These are the famous **Normal Equations**.

#### Route 2: Via Column-by-Column Orthogonality
The error $\mathbf{e}$ must be orthogonal to each individual column vector $\mathbf{a}_i$ of $A$:
$$\begin{aligned}
\mathbf{a}_1^\top \mathbf{e} &= 0 \iff \mathbf{a}_1^\top (\mathbf{b} - A\mathbf{\hat{x}}) = 0 \\
\mathbf{a}_2^\top \mathbf{e} &= 0 \iff \mathbf{a}_2^\top (\mathbf{b} - A\mathbf{\hat{x}}) = 0 \\
&\;\;\vdots \\
\mathbf{a}_n^\top \mathbf{e} &= 0 \iff \mathbf{a}_n^\top (\mathbf{b} - A\mathbf{\hat{x}}) = 0
\end{aligned}$$

Stacking these row vectors into a single matrix:
$$\begin{bmatrix} \mathbf{a}_1^\top \\ \mathbf{a}_2^\top \\ \vdots \\ \mathbf{a}_n^\top \end{bmatrix} (\mathbf{b} - A\mathbf{\hat{x}}) = \begin{bmatrix} 0 \\ 0 \\ \vdots \\ 0 \end{bmatrix} \iff A^\top (\mathbf{b} - A\mathbf{\hat{x}}) = \mathbf{0} \iff A^\top A \mathbf{\hat{x}} = A^\top \mathbf{b}$$

> [!NOTE]
> Even if the original system $A\mathbf{x} = \mathbf{b}$ has **no solution**, the Normal Equations $A^\top A \mathbf{\hat{x}} = A^\top \mathbf{b}$ are **always solvable**!

---

### C. Invertibility of $A^\top A$ and The Subspace Projection Matrix

#### Theorem: Invertibility of $A^\top A$
The $n \times n$ matrix $A^\top A$ is invertible if and only if the columns of $A$ are linearly independent (i.e., $\operatorname{rank}(A) = n$, full column rank).

* **Proof:**
  Suppose $A^\top A \mathbf{x} = \mathbf{0}$ for some $\mathbf{x} \in \mathbb{R}^n$.
  Multiply both sides on the left by $\mathbf{x}^\top$:
  $$\mathbf{x}^\top (A^\top A \mathbf{x}) = \mathbf{x}^\top \mathbf{0} = 0$$
  Using the associativity of matrix multiplication:
  $$(A\mathbf{x})^\top (A\mathbf{x}) = 0 \implies \|A\mathbf{x}\|^2 = 0 \implies A\mathbf{x} = \mathbf{0}$$
  If the columns of $A$ are linearly independent, the only solution to $A\mathbf{x} = \mathbf{0}$ is $\mathbf{x} = \mathbf{0}$.
  Therefore, $N(A^\top A) = \{\mathbf{0}\}$, proving that the square matrix $A^\top A$ is full rank and invertible. $\blacksquare$

#### Solution for $\mathbf{\hat{x}}$ and Projection $\mathbf{p}$:
When $A^\top A$ is invertible:
$$\mathbf{\hat{x}} = (A^\top A)^{-1} A^\top \mathbf{b}$$

The projection vector $\mathbf{p}$ onto $C(A)$ is:
$$\mathbf{p} = A\mathbf{\hat{x}} = A (A^\top A)^{-1} A^\top \mathbf{b}$$

We identify the general **Subspace Projection Matrix**:
$$P = A (A^\top A)^{-1} A^\top$$
$$\mathbf{p} = P\mathbf{b}$$

#### Error Projection Matrix:
The error vector $\mathbf{e}$ is the projection of $\mathbf{b}$ onto the orthogonal complement $N(A^\top)$:
$$\mathbf{e} = \mathbf{b} - \mathbf{p} = (I - P)\mathbf{b} = \left( I - A (A^\top A)^{-1} A^\top \right) \mathbf{b}$$

---

### D. Essential Properties & Special Cases of $P$

#### 1. Symmetry:
$$P^\top = \left( A (A^\top A)^{-1} A^\top \right)^\top = (A^\top)^\top \left( (A^\top A)^{-1} \right)^\top A^\top$$
Since $(A^\top A)^\top = A^\top (A^\top)^\top = A^\top A$, the inverse of a symmetric matrix is symmetric:
$$\left( (A^\top A)^{-1} \right)^\top = (A^\top A)^{-1}$$
Thus:
$$P^\top = A (A^\top A)^{-1} A^\top = P \quad \checkmark$$

#### 2. Idempotence ($P^2 = P$):
$$P^2 = \left( A (A^\top A)^{-1} A^\top \right) \left( A (A^\top A)^{-1} A^\top \right) = A (A^\top A)^{-1} \underbrace{\left( A^\top A \right) (A^\top A)^{-1}}_{= I} A^\top = A (A^\top A)^{-1} A^\top = P \quad \checkmark$$

#### 3. Characterization Theorem (Converse):
> **Theorem:** Any matrix $P$ is an orthogonal projection matrix if and only if $P^\top = P$ and $P^2 = P$.

* **Proof (Slide `f4-7`):**
  Let $P^\top = P$ and $P^2 = P$. We verify that for any $\mathbf{b}$, $P\mathbf{b}$ is the orthogonal projection onto $C(P)$.
  The error is $\mathbf{e} = \mathbf{b} - P\mathbf{b} = (I - P)\mathbf{b}$.
  Any vector in $C(P)$ can be written as $P\mathbf{c}$ for some $\mathbf{c}$.
  Taking the inner product:
  $$(\mathbf{b} - P\mathbf{b})^\top (P\mathbf{c}) = \mathbf{b}^\top (I - P)^\top P \mathbf{c} = \mathbf{b}^\top (I - P) P \mathbf{c} = \mathbf{b}^\top (P - P^2) \mathbf{c}$$
  Since $P^2 = P$, we have $P - P^2 = 0$:
  $$\mathbf{b}^\top (0) \mathbf{c} = 0$$
  Thus, the error is orthogonal to every vector in $C(P)$. $\blacksquare$

#### 4. Important Extreme Cases:
* **Case 1: $\mathbf{b} \in C(A)$**
  Then $\mathbf{b} = A\mathbf{x}$ for some $\mathbf{x}$.
  $$P\mathbf{b} = A (A^\top A)^{-1} A^\top (A\mathbf{x}) = A \underbrace{(A^\top A)^{-1} (A^\top A)}_{= I} \mathbf{x} = A\mathbf{x} = \mathbf{b}$$
  *Projection of a vector already in the subspace is itself.*
* **Case 2: $\mathbf{b} \in N(A^\top)$**
  Then $A^\top \mathbf{b} = \mathbf{0}$.
  $$P\mathbf{b} = A (A^\top A)^{-1} (A^\top \mathbf{b}) = A (A^\top A)^{-1} \mathbf{0} = \mathbf{0}$$
  *Projection of a vector perpendicular to the subspace is zero.*
* **Case 3: $A$ is square and invertible ($m = n$)**
  The column space is all of $\mathbb{R}^n$ ($C(A) = \mathbb{R}^n$).
  $$P = A (A^\top A)^{-1} A^\top = A A^{-1} (A^\top)^{-1} A^\top = I \cdot I = I$$
  *Projecting onto the entire space is the identity operator.*
* **Case 4: Single column $A = [\mathbf{a}]$ (Rank 1)**
  $$P = \mathbf{a} (\mathbf{a}^\top \mathbf{a})^{-1} \mathbf{a}^\top = \frac{\mathbf{a} \mathbf{a}^\top}{\mathbf{a}^\top \mathbf{a}}$$
  *Coincides exactly with 1D line projection.*

---

## 5. Least Squares Approximation and Linear Regression

### A. The Machine Learning Connection: Overdetermined Systems
In machine learning, we are given a dataset of $m$ observations:
$$(x_1, y_1), (x_2, y_2), \dots, (x_m, y_m)$$

We want to fit a model to predict $y$ from $x$. Consider a linear model:
$$y = \theta_1 x + \theta_0$$
where $\theta_1$ is the slope and $\theta_0$ is the intercept/offset.

Each observation gives an equation:
$$\begin{aligned}
\theta_1 x_1 + \theta_0 &= y_1 \\
\theta_1 x_2 + \theta_0 &= y_2 \\
&\;\;\vdots \\
\theta_1 x_m + \theta_0 &= y_m
\end{aligned} \iff \begin{bmatrix} x_1 & 1 \\ x_2 & 1 \\ \vdots & \vdots \\ x_m & 1 \end{bmatrix} \begin{bmatrix} \theta_1 \\ \theta_0 \end{bmatrix} = \begin{bmatrix} y_1 \\ y_2 \\ \vdots \\ y_m \end{bmatrix} \iff A\boldsymbol{\theta} = \mathbf{y}$$

In reality, experimental data contains noise, measurement errors, or nonlinearities, so the points do **not** lie on a single straight line.
Thus, $\mathbf{y} \notin C(A)$, and the system $A\boldsymbol{\theta} = \mathbf{y}$ is **inconsistent** (no exact solution exists).

#### Why not solve a subset of equations?
If we select any two points and solve for a line exactly, the error on those two points is $0$, but the prediction error on all other $m - 2$ points can be enormous.
Instead, we find the best compromised solution that **minimizes the total sum of squared errors (residuals)**:
$$E^2 = \sum_{i=1}^m \left( y_i - (\theta_1 x_i + \theta_0) \right)^2 = \|\mathbf{y} - A\boldsymbol{\theta}\|^2$$

---

### B. Calculus Derivation vs Geometric Projection Equivalence

#### 1. Scalar Calculus View (Slide `f4-1`, `f4-2`):
Suppose we have an overdetermined system in one unknown:
$$2x = b_1, \quad 3x = b_2, \quad 4x = b_3$$
We seek $x$ minimizing the squared error:
$$E^2(x) = (2x - b_1)^2 + (3x - b_2)^2 + (4x - b_3)^2$$

To find the minimum, differentiate with respect to $x$ and set to zero:
$$\frac{dE^2}{dx} = 2 \cdot 2(2x - b_1) + 2 \cdot 3(3x - b_2) + 2 \cdot 4(4x - b_3) = 0$$
Divide by 2:
$$2(2x - b_1) + 3(3x - b_2) + 4(4x - b_3) = 0$$
$$(2^2 + 3^2 + 4^2) x = 2b_1 + 3b_2 + 4b_3$$
$$\hat{x} = \frac{2b_1 + 3b_2 + 4b_3}{2^2 + 3^2 + 4^2} = \frac{\mathbf{a}^\top \mathbf{b}}{\mathbf{a}^\top \mathbf{a}}, \quad \text{where } \mathbf{a} = \begin{bmatrix} 2 \\ 3 \\ 4 \end{bmatrix}$$

#### 2. Vector Calculus View:
For general $A\boldsymbol{\theta} = \mathbf{y}$:
$$E^2(\boldsymbol{\theta}) = \|\mathbf{y} - A\boldsymbol{\theta}\|^2 = (\mathbf{y} - A\boldsymbol{\theta})^\top (\mathbf{y} - A\boldsymbol{\theta}) = \mathbf{y}^\top \mathbf{y} - 2\boldsymbol{\theta}^\top A^\top \mathbf{y} + \boldsymbol{\theta}^\top A^\top A \boldsymbol{\theta}$$

Computing the gradient with respect to parameter vector $\boldsymbol{\theta}$:
$$\nabla_{\boldsymbol{\theta}} E^2 = -2 A^\top \mathbf{y} + 2 A^\top A \boldsymbol{\theta} = \mathbf{0}$$
$$\implies A^\top A \hat{\boldsymbol{\theta}} = A^\top \mathbf{y}$$

> **Core Insight:**
> Taking the calculus derivative to minimize the sum of squared errors yields **precisely the same Normal Equations** as finding the geometric orthogonal projection onto the subspace $C(A)$!

---

### C. The Dual Geometric Perspectives of Least Squares (Slide `f5-6`)
There are two deeply illuminating ways to visualize linear regression:

```
VIEW 1: Data Space R^2 (Observation Space)           VIEW 2: Subspace Geometry in R^m (m-dimensional)
          y                                                     b (Observation vector)
          |        . (x_3, y_3)                                /|
          |       /|                                          / |
          |      / | e_3                                     /  | e = b - p
          |     /  |                                        /   | (Perpendicular to C(A))
          |  . /---+ (x_2, y_2)                            /    |
          |  |/                                     ┌─────/─────┴────────────────────────┐
          |  / (x_1, y_1)                           │    0      p = A*theta_hat          │
          | /|                                      │     \                              │
          |/ | e_1                                  │      \    Column Space C(A)        │
          └───────────────────── x                  │       \   (Plane spanned by cols)  │
            Fit line: y = m*x + c                   └────────────────────────────────────┘
```

1. **View 1 (2D Data Space):**
   * Plotted in the standard Cartesian $(x, y)$ coordinate plane.
   * There are $m$ distinct points $(x_i, y_i)$.
   * The line $y = \theta_1 x + \theta_0$ is chosen to minimize the sum of squared **vertical distances** $e_i = y_i - (\theta_1 x_i + \theta_0)$.
2. **View 2 ($m$-Dimensional Vector Space $\mathbb{R}^m$):**
   * There is a single target vector $\mathbf{y} \in \mathbb{R}^m$.
   * The columns of $A$ (the feature column and the constant column of ones) span a $2$-dimensional subspace (a plane) $C(A) \subseteq \mathbb{R}^m$.
   * The vector $\mathbf{y}$ does not lie on this plane.
   * The least squares solution projects $\mathbf{y}$ perpendicularly onto the plane $C(A)$, yielding $\mathbf{p} = A\hat{\boldsymbol{\theta}}$.
   * The error vector $\mathbf{e} = \mathbf{y} - \mathbf{p}$ is strictly perpendicular to the entire plane: $\mathbf{e} \perp C(A)$.

---

### D. Detailed Lecture Example (3-Point Fitting)
Fit the best straight line $y = \theta' x + \theta''$ through the three data points:
$$(-1, 1), \quad (1, 1), \quad (2, 3)$$

#### Step 1: Set up the matrix system $A\boldsymbol{\theta} = \mathbf{b}$
$$\begin{aligned}
\theta'(-1) + \theta'' &= 1 \\
\theta'(1) + \theta'' &= 1 \\
\theta'(2) + \theta'' &= 3
\end{aligned} \iff \begin{bmatrix} -1 & 1 \\ 1 & 1 \\ 2 & 1 \end{bmatrix} \begin{bmatrix} \theta' \\ \theta'' \end{bmatrix} = \begin{bmatrix} 1 \\ 1 \\ 3 \end{bmatrix}$$

#### Step 2: Test for consistency via Gaussian Elimination
Augmented matrix:
$$\left[\begin{array}{cc|c} -1 & 1 & 1 \\ 1 & 1 & 1 \\ 2 & 1 & 3 \end{array}\right] \xrightarrow{R_1 \leftarrow -R_1} \left[\begin{array}{cc|c} 1 & -1 & -1 \\ 1 & 1 & 1 \\ 2 & 1 & 3 \end{array}\right]$$
Eliminate column 1:
$$\xrightarrow{\substack{R_2 \leftarrow R_2 - R_1 \\ R_3 \leftarrow R_3 - 2R_1}} \left[\begin{array}{cc|c} 1 & -1 & -1 \\ 0 & 2 & 2 \\ 0 & 3 & 5 \end{array}\right] \xrightarrow{R_2 \leftarrow \frac{1}{2}R_2} \left[\begin{array}{cc|c} 1 & -1 & -1 \\ 0 & 1 & 1 \\ 0 & 3 & 5 \end{array}\right]$$
Eliminate column 2 in row 3:
$$\xrightarrow{R_3 \leftarrow R_3 - 3R_2} \left[\begin{array}{cc|c} 1 & -1 & -1 \\ 0 & 1 & 1 \\ \mathbf{0} & \mathbf{0} & \mathbf{2} \end{array}\right]$$
The final row reads $0\theta' + 0\theta'' = 2$, which is an impossibility ($0 = 2$).
Hence, the system is **inconsistent** ($\mathbf{b} \notin C(A)$).

#### Step 3: Compute $A^\top A$ and $A^\top \mathbf{b}$
$$A^\top A = \begin{bmatrix} -1 & 1 & 2 \\ 1 & 1 & 1 \end{bmatrix} \begin{bmatrix} -1 & 1 \\ 1 & 1 \\ 2 & 1 \end{bmatrix} = \begin{bmatrix} (-1)^2 + 1^2 + 2^2 & -1(1) + 1(1) + 2(1) \\ -1(1) + 1(1) + 2(1) & 1^2 + 1^2 + 1^2 \end{bmatrix} = \begin{bmatrix} 6 & 2 \\ 2 & 3 \end{bmatrix}$$

$$A^\top \mathbf{b} = \begin{bmatrix} -1 & 1 & 2 \\ 1 & 1 & 1 \end{bmatrix} \begin{bmatrix} 1 \\ 1 \\ 3 \end{bmatrix} = \begin{bmatrix} -1(1) + 1(1) + 2(3) \\ 1(1) + 1(1) + 1(3) \end{bmatrix} = \begin{bmatrix} 6 \\ 5 \end{bmatrix}$$

#### Step 4: Solve the Normal Equations $A^\top A \hat{\boldsymbol{\theta}} = A^\top \mathbf{b}$
$$\begin{bmatrix} 6 & 2 \\ 2 & 3 \end{bmatrix} \begin{bmatrix} \hat{\theta}' \\ \hat{\theta}'' \end{bmatrix} = \begin{bmatrix} 6 \\ 5 \end{bmatrix}$$

Equations:
$$\begin{aligned}
6\hat{\theta}' + 2\hat{\theta}'' &= 6 \quad \text{--- (1)} \\
2\hat{\theta}' + 3\hat{\theta}'' &= 5 \quad \text{--- (2)}
\end{aligned}$$

Multiply (2) by 3:
$$6\hat{\theta}' + 9\hat{\theta}'' = 15 \quad \text{--- (3)}$$
Subtract (1) from (3):
$$7\hat{\theta}'' = 9 \implies \hat{\theta}'' = \frac{9}{7}$$
Substitute into (1):
$$6\hat{\theta}' + 2\left(\frac{9}{7}\right) = 6 \implies 6\hat{\theta}' = \frac{42 - 18}{7} = \frac{24}{7} \implies \hat{\theta}' = \frac{4}{7}$$

The optimal least squares parameter vector is:
$$\hat{\boldsymbol{\theta}} = \begin{bmatrix} 4/7 \\ 9/7 \end{bmatrix}$$
The best-fit line is:
$$y = \frac{4}{7} x + \frac{9}{7}$$

#### Step 5: Fitted Values (Projections) and Residual Vector
* **Projected values $\mathbf{p} = A\hat{\boldsymbol{\theta}}$:**
  $$\begin{aligned}
  p_1 &= \frac{4}{7}(-1) + \frac{9}{7} = \frac{5}{7} \\
  p_2 &= \frac{4}{7}(1) + \frac{9}{7} = \frac{13}{7} \\
  p_3 &= \frac{4}{7}(2) + \frac{9}{7} = \frac{17}{7}
  \end{aligned} \implies \mathbf{p} = \begin{bmatrix} 5/7 \\ 13/7 \\ 17/7 \end{bmatrix}$$
* **Error vector $\mathbf{e} = \mathbf{b} - \mathbf{p}$:**
  $$\mathbf{e} = \begin{bmatrix} 1 - 5/7 \\ 1 - 13/7 \\ 3 - 17/7 \end{bmatrix} = \begin{bmatrix} 2/7 \\ -6/7 \\ 4/7 \end{bmatrix} = \frac{1}{7} \begin{bmatrix} 2 \\ -6 \\ 4 \end{bmatrix}$$
* **Orthogonality Verification:**
  * With Column 1 of $A$:
    $$\begin{bmatrix} -1 & 1 & 2 \end{bmatrix} \begin{bmatrix} 2/7 \\ -6/7 \\ 4/7 \end{bmatrix} = \frac{-2 - 6 + 8}{7} = 0 \quad \checkmark$$
  * With Column 2 of $A$:
    $$\begin{bmatrix} 1 & 1 & 1 \end{bmatrix} \begin{bmatrix} 2/7 \\ -6/7 \\ 4/7 \end{bmatrix} = \frac{2 - 6 + 4}{7} = 0 \quad \checkmark$$
  The residual vector $\mathbf{e}$ is exactly perpendicular to the column space $C(A)$!

---

## 6. Comprehensive Tutorial Walkthroughs and Problem Sets

### A. Tutorial 3.1: Finding the Four Fundamental Subspaces for a $4 \times 5$ Matrix

#### Problem Statement:
Obtain the four fundamental spaces of $A$ and find its rank and nullity:
$$A = \begin{bmatrix} 2 & 4 & 6 & 8 & 10 \\ 2 & 0 & 2 & 4 & -2 \\ 2 & 2 & 4 & 0 & 2 \\ 4 & 4 & 8 & 12 & 8 \end{bmatrix}$$

---

#### 1. Column Space $C(A)$ Computation:
Apply Gaussian elimination to obtain row echelon form:
* Pivot in $(1, 1)$ is $2$.
* $R_2 \leftarrow R_2 - R_1 \implies \begin{bmatrix} 0 & -4 & -4 & -4 & -12 \end{bmatrix}$
* $R_3 \leftarrow R_3 - R_1 \implies \begin{bmatrix} 0 & -2 & -2 & -8 & -8 \end{bmatrix}$
* $R_4 \leftarrow R_4 - 2R_1 \implies \begin{bmatrix} 0 & -4 & -4 & -4 & -12 \end{bmatrix}$

Intermediate matrix:
$$\begin{bmatrix} 2 & 4 & 6 & 8 & 10 \\ 0 & -4 & -4 & -4 & -12 \\ 0 & -2 & -2 & -8 & -8 \\ 0 & -4 & -4 & -4 & -12 \end{bmatrix}$$

* Pivot in $(2, 2)$ is $-4$.
* $R_3 \leftarrow R_3 - \frac{1}{2}R_2 \implies \begin{bmatrix} 0 & 0 & 0 & -6 & -2 \end{bmatrix}$
* $R_4 \leftarrow R_4 - R_2 \implies \begin{bmatrix} 0 & 0 & 0 & 0 & 0 \end{bmatrix}$

Row Echelon Form $U$:
$$U = \begin{bmatrix} \mathbf{2} & 4 & 6 & 8 & 10 \\ 0 & -\mathbf{4} & -4 & -4 & -12 \\ 0 & 0 & 0 & -\mathbf{6} & -2 \\ 0 & 0 & 0 & 0 & 0 \end{bmatrix}$$

* **Pivot Columns:** Column 1, Column 2, and Column 4.
* **Rank:** $r = 3 \implies \dim(C(A)) = 3$.
* **Basis for $C(A)$:** Formed by the pivot columns of the *original* matrix $A$:
  $$\text{Basis}(C(A)) = \left\{ \begin{bmatrix} 2 \\ 2 \\ 2 \\ 4 \end{bmatrix}, \begin{bmatrix} 4 \\ 0 \\ 2 \\ 4 \end{bmatrix}, \begin{bmatrix} 8 \\ 4 \\ 0 \\ 12 \end{bmatrix} \right\}$$

---

#### 2. Nullspace $N(A)$ Computation:
Solve $U\mathbf{x} = \mathbf{0}$:
$$\begin{aligned}
2x_1 + 4x_2 + 6x_3 + 8x_4 + 10x_5 &= 0 \quad \text{--- (1)} \\
-4x_2 - 4x_3 - 4x_4 - 12x_5 &= 0 \quad \text{--- (2)} \\
-6x_4 - 2x_5 &= 0 \quad \text{--- (3)}
\end{aligned}$$

Free variables correspond to non-pivot columns: $x_3$ and $x_5$.
$$\text{Nullity} = \dim(N(A)) = n - r = 5 - 3 = 2$$

* **Special Solution 1 ($\mathbf{u}$):** Set $x_3 = 1, x_5 = 0$:
  * From (3): $-6x_4 - 0 = 0 \implies x_4 = 0$.
  * From (2): $-4x_2 - 4(1) - 0 - 0 = 0 \implies -4x_2 = 4 \implies x_2 = -1$.
  * From (1): $2x_1 + 4(-1) + 6(1) + 0 + 0 = 0 \implies 2x_1 + 2 = 0 \implies x_1 = -1$.
  $$\mathbf{u} = \begin{bmatrix} -1 \\ -1 \\ 1 \\ 0 \\ 0 \end{bmatrix}$$

* **Special Solution 2 ($\mathbf{v}$):** Set $x_3 = 0, x_5 = 1$:
  * From (3): $-6x_4 - 2(1) = 0 \implies x_4 = -1/3$.
  * From (2): $-4x_2 - 0 - 4(-1/3) - 12(1) = 0 \implies -4x_2 = 12 - 4/3 = 32/3 \implies x_2 = -8/3$.
  * From (1): $2x_1 + 4(-8/3) + 0 + 8(-1/3) + 10(1) = 0$:
    $$2x_1 - \frac{32}{3} - \frac{8}{3} + \frac{30}{3} = 2x_1 - \frac{10}{3} = 0 \implies x_1 = \frac{5}{3}$$
  $$\mathbf{v} = \begin{bmatrix} 5/3 \\ -8/3 \\ 0 \\ -1/3 \\ 1 \end{bmatrix}$$

$$N(A) = \operatorname{span}\left\{ \begin{bmatrix} -1 \\ -1 \\ 1 \\ 0 \\ 0 \end{bmatrix}, \begin{bmatrix} 5/3 \\ -8/3 \\ 0 \\ -1/3 \\ 1 \end{bmatrix} \right\}$$

---

#### 3. Row Space $R(A) = C(A^\top)$ Computation:
Transpose matrix $A^\top$ ($5 \times 4$):
$$A^\top = \begin{bmatrix} 2 & 2 & 2 & 4 \\ 4 & 0 & 2 & 4 \\ 6 & 2 & 4 & 8 \\ 8 & 4 & 0 & 12 \\ 10 & -2 & 2 & 8 \end{bmatrix}$$

Elimination:
* $R_2 \leftarrow R_2 - 2R_1 \implies [0, -4, -2, -4]$
* $R_3 \leftarrow R_3 - 3R_1 \implies [0, -4, -2, -4]$
* $R_4 \leftarrow R_4 - 4R_1 \implies [0, -4, -8, -4]$
* $R_5 \leftarrow R_5 - 5R_1 \implies [0, -12, -8, -12]$

Eliminate with row 2:
* $R_3 \leftarrow R_3 - R_2 \implies [0, 0, 0, 0]$
* $R_4 \leftarrow R_4 - R_2 \implies [0, 0, -6, 0]$
* $R_5 \leftarrow R_5 - 3R_2 \implies [0, 0, -2, 0]$

Swap $R_3 \leftrightarrow R_5$, then eliminate $R_4 \leftarrow R_4 - 3R_3$:
Row echelon form of $A^\top$:
$$\begin{bmatrix} \mathbf{2} & 2 & 2 & 4 \\ 0 & -\mathbf{4} & -2 & -4 \\ 0 & 0 & -\mathbf{2} & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{bmatrix}$$

* Pivot rows of $A^\top$ are rows 1, 2, and 3.
* Therefore, the first 3 rows of $A$ form a basis for $R(A)$:
  $$\text{Basis}(R(A)) = \left\{ \begin{bmatrix} 2 \\ 4 \\ 6 \\ 8 \\ 10 \end{bmatrix}, \begin{bmatrix} 2 \\ 0 \\ 2 \\ 4 \\ -2 \end{bmatrix}, \begin{bmatrix} 2 \\ 2 \\ 4 \\ 0 \\ 2 \end{bmatrix} \right\}, \quad \dim(R(A)) = 3$$

---

#### 4. Left Nullspace $N(A^\top)$ Computation:
Solve $A^\top \mathbf{y} = \mathbf{0}$ using the echelon form of $A^\top$:
$$\begin{bmatrix} 2 & 2 & 2 & 4 \\ 0 & -4 & -2 & -4 \\ 0 & 0 & -2 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{bmatrix} \begin{bmatrix} y_1 \\ y_2 \\ y_3 \\ y_4 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \\ 0 \\ 0 \\ 0 \end{bmatrix}$$

* Pivot variables: $y_1, y_2, y_3$. Free variable: $y_4$.
* Dimension: $\dim(N(A^\top)) = m - r = 4 - 3 = 1$.
* Set free variable $y_4 = 1$:
  * Row 3: $-2y_3 = 0 \implies y_3 = 0$.
  * Row 2: $-4y_2 - 2(0) - 4(1) = 0 \implies y_2 = -1$.
  * Row 1: $2y_1 + 2(-1) + 2(0) + 4(1) = 0 \implies 2y_1 + 2 = 0 \implies y_1 = -1$.

$$N(A^\top) = \operatorname{span}\left\{ \begin{bmatrix} -1 \\ -1 \\ 0 \\ 1 \end{bmatrix} \right\}$$

---

### B. Tutorial 3.2: Row Space via RREF & Solvability of $Ax = b$

#### Example 2: Row Space from Reduced Row Echelon Form
For matrix $B$, find its row space by computing its RREF:
$$B = \begin{bmatrix} 1 & 1 & 2 \\ 2 & 3 & 6 \\ -2 & 1 & 2 \end{bmatrix}$$

##### Row Operations to Echelon Form:
* $R_2 \leftarrow R_2 - 2R_1$:
  $$\begin{bmatrix} 2 & 3 & 6 \end{bmatrix} - 2\begin{bmatrix} 1 & 1 & 2 \end{bmatrix} = \begin{bmatrix} 0 & 1 & 2 \end{bmatrix}$$
* $R_3 \leftarrow R_3 + 2R_1$:
  $$\begin{bmatrix} -2 & 1 & 2 \end{bmatrix} + 2\begin{bmatrix} 1 & 1 & 2 \end{bmatrix} = \begin{bmatrix} 0 & 3 & 6 \end{bmatrix}$$
* $R_3 \leftarrow R_3 - 3R_2$:
  $$\begin{bmatrix} 0 & 3 & 6 \end{bmatrix} - 3\begin{bmatrix} 0 & 1 & 2 \end{bmatrix} = \begin{bmatrix} 0 & 0 & 0 \end{bmatrix}$$

Row echelon form:
$$U = \begin{bmatrix} 1 & 1 & 2 \\ 0 & 1 & 2 \\ 0 & 0 & 0 \end{bmatrix}$$

##### Back-Substitution to RREF:
* $R_1 \leftarrow R_1 - R_2$:
  $$\begin{bmatrix} 1 & 1 & 2 \end{bmatrix} - \begin{bmatrix} 0 & 1 & 2 \end{bmatrix} = \begin{bmatrix} 1 & 0 & 0 \end{bmatrix}$$

Reduced Row Echelon Form:
$$R = \begin{bmatrix} \mathbf{1} & \mathbf{0} & \mathbf{0} \\ \mathbf{0} & \mathbf{1} & \mathbf{2} \\ 0 & 0 & 0 \end{bmatrix}$$

> [!TIP]
> The elementary row operations that transform $B$ into $R$ preserve the row space ($R(B) = R(R)$). The non-zero rows of $R$ form a canonical, simplified basis for $R(B)$:
> $$\text{Row Space of } B = \operatorname{span}\left\{ \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix}, \begin{bmatrix} 0 \\ 1 \\ 2 \end{bmatrix} \right\}$$

---

#### Example 3: Solvability Condition for $A\mathbf{x} = \mathbf{b}$
Consider the linear system:
$$\begin{aligned}
x_1 + 2x_2 - 2x_3 &= b_1 \\
2x_1 + 5x_2 - 4x_3 &= b_2 \\
4x_1 + 9x_2 - 8x_3 &= b_3
\end{aligned}$$

1. **Under what condition on $b_1, b_2, b_3$ is the system solvable?**
2. **Check whether $\mathbf{b} = [3, -1, 5]^\top$ satisfies the condition.**

##### Elimination on Augmented Matrix:
$$[A \mid \mathbf{b}] = \left[\begin{array}{ccc|c} 1 & 2 & -2 & b_1 \\ 2 & 5 & -4 & b_2 \\ 4 & 9 & -8 & b_3 \end{array}\right]$$

* $R_2 \leftarrow R_2 - 2R_1$:
  $$\left[\begin{array}{ccc|c} 0 & 1 & 0 & b_2 - 2b_1 \end{array}\right]$$
* $R_3 \leftarrow R_3 - 4R_1$:
  $$\left[\begin{array}{ccc|c} 0 & 1 & 0 & b_3 - 4b_1 \end{array}\right]$$

Intermediate matrix:
$$\left[\begin{array}{ccc|c} 1 & 2 & -2 & b_1 \\ 0 & 1 & 0 & b_2 - 2b_1 \\ 0 & 1 & 0 & b_3 - 4b_1 \end{array}\right]$$

* $R_3 \leftarrow R_3 - R_2$:
  $$\begin{aligned}
  (b_3 - 4b_1) - (b_2 - 2b_1) &= b_3 - b_2 - 2b_1
  \end{aligned}$$

Echelon form:
$$\left[\begin{array}{ccc|c} 1 & 2 & -2 & b_1 \\ 0 & 1 & 0 & b_2 - 2b_1 \\ \mathbf{0} & \mathbf{0} & \mathbf{0} & \mathbf{b_3 - b_2 - 2b_1} \end{array}\right]$$

##### Consistency Condition:
For the system to have a solution, the bottom row must not produce a contradiction ($0 = \text{non-zero}$):
$$\mathbf{b_3 - b_2 - 2b_1 = 0 \iff -2b_1 - b_2 + b_3 = 0}$$

> **Theoretical Connection:**
> Notice that $[-2, -1, 1] A = \mathbf{0}^\top$. The vector $\mathbf{y} = \begin{bmatrix} -2 \\ -1 \\ 1 \end{bmatrix}$ spans the left nullspace $N(A^\top)$!
> The solvability condition is precisely:
> $$\mathbf{y}^\top \mathbf{b} = 0 \iff \mathbf{b} \perp N(A^\top)$$
> This reinforces that $A\mathbf{x} = \mathbf{b}$ is solvable if and only if $\mathbf{b} \in C(A) = (N(A^\top))^\perp$.

##### Checking Vector $\mathbf{b} = [3, -1, 5]^\top$:
Substitute $b_1 = 3, b_2 = -1, b_3 = 5$:
$$b_3 - b_2 - 2b_1 = 5 - (-1) - 2(3) = 5 + 1 - 6 = 0$$
The condition is satisfied ($0 = 0$). Thus, the system is **solvable** and $\mathbf{b} \in C(A)$.

---

### C. Tutorial 3.3: Orthogonality, 1D Projections, and 5-Point Least Squares

#### Example 1: Pairwise Orthogonality Check
Given the set of vectors in $\mathbb{R}^4$:
$$S = \left\{ \mathbf{u} = \begin{bmatrix} 1 \\ 2 \\ 4 \\ 0 \end{bmatrix}, \; \mathbf{v} = \begin{bmatrix} -2 \\ 3 \\ -1 \\ 0 \end{bmatrix}, \; \mathbf{w} = \begin{bmatrix} 0 \\ 2 \\ 6 \\ -1 \end{bmatrix} \right\}$$
Determine which pair(s) are orthogonal:

* **Pair $(\mathbf{u}, \mathbf{v})$:**
  $$\mathbf{u} \cdot \mathbf{v} = 1(-2) + 2(3) + 4(-1) + 0(0) = -2 + 6 - 4 + 0 = 0 \implies \mathbf{u} \perp \mathbf{v} \quad \checkmark$$
* **Pair $(\mathbf{v}, \mathbf{w})$:**
  $$\mathbf{v} \cdot \mathbf{w} = -2(0) + 3(2) + (-1)(6) + 0(-1) = 0 + 6 - 6 + 0 = 0 \implies \mathbf{v} \perp \mathbf{w} \quad \checkmark$$
* **Pair $(\mathbf{u}, \mathbf{w})$:**
  $$\mathbf{u} \cdot \mathbf{w} = 1(0) + 2(2) + 4(6) + 0(-1) = 0 + 4 + 24 + 0 = 28 \ne 0 \implies \mathbf{u} \not\perp \mathbf{w}$$

**Conclusion:** The orthogonal pairs are $(\mathbf{u}, \mathbf{v})$ and $(\mathbf{v}, \mathbf{w})$.

---

#### Example 2: Projection Matrix and Error Vector
Given $\mathbf{a} = \begin{bmatrix} 2 \\ -1 \\ 2 \\ 3 \end{bmatrix}$ and $\mathbf{b} = \begin{bmatrix} 1 \\ 3 \\ -2 \\ 5 \end{bmatrix}$:
1. Find the projection matrix $P$ for $\mathbf{a}$.
2. Obtain the projection $\mathbf{p}$ of $\mathbf{b}$ onto $\mathbf{a}$ and compute the error $\mathbf{e}$.

##### 1. Projection Matrix $P$:
$$\mathbf{a}^\top \mathbf{a} = 2^2 + (-1)^2 + 2^2 + 3^2 = 4 + 1 + 4 + 9 = 18$$

$$\mathbf{a} \mathbf{a}^\top = \begin{bmatrix} 2 \\ -1 \\ 2 \\ 3 \end{bmatrix} \begin{bmatrix} 2 & -1 & 2 & 3 \end{bmatrix} = \begin{bmatrix} 4 & -2 & 4 & 6 \\ -2 & 1 & -2 & -3 \\ 4 & -2 & 4 & 6 \\ 6 & -3 & 6 & 9 \end{bmatrix}$$

$$P = \frac{\mathbf{a}\mathbf{a}^\top}{\mathbf{a}^\top \mathbf{a}} = \begin{bmatrix} 4/18 & -2/18 & 4/18 & 6/18 \\ -2/18 & 1/18 & -2/18 & -3/18 \\ 4/18 & -2/18 & 4/18 & 6/18 \\ 6/18 & -3/18 & 6/18 & 9/18 \end{bmatrix} = \begin{bmatrix} 2/9 & -1/9 & 2/9 & 1/3 \\ -1/9 & 1/18 & -1/9 & -1/6 \\ 2/9 & -1/9 & 2/9 & 1/3 \\ 1/3 & -1/6 & 1/3 & 1/2 \end{bmatrix}$$

##### 2. Projection $\mathbf{p}$ and Error $\mathbf{e}$:
$$\mathbf{a}^\top \mathbf{b} = 2(1) + (-1)(3) + 2(-2) + 3(5) = 2 - 3 - 4 + 15 = 10$$
$$\mathbf{p} = \left(\frac{\mathbf{a}^\top \mathbf{b}}{\mathbf{a}^\top \mathbf{a}}\right) \mathbf{a} = \frac{10}{18} \mathbf{a} = \frac{5}{9} \begin{bmatrix} 2 \\ -1 \\ 2 \\ 3 \end{bmatrix} = \begin{bmatrix} 10/9 \\ -5/9 \\ 10/9 \\ 5/3 \end{bmatrix}$$

Error vector:
$$\mathbf{e} = \mathbf{b} - \mathbf{p} = \begin{bmatrix} 1 \\ 3 \\ -2 \\ 5 \end{bmatrix} - \begin{bmatrix} 10/9 \\ -5/9 \\ 10/9 \\ 15/9 \end{bmatrix} = \frac{1}{9} \begin{bmatrix} 9 - 10 \\ 27 - (-5) \\ -18 - 10 \\ 45 - 15 \end{bmatrix} = \frac{1}{9} \begin{bmatrix} -1 \\ 32 \\ -28 \\ 30 \end{bmatrix}$$

##### Verification:
$$\mathbf{a}^\top \mathbf{e} = \frac{1}{9} [2(-1) - 1(32) + 2(-28) + 3(30)] = \frac{1}{9} [-2 - 32 - 56 + 90] = \frac{1}{9}[0] = 0 \quad \checkmark$$

---

#### Example 3: 5-Point Least Squares Line Fitting
Fit a straight line $y = \hat{\theta}' x + \hat{\theta}''$ through the 5 data points:

| $i$ | $x_i$ | $y_i$ |
| :---: | :---: | :---: |
| 1 | 1 | 2.6 |
| 2 | 2 | 3.4 |
| 3 | 3 | 7.1 |
| 4 | 4 | 10.2 |
| 5 | 5 | 13.5 |

##### Matrix Formulation:
$$A = \begin{bmatrix} 1 & 1 \\ 2 & 1 \\ 3 & 1 \\ 4 & 1 \\ 5 & 1 \end{bmatrix}, \quad \mathbf{b} = \begin{bmatrix} 2.6 \\ 3.4 \\ 7.1 \\ 10.2 \\ 13.5 \end{bmatrix}$$

##### Calculating $A^\top A$:
$$A^\top = \begin{bmatrix} 1 & 2 & 3 & 4 & 5 \\ 1 & 1 & 1 & 1 & 1 \end{bmatrix}$$

$$\begin{aligned}
(A^\top A)_{11} &= \sum x_i^2 = 1^2 + 2^2 + 3^2 + 4^2 + 5^2 = 1 + 4 + 9 + 16 + 25 = 55 \\
(A^\top A)_{12} = (A^\top A)_{21} &= \sum x_i = 1 + 2 + 3 + 4 + 5 = 15 \\
(A^\top A)_{22} &= \sum 1 = 5
\end{aligned}$$

$$A^\top A = \begin{bmatrix} 55 & 15 \\ 15 & 5 \end{bmatrix}$$

##### Calculating $A^\top \mathbf{b}$:
$$\begin{aligned}
(A^\top \mathbf{b})_1 &= \sum x_i y_i = 1(2.6) + 2(3.4) + 3(7.1) + 4(10.2) + 5(13.5) \\
&= 2.6 + 6.8 + 21.3 + 40.8 + 67.5 = 139.0 \\
(A^\top \mathbf{b})_2 &= \sum y_i = 2.6 + 3.4 + 7.1 + 10.2 + 13.5 = 36.8
\end{aligned}$$

$$A^\top \mathbf{b} = \begin{bmatrix} 139 \\ 36.8 \end{bmatrix}$$

##### Solving the Normal Equations:
$$\begin{bmatrix} 55 & 15 \\ 15 & 5 \end{bmatrix} \begin{bmatrix} \hat{\theta}' \\ \hat{\theta}'' \end{bmatrix} = \begin{bmatrix} 139 \\ 36.8 \end{bmatrix}$$

Equations:
$$\begin{aligned}
55\hat{\theta}' + 15\hat{\theta}'' &= 139 \quad \text{--- (1)} \\
15\hat{\theta}' + 5\hat{\theta}'' &= 36.8 \quad \text{--- (2)}
\end{aligned}$$

Multiply equation (2) by 3:
$$45\hat{\theta}' + 15\hat{\theta}'' = 110.4 \quad \text{--- (3)}$$

Subtract equation (3) from equation (1):
$$10\hat{\theta}' = 139 - 110.4 = 28.6 \implies \mathbf{\hat{\theta}' = 2.86} \quad (\text{slope})$$

Substitute $\hat{\theta}' = 2.86$ into equation (2):
$$5\hat{\theta}'' = 36.8 - 15(2.86) = 36.8 - 42.9 = -6.1 \implies \mathbf{\hat{\theta}'' = -1.22} \quad (\text{intercept})$$

##### Final Best-Fit Model:
$$y = 2.86x - 1.22$$

```
    y
    |                                                / (5, 13.5)
 15 |                                            *  /
    |                                              /
    |                                     (4, 10.2)
 10 |                                    *        /
    |                                            /
    |                            (3, 7.1)       /
  5 |                           *              /
    |                                         /
    |                 (2, 3.4)               /  y = 2.86x - 1.22
    |                *                      /
    |       (1, 2.6)*                      /
  0 └───────┬────────┬────────┬────────────┬─────────────> x
            1        2        3            4      5
```

---

## 7. Master Summary & Key ML Takeaways

### A. Summary Formula Sheet

| Concept | Mathematical Formula | Key Properties / Remarks |
| :--- | :---: | :--- |
| **Rank-Nullity Theorem** | $r + (n - r) = n$ | Dimension of row space + dimension of nullspace = number of columns. |
| **Row Space $\perp$ Nullspace** | $R(A) \perp N(A)$ in $\mathbb{R}^n$ | $R(A)^\perp = N(A)$; direct sum $\mathbb{R}^n = R(A) \oplus N(A)$. |
| **Col Space $\perp$ Left Nullspace** | $C(A) \perp N(A^\top)$ in $\mathbb{R}^m$ | $C(A)^\perp = N(A^\top)$; direct sum $\mathbb{R}^m = C(A) \oplus N(A^\top)$. |
| **Solvability Criterion** | $A\mathbf{x} = \mathbf{b} \text{ solvable} \iff \mathbf{b} \perp N(A^\top)$ | $\mathbf{y}^\top \mathbf{b} = 0$ for all $\mathbf{y} \in N(A^\top)$. |
| **1D Projection Scalar** | $\hat{x} = \frac{\mathbf{a}^\top \mathbf{b}}{\mathbf{a}^\top \mathbf{a}}$ | Derived from orthogonality $(b - \hat{x}a) \perp a$. |
| **1D Projection Matrix** | $P = \frac{\mathbf{a}\mathbf{a}^\top}{\mathbf{a}^\top \mathbf{a}}$ | $\operatorname{rank}(P) = 1$, $P^\top = P$, $P^2 = P$. |
| **Cauchy-Schwarz** | $|\mathbf{a}^\top \mathbf{b}| \le \|\mathbf{a}\| \|\mathbf{b}\|$ | Direct consequence of non-negative error norm $\|\mathbf{e}\|^2 \ge 0$. |
| **Normal Equations** | $A^\top A \mathbf{\hat{x}} = A^\top \mathbf{b}$ | Always consistent, even when $A\mathbf{x} = \mathbf{b}$ has no solution. |
| **Least Squares Solution** | $\mathbf{\hat{x}} = (A^\top A)^{-1} A^\top \mathbf{b}$ | Requires columns of $A$ to be linearly independent. |
| **Subspace Projection Matrix** | $P = A(A^\top A)^{-1} A^\top$ | Projects any vector onto $C(A)$; $P^\top = P$, $P^2 = P$. |
| **Residual Error Projector** | $I - P = I - A(A^\top A)^{-1} A^\top$ | Projects onto $N(A^\top)$; orthogonal complement of $C(A)$. |

---

### B. Direct Machine Learning Applications
1. **Ordinary Least Squares (OLS) Regression:**
   Direct solution to minimizing mean squared error ($L_2$ loss) without iterative gradient descent: $\hat{\boldsymbol{\theta}} = (X^\top X)^{-1} X^\top \mathbf{y}$.
2. **Ridge Regression ($L_2$ Regularization):**
   When feature columns are collinear or $n > m$, $X^\top X$ is singular. Adding $\lambda I$ guarantees invertibility: $\hat{\boldsymbol{\theta}}_\text{ridge} = (X^\top X + \lambda I)^{-1} X^\top \mathbf{y}$.
3. **Principal Component Analysis (PCA):**
   Projects high-dimensional feature vectors onto lower-dimensional orthogonal subspaces that maximize variance and minimize projection error.
4. **Support Vector Machines (SVMs) & Hyperplanes:**
   The normal vector to the decision boundary hyperplane is orthogonal to all vectors lying within the hyperplane, identical to the left nullspace property.
