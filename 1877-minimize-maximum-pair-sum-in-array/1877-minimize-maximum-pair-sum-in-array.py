class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        answer=0
        pointer=len(nums)-1
        for i in range(len(nums)//2):
            answer=max(answer,nums[i]+nums[pointer])
            pointer-=1
        return answer
        