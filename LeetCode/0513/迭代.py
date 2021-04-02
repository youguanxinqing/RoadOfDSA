#
# @lc app=leetcode.cn id=513 lang=python3
#
# [513] 找树左下角的值
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        queue = [root]
        while queue:
            
            tmp = []
            for n in queue:
                if n.left:
                    tmp.append(n.left)
                if n.right:
                    tmp.append(n.right)
            
            if not tmp:
                break
            queue = tmp
        return queue[0].val
# @lc code=end
