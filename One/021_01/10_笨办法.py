#
# @lc app=leetcode.cn id=228 lang=python3
#
# [228] 汇总区间
#

# @lc code=start
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        i = 0
        while i < len(nums):
            j = i+1
            while j < len(nums):
                if nums[j] - nums[j-1] != 1:
                    break
                j += 1
            res.append(f"{nums[i]}" if i == j-1 else f"{nums[i]}->{nums[j-1]}")
            i = j
        return res
# @lc code=end