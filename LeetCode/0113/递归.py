#
# @lc app=leetcode.cn id=113 lang=python3
#
# [113] 路径总和 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        res = []
        self.calculate(root, targetSum, [], res)
        return res
    
    def calculate(self, node, target, tmp, res):
        if not node:
            return 
        
        if not node.left and not node.right and target == node.val:
            tmp.append(node.val)
            res.append(tmp)
            return

        self.calculate(node.left, target-node.val, tmp+[node.val], res)
        self.calculate(node.right, target-node.val, tmp+[node.val], res)
    
# @lc code=end