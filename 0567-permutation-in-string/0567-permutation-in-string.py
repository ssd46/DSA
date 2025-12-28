class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ls=len(s1)
        s1freq=[0]*26

        for i in range(len(s1)):
            s1freq[ord(s1[i])-ord('a')]+=1

        for i in range(len(s2)- ls + 1):
            s2freq=[0]*26
            for j in range(i,i+ls):
                s2freq[ord(s2[j])-ord('a')]+=1
            if s2freq==s1freq:
                return True
        return False
            



        
       


      
            


        