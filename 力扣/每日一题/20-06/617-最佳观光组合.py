# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 求最大 A[i] + A[j] + i - j
# @Thinking :


class Solution:
    def maxScoreSightseeingPair(self, A):
        # 枚举优化
        n = len(A)
        max_i = A[0] + 0
        res = 0
        for j in range(1, n):
            max_i = max(max_i, A[j - 1] + (j - 1))
            res = max(res, max_i + A[j] - j)
        return res


s = Solution()
print(s.maxScoreSightseeingPair([82, 12, 52, 22, 62]))
