#
# @lc app=leetcode.cn id=605 lang=python3
#
# [605] 种花问题
#

# @lc code=start
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        prev, cur, next = -1, 0, 1
        
        while next <= len(flowerbed) and n != 0:
            place = False
            
            if next == len(flowerbed) and not flowerbed[prev] and not flowerbed[cur]:  # 左边界
                place = True
            elif prev < 0 and not flowerbed[cur] and not flowerbed[next]:  # 右边界
                place = True
            elif not flowerbed[prev] and not flowerbed[cur] and not flowerbed[next]:  # 常态
                place = True
            
            if place:
                flowerbed[cur] = 1
                n -= 1
            
            prev, cur, next = cur, next, next+1
        
        if n == 0:
            return True
        return False
# @lc code=end

