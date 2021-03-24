#
# @lc app=leetcode.cn id=257 lang=python3
#
# [257] 二叉树的所有路径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        res = []
        if not root:
            return res
        self.collect(root, "", res)
        return res

    def collect(self, root, tmp, res):
        if not root:
            return
        
        if not root.left and not root.right:
            res.append(tmp + f"{root.val}")
        
        self.collect(root.left, tmp + f"{root.val}->", res)
        self.collect(root.right, tmp + f"{root.val}->", res)

# @lc code=end