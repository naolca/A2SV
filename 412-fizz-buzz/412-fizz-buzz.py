class Solution:
    def fizzBuzz(self, n):
        the_array=[]
        for i in range(1,n+1):
            if i%3==0:
                if i%5==0:
                    the_array.append("FizzBuzz")
                else:
                    the_array.append("Fizz")
            elif i%5==0:
                if i%30==0:
                    the_array.append("FizzBuzz")
                else:
                    the_array.append("Buzz")
            else:
                the_array.append(str(i))
        return the_array
                
            
        