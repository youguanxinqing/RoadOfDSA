#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        rets = []
        
        if not root:
            return rets

        cur_level = 0
        cur_level_list = []
        
        queue = [(0, root)]
        while queue:
            level, node = queue.pop(0)
            if node:
                if level == cur_level:
                    cur_level_list.append(node.val)
                else:
                    rets.append(cur_level_list)
                    cur_level_list = [node.val]
                    cur_level = level

                queue.extend([(level+1, node.left), (level+1, node.right)])
        rets.append(cur_level_list)
        return rets
                
# @lc code=end