# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question :  房子排列成树的样子，相连接的房子不能同时被抢，求能抢到的最高金额
# @Thinking :

class Solution:
    def rob(self, root):
        return self.dp_helper(root)[1]

    # dp_helper函数返回一个节点为根的最大值 = [当前节点不参与计算的最大收益，当前节点的最大收益(参与/不参与)]
    def dp_helper(self, root):
        if root is None: return [0, 0]
        left_amount = self.dp_helper(root.left)  # 递归遍历左房子
        right_amount = self.dp_helper(root.right)  # 递归遍历右房子

        without_root = left_amount[1] + right_amount[1]  # 不抢根节点的房子
        with_root = root.val + left_amount[0] + right_amount[0]  # 抢根节点的房子

        return [without_root, max(with_root, without_root)]
