# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : N个监狱房间N个犯人，重新分配犯人，要求原相邻犯人分配后不在原房间且不相邻，列出所有
#             可能，如1234，分配后2413，3142。
# @Thinking :  dfs

class Solution:
    def Allocate_Rooms(self, n):
        res = []
        self.dfs(res, n, '')
        return res

    def dfs(self, res, n, s_room):
        if len(s_room) == n:
            res.append(s_room)
            return

        i = 1
        while i < n + 1:
            if not s_room:
                i += 1
                s_room.join(str(i))
                continue
                # self.dfs(res, n, s_room + str(i))
            elif abs(i - int(s_room[-1])) > 1 and i != (len(s_room) + 1):
                self.dfs(res, n, s_room + str(i))
            else:
                i += 1


s = Solution()
print(s.Allocate_Rooms(4))
