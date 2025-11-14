# Space Complexity (Python DSA Notes)

Space Complexity measures **how much extra memory** an algorithm uses relative to the input size.

---

## 🔹 Why Space Complexity Matters?

Even if an algorithm is fast, it might use too much memory and become impractical.  
Space Complexity helps us measure:

- Extra variables used  
- Data structures created  
- Recursion stack space  
- Input size storage  

---

## 🔹 Types of Space Usage

### 1. **Fixed Space (Constant Space)**
Memory that does **not change** with input size.

Examples:
- Primitive variables
- Fixed-size arrays
- Constants

Takes **O(1)** space.

### 2. **Variable Space**
Memory that **changes** depending on input size.

Examples:
- Arrays / lists that grow with input
- Recursion depth
- Dynamic data structures (linked list, tree, graph)

Often **O(n)**, **O(log n)**, etc.

---

## 🔹 Common Space Complexities

### ✔ **O(1) – Constant Space**
Algorithm uses the same amount of memory regardless of input.

Example:
```python
def sum_list(nums):
    total = 0      # constant space
    for num in nums:
        total += num
    return total
```

### ✔ **O(n) – Linear Space**
Memory grows directly with input size.

Example:
```python
def copy_list(nums):
    new_list = nums[:]   # creates new list of size n
    return new_list
```

### ✔ **O(log n) – Logarithmic Space**
Typically comes from **divide & conquer** recursion.

Example:
Binary search recursive calls stack → **O(log n)** space.

### ✔ **O(n²) – Quadratic Space**
Often from 2D arrays, matrices.

Example:
- DP tables  
- Graph adjacency matrices

---

## 🔹 Recursion & Space Complexity

Recursion adds **stack space** equal to the depth of recursion.

Example:
```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
```

Recursion depth = `n` → space = **O(n)**

---

## 🔹 Space Complexity of Common Data Structures

| Data Structure | Space Complexity |
|----------------|------------------|
| Array / List   | O(n) |
| HashMap / Dict | O(n) |
| Set            | O(n) |
| Stack / Queue  | O(n) |
| Tree           | O(n) |
| Graph (Adj List) | O(V + E) |
| Graph (Matrix)   | O(V²) |

---

## 🔹 Quick Summary Table

| Complexity | Meaning |
|-----------|---------|
| **O(1)**  | constant memory |
| **O(n)**  | memory grows with input size |
| **O(log n)** | logarithmic memory used in divide & conquer |
| **O(n²)** | quadratic memory for grids/matrices |
| **O(n + m)** | used often in graphs |

---

## ✔ Conclusion

Space Complexity helps you pick algorithms that are not just fast—but **efficient in memory** as well.  
This becomes important when solving large constraints in coding interviews or competitive programming.

---

You can now place this file inside your:

```
DSA with python/
 └── notes/
      └── space_complexity.md
```

