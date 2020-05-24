# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 求斐波那契第n项的数,答案需要先取模1e9+7(1000000007)
# 0 1 1 2 3 5 8 13 21 34 55 89 144 233

'''
# 常用的递归不可取，超出时间限制。
    def fib(n):
        if n < 1:
            return 0
        elif n <= 2:
            return 1
        else:
            return (Solution.fib(n-1)+Solution.fib(n-2)) % 1000000007
'''


class Solution:
    def fib(n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a % 1000000007


print(Solution.fib(1))
