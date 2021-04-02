#
# @lc app=leetcode.cn id=530 lang=python3
#
# [530] 二叉搜索树的最小绝对差
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:

        pre = None
        min_diff = float("inf")
        def diff(cur):
            nonlocal pre, min_diff
            if not cur:
                return

            diff(cur.left)
            
            if pre:
                min_diff = abs(cur.val - pre.val) if abs(cur.val - pre.val) < min_diff else min_diff
            pre = cur
            diff(cur.right)
        
        diff(root)
        return min_diff
# @lc code=end