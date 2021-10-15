
class Solution:
    def findCircle(self,isConnected):
        def dfs(f):
            self.isVisited[f]=True
            for i in range(self.n):
                if isConnected[f][i]==1 and not self.isVisited[i]:
                    dfs(i)

        self.n=len(isConnected)
        count=0
        self.isVisited=[False]*self.n
        for f in range(self.n):
            if not self.isVisited[f]:
                count=count+1
                dfs(f)
        return count


S=Solution()
print(S.findCircle([[1,1,0,0],[1,2,0,1],[0,0,1,0],[0,1,0,1]]))
#Space complexity is O(n)  
#Time complexity is O(n²) 


#Union-find Algorithm
class UnionFind:
    def __init__(self,n):
        self.rank=[1]*n
        self.root=[i for i in range(n)]
        self.count=n
    def find(self,a):
        if a == self.root[a]:
            return a
        self.root[a] = self.find(self.root[a])
        return self.root[a]

    def unionFind(self,a,b):
        xa=self.find(a)
        xb=self.find(b)
        if xa!=xb:
            if self.rank[xa]>self.rank[xb]:
                self.root[xb]=xa
            elif self.rank[xa]<self.rank[xb]:
                self.root[xa]=xb
            else:
                self.root[xb]=xa
                self.rank[xa]=self.rank[xa]+1
        self.count=self.count-1
 
    def province(self):
        return self.count

class Solution1:
    def findCircle(self,isConnected):
        n=len(isConnected)
        u=UnionFind(n)
        for f in range(n):
            for i in range(f+1,n):
                if isConnected[f][i]==1:
                    u.unionFind(f,i)
        u.province()



#Space complexity is O(n)
#Time complexity is O(n²)


