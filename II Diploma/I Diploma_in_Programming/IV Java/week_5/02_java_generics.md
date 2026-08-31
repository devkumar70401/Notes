# Why Generics?

- Prior to Java 5, collections stored raw `Object` references:

```java
// Pre-Generics (Legacy Java)
ArrayList list = new ArrayList();
list.add("Hello");
list.add(100); // Unintended integer added!

// Requires explicit downcasting
String s = (String) list.get(1); // Runtime ClassCastException crash!
```

- **Problems with Raw Objects**:
  1. Loss of type information
  2. Cumbersome explicit casting
  3. Errors discoverable only at runtime instead of compile-time

---

# Defining Generic Classes

- Introduce type parameters using angle brackets `<T>`:

```java
public class Box<T> {
  private T value;

  public void set(T val) { this.value = val; }
  public T get() { return this.value; }
}
```

```java
// Usage: Compile-time type enforcement
Box<String> stringBox = new Box<>();
stringBox.set("Hello");
String str = stringBox.get(); // No cast needed!

// stringBox.set(123); // Compilation Error caught immediately!
```

---

# Generic Methods

- Methods can declare their own independent type parameters:

```java
public class ArrayUtils {
  public static <T> void swap(T[] arr, int i, int j) {
    T temp = arr[i];
    arr[i] = arr[j];
    arr[j] = temp;
  }
}
```

---

# Summary

- Generics enable compile-time type safety and eliminate manual downcasting
- Type parameters (`<T, E, K, V>`) parameterize classes, interfaces, and methods
- Catches type mismatch errors at compile-time rather than runtime
