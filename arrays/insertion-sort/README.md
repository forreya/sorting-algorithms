<h1 align="center">Insertion Sort</h1>
Insertion Sort is a simple, in-place sorting algorithm that works by iterating through the array and inserting each element into its correct position relative to the already sorted portion of the array.

## Performance
- **Best Case Time Complexity**: O(n) – When the array is already sorted, only one comparison per element is needed as the middle loop only runs through one check before breaking as the left adjacent element is always already smaller than the current element being investigated.
- **Worst Case Time Complexity**: O(n^2) – If the array is sorted in reverse order, each element has to be compared and shifted the maximum number of times until it reaches the correct position at the beginning of the sorted portion of the array.
- **Space Complexity**: O(1) – Other than some pointers and variables, no additional memory is required as the algorithm is in-place.

## Logic Flow
1. Start from the second element (index 1), as a single-edge-element list is already sorted.
2. Consider the current element (the element being investigated) as the first unsorted element.
3. Compare it with its left adjacent neighbor and shift the left element one to the right if it is larger than the element being investigated.
4. Insert the element into its correct position if either:
	- If it is larger than the current left element, or
	- The traversing pointer reaches the boundary at the beginning of the array.
5. Repeat until the main outer iteration reaches the end of the array.

## Advantages
1. Simple and easy to implement.
2. Efficient for arrays that are nearly sorted or close to sorted.
3. In-place sorting so no extra memory is needed.
4. Stable sorting so it maintains the order of equal elements.

## Disadvantages
1. Inefficient for large datasets as O(n^2) time complexity makes it very slow compared to other sorting algorithms like Merge Sort or Quick Sort.