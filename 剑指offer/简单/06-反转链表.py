# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。


class Node(object):
    def __init__(self, head):
        self.val = head
        self.next = None


def reversePrint(head):
    if head == Node or head.next == Node:
        return head

    pre = None
    next = None
    while (head != None):
        next = head.next
        head.next = pre
        pre = head
        head = next
    return pre


if __name__ == "__main__":
    l1 = Node(3)
    l1.next = Node(2)
    l1.next.next = Node(1)
    l = reversePrint(l1)
    print(l.next)
