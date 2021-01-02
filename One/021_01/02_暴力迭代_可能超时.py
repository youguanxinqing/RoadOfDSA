#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#

# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_values = []
        for i in range(0, len(nums)):
            sub_nums = nums[i:i+k]
            if len(sub_nums) != k:
                break
            max_values.append(max(sub_nums))
        return max_values
            
# @lc code=end
