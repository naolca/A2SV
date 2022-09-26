class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        to_be_returned = 1#in a list, a number must have atleast one occurance
        nums.sort()
        j = 0
        to_be_returned = 1
        for i in range(1,len(nums)):
            needed = nums[i] - nums[i-1]
            length = (i - j) * needed
            k -= length
            while k < 0:
                k += nums[i] - nums[j]
                j += 1
            to_be_returned = max(to_be_returned,i-j+1)#every time this loop ends this value id the frequency if we choose to maximize the occurance of the current element
        return to_be_returned