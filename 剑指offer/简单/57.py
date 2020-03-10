# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 和为s的两个数字


def twosum(nums, target):
    for num in nums:
        t = target - num
        if t in nums and t != num:
            return [t, num]
            break


print(twosum([9, 7, 13, 15], 22))
