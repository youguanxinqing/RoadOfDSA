#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#

# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
            max_values = []
            stack = []  # 单调栈, 存放数据的索引
            for i, v in enumerate(nums[:k]):
                # 维持单调性
                while len(stack) > 0 and nums[stack[-1]] <= v:
                    stack = stack[:-1]
                stack.append(i)
            
            max_values.append(nums[stack[0]])
            for i, v in enumerate(nums[k:]):
                real_i = i + k
                
                # 向右移动时的自然淘汰
                if real_i + 1 - k > stack[0]:
                    stack = stack[1:]
                
                # 维持单调性
                while len(stack) > 0 and nums[stack[-1]] <= v:
                    stack = stack[:-1]
                
                stack.append(real_i)
                max_values.append(nums[stack[0]])
            
            return max_values

# @lc code=end
