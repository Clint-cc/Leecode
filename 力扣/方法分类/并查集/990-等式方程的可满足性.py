# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 
# @Thinking :


class Solution(object):
    def equationsPossible(self, equations):
        """
        :type equations: List[str]
        :rtype: bool
        """
        forestTree = list(range(26))

        def find(p):
            while forestTree[p] != p:
                p = forestTree[p]
            return p

        height = [1] * 26
        test = []

        for eq in equations:
            c1, c2 = ord(eq[0]) - ord('a'), ord(eq[3]) - ord('a')
            if eq[1] == '=':
                r1 = find(c1)
                r2 = find(c2)
                if r1 == r2: continue
                # 测试数据量应该很小，路径压缩没什么提升
                if height[r1] < height[r2]:
                    forestTree[r1] = forestTree[r2]
                elif height[r2] < height[r1]:
                    forestTree[r2] = forestTree[r1]
                else:
                    forestTree[r2] = forestTree[r1]
                    height[r1] += 1
            else:
                test.append([c1, c2])
        for i, j in test:
            if find(i) == find(j): return False
        return True


s = Solution()
print(s.equationsPossible(["a==b", "b!=c", "c==a"]))
