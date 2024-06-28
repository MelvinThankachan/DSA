class Recursion:

    def factorial(self, n):
        if n == 0:
            return 1
        return n * self.factorial(n - 1)

    def fibonacci(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.fibonacci(n - 1) + self.fibonacci(n - 2)

    def binary_search(self, array, target):
        left = 0
        right = len(array) - 1
        return self.binary_search_rec(array, target, left, right)

    def binary_search_rec(self, array, target, left, right):
        middle = (right + left) // 2
        if right < left:
            raise ValueError(f"{target} not in the list")
        if array[middle] == target:
            return middle
        if target > array[middle]:
            return self.binary_search_rec(array, target, left=middle + 1, right=right)
        if target < array[middle]:
            return self.binary_search_rec(array, target, left=left, right=middle - 1)

    def array_sum(self, array, i=0):
        length = len(array)
        if length == 0:
            raise IndexError("List is empty")
        if i == length - 1:
            return array[i]
        return array[i] + self.array_sum(array, i + 1)

    def reverse_string(self, string, i=0):
        length = len(string)
        if length == 0:
            return ""
        if i == length - 1:
            return string[i]
        return "" + self.reverse_string(string, i + 1) + string[i]

    def power(self, x, n):
        if n == 1:
            return x
        return x * self.power(x, n - 1)

    def palindrome(self, string):
        length = len(string)
        if length <= 1:
            return True
        if string[0] != string[-1]:
            return False
        return self.palindrome(string[1:-1])

    def combination_sum(self, array, target):
        array.sort()
        left = 0
        right = len(array) - 1
        if len(array) < 2:
            return []
        return self.combination_sum_rec(array, target, left, right)

    # def combination_sum_rec(self, array, target, left, right):
    #     if left >= right:
    #         return []
    #     left_element = array[left]
    #     right_element = array[right]
    #     if target == left_element + right_element:
    #         return [left_element, right_element]
    #     if target > left_element + right_element:
    #         return self.combination_sum_rec(array, target, left + 1, right)
    #     if target < left_element + right_element:
    #         return self.combination_sum_rec(array, target, left, right - 1)


recur = Recursion()
# print(recur.factorial(6))
# print(recur.fibonacci(5))
# array = [10, 100]
# target = 3
# print(recur.binary_search(array, target))
# print(recur.array_sum(array))
# string = "hello world"
# print(recur.reverse_string(string))
# print(recur.power(2, 5))
string = "qwq"
print(recur.palindrome(string))
