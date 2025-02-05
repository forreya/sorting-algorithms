<h1 align="center">Sorting Algorithms</h1>

<p align="center">
	<a href="#"><img alt="Python" src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54"></a>
</p>

## Description
Highly optimized and performant sorting algorithms. Each algorithm is implemented in **Python** and includes both classic and advanced sorting techniques, with detailed explanations of their logic, time complexities, and practical applications.

## Table of Contents
- [Comparison-Based Sorting](#comparison-based-sorting)
- [Non-Comparison-Based Sorting](#non-comparison-based-sorting)
- [Hybrid Sorting Algorithms](#hybrid-sorting-algorithms)
- [Contributing](#contributing)

## Setting Up
To ensure Python can import modules correctly, add the following line to your shell configuration file (e.g., `.zshrc` or `.bashrc`):

```
export PYTHONPATH="[path_to_this_directory]"
```

This path allows python to know what the top-level directory is (in this case, sorting-algorithms) so it can resolve these imports across the codebase.

## Sorting Algorithms Checklist

### **Comparison-Based Sorting**

#### For Arrays
- [x] Bubble Sort
- [x] Selection Sort
- [x] Insertion Sort
- [x] Merge Sort
- [ ] Quick Sort
- [ ] Heap Sort (uses a binary heap implemented in an array)
- [ ] Tim Sort (Python’s built-in algorithm)

#### For Linked Lists
- [ ] Merge Sort (optimal for linked lists, avoids random access issues)
- [ ] Insertion Sort (efficient for sorted insertions)

#### For Trees
- [ ] Tree Sort (binary search tree-based sorting)
- [ ] Heap Sort (uses a tree-based binary heap)

### **Non-Comparison-Based Sorting**

#### For Arrays
- [ ] Counting Sort (uses auxiliary arrays for counting frequencies)
- [ ] Radix Sort (uses arrays and queues for digit grouping)
- [ ] Bucket Sort (uses an array of buckets)

### **Hybrid Sorting Algorithms**

#### For Arrays
- [ ] IntroSort (used in modern libraries like C++’s STL sort)

#### For Distributed Systems
- [ ] Parallel Sorting Algorithms (splits arrays into chunks for concurrent sorting)
- [ ] Sorting in Distributed Systems (uses distributed arrays and priority queues)

### *Random Info**
- Sorting algorithms for **linked lists** are limited to those that don’t rely on random access.
- **Tree-based sorting** leverages binary search trees or heaps.
- **Non-comparison-based sorting** assumes numeric input or sortable keys with a known range.

## Note
You need to add this project directory to your PYTHONPATH environmental variable for the imports to work correctly.

## Contributing
If you have suggestions to optimize an algorithm, identify any issues, or improve the documentation, please fork the repository and submit a pull request. Alternatively, you can also open an issue to start a discussion about the potential improvement.