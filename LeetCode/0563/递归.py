#
# @lc app=leetcode.cn id=563 lang=python3
#
# [563] 二叉树的坡度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        
        total = 0
        def count(node):
            nonlocal total
            
            if not node:
                return 0
            
            L = count(node.left)
            R = count(node.right)
            total += abs(L-R)
            return L + R + node.val
        
        count(root)
        return total
# @lc code=end