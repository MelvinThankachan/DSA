def merge_sort(array):
    n = len(array)

    if n <= 1:
        return

    middle = n // 2
    left_half = array[:middle]
    right_half = array[middle:]
    merge_sort(left_half)
    merge_sort(right_half)

    i, j, k = 0, 0, 0
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            array[k] = left_half[i]
            i += 1
        else:
            array[k] = right_half[j]
            j += 1
        k += 1

    while i < len(left_half):
        array[k] = left_half[i]
        k, i = k + 1, i + 1
    while j < len(right_half):
        array[k] = right_half[j]
        k, j = k + 1, j + 1


array = [3, 5, 6, 1, 5, 6, 57, 4]
# array = [5, 8]
# array = [5]
# array = []
merge_sort(array)
print(array)
