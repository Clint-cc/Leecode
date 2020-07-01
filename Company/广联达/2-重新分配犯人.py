# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : N个监狱房间N个犯人，重新分配犯人，要求原相邻犯人分配后不在原房间且不相邻，列出所有
#             可能，如1234，分配后2413，3142。
# @Thinking :  dfs、回溯


class Solution:
    def Allocate_Rooms(self, n):
        res = []

        def backTrack(n, track):
            # 满足条件 返回
            if n == len(track):
                # for i in range(0,len(track)):
                #     if i+1 == int(track[i]):
                #         return

                res.append(track)
                return

            for i in range(1, n + 1):
                if not track and i == 1:  # 第一个人不能再第一个房间
                    continue
                if str(i) in track:  # 访问后的人
                    continue
                if i == len(track) + 1:  # 当前位置，不能是之前对应的人
                    continue
                if track and abs(i - int(track[-1])) <= 1:
                    continue
                backTrack(n, track + str(i))

        backTrack(n, '')
        return res

s = Solution()
print(s.Allocate_Rooms(5))
