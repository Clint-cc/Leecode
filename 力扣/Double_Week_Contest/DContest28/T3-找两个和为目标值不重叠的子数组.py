# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 
# @Thinking :
from typing import List
import math


class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        j = 0
        summ = 0
        res = [1e8 for _ in range(n)]
        min_cnt = math.inf
        for i in range(n):
            summ += arr[i]
            while (summ > target):
                summ -= arr[j]
                j += 1
            if summ == target:
                if j > 0:
                    min_cnt = min(min_cnt, (i - j + 1) + res[j - 1])
                res[i] = i - j + 1
            if i > 0:
                res[i] = min(res[i], res[i - 1])

        return -1 if min_cnt > n else min_cnt


s = Solution()
print(s.minSumOfLengths([4, 3, 2, 6, 2, 3, 4], 6))
