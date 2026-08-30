# Software Mutual Exclusion: Peterson's Algorithm

- Can we achieve mutual exclusion between two threads using pure software logic without special hardware support?
- **Peterson's Algorithm** (1981) solves mutual exclusion for two threads ($T_0$ and $T_1$).

---

# Algorithm Structure

```c
// Shared variables:
boolean flag[2]; // flag[i] = true means Thread i wants to enter
int turn;        // Whose turn it is to enter if both compete

// Code for Thread 0 (i = 0, other = 1):
flag[0] = true;         // I want to enter
turn = 1;               // Give priority to the other thread

while (flag[1] && turn == 1) {
    // Busy wait (spin)
}

// --- CRITICAL SECTION ---

flag[0] = false;        // Exit: I am done
```

---

# Correctness Proof

1. **Mutual Exclusion**: For both threads to be in the critical section simultaneously, `turn == 0` and `turn == 1` would both have to hold at the same time, which is impossible.
2. **Progress**: The `turn` variable resolves ties immediately if both set `flag = true` at the same time.
3. **Bounded Waiting**: A thread can wait at most one turn before gaining entry.

---

# Summary

- Peterson's algorithm proves that software-only mutual exclusion is mathematically possible for two threads
- Modern multi-core architectures require memory barriers / volatile semantics due to CPU instruction reordering and caching
