class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        steps = 0
        previous = nums[0]
        for i in range(1, n):
            if nums[i] <= previous:
                steps = steps + previous +1 - nums[i]
                nums[i] = previous +1          
            previous = nums[i]
        return steps