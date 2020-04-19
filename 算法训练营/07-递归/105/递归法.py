#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def buildTree(
            self,
            preorder: List[int],
            inorder: List[int]) -> TreeNode:

        if preorder and inorder:
            # father
            f = preorder.pop(0)
            node = TreeNode(f)

            f_idx = inorder.index(f)
            node.left = self.buildTree(preorder, inorder[:f_idx])
            node.right = self.buildTree(preorder, inorder[f_idx+1:])

            return node
        return None

# @lc code=end
