#
# @lc app=leetcode.cn id=429 lang=python3
#
# [429] N叉树的层序遍历
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []

        quene = [root]
        ret, level = [], []
        # 应取, 实取, 下层总数
        count, retrieve_count, level_count = 1, 0, 0
        while quene:
            node = quene.pop(0)
            retrieve_count += 1
            level.append(node.val)
            if node.children is not None:
                level_count += len(node.children)
                quene.extend(node.children)

            if retrieve_count == count:
                ret.append(level.copy())
                level.clear()
                count = level_count
                retrieve_count = 0
                level_count = 0
        return ret

# @lc code=end
