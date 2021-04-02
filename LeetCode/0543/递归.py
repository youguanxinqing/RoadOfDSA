#
# @lc app=leetcode.cn id=543 lang=python3
#
# [543] 二叉树的直径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        maxh = 0       
        
        def get_height(node):
            nonlocal maxh
            if not node:
                return 0
            
            lh = get_height(node.left)
            rh = get_height(node.right)
            maxh = max(maxh, lh+rh+1)

            return max(lh, rh) + 1
        
        get_height(root)
        return maxh - 1
# @lc code=end