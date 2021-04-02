#
# @lc app=leetcode.cn id=337 lang=python3
#
# [337] 打家劫舍 III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def __init__(self) -> None:
        self.map = {}

    def rob(self, root: TreeNode) -> int:
        if not root:
            return 0

        m = root.val
        if root.left:
            if root.left.left not in self.map:
                self.map[root.left.left] = self.rob(root.left.left)
            if root.left.right not in self.map:
                self.map[root.left.right] = self.rob(root.left.right)
            m += self.map[root.left.left] + self.map[root.left.right]
        if root.right:
            if root.right.left not in self.map:
                self.map[root.right.left] = self.rob(root.right.left)
            if root.right.right not in self.map:
                self.map[root.right.right] = self.rob(root.right.right)
            m += self.map[root.right.left] + self.map[root.right.right]

        if root.left not in self.map:
            self.map[root.left] = self.rob(root.left)
        if root.right not in self.map:
            self.map[root.right] = self.rob(root.right)
        return max([m,  + self.map[root.left] + self.map[root.right]])

# @lc code=end