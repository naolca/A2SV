class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:

        satisfaction.sort()

        @cache
        def dp(i, time):
            if i == len(satisfaction):
                return 0
            pick = dp(i + 1, time + 1) + satisfaction[i] * time
            dont = dp(i + 1, time)
            return max(pick, dont)
        return dp(0, 1)

