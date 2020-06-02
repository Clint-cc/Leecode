# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 
# @Thinking :


class Solution:
    def minReorder(self, n, connections):
        res = 0
        connections.sort(key=lambda x: (x[0], x[1]))
        print(connections)
        ordered_set = {0}  # 保存已经能正确到达0的城市
        for (l, r) in connections:
            if r in ordered_set:  # r是已经能到0的城市，那么l->r后就可到0
                ordered_set.add(l)
            elif l in ordered_set:  # r目前不可到城市0，l可到，那就让r->l后到0，重修+1
                res += 1
                ordered_set.add(r)
        return res


s = {'s': 0, 'c': 9}
print(type(s))
