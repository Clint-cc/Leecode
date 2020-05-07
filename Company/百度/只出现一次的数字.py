# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次，找出出现一次的元素，
#             (算法需要线性的时间复杂度，不使用额外空间)
# @Thinking : 方法太多：Counter函数、暴力、切片、set后求和、异或


def singleNumber(nums):
    single_num = 0
    for num in nums:  # [1,2,1,4,2]
        single_num = single_num ^ num
    return single_num


print(singleNumber([1, 2, 1, 4, 2]))
