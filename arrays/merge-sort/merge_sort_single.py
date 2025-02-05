# More-difficult Method

def merge_sort(arr: list[int]) -> list[int]:
	if len(arr) == 1:
		return arr

	left_array = arr[:len(arr)//2]
	right_array = arr[len(arr)//2:]

	# Split step
	merge_sort(left_array)
	merge_sort(right_array)

	# Merge step
	left = 0
	right = 0
	new = 0
	while left < len(left_array) and right < len(right_array):
		if left_array[left] <= right_array[right]:
			arr[new] = left_array[left]
			left += 1
		else:
			arr[new] = right_array[right]
			right +=1
		new += 1

	while left < len(left_array):
		arr[new] = left_array[left]
		left += 1
		new += 1
	
	while right < len(right_array):
		arr[new] = right_array[right]
		right += 1
		new += 1

	return arr

arr = [2,6,5,1,7,4,3]

print(f"{merge_sort(arr)}")