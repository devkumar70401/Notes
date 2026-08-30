# Modern Java Concurrency (`java.util.concurrent`)

- Java 5 introduced the high-performance `java.util.concurrent` (JUC) package.

---

# 1. Concurrent Collections

| Legacy Synchronized (Coarse Locks) | Modern Concurrent (Lock-Free / Striped) |
| :--- | :--- |
| `Vector` / `Hashtable` | **`ConcurrentHashMap<K, V>`** (Lock striping, non-blocking reads) |
| `Collections.synchronizedList()` | **`CopyOnWriteArrayList<E>`** (Immutable snapshots for read-heavy workloads) |
| Manual `wait()`/`notify()` queues | **`ArrayBlockingQueue<E>`** / **`LinkedBlockingQueue<E>`** |

---

# 2. Atomic Variables (`java.util.concurrent.atomic`)

- Lock-free, hardware-accelerated thread-safe primitives using CAS instructions:

```java
import java.util.concurrent.atomic.AtomicInteger;

public class HighThroughputCounter {
  private final AtomicInteger count = new AtomicInteger(0);

  public void increment() {
    count.incrementAndGet(); // Atomic CAS operation, zero lock overhead!
  }

  public int get() {
    return count.get();
  }
}
```

---

# 3. Explicit Locks (`ReentrantLock`)

- Provides advanced locking capabilities not possible with `synchronized`:
  - `tryLock(timeout)`: Attempt to acquire lock without blocking forever.
  - Fair locking policies.
  - Multiple independent condition variables per lock.

---

# Summary

- Replace manual synchronization with modern JUC utilities (`ConcurrentHashMap`, `BlockingQueue`)
- Use `AtomicInteger`/`AtomicLong` for high-throughput counters without lock contention
