<h1 align="center">Selection Sort</h1>
Selection Sort is a simple comparison-based sorting algorithm. It repeatedly selects the smallest (or largest) element from the unsorted part of the array and swaps it with the first unsorted element. 

## Performance
- **Time Complexity**: O(n^2) - Every unsorted element is compared with every other unsorted element.
- **Space Complexity**: O(1) - It's an in-place algorithm and requires no additional memory.

## Logic Flow
1. The outer loop iterates over the array from left to right.
2. For each iteration, assume the first unsorted element is the smallest and set it as the minimum pointer.
3. The inner loop scans the remaining unsorted portion of the array to find the smallest element, updating the minimum pointer whenever a smaller element is found.
4. After the inner loop finishes, swap the smallest element (found by the minimum pointer) with the first unsorted element.
5. Repeat this process until the entire array is sorted.


## Optimization
1. Starting the inner loop at index i (the current position of the outer loop) leads to comparing the first unsorted element at i with itself.
2. To optimize, we can start the inner loop from i + 1, skipping this redundant comparison. This way, the algorithm immediately compares this first unsorted element with the other elements in the unsorted portion of the array, saving one check each iteration.

## Advantages
1. Simple and easy to implement.
2. In-place sorting; no extra memory needed.

## Disadvantages
1. Inefficient for large datasets O(n^2). Other sorting algorithms like Merge Sort or Quick Sort are much faster.
2. Not stable: Equal elements may not maintain their original order.