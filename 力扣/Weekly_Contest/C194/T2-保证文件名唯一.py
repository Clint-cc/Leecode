# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 创建不同名的文件夹
# @Thinking :
# Eaxmples：
'''
    in: ["pes","fifa","gta","pes(2019)"]        out: ["pes","fifa","gta","pes(2019)"]
    in: ["gta","gta(1)","gta","avalon"]         out: ["gta","gta(1)","gta(2)","avalon"]
    in: ["onep","onep(1)","onep(2)","onep(3)","onep"]   out: ["onep","onep(1)","onep(2)","onep(3)","onep(4)"]
    in: ["kaido","kaido(1)","kaido","kaido(1)"]         out: ["kaido","kaido(1)","kaido(2)","kaido(1)(1)"]
'''


class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        from collections import defaultdict
        res = defaultdict(list)
        ans = []
        for i in range(len(names)):
            if names[i] not in res:
                ans.append(names[i])
                res[names[i]].append(0)
            else:
                res[names[i]].append(res[names[i]][-1] + 1)
                while names[i] + "(" + str(res[names[i]][-1]) + ")" in res:
                    res[names[i]].append(res[names[i]][-1] + 1)

                ans.append(names[i] + "(" + str(res[names[i]][-1]) + ")")
                res[ans[-1]].append(0)
        return ans
