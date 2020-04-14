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

        ret = []
        self.helper(root, ret)
        return ret

    def helper(self, node, ret):
        if node.children:
            for child in node.children:
                self.helper(child, ret)
        ret.append(node.val)
# @lc code=end
