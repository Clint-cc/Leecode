# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 
# @Thinking :
from typing import List


class Solution:
    def checkIfPrerequisite(self, n: int, es: List[List[int]], qs: List[List[int]]) -> List[bool]:
        d = [[False for _ in range(n)] for _ in range(n)]

        for e in es:
            d[e[0]][e[1]] = True

        # floyd 算法
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if d[i][k] and d[k][j]:
                        d[i][j] = True
        res = []
        for q in qs:
            res.append(d[q[0]][q[1]])
        return res


s = Solution()
print(s.checkIfPrerequisite(5, [[0, 1], [1, 2], [2, 3], [3, 4]], [[0, 4], [4, 0], [1, 3], [3, 0]]))
