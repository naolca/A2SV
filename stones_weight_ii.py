class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
     
        
        @cache
        def dp(i, summ):
            # print(i, summ)
            if i == len(stones):
                if summ < 0:
                    return inf
                return summ
            
            return min(dp(i + 1, summ - stones[i]), dp(i + 1, summ + stones[i]))
        return dp(0, 0)
