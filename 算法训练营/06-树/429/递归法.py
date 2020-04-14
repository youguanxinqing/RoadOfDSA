#
# @lc app=leetcode.cn id=429 lang=python3
#
# [429] N叉树的层序遍历
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
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []
        level_nodes = [root]
        ret = []       
        self.helper(level_nodes, ret)
        return ret
    
    def helper(self, level_nodes, ret):
        if not level_nodes:
            return
        
        level_ret, level_children = [], []
        for node in level_nodes:
            level_ret.append(node.val)
            if node.children is not None:
                level_children.extend(node.children)
        ret.append(level_ret)
        self.helper(level_children, ret)

        
# @lc code=end
