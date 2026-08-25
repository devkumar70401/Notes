# Dealing with Errors in Software

- Software systems inevitably encounter errors:
  - **User Errors**: Invalid input, file not found
  - **System Errors**: Network timeout, out of disk space, database connection lost
  - **Programmer Bugs**: Null pointer dereference, array index out of bounds

---

# Traditional Error Handling vs Exceptions

### Traditional Approach (Return Codes / Flags):
```c
int fd = open("data.txt");
if (fd == -1) {
  // Handle error immediately
}
```
- **Flaws**:
  - Clutters normal business logic with error checks
  - Callers frequently ignore return codes
  - Cannot easily propagate errors across deep call stacks

### Object-Oriented Approach (Exception Handling):
- Separate error handling code from normal execution path
- Automatically propagate errors up the call stack until a matching handler is found
- Group and differentiate error categories using an inheritance hierarchy.

---

# Summary

- Defensive programming anticipates and handles errors gracefully
- Exceptions separate normal logic from failure handling and enforce error handling policies
