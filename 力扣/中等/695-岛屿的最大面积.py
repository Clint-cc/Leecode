# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 给定一个包含了一些0和1的非空二维数组 grid , 一个岛屿是由四个方向 (水平或垂直)
#             的 1 (代表土地) 构成的组合。你可以假设二维矩阵的四个边缘都被水包围着。


def maxAreaOfIsland(grid):
    '''
    官方思路：DFS，关键点：为确保每个土地访问不超过一次，每进过一块土地，将其重置为0
    :param grid:
    :return:
    '''
    max_area = 0
    for i, x in enumerate(grid):
        for j, y in enumerate(x):
            max_area = max((dfs(grid, i, j)), max_area)

    return max_area


def dfs(grid, cur_i, cur_j):
    if cur_i < 0 or cur_j < 0 or cur_i == len(grid) or cur_j == len(grid[0]) or grid[cur_i][cur_j] != 1:
        return 0
    grid[cur_i][cur_j] = 0  # 访问当前节点后重置为0
    max_area = 1
    for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:  # 当前节点的前后左右节点
        next_i, next_j = cur_i + di, cur_j + dj
        max_area += dfs(grid, next_i, next_j)

    return max_area


print(maxAreaOfIsland([[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                       [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                       [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]))
