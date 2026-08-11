# ☕ Java Master Knowledge Vault & Interactive Notebooks

Welcome to your Java learning vault! This directory contains structured Jupyter Notebooks (`.ipynb`) featuring executable Java code, theoretical explanations, LaTeX mathematical formulas, and Mermaid architecture diagrams.

---

## 🗺️ Notebook Structure & Taxonomy

| Notebook File | Description | Status |
| :--- | :--- | :--- |
| [`01_Basics_&_OOP.ipynb`](./01_Basics_&_OOP.ipynb) | Variables, Control Flow, Classes, Interfaces, Inheritance, & Polymorphism | 🚀 Ready |
| [`02_Collections_&_Generics.ipynb`](./02_Collections_&_Generics.ipynb) | ArrayList, HashMap, HashSet, Generics, Type Erasure, Streams API | 📝 Planned |
| [`03_Exception_Handling_&_IO.ipynb`](./03_Exception_Handling_&_IO.ipynb) | Checked/Unchecked Exceptions, File I/O, NIO.2, Try-with-resources | 📝 Planned |
| [`04_Multithreading_&_Concurrency.ipynb`](./04_Multithreading_&_Concurrency.ipynb) | Threads, Synchronized, ReentrantLock, ExecutorService, Volatile | 📝 Planned |
| [`05_JVM_Internals_&_GC.md`](./05_JVM_Internals_&_GC.md) | JVM Memory Architecture (Heap vs Stack), Garbage Collection Algorithms | 📝 Planned |

---

## ⚙️ How to Run Java Notebooks in VS Code

1. Install **OpenJDK 17+** and **IJava** kernel on your system:
   ```bash
   sudo apt update && sudo apt install -y openjdk-17-jdk
   pip install jupyterlab notebook
   curl -L https://github.com/SpencerPark/IJava/releases/download/v1.3.0/ijava-1.3.0.zip -o ijava.zip
   unzip ijava.zip
   python3 install.py --sys-prefix
   ```
2. Open any `.ipynb` file in VS Code.
3. Click **Select Kernel** at the top right of VS Code and choose **Java (IJava)**.
4. Execute Java cells directly!
