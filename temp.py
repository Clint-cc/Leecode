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
# #
# def findMaxLength(nums):
#     s_sum = 0
#     total_sum = [0]
#     for num in nums:
#         if num != 0:
#             s_sum += 1
#             total_sum.append(s_sum)
#         else:
#             s_sum -= 1
#             total_sum.append(s_sum)
#     return total_sum
#
# print(findMaxLength([0,0,1,0,0,0,1,1]))


# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         snum = ""
#         for st in s:
#             if st.isalpha():
#                 snum += st
#         snum = snum.upper()
#         i, j = 0, len(snum) - 1
#         while i < j:
#             if snum[i] != snum[j]:
#                 return False
#             i += 1
#             j -= 1
#         return True
#
#
# s = Solution()
# print(s.isPalindrome("A man, a plan, a canal: Panama"))
# print(s.isPalindrome("race a car"))


# def sift(data_list, low, high):
#     i = low         # 最开始的父节点
#     j = 2*i+1       # 最开始的左子节点
#     tmp = data_list[i]
#     while j < high:    # 如果子节点没到子树的最后，那么继续
#         if data_list[j] < data_list[j+1] and j+1 <= high:
#             j += 1
#         if tmp < data_list[j]:   # 如果父节点比子节点小
#             data_list[i] = data_list[j]   # 那么父子节点互换
#             i = j                # 字节点成为父节点
#             j = 2*i+1            # 新子节点
#         else:
#             break
#     data_list[i] = tmp
#
#
# def heap_sort(data_list):
#     n = len(data_list)
#     for i in range(n//2 - 1, -1, -1):
#         sift(data_list, i, n-1)
#     # 堆建好了
#     for i in range(n-1, -1, -1):    # i指向堆的最后
#         data_list[0], data_list[i] = data_list[i], data_list[0]     # 父节点出局，堆的最后叶子节点上位
#         sift(data_list, 0, i-1)     # 调整出新的父节点
#
# data = [0, 1, 1, 1, 2, 3]
# heap_sort(data)
# print(data)  # 升序排列，若要降序排列，则建小根堆即


from collections import Counter

s = 'abc'
dict = Counter(s)

print(dict['d'])
