class MyQueue:

    def __init__(self):
        self.s1=[]
        self.s2=[]
        

    def push(self, x: int) -> None:
        self.s1.append(x)
        
        

    def pop(self) -> int:

        while(self.s1):
            self.s2.append(self.s1.pop())

        top=self.s2.pop()
        while(self.s2):
            self.s1.append(self.s2.pop())

        return top
        

    def peek(self) -> int:
        while(self.s1):
            self.s2.append(self.s1.pop())

        top=self.s2.pop()
        self.s2.append(top)
        while(self.s2):
            self.s1.append(self.s2.pop())


        return top        

        

    def empty(self) -> bool:
        if(self.s1):
            return False
        return True
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()