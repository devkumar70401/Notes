# Designing Classes in Java

- A class encapsulates state (instance variables) and methods (behavior)
- Best practice: Keep data `private` and provide validated public accessors/mutators.

```java
public class BankAccount {
  // Encapsulated instance state
  private String accountNumber;
  private double balance;

  // Constructor Overloading
  public BankAccount(String accNo, double initialBalance) {
    this.accountNumber = accNo;
    this.balance = Math.max(0.0, initialBalance);
  }

  public BankAccount(String accNo) {
    this(accNo, 0.0); // Chained constructor call
  }

  // Business Logic
  public boolean deposit(double amount) {
    if (amount > 0) {
      balance += amount;
      return true;
    }
    return false;
  }

  public boolean withdraw(double amount) {
    if (amount > 0 && amount <= balance) {
      balance -= amount;
      return true;
    }
    return false;
  }

  public double getBalance() { return balance; }
}
```

---

# The `this` Keyword

- `this` refers to the **current object instance**:
  1. Resolving shadowing between parameter names and instance variable names (`this.balance = balance;`)
  2. Calling another constructor in the same class (`this(...)`)

---

# Summary

- Classes enforce encapsulation by making fields `private`
- Multiple constructors allow flexible object initialization
- `this` represents the current active object reference
