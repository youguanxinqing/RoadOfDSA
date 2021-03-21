#
# @lc app=leetcode.cn id=103 lang=python3
#
# [103] 二叉树的锯齿形层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        res, lyst = [], [root]
        level = 0
        while lyst:
            if level & 1 == 0:
                tmp = [node.val for node in lyst]
            else:
                tmp = [node.val for node in lyst[-1::-1]]
            res.append(tmp)

            tmp = []
            for node in lyst:
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            lyst = tmp
            level += 1
        return res

# @lc code=end