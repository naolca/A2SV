class Solution:
    def minSteps(self, n: int) -> int:
        
        
        def recursion(num):
            if num == 1:
                return 0 
            steps = float('inf')
            for i in range(num//2 , 0 , -1):
                if num % i == 0:
                    steps = min(recursion(i) + num// i , steps)
            
            return steps
        
        return recursion(n)