#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if head is None:
            return head
        
        a, b = head, head
        for i in range(k):
            if b is None:
                return head
            b = b.next
        
        new_head = self.reserve(a, b)
        a.next = self.reverseKGroup(b, k)
        return new_head
    
    def reserve(self, a, b):
        pre, cur, nxt = None, a, None
        while cur != b:
            nxt = cur.next
            cur.next = pre
            pre, cur = cur, nxt
        return pre
# @lc code=end