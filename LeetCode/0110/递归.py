#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        left_h = self.count(root.left)
        right_h = self.count(root.right)
        if abs(left_h - right_h) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
    
    def count(self, node):
        if not node:
            return 0
        left = self.count(node.left)
        right = self.count(node.right)
        return 1 + (left if left > right else right)
# @lc code=end