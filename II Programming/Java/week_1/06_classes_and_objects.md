# Classes vs Objects

```mermaid
graph TD
    CLASS["Class Blueprint: Point<br>- x: double<br>- y: double<br>+ distance(other)"]
    
    CLASS -->|new Point(3, 4)| OBJ1["Heap Object 1 (0x1A)<br>x = 3.0<br>y = 4.0"]
    CLASS -->|new Point(7, 1)| OBJ2["Heap Object 2 (0x2B)<br>x = 7.0<br>y = 1.0"]

    P1["Ref: p1 (0x1A)"] --> OBJ1
    P2["Ref: p2 (0x1A)"] --> OBJ1
    P3["Ref: p3 (0x2B)"] --> OBJ2
```


- **Class**: A blueprint, template, or user-defined data type describing what attributes and behaviors instances will possess.
- **Object**: A concrete instance of a class allocated in memory at runtime.

```text
Class (Blueprint):
  Car { color, speed, drive(), brake() }

Objects (Instances in Heap):
  car1 -> { color: "Red", speed: 60 }
  car2 -> { color: "Blue", speed: 0 }
```

---

# Anatomy of a Java Class

```java
public class Point {
  // 1. Instance Variables (State)
  private double x;
  private double y;

  // 2. Constructor (Initialization)
  public Point(double x, double y) {
    this.x = x; // 'this' disambiguates instance variable from parameter
    this.y = y;
  }

  // 3. Methods (Behavior)
  public double distance(Point other) {
    double dx = this.x - other.x;
    double dy = this.y - other.y;
    return Math.sqrt(dx * dx + dy * dy);
  }

  public double getX() { return x; }
  public double getY() { return y; }
}
```

---

# Object Instantiation & References

```java
Point p1 = new Point(3.0, 4.0);
Point p2 = p1; // p2 copies the reference (memory address), NOT the object!
```

```text
Stack                  Heap
+-------+             +----------------------+
|  p1   | ----------> | Point Object         |
+-------+             |   x: 3.0, y: 4.0     |
|  p2   | ----------> |                      |
+-------+             +----------------------+
```

- Modifying state through `p2` directly affects the object observed by `p1`.

---

# Summary

- A **Class** defines the schema and behavior; an **Object** is a concrete instance residing in the Heap
- Constructors initialize newly instantiated objects
- Variable assignment for reference types copies the pointer, not the underlying object
