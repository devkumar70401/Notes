# Hardware Synchronization Primitives

- Software-only algorithms (like Peterson's) are complex and do not scale easily to hundreds of threads.
- Modern CPUs provide special **atomic hardware instructions**.

---

# 1. Test-and-Set (TAS)

- Executes reading and setting a memory address as a single uninterruptible hardware transaction:

```c
// Conceptually equivalent to atomic hardware execution:
boolean TestAndSet(boolean *target) {
    boolean rv = *target;
    *target = true;
    return rv;
}
```

```c
// Simple Spinlock using TAS:
while (TestAndSet(&lock)) {
    // Spin until lock becomes false
}
// --- Critical Section ---
lock = false;
```

---

# 2. Compare-and-Swap (CAS)

- Used as the foundation for modern lock-free algorithms and Java's `java.util.concurrent.atomic` package:

```c
int CompareAndSwap(int *val, int expected, int new_val) {
    int prev = *val;
    if (prev == expected) {
        *val = new_val;
    }
    return prev;
}
```

- If another thread modified the value in the meantime, CAS fails safely and the caller can retry in a loop without blocking.

---

# Summary

- Hardware atomic primitives (`Test-and-Set`, `Compare-and-Swap`) enable efficient locks
- CAS forms the engine of modern non-blocking, lock-free concurrency in Java
