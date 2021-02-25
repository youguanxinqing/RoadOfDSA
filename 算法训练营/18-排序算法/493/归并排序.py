#
# @lc app=leetcode.cn id=493 lang=python3
#
# [493] 翻转对
#

# @lc code=start
class Solution:
    def __init__(self) -> None:
        self.cnt = 0
    
    def reversePairs(self, nums: List[int]) -> int:
        self.merge_sort(nums)
        return self.cnt
    
    def merge_sort(self, nums):
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        left, right = self.merge_sort(nums[:mid]), self.merge_sort(nums[mid:])
        return self.merge(left, right)

    def merge(self, left, right):
        l, r = 0, 0
        while l < len(left) and r < len(right):
            if left[l] <= 2 * right[r]:
                l += 1
            else:
                self.cnt += len(left) - l
                r += 1

        l, r = 0, 0
        ret = []
        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                ret.append(left[l])
                l += 1
            else:
                ret.append(right[r])
                r += 1
        ret += left[l:]
        ret += right[r:]
        return ret
# @lc code=end