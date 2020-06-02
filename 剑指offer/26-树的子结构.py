# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 
# @Thinking :


class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        res = False
        if A and B:
            if A.val == B.val:
                res = self.is_SubTree(A, B)
            if not res:
                res = self.isSubStructure(A.left, B)
            if not res:
                res = self.isSubStructure(A.right, B)
        return res

    def is_SubTree(self, A, B) -> bool:
        # cura, curb = A, B
        # while curb:
        #     if curb.val != cura.val:
        #         return False
        #     return self.is_SubTree(cura.left, curb.left) and self.is_SubTree(cura.right, curb.right)
        # return True
        if not B:
            return True
        if not A:
            return False
        if A.val != B.val:
            return False
        return self.is_SubTree(A.left, B.left) and self.is_SubTree(A.right, B.right)
