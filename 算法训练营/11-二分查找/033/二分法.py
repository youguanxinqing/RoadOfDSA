#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums)-1
        while low <= high:
            mid = (low + high) >> 1
            # 找到了就直接返回
            if nums[mid] == target:
                return mid

            if nums[mid] < nums[high]:
                # 认为 [mid, high] 有序
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                # 认为 [low, mid] 有序
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
        
        return -1

# @lc code=end