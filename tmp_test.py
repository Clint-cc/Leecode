# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : test_file

class TreeNode:
    """
    二叉树的结点
    """

    def __init__(self, x):
        self.val = x  # 结点值
        self.left = None  # 左孩子
        self.right = None  # 右孩子


'''from functools import reduce
# def count1(x):
#     cnt = 0
#     while x:
#         x &= x - 1
#         cnt += 1
#     return cnt
# print(count1(16))

# print(sorted([1,3,5,7,8],key=lambda x:(bin(x).count('1'))
# #             )
# #      )

# print(reduce(lambda x,y:x+y, range(1,101)))

# people = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
# dict = {}
# for p in people:
#     dict.setdefault(p[0],[])
#     # dict[p[0]].append(p[1])
#
# print(dict)

# import random
#
# nums = []
# for i in range(10):
#     nums.append(i)
# random.shuffle(nums)
# print(nums)
#
# day = [1,2,3,4,5]
# days = {*day}
# print(days)

#
# for k in {'a':1,'2':3,'b':1,'c':2,'d':1}:
#     print(k, end=' ')

a = [1,2,3,4,1]
a.remove(1)
print(a)
'''


def create_tree(nodes):
    """
    根据列表构建一棵二叉树
    :param nodes: 层次遍历序列
    :return: 二叉树的根节点
    """

    def helper(node, i):  # 用列表递归创建二叉树，

        if i < len(nodes):  # 当下标索引满足条件时
            if nodes[i] in ['#', None]:  # 如果列表中下标为i的结点为空
                return None  # 返回None
            else:
                node = TreeNode(nodes[i])  # 构建当前结点
                node.left = helper(node.left, 2 * i + 1)  # 构建左子树，通过下标查找
                node.right = helper(node.right, 2 * i + 2)  # 构建右子树，通过下标查找
                return node  # 返回根节点为下标为i的元素的子树
        return node  # 返回根节点

    root = TreeNode(0)  # 临时结点
    root = helper(root, 0)  # 建立树
    return root


print(create_tree(root=TreeNode(4,
                                TreeNode(2, TreeNode(1), TreeNode(3)),
                                TreeNode(7, TreeNode(6), TreeNode(8))
                                )))
