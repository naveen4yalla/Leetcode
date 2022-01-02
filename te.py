import heapq
class Solution:
    def kWeakestRows(self, mat,k):
        n=len(mat)
        ans=[]
        #ls=dict.fromkeys(range(n))
        ls={}
        temp=0
        for i in range(n):
            for j in range(len(mat[i])):
                if mat[i][j]==1:
                    temp=temp+1
            ls[i]=temp
            temp=0
        for f in range(k):
            best_key = min(ls, key=ls.get)
            ans.append(best_key)
        return ans
s=Solution()
s.kWeakestRows([[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]],3)
