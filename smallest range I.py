class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:


        nums.sort()
        if len(nums) == 1:
            return 0

        best =  (nums[-1] - k )-( nums[0] + k)
        return best if best > 0 else 0
        
