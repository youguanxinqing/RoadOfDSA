#
# @lc app=leetcode.cn id=231 lang=python3
#
# [231] 2的幂
#

# @lc code=start
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        
        while n:
            if n & 1 == 1:
                n >>= 1
                break
            else:
                n >>= 1
        return n == 0
# @lc code=end