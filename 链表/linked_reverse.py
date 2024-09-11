# -*- coding:utf-8 -*-
from linked import LinkedList

class MyLinkedList(LinkedList):
    def linked_reverse(self):
        prev = None
        curr = self.head
        while curr is not None:
            next_node = curr.next #移动前,先记录下一个节点
            curr.next = prev #当前节点指向前一个节点
            prev = curr #前节点移动到当前节点
            curr = next_node #当前节点移动到下一个节点
        self.head = prev
