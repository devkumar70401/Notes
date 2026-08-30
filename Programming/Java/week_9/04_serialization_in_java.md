# Object Serialization in Java

- **Serialization**: The process of converting an in-memory Java object graph into a binary byte stream for storage on disk or transmission over a network.
- **Deserialization**: Reconstructing the exact live Java object graph from the binary stream.

---

# The `Serializable` Marker Interface

- To allow serialization, a class must implement the `java.io.Serializable` marker interface (contains no methods):

```java
import java.io.*;

public class UserSession implements Serializable {
  private static final long serialVersionUID = 1L; // Schema version

  private String username;
  private transient String passwordHash; // 'transient' skips serialization!

  public UserSession(String u, String p) {
    this.username = u;
    this.passwordHash = p;
  }
}
```

---

# The `transient` Keyword & `serialVersionUID`

- **`transient`**: Marks sensitive or non-serializable fields (passwords, database connections, thread references) that must **not** be saved to the stream.
- **`serialVersionUID`**: A version identifier for the class schema. If modified between serialization and deserialization, prevents loading corrupted/incompatible objects (`InvalidClassException`).

---

# Reading & Writing Objects

```java
// Saving an object (Serialization)
try (ObjectOutputStream out = new ObjectOutputStream(new FileOutputStream("session.dat"))) {
  out.writeObject(new UserSession("alice", "secret123"));
}

// Loading an object (Deserialization)
try (ObjectInputStream in = new ObjectInputStream(new FileInputStream("session.dat"))) {
  UserSession session = (UserSession) in.readObject();
}
```

---

# Summary

- Serialization persists entire object graphs to byte streams
- Implement `Serializable` and declare explicit `serialVersionUID`
- Use `transient` to protect sensitive or transient state
