#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#

# @lc code=start


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.helper(nums, [], res, len(nums))
        return list(res)

    def helper(self, nums, tmp, res, need_value):
        if not need_value and tmp not in res:
            res.append(tmp)
            return

        for num in nums:
            tmp_copy = tmp.copy()
            nums_copy = nums.copy()
            tmp_copy.append(num)
            nums_copy.remove(num)
            self.helper(nums_copy, tmp_copy, res, need_value-1)
# @lc code=end
