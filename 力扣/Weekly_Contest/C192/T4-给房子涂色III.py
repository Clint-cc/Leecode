# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 
# @Thinking :
from typing import List
import math


class Solution:
    def minCost(self, hs: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        # DP：
        # 状态表示：f(v, j, k)
        # 集合：所有染完前v个房子且目前有j个街区，且第v个房子的颜色是k的所有方案
        # 属性：求最小值

        # 转态计算：f(i-1, j, u) + cost(i, k)
        #          f(i - 1, j - 1, u) + cost(i, k)

        # 初始化：
        # 第0个房子有颜色：f(0, 1, k) = 0
        # 第0个房子有颜色：f(0, 1, i) = cost(0, i)

        dp = [[[math.inf for _ in range(n + 1)] for _ in range(m + 1)] for _ in range(m)]

        # DP初始化
        if hs[0]:
            dp[0][1][hs[0]] = 0
        else:
            for i in range(1, n + 1):
                dp[0][1][i] = cost[0][i - 1]

        for i in range(1, m):
            for j in range(1, target + 1):
                if hs[i]:
                    k = hs[i]
                    for u in range(1, n + 1):
                        if u == k:
                            dp[i][j][k] = min(dp[i][j][k], dp[i - 1][j][u])
                        else:
                            dp[i][j][k] = min(dp[i][j][k], dp[i - 1][j - 1][u])
                else:
                    for k in range(1, n + 1):
                        for u in range(1, n + 1):
                            if u == k:
                                dp[i][j][k] = min(dp[i][j][k], dp[i - 1][j][u] + cost[i][k - 1])
                            else:
                                dp[i][j][k] = min(dp[i][j][k], dp[i - 1][j - 1][u] + cost[i][k - 1])

        res = math.inf
        for i in range(1, n + 1):
            res = min(res, dp[m - 1][target][i])

        return -1 if res == math.inf else res


s = Solution()
print(s.minCost([0, 0, 0, 0, 0], [[1, 10], [10, 1], [10, 1], [1, 10], [5, 1]], 5, 2, 3))
print(s.minCost([0, 2, 1, 2, 0], [[1, 10], [10, 1], [10, 1], [1, 10], [5, 1]], 5, 2, 3))
print(s.minCost([0, 0, 0, 0, 0], [[1, 10], [10, 1], [1, 10], [10, 1], [1, 10]], 5, 2, 5))
print(s.minCost([3, 1, 2, 3], [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]], 4, 3, 3))
