def bubble_sort(array, n = -1):
    if n == -1:
        n = len(array)
    for i in range(n - 1):
        if array[i] > array[i+1]:
            temp = array[i+1]
            array[i+1] = array[i]
            array[i] = temp
    if n == 0:
        return array
    return bubble_sort(array, n-1)


array = [8, 2, 1, 0, 6, 4, 2]
sorted_array = bubble_sort(array)
print(sorted_array)