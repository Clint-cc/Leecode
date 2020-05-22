# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 
# @Thinking :


class Solution:
    def isValidBST(self, root):
        import math
        ma, mi = math.inf, -math.inf
        return self.isValidBST2(root, ma, mi)

    def isValidBST2(self, root, max_val, min_val):
        if not root: return True
        if root.val <= min_val:
            return False
        elif root.val >= max_val:
            return False
        return self.isValidBST2(root.left, root.val, min_val) and self.isValidBST2(root.right, max_val, root.val)
