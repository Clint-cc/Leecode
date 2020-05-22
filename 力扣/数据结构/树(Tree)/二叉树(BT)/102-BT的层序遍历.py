# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 给一个二叉树，请你返回其按层序遍历得到的节点值(即逐层地，从左到右访问所有节点)
# @Thinking :

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        self.dfs(root, res, 0)
        return res

    def dfs(self, root, res, depth):
        if not root:
            return
        if len(res) == depth:
            res.append([])
        res[depth].append(root.val)

        if root.left is not None:
            self.dfs(root.left, res, depth + 1)
        if root.right is not None:
            self.dfs(root.right, res, depth + 1)
        # return tmp
