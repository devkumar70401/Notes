# Java Maps (`Map<K, V>`)

- A `Map` stores **Key-Value pairs** (associations / dictionaries)
- Keys are strictly **unique**; each key maps to exactly one value
- `Map` is part of JCF, but does **not** extend `Collection<E>` (it models mappings, not single-element collections).

```text
Keys (Set) ----> Values (Collection)
  "alice"  ---->  95
  "bob"    ---->  82
```

---

# Concrete Map Implementations

| Implementation | Internal Structure | Ordering | Lookup / Insert |
| :--- | :--- | :--- | :--- |
| **`HashMap<K,V>`** | Hash Table (Buckets + Red-Black trees) | None | **$O(1)$** average |
| **`TreeMap<K,V>`** | Red-Black Tree | Sorted by Key | **$O(\log n)$** |
| **`LinkedHashMap<K,V>`** | Hash Table + Doubly-Linked List | Insertion order (or access order for LRU) | **$O(1)$** |

---

# The `hashCode()` and `equals()` Contract

For custom classes used as Map keys:

1. If `o1.equals(o2)` is `true`, then `o1.hashCode() == o2.hashCode()` **must be true**.
2. If `hashCode()` is unequal, `equals()` must be `false`.
3. Inconsistent `hashCode()` causes keys to be placed in wrong buckets, making them unretrievable!

```java
// Iterating over a Map
Map<String, Integer> scores = new HashMap<>();
scores.put("Alice", 95);
scores.put("Bob", 88);

// Iterating over Key-Value entries
for (Map.Entry<String, Integer> entry : scores.entrySet()) {
  System.out.println(entry.getKey() + " -> " + entry.getValue());
}
```

---

# Summary

- `Map<K, V>` associates unique keys with values
- `HashMap` is the default high-performance choice ($O(1)$)
- Custom map keys must correctly override both `equals()` and `hashCode()`
