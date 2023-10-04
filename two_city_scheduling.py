class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        @cache
        def dp(i, c):
            if i == n:
                return 0 if c == n // 2 else inf
            ans = min(dp(i + 1, c + 1) + costs[i][0], dp(i + 1, c) + costs[i][1])
            return ans
        return dp(0, 0)
