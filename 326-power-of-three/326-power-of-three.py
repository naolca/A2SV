class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<=0:
            return False
        if n==1:
            return True
        num=1
        three=3
        while three<n:
            three=3**num
            num+=1
        if three==n:
            return True
        else:
            return False
        