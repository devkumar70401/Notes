# Local Variable Type Inference (`var`)

- Introduced in Java 10 to reduce repetitive boilerplate
- Allows the compiler to **infer the type** of a local variable from its initialization expression at compile-time.

```java
// Traditional Java:
Map<String, List<Employee>> departmentStaff = new HashMap<String, List<Employee>>();

// With Type Inference (var):
var departmentStaff = new HashMap<String, List<Employee>>();
var count = 42;          // Inferred as int
var message = "Hello";   // Inferred as String
```

---

# What `var` IS and IS NOT

- **`var` is STILL statically typed**: Type is fixed at compile-time; cannot assign an integer to `message` later!
- **`var` is NOT `any` or dynamic typing** (unlike Python or JavaScript).

### Restrictions on `var`:
- Only permitted for **local variables inside methods with initializers**
- Cannot be used for:
  - Class instance variables / fields
  - Method parameters or return types
  - Uninitialized variables (`var x;` is illegal)
  - Null initialization (`var x = null;` is illegal)

---

# Summary

- `var` reduces visual clutter while maintaining full static compile-time type safety
- Restricted strictly to initialized local variables within method bodies
