
#
# @lc app=leetcode.cn id=771 lang=python3
#
# [771] 宝石与石头
#

# @lc code=start


class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count = 0
        for s in S:
            if s in J:
                count += 1
        return count

# @lc code=end
