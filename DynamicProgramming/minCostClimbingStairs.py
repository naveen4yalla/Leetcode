from functools import lru_cache
class Solution:
    def minCostClimbingStairs(self,cost):
        first=second=0
        for i in range(2,len(cost)+1):
            t=first
            first=min(first+cost[i-1],second+cost[i-2])
            second=t
        return first
s=Solution()
s.minCostClimbingStairs([10,15,20])



#Memorization Top-Down
 """ class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @cache
        def minimum_cost(i):
            if i <= 1:
                return 0
            
            down_one = cost[i - 1] + minimum_cost(i - 1)
            down_two = cost[i - 2] + minimum_cost(i - 2)
            return min(down_one, down_two) 

        return minimum_cost(len(cost)) """