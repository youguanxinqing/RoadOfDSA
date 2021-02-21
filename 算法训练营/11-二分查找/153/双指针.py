#
# @lc app=leetcode.cn id=153 lang=python3
#
# [153] 寻找旋转排序数组中的最小值
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums)-1
        while low < high:
            mid = (low + high) >> 1
            if nums[mid] < nums[high]:
                high -= 1
            else:
                low += 1
        return nums[low]

# @lc code=end