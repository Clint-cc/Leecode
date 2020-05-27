# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : test_file
#
# favoriteCompanies = [["leetcode"],["google"],["facebook"],["amazon"]]
# a = ["leetcode"]
# b = ["google", "leetcode"]
# # print(b.s)


# a = 1  # 对象 1 被 变量a引用，对象1的引用计数器为1
# b = a  # 对象1 被变量b引用，对象1的引用计数器加1
# c = a  # 1对象1 被变量c引用，对象1的引用计数器加1
# del a  # 删除变量a，解除a对1的引用
# del b  # 删除变量b，解除b对1的引用
# print(a)
# print(b)
# print(c)  # 最终变量c仍然引用1


# nums = list(map(int, input().split()))
# print(nums)

l, r = map(int, input().split())
cnt = 0
for i in range(l, r + 1):
    if ((1 + i) * i // 2) % 3 == 0:
        cnt += 1
print(cnt)
