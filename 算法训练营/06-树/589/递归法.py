#
# @lc app=leetcode.cn id=589 lang=python3
#
# [589] N叉树的前序遍历
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
    def preorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []

        ret = []
        self.helper(root, ret)
        return ret

    def helper(self, node, ret):
        ret.append(node.val)
        if node.children is not None:
            for node in node.children:
                self.helper(node, ret)
# @lc code=end
