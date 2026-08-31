# Functional Programming in Java: Lambdas

- Traditionally, Java treated only objects and primitives as first-class citizens.
- **Java 8 introduced Lambda Expressions**: Treating functions as first-class values that can be passed as arguments, stored in variables, and returned from methods.

---

# Lambda Syntax

```text
(parameters) -> { body }
```

```java
// Traditional Anonymous Inner Class:
Collections.sort(names, new Comparator<String>() {
  public int compare(String a, String b) {
    return a.length() - b.length();
  }
});

// Concise Lambda Expression:
Collections.sort(names, (a, b) -> a.length() - b.length());
```

---

# Functional Interfaces (`@FunctionalInterface`)

- An interface with **exactly one abstract method** (SAM):

| Interface | Method Signature | Purpose |
| :--- | :--- | :--- |
| **`Predicate<T>`** | `boolean test(T t)` | Filtering / Condition check |
| **`Function<T, R>`** | `R apply(T t)` | Transforming `T` to `R` |
| **`Consumer<T>`** | `void accept(T t)` | Consuming / Action with no return |
| **`Supplier<T>`** | `T get()` | Factory / Generating a value |

---

# Method References (`Class::method`)

- Even more concise shorthand for lambdas that simply forward arguments:
  ```java
  // Lambda:
  names.forEach(s -> System.out.println(s));

  // Method Reference:
  names.forEach(System.out::println);
  ```

---

# Summary

- Lambdas provide concise functional syntax in Java
- Backed by **Functional Interfaces** with a single abstract method
- Method references (`::`) provide readable syntactic shorthand
