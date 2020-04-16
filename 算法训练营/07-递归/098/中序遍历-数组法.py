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
        cache = []
        self.helper(root, cache)
        for i in range(1, len(cache)):
            if cache[i-1] >= cache[i]:
                return False
        return True

    def helper(self, node, cache):
        if node is None:
            return
        self.helper(node.left, cache)
        cache.append(node.val)
        self.helper(node.right, cache)

# @lc code=end
