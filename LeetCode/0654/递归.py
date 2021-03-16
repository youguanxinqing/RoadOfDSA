#
# @lc app=leetcode.cn id=654 lang=python3
#
# [654] 最大二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if nums:
            max_v = max(nums)
            idx = nums.index(max_v)
            
            root = TreeNode(max_v)
            root.left = self.constructMaximumBinaryTree(nums[:idx])
            root.right = self.constructMaximumBinaryTree(nums[idx+1:])
            
            return root
# @lc code=end