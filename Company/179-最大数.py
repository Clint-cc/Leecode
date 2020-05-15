# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 给定一组非负整数，重新排列它们的顺序使之组成一个最大的整数。
# @Thinking :
from typing import List


# 方法一：
# class LargerNumKey(str):
#     def __lt__(x, y):
#         return x + y > y + x
# class Solution:
#     def largestNumber(self, nums):
#         if not nums: return ''
#         nums = map(str, nums)  # 将元素转为字符串
#         nums = list(sorted(nums, key=LargerNumKey))  # 自定义排序，根据'富比较'
#         largest_num = ''.join(nums)  # 将排序后的列表一次拼接
#         return '0' if largest_num[0] == '0' else largest_num

# 方法二：
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        from functools import cmp_to_key  # 导入比较函数
        if not nums: return ''
        nums = map(str, nums)  # 将元素转为字符串
        nums = sorted(nums, key=cmp_to_key(lambda x, y: int(y + x) - int(x + y)))  # 自定义排序
        return ''.join(nums).lstrip('0') or '0'  # 防止用例为多个0


s = Solution()
print(s.largestNumber([10, 11]))
