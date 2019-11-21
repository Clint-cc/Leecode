# -*- coding:utf-8 -*-
# @Author  : Clint


def gene(numRows):
    r = []
    for i in range(numRows):
        r.append([1]+[sum(r[-1][j:j+2]) for j in range(i)])
    return r


print(gene(3))


# 方法二
'''
def tri(max):
    b = [1, ]                           # 第0行固定是[1]
    for i in range(max):                # 循环每一行
        yield b
        c = []                          # 初始化一个list c
        for j in range(i + 1):          # 第n行固定有n+1个数
            if j < i:                   # 上一行最多只有n个数，所以b[n+1]不存在
                c += [b[j] + b[j + 1]]  # 除开头尾两个[1],其余的数都是上一行两两相加
        b = [1, ] + c + [1, ]           # 加上头尾两个[1]
    return 'done'

'''