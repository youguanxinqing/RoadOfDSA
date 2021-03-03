#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#

# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        single_queue = []
        
        for i in range(k-1):
            while single_queue:
                if nums[single_queue[-1]] < nums[i]:
                    single_queue.pop()
                else:
                    break
            single_queue.append(i)
        
        max_vars = []
        for i in range(k-1, len(nums)):
            
            while single_queue:
                if nums[single_queue[-1]] < nums[i]:
                    single_queue.pop()
                else:
                    break
            single_queue.append(i)
            
            max_vars.append(nums[single_queue[0]])

            if i - single_queue[0] >= k-1:
                single_queue = single_queue[1:]
            
        return max_vars

# @lc code=end