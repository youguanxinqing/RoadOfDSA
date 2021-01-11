#
# @lc app=leetcode.cn id=1202 lang=python3
#
# [1202] 交换字符串中的元素
#

# @lc code=start
class UnionFind(object):
    def __init__(self, s) -> None:
        self.parents = list(range(len(s)))
        self.ranks = [0 for _ in range(len(s)) ]
    
    def find(self, i) -> int:
        root = i
        while root != self.parents[root]:
            root = self.parents[root]
        while i != self.parents[i]:
            i, self.parents[i] = self.parents[i], root
        return root
    
    def union(self, i, j):
        ri = self.find(i)
        rj = self.find(j)
        if ri != rj:
            mi = ri if self.ranks[ri] < self.ranks[rj] else rj
            ma = ri + rj - mi
            self.parents[ma] = self.parents[mi]
            if self.ranks[ma] == self.ranks[mi]:
                self.ranks[ma] += 1

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        uf = UnionFind(s)
        list(map(lambda item: uf.union(*item), pairs))
        
        classfiy = {}
        for i in range(len(s)):
            r = uf.find(i)
            if r in classfiy:
                classfiy[r].append(i)
            else:
                classfiy[r] = [i]
        
        res = ["" for _ in range(len(s))]
        for _, v in classfiy.items():
            for i, j in zip(sorted(set(v)), sorted(set(v), key=lambda i: s[i])):
                res[i] = s[j]
        return "".join(res)
        
# @lc code=end