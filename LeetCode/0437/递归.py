#
# @lc app=leetcode.cn id=437 lang=python3
#
# [437] 路径总和 III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        return self.count(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
    
    def count(self, root, sum):
        if not root:
            return 0

        cnt = 1 if root.val == sum else 0
        cnt += self.count(root.left, sum-root.val)
        cnt += self.count(root.right, sum-root.val)
        return cnt
# @lc code=end