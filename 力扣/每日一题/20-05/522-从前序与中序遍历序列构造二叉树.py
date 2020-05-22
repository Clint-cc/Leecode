# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 根据一棵树的前序遍历与中序遍历构造二叉树。
# @Thinking :


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:  return
        root = TreeNode(preorder[0])
        idx = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1:1 + idx], inorder[:idx])
        root.right = self.buildTree(preorder[1 + idx:], inorder[idx + 1:])
        return root
