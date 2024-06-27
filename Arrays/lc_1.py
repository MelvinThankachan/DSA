# Two Sum (LeetCode - Problem 1)



def twoSum(nums, target):
    nums_map = {}

    for i, j in enumerate(nums):
        check = target - j
        if check in nums_map:
            return [nums_map[check], i]
        else:
            nums_map[j] = i


nums = [2, 7, 11, 15]
target = 9
print("Indices of Two Sum:", twoSum(nums, target))
