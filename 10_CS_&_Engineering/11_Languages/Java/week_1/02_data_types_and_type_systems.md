# Types in Programming Languages

- A **type** defines:
  1. A set of valid values
  2. A set of valid operations that can be performed on those values
  3. The underlying memory representation (bit-width and encoding)
- Types prevent nonsensical operations at runtime (e.g., dividing a string by a float).

---

# Static vs Dynamic Typing

| Feature | Statically Typed (Java, C++) | Dynamically Typed (Python, JS) |
| :--- | :--- | :--- |
| **Type Checking** | At **Compile-Time** | At **Run-Time** |
| **Variable Declaration** | Explicitly typed (`int x = 10;`) | Inferred/Bound on assignment (`x = 10`) |
| **Error Detection** | Early bug detection before execution | Flexible, but errors surface during execution |
| **Performance** | Faster (no runtime type inspection) | Slower (runtime type lookups) |

---

# Java's Type System: The Two Universes

Java strictly divides types into two distinct categories:

### 1. Primitive Types (Value Types)
- Directly store raw values in memory (on the Stack)
- Fixed size, highly efficient:
  - Integers: `byte` (8-bit), `short` (16-bit), `int` (32-bit), `long` (64-bit)
  - Floating-point: `float` (32-bit), `double` (64-bit)
  - Character: `char` (16-bit Unicode)
  - Boolean: `boolean` (`true` / `false`)

### 2. Reference Types (Pointer Types)
- Variables do **not** store the raw data directly; they store the **memory address (reference)** pointing to an object residing in the **Heap**
- Includes: Classes, Arrays, Interfaces, `String`, Enums.

```java
int a = 42;             // Stored directly as 32-bit value in stack frame
String s = "Hello";     // 's' holds reference (address) pointing to Heap object
int[] arr = new int[5]; // 'arr' holds reference pointing to Heap array
```

---

# Summary

- A type specifies valid values, operations, and memory structure
- Java is **statically typed**: every expression's type is known and verified at compile-time
- Java maintains a clean separation between **Primitive Types** (raw values on Stack) and **Reference Types** (pointers to Heap objects)
