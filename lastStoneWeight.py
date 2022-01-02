import heapq
class Solution:
    def lastStoneWeight(self,stones):
        n=len(stones)
        if n==1:
            return stones[0]
        for f in range(0,n):
            stones[f]=stones[f]*-1
        heapq.heapify(stones)
        while n!=1:
            a=abs(heapq.heappop(stones))
            b=abs(heapq.heappop(stones))
            if a!=b:
                heapq.heappush(stones,-(a-b))
                n=n-1
            else:
                n=n-2
        return abs(stones[0])
s=Solution()
print(s.lastStoneWeight([2,2]))

            


