#
# @lc app=leetcode.cn id=63 lang=python3
#
# [63] 不同路径 II
#

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        map = [[0]*n for _ in range(m)]
        for i in range(n):
            if obstacleGrid[0][i] == 1:
                break
            map[0][i] = 1
        
        for i in range(m):
            if obstacleGrid[i][0] == 1:
                break
            map[i][0] = 1
        
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    map[i][j] = 0
                else:
                    map[i][j] = map[i-1][j] + map[i][j-1]
        return map[m-1][n-1]
# @lc code=end