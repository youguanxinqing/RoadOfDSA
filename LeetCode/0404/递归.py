#
# @lc app=leetcode.cn id=404 lang=python3
#
# [404] 左叶子之和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        return self.count(root, "")
    
    def count(self, root, flag):
        if not root:
            return 0
        
        if not root.left and not root.right:
            if flag == "l":
                return root.val
            else:
                return 0
        
        return self.count(root.left, "l") + self.count(root.right, "r")
# @lc code=end