class MinStack:

    def __init__(self):
        self.s=[]

        

    def push(self, val: int) -> None:
        if(not self.s):
            self.s.append((val,val))
        else:
            self.s.append((val,min(val,self.s[-1][1])))

        





    def pop(self) -> None:
        if(self.s):
            self.s.pop()
        
        

    def top(self) -> int:
        if(self.s):
            return self.s[-1][0]
        
        

    def getMin(self) -> int:
      return self.s[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()