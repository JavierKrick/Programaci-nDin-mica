#LeetCode 50

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1/ self.myPowAux(x,-n)
        else: return self.myPowAux(x,n)


    def myPowAux(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x
        mitad = self.myPowAux(x,n//2)
        res = mitad*mitad
        if (n & 1 == 1):
            res = res * x
        return res
            
