# Memory Organization in Execution

When a Java program runs, the JVM allocates memory into two primary runtime areas:

```text
+------------------------------------+
|               STACK                |
|  - Method Call Frames              |
|  - Local primitive variables       |
|  - Object reference pointers       |
|  - Fast, LIFO allocation           |
+------------------------------------+
|               HEAP                 |
|  - Dynamically allocated Objects   |
|  - Arrays                          |
|  - Managed by Garbage Collector    |
+------------------------------------+
```

---

# The Stack (Execution Frames)

- Follows **Last-In, First-Out (LIFO)** execution order
- Whenever a method is invoked:
  - A new **Stack Frame** is pushed onto the call stack
  - Stores method arguments, local primitive variables, and references
- When the method finishes execution:
  - Its stack frame is automatically popped off and destroyed
  - Extremely fast allocation and deallocation with zero fragmentation overhead.

---

# The Heap (Dynamic Object Storage)

- All objects created using the **`new`** keyword are allocated in the Heap
- Heap memory persists independently of method call lifetimes:
  - An object created inside a function remains alive as long as some reference points to it.

```java
public void createObjects() {
  int x = 100;                 // Local primitive -> Stack
  int[] data = new int[1000];  // Array object -> Heap, reference 'data' -> Stack
} // Method returns: Stack frame for createObjects() is popped.
  // 'data' reference is destroyed, but Heap memory for int[1000] remains until GC collects it.
```

---

# Garbage Collection (Automatic Reclamation)

- In C/C++, manual deallocation (`free(p)` / `delete p`) leads to:
  - **Memory Leaks**: Forgetting to free memory
  - **Dangling Pointers**: Freeing memory while references still exist
- **Java's Garbage Collector (GC)**:
  - Automatically runs in the background
  - Identifies objects that are **unreachable** (no active references leading from the Stack / Roots)
  - Safely reclaims their memory.

---

# Summary

- **Stack**: Stores local method execution frames, primitive variables, and object references (automatic, deterministic lifecycle).
- **Heap**: Stores all objects and arrays allocated with `new` (dynamic lifecycle).
- Java eliminates manual memory management bugs through background **Garbage Collection**.
