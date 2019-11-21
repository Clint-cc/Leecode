# -*- coding:utf-8 -*-
# @Author  : Clint


def guess(x):
    pick = 6
    if x > pick:
        return 1  # 选的数大了
    elif x < pick:
        return -1  # 选的数小了
    else:
        return 0  # 选对了


def guessNumber(n):
    left = 1
    right = n
    while left <= right:

        mid = (left + right) // 2
        if guess(mid) == -1:
            left = mid + 1
        elif guess(mid) == 1:
            right = mid - 1
        else:
            return mid
            break


print(guessNumber(10))
