class Solution:
    def fib(self, n: int) -> int:
        if n==0:
            return 0
        else:
            the_list=[]
            the_list.append(0)
            the_list.append(1)
            for i in range(2,n):
                the_list.append(the_list[i-1]+the_list[i-2])

        return the_list[-1]+the_list[-2]