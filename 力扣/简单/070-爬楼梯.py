# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint


def climbStairs(n):
    dp = []
    dp.append(1)  # 初始状态，只有1阶的时候有一种走法
    dp.append(2)  # 有2阶的时候有两种走法
    if n == 1:
        return 1
    if n == 2:
        return 2
    for i in range(2, n):
        dp.append(dp[i - 1] + dp[i - 2])
    print(dp)
    return dp[-1]


print(climbStairs(6))
