# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。
# @Thinking :

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        if abs(self.maxDepth(root.left) - self.maxDepth(root.right)) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    # 结合求子树的最大深度
    def maxDepth(self, root: TreeNode) -> int:
        if not root: return 0
        from collections import deque
        queue = deque()
        queue.append((1, root))  # 初始化深度为0
        max_depth = 1  # 初始化最大深度为0

        while queue:
            cur_depth, node = queue.pop()
            if not node.left and not node.right:
                max_depth = max(cur_depth, max_depth)
            if node.left:
                queue.append((cur_depth + 1, node.left))
            if node.right:
                queue.append((cur_depth + 1, node.right))
        return max_depth
