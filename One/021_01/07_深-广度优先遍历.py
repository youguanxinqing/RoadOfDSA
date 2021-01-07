#
# @lc app=leetcode.cn id=547 lang=python3
#
# [547] 省份数量
#

# @lc code=start
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        black = set()
        prov_count = 0
        n = len(isConnected)
        
        for i in range(0, n):
            if i in black:
                continue
                
            q = [i]
            while len(q) != 0:
                point = q.pop()
                if point in black:
                    continue
                black.add(point)
                for j in range(0, n):
                    if isConnected[point][j] == 1:
                        q.append(j)
            prov_count += 1
        
        return prov_count

# @lc code=end