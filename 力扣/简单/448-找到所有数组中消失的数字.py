# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint


def findDisappNun(nums):
    n = len(nums)
    for i in range(1, n + 1):
        if i in nums:
            while i in nums:
                nums.remove(i)
        else:
            nums.append(i)
    return nums


print(findDisappNun([4, 9, 2, 7, 8, 2, 5, 1, 7]))
