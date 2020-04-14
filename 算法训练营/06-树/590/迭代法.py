#
# @lc app=leetcode.cn id=590 lang=python3
#
# [590] N叉树的后序遍历
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []

        records = set()
        stack, ret = [root], []
        while stack:
            node = stack.pop()
            if node.children and node not in records:
                stack.append(node)
                stack.extend(node.children[::-1])
                records.add(node)
            else:
                ret.append(node.val)
        return ret
# @lc code=end
