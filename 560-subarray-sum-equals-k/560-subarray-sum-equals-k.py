class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        SUM = 0
        count = 0
        DICT = defaultdict(int)
        DICT[0] = 1
        for i in range(len(nums)):
            SUM += nums[i]
            if SUM-k in DICT:
                count += DICT[SUM-k]
            DICT[SUM] += 1
        return count
        