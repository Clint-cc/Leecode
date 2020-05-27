# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 
# @Thinking :


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1: return l2  # 递归结束的条件
        if not l2: return l1

        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


LN1 = ListNode(1)
LN1.next = ListNode(2)
LN1.next.next = ListNode(3)

LN2 = ListNode(1)
LN2.next = ListNode(3)
LN2.next.next = ListNode(4)

solve = Solution()
merged_Node = solve.mergeTwoLists(LN1, LN2)  # 合并后的链表

from PrintLinkedNode import printLN

prLN = printLN()

prLN.printLinkedNode(merged_Node)
