#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num = 0
        passes = set()
        n, m = len(grid), len(grid[0])
        
        for (i, j) in ((i, j) for i in range(n) for j in range(m)):
            if grid[i][j] == "0" or (i, j) in passes:
                continue
            
            q = [(i, j)]
            while len(q) != 0:
                x, y = q.pop()
                passes.add((x, y))

                for (x, y) in ((x-1, y), (x+1, y), (x, y-1), (x, y+1)):
                    if 0<=x<n and 0<=y<m and grid[x][y] == "1" and (x,y) not in passes:
                        q.append((x,y))
            num += 1
        return num

# @lc code=end
