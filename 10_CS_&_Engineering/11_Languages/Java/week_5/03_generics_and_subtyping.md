# Invariance of Generics

- If `Manager` is a subclass of `Employee`, is `List<Manager>` a subtype of `List<Employee>`?
- **NO! Generics are invariant.**

### Why `List<Manager>` cannot extend `List<Employee>`:

```java
List<Manager> managers = new ArrayList<>();

// If this were legal:
List<Employee> employees = managers; // Hypothetical!

// Then someone could write:
employees.add(new Employee("Intern", 20000.0)); // Adding normal employee to manager list!

// Now managers.get(0) returns a plain Employee when expecting a Manager -> Crash!
```

---

# Wildcards in Java

Java provides **Wildcards (`?`)** to restore safe subtyping relationships:

### 1. Upper Bounded Wildcard (`? extends T`) — Covariance
- Accepts `T` or any subclass of `T`
- **Read-Only**: Safe to read items as `T`, but **cannot add** new items (except `null`):
  ```java
  public double sumOfSalaries(List<? extends Employee> list) {
    double sum = 0;
    for (Employee e : list) {
      sum += e.getSalary(); // Safe to read as Employee
    }
    return sum;
  }
  ```

### 2. Lower Bounded Wildcard (`? super T`) — Contravariance
- Accepts `T` or any superclass of `T`
- **Write-Safe**: Safe to add items of type `T`:
  ```java
  public void addManagers(List<? super Manager> list) {
    list.add(new Manager("Bob", 80000.0, "Eve")); // Safe to write Manager
  }
  ```

---

# The PECS Rule

> **PECS**: **P**roducer **E**xtends, **C**onsumer **S**uper

- If your method **reads/produces** data from a parameter collection: use `? extends T`
- If your method **writes/consumes** data into a parameter collection: use `? super T`

---

# Summary

- Generics are invariant by default to preserve type safety
- `List<? extends T>` allows reading from a collection of subtypes
- `List<? super T>` allows writing into a collection of supertypes
- Apply the **PECS** rule for clean, flexible API design
