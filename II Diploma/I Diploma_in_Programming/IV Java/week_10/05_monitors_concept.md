# The Monitor Abstraction

```mermaid
graph TD
    subgraph Monitor Structure
        ENTRY["Entry Queue (Threads waiting to enter)"]
        MUTEX["Mutual Exclusion Lock<br>[ Active Running Thread ]"]
        WAITSET["Condition Variable Wait Set<br>(Threads calling wait())"]
    end

    ENTRY -->|Acquires Lock| MUTEX
    MUTEX -->|condition not met: wait()| WAITSET
    WAITSET -->|condition met: notify()| MUTEX
```


- Writing raw low-level synchronization (semaphores, spinlocks) is error-prone (forgetting to unlock leads to deadlock).
- **Monitor** (invented by C.A.R. Hoare and Edsger Dijkstra):
  - A high-level synchronization construct that encapsulates data, methods, and automatic mutual exclusion into a single module.

```text
+-------------------------------------------------------+
|                       MONITOR                         |
|                                                       |
|  [ Private Shared State ]                             |
|                                                       |
|  [ Public Synchronized Methods ]                      |
|    - Automatic Mutual Exclusion:                      |
|      Only ONE thread can execute inside at any time   |
|                                                       |
|  [ Condition Variables: wait() / signal() ]           |
|    - Allows threads to suspend and wake up            |
+-------------------------------------------------------+
```

---

# Condition Variables (`wait` and `signal`)

- If a thread enters a monitor and finds that a pre-condition is not met (e.g. buffer is full):
  - It calls **`wait()`**: Releases the monitor lock and goes to sleep in the wait-set.
- When another thread changes state (e.g. consumes an item):
  - It calls **`signal()` / `notify()`**: Wakes up a waiting thread to re-acquire the lock and continue.

---

# Summary

- Monitors encapsulate mutual exclusion and shared state into a safe abstraction
- Condition variables allow threads to yield locks and wait for state changes safely
