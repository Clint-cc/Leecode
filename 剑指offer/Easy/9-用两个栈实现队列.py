# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 双栈实现队列
# @Thinking :


class CQueue:
    def __init__(self):
        self.stack1, self.stack2 = [], []

    def appendTail(self, value: int) -> None:  # 填元素到队尾
        self.stack1.append(value)
        return

    def deleteHead(self) -> int:  # 删除队头元素并返回
        # 队头有元素则返回
        if self.stack2: return self.stack2.pop()
        # 队尾无元素，则删除
        if not self.stack1: return -1
        # 队尾有元素，加到队头
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        return self.stack2.pop()
