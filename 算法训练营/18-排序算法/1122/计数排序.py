#
# @lc app=leetcode.cn id=1122 lang=python3
#
# [1122] 数组的相对排序
#

# @lc code=start
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr2Set = set(arr2)

        counter = {}
        unexpected_list = []
        for item in arr1:
            if item not in arr2Set:
                unexpected_list.append(item)
            else:
                if item not in counter:
                    counter[item] = 1
                else:
                    counter[item] += 1
        
        ret = []
        for item in arr2:
            ret.extend((item for _ in range(counter[item])))
        ret.extend(sorted(unexpected_list))
        return ret
# @lc code=end