#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start


class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        r1, r2, r3 = 1, 2, 0
        for _ in range(3, n + 1):
            r3 = r1 + r2
            r1 = r2
            r2 = r3
        return r3

# @lc code=end
