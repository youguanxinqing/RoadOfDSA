#
# @lc app=leetcode.cn id=538 lang=python3
#
# [538] 把二叉搜索树转换为累加树
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
        self.num = 0

    def tracker(self, root):
        if not root:
            return
        
        self.tracker(root.right)
        self.num += root.val
        root.val = self.num
        self.tracker(root.left)

    def convertBST(self, root: TreeNode) -> TreeNode:
        self.tracker(root)
        return root
        
# @lc code=end