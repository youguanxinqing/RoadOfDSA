#
# @lc app=leetcode.cn id=222 lang=python3
#
# [222] 完全二叉树的节点个数
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        
        cnt, queue = 0, [root]
        while queue:
            cnt += len(queue)

            tmp = []
            for n in queue:
                if n.left:
                    tmp.append(n.left)
                if n.right:
                    tmp.append(n.right)
            queue = tmp
        return cnt
# @lc code=end