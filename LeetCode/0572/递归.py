#
# @lc app=leetcode.cn id=572 lang=python3
#
# [572] 另一个树的子树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s:
            return self.compare_tree(s, t)
        
        queue = [s]
        while queue:
            node = queue.pop(0)
            
            if self.compare_tree(node, t):
                return True
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return False

    def compare_tree(self, s, t) -> bool:
        if not s and not t:
            return True
        elif not s or not t:
            return False
        
        if s.val != t.val:
            return False
        return self.compare_tree(s.left, t.left) and self.compare_tree(s.right, t.right)
# @lc code=end