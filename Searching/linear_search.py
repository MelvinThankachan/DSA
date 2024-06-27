def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


arr = [3, 5, 2, 7, 9, 8, 1]
target = 8
print(f"Index of {target}:", linear_search(arr, target))
