#
# @lc app=leetcode.cn id=501 lang=python3
#
# [501] 二叉搜索树中的众数
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        res = []
        base = float("inf")
        count, max_count = 0, 0
        
        def update(val):
            nonlocal base, count, max_count
            if val == base:
                count += 1
            else:
                base = val
                count = 1
            
            if count == max_count:
                res.append(val)
            elif count > max_count:
                res.clear()
                res.append(val)
                max_count = count

        def inorder(root):
            if not root:
                return 
            inorder(root.left)
            update(root.val)
            inorder(root.right)
        
        inorder(root)
        return res

# @lc code=end