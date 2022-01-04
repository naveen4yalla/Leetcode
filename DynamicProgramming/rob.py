class Solution:
    def rob(self,arr):
        dp=[0]*len(arr)
        dp[0]=arr[0]
        dp[1]=max(arr[0],arr[1])
        for f in range(2,len(arr)):
            dp[f]=max(dp[f-1],dp[f-2]+arr[f])
        return dp[-1]
s=Solution()
print(s.rob([1,2,3,1]))
#time complexity o(n)
#space complexity o(n)


