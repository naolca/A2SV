class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        goodpairs=0#this stores the number of good pairs in the list
        for index,element in enumerate(nums):
            for new_index , new_element in enumerate(nums[index+1:]):#this is done to exclude elements before the current element.
                if element==new_element:
                    goodpairs+=1
        return goodpairs
