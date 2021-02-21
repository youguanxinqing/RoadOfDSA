#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        low, high = 0, x//2+1
        while low < high:
            mid = (low + high + 1) >> 1
            if mid**2 > x:
                high = mid - 1
            else:
                low = mid
        return low

# @lc code=end