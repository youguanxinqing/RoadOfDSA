#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        ret = []
        self.helper(root, ret)
        return ret
    
    def helper(self, root, ret):
        if root:
            ret.append(root.val)
            self.helper(root.left, ret)
            self.helper(root.right, ret)
# @lc code=end
