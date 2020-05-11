# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question :
# @Thinking :

def Maxsubstr(nums):
    for i in range(1, len(nums)):
        nums[i] += max(nums[i - 1], 0)
        return max(nums)
