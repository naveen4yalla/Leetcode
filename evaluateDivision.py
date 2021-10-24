from collections import defaultdict
from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph=defaultdict(defaultdict)
        for (i,v),x in zip(equations,values):
            graph[i][v]=x
            graph[v][i]=1/x
        print(graph)
S=Solution()
S.calcEquation([["a","b"],["b","c"],["bc","cd"]],[1.5,2.5,5.0],[["a","c"],["c","b"],["bc","cd"],["cd","bc"]])