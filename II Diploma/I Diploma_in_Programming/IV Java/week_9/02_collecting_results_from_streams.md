# Collecting Stream Results

- Terminal operations often need to accumulate stream elements into data structures or summary metrics.
- The **`collect()`** method accepts a **`Collector`** (provided by `java.util.stream.Collectors`).

---

# Common Collectors

### 1. Accumulating into Collections:
```java
List<String> list = stream.collect(Collectors.toList());
Set<String> set = stream.collect(Collectors.toSet());
```

### 2. Joining Strings:
```java
String csv = stream.collect(Collectors.joining(", ", "[", "]"));
// Produces: "[Apple, Banana, Orange]"
```

### 3. Grouping and Partitioning:
```java
List<Employee> staff = getStaff();

// Group employees by department:
Map<String, List<Employee>> byDept = staff.stream()
    .collect(Collectors.groupingBy(Employee::getDepartment));

// Partition into high-earners and normal:
Map<Boolean, List<Employee>> partitioned = staff.stream()
    .collect(Collectors.partitioningBy(e -> e.getSalary() > 100000));
```

### 4. Downstream Reductions:
```java
// Count employees per department
Map<String, Long> countByDept = staff.stream()
    .collect(Collectors.groupingBy(Employee::getDepartment, Collectors.counting()));
```

---

# Summary

- `Collectors` provides powerful accumulation, grouping, and aggregation primitives
- `groupingBy` partitions data into complex hierarchical map structures in a single pipeline
