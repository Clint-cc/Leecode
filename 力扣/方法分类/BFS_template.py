# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : BFS模板
# @Thinking : 问题的本质都是让在一副图中找到从起点start到终点target的最近距离；


# 粗代码：
def BFS(self, start: TreeNode, target: TreeNode):  # 计算从satrt到target的距离
    from collections import deque
    queue = deque()  # 新建队列
    visited = []  # 避免走回头路，有的地方不需要，如树，因为没有子节点到父节点的指针

    queue.append(start)  # 将起点加入队列
    visited.append(start)  # 访问过的记录起来，避免重复访问
    step = 0  # 记录扩散的步数，如果是树，就是扩散的深度depth
    while queue:
        size = len(queue)  # 队列中节点的个数
        for _ in range(size):  # 将当前队列的所有节点想四周扩散
            cur_node = queue.popleft()  # 横向依次取出各节点
            if cur_node is target:  # 重点：这里判断是否抵达终点
                return step
            for x in cur_node.相邻节点:  # 遍历cur的相邻节点
                if x:  # 节点不为空就加入队列
                    queue.append(x)
                if x not in visited:
                    visited.append(x)
        depth += 1  # 横向遍历完一次，更新步数
