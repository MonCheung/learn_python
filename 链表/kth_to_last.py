from linked import LinkedList


class MyLinkedList(LinkedList):

    def kth_to_last_elem(self, k):
        ### 补充代码 ###
        if self.head is None:
            return None
        if k >= self.__len__():
            return None
        #使用双指针来定位链表倒数第 k+1 个结点
        slow = self.head
        fast = self.head

        #先把fast指针移动k+1步
        for i in range(k+1):
            fast = fast.next

        #把fast和slow一起移动，判断fast是否到达尾节点，输出slow
        while fast is not None:
            fast = fast.next
            slow = slow.next

        return slow.data
