# Structure of a Java Program

- In Java, all code must reside inside a class definition
- Standard canonical structure:

```java
public class HelloWorld {
  public static void main(String[] args) {
    System.out.println("Hello, World!");
  }
}
```

---

# Deconstructing `main`

- **`public`**: Method is globally accessible so the JVM runtime can invoke it from outside the package.
- **`static`**: Method belongs to the class itself; JVM can call `main` without creating an instance of `HelloWorld`.
- **`void`**: Method does not return any value.
- **`String[] args`**: Array of command-line string arguments passed to the program.

---

# Compilation and Execution Flow

```bash
# 1. Compile source (.java) to bytecode (.class)
javac HelloWorld.java

# 2. Run bytecode on the Java Virtual Machine
java HelloWorld
```

- If `HelloWorld.java` contains `public class HelloWorld`, the file name **must exactly match** the public class name (`HelloWorld.java`).

---

# Summary

- Every Java application requires a `public static void main(String[] args)` entry point
- File names must match public class names
- `javac` compiles source code into portable JVM bytecode (`.class`)
