# -*- coding:utf-8 -*-
import unittest
from linked import LinkedList

class MyLinkedList(LinkedList):
    def  remove_dupes(self):
        if self.head is None:
            return self.head
        seen = set()
        curr = self.head
        seen.add(curr.data)

        while  curr and curr.next:
            if curr.next.data in seen:
                curr.next = curr.next.next
            else:
                seen.add(curr.next.data)
                curr = curr.next
        return self.head
