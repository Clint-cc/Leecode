# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。


# 超出时间限制
'''
def majorityElement(nums):
    for i in nums:
        if nums.count(i) > (len(nums) / 2):
            return i
'''

# 众数的特点
'''
def majorityElement(nums):
    nums.sort()
    return nums[len(nums)//2]
'''


# 第一个数开始count=1，遇到相同的就加1，遇到不同的就减1，
# 减到0就重新换个数开始计数，总能找到最多的那个
def majorityElement(nums):
    res = nums[0]
    count = 1
    for num in nums:
        if num == res:
            count += 1
        else:
            count -= 1
            if count == 0:
                res = num
                count = 1
    return res


print(majorityElement([3, 2, 3]))
