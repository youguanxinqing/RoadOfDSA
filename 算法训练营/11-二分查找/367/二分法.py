#
# @lc app=leetcode.cn id=367 lang=python3
#
# [367] 有效的完全平方数
#

# @lc code=start
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        low, high = 0, num//2+1
        while low <= high:
            mid = (low + high) >> 1
            if mid**2 == num:
                return True
            elif mid**2 > num:
                high = mid - 1
            else:
                low = mid + 1
        return low**2 == num
# @lc code=end