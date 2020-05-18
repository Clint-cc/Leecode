# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 寻找左侧边界的⼆分搜索
# @Thinking :

# 找左边侧的二分查找,如[1,2,2,2,5,7,9] 找2的位置应该是 index = 1
def left_bound_search(nums, target):
    if len(nums) == 0: return -1
    left, right = 0, len(nums)  # 注意

    while left < right:  # 左闭右开
        mid = (left + right) // 2
        if nums[mid] == target:
            right = mid
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid  #

    if left == len(nums): return -1  # target比所有数都打
    return left if nums[left] == target else -1


print(left_bound_search([2, 2, 2, 3, 4], 2))
