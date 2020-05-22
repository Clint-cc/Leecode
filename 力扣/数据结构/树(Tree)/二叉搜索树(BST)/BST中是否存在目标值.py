# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 判断一个目标数是否在BST中
# @Thinking : 进阶方法是利用好BST左小右大

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Is_In_BST(self, root, target):
        # 1\一般方法，逐个遍历
        if not root: return False
        if root.val == target: return True
        return self.Is_In_BST(root.left, target) or self.Is_In_BST(root.right, target)

        # 2\利用BST，左小右大特性
        if not root: return False
        if root.val == target:
            return True
        elif root.val < target:
            return self.Is_In_BST(root.right, target)
        elif root.val > target:
            self.Is_In_BST(root.left, target)
