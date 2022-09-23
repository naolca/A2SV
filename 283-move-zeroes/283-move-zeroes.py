class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #this can be solved by treating the array as a linked list.
        current_index=0#this represents the current element
        next_index=1#this is the pointer pointing to the next element.
        while next_index<len(nums):
            if nums[current_index]==0 and nums[next_index]!=0:
                nums[current_index],nums[next_index]=nums[next_index],nums[current_index]
                current_index+=1
                next_index+=1
            elif nums[current_index]==nums[next_index]==0:#in this case we move on to the next og the next of the current element.
                next_index+=1
            else:
                current_index+=1
                next_index+=1