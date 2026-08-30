# Nested objects

- An instance variable can be user defined type
  - `Employee` uses `Date`
- `Date` is a public class, also available to other classes

```java
public class Employee {
  private String name;
  private double salary;
  private Date joindate;

  ...

}
```

```java
public class Date {
  private int day, month year;
  ...
}
```

- Date is a public class, also available to other classes
- When could a private class make sense?

---

- `LinkedList` is built using `Node`

```java
public class Node {
  public Object data;
  public Node next;
  ...
}
```

```java
public Class LinkedList {
  private int size;
  private Node first;

  public Object head() {
    Object returnval = null;
    if (first != null){
      returnval = first.data;
      first = first.next;
    }
    return (returnval);
  }
}
```

- Why Should `Node` be public?
  - May want to enhance with `prev` field, doubly linked list
  - Does not affect interface of `LinkedList`
- Instead, make `Node` a private class
  - Nested within `LinkedList`
  - Also called an **inner** class

```java
public class LinkedList{
  private int size;
  private Node first;

  public Object head() { ... }

  public void insert(Object newdata){
    ...
  }

  private class Node{
    public Object data;
    public Node next;
  }
}
```

- Objects of private class can see private components of enclosing class

---

# Summary

- An object can have nested objects as instance variables
- In some situations, the structure of these nested objects need not be exposed
- Private classes allow an additional degree of data encapsulation
- Combine private classes with interfaces to provide controlled access to the state of an object

























