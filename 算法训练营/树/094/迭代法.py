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
        stack = [root]
        records, ret = set(), []
        while stack:
            elem = stack.pop()
            if elem is None:
                continue
            if elem.left and elem.left not in records:
                stack.extend([elem, elem.left])
                continue
            ret.append(elem.val)
            records.add(elem)
            if elem.right:
                stack.append(elem.right)
        return ret
        
# @lc code=end
