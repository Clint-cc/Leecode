# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 给定单向链表的头指针和一个要删除的节点的值，定义一个函数删除该节点。返回删除后的链表的头节点
# @Thinking :


class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if not head: return
        pre = head
        while pre:
            if pre.val == val:
                return head.next
            if pre.next.val == val:
                pre.next = pre.next.next
                return head
            pre = pre.next
        return head
