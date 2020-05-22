# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 
# @Thinking : 需注意特殊的二叉树计算节点方式

'''
    # 完全二叉树：每⼀层都是紧凑靠左排列的
    # 满二叉树：每层都是是满的，像⼀个稳定的三⾓形
'''


class Solution:
    # 普通二叉树计算节点
    def countNodes(self, root):
        if not root: return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    # 满二叉树计算节点，（和高度有关）
    def man_countNodes(self, root):
        h = 0
        while root:
            root = root.left
            h += 1
        return pow(2, h) - 1

    # 完全二叉树计算节点，算是普通二叉树和完全二叉树的结合版
    def wq_countNodes(self, root):  # O(logN*logN)
        l, r = root, root
        hl, hr = 0, 0  # 记录左右子树的高度
        while l:
            l = l.left
            hl += 1
        while r:
            r = r.right
            hr += 1
        if hl == hr:  # 如果左右⼦树的⾼度相同，则是⼀棵满⼆叉树
            return pow(2, hl) - 1
        # 如果左右⾼度不同，则按照普通⼆叉树的逻辑计算
        return 1 + wq_countNodes(root.left) + wq_countNodes(root.right);
