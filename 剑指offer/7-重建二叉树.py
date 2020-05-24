# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 面试题07. 输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。假设输入的前序遍历
#             和中序遍历的结果中都不含重复的数字。
# @Thinking :
class Solution:
    def buildTree(self, preorder, inorder):
        '''
        思路：递归问题
        :param preorder:
        :param inorder:
        :return:
        '''
        self.dic = {}
        self.po = preorder
        for i in range(len(inorder)):
            self.dic[inorder[i]] = i

        return self.recur(0, 0, len(inorder) - 1)

    def recur(self, pre_root, in_left, in_right):
        if in_left > in_right:
            return

        root = TreeNode(self.po[pre_root])
        i = self.dic[self.po[pre_root]]
        root.left = self.recur(pre_root + 1, in_left, i - 1)
        root.right = self.recur(i - in_left + pre_root + 1, i + 1, in_right)
        return root


s = Solution()
print(s.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7]))
