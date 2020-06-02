# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 
# @Thinking :

'''
迭代的话，需要借助栈来进行
'''


class Solution:
    # 前序
    def preOrder(self, root):
        stack, res = [], []
        stack, append(root)
        if not root: return res
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:  # 注意这里需要判断子节点是否为空
                stack.append(node.right)  # 由于栈先进后出，所以先将右子树入栈
            if node.left:
                stack.append(node.left)
        return res

    # 中序
    def inOrder(self, root):
        stack, res = [], []
        if not root: return res
        stack.append(root)
        while True:
            while root:
                root = root.left
            if not stack: return res
            root = stack.pop()
            res.append(root.val)
            root = root.right

    # 后序
    def postOrder(self, root):
        stack, res = [], []
        stack, append(root)
        while stack:
            node = stack.pop()
            stack.append(node.left)  # 由于栈先进后出，所以先将右子树入栈
            stack.append(node.right)
            res.append(node.val)
        return res[::-1]

    # 迭代的模板：
    class Solution:
        def preOrder(self, root):
            if not root: return []
            cur, stack, res = root, [], []
            while cur or stack:
                while cur:
                    res.append(cur.val)  # 前序/后序，先加入结果
                    stack.append(cur)
                    cur = cur.left  # 前序，到达最左边
                    # cur = cur.right  # 后序，到达最右端
                node = stack.pop()
                # res.append(cur.val)  # 中序，出栈时加入结果
                cur = node.right
                # cur = node.right  # 后序，先从右端遍历
            return res
            # return res[::-1] # 后序需要倒置
