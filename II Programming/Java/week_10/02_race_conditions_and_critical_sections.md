# The Race Condition Problem

- A **Race Condition** occurs when multiple threads concurrently read and write shared mutable state, and the final outcome depends on the unpredictable timing/interleaving of execution.

---

# The Classic `count++` Lost Update Bug

Consider a simple counter incremented by two concurrent threads:

```java
// Java source:
count++;

// Translates to 3 low-level machine instructions:
1. LOAD  Reg1, count  (Read current value)
2. ADD   Reg1, 1      (Increment register)
3. STORE count, Reg1  (Write back to memory)
```

### Dangerous Interleaving:
```text
Thread 1 (Wants to increment)     Thread 2 (Wants to increment)     count (Memory)
----------------------------------------------------------------------------------
1. LOAD Reg1, count (sees 0)                                            0
                                  1. LOAD Reg2, count (sees 0)          0
2. ADD  Reg1, 1 (Reg1 = 1)                                              0
                                  2. ADD  Reg2, 1 (Reg2 = 1)            0
3. STORE count, Reg1 (writes 1)                                         1
                                  3. STORE count, Reg2 (writes 1)       1  <-- Lost Update!
```

- Both threads incremented the counter, but the final value is `1` instead of `2`!

---

# The Critical Section Problem

- **Critical Section**: A block of code that accesses shared mutable resources and must not be concurrently executed by more than one thread.
- **Three Requirements for Correct Synchronization**:
  1. **Mutual Exclusion**: At most one thread can execute in the critical section at any instant.
  2. **Progress**: If no thread is in the critical section, only threads waiting to enter can participate in deciding who enters next.
  3. **Bounded Waiting**: A thread requesting entry must not wait indefinitely (no starvation).

---

# Summary

- Race conditions cause silent data corruption due to non-atomic read-modify-write sequences
- Critical sections require strict **Mutual Exclusion**, **Progress**, and **Bounded Waiting**
