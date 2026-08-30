# Modifiers in Java

- Java provides modifiers to control:
  1. **Visibility & Encapsulation**: `public`, `private`, `protected`, package-private (default)
  2. **Lifecycle & Membership**: `static`
  3. **Immutability & Extensibility**: `final`
- These modifiers apply orthogonally to **classes**, **instance variables**, and **methods**.

---

# 1. `public` vs `private`

- Core rule of encapsulation:
  - **Instance variables** are typically `private` (hidden from direct external access).
  - **Methods** providing the public interface are `public`.

### Do Private Methods Make Sense?
- **Yes!** Private methods act as internal helper functions:
  - Break down complex public methods into manageable sub-tasks
  - Hide implementation details and internal state checks that external callers should never invoke directly.

```java
public class Stack {
  private int[] values;
  private int tos;   // Top of stack
  private int size;

  public void push(int i) {
    if (stack_full()) {
      extend_stack(); // Internal reallocation
    }
    values[tos++] = i;
  }

  // Private helper methods
  private boolean stack_full() {
    return (tos == size);
  }

  private void extend_stack() {
    // Allocate double space, copy values, update size
  }
}
```

---

# Accessor and Mutator Design Pitfalls

- Simply adding a `get` and `set` method for every private variable is a common anti-pattern.
- Example with `Date`:

```java
public class Date {
  private int day, month, year;

  // ⚠️ RISK: Allows inconsistent intermediate states!
  public void setDay(int d) { day = d; }
  public void setMonth(int m) { month = m; }
  public void setYear(int y) { year = y; }
}
```

- If `Date` is `31-01-2026` and the caller calls `setMonth(2)`, the object temporarily enters an invalid state (`31-02-2026`)!
- **Better Design**: Provide atomic mutators that validate the entire state transition together:

```java
public class Date {
  private int day, month, year;

  public void setDate(int d, int m, int y) {
    if (!isValidDate(d, m, y)) {
      throw new IllegalArgumentException("Invalid date combination");
    }
    this.day = d;
    this.month = m;
    this.year = y;
  }
}
```

---

# 2. `static` Components

```mermaid
graph TD
    subgraph Class State: Order (Heap Memory)
        STAT["static lastorderid = 2<br>(Single Shared Counter)"]
    end

    subgraph Instance 1: order1
        O1["orderid = 1"]
    end

    subgraph Instance 2: order2
        O2["orderid = 2"]
    end

    O1 -.->|reads/increments| STAT
    O2 -.->|reads/increments| STAT
```


- A `static` component belongs to the **class itself**, rather than to any specific instance/object.
- Exists in memory even if no objects of the class are ever instantiated.

### Public Static:
- Global constants: `Math.PI`, `Integer.MAX_VALUE`
- Stateless utility functions: `Math.sqrt(x)`, `Arrays.sort(a)`, `main(String[] args)`

### Private Static (Cross-Instance Bookkeeping):
- Shared state among all instances of a class:

```java
public class Order {
  // Shared counter across all Order objects
  private static int lastorderid = 0;

  // Unique per-object instance variable
  private int orderid;

  public Order() {
    lastorderid++;
    this.orderid = lastorderid; // Assigns unique sequential ID
  }

  public int getOrderId() {
    return orderid;
  }
}
```

- ⚠️ *Note*: When multiple threads create `Order` objects concurrently, updates to `lastorderid` require synchronization to avoid race conditions.

---

# 3. `final` Components

- The `final` keyword denotes **immutability** and **non-overridability**:

### Final Variables:
- Value cannot be reassigned once initialized:
  ```java
  public static final double PI = 3.141592653589793;
  ```

### Final Methods:
- A `final` method **cannot be overridden** by any subclass:
  ```java
  public class Account {
    // Critical security check that subclasses must not tamper with
    public final boolean verifyPassword(String input) {
      ...
    }
  }
  ```

### Final Classes:
- A `final` class **cannot be extended** by any subclass:
  ```java
  public final class String { ... }
  ```
- Protects core language/security structures from malicious subclass tampering.

---

# Summary

| Modifier | On Variables | On Methods | On Classes |
| :--- | :--- | :--- | :--- |
| **`private`** | Accessible only within declaring class | Internal helper method | Permitted for nested/inner classes |
| **`public`** | Accessible from anywhere | Part of public API contract | Top-level class accessible anywhere |
| **`static`** | Single copy shared across all instances | Invoked on class name, cannot access instance variables (`this`) | Static nested class |
| **`final`** | Constant (cannot be reassigned) | Cannot be overridden by subclasses | Cannot be extended / subclassed |
