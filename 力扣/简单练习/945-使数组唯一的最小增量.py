# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 给定整数数组 A，每次 move 操作将会选择任意 A[i]，并将其递增 1。
#             返回使 A 中的每个值都是唯一的最少操作次数。


'''
# 超出时间限制
def minIncrementForUnique(A):
    tmpA = sorted(A)
    count = 0
    for i in range(1,len(tmpA)):
        while tmpA[i] <= tmpA[i-1]:
            tmpA[i] += 1
            count += 1
    return count

print(minIncrementForUnique([3,2,1,2,1,7]))
'''


def minIncrementForUnique(A):
    A.sort()
    count = 0
    for i in range(1, len(A)):
        if A[i] <= A[i - 1]:
            count += A[i - 1] - A[i] + 1
            A[i] = A[i - 1] + 1
    return count


print(minIncrementForUnique([3, 2, 1, 2, 1, 7]))
