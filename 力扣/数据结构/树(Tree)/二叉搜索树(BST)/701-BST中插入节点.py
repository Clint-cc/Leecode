# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 给定二叉搜索树（BST）的根节点和要插入树中的值，将值插入二叉搜索树。
#             返回插入后二叉搜索树的根节点。 保证原始二叉搜索树中不存在新值。
# @Thinking :


class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        # 找到空位置插入新节点
        if not root:
            return TreeNode(val)
        # if root.val == val:
        # BST中一般不会插入已存在的元素
        if root.val < val:
            root.right = self.insertIntoBST(root.right, val)
        elif root.val > val:
            root.left = self.insertIntoBST(root.left, val)
        return root
