# def twoSum(nums: list, target: int):
#     counter = 0
#     for i, y in enumerate(nums):
#         for j, k in enumerate(nums):
#             if y + k == target and j != i:
#                 print([i, j])
#                 return [i, j]
#
#
# nums = [3, 3]
# target = 6
# twoSum(nums=nums, target=target)
# def twoSum(nums: list, target: int):
#     seen = set()
#     for k, y in enumerate(nums):
#         if (target - y) in seen:
#             print(k, nums.index(target - y))
#             print(y, target - y)
#         else:
#             seen.add(y)
#
#
# """
# [1,2,3]
# target = 4
# ----
# seen = {3,2}
# picked = 1
# 4 -1 = 3 ------
#
# picked = 2
# 4-2 = 2
#
# picked = 3
# 4-3 = 1
#
# """
# nums = [5, 1, 2]
# target = 6
# twoSum(nums=nums, target=target)
