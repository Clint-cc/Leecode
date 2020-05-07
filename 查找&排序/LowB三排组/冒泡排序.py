# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 排序(正序)
# @Thinking : 比较列表中两个相邻的数，如果前面比后面的大，就交换位置


def Bubble_Sort(nums):
    n = len(nums)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums


print(Bubble_Sort([6, 1, 3, 4, 8, 7, 9, 5, 0, 2]))
