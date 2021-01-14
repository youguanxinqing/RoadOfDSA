#
# @lc app=leetcode.cn id=1018 lang=python3
#
# [1018] 可被 5 整除的二进制前缀
#

# @lc code=start
class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        def inner(n: int, A: List[int]):
            for i in A:
                n |= i
                yield n % 5 == 0
                n <<= 1
        return list(inner(0, A))

# @lc code=end
