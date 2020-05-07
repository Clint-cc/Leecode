# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question :

# def mirrorTree(root:TreeNode) -> TreeNode:
#     if not root:
#         return
#     root.left, root.right = mirrorTree(root.right), mirrorTree(root.left)
#     return root

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if root:
            root.left, root.right = self.mirrorTree(root.right), self.mirrorTree(root.left)
        return root


print(Solution.mirrorTree([4, 2, 7, 1, 3, 6, 9]))
