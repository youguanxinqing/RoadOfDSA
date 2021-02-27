#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        y, sum = abs(x), 0
        
        while y:
            sum *= 10
            sum += y % 10
            y //= 10
        
        sum = sum if x > 0 else -sum
        if -2**31 <= sum <= 2**31-1:
            return sum
        return 0
# @lc code=end