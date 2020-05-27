# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 
# @Thinking :

n, x = map(int, input().split())
res = []
for i in range(n):
    a, b = map(int, input().split())
    # print(a, b)
    res.append([a, b])
# n, x, res = 3, 4, [[1,2], [2,3], [3,4]]

ans = 0
for i in range(n):
    if ans + res[i][0] + res[i][1] > x:
        ans += res[i][0] + res[i][1] - x

print(ans)
