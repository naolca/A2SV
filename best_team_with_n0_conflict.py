class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        

        new = [[ages[i], scores[i]] for i in range(len(scores))]

        new.sort()
        nums = [new[i][1] for i in range(len(new))]
        
        
        @cache
        def dp(i):
            if i == len(nums):
                return 0
            _max = nums[i]
            for idx in range(i + 1, len(nums)):
                if nums[idx] >= nums[i]:
                    _max = max(_max, dp(idx) + nums[i])

            return _max
        _max = 0
        for i in range(len(nums)):
            _max = max(_max, dp(i))
        return _max
