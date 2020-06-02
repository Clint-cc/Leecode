# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 
# @Thinking :

# 先序、中序、后序三种遍历方法，如果是DFS的话，模板高度统一，
# 哪种遍历方式取决于将root.val放入res的是顺序
class Solution:
    # 先序
    def preOrder(self, root):
        res = []

        def dfs(root):
            if not root: return
            res.append(root.val)  # 将root.val放入res中
            dfs(root.left)  # 左
            dfs(root.right)  # 右

        dfs(root)
        return res

    # 中序
    def inOrder(self, root):
        res = []

        def dfs(root):
            if not root: return
            dfs(root.left)  # 左
            res.append(root.val)  # 将root.val放入res中
            dfs(root.right)  # 右

        dfs(root)
        return res

    # 后序
    def postOrder(self, root):
        res = []

        def dfs(root):
            if not root: return
            dfs(root.left)  # 左
            dfs(root.right)  # 右
            res.append(root.val)  # 将root.val放入res中

        dfs(root)
        return res
