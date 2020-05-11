
#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#

# @lc code=start


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        clear_str = [i for i in s.split() if i]
        if len(clear_str) > 0:
            return len(clear_str[-1])
        return 0
# @lc code=end
