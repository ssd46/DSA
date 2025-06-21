class Solution:
    def isPalindrome(self, s: str) -> bool:
        f=0
        l=len(s)-1
        while(f<l):
            while(f<l and not self.isAplhaNum(s[f])):
                f+=1
            while(l>f and not self.isAplhaNum(s[l])):
                l-=1
            if(s[f].lower() !=s[l].lower()):
                return False
            l-=1
            f+=1
        return True
        




    def isAplhaNum(self,c):
        return ((ord('A')<=ord(c)<=ord('Z')) or
                (ord('a')<=ord(c)<=ord('z')) or
                (ord('0')<=ord(c)<=ord('9'))
        )
        