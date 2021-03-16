#
# @lc app=leetcode.cn id=652 lang=python3
#
# [652] 寻找重复的子树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.m = {}
        self.res = []
    
    def serialize(self, root):
        if root:
            left = self.serialize(root.left)
            right = self.serialize(root.right)
            
            subtree = f"{left},{right},{root.val}"
            cnt = self.m.get(subtree, 0)
            if cnt == 1:
                self.res.append(root)
            self.m[subtree] = cnt+1
            
            return subtree
        
        return "#"

    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        self.serialize(root)
        return self.res

# @lc code=end