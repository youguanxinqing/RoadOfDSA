#
# @lc app=leetcode.cn id=129 lang=python3
#
# [129] 求根节点到叶节点数字之和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        res = []
        self.calculate(root, 0, res)
        return sum(res)
    
    def calculate(self, node, num, res):
        if not node:
            return
        
        if not node.left and not node.right:
            res.append(num+node.val)
            return
        
        num += node.val
        num *= 10
        self.calculate(node.left, num, res)
        self.calculate(node.right, num, res)
# @lc code=end