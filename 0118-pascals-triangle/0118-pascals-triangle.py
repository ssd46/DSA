class Solution:
    def genRow(self,row):
        ans=1
        answer=[]
        answer.append(ans)
        for col in range(1,row):
            ans=ans*(row-col)
            ans=ans//col
            answer.append(ans)
        return answer

    def generate(self, numRows: int) -> List[List[int]]:
        l=[]
        for i in range(1,numRows+1):
            l.append(self.genRow(i))

        return l
        







        