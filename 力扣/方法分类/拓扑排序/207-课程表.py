# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 
# @Thinking :
from typing import List
from collections import deque


class Solution:

    # 思想：该方法的每一步总是输出当前无前趋（即入度为零）的顶点
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        :type numCourses: int 课程门数
        :type prerequisites: List[List[int]] 课程与课程之间的关系
        :rtype: bool
        """
        # 课程的长度
        clen = len(prerequisites)
        if clen == 0: return True  # 没有课程，当然可以完成课程的学习

        # 步骤1：统计每个顶点的入度
        # 入度数组，记录了指向它的结点的个数，一开始全部为 0
        in_degrees = [0 for _ in range(numCourses)]
        # 邻接表，使用散列表是为了去重
        adj = [set() for _ in range(numCourses)]

        # 想要学习课程 0，你需要先完成课程1，我们用一个匹配来表示他们: [0,1]
        # [0, 1]表示1在先，0在后
        # 注意：邻接表存放的是后继 successor 结点的集合
        for second, first in prerequisites:
            in_degrees[second] += 1
            adj[first].add(second)

        # 步骤2：拓扑排序开始之前，先把所有入度为 0 的结点加入到一个队列中
        # 首先遍历一遍，把所有入度为 0 的结点都加入队列
        queue = deque()
        for i in range(numCourses):
            if in_degrees[i] == 0:
                queue.append(i)

        counter = 0
        while queue:
            top = queue.popleft()
