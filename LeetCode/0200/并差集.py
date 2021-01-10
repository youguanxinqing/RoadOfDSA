#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#

# @lc code=start

class UnionFind(object):
    def __init__(self, grid) -> None:
        n, m = len(grid), len(grid[0])

        self.parents = list(range(m * n))
        self.ranks = [0 for _ in range(m * n)]
        
        self.count = len(
            list(
                filter(
                    lambda item: (lambda i, j: grid[i][j] == "1")(*item), 
                    ((i, j) for i in range(n) for j in range(m))
                )
            )
        )
        
    def find(self, i) -> int:
        root = i
        while root != self.parents[root]:
            root = self.parents[root]
        while i != self.parents[i]:
            i, self.parents[i] = self.parents[i], root
        return root
    
    def union(self, i, j):
        pi, pj = self.find(i), self.find(j)
        if pi == pj:
            return
        
        min_rank = pi if self.ranks[pi] < self.ranks[pj] else pj
        max_rank = pi+pj - min_rank
        self.parents[max_rank] = self.parents[min_rank]
        if self.ranks[min_rank] == self.ranks[max_rank]:
            self.ranks[max_rank] += 1
        self.count -= 1

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        uf = UnionFind(grid)
        n, m = len(grid), len(grid[0])
        for (i, j) in ((i, j) for i in range(n) for j in range(m)):
            if grid[i][j] == "0":
                continue
            for (x, y) in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
                if 0<= x < n and 0 <= y < m and grid[x][y] == "1":
                    uf.union(i*m + j, x*m + y)
        return uf.count

# @lc code=end