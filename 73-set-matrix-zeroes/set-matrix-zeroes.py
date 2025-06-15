class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        oz=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if(matrix[i][j]==0):
                    oz.append((i,j))

        for i in oz:
            for k in range(len(matrix[0])):
                matrix[i[0]][k]=0

            for c in range(len(matrix)):
                matrix[c][i[1]]=0

        return matrix
    

        
        