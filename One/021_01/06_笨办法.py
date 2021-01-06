#
# @lc app=leetcode.cn id=399 lang=python3
#
# [399] 除法求值
#

# @lc code=start
class Solution:
    @staticmethod
    def make_query_dict(equations: List[List[str]], values: List[float]) -> dict:
        """
            构建查询路径

            input: equations=[["a","b"],["b","c"]], values=[2.0,3.0]

            root = {
                'a': {'b': 2.0}, 
                'b': {'a': 0.5, 'c': 3.0}, 
                'c': {'b': 0.3333333333333333}
            }
        """
        root = {}
        for idx, (x, y) in enumerate(equations):
            # x -> y -> score
            target = root.get(x)
            if target is None:
                root[x] = {}
                target = root[x]
            target[y] = values[idx]

            # y -> x -> score
            target = root.get(y)
            if target is None:
                root[y] = {}
                target = root[y]
            target[x] = 1 / values[idx]
        return root
    
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        results = []
        
        d = self.make_query_dict(equations, values)  # 构建查询字典
        nodes = set(d.keys())  # 获取所有节点
        for (x, y) in queries:
            # 不能组成路径
            if x not in nodes or y not in nodes:
                results.append(-1.0)
                continue
            # 原地
            if x == y:
                results.append(1.0)
                continue
                
            score = self.query_score(d, x, y, score=1, pass_set=set())
            if score is None:
                results.append(-1.0)
            else:
                results.append(score)
        
        return results
    
    def query_score(
        self, 
        d: dict, 
        s: int, 
        e: int, 
        score: float = 1.0, 
        pass_set: set = None,
    ) -> Optional[float]:
        """
            深度遍历
            
            pass_set: 路径记录(避免出现环)
        """
        if e in d[s]:
            return d[s][e] * score
               
        pass_set.add(s)  # 路过
        
        for next, part_score in d[s].items():

            if next in pass_set:
                continue
            
            result_score = self.query_score(d, next, e, score*part_score, pass_set)
            if result_score is not None:
                return result_score

# @lc code=end