#Top down Recursion 
from functools import lru_cache
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        @lru_cache(maxsize=None)
        def solve(a,b):
            if a==len(text1) or b==len(text2):
                return 0
            if text1[a]==text2[b]:
                return 1+solve(a+1,b+1)
            else:
                return max(solve(a+1,b),solve(a,b+1))
        return solve(0,0)
class Solution:
    def longestCommonSubsequence(self, text1, text2):
        dp_grid = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        for col in reversed(range(len(text2))):
            for row in reversed(range(len(text1))):
               if text2[col] == text1[row]:
                    dp_grid[row][col] = 1 + dp_grid[row + 1][col + 1]
               else:
                    dp_grid[row][col] = max(dp_grid[row + 1][col], dp_grid[row][col + 1])
        
       
        return dp_grid[0][0]
s=Solution()
print(s.longestCommonSubsequence("abc","fgabfghc"))

#space complexity is o(min(m,n))
#time complexity is o(min(m,n))
