def insertion_sort(arr: list[int]) -> list[int]:
	for i in range(1, len(arr)):
		curr_pointer = i
		for j in range(i - 1, -1, -1):
			if arr[curr_pointer] > arr[j]:
				break
			arr[curr_pointer], arr[j] = arr[j], arr[curr_pointer]
			curr_pointer = j
	return arr

def insertion_sort_2(arr: list[int]) -> list[int]:
	for i in range(1, len(arr)):
		comparison_val = arr[i]
		j = i - 1
		while comparison_val < arr[j] and j >= 0:
			arr[j + 1] = arr[j]
			j -= 1
		arr[j + 1] = comparison_val
	return arr

arr = [2, 8, 5, 3, 9, 4, 1]
print(f"Result: {insertion_sort_2(arr)}")