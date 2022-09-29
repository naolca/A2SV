class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        dict=Counter(arr)
        times=0
        if len(dict)<=2:
            return 1



        most=0
        for element in sorted(dict.values(),reverse=True):
            if times>=len(arr)//2:
                return most
            times+=element
            most+=1
        
        
        