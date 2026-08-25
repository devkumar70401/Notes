# Algorithms + Data Structures = Programs

- Title of Niklaus Wirth's famous introduction to Pascal
- Traditionally, algorithms come first
- **Structured programming**:
  - Design a set of procedures for specific tasks
  - Top-down functional decomposition
  - Combine them to build complex systems
  - Data structures are secondary, designed to serve the algorithms
- Works well for small to medium scale procedural tasks

---

# The Shift to Object-Oriented Design

- In large software systems, data outlives algorithms
- When algorithms change, structured programs require widespread rewrites
- **Object-Oriented Programming (OOP)** flips the perspective:
  - Focus first on the entities (Data + Behavior)
  - Organize systems around cooperating objects rather than global procedural flows
- A natural way to model real-world domains:
  - E-commerce system: `Item`, `Order`, `Payment`, `Account`
  - Graphics system: `Shape`, `Circle`, `Canvas`, `Renderer`

---

# Identifying Objects and Methods

- **Nouns vs Verbs Rule**:
  - **Nouns** signify **Objects / Classes** (Entities that hold state)
  - **Verbs** denote **Methods / Operations** (Actions performed on or by objects)
- Real-world E-commerce workflow:
  - `Items` are added to `Orders`
  - `Orders` are shipped or cancelled
  - `Payments` are accepted or rejected
  - `Accounts` hold customer credit and history
- Associate with each `Order`, a method to add an `Item`:

```java
public class Order {
  private List<Item> items;
  private OrderStatus status;

  public void addItem(Item item) {
    // Add item to order
  }

  public void shipOrder() {
    // Process shipping
  }

  public void cancelOrder() {
    // Cancel order
  }
}
```

---

# The Three Core Pillars of an Object

An object is defined by three fundamental properties:

### 1. Behavior
- What methods can operate on the object?
- Defines the public interface and capabilities of the object

### 2. State
- How does the object react when methods are invoked?
- State is stored inside the **instance variables**
- **Encapsulation**: State should not change directly from the outside; it must be updated only through methods

### 3. Identity
- How do we distinguish between different objects of the same class?
- Two distinct objects can have the exact same state (e.g., two separate orders containing the identical item at the identical price), but they are distinct instances with unique identities (memory locations)

---

# Interaction Between State and Behavior

- State and behavior are tightly coupled:
  - An object's current state directly governs its legal behavior
  - An invoked method alters the internal state of the object

```java
public class Order {
  private OrderStatus status; // PENDING, SHIPPED, CANCELLED
  private List<Item> items;

  public void addItem(Item item) {
    // Cannot add an item to an order that has already been shipped!
    if (this.status == OrderStatus.SHIPPED) {
      throw new IllegalStateException("Cannot add items to a shipped order.");
    }
    items.add(item);
  }

  public void shipOrder() {
    // Cannot ship an empty order!
    if (items.isEmpty()) {
      throw new IllegalStateException("Cannot ship an empty order.");
    }
    this.status = OrderStatus.SHIPPED;
  }
}
```

---

# Relationships Between Classes

In a well-designed OO system, classes interact via three main relationships:

### 1. Dependence ("Uses-A")
- A class depends on another if it manipulates objects of that class
- Example: `Order` needs `Account` to check credit balance
- `Item` does not depend on `Account`
- **Design Goal**: Minimize unnecessary dependencies to achieve **low coupling**

### 2. Aggregation ("Has-A")
- An object contains one or more objects of another class as instance variables
- Example: An `Order` contains `Item` objects and a `Customer` object

### 3. Inheritance ("Is-A")
- One class is a specialized version of another class
- Example: `ExpressOrder` inherits from `Order`
  - Reuses base order state and behavior
  - Adds specialized behavior (priority dispatch, extra shipping fee calculation)

---

# Summary

- Object-oriented programming shifts focus from procedural algorithm decomposition to domain object modeling
- **Nouns** map to objects; **verbs** map to methods
- Every object is characterized by **State**, **Behavior**, and **Identity**
- State dictates valid behavior, and behavior modifies state (protected via **Encapsulation**)
- Three primary relationships connect classes:
  - **Dependence** (Coupling — keep it minimal)
  - **Aggregation** (Composition / Has-A)
  - **Inheritance** (Specialization / Is-A)
