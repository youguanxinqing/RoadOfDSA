#
# @lc app=leetcode.cn id=509 lang=python3
#
# [509] 斐波那契数
#

# @lc code=start
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        # f(n=2) = 1, f(n=1) = 1
        fn, fn_1 = 1, 1
        while (n-2):
            fn, fn_1 = fn + fn_1, fn
            n -= 1
        
        return fn
# @lc code=end
