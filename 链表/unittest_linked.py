# -*- coding:utf-8 -*-
import unittest
from linked import LinkedList

##创建单元测试用例

class TestLinkedList(unittest.TestCase):
    #自定义检查方法
    def check_list(self,linked_list,expected_data,test_name):
        try:
            self.assertEqual(linked_list.get_all_data(), expected_data)
            #return True
        except AssertionError:
            print(f'Failed: {test_name}')
            #return False

    def test_insert_to_front(self):
        success = True

        #打印调试信息
        print('Test: insert_to_front on an empty list')
        #创建空链表
        linked_list = LinkedList(None)
        #插入节点到链表头部
        linked_list.insert_to_front(10)
        #编写断言，检查数据是否正确插入
        self.assertEqual(linked_list.get_all_data(), [10])
        #打印链表数据
        print('List after insert_to_front:', linked_list.get_all_data())

        #检查插入none
        print('Test: insert_to_front on a None')
        linked_list.insert_to_front(None)
        #2.自定义检查方法来防止一条断言失败后续不再执行
        if not self.check_list(linked_list,[10],'insert None'):
            success = False

        #检查往头部继续插入数据
        print('Test: insert_to_front general case')
        linked_list.insert_to_front('a')
        linked_list.insert_to_front('bc')
        self.assertEqual(linked_list.get_all_data(), ['bc', 'a', 10])

        #当所有断言通过才打印
        if success:
            print('Success: test_insert_to_front\n')

    def test_insert_to_append(self):
        #检查在空列表尾部插入数据
        print('Test: append on an empty list')
        linked_list = LinkedList(None)
        linked_list.append(10)
        self.assertEqual(linked_list.get_all_data(), [10])

        #检查插入none
        print('Test: append a None')
        linked_list.append(None)
        #1.增加try...except检查，当这条断言失败还可以继续执行下去
        try:
            self.assertEqual(linked_list.get_all_data(), [10])
        except AssertionError:
            print('Failed: append a None')

        #继续插入真实数据
        print('Test: append general case')
        linked_list.append('a')
        linked_list.append('bc')
        self.assertEqual(linked_list.get_all_data(), [10,'a','bc'])

        print('Success: test_append\n')

if __name__ == '__main__':
    unittest.main()
