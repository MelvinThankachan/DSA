def twoSum(nums, target):
    need_dict = {}
    for i, element in enumerate(nums):
        need = target - element
        try:
            need_index = need_dict.get(str(need))
            if need_index:
                return [need_index, i]
        except:
            pass
        need_dict[str(need)] = i
nums = [2,7,11,15]
target = 9
output = twoSum(nums, target)
print(output)