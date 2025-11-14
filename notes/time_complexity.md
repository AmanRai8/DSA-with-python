# 🕒 Time Complexity (Big-O Notation)

Time complexity tells us how **fast an algorithm grows** as the input
size increases.\
It does *not* measure actual time, but the **number of operations**
relative to input size.

------------------------------------------------------------------------

## 🚀 Why Time Complexity?

-   Helps compare algorithms
-   Predicts performance for large inputs
-   Avoids slow and inefficient solutions

------------------------------------------------------------------------

## 🔥 Common Big-O Complexities

### **O(1) --- Constant Time**

Runs in the same time regardless of input size.

``` python
arr[0]
```

------------------------------------------------------------------------

### **O(n) --- Linear Time**

Work grows proportionally with input size.

``` python
for x in arr:
    print(x)
```

------------------------------------------------------------------------

### **O(log n) --- Logarithmic Time**

Input size is reduced in each step.

Used in: - Binary search\
- Efficient divide-and-conquer algorithms

------------------------------------------------------------------------

### **O(n log n)**

Most efficient comparison-based sorting algorithms: - Merge Sort\
- Quick Sort\
- Heap Sort

------------------------------------------------------------------------

### **O(n²) --- Quadratic Time**

Nested loops.

``` python
for i in arr:
    for j in arr:
        print(i, j)
```

------------------------------------------------------------------------

### **O(2ⁿ) --- Exponential Time**

Very slow --- used in brute-force recursion.

Example: - Naive recursive Fibonacci

------------------------------------------------------------------------

### **O(n!) --- Factorial Time**

Extremely slow.\
Used in generating permutations.

------------------------------------------------------------------------

## 🧠 Quick Identification Tricks

  Code Pattern                  Time Complexity
  ----------------------------- -----------------
  Single loop                   O(n)
  Nested loops                  O(n²)
  Divide input by 2 each step   O(log n)
  Loop + log operation          O(n log n)
  Adding constant variables     O(1)

------------------------------------------------------------------------

## 📌 Summary

-   Time complexity describes **how an algorithm scales**.\
-   Big-O notation focuses on the **worst-case scenario**.\
-   Choosing efficient algorithms saves time and resources.

------------------------------------------------------------------------

Keep this file in your repo inside your `notes/` folder for quick
reference.
