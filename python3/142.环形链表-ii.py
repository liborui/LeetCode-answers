#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        fast_ptr, slow_ptr = head, head
        while fast_ptr and fast_ptr.next:
            fast_ptr = fast_ptr.next.next
            slow_ptr = slow_ptr.next
            if fast_ptr == slow_ptr:
                slow_ptr = head
                while fast_ptr != slow_ptr:
                    fast_ptr = fast_ptr.next
                    slow_ptr = slow_ptr.next
                return fast_ptr
        return None
# @lc code=end

