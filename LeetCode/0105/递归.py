#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if preorder:
            root_val = preorder[0]
            root_val_idx = inorder.index(root_val)

            left, right = inorder[:root_val_idx], inorder[root_val_idx+1:]

            root = TreeNode(root_val)
            root.left = self.buildTree(preorder[1:len(left)+1], left)
            root.right = self.buildTree(preorder[len(left)+1:], right)
            
            return root
# @lc code=end