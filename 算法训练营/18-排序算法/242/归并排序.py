#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start
def merge_sort(s: str):
    if len(s) <= 1:
        return s
    
    mid = len(s) // 2
    left = merge_sort(s[:mid])
    right = merge_sort(s[mid:])
    return merge(left, right)

def merge(left, right):
    l, r = 0, 0
    s = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            s.append(left[l])
            l += 1
        else:
            s.append(right[r])
            r += 1
    s.extend(left[l:])
    s.extend(right[r:])
    return "".join(s)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return merge_sort(s) == merge_sort(t)
# @lc code=end