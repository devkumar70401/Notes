# Object Cloning in Java

- Assigning reference variables copies only the pointer, not the object state (`p2 = p1`).
- To create an independent duplicate of an object, Java provides `Object.clone()`.

---

# Shallow Copy vs Deep Copy

```text
Shallow Copy:
Original ----> [ Object A: salary, Date Ref ] ----> [ Date Object: 2026 ]
                      ^
Clone -------> [ Object B: salary, Date Ref ] ----+ (Shares same Date!)

Deep Copy:
Original ----> [ Object A: salary, Date Ref1 ] ----> [ Date Object: 2026 ]
Clone -------> [ Object B: salary, Date Ref2 ] ----> [ New Date Object: 2026 ]
```

- **Shallow Copy**: Copies primitive fields directly, but reference fields point to the *same* shared nested objects.
- **Deep Copy**: Recursively creates new copies of all nested reference objects.

---

# Implementing `Cloneable`

- To use `clone()`, a class must implement the **`Cloneable`** marker interface:

```java
public class Employee implements Cloneable {
  private String name;
  private Date hireDate;

  // Deep copy implementation
  @Override
  public Employee clone() throws CloneNotSupportedException {
    Employee cloned = (Employee) super.clone(); // Shallow copy
    cloned.hireDate = (Date) this.hireDate.clone(); // Deep copy mutable field
    return cloned;
  }
}
```

> **Modern Alternative**: Use **Copy Constructors** (`public Employee(Employee other)`) instead of `clone()` to avoid tricky Cloneable pitfalls.

---

# Summary

- `Object.clone()` performs a shallow copy by default
- Deep copies require explicit cloning of mutable nested objects
- Copy constructors are widely favored in modern Java over `Cloneable`
