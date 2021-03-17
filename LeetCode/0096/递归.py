#
# @lc app=leetcode.cn id=96 lang=python3
#
# [96] 不同的二叉搜索树
#

# @lc code=start
class Solution:
    def numTrees(self, n: int) -> int:
        m = {}
        return self.count(1, n, m)
    
    def count(self, lo, hi, m):
        if lo > hi:
            return 1

        res = 0
        for i in range(lo, hi+1):
            if (lo, i-1) not in m:
                m[(lo, i-1)] = self.count(lo, i-1, m)
            if (i+1, hi) not in m:
                m[(i+1, hi)] = self.count(i+1, hi, m)
            res += m[(lo, i-1)] * m[(i+1, hi)]
        return res
# @lc code=end