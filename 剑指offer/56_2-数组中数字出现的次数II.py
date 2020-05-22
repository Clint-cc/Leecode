# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question :在一个数组 nums中除一个数字只出现一次之外，其他数字都出现了三次。请找出那个只出现一次的数字。


def singleNumber(nums):
    if not len(nums):
        return 0
    elif len(nums) == 1:
        return nums[0]
    nums.sort()
    if nums[0] != nums[1]:
        return nums[0]
    if nums[len(nums) - 1] != nums[len(nums) - 2]:
        return nums[len(nums) - 1]
    for i in range(1, len(nums) - 2):
        if nums[i] != nums[i - 1] and nums[i] != nums[i + 1]:
            return nums[i]


print(singleNumber([9, 1, 7, 9, 7, 9, 7]))
