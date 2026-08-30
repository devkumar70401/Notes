# Array Creation

## Introduction

There are 6 general methods to create arrays

1. From Python structures(i.e. lists and tuples)
2. From Numpy intrinsic methods (e.g. arange, ones, like, etc.)
3. Replicating, joining, or mutating existing arrays
4. Reading arrays from disk, either from standard or custom formats
5. Creating arrays from raw bytes through the use of strings or buffers.
6. Use of special library functions(e.g. random)

```python
import numpy as np
```

---

## 1) Converting Python sequences to NumPy arrays

- a list of numbers will create a 1D array,
- a list of lists will create a 2D array,
- further nested lists will create higher-dimensional arrays. In general, any array object is called an **ndarray** in NumPy.

```python
a1D = np.array([1, 2, 3, 4])

a2D = np.array([[1, 2], 
                [3, 4]])

a3D = np.array([[[1, 2], 
                 [3, 4]], 
                
                [[5, 6], 
                 [7, 8]]])

a1D, a2D, a3D
```

**Output:**
```text
(array([1, 2, 3, 4]),
 array([[1, 2],
        [3, 4]]),
 array([[[1, 2],
         [3, 4]],
 
        [[5, 6],
         [7, 8]]]))
```

```python
%%script ipython

import numpy as np
np.array([127, 128, 129], dtype=np.int8)
```

**Output:**
```text
Python 3.14.4 (main, Jun 18 2026, 14:25:02) [GCC 15.2.0]
Type 'copyright', 'credits' or 'license' for more information
IPython 9.15.0 -- An enhanced Interactive Python. Type '?' for help.
Tip: You can use Ctrl-O to force a new line in terminal IPython

In [1]: 
In [1]: 
In [2]: ---------------------------------------------------------------------------
OverflowError                             Traceback (most recent call last)
Cell In[2], line 1
----> 1 np.array([127, 128, 129], dtype=np.int8)

OverflowError: Python integer 128 out of bounds for int8

In [3]: Do you really want to exit ([y]/n)?
```

```python
a = np.array([2, 3, 4], dtype=np.uint32)
b = np.array([5, 6, 7], dtype=np.uint32)
c_unsigned32 = a - b
print('unsigned c:', c_unsigned32, c_unsigned32.dtype)
c_signed32 = a - b.astype(np.int32)
print('signed c:', c_signed32, c_signed32.dtype)
```

**Output:**
```text
unsigned c: [4294967293 4294967293 4294967293] uint32
signed c: [-3 -3 -3] int64
```

NOTE:
- when you perform operations with two arrays of the same dtype: uint32, the resulting array is the same type.
- When you perform operations with different dtype, NumPy will assign a new type that satisfies all of the array elements involved in the computation, here uint32 and int32 can both be represented in as int64.

> NOTE:
> - Be aware of Datatype mismatch.
> - Recommended to specify data type explicitly

---

## 2) Intrinsic Numpy array creation functions

- Numpy has over 40 built in functions for array creation.
- following major types
  - 1D arrays
  - 2d arrays
  - ndarrays

### 1D array creation functions
