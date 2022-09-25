class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<=0:
            return False
        if n==1:
            return True
        num=1
        four=4
        while three<n:
            four=4**num
            num+=1
        if three==n:
            return True
        else:
            return False
        
