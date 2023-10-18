class MinStack:

    def __init__(self):
        self.stack=[]
        self.tempoStack=[]
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if(len(self.tempoStack)==0):
            self.tempoStack.append(val)
        else:
            if(self.tempoStack[-1]>=val):
                self.tempoStack.append(val)

        

    def pop(self) -> None:
        if(self.stack[-1]==self.tempoStack[-1]):
            del self.tempoStack[-1]
        del self.stack[-1]

        
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.tempoStack[-1]

        
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
