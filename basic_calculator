class Solution:
    def calculate(self, s: str) -> int:
            stack=[]        
            tempo=0#this holds the intermidate value to be used in the evaluation depending on the symbol encountered.
            sign='+'#this is used because it won't affect the value of the number in consideration
            for i in range(len(s)):
                if s[i].isdigit():
                    tempo=tempo*10+int(s[i])
                if s[i] in '+-*/' or i==len(s)-1:
                    if sign=='+':
                        stack.append(tempo)
                    if sign=='-':
                        stack.append(-tempo)
                    if sign=='*':
                        new_tempo=stack.pop()*tempo
                        stack.append(new_tempo)
                    if sign=='/':
                        a=stack.pop()
                        if a>=0:
                            new_tempo=a//tempo
                        else:
                            new_tempo=-((-a)//tempo)
                        stack.append(new_tempo)
                    sign=s[i]
                    tempo=0
                    
            return sum(stack)#finally we return the sum of the values of the stack we used.
            
