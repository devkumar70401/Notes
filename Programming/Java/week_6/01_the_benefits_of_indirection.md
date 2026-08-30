# The Principle of Indirection

> *"All problems in computer science can be solved by another level of indirection, except of course for the problem of too many levels of indirection."* — David Wheeler

- **Indirection**: Accessing a value or resource through an intermediate reference (pointer/handle) rather than directly.

---

# Why Indirection Matters in Data Structures

### 1. Decoupling Interface from Representation
- A client holds a reference to a `List` interface without knowing whether it is backed by a contiguous array or a doubly-linked node chain.

### 2. Flexible Resizing & Allocation
- Dynamic structures can swap out internal memory blocks without changing external object references held by clients:

```text
Client Reference -----> [ LinearList Object ]
                               |
                               +-----> [ Internal Buffer: Array of 100 items ]
                                                | (Expands to)
                                                v
                                       [ New Buffer: Array of 200 items ]
```

---

# Summary

- Indirection provides flexibility by separating reference handles from actual data storage
- Enables dynamic memory resizing, polymorphic method binding, and encapsulation
