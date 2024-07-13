def insertion_sort(array):

    def shift(array, left_index, right_index):
        last = array[right_index]
        for i in range(right_index, left_index, -1):
            array[i] = array[i - 1]
        array[left_index] = last

    n = len(array)
    for i in range(1, n):
        current = array[i]
        for j in range(i):
            if array[j] > current:
                shift(array, j, i)
                break

    return array


array = [5, 8, 2, 1, 0, 6, 4, 2]
array = [5, 8]
array = [5]
array = []
sorted_array = insertion_sort(array)
print(sorted_array)
