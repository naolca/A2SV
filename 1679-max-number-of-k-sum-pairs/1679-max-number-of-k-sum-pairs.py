class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        tempo = sorted(nums)
        start,end = 0, len(nums)-1
        count = 0
        while(start<end):
            sum = tempo[start]+tempo[end]
            if sum==k:
                start+=1
                end-=1
                count+=1
            elif sum<k:
                start+=1
            else:
                end-=1
        return count
                    