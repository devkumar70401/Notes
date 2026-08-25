# Logging in Java (`java.util.logging`)

- Why avoid `System.out.println` in production?
  1. Cannot be toggled dynamically without code edits
  2. No timestamps, thread IDs, or severity classification
  3. Slow and unbuffered (causes I/O bottlenecks)

---

# Log Levels

Java provides standard hierarchical logging levels:

```text
SEVERE  (Highest severity - critical error)
WARNING (Potential problem)
INFO    (Standard milestone / operational info)
CONFIG  (Configuration details)
FINE    (Debug info)
FINER   (Detailed debug)
FINEST  (Lowest severity - tracing)
```

---

# Standard Logging Setup

```java
import java.util.logging.*;

public class Server {
  private static final Logger logger = Logger.getLogger(Server.class.getName());

  public void start() {
    logger.info("Server is starting on port 8080...");
    try {
      // Connect to database
    } catch (Exception e) {
      logger.log(Level.SEVERE, "Database connection failed", e);
    }
  }
}
```

---

# Summary

- `java.util.logging` provides structured, configurable diagnostics
- Log levels control verbosity across development, staging, and production
- Essential for debugging distributed systems and backend services
