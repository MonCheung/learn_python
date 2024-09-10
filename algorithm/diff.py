# -*- coding:utf-8 -*-
class Solution(object):

    def find_diff(self, str1, str2):
        if str1 is None or str2 is None:
            raise TypeError

        if abs(len(str1)-len(str2)) != 1:
            return None

        if len(str1) < len(str2):
            str1,str2 = str2,str1

        #创建两个指针遍历字符串
        i,j = 0,0
        different_char = None
        found_difference = False

        while i<len(str1) and j<len(str2):
            if str1[i] != str2[j]:
                found_difference = True
                different_char = str1[i]
                i += 1
            else:
                i += 1
                j += 1


        if found_difference or (i == len(str1) - 1  and j == len(str2)):
            print(i,j)
            return different_char

        return None

sol=Solution()

print(sol.find_diff('aaabbcdd', 'abdbaaedc'))
print(sol.find_diff('ab', 'abc'))
print(sol.find_diff('ab', 'aab'))
