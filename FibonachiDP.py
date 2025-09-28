## Fibonachi Top Up

class Solution:
    def fib(self, n: int) -> int:
        diccionario = {}
        res = self.fibonachi(n,diccionario)
        return res


    def fibonachi(self,n,diccionario):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        if n in diccionario:
            return diccionario[n]
        nmenos1 = self.fibonachi(n-1, diccionario)
        nmenos2 = self.fibonachi(n-2, diccionario)
        res = nmenos1 + nmenos2
        diccionario[n] = res
        return res



## Fibonachi Bottom Up
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1

        dp = [0] * (n+1)
        dp[0] = 0
        dp[1] = 1
        for i in range (2,n+1):
            dp[i] = dp[i-2]+dp[i-1]
        return dp[n]
