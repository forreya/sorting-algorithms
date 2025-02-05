<h1 align="center">Merge Sort</h1>
Merge sort is a classic divide and conquer sorting algorithm. It works by recursively splitting an array into halves, sorting each half, and then merging the sorted halves into a single sorted array. This process means that the overall time complexity remains consistent, even in the worst case.

## Performance
- **Time Complexity**: O(nlog(n)) - The array is recursively split into two halves until arrays of size 1 are reached. This division takes O(log n) levels. At each level, merging two sorted arrays takes O(n) time (the total number of elements across all subarrays at that level is n).
- **Space Complexity**: O(n) - Merge sort uses depth-first recursion, which means that recursive calls for the left and right halves are processed sequentially rather than concurrently. Although each recursive call holds its own left and right sorted arrays until merged, only one branch of the recursion is active at a time. Along any branch, the sizes of arrays decrease (n, n/2, n/4, …), so their sum is bounded by approximately 2n. Therefore, even though memory is allocated at each level, the peak memory usage remains O(n) and does not accumulate to O(n log n).

## What Data Exactly Contributes To The Space Complexity?
At each level of recursion, the primary variables that take up extra space are the temporary arrays created during the split: namely, the left_arr and right_arr (and their sorted results, stored in variables such as left_sorted and right_sorted). In addition, the merge function creates a new 'merged' array when combining two halves.

## Logic Flow
1. The merge_sort function first checks if the length of arr is 1. If true, it returns arr immediately since a single-element array is already sorted. This is the base case that acts as the stopping point for recursion.
2. The array is split into two halves using slicing. The function then recursively calls itself on each half, breaking down the array until it reaches the base case (arrays of size 1).
3. Once the two halves are sorted (returned from the recursive calls), the merge function is called with these two sorted arrays as arguments. The result of this merge is returned so that at each level of recursion, the sorted merged version is passed up the recursion stack and set to either the left half or right half of the previous recursive call.
4. Inside the merge function, two pointers (left and right) traverse left_arr and right_arr until one is fully traversed. In this main loop, the function compares elements from both arrays and appends the smaller element to the merged array at every iteration until the loop breaks.
5. There will be two additional while loops after the main one to append all the remaining elements from either left_arr or right_arr based on which one still has elements remaining.
6. The newly created 'merged array', which represents the fully sorted combination of the two halves, is returned. As the recursion unwinds, these sorted arrays are continuously merged and returned until the top-level call returns the final completely sorted array.

## Advantages
1. Consistent performance by guaranteeing O(n log n) performance across best, average, and worst cases.
2. Stable algorithm so it maintains the relative order of equal elements, which can be important in certain applications.

## Disadvantages
1. Requires O(n) extra space due to the right and left arrays that are created at each level of recursion + the 'merged' array to store the result of combining two halves.