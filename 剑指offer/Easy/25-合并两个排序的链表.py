# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 
# @Thinking :

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        elif not l2:
            return l1

        p = None
        if l1.val <= l2.val:
            p = l1
            p.next = self.mergeTwoLists(l1.next, l2)
        else:
            p = l2
            p.next = self.mergeTwoLists(l1, l2.next)
        return p
