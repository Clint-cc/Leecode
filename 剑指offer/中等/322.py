# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可凑成总金额
#             所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。


# 动态规划的思路
# f(n) = min(f(n - c1), f(n - c2), ... , f(n - cn)) + 1
# dp[i] = min([dp[n - i] for i in coins]) + 1
# n为凑齐的金额，cn代表每种面额硬币

'''
class Solution:
    def coinChange(coins, amount):
        coins = list(reversed(sorted(coins)))
        for i in coins:               # coins= [5, 2, 1]   amount = 17
            csum = 0
            while csum < amount:
                csum += i
'''
'''
class Solution(object):
    def coinChange(coins, amount):   # [1,2,5]   11
        res = [0 for _ in range(amount + 1)]

        for i in range(1, amount + 1):
            cost = float("inf")
            for c in coins:
                if i - c >= 0:
                    cost = min(cost, res[i-c]+1)
            res[i] = cost

        if res[amount] == float("inf"):
            return -1
        else:
            return res[amount]
'''


def coinChange(coins, amount):
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for j in range(len(coins)):
            if i >= coins[j]:
                dp[i] = min(dp[i], dp[i - coins[j]] + 1)

    return -1 if dp[-1] == amount + 1 else dp[-1]


print(coinChange([2, 1, 5], 11))
