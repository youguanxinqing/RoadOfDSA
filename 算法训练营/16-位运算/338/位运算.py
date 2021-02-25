#
# @lc app=leetcode.cn id=338 lang=python3
#
# [338] 比特位计数
#

# @lc code=start
class Solution:
    def countBits(self, num: int) -> List[int]:
        ret = [0 for _ in range(num+1)]
        for i in range(num+1):
            if i & 1:  # 基数
                ret[i] = ret[i-1]+1
            else:  # 偶数
                ret[i] = ret[i//2]
        return ret
        
# @lc code=end