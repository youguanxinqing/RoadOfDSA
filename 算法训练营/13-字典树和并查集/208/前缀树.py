#
# @lc app=leetcode.cn id=208 lang=python3
#
# [208] 实现 Trie (前缀树)
#

# @lc code=start
class Node(object):
    def __init__(self, val, end=False) -> None:
        self.val = val
        self.end = end
        self.children = [None for _ in range(26)]

class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node(None)

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for alpha in word:
            if node.children[ord(alpha) - 97] is None:
                node.children[ord(alpha) - 97] = Node(alpha)
            node = node.children[ord(alpha) - 97]
        node.end = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for alpha in word:
            if node.children[ord(alpha) - 97] is None:
                return False
            node = node.children[ord(alpha) - 97]
        return node.end       

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for alpha in prefix:
            if node.children[ord(alpha) - 97] is None:
                return False
            node = node.children[ord(alpha) - 97]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end