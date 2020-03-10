# -*- coding:utf-8 -*-
# @Author  : Clint


def maxProfit(prices):       # [7,1,5,3,6,4]
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


print(maxProfit([7,1,5,3,6,4]))


