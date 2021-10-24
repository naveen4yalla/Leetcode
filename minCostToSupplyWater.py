from collections import defaultdict
import heapq as h
class Solution:
    def minCostToSupplyWater(self,n,wells,pipes):
        graph=defaultdict(list)

        #Add a virtual node 0 
        for index,cost in enumerate(wells):
            graph[0].append((cost,index+1))
        #Add remaining nodes 
        for x,y,cost in pipes:
            graph[x].append((cost,y))
            graph[y].append((cost,x))
        minimumSpanningTree=set([0])
        h.heapify(graph[0])
        edgesHeap=graph[0]
        totalCost=0
        print(graph)
        print(edgesHeap)
        print("bfgdg")
        while len(minimumSpanningTree)<n+1:
            cost,nextHouse=h.heappop(edgesHeap)
            print(cost,nextHouse,"house")
            if nextHouse not in minimumSpanningTree:
                minimumSpanningTree.add(nextHouse)
                totalCost=totalCost+cost
            for newCost ,neighbourHouse in graph[nextHouse]:
                if neighbourHouse not in minimumSpanningTree:
                    h.heappush(edgesHeap,(newCost,neighbourHouse))
            print(edgesHeap)
    print()
S=Solution()
S.minCostToSupplyWater(3,[1,2,2],[[1,2,1],[2,3,1]])

