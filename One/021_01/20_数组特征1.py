#
# @lc app=leetcode.cn id=628 lang=python3
#
# [628] 三个数的最大乘积
#

# @lc code=start
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        max1, max2, max3 = float("-inf"), float("-inf"), float("-inf")
        min1, min2 = float("inf"), float("inf")

        for n in nums:
            if n > max1:
                max1, max2, max3 = n, max1, max2
            elif n > max2:
                max2, max3 = n, max2
            elif n > max3:
                max3 = n
            
            if n < min1:
                min1, min2 = n, min1
            elif n < min2:
                min2 = n
        
        return max(int(max1*max2*max3), int(max1*min1*min2))
# @lc code=end
