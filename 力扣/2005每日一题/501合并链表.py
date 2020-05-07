# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question :
# [1,2,4,6], [2,3,7]

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 and l2:
            if l1.val > l2.val: l1, l2 = l2, l1
            l1.next = self.mergeTwoLists(l1.next, l2)

        curr = ListNode
        res = curr.val
        while l1.next:
            res = f'{res}->{res.next.val}'
        return res


s = Solution()
a = ListNode(1)
a.next = ListNode(2)
a.next.next = ListNode(4)

b = ListNode(1)
b.next = ListNode(3)
b.next.next = ListNode(4)

print(s.mergeTwoLists(a, b))
