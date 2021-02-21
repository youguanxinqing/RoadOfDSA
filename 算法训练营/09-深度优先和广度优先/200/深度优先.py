#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        total = 0
        m, n = len(grid), len(grid[0])
        
        visited = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "0" or (i, j) in visited:
                    continue
                
                stack = [(i, j)]
                visited.add((i, j))
                while stack:
                    x, y = stack.pop()
                    
                    around = [(x-1, y), (x, y+1), (x+1, y), (x, y-1)]
                    for (x, y) in around:
                        flag = (
                            0 <= x < m 
                            and 0 <= y < n 
                            and grid[x][y] == "1"
                            and (x, y) not in visited
                        )
                        if flag:
                            stack.append((x, y))
                            visited.add((x, y))
                
                total += 1
        return total

# @lc code=end