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
s=Solution()
print(s.longestCommonSubsequence("abc","fgabfghc"))
