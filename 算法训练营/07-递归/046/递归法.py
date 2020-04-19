#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        tmp, res = [], []
        self.helper(nums, tmp, res, len(nums))
        return res

    def helper(self, nums, tmp, res, need_value):
        if not need_value:
            res.append(tmp)
            return

        for num in nums:
            tmp_copy = tmp.copy()
            tmp_copy.append(num)
            nums_copy = nums.copy()
            nums_copy.remove(num)
            self.helper(nums_copy, tmp_copy, res, need_value-1)
# @lc code=end
