# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 排序(正序)
# @Thinking : 取一个元素tmp(第一个元素)，使元素tmp归位；列表被tmp分成两部分，左边都比tmp小，右边比tmp大，递归完成排序；


def Quick_Sort(nums, left, right):
    if left < right:
        mid = partition(nums, left, right)
        Quick_Sort(nums, left, mid - 1)
        Quick_Sort(nums, mid + 1, right)


def partition(nums, left, right):
    tmp = nums[left]
    while left < right:
        while left < right and nums[right] >= tmp:
            right -= 1
        nums[left] = nums[right]

        while left < right and nums[left] <= tmp:
            left += 1
        nums[right] = nums[left]
    nums[left] = tmp
    return left


nums = [7, 1, 3, 4, 8, 0, 9, 5, 6, 2]
Quick_Sort(nums, 0, len(nums) - 1)
print(nums)
