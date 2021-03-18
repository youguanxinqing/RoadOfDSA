#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] 不同路径
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        map = [[0]*n for _ in range(m)]
        
        for i in range(n):
            map[0][i] = 1

        for i in range(m):
            map[i][0] = 1
        
        for i in range(1, m):
            for j in range(1, n):
                map[i][j] = map[i-1][j] + map[i][j-1]
        return map[m-1][n-1]

# @lc code=end