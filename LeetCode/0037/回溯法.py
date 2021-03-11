#
# @lc app=leetcode.cn id=37 lang=python3
#
# [37] 解数独
#

# @lc code=start
class Solution:

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.pos = -1
        self.board = board
        self.backtrack()
    
    def next_pos(self):
        self.pos += 1
        if self.pos >= 81:
            return None
        return self.pos // 9, self.pos % 9
    
    def backtrack(self):
        pos = self.next_pos()
        if not pos:
            return True
        
        x, y = pos
        if self.board[x][y] != ".":
            return self.backtrack()
        
        for i in range(1, 10):
            i = str(i)
            if i in self.collect_cur_row(x, y):
                continue
            if i in self.collect_cur_col(x, y):
                continue
            if i in self.collect_cur_arround(x, y):
                continue
            
            self.board[x][y] = i
            if not self.backtrack():
                self.board[x][y] = "."
                self.pos = x * 9 + y
            else:
                return True
        return False
   
    def collect_cur_row(self, i, _) -> list:
        return self.board[i]
    
    def collect_cur_col(self, _, j) -> list:
        return [self.board[i][j] for i in range(9)]
    
    def collect_cur_arround(self, i, j) -> list:
        x, y = i - i%3, j - j%3
        return [self.board[x+ii][y+jj] for ii in range(3) for jj in range(3)]
# @lc code=end