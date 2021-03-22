#
# @lc app=leetcode.cn id=117 lang=python3
#
# [117] 填充每个节点的下一个右侧节点指针 II
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        queue = [root]
        while queue:
            num = len(queue)
            for i in range(num):
                if i+1 < num:
                    queue[i].next = queue[i+1]
            
            tmp = []
            for n in queue:
                if n.left:
                    tmp.append(n.left)
                if n.right:
                    tmp.append(n.right)
            queue = tmp
        
        return root

# @lc code=end