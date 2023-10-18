class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        @cache
        def dp(i):
            if i >= len(days):
                return 0

            # choose 1
            idx = bisect_left(days, days[i] + 1)
            one = dp(idx) + costs[0]

            # choose 7
            idx = bisect_left(days, days[i] + 7)
            seven = dp(idx) + costs[1]

            # choose 30
            idx = bisect_left(days, days[i] + 30)
            selasa = dp(idx) + costs[2]
            
            return min(one, seven, selasa)
        return dp(0)



            

        
        
