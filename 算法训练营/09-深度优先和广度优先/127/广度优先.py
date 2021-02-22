#
# @lc app=leetcode.cn id=127 lang=python3
#
# [127] 单词接龙
#

# @lc code=start
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordList:
            return 0
        
        queue, visitMap = [], {}

        queue.append(beginWord)
        visitMap[beginWord] = 1
        # 广度优先
        while queue:
            word = queue.pop(0)
            path = visitMap[word]
            for i in range(len(beginWord)):
                for j in range(26):
                    newWord = word[:i] + chr(j + ord("a")) + word[i+1:]
                    if newWord == endWord:
                        return path + 1
                    if newWord in wordSet and newWord not in visitMap:
                        visitMap[newWord] = path + 1
                        queue.append(newWord)
        return 0
# @lc code=end
