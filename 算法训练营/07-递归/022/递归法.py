#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ret = []

        def generate(left, right, max, s):
            if left == max and right == max:
                ret.append(s)
                return
            if left < max:
                generate(left+1, right, max, s + "(")
            if right < left:
                generate(left, right+1, max, s + ")")

        generate(0, 0, n, "")
        return ret
# @lc code=end
