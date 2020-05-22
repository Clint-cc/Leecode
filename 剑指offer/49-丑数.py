# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 我们把只包含因子 2、3和5的数称作丑数（Ugly Number）。求按从小到大
#             的顺序的第n个丑数。


def nthUglyNumber(n):
    ugly_list = [1]
    p2, p3, p5 = 0, 0, 0
    for i in range(1, n):
        umin = min(ugly_list[p2] * 2, ugly_list[p3] * 3, ugly_list[p5] * 5)
        # 一开始我没找到问题，最后发现这里不能用else if
        # 因为在丑数为6的时候，可能有两种情况，这时两个指针都要后移
        if umin == ugly_list[p2] * 2:
            p2 += 1
        if umin == ugly_list[p3] * 3:
            p3 += 1
        if umin == ugly_list[p5] * 5:
            p5 += 1
        ugly_list.append(umin)
    return ugly_list[-1]


print(nthUglyNumber(10))
