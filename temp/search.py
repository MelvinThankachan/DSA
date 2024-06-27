# Linear Search
# Binary Search
# Ternary Search
# Jump Search
# Exponential Search


def linear_search(array, target):
    for i, element in enumerate(array):
        if element == target:
            return i
    raise ValueError(f"{target} not in the list")


def binary_search_iteration(array, target):
    left = 0
    right = len(array) - 1
    if target > array[right] or target < array[left]:
        raise ValueError(f"{target} not in the list")
    if target == array[left]:
        return left
    if target == array[right]:
        return right
    while right != left + 1:
        middle = (left + right) // 2
        if target > array[middle]:
            left = middle
        elif target < array[middle]:
            right = middle
        elif target == array[middle]:
            return middle
    raise ValueError(f"{target} not in the list")


def binary_search_recursive(array, target):
    left = 0
    right = len(array) - 1
    middle = (left + right) // 2
    if array[middle] == target:
        return middle
    if array[right] == target:
        return right
    if array[left] == target:
        return left
    if target > array[right] or target < array[left]:
        raise ValueError(f"{target} not in the list")
    if right == left + 1:
        raise ValueError(f"{target} not in the list")
    if target > array[middle]:
        binary_search_recursive(array=array[middle:right], target=target)
    elif target < array[middle]:
        binary_search_recursive(array=array[left:middle], target=target)

def binary_search_iter(array, target):
    left = 0
    right = len(array) - 1
    while right < left:
        middle = (left + right) // 2
        if target > array[middle]:
            left = middle + 1
        if target < array[middle]:
            right = middle - 1
        if target == array[middle]:
            return middle
    raise ValueError(f"{target} not in the list")

integer_array = [
    23,
    45,
    12,
    67,
    90,
    34,
    56,
    78,
    91,
    20,
    11,
    55,
    88,
    37,
    62,
    15,
    72,
    84,
    19,
    47,
    30,
    66,
    99,
    25,
    81,
    13,
    50,
    73,
    92,
    38,
    64,
    17,
    79,
    96,
    22,
    42,
    58,
    87,
    10,
    53,
    74,
    93,
    29,
    85,
    16,
    41,
    60,
    82,
    18,
    49,
    35,
    68,
    95,
    21,
    48,
    14,
    54,
    77,
    89,
    24,
    44,
    69,
    94,
    31,
    76,
    32,
    61,
    83,
    27,
    52,
    70,
    97,
    26,
    80,
    39,
    63,
    86,
    33,
    59,
    75,
    98,
    28,
    43,
    65,
    36,
    57,
    71,
    40,
    51,
    100,
    9,
    46,
    7,
    3,
    5,
    2,
    1,
    4,
    6,
    8,
]
integer_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
integer_array.sort()
target = 10
print(integer_array)

# print(linear_search(integer_array, target))
# print(binary_search_iteration(integer_array, target))
# print(binary_search_iteration(integer_array, target))
print(binary_search_iter(integer_array, target))
print(integer_array.index(target))
