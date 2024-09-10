# -*- coding:utf-8 -*-
class UniqueChars(object):

    def has_unique_chars(self, string):
        if string is None:
            return False

        char=[]

        for j in string:
            if j in char:
                return False
            char.append(j)

        return True

# 实例化 UniqueChars 类
unique_chars_checker = UniqueChars()


##单元测试
self.assertEqual(has_unique_chars(None), False)
self.assertEqual(has_unique_chars(''), True)
self.assertEqual(has_unique_chars('foo'), False)
self.assertEqual(has_unique_chars('bar'), True)
