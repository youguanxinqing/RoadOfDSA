#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        low, high = 0, len(height)-1
        while low < high:
            area = (height[low] if height[low] < height[high] else height[high]) * (high-low)
            if area > max_area:
                max_area = area
            if height[low] < height[high]:
                low += 1
            else:
                high -= 1
        return max_area
# @lc code=end