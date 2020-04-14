#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ret = []
        self.helper(root, ret)
        return ret

    def helper(self, root, ret):
        if root:
            self.helper(root.left, ret)
            ret.append(root.val)
            self.helper(root.right, ret)
# @lc code=end

