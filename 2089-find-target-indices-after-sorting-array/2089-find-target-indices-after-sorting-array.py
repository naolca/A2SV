class Solution:
    def targetIndices(self, nums, target):
        nums=sorted(nums)
        list_2b_returned=[]
        for index,number in enumerate(nums):
            if number==target:
                list_2b_returned.append(index)
        return list_2b_returned
                
            