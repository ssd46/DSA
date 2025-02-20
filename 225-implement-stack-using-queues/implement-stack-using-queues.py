class MyStack:

    def __init__(self):
        self.q1=[]
        

    def push(self, x: int) -> None:
        self.q1.append(x)
        element=self.q1.pop()
        self.q1.insert(0,element)
        print(self.q1)
        
        

    def pop(self) -> int:
        return self.q1.pop(0)
        
        

    def top(self) -> int:
        return self.q1[0]       
        

    def empty(self) -> bool:
        if(len(self.q1) ==1 ):
            return False
        else:

            return True       


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()