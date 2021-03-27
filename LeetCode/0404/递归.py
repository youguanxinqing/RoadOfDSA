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
        return self.count(root, False)

    def count(self, root, is_left):
        if not root:
            return 0
        
        if is_left and not root.left and not root.right:
            return root.val + self.count(root.left, True) + self.count(root.right, False)
        return self.count(root.left, True) + self.count(root.right, False)

# @lc code=end