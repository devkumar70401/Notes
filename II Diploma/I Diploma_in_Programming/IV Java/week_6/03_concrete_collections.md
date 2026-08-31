# Concrete Collection Implementations

Choosing the right collection implementation directly impacts runtime performance and memory usage.

---

# 1. Lists: `ArrayList` vs `LinkedList`

| Operation | `ArrayList<E>` (Dynamic Array) | `LinkedList<E>` (Doubly-Linked) |
| :--- | :--- | :--- |
| **Random Access (`get(i)`)** | **$O(1)$** (Direct pointer arithmetic) | **$O(n)$** (Sequential traversal) |
| **Insert/Delete at End** | **$O(1)$** amortized | **$O(1)$** |
| **Insert/Delete at Beginning/Middle** | **$O(n)$** (Requires element shifting) | **$O(1)$** (Once node is located) |
| **Memory Overhead** | Low (contiguous memory) | High (extra pointers per node) |

> **Rule of Thumb**: Default to `ArrayList` in 95% of cases due to CPU cache locality and $O(1)$ random access.

---

# 2. Sets: `HashSet` vs `TreeSet`

| Feature | `HashSet<E>` | `TreeSet<E>` |
| :--- | :--- | :--- |
| **Underlying Structure** | Hash Table (`HashMap`) | Red-Black Balanced Binary Search Tree |
| **Time Complexity** | **$O(1)$** average (`add`/`contains`) | **$O(\log n)$** guaranteed |
| **Ordering** | Unordered / Unpredictable | **Sorted natural order** or via `Comparator` |
| **Requirement on `<E>`** | Valid `hashCode()` and `equals()` | Implements `Comparable<E>` |

---

# Summary

- Use `ArrayList` for fast random access and low memory overhead
- Use `HashSet` for high-throughput uniqueness checks ($O(1)$)
- Use `TreeSet` when elements must be maintained in sorted order ($O(\log n)$)
