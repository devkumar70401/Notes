# Interfaces 

- An interface is a purely abstract class
  - All methods are abstract
- A class **implements** an interface
  - Provide concrete code for each abstract function
- Classes can implement multiple interfaces
  - Abstract functions, so no contradictory inheritance 
- Interfaces describe relevant aspects of a class 
  - Abstract functions describe a specific "slice" of capabilities 
  - Another class only needs to know about these capabilities 

# Exposing limited capabilities
- Generic `quicksort` for any datatype that supports comparisons
- Express this capability by making the arguments type `Comparable[]`
  - Only information that `quicksort` needs about the underlying type
  - All other aspects are irrelevant 

```Java
public class SortFunctions {
    public static void quicksort(Comparable[] a) {
        ...
        // Usual code for quicksort, except that 
        // to compare a[i] and a[j] we use 
        // a[i].cmp(a[j])
    }
} 
```

- Describe the relevant functions supported by `Comparable` objects through an interface 

```java
public interface Comparable {
    public abstract int cmp(Comparable s);
    // return -1 if this < s,
    //         0 if this == s,
    //        -1 if this < s
}
```

- However, we cannot express the intended behavior of cmp explicitly

# Adding methods to interfaces

- Java interfaces extended to allow functions to be added
- Interface cannot be created as an object 
- Static functions
  - Cannot access instance variables
  - Invoke directly or using interface name: `Comparable.cmpdoc()`
- In an interface, we can define a static function 

```java
public interface Comparable{
    public static string cmpdoc(){
        String s;
        s = "Return -1 if this < s, ";
        s = s + " 0 if this == s, ";
        s = s + "+1 if this > s. ";
        return (s);
    }
}
```

- Default functions
  - Provide a default implementation for some functions
  - Class can override these
  - Invoke like normal method, using object name: `a[i].cmp(a[j])`

```java
public interface Comparable{
    public default int cmp(Comparable s) {
        return (0);
    }
}
```

# Dealing with conflicts

- Old problem of multiple inheritance returns
  - Conflict between static/default methods

```java
public interface Person{
    public default String getName() {
        return("No Name");
    }
}

public interface Designation{
    public default String getName() {
        return ("No Designation");
    }
}

public class Employee implements Person, Designation {
    ...
}
```

- Subclass `must` provide a fresh implementation 

```java
public class Employee implements Person, Designation {
    ...

    public String getName() {
        ...
    }
}
```

- Conflict could be between a class and an interface 
  - `Employee` inherits from class `Person` and implements `Designation`
  - Method inherited from the class "wins"
  - Motivated  by reverse compatibility

```java
public class Employee extends Person implements Designation {
    ...
}
```

# Summary
****
- Interface express abstract capabilities
  - Capabilities are expressed in terms of methods that must be present
  - Cannot specify the intended behaviour of these functions 
- Java later allowed concrete functions to be added to interfaces 
  - Static functions -- cannot access instance variables 
  - Default functions -- may be overridden
- Reintroduces conflicts in multiple inheritance 
  - Subclass must resolve the conflict between superclass and interface 
  - Special "class wins" rule for conflict between superclass and interface 
- Pitfalls of extending a language and maintaining compatibility
