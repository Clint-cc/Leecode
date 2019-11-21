# -*- coding:utf-8 -*-
# @Author  : Clint

# 找到一个二进制位数与num相同但每一位都为1的数，
# 然后用这个数 减去 num。例如 0b111-0b101=0b10,7-5=2,这里7就是我们要找的数


def findComplement(num):
    i = 1
    # 最高位为1，其余为0，刚好比num大然后用这个数减去1就是我们要找的数
    while num >= i:
        i = i << 1  # 每次向左移1位 i=0b1000
    return i-1-num