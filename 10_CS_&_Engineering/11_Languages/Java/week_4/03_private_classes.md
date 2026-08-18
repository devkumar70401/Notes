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

}
```

```java

```