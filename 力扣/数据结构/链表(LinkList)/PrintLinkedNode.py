# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question :   # 打印链表
# @Thinking :


class PrintLN:
    def printLinkedNode(self, Node):
        LN_to_Array = []
        while Node:
            LN_to_Array.append(Node.val)
            Node = Node.next
        print(LN_to_Array)
