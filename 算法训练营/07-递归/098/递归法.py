#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.helper(root, None, None)

    def helper(self, root, min, max) -> bool:
        if root is None:
            return True

        if min is not None and root.val <= min:
            return False
        if max is not None and root.val >= max:
            return False

        return (
            self.helper(root.left, min, root.val)
            and self.helper(root.right, root.val, max)
        )

# @lc code=end
