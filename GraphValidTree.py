#Union find 
class Solution:
    def validTree(self, n, edges) -> bool:
        if len(edges)!=n-1:
            return False
        unionFind =UnionFind(n)
        for a,b in edges:
            if not unionFind.union(a,b):
                return False
        return True
class UnionFind:
    def __init__(self,size):
        self.root=[f for f in range(size)]
        self.rank=[1]*size
    def find(self,n):
        if self.root[n]==n:
            return n
        self.root[n]=self.find(self.root[n])
        return self.root[n]
    def union(self,x,y):
        rootx=self.find(x)
        rooty=self.find(y)
        if rootx==rooty:
            return False
        if rootx!=rooty:
            if  self.rank[rootx]>self.rank[rooty]:
                self.root[rooty]=rootx
            elif self.rank[rootx]<self.rank[rooty]:
                 self.root[rootx]=rooty
            else:
                 self.root[rooty]=rootx
                 self.rank[rootx]=self.rank[rootx]+1
        return True


#bfs search
class Solution1:
    def validTree(self,n,list):
        if len(list)!=n-1: return False
        adjancyList=[[] for _ in range(n)]
        for a,b in list:
            adjancyList[a].append(b)
            adjancyList[b].append(a)
        visited=[False]*n
        queue=[]
        queue.append(0)
        visited[0]=True
        parent = -1
        while queue:
            pop=queue.pop(0)
            for i in adjancyList[pop]:
                if i == parent:
                    continue

                if visited[i] == False:
                    visited[i]==True
                    queue.append(i)
                else:
                    return False
                
                parent=pop
        return all(visited)



