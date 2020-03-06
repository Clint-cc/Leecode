# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 找到二维数组中的任意一个重复的数


class Solution:
    def findRepeatNumber(nums):
        nums = sorted(nums)
        # print(nums)
        pre = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == pre:
                return nums[i]
            else:
                pre = nums[i]


print(Solution.findRepeatNumber([6, 3, 1, 0, 2, 5, 3, 5]))
