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
#
# l, r = map(int, input().split())
# cnt = 0
# for i in range(l, r + 1):
#     if ((1 + i) * i // 2) % 3 == 0:
#         cnt += 1
# print(cnt)
# class Solution:
#     def longestValidParentheses(self, s: str) -> int:
#         res = 0
#         stack = []
#         for subs in s:
#             if subs == '(':
#                 stack.append(subs)
#             elif subs == ')' and stack:
#                 stack.pop()
#                 res += 2
#         return res
#
# s = Solution()
# print(s.longestValidParentheses("(()(()))(("))
#
#
#
#
# from itertools import product
# s = '010101'
# for sub in product(s, repeat=3):
#     print(str(sub))
#     # print(''.join(x[0]+ x[1] for x in sub))
#     # yield tuple(sub)

# class Solution:
#     def hasAllCodes(self, s: str, k: int) -> bool:
#         n = len(s)
#         res = []
#         for i in range(n-k+1):
#             res.append(s[i:i+k])
#         print(res)
#
#         resset = set(res)
#         print(resset)
#         if len(resset) != 2**k:  # "00110001100011000110"
#             return False
#         else:
#             return True
#
#
# s = Solution()
#
# print(s.hasAllCodes("00110110", 2))
# print(s.hasAllCodes("00110", 2))
# print(s.hasAllCodes("0110", 2))
# print(s.hasAllCodes("0110", 1))
# print(s.hasAllCodes("0000000001011100", 4))

# "00110110"
# 2
# "00110"
# 2
# "0110"
# 1
# "0110"
# 2
# "0000000001011100"
# 4

a = [0] * 5
a[0] = [1, 3]
print(a)
