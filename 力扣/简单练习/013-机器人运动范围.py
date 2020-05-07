# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question :

def movingCount(m, n, k):  # BFS
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # 移动方向
    res = 1
    checked = {(0, 0)}
    q = [(0, 0)]  # BFS和先后顺序有关的(如最短路径等),就用队列deque(), 如果和先后顺序无关
    # 的(如只要求走遍能走的),用list.pop()也一样,都是O(1).

    while q:
        x, y = q.pop()
        for i, j in moves:
            new_x = x + i
            new_y = y + j
            if 0 <= new_x < m and 0 <= new_y < n and (new_x, new_y) not in checked:
                if sum(int(i) for i in str(new_x) + str(new_y)) <= k:
                    checked.add((new_x, new_y))
                    q.append((new_x, new_y))
                    res += 1
    return res


print(movingCount(20, 20, 6))
