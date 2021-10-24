from collections import defaultdict
class Solution:
    def validPath(self, n, edges, start, end):
            neighbors = defaultdict(list)
            for n1, n2 in edges:
                neighbors[n1].append(n2)
                neighbors[n2].append(n1)
            print(neighbors)   
            queue=[]
            queue.append(start)
            seen = set([start])
            while queue:
                node = queue.pop(0)            
                if node == end:
                    return True            
                for n in neighbors[node]:
                    if n not in seen:
                        seen.add(n)
                        queue.append(n)
                    
            return False
S=Solution()
print(S.validPath(1,[],0,0))