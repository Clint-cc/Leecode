# -*- coding:utf-8 -*-
# @Author  : Clint


def hamm(x, y):
    return bin(x ^ y).count('1')


print(hamm(4, 1))