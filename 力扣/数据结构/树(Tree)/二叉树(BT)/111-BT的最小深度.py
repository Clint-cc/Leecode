# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 
# @Thinking :
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def bfs_minDepth(self, root):  # bfs
        if not root: return 0
        queue = deque()  # 新建队列
        queue.append((1, root))  # root节点开始算1层，所以初始化1
        while queue:
            depth, node = queue.pop()
            if node.left is None and node.right is None:
                return depth
            if node.left:
                queue.append((depth + 1, node.left))
            if node.right:
                queue.append((depth + 1, node.right))

    class Solution:
        def dfs_minDepth(self, root):  # dfs
            if not root: return 0
            stack = [(1, root)]
            min_depth = float('inf')
            while stack:
                depth, node = stack.pop()
                if not node.left and not node.right:
                    min_depth = min(min_depth, depth)

                if node.right:
                    stack.append((depth + 1, node.right))
                if node.left:
                    stack.append((depth + 1, node.left))
            return min_depth


s = Solution()
print(s.bfs_minDepth())
