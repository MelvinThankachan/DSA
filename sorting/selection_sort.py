def selection_sort(array):
    n = len(array)
    for i in range(n):
        min_index = n - 1
        for j in range(i, n):
            if array[j] < array[min_index]:
                min_index = j
        temp = array[i]
        array[i] = array[min_index]
        array[min_index] = temp
    return array


array = [5, 8, 2, 1, 0, 6, 4, 2]
sorted_array = selection_sort(array)
print(sorted_array)