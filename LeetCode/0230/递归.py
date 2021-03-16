#
# @lc app=leetcode.cn id=230 lang=python3
#
# [230] 二叉搜索树中第K小的元素
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.vals = []
    
    def serialize(self, root):
        if root:
            self.serialize(root.left)
            self.vals.append(root.val)
            self.serialize(root.right)

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.serialize(root)
        return self.vals[k-1]

# @lc code=end
