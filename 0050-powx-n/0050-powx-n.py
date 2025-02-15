class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        
        if n < 0:
            return 1 / self.myPow(x, - n)

        half = self.myPow(x, n // 2)

        return half * half if n & 1 == 0 else half * half * x
        

       
        