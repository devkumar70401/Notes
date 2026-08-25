# The Billion Dollar Mistake: `null`

> *"I call it my billion-dollar mistake. It was the invention of the null reference in 1965."* — Sir Tony Hoare

- Returning `null` when a value is absent leads to ubiquitous `NullPointerException` (NPE) bugs.
- **Java 8 Solution**: **`Optional<T>`** — a container object which may or may not contain a non-null value.

---

# Working with `Optional<T>`

### 1. Creating Optionals:
```java
Optional<String> opt1 = Optional.of("Hello");      // Non-null value
Optional<String> opt2 = Optional.ofNullable(val);  // Safe if val might be null
Optional<String> opt3 = Optional.empty();          // Explicitly empty
```

### 2. Functional Value Extraction:
```java
// Avoid get() without checking isPresent()!
// Instead, use functional style:

String result = opt.orElse("Default Value");
String computed = opt.orElseGet(() -> computeFallback());
String required = opt.orElseThrow(() -> new IllegalArgumentException("Missing value"));

// Execute action only if value exists
opt.ifPresent(v -> System.out.println("Found: " + v));
```

### 3. Transforming Optionals:
```java
Optional<Integer> length = opt.map(String::length);
```

---

# Summary

- `Optional<T>` explicitly signals that a method return value may be absent
- Eliminates defensive `if (x != null)` clutter
- Use functional methods (`orElse`, `map`, `ifPresent`) rather than direct `.get()`
