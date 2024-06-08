def quicksort(arr):
    if len(arr) <= 1:
        return arr

    # pivot
    pivot = arr[0]

    less = []
    greater = []

    for x in arr[1:]:
        if x <= pivot:
            less.append(x)
        else:
            greater.append(x)
    sorted_less = quicksort(less)
    sorted_greater = quicksort(greater)
    return sorted_less + [pivot] + sorted_greater

arr = [3, 6, 8, 10, 1, 2, 1]
print(quicksort(arr))  # Output: [1, 1, 2, 3, 6, 8, 10]