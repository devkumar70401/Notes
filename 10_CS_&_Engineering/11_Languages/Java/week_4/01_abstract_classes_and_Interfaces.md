# Grouping together classes

- Sometimes we collect together classes under a common heading 
- Classes `Circle`, `Square` and `Rectangle` are all shapes
- Create a class `Shape` so that `Circle`, `Square`, `Rectangle` extend `Shape`
- We want to force every `Shape` to define a function `public double perimeter()`
- Could define a function in `Shape` that returns an absurd value `public double perimeter() { return (-1.0); } `
- Rely on the subclass to redefine this function
- What if this doesn't happen?
  - Should not depend on programmer discipline

# Abstract Classes

A better solution

- Provides an *abstract definition* in `Shape`
`public abstract double perimeter();`
- Forces subclasses to provide a concrete implementation
- Cannot create objects from a class that has abstract functions
- `shape` must itself be declared to be `abstract`

```java
public abstract class Shape 
{
  ...
  public abstract double perimeter();
  ...
}
```

- `abstract` here implies whichever class inherits this class must have this function or any function defined as abstract inside superclass.
- If there is even one method in the class then class needs to be an abstract class.
- Can still declare variables whose type is an abstract class

```java
Shape shapearr[] = new Shape[3];
double sizearr[] = new double[3];

shapearr[0] = new Circle(...);
shapearr[1] = new Square(...);
shapearr[2] = new Rectangle(...);

for(i = 0; i < 2; i++)
{
  sizearr[i] = shapearr[i].perimeter();
  // each shapearr[i] calls the appropriate method
  ...
}
```

- If even Circle has abstract perimeter then we cannot work like this then we have to make another class or subclass to make it work.
- Use abstract classes to specify generic properties
- Abstract method signature must be same across all same name methods inside all subclasses 

# Generic functions

```java
public abstract class Comparable
{
  public abstract int cmp(Comparable s);
  // return -1 if this < s,
  //         0 if this == s,
  //         +1 if this > s
}
```

- Now we can sort any array of objects that extend Comparable

```java
public class SortFunctions
{
  public static void quicksort(Comparable[] a)
  {
    ...
    //usual coode for quicksort, except that 
    // to compare a[i] and a[j] we use a[i].cmp(a[j])
  }
}
```

- To use this definition of `quicksort`, we write

```java
public class Myclass extends Comparable
{
  private double size;  // quantity used for comparison

  public int cmp(Comparable s)
  {
    if (s instanceof Myclass)
    {
      // compare this.size  and ((Myclass) s).size
      // Note the cast to access s.size
    }
  }
}
```
# Multiple Inheritance

- Can we sort `Circle` objects using the generic functions in `SortFunctions`?
  - `Circle` already extends `Shape` 
  - Java does not alow `Circle` to also extend `Comparable`!
- An `interface` is an abstract class with no concrete components

```java
public interface Comparable
{
  public abstract int cmp(Comparable s);
}
```

- A class that extends an interfaces said to implement it:

```java
public class Circle extends Shape implements Comprable {
  public double perimeter() {
    ...
  }
  public int cmp(Comparable s) {
    ...
  }
}
```

- Can extend only one class, but can implement multiple interfaces 

# Summary

- We can use the class hierarchy  to group together related classes
- An abstract method in a parent class forces each subclass to implements it in a sensible manner
- Any class with an abstract method is itself abstract
  - Cannot create objects corresponding to an abstract class
  - However, we can define variables whose type is an abstract class
- Abstract classes can also describe capabilities, allowing for generic functions
- An interface is an abstract class with no concrete components
  - A class to extend only one parent class, but it can implement any number of interfaces




