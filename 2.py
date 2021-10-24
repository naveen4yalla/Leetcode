from collections import defaultdict
class Solution:
    def smallestStringWithSwaps(self, s, pairs):
        
        
        
        graph = defaultdict(set)
 
        def addEdges(u,v):
            graph[u].add(v)
            graph[v].add(u)
            
        for i in pairs:
            u =  i[0]
            v =  i[1]
            addEdges(u,v)
            
        
        visited = [False]*len(s)
        stack = []
        res = []
        def dfs(node):
            
            if(visited[node] == False):
                visited[node] = True
            else:
                return
            
            for neig in graph[node]:
                dfs(neig)
            
            stack.append(node)
            
            
        for i in range(len(visited)):
            if(visited[i] == False):
                dfs(i)
                res.append(stack[::])
                stack.clear()
        
        
        string  = [' ']*len(s)
        print(res)
        print(string)
        for lst in res:
            sort_ = []
            for i in lst:
                sort_.append(s[i])
            print(sort_,lst)    
            sort_.sort()
            lst.sort()
            print(sort_,lst) 
            print
            for t in range(0,len(lst)):
                string[lst[t]] = sort_[t]
                
                
        return ''.join(string)
S=Solution()
S.smallestStringWithSwaps("bcad",[[0,3],[1,2]])