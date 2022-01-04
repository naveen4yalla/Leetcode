from functools import lru_cache
class Solution:
    def maximumScore(self, nums, multipliers):
        m=len(multipliers)
        n=len(nums)
        @lru_cache(2000)
        def solve(left,i,right):
            if i>=m:
                return 0
            mul=multipliers[i]
            return max(mul*nums[left]+solve(left+1,i+1,right),mul*nums[right]+solve(left,i+1,right-1))
        return solve(0,0,n-1)
s=Solution()
s.maximumScore([-5,-3,-3,-2,7,1],[-10,-5,3,4,6])

#Time complexity is o(m)
#space complexity is o(m)