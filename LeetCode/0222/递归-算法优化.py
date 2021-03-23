#
# @lc app=leetcode.cn id=222 lang=python3
#
# [222] 完全二叉树的节点个数
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        lh = self.count_level(root.left)
        rh = self.count_level(root.right)
        if lh == rh:
            return self.countNodes(root.right) + (1 << lh)
        return self.countNodes(root.left) + (1 << rh)


    def count_level(self, root):
        level = 0
        while root:
            level += 1
            root = root.left
        return level
# @lc code=end