# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 给定一个数组，它的第i个元素是一支给定股票第i天的价格，求最大利润
# @Thinking :

class Solution:
    def maxProfit(self, prices):  # [7,1,5,3,6,4]
        if not len(prices):
            return 0
        minprice = max(prices)
        maxprofit = 0
        for i in range(len(prices)):
            if prices[i] <= minprice:
                minprice = prices[i]
            elif prices[i] - minprice > maxprofit:
                maxprofit = prices[i] - minprice

        return maxprofit


s = Solution()
print(s.maxProfit([7, 1, 5, 3, 6, 4]))
