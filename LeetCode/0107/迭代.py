#
# @lc app=leetcode.cn id=107 lang=python3
#
# [107] 二叉树的层序遍历 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        res, queue = [], [root]
        while queue:
            res.append([n.val for n in queue])

            tmp = []
            for n in queue:
                if n.left:
                    tmp.append(n.left)
                if n.right:
                    tmp.append(n.right)
            queue = tmp
        return res[-1::-1]

# @lc code=end