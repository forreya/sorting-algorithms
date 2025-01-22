<h1 align="center">Bubble Sort</h1>
Bubble Sort is a simple sorting algorithm that repeatedly steps through the list a maximum of N times, compares adjacent elements, and swaps them if they are in the wrong order. This process continues until the list is sorted.

## Performance
- **Best Case Time Complexity**: O(n) - When the list is already sorted, only one pass will be needed to discover that no swaps are required and so the outer loop will end early.
- **Worst Case Time Complexity**: O(n^2) - If the list is reversed, the largest element starts at the beginning and needs N-1 swaps to reach its correct position at the end. Similarly, the smallest element starts at the end and takes N-1 passes to "bubble up" to the beginning.
- **Space Complexity**: O(1) - As no additional data structures are used. We are simply stepping through and swapping elements as needed.

## Logic Flow
1. Create an outer loop to step through the array up to N times (where N is the length of the array).
2. Create an inner loop to compare adjacent elements and swap them if they are in the wrong order.
3. For the outer loop, initialize a 'swapped' variable and set it to False. This will tracks whether a swap occurred during each pass.
4. If no swaps occur in a pass, the list is already sorted and the 'swapped' variable will remain False, so the algorithm will terminate early.
5. In the worst case, the total number of 'step-throughs' will be N.

## Optimization w/ Early Termination
1. The swapped flag is initialized to False at the start of each outer loop iteration. If any swaps occur during the inner loop (aka the 'stepping' process), swapped is set to True.
2. If there is an iteration where no swaps occur (i.e., swapped remains False), the algorithm will break out of the loop.
3. This avoids redundant iterations that won't actually result in any more swaps, reducing the practical time complexity. 

## Advantages
1. Simple and easy to implement.
2. In-place sorting; no extra memory needed.

## Disadvantages
1. Inefficient for large datasets O(n^2). Other sorting algorithms like Merge Sort or Quick Sort are much faster on average.