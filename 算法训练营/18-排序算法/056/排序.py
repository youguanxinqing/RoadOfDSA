#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        
        ret = []
        
        soted_intervals = sorted(intervals, key=lambda t: t[0])
        
        pre = soted_intervals.pop(0)
        while soted_intervals:
            cur = soted_intervals.pop(0)
            if pre[1] >= cur[0]:
                pre = [pre[0], cur[1] if cur[1] > pre[1] else pre[1]]
            else:
                ret.append(pre)
                pre = cur
        ret.append(pre)
        return ret

# @lc code=end