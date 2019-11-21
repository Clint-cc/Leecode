# -*- coding:utf-8 -*-
# @Author  : Clint

# 又是一个关于动态规划的算法题
a = [2, 5, 8, 3, 9, 12, 6]


def rob(nums):
    n = len(nums)
    if n == 0:
        return 0
    if n <= 2:
        return max(nums)
    i = 3
    dp = [nums[0]] + [nums[1]] + [nums[0] + nums[2]] + [0] * (n - 3)
    while i < n:
        dp[i] = max(dp[i - 2] + nums[i], dp[i - 3] + nums[i])
        i += 1
    return max(dp)


print(rob(a))
