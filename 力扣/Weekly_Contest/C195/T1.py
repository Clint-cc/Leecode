# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 
# @Thinking :


class Solution:
    def isPathCrossing(self, path: str) -> bool:
        paths = [[0, 0], ]

        # [[0,0], [0,1],[]]
        for p in path:
            if p == 'N':
                qd[1] += 1
                if qd not in paths:
                    paths.append(qd)
                else:
                    return True
            elif p == 'S':
                qd[1] -= 1
                if qd not in paths:
                    paths.append(qd)
                else:
                    return True
            elif p == 'E':
                qd[0] += 1
                if qd not in paths:
                    paths.append(qd)
                else:
                    return True
            else:
                qd[0] -= 1
                if qd not in paths:
                    paths.append(qd)
                else:
                    return True
        return False


s = Solution()
print(s.isPathCrossing("NES"))
