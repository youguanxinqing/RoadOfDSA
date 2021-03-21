#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.serialize(root.left, is_left=True) == self.serialize(root.right, is_left=False)
        
    
    def serialize(self, root, is_left) -> str:
        if not root:
            return "#"
        left = self.serialize(root.left, True)
        right = self.serialize(root.right, False)
        
        if is_left:
            return f"{left},{right},{root.val}"
        return f"{right},{left},{root.val}"

# @lc code=end
