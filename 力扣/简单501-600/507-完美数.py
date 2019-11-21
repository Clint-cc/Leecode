# -*- coding:utf-8 -*-
# @Author  : Clint
# 56 = 1+2+4+7+8+14+28
import math

def checkperfnum(num):
    k = [1, ]
    for i in range(2, int(math.sqrt(num))+1):
        a, b = divmod(num, i)
        if b == 0:
            k.append(i)
            k.append(a)
        else:
            continue
    print(k)
    if sum(k) == num:
        return True
    else:
        return False


print(checkperfnum(6))
