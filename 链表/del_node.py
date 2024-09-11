from linked import LinkedList


class MyLinkedList(LinkedList):

    def delete_node(self, node):
        ### 补充代码 ###
        if self.head is None or node is None:
            return
        if self.head == node:
            if self.head.next is None:
                self.head.data = None
            else:
                self.head = self.head.next  # 直接将头指针指向下一个节点
            return


        prev = self.head
        curr = self.head.next
        while curr is not None:
            if curr == node:
                if curr.next is None:
                    curr.data = None
                    return
                else:
                    prev.next = curr.next
                    return
            prev = prev.next
            curr = curr.next
