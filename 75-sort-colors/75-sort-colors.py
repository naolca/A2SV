class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=0
        while n<len(nums):
            for i in range(len(nums)-1):
                if nums[i]>nums[i+1]:
                    temp=nums[i]
                    nums[i]=nums[i+1]
                    nums[i+1]=temp
                else:
                    continue
            n+=1