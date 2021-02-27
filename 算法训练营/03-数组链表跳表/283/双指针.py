#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return 
        
        prev, next = 0, 1
        while next < len(nums):
            if nums[prev] == 0 and nums[next] == 0:
                next += 1
                continue

            if nums[prev] == 0 and nums[next] != 0:
                nums[prev], nums[next] = nums[next], nums[prev]
            
            prev += 1
            next += 1
# @lc code=end