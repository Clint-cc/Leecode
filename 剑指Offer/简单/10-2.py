# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个
#             n级的台阶总共有多少种跳法。


def numWays(n):  # 1 2 3 5 8 13 21
    '''
    思路：设跳上 nn 级台阶有 f(n)f(n) 种跳法。在所有跳法中，青蛙的最后一步只有
    两种情况： 跳上 11 级或 22 级台阶。还是递归问题，只不过f(0)=1这里是个坑，
    就是说跳0级台阶有一种方法，就是不跳
    :param n:
    :return:
    '''
    a, b = 1, 1
    for _ in range(n):
        a, b = b, a + b
    return a % 1000000007


print(numWays(7))
