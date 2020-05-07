# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question :


def maxDistance(grid):
    import queue
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    queue_s = queue.Queue()
    m, n = len(grid), len(grid[0])

    # 把所有的陆地入队
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                queue_s.put((i, j))

    # 从各个陆地一圈一圈的遍历海洋，最后遍历到海洋的就是离陆地最远的海洋。
    has_Ocean = False
    point = []
    while not queue_s.empty():
        point = queue_s.get()
        x, y = point[0], point[1]
        # 取出队列的元素，将其四周的海洋入队
        for i in range(4):
            newX = x + dx[i]
            newY = y + dy[i]
            if newX < 0 or newX >= m or newY < 0 or newY >= n or grid[newX][newY] != 0:
                continue
            grid[newX][newY] = grid[x][y] + 1
            has_Ocean = True
            queue_s.put((newX, newY))

    # 没有陆地或者没有海洋，返回-1
    if not point or not has_Ocean:
        return -1

    # 没有最后一次遍历到的海洋的距离
    return grid[point[0]][point[1]] - 1


print(maxDistance([[1, 0, 0],
                   [0, 0, 0],
                   [0, 0, 0]]
                  )
      )
