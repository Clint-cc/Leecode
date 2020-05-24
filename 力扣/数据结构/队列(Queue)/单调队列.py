# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 实现单调队列
# @Thinking :


from collections import deque

queue = deque()
queue.append(3)  # 队头插入元素
print(queue)
queue.appendleft(4)  # 队尾插入元素
print(queue)

print(queue[-1])
print(queue[0])

print(queue.pop())  # 删除队头元素
print(queue.popleft())  # 删除队头元素
