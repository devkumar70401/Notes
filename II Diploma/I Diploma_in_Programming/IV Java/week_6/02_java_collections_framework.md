# Java Collections Framework (JCF)

```mermaid
graph TD
    ITER["Iterable&lt;E&gt;"] --> COLL["Collection&lt;E&gt;"]
    
    COLL --> LIST["List&lt;E&gt;<br>(Ordered, Duplicates Allowed)"]
    COLL --> SET["Set&lt;E&gt;<br>(Unique Elements)"]
    COLL --> QUEUE["Queue&lt;E&gt;<br>(FIFO Staging)"]

    LIST --> AL["ArrayList&lt;E&gt;"]
    LIST --> LL["LinkedList&lt;E&gt;"]

    SET --> HS["HashSet&lt;E&gt;"]
    SET --> TS["TreeSet&lt;E&gt; (SortedSet)"]

    QUEUE --> PQ["PriorityQueue&lt;E&gt;"]
    QUEUE --> DEQ["Deque&lt;E&gt; (ArrayDeque)"]
```


- Prior to Java 2, data structures were ad-hoc (`Vector`, `Hashtable`, raw arrays).
- JCF provides a unified architecture for representing and manipulating collections.

```text
                         Iterable<E>
                              |
                        Collection<E>
                      /       |                            /        |                        List<E>     Set<E>    Queue<E>
                              |          |
                           SortedSet<E> Deque<E>
```

---

# Core Collection Interfaces

| Interface | Characteristics | Key Implementations |
| :--- | :--- | :--- |
| **`Collection<E>`** | Root interface for groups of objects (`add`, `remove`, `contains`, `size`) | All below |
| **`List<E>`** | **Ordered sequence**, allows duplicates, indexed access (`get(i)`) | `ArrayList`, `LinkedList` |
| **`Set<E>`** | **No duplicates**, models mathematical sets | `HashSet`, `TreeSet`, `LinkedHashSet` |
| **`Queue<E>`** | FIFO ordering for staging elements (`offer`, `poll`, `peek`) | `PriorityQueue`, `ArrayDeque` |
| **`Deque<E>`** | Double-ended queue, supports stack and queue operations | `ArrayDeque`, `LinkedList` |

---

# Summary

- The Java Collections Framework provides standardized, reusable data structures
- Built around core interfaces: `List` (ordered), `Set` (unique), `Queue` (buffered)
- All collections implement `Iterable<E>`, allowing enhanced `for-each` traversal
