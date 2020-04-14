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
        stack = [root]
        records, ret = set(), []
        while stack:
            elem = stack.pop()
            if elem is None:
                continue
            if elem not in records:
                ret.append(elem.val)
                records.add(elem)
            if elem.left and elem.left not in records:
                stack.extend([elem, elem.left])
                continue
            if elem.right:
                stack.append(elem.right)
        return ret

# @lc code=end
