class Solution:
    def smallerNumbersThanCurrent(self, nums):
        the_list_2b_returned=[0]*len(nums)
        for index,number in enumerate(nums):
            for j in range(len(nums)):
                
                if j==index:
                    continue
                else:
                    if nums[j]<number:
                        the_list_2b_returned[index]+=1
        return the_list_2b_returned