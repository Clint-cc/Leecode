# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 寻找右侧边界的⼆分搜索
# @Thinking :

# 找右边侧的二分查找,如[1,2,2,2,5,7,9] 找2的位置应该是 index = 3
def right_bound_search(nums, target):
    if len(nums) == 0: return -1
    left, right = 0, len(nums)  # 左闭右开

    while left < right:  #
        mid = (left + right) // 2
        if nums[mid] == target:
            left = mid + 1  # 成立不要立即返回
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid  #
    # return right - 1
    if left == 0: return -1  # target比所有数都打
    return left - 1 if nums[left - 1] == target else -1


print(right_bound_search([1, 2, 2, 2, 5, 7, 9], 2))
