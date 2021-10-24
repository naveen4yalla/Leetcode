from collections import defaultdict
import heapq
class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    # The union function with union by rank
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1


class Solution:
    def smallestStringWithSwaps(self, s, pairs):
        uf = UnionFind(len(s))
        for i in range(len(pairs)):
            x, y = pairs[i]
            uf.union(x, y)
            
        groups = defaultdict(list)
        for i in range(len(s)):
            uf.root[i] = uf.find(i)
            heapq.heappush(groups[uf.root[i]], s[i])
            print(groups,"ddd")
        print(groups)
        res = []
        for i in range(len(s)):
            res.append(heapq.heappop(groups[uf.root[i]]))
        return ('').join(res)
S=Solution()
S.smallestStringWithSwaps("dcab",[[0,3],[1,2]])