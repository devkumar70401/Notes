# Three Types of Polymorphism

Polymorphism means "having many forms". In computer science and Java, it manifests in three distinct ways:

```text
                  +-----------------------------------+
                  |           POLYMORPHISM            |
                  +-----------------------------------+
                   /                |                                  /                 |                         1. Ad-Hoc            2. Subtype           3. Parametric
        (Overloading)        (Inheritance)        (Generics)
```

---

# 1. Ad-Hoc Polymorphism (Method Overloading)
- Same function name with different parameter signatures in the same class
- Selection resolved **statically at compile-time** by the compiler based on argument types:
  ```java
  Arrays.sort(int[] a);
  Arrays.sort(double[] a);
  ```

---

# 2. Subtype Polymorphism (Inheritance & Dynamic Dispatch)
- Methods defined in a superclass and overridden in subclasses with identical signatures
- Selection resolved **dynamically at run-time** based on the actual receiver object type:
  ```java
  Shape s = new Circle(5.0);
  s.perimeter(); // Dynamically dispatches to Circle.perimeter()
  ```

---

# 3. Parametric Polymorphism (Generics)
- Code written without regard to any specific data type, using explicit type parameters (`<T>`)
- Allows writing algorithms and data structures that work uniformly across arbitrary types with strict compile-time type checking.

---

# Summary

- **Ad-hoc**: Overloading (compile-time choice based on parameters)
- **Subtype**: Overriding (runtime choice based on dynamic object identity)
- **Parametric**: Generics (type parameters enforcing uniform behavior across types)
