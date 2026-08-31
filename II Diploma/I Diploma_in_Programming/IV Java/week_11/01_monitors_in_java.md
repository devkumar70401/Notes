# Java's Built-In Monitor Mechanism

- In Java, **every single object** has an intrinsic monitor lock (often called a *mutex* or *monitor*).
- Java implements monitors using the **`synchronized`** keyword.

---

# 1. Synchronized Methods

```java
public class SynchronizedCounter {
  private int count = 0;

  // Acquires 'this' object's intrinsic lock before entering
  public synchronized void increment() {
    count++;
  } // Automatically releases lock upon return or exception

  public synchronized int getCount() {
    return count;
  }
}
```

---

# 2. Synchronized Blocks

- Lock only the critical section rather than the entire method for better throughput:

```java
public void updateData(Object item) {
  // Unsynchronized prep work...
  
  synchronized(this) {
    // Critical Section: Only one thread here at a time
    sharedList.add(item);
  }
}
```

---

# 3. Inter-Thread Communication: `wait()`, `notify()`, `notifyAll()`

- Defined directly on `java.lang.Object`:
  - `wait()`: Releases object lock and sleeps until notified.
  - `notify()`: Wakes up one arbitrary thread from the wait set.
  - `notifyAll()`: Wakes up all waiting threads.

> **Golden Rule**: Always call `wait()` inside a **`while` loop**, never an `if` statement (to handle spurious wakeups)!

```java
synchronized(lock) {
  while (!conditionMet()) {
    lock.wait(); // Releases lock, re-acquires upon wake up
  }
  // Safe to proceed
}
```

---

# Summary

- Every Java object has an intrinsic monitor lock accessed via `synchronized`
- `wait()` and `notifyAll()` enable coordinated multi-threaded signaling
- Always evaluate waiting conditions inside a `while` loop
