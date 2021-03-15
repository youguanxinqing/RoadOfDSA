#
# @lc app=leetcode.cn id=496 lang=python3
#
# [496] 下一个更大元素 I
#

# @lc code=start
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for n in nums1:
            maxv, start = -1, False
            for m in nums2:
                if n == m:
                    start = True
                
                if start and m > n:
                    maxv = m   
                    break
            res.append(maxv)
        return res
                
# @lc code=end