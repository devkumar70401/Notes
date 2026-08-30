# Assertions in Java

- An **assertion** is a statement that verifies an internal invariant that the programmer believes to be unconditionally true.

```java
assert condition : "Error message if condition is false";
```

```java
public void setPercent(double p) {
  assert p >= 0.0 && p <= 100.0 : "Invalid percentage: " + p;
  this.percentage = p;
}
```

---

# Enabling Assertions

- By default, the JVM disables assertions at runtime for performance
- Enable them during testing/development using the **`-ea`** flag:
  ```bash
  java -ea MyApp
  ```

---

# Assertions vs Exceptions

- **Use Assertions**: For internal sanity checks, pre-conditions of private methods, and post-conditions (verifying code correctness during development).
- **Use Exceptions**: For validating public API parameters, user inputs, and runtime environmental failures.

---

# Summary

- Assertions document and verify developer assumptions during testing
- Disabled in production by default; enabled with `-ea`
- Do not use assertions in place of proper public exception handling
