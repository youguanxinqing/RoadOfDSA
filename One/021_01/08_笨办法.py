#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 旋转数组
#

# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        moved_set = set()
        
        for i in range(n):
            
            if i in moved_set:
                continue
            
            move_i, move_v = i, nums[i]
            while move_i not in moved_set:
                next_i = (move_i + k) % n
                nums[next_i], move_v = move_v, nums[next_i]
                moved_set.add(move_i)
                move_i = next_i

# @lc code=end