
#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#

# @lc code=start


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        pre_len = 0
        cur_len = 0  # 当前字符串长度

        for i in s:
            if i != " ":
                cur_len += 1
                continue
            pre_len = cur_len if cur_len > 0 else pre_len
            cur_len = 0

        return cur_len if cur_len > 0 else pre_len
# @lc code=end
