#
# @lc app=leetcode.cn id=297 lang=python3
#
# [297] 二叉树的序列化与反序列化
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        string = ""
        stack = [root]
        while stack:
            node = stack.pop(0)
            if node is None:
                string += "null,"
                continue
            else:
                string += f"{node.val},"

            stack.extend([node.left, node.right])

        return f"[{string[:-1]}]"

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        nodes = data.strip("[").strip("]").split(",")
        header = nodes.pop(0)
        if header == "null":
            return None

        root = TreeNode(int(header))
        stack = [root]
        while nodes and stack:
            node = stack.pop(0)
            if node and nodes:
                n = nodes.pop(0)
                node.left = TreeNode(int(n)) if n != "null" else None
                stack.append(node.left)
            if node and nodes:
                n = nodes.pop(0)
                node.right = TreeNode(int(n)) if n != "null" else None
                stack.append(node.right)
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
# @lc code=end
