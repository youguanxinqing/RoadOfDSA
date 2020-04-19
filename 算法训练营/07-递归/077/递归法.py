#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#

# @lc code=start


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        self.helper([i for i in range(1, n+1)], [], res, k)
        return res

    def helper(self, nums, tmp, res, need_value):
        if not need_value:
            res.append(tmp)
            return

        for i, _ in enumerate(nums):
            tmp_copy = tmp.copy()
            nums_copy = nums.copy()
            tmp_copy.append(nums_copy.pop(i))
            self.helper(nums_copy[i:], tmp_copy, res, need_value-1)
# @lc code=end
