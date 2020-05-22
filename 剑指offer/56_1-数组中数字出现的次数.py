# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。请写程序找出这两个只出现一次的数字


def singleNumbers(nums):
    '''
    思路： 异或运算
        任何数和本身异或则为0
        任何数和 0 异或是本身
    :param nums:
    :return:
    '''
    res = []
    n = len(nums)
    nums.sort()
    if nums[0] != nums[1]:
        res.append(nums[0])
    if nums[n - 1] != nums[n - 2]:
        res.append(nums[n - 1])
    for i in range(1, len(nums) - 1):
        if len(res) == 2:
            return res
        if nums[i] != nums[i - 1] and nums[i] != nums[i + 1]:
            res.append(nums[i])


print(singleNumbers([1, 2, 10, 4, 1, 4, 3, 3]))
