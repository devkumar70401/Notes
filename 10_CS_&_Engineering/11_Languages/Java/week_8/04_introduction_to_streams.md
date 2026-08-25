# Introduction to Java Streams API

- A **Stream** is a sequence of elements supporting sequential and parallel aggregate operations.
- Shifts programming from **imperative** ("how to loop and mutate") to **declarative** ("what transformations to perform").

---

# The 3-Stage Stream Pipeline

```text
[ Data Source ] ----> [ Intermediate Operations ] ----> [ Terminal Operation ]
(List, Array)           (filter, map, sorted)             (collect, count, sum)
```

1. **Source**: Collection, array, or I/O channel.
2. **Intermediate Operations (Lazy)**: Returns a new Stream; executed only when terminal operation is called (`filter`, `map`, `distinct`, `sorted`, `limit`).
3. **Terminal Operation (Eager)**: Produces a final result or side-effect (`toList()`, `reduce()`, `count()`, `forEach()`).

---

# Declarative Stream Example

```java
List<Employee> staff = getStaff();

// Find names of top 3 highest paid managers sorted alphabetically:
List<String> topManagers = staff.stream()
    .filter(e -> e instanceof Manager)
    .filter(e -> e.getSalary() > 80000)
    .map(Employee::getName)
    .sorted()
    .limit(3)
    .toList();
```

---

# Summary

- Streams provide declarative, composable data pipeline transformations
- Intermediate operations are **lazy** and optimize execution
- Terminal operations trigger pipeline evaluation to produce results
