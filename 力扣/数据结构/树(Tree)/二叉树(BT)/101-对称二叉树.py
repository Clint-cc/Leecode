# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 给定一个二叉树，检查它是否是镜像对称的。
# @Thinking :  能想到递归，一定用递归

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.l_r_Symmetric(root, root)

    def l_r_Symmetric(self, l_root, r_root):
        if not l_root and not r_root:
            return True
        elif not l_root or not r_root:
            return False

        if l_root.val == r_root.val:
            return self.l_r_Symmetric(l_root.left, r_root.right) and \
                   self.l_r_Symmetric(l_root.right, r_root.left)
