# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 
# @Thinking :

class Solution:
    def recoverFromPreorder(self, S: str):
        # preroot = TreeNode(None)
        # if not s: return preroot
        stack = []
        stack.append(S[0])
        from collections import defaultdict
        dicts = defaultdict(list)
        i = 1
        while i < len(S):
            d = 0
            while S[i] == '-':
                d += 1
                i += 1
            dicts[d].append(S[i])
            i += 1
        return dicts


s = Solution()
print(s.recoverFromPreorder("1-2--3---4-5--6---7"))

# [1,2,3,4,null,null,5,6,7,nul,null]
