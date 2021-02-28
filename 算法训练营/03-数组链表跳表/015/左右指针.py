#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        i = 0
        while i < len(nums):
            iv = nums[i]
            gen = ([iv]+item for item in self.twoSum(nums[i+1:], -nums[i]))
            res.extend(gen)
            while i < len(nums) and nums[i] == iv:
                i += 1
        return res

    def twoSum(self, nums: List[int], target):
        left, right = 0, len(nums)-1
        while left < right:
            lv, rv = nums[left], nums[right]
            if lv + rv > target:
                while left < right and nums[right] == rv:
                    right -= 1
            elif lv + rv < target:
                while left < right and nums[left] == lv:
                    left += 1
            else:
                yield [nums[left], nums[right]]
                while left < right and nums[right] == rv:
                    right -= 1
                while left < right and nums[left] == lv:
                    left += 1
# @lc code=end