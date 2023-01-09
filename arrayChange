class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:

        d={}

        for i,number in enumerate(nums):
            d[number]=i
        print(d)
        
        for pair in operations:
            d[pair[1]]=d[pair[0]]
            nums[d[pair[0]]]=pair[1]

            
        return nums
