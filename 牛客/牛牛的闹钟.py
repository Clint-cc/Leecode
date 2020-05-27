# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 
# @Thinking :

n = int(input())
num = []
for i in range(n):
    h, m = map(int, input().split())
    num.append([h, m])
x = int(input())
ch, cm = map(int, input().split())

import math

res = -math.inf
for i in range(3):
    if num[i][0] * 60 + num[i][1] <= ch * 60 + cm - x:
        res = max(num[i][0] * 60 + num[i][1], res)

print(res // 60, res % 60)
