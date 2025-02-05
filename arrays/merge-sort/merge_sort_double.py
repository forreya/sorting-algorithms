# Preferred Method

def merge_sort(arr: list[int]) -> list[int]:
	if len(arr) == 1:
		return arr

	left_sorted = merge_sort(arr[:len(arr)//2])
	right_sorted = merge_sort(arr[len(arr)//2:])

	return merge(left_sorted, right_sorted)

def merge(left_arr, right_arr) -> list[int]:
	merged = []
	left = 0
	right = 0

	while left < len(left_arr) and right < len(right_arr):
		if left_arr[left] <= right_arr[right]:
			merged.append(left_arr[left])
			left += 1
		else:
			merged.append(right_arr[right])
			right += 1
	
	while left < len(left_arr):
		merged.append(left_arr[left])
		left += 1

	while right < len(right_arr):
		merged.append(right_arr[right])
		right += 1
	
	return merged

arr = [1]

print(f"{merge_sort(arr)}")