# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 给你一个房屋数组houses 和一个整数 k ，其中 houses[i] 是第 i 栋房子在一条街上的位置，现需要在这条街上安排 k 个邮筒。
#             请你返回每栋房子与离它最近的邮筒之间的距离的最小总和。
# @Thinking :
from typing import List


class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        # dp[i][j] 表示i个房子，j个邮局的最小划分方法
        # 转移方程：
        #   dp[i][j] = min(dp[k-1][j-1] + rec[k][i], dp[i][j])    # k >=j-1 and k<=i
        #   rec[i][j] 表示从第i个房子到第j个房子，用一个邮箱最小的花费，提前预处理
        import math
        houses.sort()
        n = len(houses)
        rec = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(i, n):
                mid = (i + j) // 2
                for x in range(i, j + 1):
                    rec[i][j] += abs(houses[x] - houses[mid])

        dp = [[math.inf for _ in range(k + 1)] for _ in range(n)]
        for i in range(n):
            dp[i][1] = rec[0][i]
        for i in range(n):
            for j in range(2, min(i + 1, k) + 1):
                for y in range(j - 1, i + 1):
                    dp[i][j] = min(dp[i][j], dp[y - 1][j - 1] + rec[y][i])

        return dp[n - 1][k]


s = Solution()
print(s.minDistance([1, 4, 8, 10, 20], 3))
print(s.minDistance([2, 3, 5, 12, 18], 2))
print(s.minDistance([7, 4, 6, 1], 1))
print(s.minDistance([3, 6, 14, 10], 4))
