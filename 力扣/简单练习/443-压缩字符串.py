# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 
# @Thinking :
class Solution:
    def compress(self, chars):  # ["a","a","a","a","a","b","b","c","c","c","c","c","c","c","c","c","c","c","c"]
        anchor = write = 0
        for read, c in enumerate(chars):
            if read + 1 == len(chars) or chars[read + 1] != c:
                chars[write] = chars[anchor]
                write += 1
                if read > anchor:
                    for digit in str(read - anchor + 1):
                        chars[write] = digit
                        write += 1
                anchor = read + 1
        return chars, write


s = Solution()
print(s.compress(["a", "a", "a", "a", "b", "b", "c", "c", "c", "c", "c", "c", "c", "c", "c", "c", "c", "c"]))
