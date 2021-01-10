#
# @lc app=leetcode.cn id=990 lang=python3
#
# [990] 等式方程的可满足性
#

# @lc code=start
class Solution:
    def __init__(self) -> None:
        self.table = {chr(i): chr(i) for i in range(97, 97+26)}

    def find(self, alpha) -> str:
        root = alpha
        while root != self.table[root]:
            root = self.table[root]
        while alpha != self.table[alpha]:
            alpha, self.table[alpha] = self.table[alpha], root
        return root
    
    def union(self, a1, a2):
        r1 = self.find(a1)
        r2 = self.find(a2)
        if r1 != r2:
            self.table[r1] = self.table[r2]
    
    def is_neq(self, a1, a2) -> bool :
        return self.find(a1) != self.find(a2)
    
    def min_max(self, x, y):
        mi = x if x < y else y
        ma = x if x > y else y
        return mi, ma
    
    def equationsPossible(self, equations: List[str]) -> bool:
        for expr in filter(lambda expr: "==" in expr, equations):
            mi, ma = self.min_max(expr[0], expr[-1])
            self.union(mi, ma)
        
        for expr in filter(lambda expr: "!=" in expr, equations):
            mi, ma = self.min_max(expr[0], expr[-1])
            if self.is_neq(mi, ma):
                continue
            return False
        return True
        
# @lc code=end
