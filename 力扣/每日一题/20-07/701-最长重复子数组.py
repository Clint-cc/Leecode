# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 
# @Thinking :


class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        n, m = len(A), len(B)
        # dp[i-1][j-1]  为 A以i-1结尾，B以j-1结尾的最长重复子数组长度
        res = 0
        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

        # 初始化,A没数的时候，或者B没数的时候 （可不写）
        # for i in range(m):
        #     dp[0][i] = 0
        # for j in range(n):
        #     dp[j][0] = 0

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = 0  # 易错：这里只要不连续相等，就重置为0，而不是等于dp[i-1][j-1]
                res = max(dp[i][j], res)

        return res
