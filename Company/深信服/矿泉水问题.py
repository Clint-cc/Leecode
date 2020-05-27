# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 小明横穿沙漠，需要携带至少x毫升的水。有两种规格的矿泉水可供选购：小瓶矿泉水每瓶500ml，
#             价格a元。大瓶矿泉水每瓶1500ml，价格b元。小明打算买一些矿泉水用于横穿沙漠，为了保证至
#             少买到x毫升的水，小明至少需要花费多少钱？
# @Thinking :

# 4999 5 10   [500, 1500]

class Solution:
    def mineralWater(self):
        x, a, b = 3000, 10, 25
        d = {1: 10, 3: 25}
        x = (x + 499) // 500
        dp = [float("inf")] * (x + 2)
        dp[0] = 0
        for k in d.keys():
            for ck in range(k, len(dp)):
                dp[ck] = min(dp[ck], dp[ck - k] + d[k])
        return min(dp[x:])
        # print(min(dp[x:]))


s = Solution()
print(s.mineralWater())
