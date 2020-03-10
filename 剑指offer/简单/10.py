# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 求斐波那契第n项的数
# 0 1 1 2 3 5 8 13 21 34 55 89 144 233

class Solution:
    # 常用的递归不可取，超出时间限制。
    '''
    def fib(n):
        if n < 1:
            return 0
        elif n <= 2:
            return 1
        else:
            return Solution.fib(n-1)+Solution.fib(n-2)
    '''


print(Solution.fib(5))
