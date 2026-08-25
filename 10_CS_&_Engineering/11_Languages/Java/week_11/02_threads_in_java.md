# Creating & Managing Threads in Java

There are two primary ways to define and run a thread in Java:

---

# 1. Implementing `Runnable` (Preferred)

- Decouples task execution from thread management:

```java
public class WorkerTask implements Runnable {
  @Override
  public void run() {
    System.out.println("Running in thread: " + Thread.currentThread().getName());
  }
}

// Execution:
Thread t = new Thread(new WorkerTask());
t.start(); // Spawns new OS thread and invokes run()
```

---

# 2. Extending `Thread`

```java
public class MyThread extends Thread {
  @Override
  public void run() {
    System.out.println("Running...");
  }
}

MyThread t = new MyThread();
t.start();
```

---

# Thread Lifecycle States

```text
NEW ----(start())----> RUNNABLE <========> BLOCKED / WAITING / TIMED_WAITING
                          |
                          v (run() completes)
                      TERMINATED
```

---

# Key Thread Operations

- **`t.start()`**: Spawns the thread and executes `run()`. (Never call `run()` directly, as that runs on the calling thread!).
- **`t.join()`**: The calling thread waits until thread `t` completes execution.
- **`t.interrupt()`**: Signals a thread to stop or wake up from sleep.

---

# Summary

- Prefer implementing `Runnable` or using Lambdas: `new Thread(() -> { ... }).start()`
- Use `join()` for thread synchronization and deterministic completion
