# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 已有方法rand7可生成1-7范围内的均匀随机整数，写一个方法rand10生成1到10范围内的均匀随机整数；
# @Thinking : 等概率映射，rand7 + (rand7 - 1) * 7, 1-10，11-20，21-30，31-40都是等概率出现的，每个
#             数只能有且一种组合方式出现;

def random7():
    s = [1, 2, 3, 4, 5, 6, 7]
    import random
    return random.choice(s)


def random10():
    num = (random7() - 1) * 7 + random7()
    while num > 40:
        num = (random7() - 1) * 7 + random7()
    return 1 + (num - 1) % 10


print(random10())
