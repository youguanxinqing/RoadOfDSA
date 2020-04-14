#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start


class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        return self.helper(n, cache)

    def helper(self, n, cache):
        if n < 1:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2

        if n in cache:
            return cache[n]

        cache[n] = self.helper(n-1, cache) + self.helper(n-2, cache)
        return cache[n]

# @lc code=end
