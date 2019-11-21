# -*- coding:utf-8 -*-
# @Author  : Clint
# -*- coding:utf-8 -*-
# @Author  : Clint
x = -123


def reverse_num(num):
    if num > 0:
        a = len(str(num))         # a=3
        n = len(str(num))-1       # n=2
        sum = 0
        while n >= 0:
            s = num//10**n
            s = s * 10**(a-1-n)
            num = num % 10**n
            sum += s
            n -= 1
        if sum <= 2**31-1:
            return sum
        else:
            return 0
    else:
        num = abs(num)
        num = -reverse_num(num)
        if num >= -2**31:
            return num
        else:
            return 0


print(reverse_num(x))
