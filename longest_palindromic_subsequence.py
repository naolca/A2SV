class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:



        @cache
        def dp(i1 , i2):

            if i1 > i2:
                return 0
            if i1 == i2:
                return 1
                
            if s[i1] == s[i2]:
                return dp(i1 + 1 , i2 - 1) + 2
            return max(dp(i1 + 1 , i2) , dp(i1  , i2 - 1))
        
        return dp(0, len(s) - 1)
        
        
