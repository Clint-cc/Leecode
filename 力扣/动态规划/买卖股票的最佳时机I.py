# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 给定一个数组，它的第i个元素是一支给定股票第i天的价格，求最大利润
# @Thinking :
'''
                # base case1: 还未开始 利润为0
                dp[-1][k][0] = 0
                # base case2: 还未开始，不可能持有股票，设为负无穷
                dp[-1][k][1] = -math.inf
                # base case3: k是从1开始的，k=0意味着不允许交易，利润
                dp[i][0][0] = 0
                # base case4: k次交易完成后，不可能还持有，设为负无穷
                dp[i][0][1] = -math.inf

                # 状态转移方程
                dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
                dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k][0] - prices[i])
'''
import math


class Solution:
    # 简单的dp，提交超时
    # def maxProfit(self, prices):
    #     n = len(prices)
    #     dp = [0 for _ in range(n)]
    #     for i in range(1, n):
    #         for j in range(i):
    #             if prices[i] > prices[j]:
    #                 dp[i] = max(dp[i], prices[i] - prices[j])
    #     return max(dp)

    # 穷举、状态转移、dp
    # [i][k][0/1]: i表示第i天， k表示第k次交易， 0/1：0表示不持有股票， 1表示持有股票
    def maxProfit(self, prices):
        n = len(prices)
        # import numpy
        dp = [[i for i in range(2)] for _ in range(n)]
        for i in range(n):
            if i - 1 == -1:
                dp[i][0] = 0
                dp[i][1] = -prices[i]
                continue
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
        return dp[n - 1][0]

s = Solution()
print(s.maxProfit([7, 1, 5, 3, 6, 4]))
