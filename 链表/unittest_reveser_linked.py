# -*- coding:utf-8 -*-
import unittest
from linked_reverse import MyLinkedList
from linked import Node

class Test_reverse(unittest.TestCase):
    """docstring for Test_reverse."""

    def test_reverse_linked(self):
        #测试空链表
        linked_list = MyLinkedList(None)
        print('Test: Empty list')
        linked_list.linked_reverse()
        self.assertEqual(linked_list.get_all_data(),[])

        #单节点链表
        print('Test: One element list')
        linked_list.insert_to_front(2)
        linked_list.linked_reverse()
        self.assertEqual(linked_list.get_all_data(),[2])

        #多结点链表
        print('Test: more element list')
        linked_list = MyLinkedList(None)
        linked_list.insert_to_front(4)
        linked_list.insert_to_front(3)
        linked_list.insert_to_front(2)
        linked_list.insert_to_front(1)
        linked_list.linked_reverse()
        self.assertEqual(linked_list.get_all_data(),[4,3,2,1])

if __name__ == '__main__':
    unittest.main()
