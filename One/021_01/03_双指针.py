#
# @lc app=leetcode.cn id=86 lang=python3
#
# [86] 分隔链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        root = ListNode(None)
        root.next = head
        insert_point, move_pointer = None, root
        
        while move_pointer.next:
            if move_pointer.next.val < x and insert_point is not None:
                # 交换
                tmp_node = insert_point.next
                insert_point.next = move_pointer.next
                move_pointer.next = move_pointer.next.next
                insert_point.next.next = tmp_node
                # 为保证相对位置，交换之后往前走一个节点
                insert_point = insert_point.next
                continue
            if move_pointer.next.val >= x and insert_point is None:
                # 如果第一次出现 >= x, 设置插入点
                insert_point = move_pointer
            move_pointer = move_pointer.next

        return root.next

# @lc code=end