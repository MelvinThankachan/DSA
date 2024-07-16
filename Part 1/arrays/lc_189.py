# Rotate Array (LeetCode - Problem 189)


def rotate_array(nums, k):
    n = len(nums)
    k = k % n
    nums[:] = nums[-k:] + nums[:-k]


nums = [1, 2, 3, 4, 5, 6, 7]
rotate_array(nums, 3)
print("Rotated Array:", nums)
