#
# @lc app=leetcode.cn id=606 lang=python3
#
# [606] 根据二叉树创建字符串
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def tree2str(self, t: TreeNode) -> str:
        if not t:
            return ""

        def serialize(node):
            if not node:
                return "()"
            
            L = serialize(node.left)
            R = serialize(node.right)
            
            if L == "()" and R == "()":
                return f"{node.val}"
            elif L == "()" and R != "()":
                return f"{node.val}()({R})"
            elif L != "()" and R == "()":
                return f"{node.val}({L})"
            else:
                return f"{node.val}({L})({R})"
        
        return serialize(t)
# @lc code=end