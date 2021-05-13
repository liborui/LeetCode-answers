#
# @lc app=leetcode.cn id=707 lang=python3
#
# [707] 设计链表
#

# @lc code=start
class LinkedNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.len = 0
        self.zero_head = LinkedNode(0)
        self.zero_tail = LinkedNode(0)


    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index > self.len:
            return -1
        curr = self.zero_head
        for _ in range(index+1):
            curr = curr.next
        return self.val


    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        self.addAtIndex(0, val)
           


    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """


    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        newNode = LinkedNode(val)
        if self.len == 0:
            self.zero_head.next = newNode
            newNode.next = self.zero_tail
            self.zero_tail.prev = newNode
            newNode.prev = self.zero_head
        else:
            curr = self.zero_head
            for _ in range(index + 1):
                curr = curr.next
            curr.next.prev = newNode
            newNode.next = curr.next
            newNode.prev = curr
            curr.next = newNode



    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if self.len == 0 or index > self.len:
            return
        if self.len == 1:
            self.zero_head.next = None
            self.zero_tail.prev = None
        else:
            curr = self.zero_head
            for _ in range(index+1):
                curr = curr.next
            prev = curr.prev
            prev.next = curr.next
            curr.next.prev = prev.



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
# @lc code=end

