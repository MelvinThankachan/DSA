def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


arr = [1, 3, 5, 7, 9, 11, 13, 15]
target = 7
print(f"Index of {target}:", binary_search(arr, target))
