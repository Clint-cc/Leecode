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
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# l1 = ListNode(0)
# # l1 = ListNode(2)
# # l1.next = ListNode(4)
# # l1.next.next = ListNode(3)
# # l1.next.next.next = ListNode(None)
#
# l2 = ListNode(0)
# # l2 = ListNode(5)
# # l2.next = ListNode(6)
# # l2.next.next = ListNode(4)
# # l2.next.next.next = ListNode(None)
#
#
# # class Solution:
# #     def addTwoNumbers(self, l1: ListNode, l2: ListNode):
# #         s1, s2 = '', ''
# #         while l1:
# #             s1 += str(l1.val)
# #             l1 = l1.next
# #         num1 = int(s1[::-1])
# #
# #         while l2:
# #             s2 += str(l2.val)
# #             l2 = l2.next
# #         num2 = int(s2[::-1])
# #
# #         res = num1 + num2
# #
# #         result = ListNode(None)
# #         cur = result
# #         while res:
# #             cur.next = ListNode(res % 10)
# #             res = res // 10
# #             cur = cur.next
# #         return result.next
# #
# # s = Solution()
# # # print()
# # p = s.addTwoNumbers(l1, l2)
# # while p:
# #     print(p.val, end=' ')
# #     p = p.next
#
