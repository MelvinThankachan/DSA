def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array.pop()
    lower = []
    higher = []
    for item in array:
        if item > pivot:
            higher.append(item)
        else:
            lower.append(item)
    return quick_sort(lower) + [pivot] + quick_sort(higher)


array = [5, 8, 2, 1, 0, 6, 4, 2, 3, 6]
# array = [5, 8]
# array = [5]
# array = []   
print(quick_sort(array))