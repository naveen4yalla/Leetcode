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
print(S.findCircle([[1,0,0],[0,1,0],[0,0,1]]))

