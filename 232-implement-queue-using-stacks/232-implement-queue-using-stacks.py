class MyQueue:

    def __init__(self):#i will first initialize the two stacks i will use in this implementation
        self.stack1=[]
        self.stack2=[]
        

    def push(self, x: int) -> None:
        self.stack1.append(x)

        

    def pop(self) -> int:
        self.migrate()
        return self.stack2.pop()
        
    def peek(self) -> int:
        self.migrate()
        return self.stack2[-1]
        
    def empty(self) -> bool:
        return (not self.stack1) and (not self.stack2)
    
    def migrate(self) -> None:#this additional function moves the elements of one of the stacks to the other.this helps me to achieve the FIFO nature of queues.
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()