#
# @lc app=leetcode.cn id=605 lang=python3
#
# [605] 种花问题
#

# @lc code=start
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed) == 1:
            return (1 if flowerbed[0]==0 else 0) >= n
        
        can_place_num = 0
        cur = 0
        max_index = len(flowerbed) - 1
        while cur <= max_index:
            if (cur+1 > max_index and not flowerbed[cur]) or (not flowerbed[cur] and not flowerbed[cur+1]):
                can_place_num += 1
                flowerbed[cur] = 1
            
            if flowerbed[cur]:
                cur += 2
            elif flowerbed[cur+1]:
                cur += 3
        
        return can_place_num >= n
                

# @lc code=end