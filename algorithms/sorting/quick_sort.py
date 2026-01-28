def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    less = [value for value in arr if value < pivot]
    greater = [value for value in arr if value > pivot]

    return quick_sort(less) + [pivot] + quick_sort(greater)

print(quick_sort([5, 2, 1, 6, 3, 9, 4, 8, 7]))