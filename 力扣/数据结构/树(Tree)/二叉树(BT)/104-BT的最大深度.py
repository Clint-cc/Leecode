# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 
# @Thinking :

class Solution:
    def maxDepth(self, root):
        # 非递归dfs
        # from collections import deque
        # if not root: return 0
        # queue = deque()  # 新建队列
        # queue.append((1, root))  # 初始化, 根非空深度至少是1
        # max_depth = 1  # 初始化最大深度为1
        # while queue:
        #     cur_depth, node = queue.popleft()
        #     if not node.left and not node.right:
        #         max_depth = max(cur_depth, max_depth)
        #     if node.left:
        #         queue.append((cur_depth + 1, node.left))
        #     if node.right:
        #         queue.append((cur_depth + 1, node.right))
        # return max_depth

        # 递归两行搞定
        if not root: return 0
        return max(1 + self.maxDepth(root.left), 1 + self.maxDepth(root.right))
