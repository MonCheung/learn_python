# -*- coding:utf-8 -*-

class Node(object):
    def __init__(self, data, next=None):
        # 初始化节点，包含数据和指向下一个节点的引用
        self.data = data
        self.next = next

    def __str__(self):
        # 返回节点数据的字符串表示
        return str(self.data)


class LinkedList(object):
    def __init__(self, head=None):
        # 初始化链表，可选头节点
        self.head = head

    def __len__(self):
        # 返回链表的长度
        curr_node = self.head
        counter = 0
        while curr_node is not None:
            counter += 1
            curr_node = curr_node.next
        return counter

    def insert_to_front(self, data):
        # 在链表头部插入节点
        if data is None:
            return None
        node = Node(data, self.head)
        self.head = node
        return node

    def append(self, data):
        # 在链表尾部追加节点
        if data is None:
            return None
        node = Node(data)
        if self.head is None:
            self.head = node
            return node
        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next
        curr_node.next = node
        return node

    def find(self, data):
        # 查找并返回包含指定数据的节点
        if data is None:
            return None
        curr_node = self.head
        while curr_node is not None:
            if curr_node.data == data:
                return curr_node
            curr_node = curr_node.next
        return None

    def delete(self, data):
        # 删除包含指定数据的节点
        if data is None:
            return
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        prev_node = self.head
        curr_node = self.head.next
        while curr_node is not None:
            if curr_node.data == data:
                prev_node.next = curr_node.next
                return
            prev_node = curr_node
            curr_node = curr_node.next

    def print_list(self):
        # 打印链表中的所有节点
        curr_node = self.head
        while curr_node is not None:
            print(curr_node.data)
            curr_node = curr_node.next

    def get_all_data(self):
        # 返回链表中所有节点的数据列表
        data = []
        curr_node = self.head
        while curr_node is not None:
            data.append(curr_node.data)
            curr_node = curr_node.next
        return data
