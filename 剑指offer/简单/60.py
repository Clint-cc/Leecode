# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 把n个骰子扔在地上，所有骰子朝上一面的点数之和为s。输入n，打印出s的所有可能的值出现的概率。


def twoSum(n):
    fenmu = 6 ** n
    for i in range(n, n * 6 + 1):
        # print("{:.5f}".format(i/fenmu))
        # print('%.5f'%(i/fenmu))
        print(format((i / fenmu), '.5f'))


twoSum(1)
