# The Java Reflection API

- **Reflection**: The capability of a running Java program to inspect and manipulate its own classes, methods, fields, and constructors dynamically at runtime.

---

# The `Class<T>` Object

- For every class loaded into memory, the JVM maintains a unique instance of `java.lang.Class`:

```java
// Three ways to obtain a Class object:
Class<?> c1 = Employee.class;
Class<?> c2 = e.getClass();
Class<?> c3 = Class.forName("com.example.Employee");
```

---

# Inspecting Class Metadata

```java
import java.lang.reflect.*;

public class Inspector {
  public static void inspect(Object obj) {
    Class<?> clazz = obj.getClass();
    System.out.println("Class Name: " + clazz.getName());

    // Print all declared methods
    Method[] methods = clazz.getDeclaredMethods();
    for (Method m : methods) {
      System.out.println("Method: " + m.getName() + " Return Type: " + m.getReturnType());
    }

    // Print all fields
    Field[] fields = clazz.getDeclaredFields();
    for (Field f : fields) {
      System.out.println("Field: " + f.getName() + " Type: " + f.getType());
    }
  }
}
```

---

# Trade-Offs of Reflection

- **Benefits**: Essential for frameworks (Spring, JUnit, ORM libraries, JSON serializers) that need to discover annotations and instantiate objects dynamically.
- **Costs**:
  1. Performance overhead (bypasses JIT optimizations)
  2. Bypasses compile-time type safety
  3. Can break encapsulation (`setAccessible(true)` can access private fields)

---

# Summary

- Reflection allows runtime introspection of class structures, methods, and annotations
- Fundamental to modern frameworks, dependency injection, and testing tools
- Should be used judiciously due to performance and safety trade-offs
