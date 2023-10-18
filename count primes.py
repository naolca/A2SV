class Solution:
    def countPrimes(self, n: int) -> int:


        if n < 2:
            return 0

        lst = [True for i in range(n)]

        lst[0] = False
        lst[1] = False

        for i in range(2, len(lst)):
            if lst[i]:
                j = i + i
                while j < len(lst):
                    lst[j] = False
                    j += i
        return lst.count(True)
       
                    

