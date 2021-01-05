#
# @lc app=leetcode.cn id=830 lang=python3
#
# [830] 较大分组的位置
#

# @lc code=start
class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        results = []
        prev = None
        for cur in range(0, len(s)):
            if prev is None:
                prev = cur
                continue
            if s[prev] != s[cur]:
                if (cur - prev) >= 3:
                    results.append([prev, cur-1])
                prev = cur
        
        if (len(s) - prev) >= 3:
            results.append([prev, len(s)-1])
        return results

# @lc code=end