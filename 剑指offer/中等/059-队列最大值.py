# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 定义一个队列并实现函数max_value得到队列里的最大值，
#             要求函数max_value、push_back 和 pop_front 的时间复杂度都是O(1)。


class MaxQueue:

    def __init__(self):
        from collections import deque
        self.que = deque()
        self.sort_que = deque()

    def max_value(self):
        """
        :rtype: int
        """
        return self.sort_que[0] if self.sort_que else -1

    def push_back(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.que.append(value)
        while self.sort_que and self.sort_que[-1] < value:
            self.sort_que.pop()
        self.sort_que.append(value)

    def pop_front(self):
        """
        :rtype: int
        """
        if not self.que: return -1
        res = self.que.popleft()
        if res == self.sort_que[0]:
            self.sort_que.popleft()
        return res
