# Event Handling in Swing

- Swing uses the **Observer Pattern** (Listener Model) to wire user actions to code execution.

---

# Handling Button Clicks: `ActionListener`

```java
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class SimpleClickCounter extends JFrame {
  private int count = 0;
  private final JLabel label;
  private final JButton button;

  public SimpleClickCounter() {
    setTitle("Click Counter");
    setSize(300, 150);
    setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    setLayout(new FlowLayout());

    label = new JLabel("Clicks: 0");
    button = new JButton("Click Me!");

    // Modern Lambda Event Listener:
    button.addActionListener(e -> {
      count++;
      label.setText("Clicks: " + count);
    });

    add(label);
    add(button);
  }

  public static void main(String[] args) {
    // Run UI initialization on Event Dispatch Thread
    SwingUtilities.invokeLater(() -> {
      new SimpleClickCounter().setVisible(true);
    });
  }
}
```

---

# Evolution of Event Handlers in Java

```java
// 1. Classic Anonymous Inner Class (Java 1.1 - 7):
button.addActionListener(new ActionListener() {
  public void actionPerformed(ActionEvent e) {
    System.out.println("Clicked!");
  }
});

// 2. Modern Lambda Expression (Java 8+):
button.addActionListener(e -> System.out.println("Clicked!"));
```

---

# Summary

- Register event listeners using `.addActionListener()`
- Lambdas provide clean, single-line event handling callbacks in modern Swing
- Always instantiate Swing UIs on the Event Dispatch Thread via `SwingUtilities.invokeLater()`
