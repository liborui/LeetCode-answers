#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummyHead = ListNode(0)
        dummyHead.next = head
        slow_ptr, fast_ptr, temp_ptr = dummyHead, dummyHead, dummyHead
        for _ in range(n):
            fast_ptr = fast_ptr.next
        while fast_ptr.next != None:
            fast_ptr = fast_ptr.next
            temp_ptr = slow_ptr
            slow_ptr = slow_ptr.next
        slow_ptr.next = slow_ptr.next.next
        return dummyHead.next


# @lc code=end

