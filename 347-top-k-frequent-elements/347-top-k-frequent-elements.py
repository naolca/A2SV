class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
         my_list = collections.Counter(nums).most_common() 
         return [my_list[i][0] for i in range(k)]#this means return the most k frequent elements
            
            
            
            
        
            
        
            
        