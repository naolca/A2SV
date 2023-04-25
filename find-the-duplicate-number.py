class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        d=defaultdict(int)

        for number in nums:
            if d[number]>=1:
                return number
            else:
                d[number]+=1