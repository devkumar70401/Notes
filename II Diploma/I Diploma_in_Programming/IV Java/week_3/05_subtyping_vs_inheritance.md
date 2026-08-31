# Subtyping vs Inheritance: Two Distinct Concepts

- In Object-Oriented languages like Java, the class hierarchy combines two fundamentally different ideas into a single mechanism (`extends`):
  1. **Subtyping** (Interface Compatibility / Contract)
  2. **Inheritance** (Implementation Reuse / Code Sharing)

---

# 1. Subtyping (Behavioral Compatibility)

- **Definition**: Type `B` is a subtype of type `A` if the capabilities of `B` are a **superset** of `A`.
- **Substitution Principle (Liskov Substitution)**:
  - If `B` is a subtype of `A`, wherever an object of type `A` is expected, an object of type `B` can be safely provided:
    ```java
    Employee e = new Manager("Alice", 80000.0, "Bob");
    ```
- Subtyping is about **external interface compatibility**:
  - Every method that can be invoked on `A` can also be invoked on `B` with valid semantics.

---

# 2. Inheritance (Code Reuse)

- **Definition**: Class `B` inherits from class `A` if `B` is implemented by directly reusing the code and state mechanisms written for `A`.
- Example: `Manager` reuses `Employee`'s constructor and bonus calculation (`super.bonus()`).
- Inheritance is about **internal implementation mechanics**:
  - Reusing existing code to avoid duplication.

---

# The Classic Counterexample: Queue, Stack, and Deque

Consider three fundamental data structures:

| Data Structure | Operations Supported |
| :--- | :--- |
| **`Queue`** (FIFO) | `insert_rear()`, `delete_front()` |
| **`Stack`** (LIFO) | `insert_front()`, `delete_front()` |
| **`Deque`** (Double-Ended Queue) | `insert_front()`, `delete_front()`, `insert_rear()`, `delete_rear()` |

---

# Analyzing the Relationships

```mermaid
graph TD
    subgraph Subtyping Hierarchy (Capabilities)
        Q1["Queue (2 ops)"]
        S1["Stack (2 ops)"]
        D1["Deque (4 ops)"]
        D1 -.->|Subtype of| Q1
        D1 -.->|Subtype of| S1
    end

    subgraph Inheritance Hierarchy (Code Reuse)
        D2["Deque (Doubly-Linked Core)"]
        Q2["Queue (Restricted Deque)"]
        S2["Stack (Restricted Deque)"]
        Q2 -->|Reuses implementation| D2
        S2 -->|Reuses implementation| D2
    end
```


### From the Perspective of Subtyping (Capabilities):
- `Deque` provides all 4 operations.
- Anyone expecting a `Queue` needs only `insert_rear()` and `delete_front()` (which `Deque` supports).
- Anyone expecting a `Stack` needs only `insert_front()` and `delete_front()` (which `Deque` supports).
- **Subtype Conclusion**: `Deque` is a **subtype** of `Queue` and a **subtype** of `Stack`!
  ```text
  Queue (2 ops)      Stack (2 ops)
        \                 /
         \               /
          Deque (4 ops)  [Subtype]
  ```

### From the Perspective of Inheritance (Code Reuse):
- Suppose you already spent time writing a complex, bug-free doubly-linked `Deque` class with all 4 operations.
- How can you implement `Stack` and `Queue` with minimal work?
  - Simply reuse (`inherit from`) `Deque`, and suppress or restrict the unused two methods!
- **Inheritance Conclusion**: `Queue` and `Stack` should inherit from `Deque`!
  ```text
          Deque (4 ops)
         /             \
        /               \
  Queue (reused)    Stack (reused)  [Inheritance]
  ```

---

# The Design Tension

- Notice the complete contradiction:
  - **Subtyping Arrow**: Points from `Deque` towards `Queue` / `Stack`
  - **Inheritance Arrow**: Points from `Queue` / `Stack` towards `Deque`
- When a language forces both concepts into a single `class A extends B` mechanism:
  - We often inherit implementation we do not want, OR
  - We miss out on clean subtype polymorphism.
- **Modern Solution**: Separate interfaces from classes:
  - Use **Interfaces** for Subtyping contracts (`implements`)
  - Use **Composition / Delegation** (or abstract classes) for Code Reuse.

---

# Summary

- **Subtyping** represents interface compatibility (every operation of `A` is supported by `B`).
- **Inheritance** represents implementation reuse (`B` reuses methods/code written for `A`).
- The `Queue`, `Stack`, and `Deque` example proves that subtyping relationships and code reuse hierarchies can point in opposite directions.
- Conflating subtyping and inheritance in a single class hierarchy can lead to brittle designs, motivating the use of Interfaces and Composition.
