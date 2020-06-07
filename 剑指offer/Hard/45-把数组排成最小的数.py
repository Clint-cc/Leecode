# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 输入一个非负整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
# @Thinking :
from typing import List


class Solution(str):
    # def __lt__(self, y):
    #     return self + y < y + self

    def minNumber(self, nums: List[int]) -> str:
        # res = sorted(map(str, nums), key=Solution)

        from functools import cmp_to_key
        res = sorted(map(str, nums), key=cmp_to_key(lambda x, y: int(x + y) - int(y + x)))

        return ''.join(res)


s = Solution()
print(s.minNumber([3, 30, 34, 5, 50, 9]))
