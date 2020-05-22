# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 给定一个二叉搜索树的根节点 root 和一个值 key，删除二叉搜索树中的 key 对应的节点。
# @Thinking :

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root: return None  # 空树处理
        # 找到节点位置就删除节点
        if root.val == key:
            # 删除操作
            # 情况1和2
            if root.left == None: return root.right
            if root.right == None: return root.left

            # 情况3
            if root.left != None and root.right != None:
                min_node = self.getMin(root.right)
                root.val = min_node.val  # 把当前 root 改成 minNode
                root.right = self.deleteNode(root.right, min_node.val)  # 删除minNode

        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        return root

    def getMin(self, node):
        while node != None:
            node = node.left
        return node
