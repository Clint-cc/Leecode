# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 给定两个非空二叉树 s 和 t，检验 s 中是否包含和 t 具有相同结构和节点值的子树。s 的一个子树包括 s 的一个
#             节点和这个节点的所有子孙。s 也可以看做它自身的一棵子树。
# @Thinking : 需要编写一个函数判断s中某个节点所对应的子树是否和t完全相同。如果s和t直接满足了相同的条件就直接返回，否则
#             递归求解 s 的左右子树是否含有和 t 相同的结构

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isSameTree(self, a, b):
        if not a and not b:
            return True
        if not a or not b:
            return False
        # 证明两树相等的三个条件：当前node值相等，各自左右子树也对于相等
        return a.val == b.val and self.isSameTree(a.left, b.left) \
               and self.isSameTree(a.right, b.right)

    def isSubTree(self, s, t):
        if not s:  # 判断s是否为空
            return False

        if self.isSameTree(s, t):
            return True

        return self.isSameTree(s.left, t) or self.isSameTree(s.right, t)
