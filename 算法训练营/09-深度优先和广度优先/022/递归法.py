#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        rets = []
        def generate(left, right, s):
            if left == n and right == n:
                rets.append(s)
                return
            
            if left < n:
                generate(left+1, right, s+"(")
            if left > right:
                generate(left, right+1, s+")")
                
        return rets
# @lc code=end