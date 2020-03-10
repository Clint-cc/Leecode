# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 把字符串s中的每个空格替换成"%20"


class Solution:
    def replaceSpace(s):
        '''
            # 调用replace方法 (不推荐)
            def replaceSpace(s):
                return s.replace(" ", "%20")
        '''

        "# 遍历字符串"
        res = ''
        for i in s:
            if i != ' ':
                res += i
            else:
                res += "%20"
        return res


print(Solution.replaceSpace("we are you "))
