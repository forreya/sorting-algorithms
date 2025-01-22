
def bubble_sort(arr: list[int]) -> list[int]:
	for _ in range(len(arr)):
		swapped = False
		for x in range(len(arr)-1):
			if arr[x] > arr[x+1]:
				swapped = True
				arr[x], arr[x+1] = arr[x+1], arr[x]
		if not swapped:
			break
	return arr

arr = [2, 8, 5, 3, 9, 4, 1]
print(f"Result: {bubble_sort(arr)}")