def selection_sort(arr) -> list:
	for i in range(len(arr)):
		minimum_pointer = i
		for j in range(i + 1, len(arr)):
			if arr[j] < arr[minimum_pointer]:
				minimum_pointer = j
		arr[i], arr[minimum_pointer] = arr[minimum_pointer], arr[i]
	return arr

arr = [2, 8, 5, 3, 9, 4, 1]
print(f"Result: {selection_sort(arr)}")