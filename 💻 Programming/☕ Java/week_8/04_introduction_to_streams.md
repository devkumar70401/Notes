# Introduction to Java Streams API

- A **Stream** is a sequence of elements supporting sequential and parallel aggregate operations.
- Shifts programming from **imperative** ("how to loop and mutate") to **declarative** ("what transformations to perform").

---

# The 3-Stage Stream Pipeline

```mermaid
graph LR
    SRC["List&lt;Employee&gt;<br>(Data Source)"] -->|stream()| F1["filter(e -> isManager)"]
    F1 --> F2["filter(e -> salary > 80k)"]
    F2 --> M1["map(Employee::getName)"]
    M1 --> S1["sorted()"]
    S1 -->|collect(toList)| RES["List&lt;String&gt;<br>(Final Result)"]
    
    style SRC fill:#3b82f6,stroke:#fff,color:#fff
    style RES fill:#10b981,stroke:#fff,color:#fff
```


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
