#
# @lc app=leetcode.cn id=509 lang=python3
#
# [509] 斐波那契数
#

# @lc code=start
class Solution:
    
    cache = {}
    
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1

        n1 = self.cache.get(n-1)
        if n1 is None:
            n1 = self.fib(n-1)
            self.cache[n-1] = n1
        
        n2 = self.cache.get(n-2)
        if n2 is None:
            n2 = self.fib(n-2)
            self.cache[n-2] = n2
        
        return n1 + n2
# @lc code=end