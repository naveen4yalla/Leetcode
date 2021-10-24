from collections import defaultdict
class Solution:
    def validPath(self, n, edges, start, end):
        graph=defaultdict(list)
        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)
        print(graph)
        queue=[]
        queue.append(start)
        visited=[False]*n
        visited[start]=True
        while queue:
            temp=queue.pop(0)
            if temp==end:
                return True
            for f in graph[temp]:
                if  f not in visited:
                         queue.append(f)
                         visited[f]=True
        return False
S=Solution()
print(S.validPath(1,[],0,0))


