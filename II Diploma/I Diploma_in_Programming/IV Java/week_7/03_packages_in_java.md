# Packages in Java

- A **package** is a namespace mechanism that groups related classes, interfaces, and sub-packages.
- Solves two major engineering problems:
  1. **Name Collisions**: Two different libraries can define `Date` without conflict (`java.util.Date` vs `java.sql.Date`).
  2. **Access Control**: Regulates visibility across architectural layers.

---

# Mapping Packages to Directory Structure

- Package declarations must match the directory hierarchy on disk:
  ```java
  package com.myapp.services;

  public class PaymentService { ... }
  ```
- File must be located at: `com/myapp/services/PaymentService.java`.

---

# The Four Access Levels in Java

| Modifier | Same Class | Same Package | Subclass (Different Pkg) | World (Everywhere) |
| :--- | :---: | :---: | :---: | :---: |
| **`private`** | ✅ | ❌ | ❌ | ❌ |
| **Package-Private (Default)** | ✅ | ✅ | ❌ | ❌ |
| **`protected`** | ✅ | ✅ | ✅ | ❌ |
| **`public`** | ✅ | ✅ | ✅ | ✅ |

---

# Summary

- Packages organize large codebases and prevent name clashes
- Package structure mirrors filesystem directory hierarchy
- Access modifiers enforce encapsulation across package and inheritance boundaries
