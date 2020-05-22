# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 给一个二叉树，请你返回其按层序遍历得到的节点值(即逐层地，从左到右访问所有节点)
# @Thinking :

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class Solution:
    def bfs_levelOrder(self, root):
        res = []
        queue = deque()
        queue.append(root)
        while queue:
            size = len(queue)
            level = []
            for _ in range(size):
                cur = queue.popleft()
                if not cur:
                    continue
                level.append(cur.val)
                queue.append(cur.left)
                queue.append(cur.right)
            if level:
                res.append(level)
        return res
