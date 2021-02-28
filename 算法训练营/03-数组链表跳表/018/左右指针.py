#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#

# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        return self.nSum(nums, 4, 0, target)

    def nSum(self, nums, n, start, target):
        sz = len(nums)
        res = []
        if n < 2 or sz < n:
            return res
        elif n == 2:
            left, right = start, len(nums)-1
            while left < right:
                lv, rv = nums[left], nums[right]
                if lv + rv > target:
                    while left < right and nums[right] == rv:
                        right -= 1
                elif lv + rv < target:
                    while left < right and nums[left] == lv:
                        left += 1
                else:
                    res.append([lv, rv])
                    while left < right and nums[right] == rv:
                        right -= 1
                    while left < right and nums[left] == lv:
                        left += 1
        else:
            i = start
            while i < len(nums):
                iv = nums[i]
                subres = self.nSum(nums, n-1, i+1, target-iv)
                res.extend(([iv]+item for item in subres))
                while i < len(nums) and nums[i] == iv:
                    i += 1
        return res

# @lc code=end