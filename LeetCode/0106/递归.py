#
# @lc app=leetcode.cn id=106 lang=python3
#
# [106] 从中序与后序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if postorder:
            root_val = postorder[-1]
            root_val_idx = inorder.index(root_val)

            left, right = inorder[:root_val_idx], inorder[root_val_idx+1:]

            root = TreeNode(root_val)
            root.left = self.buildTree(left, postorder[:len(left)])
            root.right = self.buildTree(right, postorder[len(left):-1])

            return root
# @lc code=end