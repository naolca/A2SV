class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        while len(tokens) > 1:
            t = tokens.pop(0)#this is important to reach otherwise the loop wont end.
            if t not in '+-*/': #if the element is a number,it gets appended to the last of the tokens.
                tokens.append(t)
            else:#whereas if the element is a symbol of valuation, then the previous 2 numbers coming before are joined and evaluated.
                num1, num2 = tokens.pop(), tokens.pop()
                tokens.append(str(int(eval(''.join([num2,t,num1])))))
        return int(tokens[0]) #finally when the loop is finalized then we are left with the answer.

        