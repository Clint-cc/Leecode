# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 
# @Thinking :
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        if k <= 0 or n <= 0: return res

        def backTrack(n, k, start, track):
            if k == len(track):
                res.append(track)
                return
            for i in range(start, n + 1):
                backTrack(n, k, i + 1, track + [i])

        backTrack(n, k, 1, [])

        return res


s = Solution()
print(s.combine(4, 3))
