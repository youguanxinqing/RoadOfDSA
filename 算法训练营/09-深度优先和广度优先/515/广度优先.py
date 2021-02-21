#
# @lc app=leetcode.cn id=515 lang=python3
#
# [515] 在每个树行中找最大值
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:

        max_nums = []

        queue = [] if not root else [root]
        while queue:
            cur_level_nodes = queue
            queue = []
            maxv = cur_level_nodes[0].val
            for node in cur_level_nodes:
                if maxv < node.val:
                    maxv = node.val
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            max_nums.append(maxv)
        
        return max_nums
        
# @lc code=end