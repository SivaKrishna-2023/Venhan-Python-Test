from typing import List

def merge_sort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr


    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half_sorted = merge_sort(left_half)
    right_half_sorted = merge_sort(right_half)

    return merge(left_half_sorted, right_half_sorted)

def merge(left: List[int], right: List[int]) -> List[int]:
    result = []
    left_idx = 0
    right_idx = 0


    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1

    while left_idx < len(left):
        result.append(left[left_idx])
        left_idx += 1

    while right_idx < len(right):
        result.append(right[right_idx])
        right_idx += 1

    return result


arr = [5, 3, 8, 1, 2, 7, 4, 6]
sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)