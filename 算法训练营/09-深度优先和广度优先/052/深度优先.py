#
# @lc app=leetcode.cn id=52 lang=python3
#
# [52] N皇后 II
#

# @lc code=start
class Solution:
    def __init__(self) -> None:
        self.result = []
        self.cols, self.pie, self.na = set(), set(), set()
    
    def totalNQueens(self, n: int) -> int:
        if n < 1:
            return 0
        
        self.dfs(n, 0, [])
        return len(self.result)
    
    def dfs(self, n, row, cur_state):
        if row >= n:
            self.result.append(cur_state)
            return
        
        for col in range(n):
            if col in self.cols or row + col in self.pie or row - col in self.na:
                continue
            
            self.cols.add(col)
            self.pie.add(row + col)
            self.na.add(row - col)

            self.dfs(n, row+1, cur_state+[col])

            self.cols.remove(col)
            self.pie.remove(row + col)
            self.na.remove(row - col)

# @lc code=end