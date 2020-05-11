#
# @lc app=leetcode.cn id=709 lang=python3
#
# [709] 转换成小写字母
#

# @lc code=start


class Solution:
    def toLowerCase(self, str: str) -> str:
        delta = ord("a") - ord("A")
        target_str = ""
        for ch in str:
            new_ch = chr(ord(ch) + delta) if "Z" >= ch >= "A" else ch
            target_str += new_ch

        return target_str

# @lc code=end
